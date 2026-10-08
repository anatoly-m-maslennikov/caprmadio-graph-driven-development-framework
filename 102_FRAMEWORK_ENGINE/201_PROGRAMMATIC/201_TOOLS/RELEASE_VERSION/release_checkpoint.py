"""Closed, effect-free checkpoint codec for a private Release Action Run.

This module deliberately only encodes and restores already-observed local
state.  It does not write a checkpoint, record a Journal Event, invoke a
Tool, import a provider, or recreate a Docker executor.  A caller which has
durably stored the returned bytes must independently re-admit an executor
before an image phase can be attempted after restoration.
"""

from __future__ import annotations

import base64
import hashlib
import json
import math
from dataclasses import asdict, fields
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, TypeVar

from release_actions import (
    PHASES,
    AdmittedImageExecutor,
    ReleaseActionRun,
    ReleasePhaseResult,
    SelectedReleaseActionContext,
    _fingerprint,
)
from release_compilation import ReleaseCompilationPreflight
from release_contract import (
    CandidateBuildRequest,
    CandidateSnapshotManifest,
    ReleaseContractError,
    SealedAuthority,
    ValidatedCandidate,
    _safe_relative,
    canonical_json,
)
from release_handoff import (
    CompilerEntrypoint,
    SealedCandidateCompilation,
    SealedSourceCopy,
)
from release_e2e_gate import CandidateE2EGateEvidence, HarnessReceipt
from release_image import ImageBuildEvidence, ImageRetirementEvidence, ImageVerificationEvidence
from release_promotion import PromotionEvidence
from release_suite import SuiteGateEvidence
from release_version import ReleaseVersionRequest


RELEASE_ACTION_CHECKPOINT_SCHEMA = "caprmedio.release_version.action_run_checkpoint.v1"
_TAGGED_TYPES = {
    "candidate": ValidatedCandidate,
    "preflight": ReleaseCompilationPreflight,
    "source_copy": SealedSourceCopy,
    "compilation": SealedCandidateCompilation,
    "suite": SuiteGateEvidence,
    "package": dict,
    "build": ImageBuildEvidence,
    "verification": ImageVerificationEvidence,
    "e2e": CandidateE2EGateEvidence,
    "promotion": PromotionEvidence,
    "retirement": ImageRetirementEvidence,
}
_STATE_NAMES = (
    "candidate", "preflight", "source_copy", "compilation", "suite", "package", "build",
    "verification", "e2e", "full_gate", "promotion", "retirement",
)
_PHASE_STATE = {
    "freeze": "candidate",
    "validate": "candidate",
    "deliver_sources": "source_copy",
    "compile": "compilation",
    "closed_unit_gate": "suite",
    "stage_candidate": "package",
    "candidate_image_build": "build",
    "candidate_image_canary": "verification",
    "host_candidate_e2e": "e2e",
    "aggregate_full_gate": "full_gate",
    "promote": "promotion",
    "retire": "retirement",
}
_SHA256_HEX = frozenset("0123456789abcdef")
_PENDING_EVENT_OUTCOMES = frozenset({"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"})
_T = TypeVar("_T")


def _full_gate_type() -> type[Any]:
    """Resolve the independently owned aggregate model only when needed.

    Earlier Release phases do not need the aggregate implementation.  The
    codec nevertheless refuses any full-gate state unless its producer's
    concrete model is present and exact.
    """

    from release_full_gate import FullGateEvidence

    return FullGateEvidence


def _tagged_type(name: str) -> type[Any]:
    if name == "full_gate":
        return _full_gate_type()
    return _TAGGED_TYPES[name]


def _error(code: str, message: str) -> ReleaseContractError:
    return ReleaseContractError(code, message)


def release_action_checkpoint_sha256(checkpoint: Mapping[str, Any]) -> str:
    """Digest one checkpoint with its self-excluding digest blanked.

    The caller receives only a pure digest calculation.  It does not create a
    carrier, change a Run, or establish any Journal record.
    """

    value = dict(checkpoint)
    value["sha256"] = "0" * 64
    return hashlib.sha256(canonical_json(value)).hexdigest()


def _mapping(value: Any, required: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != required:
        raise _error("release-checkpoint-invalid", f"{label} has unknown, missing, or non-object members")
    return value


def _text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip() or "\n" in value or "\r" in value:
        raise _error("release-checkpoint-invalid", f"{label} must be one bounded non-empty string")
    return value


def _sha256(value: Any, label: str) -> str:
    value = _text(value, label)
    if len(value) != 64 or any(character not in _SHA256_HEX for character in value):
        raise _error("release-checkpoint-invalid", f"{label} must be one lowercase SHA-256 digest")
    return value


def _index(value: Any, label: str) -> int:
    if type(value) is not int or value < 0 or value >= len(PHASES):
        raise _error("release-checkpoint-invalid", f"{label} is outside the selected phase graph")
    return value


def _safe_path(value: Any, label: str) -> str:
    try:
        return _safe_relative(_text(value, label), label)
    except ValueError as error:
        raise _error("release-checkpoint-invalid", f"{label} is not a safe Project-relative path") from error


def _json_value(value: Any, label: str) -> Any:
    """Reject executable and non-canonical values before JSON serialization."""

    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float:
        if not math.isfinite(value):
            raise _error("release-checkpoint-invalid", f"{label} contains a non-finite number")
        return value
    if isinstance(value, bytes):
        return {"encoding": "base64", "data": base64.b64encode(value).decode("ascii")}
    if isinstance(value, (list, tuple)):
        return [_json_value(item, label) for item in value]
    if isinstance(value, dict):
        if any(not isinstance(key, str) for key in value):
            raise _error("release-checkpoint-invalid", f"{label} has a non-string object key")
        return {key: _json_value(item, label) for key, item in value.items()}
    raise _error("release-checkpoint-invalid", f"{label} contains an unsupported executable or object value")


def _bytes(value: Any, label: str) -> bytes:
    encoded = _mapping(value, {"encoding", "data"}, label)
    if encoded["encoding"] != "base64" or not isinstance(encoded["data"], str):
        raise _error("release-checkpoint-invalid", f"{label} is not a closed base64 byte value")
    try:
        decoded = base64.b64decode(encoded["data"], validate=True)
    except (ValueError, TypeError) as error:
        raise _error("release-checkpoint-invalid", f"{label} has invalid base64 bytes") from error
    if base64.b64encode(decoded).decode("ascii") != encoded["data"]:
        raise _error("release-checkpoint-invalid", f"{label} base64 is not canonical")
    return decoded


def _dump_model(value: Any, cls: type[Any], label: str) -> dict[str, Any]:
    if type(value) is not cls:
        raise _error("release-checkpoint-invalid", f"{label} is not the expected typed value")
    return _json_value(value.model_dump(mode="json", by_alias=True), label)


def _load_model(value: Any, cls: type[_T], label: str) -> _T:
    if not isinstance(value, dict):
        raise _error("release-checkpoint-invalid", f"{label} must be an object")
    try:
        return cls.model_validate(value)
    except (TypeError, ValueError) as error:
        raise _error("release-checkpoint-invalid", f"{label} violates its closed typed contract") from error


def _dump_dataclass(value: Any, cls: type[Any], label: str) -> dict[str, Any]:
    if type(value) is not cls:
        raise _error("release-checkpoint-invalid", f"{label} is not the expected typed value")
    return _json_value(asdict(value), label)


def _load_dataclass(value: Any, cls: type[_T], label: str, *, tuple_fields: frozenset[str] = frozenset()) -> _T:
    required = {item.name for item in fields(cls)}
    payload = _mapping(value, required, label)
    restored = dict(payload)
    for field_name in tuple_fields:
        source = restored.get(field_name)
        if not isinstance(source, list) or any(not isinstance(item, str) for item in source):
            raise _error("release-checkpoint-invalid", f"{label}.{field_name} must be a string list")
        restored[field_name] = tuple(source)
    try:
        return cls(**restored)
    except (TypeError, ValueError) as error:
        raise _error("release-checkpoint-invalid", f"{label} cannot construct its typed state") from error


def _candidate_value(candidate: ValidatedCandidate) -> dict[str, Any]:
    if type(candidate) is not ValidatedCandidate:
        raise _error("release-checkpoint-invalid", "candidate is not locally validated typed state")
    return {
        "project_root": candidate.project_root,
        "manifest": _dump_model(candidate.manifest, CandidateSnapshotManifest, "candidate.manifest"),
        "authority": _dump_model(candidate.authority, SealedAuthority, "candidate.authority"),
        "intent": _dump_model(candidate.intent, CandidateBuildRequest, "candidate.intent"),
    }


def _load_candidate(value: Any, root: str) -> ValidatedCandidate:
    payload = _mapping(value, {"project_root", "manifest", "authority", "intent"}, "candidate")
    if payload["project_root"] != root:
        raise _error("release-checkpoint-binding-mismatch", "candidate root differs from the checkpoint root")
    manifest = _load_model(payload["manifest"], CandidateSnapshotManifest, "candidate.manifest")
    authority = _load_model(payload["authority"], SealedAuthority, "candidate.authority")
    intent = _load_model(payload["intent"], CandidateBuildRequest, "candidate.intent")
    if (
        authority.executing_release != manifest.executing_release
        or authority.candidate_release != manifest.candidate_release
        or authority.canonical_source_snapshot_digest != manifest.canonical_source_snapshot_digest
        or authority.project_structure_digest != manifest.project_structure_digest
        or authority.framework_settings_digest != manifest.framework_settings_digest
        or authority.source_frontier_digest != manifest.source_frontier_digest
        or authority.nested_source_recursive_sha256_before != manifest.nested_source_recursive_sha256_before
        or authority.expected_candidate_snapshot_manifest_sha256 != manifest.sha256
        or intent.candidate_release != manifest.candidate_release
        or intent.expected_derived_source_copy_sha256 != manifest.expected_derived_source_copy_sha256
        or intent.expected_compiled_output_sha256 != manifest.expected_compiled_output_sha256
        or intent.full_suite_environment != manifest.full_suite_environment
        or intent.candidate_image_reference != manifest.candidate_image.candidate_image_reference
    ):
        raise _error("release-checkpoint-binding-mismatch", "candidate authority or intent is not exactly manifest-bound")
    return ValidatedCandidate(root, manifest, authority, intent)


def _preflight_value(value: ReleaseCompilationPreflight) -> dict[str, Any]:
    if type(value) is not ReleaseCompilationPreflight:
        raise _error("release-checkpoint-invalid", "preflight is not typed state")
    if any(not isinstance(path, str) or not isinstance(contents, bytes) for path, contents in value.output_files.items()):
        raise _error("release-checkpoint-invalid", "preflight output files are not typed bytes")
    return {
        "candidate_release": value.candidate_release,
        "expected_derived_source_copy_sha256": value.expected_derived_source_copy_sha256,
        "expected_compiled_output_sha256": value.expected_compiled_output_sha256,
        "compiler_entrypoint": _dump_model(value.compiler_entrypoint, CompilerEntrypoint, "preflight.compiler_entrypoint"),
        "canonical_source_snapshot_digest": value.canonical_source_snapshot_digest,
        "compiler_frontier_digest": value.compiler_frontier_digest,
        "nested_source_recursive_sha256_before": value.nested_source_recursive_sha256_before,
        "output_files": [
            {"path": _safe_path(path, "preflight.output_files.path"), "bytes": _json_value(contents, "preflight.output_files.bytes")}
            for path, contents in sorted(value.output_files.items())
        ],
        "child_manifest_bytes": _json_value(value.child_manifest_bytes, "preflight.child_manifest_bytes"),
    }


def _load_preflight(value: Any, candidate: ValidatedCandidate) -> ReleaseCompilationPreflight:
    payload = _mapping(value, {
        "candidate_release", "expected_derived_source_copy_sha256", "expected_compiled_output_sha256",
        "compiler_entrypoint", "canonical_source_snapshot_digest", "compiler_frontier_digest",
        "nested_source_recursive_sha256_before", "output_files", "child_manifest_bytes",
    }, "preflight")
    if not isinstance(payload["output_files"], list):
        raise _error("release-checkpoint-invalid", "preflight.output_files must be a list")
    output_files: dict[str, bytes] = {}
    previous = None
    for item in payload["output_files"]:
        entry = _mapping(item, {"path", "bytes"}, "preflight.output_file")
        path = _safe_path(entry["path"], "preflight.output_file.path")
        if previous is not None and path <= previous:
            raise _error("release-checkpoint-invalid", "preflight output files are not uniquely canonical ordered")
        previous = path
        output_files[path] = _bytes(entry["bytes"], "preflight.output_file.bytes")
    try:
        preflight = ReleaseCompilationPreflight(
            candidate_release=_text(payload["candidate_release"], "preflight.candidate_release"),
            expected_derived_source_copy_sha256=_sha256(payload["expected_derived_source_copy_sha256"], "preflight.expected_derived_source_copy_sha256"),
            expected_compiled_output_sha256=_sha256(payload["expected_compiled_output_sha256"], "preflight.expected_compiled_output_sha256"),
            compiler_entrypoint=_load_model(payload["compiler_entrypoint"], CompilerEntrypoint, "preflight.compiler_entrypoint"),
            canonical_source_snapshot_digest=_sha256(payload["canonical_source_snapshot_digest"], "preflight.canonical_source_snapshot_digest"),
            compiler_frontier_digest=_sha256(payload["compiler_frontier_digest"], "preflight.compiler_frontier_digest"),
            nested_source_recursive_sha256_before=_sha256(payload["nested_source_recursive_sha256_before"], "preflight.nested_source_recursive_sha256_before"),
            output_files=output_files,
            child_manifest_bytes=_bytes(payload["child_manifest_bytes"], "preflight.child_manifest_bytes"),
        )
    except (TypeError, ValueError) as error:
        raise _error("release-checkpoint-invalid", "preflight cannot construct typed state") from error
    manifest = candidate.manifest
    if (
        preflight.candidate_release != manifest.candidate_release
        or preflight.expected_derived_source_copy_sha256 != manifest.expected_derived_source_copy_sha256
        or preflight.expected_compiled_output_sha256 != manifest.expected_compiled_output_sha256
        or preflight.canonical_source_snapshot_digest != manifest.canonical_source_snapshot_digest
        or preflight.compiler_frontier_digest != candidate.authority.source_frontier_digest
        or preflight.nested_source_recursive_sha256_before != manifest.nested_source_recursive_sha256_before
    ):
        raise _error("release-checkpoint-binding-mismatch", "preflight is not exactly candidate-bound")
    return preflight


def _tag(name: str, value: Any) -> dict[str, Any]:
    if name not in _STATE_NAMES:
        raise _error("release-checkpoint-invalid", "checkpoint has an unknown state tag")
    if name == "candidate":
        payload = _candidate_value(value)
    elif name == "preflight":
        payload = _preflight_value(value)
    elif name == "source_copy":
        if type(value) is not SealedSourceCopy:
            raise _error("release-checkpoint-invalid", "source_copy is not typed state")
        payload = {
            "candidate": _candidate_value(value.candidate),
            "source_copy_root": _safe_path(value.source_copy_root, "source_copy.source_copy_root"),
            "actual_derived_source_copy_sha256": _sha256(value.actual_derived_source_copy_sha256, "source_copy.actual_derived_source_copy_sha256"),
        }
    elif name in {"compilation"}:
        payload = _dump_model(value, SealedCandidateCompilation, name)
    elif name == "package":
        payload = _package_value(value)
    else:
        payload = _dump_dataclass(value, _tagged_type(name), name)
    return {"tag": name, "value": payload}


def _package_value(value: Any) -> dict[str, Any]:
    if type(value) is not dict:
        raise _error("release-checkpoint-invalid", "package is not a typed package result")
    required = {"staged", "verified", "candidate_snapshot_manifest_sha256", "release_root", "file_count"}
    payload = _mapping(value, required, "package")
    if type(payload["staged"]) is not bool or payload["verified"] is not True or type(payload["file_count"]) is not int or payload["file_count"] < 0:
        raise _error("release-checkpoint-invalid", "package result has invalid closed values")
    return {
        "staged": payload["staged"],
        "verified": True,
        "candidate_snapshot_manifest_sha256": _sha256(payload["candidate_snapshot_manifest_sha256"], "package.candidate_snapshot_manifest_sha256"),
        "release_root": _safe_path(payload["release_root"], "package.release_root"),
        "file_count": payload["file_count"],
    }


def _load_e2e(value: Any) -> CandidateE2EGateEvidence:
    """Restore nested host-E2E receipts as their closed dataclass types."""

    required = {item.name for item in fields(CandidateE2EGateEvidence)}
    payload = _mapping(value, required, "e2e")
    rows = payload["harness_receipts"]
    if not isinstance(rows, list):
        raise _error("release-checkpoint-invalid", "e2e.harness_receipts must be a list")
    restored_rows = tuple(
        _load_dataclass(row, HarnessReceipt, "e2e.harness_receipt", tuple_fields=frozenset({"argv"}))
        for row in rows
    )
    restored = dict(payload)
    restored["harness_receipts"] = restored_rows
    try:
        return CandidateE2EGateEvidence(**restored)
    except (TypeError, ValueError) as error:
        raise _error("release-checkpoint-invalid", "e2e cannot construct typed state") from error


def _load_tag(value: Any, candidate: ValidatedCandidate | None, root: str) -> tuple[str, Any]:
    tagged = _mapping(value, {"tag", "value"}, "tagged state")
    name = _text(tagged["tag"], "tagged state.tag")
    if name not in _STATE_NAMES:
        raise _error("release-checkpoint-invalid", "checkpoint names an unsupported typed state")
    if name == "candidate":
        return name, _load_candidate(tagged["value"], root)
    if candidate is None:
        raise _error("release-checkpoint-binding-mismatch", f"{name} appears before its sealed candidate")
    if name == "preflight":
        return name, _load_preflight(tagged["value"], candidate)
    if name == "source_copy":
        payload = _mapping(tagged["value"], {"candidate", "source_copy_root", "actual_derived_source_copy_sha256"}, "source_copy")
        restored_candidate = _load_candidate(payload["candidate"], root)
        source_copy = SealedSourceCopy(
            restored_candidate,
            _safe_path(payload["source_copy_root"], "source_copy.source_copy_root"),
            _sha256(payload["actual_derived_source_copy_sha256"], "source_copy.actual_derived_source_copy_sha256"),
        )
        if source_copy.candidate != candidate or source_copy.actual_derived_source_copy_sha256 != candidate.manifest.expected_derived_source_copy_sha256:
            raise _error("release-checkpoint-binding-mismatch", "source copy is not exactly candidate-bound")
        return name, source_copy
    if name == "compilation":
        restored = _load_model(tagged["value"], SealedCandidateCompilation, "compilation")
        if restored.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256 or restored.authority != candidate.authority:
            raise _error("release-checkpoint-binding-mismatch", "compilation is not exactly candidate-bound")
        return name, restored
    if name == "package":
        package = _package_value(tagged["value"])
        if package["candidate_snapshot_manifest_sha256"] != candidate.manifest.sha256:
            raise _error("release-checkpoint-binding-mismatch", "package is not exactly candidate-bound")
        return name, package
    cls = _tagged_type(name)
    tuples = {
        "suite": frozenset({"command", "coverage"}),
        "retirement": frozenset({"retaining_container_refs", "observed_rollback_refs", "required_rollback_refs"}),
    }.get(name, frozenset())
    if name == "e2e":
        restored = _load_e2e(tagged["value"])
    else:
        restored = _load_dataclass(tagged["value"], cls, name, tuple_fields=tuples)
    if getattr(restored, "candidate_snapshot_manifest_sha256", None) != candidate.manifest.sha256:
        raise _error("release-checkpoint-binding-mismatch", f"{name} is not exactly candidate-bound")
    return name, restored


def _context_value(context: SelectedReleaseActionContext) -> dict[str, Any]:
    if type(context) is not SelectedReleaseActionContext:
        raise _error("release-checkpoint-invalid", "context is not selected typed state")
    return _dump_dataclass(context, SelectedReleaseActionContext, "context")


# Checkpoints preserve the selected Workflow definition recorded when the Run
# began.  Retain the immediately preceding O164 revision for status/recovery,
# but reject an unknown revision rather than silently rebinding it.
_SUPPORTED_RELEASE_WORKFLOW_VERSIONS = frozenset({5, 6})


def _load_context(value: Any, index: int, *, root: str, workflow_run_id: str, fingerprint: str) -> SelectedReleaseActionContext:
    context = _load_dataclass(value, SelectedReleaseActionContext, "context")
    if (
        context.project_root != root
        or context.workflow_run_id != workflow_run_id
        or context.parent_workflow_run_id != workflow_run_id
        or context.parent_step_run_id != context.step_run_id
        or context.frozen_parameters_sha256 != fingerprint
        or context.workflow_atom_id != "CA-O-164"
        or type(context.workflow_version) is not int
        or context.workflow_version not in _SUPPORTED_RELEASE_WORKFLOW_VERSIONS
    ):
        raise _error("release-checkpoint-binding-mismatch", "context does not belong to the frozen selected Run")
    for name, identity in (("step_run_id", context.step_run_id), ("action_run_id", context.action_run_id)):
        _text(identity, f"context.{name}")
    step, action, _phase = PHASES[index]
    if (context.step_atom_id, context.action_atom_id) != (step, action):
        raise _error("release-checkpoint-phase-mismatch", "context Step/Action is outside its selected phase")
    return context


def _result_value(result: ReleasePhaseResult) -> dict[str, Any]:
    if type(result) is not ReleasePhaseResult:
        raise _error("release-checkpoint-invalid", "phase result is not typed state")
    # ``asdict`` would recursively expand the typed ``output`` evidence before
    # this codec can apply its closed tag.  Copy every other exact dataclass
    # member directly, so the output has one and only one admitted encoding.
    payload = {
        item.name: _json_value(getattr(result, item.name), f"result.{item.name}")
        for item in fields(ReleasePhaseResult)
        if item.name != "output"
    }
    output = result.output
    if output is None:
        payload["output"] = None
        return payload
    matching = [name for name, cls in _TAGGED_TYPES.items() if type(output) is cls]
    if not matching and type(output) is _full_gate_type():
        matching = ["full_gate"]
    if len(matching) != 1:
        raise _error("release-checkpoint-invalid", "phase result output is not an admitted typed Release observation")
    payload["output"] = _tag(matching[0], output)
    return payload


def _shared_recording(value: Any, label: str) -> dict[str, str] | None:
    """Validate the one current closed retirement-recording handoff.

    This is deliberately a packet for the shared recorder, not its durable
    receipt.  The checkpoint keeps it only so recovery can request that same
    recorder action without inventing or broadening the private Release Run.
    """

    if value is None:
        return None
    packet = _mapping(value, {
        "on_recorded_result", "candidate_snapshot_manifest_sha256", "prior_image_digest",
        "retirement_receipt_ref", "retirement_receipt_sha256",
    }, label)
    return {
        "on_recorded_result": _text(packet["on_recorded_result"], f"{label}.on_recorded_result"),
        "candidate_snapshot_manifest_sha256": _sha256(packet["candidate_snapshot_manifest_sha256"], f"{label}.candidate_snapshot_manifest_sha256"),
        "prior_image_digest": _text(packet["prior_image_digest"], f"{label}.prior_image_digest"),
        "retirement_receipt_ref": _safe_path(packet["retirement_receipt_ref"], f"{label}.retirement_receipt_ref"),
        "retirement_receipt_sha256": _sha256(packet["retirement_receipt_sha256"], f"{label}.retirement_receipt_sha256"),
    }


def _load_result(value: Any, index: int, context: SelectedReleaseActionContext, candidate: ValidatedCandidate) -> ReleasePhaseResult:
    required = {item.name for item in fields(ReleasePhaseResult)}
    payload = _mapping(value, required, "result")
    output = payload["output"]
    restored_output = None
    if output is not None:
        tag, restored_output = _load_tag(output, candidate, candidate.project_root)
        expected = _PHASE_STATE[PHASES[index][2]]
        if tag != expected:
            raise _error("release-checkpoint-phase-mismatch", "phase result output has an invalid observation type")
    copied = dict(payload)
    copied["output"] = restored_output
    if "shared_action_recording" in copied:
        copied["shared_action_recording"] = _shared_recording(copied["shared_action_recording"], "result.shared_action_recording")
    result = _load_dataclass(copied, ReleasePhaseResult, "result", tuple_fields=frozenset({"attempted_effects", "effect_evidence_refs", "declared_run_receipt_refs"}))
    step, action, phase = PHASES[index]
    if (
        result.workflow_run_id != context.workflow_run_id
        or result.step_run_id != context.step_run_id
        or result.action_run_id != context.action_run_id
        or result.step_atom_id != step
        or result.action_atom_id != action
        or result.phase != phase
        or result.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
        or result.recording_state != "shared_session_provider_pending"
        or result.outcome not in {"prepared", "completed", "blocked", "failed", "pending", "effect_uncertain"}
    ):
        raise _error("release-checkpoint-phase-mismatch", "result does not match its selected phase context")
    if result.output is not None and result.output != restored_output:
        raise _error("release-checkpoint-invalid", "result output was not reconstructed exactly")
    if result.shared_action_recording is not None:
        packet = _shared_recording(result.shared_action_recording, "result.shared_action_recording")
        if (
            index != len(PHASES) - 1
            or result.phase != "retire"
            or result.outcome != "pending"
            or result.effect_outcome != "retired"
            or packet["candidate_snapshot_manifest_sha256"] != candidate.manifest.sha256
            or not isinstance(result.output, ImageRetirementEvidence)
            or packet["prior_image_digest"] != result.output.prior_image_digest
            or packet["retirement_receipt_sha256"] != result.output.receipt_sha256
            or packet["retirement_receipt_ref"] != f"{result.output.evidence_root}/receipt.json"
        ):
            raise _error("release-checkpoint-phase-mismatch", "shared recording handoff is not the exact terminal retirement packet")
    return result


def _canonical_input(value: bytes | str) -> dict[str, Any]:
    raw = value if isinstance(value, bytes) else value.encode("utf-8") if isinstance(value, str) else None
    if raw is None:
        raise _error("release-checkpoint-invalid", "checkpoint must be canonical JSON bytes or text")
    try:
        decoded = json.loads(raw.decode("utf-8"), parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    except (UnicodeDecodeError, ValueError, TypeError) as error:
        raise _error("release-checkpoint-invalid", "checkpoint is not valid canonical JSON") from error
    if not isinstance(decoded, dict) or canonical_json(decoded) != raw:
        raise _error("release-checkpoint-invalid", "checkpoint JSON is not canonical and closed")
    return decoded


# ``_load_state`` needs two values before it can restore later fields.  Keeping
# that state local avoids a global registry or provider side channel.
class _StateReader:
    def __init__(self, root: str) -> None:
        self.root = root
        self.candidate: ValidatedCandidate | None = None

    def read(self, name: str, value: Any) -> Any:
        if value is None:
            return None
        tag, restored = _load_tag(value, self.candidate, self.root)
        if tag != name:
            raise _error("release-checkpoint-invalid", "state field tag does not match its fixed field")
        if name == "candidate":
            self.candidate = restored
        return restored


def _state_value(run: ReleaseActionRun, name: str) -> Any:
    value = getattr(run, name)
    return None if value is None else _tag(name, value)


def _validate_state_dependencies(state: dict[str, Any], candidate: ValidatedCandidate | None, preflight: ReleaseCompilationPreflight | None) -> None:
    if (candidate is None) != (preflight is None):
        raise _error("release-checkpoint-phase-mismatch", "candidate and preflight must be retained together")
    if candidate is None:
        if any(state[name] is not None for name in _STATE_NAMES[2:]):
            raise _error("release-checkpoint-phase-mismatch", "post-freeze evidence lacks the frozen candidate")
        return
    source_copy = state["source_copy"]
    compilation = state["compilation"]
    suite = state["suite"]
    package = state["package"]
    build = state["build"]
    verification = state["verification"]
    e2e = state["e2e"]
    full_gate = state["full_gate"]
    promotion = state["promotion"]
    retirement = state["retirement"]
    if source_copy is None and any(value is not None for value in (compilation, suite, package, build, verification, e2e, full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "post-delivery evidence lacks the retained source copy")
    if compilation is None and any(value is not None for value in (suite, package, build, verification, e2e, full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "post-compilation evidence lacks compilation")
    if suite is None and any(value is not None for value in (package, build, verification, e2e, full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "post-suite evidence lacks suite evidence")
    if package is None and any(value is not None for value in (build, verification, e2e, full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "image evidence lacks candidate package staging")
    if build is None and any(value is not None for value in (verification, e2e, full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "later evidence lacks image build evidence")
    if verification is None and any(value is not None for value in (e2e, full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "later evidence lacks candidate verification")
    if e2e is None and any(value is not None for value in (full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "later evidence lacks host candidate E2E evidence")
    if full_gate is None and any(value is not None for value in (promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "later evidence lacks aggregate full-gate evidence")
    if promotion is not None and (not e2e.passed or not full_gate.passed):
        raise _error("release-checkpoint-phase-mismatch", "promotion lacks passing host E2E and aggregate evidence")
    if full_gate is not None and (
        full_gate.phase_map_sha256 != suite.phase_map_sha256
        or full_gate.phase_map_sha256 != e2e.phase_map_sha256
        or full_gate.candidate_image_digest != build.candidate_image_digest
        or full_gate.candidate_image_digest != verification.candidate_image_digest
        or full_gate.candidate_image_digest != e2e.candidate_image_digest
        or full_gate.suite_receipt_sha256 != suite.receipt_sha256
        or full_gate.build_receipt_sha256 != build.receipt_sha256
        or full_gate.image_receipt_sha256 != verification.receipt_sha256
        or full_gate.e2e_receipt_sha256 != e2e.receipt_sha256
    ):
        raise _error("release-checkpoint-binding-mismatch", "aggregate differs from its exact retained predecessor receipts")
    if promotion is None and retirement is not None:
        raise _error("release-checkpoint-phase-mismatch", "retirement evidence lacks promotion evidence")


def _validate_phase_continuity(
    *, next_phase: int, stopped: bool, in_progress: SelectedReleaseActionContext | None,
    contexts: dict[int, SelectedReleaseActionContext], results: dict[int, ReleasePhaseResult],
) -> None:
    if next_phase < 0 or next_phase > len(PHASES):
        raise _error("release-checkpoint-phase-mismatch", "next phase is outside the selected Workflow")
    completed = set(range(next_phase))
    if set(results) - (completed | ({next_phase} if next_phase < len(PHASES) else set())):
        raise _error("release-checkpoint-phase-mismatch", "checkpoint has a result outside the reachable prefix")
    for index in completed:
        if index not in contexts or index not in results or results[index].outcome != "completed":
            raise _error("release-checkpoint-phase-mismatch", "completed prefix lacks exact completed observations")
    if any(index not in contexts for index in results):
        raise _error("release-checkpoint-phase-mismatch", "result has no retained selected context")
    terminal = results.get(next_phase) if next_phase < len(PHASES) else None
    if terminal is not None and terminal.outcome == "completed":
        raise _error("release-checkpoint-phase-mismatch", "completed result did not advance the selected phase")
    if in_progress is not None:
        if next_phase >= len(PHASES) or contexts.get(next_phase) != in_progress or terminal is not None:
            raise _error("release-checkpoint-phase-mismatch", "in-progress state is not one reachable selected phase")
        if stopped:
            raise _error("release-checkpoint-phase-mismatch", "stopped Run cannot retain an in-progress effect")
    elif not stopped and (terminal is not None or set(results) != completed):
        raise _error("release-checkpoint-phase-mismatch", "active Run has an unadvanced terminal result")
    elif stopped and terminal is None and next_phase < len(PHASES):
        raise _error("release-checkpoint-phase-mismatch", "stopped Run lacks terminal or interrupted phase evidence")


def _validate_result_outputs(results: dict[int, ReleasePhaseResult], state: dict[str, Any]) -> None:
    """A result may point only to the exact retained observation for its phase."""

    for index, result in results.items():
        expected = state[_PHASE_STATE[PHASES[index][2]]]
        if result.output is not None and result.output != expected:
            raise _error("release-checkpoint-phase-mismatch", "phase result does not retain its exact state observation")
        if result.outcome == "completed" and result.output is None:
            raise _error("release-checkpoint-phase-mismatch", "completed phase lacks its typed observation")


def _shared_recordings_value(
    shared_recordings: Mapping[int, Mapping[str, Any]] | None,
    results: Mapping[int, ReleasePhaseResult],
) -> list[dict[str, Any]]:
    """Encode only durable shared Action-terminal receipt references.

    These entries are not another Journal.  They are the exact receipt
    references already issued by the shared dispatcher, retained beside the
    private frontier so recovery can distinguish a recorded terminal Action
    from an uncertain effect.
    """

    if shared_recordings is None:
        return []
    if not isinstance(shared_recordings, Mapping):
        raise _error("release-checkpoint-invalid", "shared recordings must be indexed typed state")
    indexed: list[tuple[int, Mapping[str, Any]]] = []
    for raw_index, source in shared_recordings.items():
        index = _index(raw_index, "shared_recordings.index")
        indexed.append((index, source))
    records: list[dict[str, Any]] = []
    for index, source in sorted(indexed):
        if index not in results:
            raise _error("release-checkpoint-phase-mismatch", "shared recording has no retained phase result")
        packet = _mapping(source, {"terminal_outcome", "receipt_refs"}, "shared_recording")
        terminal_outcome = _text(packet["terminal_outcome"], "shared_recording.terminal_outcome")
        if terminal_outcome not in {"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"}:
            raise _error("release-checkpoint-invalid", "shared recording has an unsupported terminal outcome")
        refs = packet["receipt_refs"]
        if not isinstance(refs, (list, tuple)) or not refs:
            raise _error("release-checkpoint-invalid", "shared recording requires canonical receipt references")
        receipt_refs = [_text(reference, "shared_recording.receipt_refs") for reference in refs]
        if len(set(receipt_refs)) != len(receipt_refs):
            raise _error("release-checkpoint-invalid", "shared recording repeats one canonical receipt reference")
        records.append({"index": index, "terminal_outcome": terminal_outcome, "receipt_refs": receipt_refs})
    if len({record["index"] for record in records}) != len(records):
        raise _error("release-checkpoint-invalid", "shared recordings repeat one selected phase")
    return records


def _load_shared_recordings(value: Any, results: Mapping[int, ReleasePhaseResult]) -> dict[int, dict[str, Any]]:
    if not isinstance(value, list):
        raise _error("release-checkpoint-invalid", "shared recordings must be a canonical list")
    restored: dict[int, dict[str, Any]] = {}
    prior = -1
    for source in value:
        packet = _mapping(source, {"index", "terminal_outcome", "receipt_refs"}, "shared_recording")
        index = _index(packet["index"], "shared_recording.index")
        if index <= prior or index not in results:
            raise _error("release-checkpoint-phase-mismatch", "shared recording is unordered, repeated, or has no phase result")
        prior = index
        terminal_outcome = _text(packet["terminal_outcome"], "shared_recording.terminal_outcome")
        if terminal_outcome not in {"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"}:
            raise _error("release-checkpoint-invalid", "shared recording has an unsupported terminal outcome")
        refs = packet["receipt_refs"]
        if not isinstance(refs, list) or not refs:
            raise _error("release-checkpoint-invalid", "shared recording requires canonical receipt references")
        receipt_refs = [_text(reference, "shared_recording.receipt_refs") for reference in refs]
        if len(set(receipt_refs)) != len(receipt_refs):
            raise _error("release-checkpoint-invalid", "shared recording repeats one canonical receipt reference")
        restored[index] = {"terminal_outcome": terminal_outcome, "receipt_refs": tuple(receipt_refs)}
    return restored


def _pending_recordings_value(
    pending_recordings: Mapping[int, Mapping[str, Any]] | None,
    results: Mapping[int, ReleasePhaseResult],
    shared_recordings: Mapping[int, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Encode unresolved shared-recorder identities without treating them as proof.

    A pending entry names the single sealed Journal event whose original bytes
    the shared recorder must reconcile.  It is deliberately not a receipt,
    terminal result, or authority to advance a Release phase.  Its
    ``event_outcome`` is the original outcome sealed in the failed Journal
    append; it is not a claim that a durable terminal receipt exists.
    """

    if pending_recordings is None:
        return []
    if not isinstance(pending_recordings, Mapping):
        raise _error("release-checkpoint-invalid", "pending recordings must be indexed typed state")
    indexed: list[tuple[int, Mapping[str, Any]]] = []
    for raw_index, source in pending_recordings.items():
        index = _index(raw_index, "pending_recordings.index")
        if not isinstance(source, Mapping):
            raise _error("release-checkpoint-invalid", "pending recording must be one closed object")
        indexed.append((index, source))
    records: list[dict[str, Any]] = []
    seen_event_ids: set[str] = set()
    for index, source in sorted(indexed):
        if index not in results:
            raise _error("release-checkpoint-phase-mismatch", "pending recording has no retained phase result")
        if index in shared_recordings:
            raise _error("release-checkpoint-phase-mismatch", "one phase cannot be both pending and durably recorded")
        packet = _mapping(dict(source), {"event_id", "event_outcome"}, "pending_recording")
        event_id = _text(packet["event_id"], "pending_recording.event_id")
        event_outcome = _text(packet["event_outcome"], "pending_recording.event_outcome")
        if event_outcome not in _PENDING_EVENT_OUTCOMES:
            raise _error("release-checkpoint-invalid", "pending recording has an unsupported original event outcome")
        if event_id in seen_event_ids:
            raise _error("release-checkpoint-invalid", "pending recordings repeat one event identity")
        seen_event_ids.add(event_id)
        records.append({"index": index, "event_id": event_id, "event_outcome": event_outcome})
    if len({record["index"] for record in records}) != len(records):
        raise _error("release-checkpoint-invalid", "pending recordings repeat one selected phase")
    return records


def _load_pending_recordings(
    value: Any,
    results: Mapping[int, ReleasePhaseResult],
    shared_recordings: Mapping[int, Mapping[str, Any]],
) -> dict[int, dict[str, str]]:
    if not isinstance(value, list):
        raise _error("release-checkpoint-invalid", "pending recordings must be a canonical list")
    restored: dict[int, dict[str, str]] = {}
    prior = -1
    seen_event_ids: set[str] = set()
    for source in value:
        packet = _mapping(source, {"index", "event_id", "event_outcome"}, "pending_recording")
        index = _index(packet["index"], "pending_recording.index")
        if index <= prior or index not in results:
            raise _error("release-checkpoint-phase-mismatch", "pending recording is unordered, repeated, or has no phase result")
        if index in shared_recordings:
            raise _error("release-checkpoint-phase-mismatch", "one phase cannot be both pending and durably recorded")
        prior = index
        event_id = _text(packet["event_id"], "pending_recording.event_id")
        event_outcome = _text(packet["event_outcome"], "pending_recording.event_outcome")
        if event_outcome not in _PENDING_EVENT_OUTCOMES:
            raise _error("release-checkpoint-invalid", "pending recording has an unsupported original event outcome")
        if event_id in seen_event_ids:
            raise _error("release-checkpoint-invalid", "pending recordings repeat one event identity")
        seen_event_ids.add(event_id)
        restored[index] = {"event_id": event_id, "event_outcome": event_outcome}
    return restored


def encode_release_action_checkpoint(
    run: ReleaseActionRun, *, shared_recordings: Mapping[int, Mapping[str, Any]] | None = None,
    pending_recordings: Mapping[int, Mapping[str, Any]] | None = None,
) -> bytes:
    """Return one canonical, closed JSON checkpoint without persisting it."""

    if type(run) is not ReleaseActionRun:
        raise _error("release-checkpoint-invalid", "checkpoint requires one private ReleaseActionRun")
    root = str(Path(run.project_root).resolve(strict=True))
    if root != run.project_root:
        raise _error("release-checkpoint-binding-mismatch", "run root is not canonical")
    request = _load_model(run.request.model_dump(mode="json", by_alias=True), ReleaseVersionRequest, "request")
    if request.project_root != root or _fingerprint(request) != _sha256(run.frozen_parameters_sha256, "frozen_parameters_sha256"):
        raise _error("release-checkpoint-binding-mismatch", "run request, root, or fingerprint is not frozen")
    contexts = []
    for index, context in sorted(run.contexts.items()):
        index = _index(index, "contexts.index")
        _load_context(_context_value(context), index, root=root, workflow_run_id=run.workflow_run_id, fingerprint=run.frozen_parameters_sha256)
        contexts.append({"index": index, "context": _context_value(context)})
    results = []
    candidate = run.candidate
    if candidate is not None:
        candidate = _load_candidate(_candidate_value(candidate), root)
    for index, result in sorted(run.results.items()):
        index = _index(index, "results.index")
        if candidate is None or index not in run.contexts:
            raise _error("release-checkpoint-phase-mismatch", "result has no frozen candidate or context")
        _load_result(_result_value(result), index, run.contexts[index], candidate)
        results.append({"index": index, "result": _result_value(result)})
    if run.in_progress is not None:
        _load_context(_context_value(run.in_progress), run.next_phase, root=root, workflow_run_id=run.workflow_run_id, fingerprint=run.frozen_parameters_sha256)
    state = {name: _state_value(run, name) for name in _STATE_NAMES}
    reader = _StateReader(root)
    restored_state = {name: reader.read(name, state[name]) for name in _STATE_NAMES}
    _validate_state_dependencies(restored_state, reader.candidate, restored_state["preflight"])
    _validate_phase_continuity(next_phase=run.next_phase, stopped=run.stopped, in_progress=run.in_progress,
                               contexts=run.contexts, results=run.results)
    _validate_result_outputs(run.results, restored_state)
    recording_payload = _shared_recordings_value(shared_recordings, run.results)
    pending_recording_payload = _pending_recordings_value(
        pending_recordings, run.results,
        {record["index"]: record for record in recording_payload},
    )
    payload = {
        "schema": RELEASE_ACTION_CHECKPOINT_SCHEMA,
        "kind": "release_action_run",
        "sha256": "0" * 64,
        "project_root": root,
        "workflow_run_id": _text(run.workflow_run_id, "workflow_run_id"),
        "frozen_parameters_sha256": _sha256(run.frozen_parameters_sha256, "frozen_parameters_sha256"),
        "request": _dump_model(request, ReleaseVersionRequest, "request"),
        "next_phase": run.next_phase,
        "stopped": run.stopped,
        "in_progress": None if run.in_progress is None else _context_value(run.in_progress),
        "contexts": contexts,
        "results": results,
        "shared_recordings": recording_payload,
        "pending_recordings": pending_recording_payload,
        "state": state,
    }
    if type(run.stopped) is not bool:
        raise _error("release-checkpoint-invalid", "stopped must be a boolean")
    payload["sha256"] = release_action_checkpoint_sha256(payload)
    return canonical_json(payload)


def dump_release_checkpoint(
    run: ReleaseActionRun, *, shared_recordings: Mapping[int, Mapping[str, Any]] | None = None,
    pending_recordings: Mapping[int, Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Return a closed, digest-sealed checkpoint envelope without persisting it."""

    return json.loads(encode_release_action_checkpoint(
        run, shared_recordings=shared_recordings, pending_recordings=pending_recordings,
    ).decode("utf-8"))


def derive_unknown_effect_terminal_checkpoint(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Derive, but never replace, N15's stopped unknown-effect frontier.

    The original checkpoint is historical evidence for the host-loss boundary.
    This narrowly scoped codec operation restores that evidence, proves the
    one admitted pre-effect frontier, and emits a *separate* terminal
    checkpoint.  It has no Journal, provider, Docker, or filesystem effect.

    Its caller is responsible for retaining the original checkpoint bytes and
    choosing the governed companion carrier for the returned payload.
    """

    if not isinstance(payload, Mapping):
        raise _error("release-checkpoint-invalid", "unknown-effect resolution requires one checkpoint envelope")
    run, shared_recordings, pending_recordings = _restore_release_action_checkpoint(canonical_json(dict(payload)))
    context = run.in_progress
    if (
        run.workflow_run_id != "release-epic-resume-20261006-N15"
        or run.next_phase != 4
        or run.stopped is not False
        or context is None
        or set(run.contexts) != {0, 1, 2, 3, 4}
        or set(run.results) != {0, 1, 2, 3}
        or any(run.results[index].outcome != "completed" for index in range(4))
        or set(shared_recordings) != {0, 1, 2, 3}
        or pending_recordings
    ):
        raise _error("release-checkpoint-unknown-effect-mismatch", "checkpoint is not the admitted N15 unknown-effect frontier")
    if any(
        record.get("terminal_outcome") != "completed"
        or not isinstance(record.get("receipt_refs"), tuple)
        or len(record["receipt_refs"]) != 1
        for record in shared_recordings.values()
    ):
        raise _error("release-checkpoint-unknown-effect-mismatch", "checkpoint predecessor receipts are not exact completed records")
    step, action, phase = PHASES[4]
    if (
        context != run.contexts[4]
        or context.workflow_run_id != run.workflow_run_id
        or context.step_run_id != "release-epic-resume-20261006-N15:step:5"
        or context.action_run_id != "release-epic-resume-20261006-N15:step:5:action:1"
        or (context.step_atom_id, context.action_atom_id, phase) != (step, action, "closed_unit_gate")
        or run.candidate is None
    ):
        raise _error("release-checkpoint-unknown-effect-mismatch", "checkpoint has a different N15 in-progress occurrence")

    run.results[4] = ReleasePhaseResult(
        workflow_run_id=context.workflow_run_id,
        step_run_id=context.step_run_id,
        action_run_id=context.action_run_id,
        step_atom_id=step,
        action_atom_id=action,
        phase=phase,
        outcome="effect_uncertain",
        reason="unknown_effect",
        candidate_snapshot_manifest_sha256=run.candidate.manifest.sha256,
        attempted_effects=(),
        effect_evidence_refs=(),
        declared_run_receipt_refs=(),
    )
    run.in_progress = None
    run.stopped = True
    # The terminal companion must retain the same completed predecessor
    # receipts.  The original carrier remains untouched; this copy only adds
    # the stopped phase-four uncertainty result.
    return dump_release_checkpoint(run, shared_recordings=shared_recordings, pending_recordings={})


def _restore_release_action_checkpoint(
    checkpoint: bytes | str, *, image_executor: AdmittedImageExecutor | None = None,
) -> tuple[ReleaseActionRun, dict[int, dict[str, Any]], dict[int, dict[str, str]]]:
    """Restore exact private state; an executor is deliberately reinjected externally."""

    payload = _mapping(_canonical_input(checkpoint), {
        "schema", "kind", "sha256", "project_root", "workflow_run_id", "frozen_parameters_sha256", "request",
        "next_phase", "stopped", "in_progress", "contexts", "results", "shared_recordings", "pending_recordings", "state",
    }, "checkpoint")
    if payload["schema"] != RELEASE_ACTION_CHECKPOINT_SCHEMA or payload["kind"] != "release_action_run":
        raise _error("release-checkpoint-schema-unsupported", "checkpoint schema or kind is not supported")
    if _sha256(payload["sha256"], "sha256") != release_action_checkpoint_sha256(payload):
        raise _error("release-checkpoint-digest-mismatch", "checkpoint content digest does not match its canonical bytes")
    root = str(Path(_text(payload["project_root"], "project_root")).resolve(strict=True))
    if payload["project_root"] != root:
        raise _error("release-checkpoint-binding-mismatch", "checkpoint root is not canonical")
    workflow_run_id = _text(payload["workflow_run_id"], "workflow_run_id")
    fingerprint = _sha256(payload["frozen_parameters_sha256"], "frozen_parameters_sha256")
    request = _load_model(payload["request"], ReleaseVersionRequest, "request")
    if request.project_root != root or _fingerprint(request) != fingerprint:
        raise _error("release-checkpoint-binding-mismatch", "request root or fingerprint does not match checkpoint")
    if type(payload["next_phase"]) is not int or not 0 <= payload["next_phase"] <= len(PHASES) or type(payload["stopped"]) is not bool:
        raise _error("release-checkpoint-phase-mismatch", "checkpoint next phase or stopped value is invalid")
    if image_executor is not None and (
        type(image_executor) is not AdmittedImageExecutor
        or image_executor.project_root != root
        or image_executor.workflow_run_id != workflow_run_id
        or not callable(getattr(image_executor.executor, "run", None))
    ):
        raise _error("release-checkpoint-executor-unadmitted", "restored Run executor is not externally re-admitted")
    reader = _StateReader(root)
    state_payload = _mapping(payload["state"], set(_STATE_NAMES), "state")
    state = {name: reader.read(name, state_payload[name]) for name in _STATE_NAMES}
    candidate = reader.candidate
    _validate_state_dependencies(state, candidate, state["preflight"])
    contexts: dict[int, SelectedReleaseActionContext] = {}
    if not isinstance(payload["contexts"], list):
        raise _error("release-checkpoint-invalid", "contexts must be a canonical list")
    for entry in payload["contexts"]:
        record = _mapping(entry, {"index", "context"}, "context record")
        index = _index(record["index"], "contexts.index")
        if index in contexts:
            raise _error("release-checkpoint-invalid", "contexts repeat a selected phase")
        contexts[index] = _load_context(record["context"], index, root=root, workflow_run_id=workflow_run_id, fingerprint=fingerprint)
    if not isinstance(payload["results"], list) or candidate is None:
        if payload["results"] or candidate is not None:
            raise _error("release-checkpoint-invalid", "results require one frozen candidate")
        results: dict[int, ReleasePhaseResult] = {}
    else:
        results = {}
        for entry in payload["results"]:
            record = _mapping(entry, {"index", "result"}, "result record")
            index = _index(record["index"], "results.index")
            if index in results or index not in contexts:
                raise _error("release-checkpoint-invalid", "result repeats or lacks its selected context")
            results[index] = _load_result(record["result"], index, contexts[index], candidate)
    in_progress = None
    if payload["in_progress"] is not None:
        in_progress = _load_context(payload["in_progress"], payload["next_phase"], root=root,
                                    workflow_run_id=workflow_run_id, fingerprint=fingerprint)
    _validate_phase_continuity(next_phase=payload["next_phase"], stopped=payload["stopped"], in_progress=in_progress,
                               contexts=contexts, results=results)
    _validate_result_outputs(results, state)
    shared_recordings = _load_shared_recordings(payload["shared_recordings"], results)
    pending_recordings = _load_pending_recordings(payload["pending_recordings"], results, shared_recordings)
    return ReleaseActionRun(
        project_root=root,
        workflow_run_id=workflow_run_id,
        frozen_parameters_sha256=fingerprint,
        request=request,
        image_executor=image_executor,
        next_phase=payload["next_phase"],
        stopped=payload["stopped"],
        in_progress=in_progress,
        contexts=contexts,
        results=results,
        **state,
    ), shared_recordings, pending_recordings


def restore_release_action_checkpoint(
    checkpoint: bytes | str, *, image_executor: AdmittedImageExecutor | None = None,
) -> ReleaseActionRun:
    """Restore exact private state; an executor is deliberately reinjected externally."""

    run, _shared_recordings, _pending_recordings = _restore_release_action_checkpoint(
        checkpoint, image_executor=image_executor,
    )
    return run


def load_release_checkpoint(
    payload: Mapping[str, Any], *, expected_request: ReleaseVersionRequest | Mapping[str, Any],
    expected_workflow_run_id: str, image_executor: AdmittedImageExecutor | None = None,
) -> tuple[ReleaseActionRun, dict[int, dict[str, Any]]]:
    """Restore a sealed envelope only for the caller's exact frozen Run.

    The shared terminal records are returned separately because the private
    ``ReleaseActionRun`` intentionally owns no Journal or dispatcher state.
    Their receipt references must be admitted by the shared dispatcher before
    it treats an effect as terminal; this function never does that admission.
    """

    if not isinstance(payload, Mapping):
        raise _error("release-checkpoint-invalid", "checkpoint envelope must be one object")
    expected = expected_request if type(expected_request) is ReleaseVersionRequest else _load_model(
        expected_request, ReleaseVersionRequest, "expected_request",
    )
    expected_id = _text(expected_workflow_run_id, "expected_workflow_run_id")
    run, recordings, _pending_recordings = _restore_release_action_checkpoint(
        canonical_json(dict(payload)), image_executor=image_executor,
    )
    if run.workflow_run_id != expected_id or run.request != expected or run.frozen_parameters_sha256 != _fingerprint(expected):
        raise _error("release-checkpoint-binding-mismatch", "checkpoint is not for the exact expected frozen Release Run")
    return run, recordings


def extract_pending_recordings(payload: Mapping[str, Any]) -> Mapping[int, Mapping[str, str]]:
    """Return immutable pending-recorder identities from one sealed checkpoint.

    The returned values are recovery hints only.  A caller must still reopen
    the exact pending Journal Event through the canonical shared recorder and
    obtain a durable receipt before it may regard a phase as terminal.
    """

    if not isinstance(payload, Mapping):
        raise _error("release-checkpoint-invalid", "checkpoint envelope must be one object")
    _run, _recordings, pending_recordings = _restore_release_action_checkpoint(canonical_json(dict(payload)))
    return MappingProxyType({
        index: MappingProxyType(dict(record))
        for index, record in pending_recordings.items()
    })


__all__ = [
    "RELEASE_ACTION_CHECKPOINT_SCHEMA",
    "derive_unknown_effect_terminal_checkpoint",
    "release_action_checkpoint_sha256",
    "dump_release_checkpoint",
    "encode_release_action_checkpoint",
    "load_release_checkpoint",
    "extract_pending_recordings",
    "restore_release_action_checkpoint",
]
