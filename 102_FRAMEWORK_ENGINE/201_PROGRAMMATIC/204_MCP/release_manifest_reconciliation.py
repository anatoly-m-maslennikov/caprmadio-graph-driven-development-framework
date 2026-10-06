"""Private, recording-only reconciliation for the selected Release binding.

This module advances Journal observation of the bytes that are already present
in the canonical binding carrier.  It does not write the Manifest, refresh its
admission, dispatch a route, or represent a historical change as completed.
"""
from __future__ import annotations

from contextlib import contextmanager
import datetime as dt
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from types import MappingProxyType
from typing import Any, Mapping
import weakref


MCP = Path(__file__).resolve().parent
TOOLS = MCP.parent / "201_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import work_journal  # noqa: E402
from release_manifest_authorization import (  # noqa: E402
    _journal_context,
    _operator_row,
    _root as authorization_root,
    _safe_ref,
    _source_frontier_digest,
    ReleaseManifestAuthorizationError,
)
from release_source_admission import (  # noqa: E402
    ReleaseSourceAdmissionError,
    derive_release_graph_admission,
)
from selected_routes import (  # noqa: E402
    SelectedRouteError,
    canonical_digest,
    load_release_manifest_refresh_base,
    selected_manifest_ref,
)


ACTION_ID = "MCP_RELEASE_MANIFEST_PUBLICATION"
STRUCTURAL_SCOPE = "MCP"
_OBSERVATION_PREFIX = "release-manifest-reconciliation:"
_PENDING_PREFIX = _OBSERVATION_PREFIX
_SHA256 = re.compile(r"[0-9a-f]{64}")
_HEX = re.compile(r"[0-9a-f]{40,64}")

_PLAN_FIELDS = frozenset({
    "operation",
    "manifest_ref",
    "observed_raw_sha256",
    "git_head_commit",
    "git_blob_oid",
    "git_blob_sha256",
    "latest_event_id",
    "latest_event_digest",
    "latest_result_sha256",
    "latest_version",
    "next_version",
    "observation_event_id",
    "refresh_base_digest",
    "source_frontier_digest",
    "observation_state",
})


class ReleaseManifestReconciliationError(ValueError):
    """The exact current-state observation cannot be safely recorded."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


class ReconciliationAuthorizationContext:
    """Opaque host-issued authority for one exact observation plan."""

    __slots__ = (
        "_root", "_plan", "_operator_name", "_journal_author", "_llm_session",
        "_authorization_ref", "_purpose", "_pending_event_id", "_pending_event_digest",
        "__weakref__",
    )

    def __init__(self, *_: object, **__: object) -> None:
        raise TypeError("ReconciliationAuthorizationContext is issued only by a trusted host")

    def __setattr__(self, _: str, __: object) -> None:
        raise AttributeError("ReconciliationAuthorizationContext is immutable")

    def __repr__(self) -> str:
        return "<ReconciliationAuthorizationContext trusted-host-issued>"

    def __reduce__(self) -> object:
        raise TypeError("ReconciliationAuthorizationContext is not serializable")

    def __reduce_ex__(self, _: int) -> object:
        raise TypeError("ReconciliationAuthorizationContext is not serializable")

    def __getstate__(self) -> object:
        raise TypeError("ReconciliationAuthorizationContext is not serializable")

    @property
    def operator_name(self) -> str:
        return self._operator_name

    @property
    def journal_author(self) -> str:
        return self._journal_author

    @property
    def llm_session(self) -> dict[str, str]:
        return {"app": self._llm_session[0], "uuid": self._llm_session[1]}

    @property
    def authorization_ref(self) -> str:
        return self._authorization_ref

    @property
    def pending_event_id(self) -> str | None:
        return self._pending_event_id


_issued: dict[int, tuple[weakref.ReferenceType[ReconciliationAuthorizationContext], tuple[object, ...]]] = {}


def _reject(code: str, message: str) -> None:
    raise ReleaseManifestReconciliationError(code, message)


def _root(value: str | Path) -> Path:
    try:
        requested = Path(value)
        root = requested.resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise ReleaseManifestReconciliationError("reconciliation-root-invalid", "Project root is unavailable") from error
    if requested.is_symlink() or root.is_symlink() or not root.is_dir():
        _reject("reconciliation-root-invalid", "Project root must be a regular directory")
    return root


def _digest(value: object, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        _reject("reconciliation-plan-invalid", f"{label} must be a lowercase SHA-256 digest")
    return value


def _safe_event_id(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or "\n" in value or "\r" in value:
        _reject("reconciliation-plan-invalid", f"{label} must be a non-empty single-line identity")
    return value


def _read_regular(root: Path, relative: str, *, label: str) -> bytes:
    try:
        path = PurePosixPath(relative)
    except (TypeError, ValueError) as error:
        raise ReleaseManifestReconciliationError("reconciliation-input-invalid", f"{label} is unsafe") from error
    if path.is_absolute() or not path.parts or any(part in {"", ".", ".."} for part in path.parts):
        _reject("reconciliation-input-invalid", f"{label} must be a safe repository-relative path")
    cursor = root
    try:
        for part in path.parts:
            cursor /= part
            if cursor.is_symlink():
                _reject("reconciliation-input-invalid", f"{label} has a symlinked ancestor")
        if not cursor.is_file():
            _reject("reconciliation-input-invalid", f"{label} is unavailable")
        return cursor.read_bytes()
    except ReleaseManifestReconciliationError:
        raise
    except OSError as error:
        raise ReleaseManifestReconciliationError("reconciliation-input-invalid", f"{label} is unreadable") from error


def _git_output(root: Path, arguments: list[str], *, text: bool) -> str | bytes:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *arguments],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
            text=text,
        )
    except OSError as error:
        raise ReleaseManifestReconciliationError("reconciliation-git-unavailable", "Git proof is unavailable") from error
    if result.returncode != 0:
        raise ReleaseManifestReconciliationError("reconciliation-git-unavailable", "Git proof command failed")
    return result.stdout


def _git_proof(root: Path, manifest_ref: str) -> dict[str, str]:
    commit = str(_git_output(root, ["rev-parse", "HEAD"], text=True)).strip()
    blob_oid = str(_git_output(root, ["rev-parse", f"HEAD:{manifest_ref}"], text=True)).strip()
    committed = _git_output(root, ["show", f"HEAD:{manifest_ref}"], text=False)
    if _HEX.fullmatch(commit) is None or _HEX.fullmatch(blob_oid) is None or not isinstance(committed, bytes):
        _reject("reconciliation-git-invalid", "Git HEAD/blob proof has an invalid identity")
    return {
        "commit": commit,
        "blob_oid": blob_oid,
        "path": manifest_ref,
        "sha256": hashlib.sha256(committed).hexdigest(),
    }


def _source_facts(root: Path, manifest_ref: str) -> tuple[str, str]:
    try:
        base = load_release_manifest_refresh_base(root)
        _, admission = derive_release_graph_admission(root)
    except (OSError, TypeError, ValueError, SelectedRouteError, ReleaseSourceAdmissionError) as error:
        raise ReleaseManifestReconciliationError(
            "reconciliation-source-stale", "current D572 refresh-base admission is unavailable"
        ) from error
    if not isinstance(base, dict) or base.get("manifest_ref") != manifest_ref:
        _reject("reconciliation-source-stale", "refresh-base validator returned a different Manifest carrier")
    return canonical_digest(base), _source_frontier_digest(admission)


def _validate_plan(value: Any, root: Path) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        _reject("reconciliation-plan-invalid", "reconciliation plan must be an object")
    fields = set(value)
    if fields - {"mode", *_PLAN_FIELDS} or not _PLAN_FIELDS <= fields:
        _reject("reconciliation-plan-invalid", "reconciliation plan has unsupported or missing fields")
    if value.get("mode", "plan") != "plan" or value["operation"] != "reconciliation":
        _reject("reconciliation-plan-invalid", "plan operation must be reconciliation")
    manifest_ref = value["manifest_ref"]
    if manifest_ref != selected_manifest_ref(root):
        _reject("reconciliation-plan-invalid", "plan targets a different Manifest carrier")
    state = value["observation_state"]
    if state not in {"required", "already_recorded"}:
        _reject("reconciliation-plan-invalid", "plan observation state is invalid")
    for field in ("git_head_commit", "git_blob_oid", "latest_event_id", "observation_event_id"):
        _safe_event_id(value[field], field)
    for field in (
        "observed_raw_sha256", "git_blob_sha256", "latest_event_digest", "latest_result_sha256",
        "refresh_base_digest", "source_frontier_digest",
    ):
        _digest(value[field], field)
    for field in ("latest_version", "next_version"):
        if type(value[field]) is not int or value[field] < 1:
            _reject("reconciliation-plan-invalid", f"{field} must be a positive integer")
    if state == "required" and value["next_version"] != value["latest_version"] + 1:
        _reject("reconciliation-plan-invalid", "required observation must advance the predecessor revision by one")
    if state == "already_recorded" and value["next_version"] != value["latest_version"]:
        _reject("reconciliation-plan-invalid", "already-recorded observation must retain its recorded revision")
    return {
        "mode": "plan",
        "operation": "reconciliation",
        "manifest_ref": manifest_ref,
        "observed_raw_sha256": value["observed_raw_sha256"],
        "git_head_commit": value["git_head_commit"],
        "git_blob_oid": value["git_blob_oid"],
        "git_blob_sha256": value["git_blob_sha256"],
        "latest_event_id": value["latest_event_id"],
        "latest_event_digest": value["latest_event_digest"],
        "latest_result_sha256": value["latest_result_sha256"],
        "latest_version": value["latest_version"],
        "next_version": value["next_version"],
        "observation_event_id": value["observation_event_id"],
        "refresh_base_digest": value["refresh_base_digest"],
        "source_frontier_digest": value["source_frontier_digest"],
        "observation_state": state,
    }


def _observation_event_id(plan: Mapping[str, Any]) -> str:
    identity = {
        "action_id": ACTION_ID,
        "manifest_ref": plan["manifest_ref"],
        "observed_raw_sha256": plan["observed_raw_sha256"],
        "predecessor_event_id": plan["latest_event_id"],
        "predecessor_version": plan["latest_version"],
        "predecessor_sha256": plan["latest_result_sha256"],
    }
    return _OBSERVATION_PREFIX + work_journal.canonical_json_digest(identity)


def _history(root: Path, manifest_ref: str) -> list[dict[str, Any]]:
    journal_root = root / work_journal.configured_journal_root(root)
    records: list[dict[str, Any]] = []
    try:
        carriers = sorted(journal_root.glob("*.ndjson")) if journal_root.exists() else []
        for carrier in carriers:
            if carrier.is_symlink() or not carrier.is_file():
                continue
            try:
                _, raw_records = work_journal._carrier_records(carrier)
            except (OSError, RuntimeError, work_journal.WorkJournalError) as error:
                raise ReleaseManifestReconciliationError(
                    "reconciliation-history-invalid", "Journal carrier is unreadable or malformed"
                ) from error
            for line, raw in enumerate(raw_records, start=1):
                result = raw.get("result") if isinstance(raw, dict) else None
                if not isinstance(result, dict) or result.get("path") != manifest_ref:
                    continue
                if raw.get("schema_version") != 3 or raw.get("kind") not in {
                    "governed_project_state", "governed_project_change",
                }:
                    _reject("reconciliation-history-invalid", "target history contains an unsupported Journal event")
                try:
                    event = work_journal.validate_sealed_event(raw)
                except work_journal.WorkJournalError as error:
                    raise ReleaseManifestReconciliationError(
                        "reconciliation-history-invalid", "target history contains an invalid sealed event"
                    ) from error
                result = event.get("result")
                if not isinstance(result, dict) or result.get("state") != "present":
                    _reject("reconciliation-history-invalid", "target history must contain present carrier states")
                version = result.get("version")
                if type(version) is not int or version < 1:
                    _reject("reconciliation-history-invalid", "target history has an invalid carrier revision")
                records.append({
                    "event": event,
                    "carrier": carrier,
                    "line": line,
                    "version": version,
                    "sha256": result["sha256"],
                })
    except ReleaseManifestReconciliationError:
        raise
    except OSError as error:
        raise ReleaseManifestReconciliationError("reconciliation-history-invalid", "Journal history is unreadable") from error
    if not records:
        _reject("reconciliation-history-invalid", "no target-specific Journal history exists")
    records.sort(key=lambda item: (item["version"], str(item["event"]["event_id"])))
    by_version: dict[int, dict[str, Any]] = {}
    for item in records:
        prior = by_version.get(item["version"])
        if prior is not None:
            _reject("reconciliation-history-conflict", "target history has duplicate carrier revisions")
        by_version[item["version"]] = item
    versions = sorted(by_version)
    if versions != list(range(1, versions[-1] + 1)):
        _reject("reconciliation-history-invalid", "target history has a missing carrier revision")
    ordered = [by_version[version] for version in versions]
    for prior, item in zip(ordered, ordered[1:]):
        event = item["event"]
        if event.get("event") == "completed":
            if event.get("previous_result_event") != prior["event"]["event_id"]:
                _reject("reconciliation-history-invalid", "completed target history does not link its predecessor")
        elif event.get("event") == "recovered":
            evidence = event.get("recovery_evidence")
            carrier = evidence.get("carrier") if isinstance(evidence, dict) else None
            if not isinstance(carrier, dict) or set(carrier) != {
                "identity", "kind", "filename", "version", "sha256",
                "predecessor_event_id", "predecessor_version", "predecessor_sha256",
            }:
                _reject("reconciliation-history-invalid", "recovered target history lacks its predecessor witness")
            if (
                carrier["predecessor_event_id"] != prior["event"]["event_id"]
                or carrier["predecessor_version"] != prior["version"]
                or carrier["predecessor_sha256"] != prior["sha256"]
            ):
                _reject("reconciliation-history-invalid", "recovered target history has a false predecessor witness")
        else:
            _reject("reconciliation-history-invalid", "target history has an unsupported lifecycle event")
    return ordered


def _pending_root(root: Path) -> Path:
    return root / work_journal.configured_runtime_root(root) / "state" / "work_journal" / "pending"


def _pending_for_target(root: Path, manifest_ref: str) -> tuple[list[tuple[str, dict[str, Any], dict[str, Any]]], list[str]]:
    own: list[tuple[str, dict[str, Any], dict[str, Any]]] = []
    competing: list[str] = []
    pending_root = _pending_root(root)
    if not pending_root.exists():
        return own, competing
    for path in sorted(pending_root.glob("*.json")):
        if path.is_symlink() or not path.is_file():
            continue
        try:
            pending, event, context, _ = work_journal._read_pending_event(root, path.stem)
        except work_journal.WorkJournalError as error:
            raise ReleaseManifestReconciliationError(
                "reconciliation-pending-invalid", "a pending Journal observation is invalid"
            ) from error
        refs = [pending.get("result_ref"), *pending.get("effect_refs", [])]
        if manifest_ref not in refs:
            continue
        diagnostic = pending.get("diagnostic")
        if isinstance(diagnostic, str) and diagnostic.startswith(_PENDING_PREFIX):
            own.append((path.stem, pending, event))
        else:
            competing.append(path.stem)
    return own, competing


def _read_facts(root: Path, *, allow_own_pending: bool = False) -> dict[str, Any]:
    manifest_ref = selected_manifest_ref(root)
    raw = _read_regular(root, manifest_ref, label="selected Manifest carrier")
    observed = hashlib.sha256(raw).hexdigest()
    git = _git_proof(root, manifest_ref)
    if git["sha256"] != observed:
        _reject("reconciliation-dirty-input", "physical Manifest bytes differ from the exact Git HEAD blob")
    refresh_base_digest, source_frontier_digest = _source_facts(root, manifest_ref)
    history = _history(root, manifest_ref)
    own, competing = _pending_for_target(root, manifest_ref)
    if competing:
        _reject("reconciliation-pending-publication", "a competing publication intent is pending for the Manifest")
    if own and not allow_own_pending:
        _reject("reconciliation-pending-observation", "an observation is already pending recording")
    return {
        "manifest_ref": manifest_ref,
        "observed_raw_sha256": observed,
        "git": git,
        "refresh_base_digest": refresh_base_digest,
        "source_frontier_digest": source_frontier_digest,
        "history": history,
        "own_pending": own,
    }


def _already_recorded(plan: Mapping[str, Any], latest: Mapping[str, Any]) -> bool:
    event = latest["event"]
    result = event.get("result")
    return (
        event.get("event_id") == plan["observation_event_id"]
        and event.get("event") == "recovered"
        and event.get("kind") == "governed_project_state"
        and result == {
            "state": "present",
            "filename": Path(plan["manifest_ref"]).name,
            "version": plan["next_version"],
            "path": plan["manifest_ref"],
            "sha256": plan["observed_raw_sha256"],
        }
    )


def _event_matches_plan(event: Mapping[str, Any], plan: Mapping[str, Any]) -> bool:
    if not _already_recorded(plan, {"event": event}):
        return False
    evidence = event.get("recovery_evidence")
    if not isinstance(evidence, dict) or set(evidence) != {"git", "carrier"}:
        return False
    git = evidence.get("git")
    carrier = evidence.get("carrier")
    if not isinstance(git, dict) or git != {
        "commit": plan["git_head_commit"],
        "blob_oid": plan["git_blob_oid"],
        "path": plan["manifest_ref"],
        "sha256": plan["observed_raw_sha256"],
    }:
        return False
    if not isinstance(carrier, dict) or set(carrier) != {
        "identity", "kind", "filename", "version", "sha256",
        "predecessor_event_id", "predecessor_version", "predecessor_sha256",
    }:
        return False
    return carrier == {
        "identity": "selected_workflow_bindings",
        "kind": "file",
        "filename": Path(plan["manifest_ref"]).name,
        "version": plan["next_version"],
        "sha256": plan["observed_raw_sha256"],
        "predecessor_event_id": plan["latest_event_id"],
        "predecessor_version": plan["latest_version"],
        "predecessor_sha256": plan["latest_result_sha256"],
    }


def _plan_from_facts(facts: Mapping[str, Any]) -> dict[str, Any]:
    history = facts["history"]
    latest = history[-1]
    latest_event = latest["event"]
    state = "required"
    next_version = latest["version"] + 1
    observation_event_id = _observation_event_id({
        "manifest_ref": facts["manifest_ref"],
        "observed_raw_sha256": facts["observed_raw_sha256"],
        "latest_event_id": latest_event["event_id"],
        "latest_version": latest["version"],
        "latest_result_sha256": latest["sha256"],
    })
    if latest["sha256"] == facts["observed_raw_sha256"]:
        if latest_event.get("event") != "recovered" or latest["version"] <= 1:
            _reject(
                "reconciliation-not-required",
                "the exact current Git-backed bytes already have a non-reconciliation Journal state",
            )
        predecessor = history[-2]
        candidate = {
            "manifest_ref": facts["manifest_ref"],
            "observed_raw_sha256": facts["observed_raw_sha256"],
            "latest_event_id": predecessor["event"]["event_id"],
            "latest_version": predecessor["version"],
            "latest_result_sha256": predecessor["sha256"],
            "next_version": latest["version"],
            "observation_event_id": _observation_event_id({
                "manifest_ref": facts["manifest_ref"],
                "observed_raw_sha256": facts["observed_raw_sha256"],
                "latest_event_id": predecessor["event"]["event_id"],
                "latest_version": predecessor["version"],
                "latest_result_sha256": predecessor["sha256"],
            }),
        }
        if _event_matches_plan(latest_event, {
            **candidate,
            "git_head_commit": facts["git"]["commit"],
            "git_blob_oid": facts["git"]["blob_oid"],
        }):
            state = "already_recorded"
            next_version = latest["version"]
            observation_event_id = latest_event["event_id"]
        else:
            _reject("reconciliation-history-invalid", "current recovered state has unequal predecessor evidence")
    plan = {
        "mode": "plan",
        "operation": "reconciliation",
        "manifest_ref": facts["manifest_ref"],
        "observed_raw_sha256": facts["observed_raw_sha256"],
        "git_head_commit": facts["git"]["commit"],
        "git_blob_oid": facts["git"]["blob_oid"],
        "git_blob_sha256": facts["git"]["sha256"],
        "latest_event_id": latest_event["event_id"],
        "latest_event_digest": latest_event["event_digest"],
        "latest_result_sha256": latest["sha256"],
        "latest_version": latest["version"],
        "next_version": next_version,
        "observation_event_id": observation_event_id,
        "refresh_base_digest": facts["refresh_base_digest"],
        "source_frontier_digest": facts["source_frontier_digest"],
        "observation_state": state,
    }
    return _validate_plan(plan, _root(facts["root"]))


def plan_release_manifest_reconciliation(project_root: str | Path) -> dict[str, Any]:
    """Return a read-only plan for one exact current-state observation."""
    root = _root(project_root)
    facts = _read_facts(root)
    facts = {**facts, "root": root}
    return _plan_from_facts(facts)


def _snapshot(context: ReconciliationAuthorizationContext) -> tuple[object, ...]:
    if type(context) is not ReconciliationAuthorizationContext:
        _reject("reconciliation-context-forged", "context has the wrong type")
    issued = _issued.get(id(context))
    if issued is None or issued[0]() is not context:
        _reject("reconciliation-context-forged", "context was not issued by this trusted host")
    values = (
        context._root,
        tuple(sorted(context._plan.items())),
        context._operator_name,
        context._journal_author,
        context._llm_session,
        context._authorization_ref,
        context._purpose,
        context._pending_event_id,
        context._pending_event_digest,
    )
    if values != issued[1]:
        _reject("reconciliation-context-forged", "context was altered after issuance")
    return values


def _issue_context(
    root: Path,
    plan: Mapping[str, Any],
    *,
    operator_name: str,
    journal_author: str,
    llm_session: tuple[str, str],
    authorization_ref: str,
    purpose: str,
    pending_event_id: str | None = None,
    pending_event_digest: str | None = None,
) -> ReconciliationAuthorizationContext:
    context = object.__new__(ReconciliationAuthorizationContext)
    object.__setattr__(context, "_root", root.as_posix())
    object.__setattr__(context, "_plan", MappingProxyType(dict(plan)))
    object.__setattr__(context, "_operator_name", operator_name)
    object.__setattr__(context, "_journal_author", journal_author)
    object.__setattr__(context, "_llm_session", llm_session)
    object.__setattr__(context, "_authorization_ref", authorization_ref)
    object.__setattr__(context, "_purpose", purpose)
    object.__setattr__(context, "_pending_event_id", pending_event_id)
    object.__setattr__(context, "_pending_event_digest", pending_event_digest)
    values = (
        context._root,
        tuple(sorted(context._plan.items())),
        context._operator_name,
        context._journal_author,
        context._llm_session,
        context._authorization_ref,
        context._purpose,
        context._pending_event_id,
        context._pending_event_digest,
    )
    identifier = id(context)
    _issued[identifier] = (weakref.ref(context, lambda _reference: _issued.pop(identifier, None)), values)
    return context


def authorize_operator_reconciliation(
    project_root: str | Path,
    plan: Mapping[str, Any],
    *,
    operator_name: str,
    journal_author: str,
    llm_session: Mapping[str, str],
    authorization_ref: str,
) -> ReconciliationAuthorizationContext:
    """Issue one opaque authority for one exact observation plan."""
    root = _root(project_root)
    supplied = _validate_plan(plan, root)
    expected = plan_release_manifest_reconciliation(root)
    if supplied != expected:
        _reject("reconciliation-plan-stale", "plan differs from the current Git-backed observation")
    try:
        operator = _operator_row(root, operator_name)
        author, session = _journal_context(operator, journal_author, llm_session)
        reference = _safe_ref(authorization_ref, "authorization_ref")
    except (ReleaseManifestAuthorizationError, OSError, TypeError, ValueError) as error:
        raise ReleaseManifestReconciliationError("reconciliation-authorization-invalid", str(error)) from error
    return _issue_context(
        root, supplied, operator_name=operator_name, journal_author=author, llm_session=session,
        authorization_ref=reference, purpose="reconciliation",
    )


def _pending_metadata(root: Path, pending_event_id: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    try:
        pending, event, context, _ = work_journal._read_pending_event(root, pending_event_id)
    except work_journal.WorkJournalError as error:
        raise ReleaseManifestReconciliationError(
            "reconciliation-pending-invalid", "sealed observation pending evidence is unavailable"
        ) from error
    diagnostic = pending.get("diagnostic")
    if not isinstance(diagnostic, str) or not diagnostic.startswith(_PENDING_PREFIX):
        _reject("reconciliation-pending-invalid", "pending evidence does not belong to reconciliation")
    try:
        metadata = json.loads(diagnostic.removeprefix(_PENDING_PREFIX))
    except json.JSONDecodeError as error:
        raise ReleaseManifestReconciliationError("reconciliation-pending-invalid", "pending diagnostic is invalid") from error
    if not isinstance(metadata, dict) or set(metadata) != {"plan", "event_id", "event_digest", "event_payload_sha256"}:
        _reject("reconciliation-pending-invalid", "pending diagnostic has unsupported fields")
    plan = _validate_plan(metadata["plan"], root)
    if metadata["event_id"] != pending_event_id or event.get("event_id") != pending_event_id:
        _reject("reconciliation-pending-invalid", "pending event identity differs from its diagnostic")
    if metadata["event_digest"] != event.get("event_digest"):
        _reject("reconciliation-pending-invalid", "pending event digest differs from its diagnostic")
    if metadata["event_payload_sha256"] != hashlib.sha256(
        work_journal.canonical_json_bytes(event) + b"\n"
    ).hexdigest():
        _reject("reconciliation-pending-invalid", "pending event bytes differ from its diagnostic")
    if pending.get("result_ref") != plan["manifest_ref"] or pending.get("effect_refs") != []:
        _reject("reconciliation-pending-invalid", "reconciliation pending evidence has a Manifest effect reference")
    _validate_observation_event(event, plan)
    return plan, event, context


def _validate_observation_event(event: Mapping[str, Any], plan: Mapping[str, Any]) -> None:
    try:
        sealed = work_journal.validate_sealed_event(event)
    except work_journal.WorkJournalError as error:
        raise ReleaseManifestReconciliationError("reconciliation-event-invalid", "observation event is not sealed") from error
    if not _event_matches_plan(sealed, plan):
        _reject("reconciliation-event-invalid", "observation event does not match the exact plan")


def authorize_operator_reconciliation_recovery(
    project_root: str | Path,
    pending_event_id: str,
    *,
    operator_name: str,
    journal_author: str,
    llm_session: Mapping[str, str],
    authorization_ref: str,
) -> ReconciliationAuthorizationContext:
    """Issue recording-only authority for one existing sealed observation."""
    root = _root(project_root)
    if not isinstance(pending_event_id, str) or not pending_event_id:
        _reject("reconciliation-pending-invalid", "pending event identity is required")
    plan, event, _ = _pending_metadata(root, pending_event_id)
    try:
        operator = _operator_row(root, operator_name)
        author, session = _journal_context(operator, journal_author, llm_session)
        reference = _safe_ref(authorization_ref, "authorization_ref")
    except (ReleaseManifestAuthorizationError, OSError, TypeError, ValueError) as error:
        raise ReleaseManifestReconciliationError("reconciliation-authorization-invalid", str(error)) from error
    return _issue_context(
        root, plan, operator_name=operator_name, journal_author=author, llm_session=session,
        authorization_ref=reference, purpose="reconciliation-recovery", pending_event_id=pending_event_id,
        pending_event_digest=str(event["event_digest"]),
    )


def _event_receipt(root: Path, event: Mapping[str, Any]) -> dict[str, Any] | None:
    try:
        value = work_journal._existing_receipt(root, event)
    except work_journal.WorkJournalError as error:
        raise ReleaseManifestReconciliationError("reconciliation-recording-invalid", "Journal receipt is invalid") from error
    return dict(value) if isinstance(value, Mapping) else None


@contextmanager
def _carrier_lock(root: Path, manifest_ref: str):
    entered = False
    try:
        with work_journal._event_lock(root, "release-manifest-carrier:" + manifest_ref):
            entered = True
            yield
    except (OSError, RuntimeError, work_journal.WorkJournalError) as error:
        if entered:
            raise
        raise ReleaseManifestReconciliationError(
            "reconciliation-lock-unavailable", "the Release Manifest carrier Journal lock is unavailable"
        ) from error


def _pending_path(root: Path, event_id: str) -> Path:
    return _pending_root(root) / f"{event_id}.json"


def _recheck_context(context: ReconciliationAuthorizationContext, root: Path, plan: Mapping[str, Any], *, purpose: str) -> None:
    snapshot = _snapshot(context)
    if snapshot[0] != root.as_posix() or dict(snapshot[1]) != dict(plan) or snapshot[6] != purpose:
        _reject("reconciliation-context-stale", "trusted reconciliation context does not bind this exact plan")
    try:
        operator = _operator_row(root, snapshot[2])
        _journal_context(operator, snapshot[3], {"app": snapshot[4][0], "uuid": snapshot[4][1]})
    except (ReleaseManifestAuthorizationError, OSError, TypeError, ValueError) as error:
        raise ReleaseManifestReconciliationError("reconciliation-authorization-invalid", str(error)) from error


def _build_observation_event(root: Path, plan: Mapping[str, Any], context: ReconciliationAuthorizationContext) -> dict[str, Any]:
    snapshot = _snapshot(context)
    moment = dt.datetime.now().astimezone()
    if moment.tzinfo is None or moment.utcoffset() is None:
        _reject("reconciliation-time-invalid", "Journal observation time must be timezone-aware")
    evidence = {
        "git": {
            "commit": plan["git_head_commit"],
            "blob_oid": plan["git_blob_oid"],
            "path": plan["manifest_ref"],
            "sha256": plan["observed_raw_sha256"],
        },
        "carrier": {
            "identity": "selected_workflow_bindings",
            "kind": "file",
            "filename": Path(plan["manifest_ref"]).name,
            "version": plan["next_version"],
            "sha256": plan["observed_raw_sha256"],
            "predecessor_event_id": plan["latest_event_id"],
            "predecessor_version": plan["latest_version"],
            "predecessor_sha256": plan["latest_result_sha256"],
        },
    }
    event = {
        "event_id": plan["observation_event_id"],
        "schema_version": 3,
        "action_id": ACTION_ID,
        "event": "recovered",
        "kind": "governed_project_state",
        "subject_kind": "file",
        "author": snapshot[3],
        "occurred_at": moment.isoformat(timespec="seconds"),
        "llm_session": {"app": snapshot[4][0], "uuid": snapshot[4][1]},
        "structural_scope": STRUCTURAL_SCOPE,
        "result": {
            "state": "present",
            "filename": Path(plan["manifest_ref"]).name,
            "version": plan["next_version"],
            "path": plan["manifest_ref"],
            "sha256": plan["observed_raw_sha256"],
        },
        "recovery_evidence": evidence,
    }
    return work_journal.with_event_digest(event)


def _pending_diagnostic(plan: Mapping[str, Any], event: Mapping[str, Any]) -> str:
    metadata = {
        "plan": dict(plan),
        "event_id": event["event_id"],
        "event_digest": event["event_digest"],
        "event_payload_sha256": hashlib.sha256(work_journal.canonical_json_bytes(event) + b"\n").hexdigest(),
    }
    return _PENDING_PREFIX + work_journal.canonical_json_bytes(metadata).decode("utf-8")


def _blocked(plan: Mapping[str, Any], message: str) -> dict[str, Any]:
    return {"mode": "execute", "disposition": "blocked", "reconciliation_requirement": message, **dict(plan)}


def _facts_match_plan(facts: Mapping[str, Any], plan: Mapping[str, Any]) -> bool:
    latest = facts["history"][-1]
    return _facts_static_match_plan(facts, plan) and (
        latest["event"]["event_id"] == plan["latest_event_id"]
        and latest["event"]["event_digest"] == plan["latest_event_digest"]
        and latest["version"] == plan["latest_version"]
        and latest["sha256"] == plan["latest_result_sha256"]
    )


def _facts_static_match_plan(facts: Mapping[str, Any], plan: Mapping[str, Any]) -> bool:
    return (
        facts["observed_raw_sha256"] == plan["observed_raw_sha256"]
        and facts["git"]["commit"] == plan["git_head_commit"]
        and facts["git"]["blob_oid"] == plan["git_blob_oid"]
        and facts["git"]["sha256"] == plan["git_blob_sha256"]
        and facts["refresh_base_digest"] == plan["refresh_base_digest"]
        and facts["source_frontier_digest"] == plan["source_frontier_digest"]
    )


def _already_recorded_current(latest: Mapping[str, Any], plan: Mapping[str, Any]) -> bool:
    event = latest["event"]
    if (
        event.get("event_id") != plan["observation_event_id"]
        or latest["version"] != plan["next_version"]
        or latest["sha256"] != plan["observed_raw_sha256"]
    ):
        return False
    if event.get("event") == "completed":
        return True
    if event.get("event") == "recovered" and latest["version"] == 1:
        return True
    return _event_matches_plan(event, plan)


def _bound_pending(
    root: Path,
    own: list[tuple[str, dict[str, Any], dict[str, Any]]],
    plan: Mapping[str, Any],
) -> tuple[str, dict[str, Any]] | None:
    if len(own) > 1:
        _reject("reconciliation-pending-conflict", "multiple reconciliation observations are pending")
    if not own:
        return None
    pending_id = own[0][0]
    pending_plan, pending_event, _ = _pending_metadata(root, pending_id)
    if pending_plan != dict(plan) or not _event_matches_plan(pending_event, plan):
        _reject("reconciliation-pending-conflict", "pending observation is not bound to this exact plan")
    return pending_id, pending_event


def reconcile_release_manifest_history(
    project_root: str | Path,
    *,
    execute: bool = False,
    authorization: Any = None,
) -> dict[str, Any]:
    """Observe the exact current binding state, never replacing Manifest bytes."""
    if type(execute) is not bool:
        raise ReleaseManifestReconciliationError("reconciliation-input-invalid", "execute must be a boolean")
    root = _root(project_root)
    if not execute:
        return plan_release_manifest_reconciliation(root)
    if not isinstance(authorization, ReconciliationAuthorizationContext):
        _reject("reconciliation-authorization-invalid", "execute requires an opaque host-created context")
    snapshot = _snapshot(authorization)
    plan = _validate_plan(dict(snapshot[1]), root)
    _recheck_context(authorization, root, plan, purpose="reconciliation")
    try:
        with _carrier_lock(root, plan["manifest_ref"]):
            facts = _read_facts(root, allow_own_pending=True)
            history = facts["history"]
            latest = history[-1]
            own, competing = _pending_for_target(root, plan["manifest_ref"])
            if competing:
                return _blocked(plan, "a competing publication intent is pending for the Manifest")
            pending = _bound_pending(root, own, plan)
            if not _facts_static_match_plan(facts, plan):
                return _blocked(plan, "Git, Manifest, source frontier, or target history changed after authorization")
            if _event_matches_plan(latest["event"], plan):
                receipt = _event_receipt(root, latest["event"])
                if pending is not None:
                    try:
                        receipt = work_journal.recover_pending_event(root, pending[0])
                    except (OSError, RuntimeError, TypeError, ValueError, work_journal.WorkJournalError) as error:
                        return {
                            "mode": "execute", "disposition": "recording_required",
                            "pending_event_id": pending[0], "recording_requirement": str(error), **plan,
                        }
                result = {
                    "mode": "execute", "disposition": "already_recorded",
                    "event_id": latest["event"]["event_id"], **plan,
                }
                if receipt:
                    result["recording_ref"] = "journal:" + str(receipt["event_id"])
                return result
            if not _facts_match_plan(facts, plan):
                return _blocked(plan, "Git, Manifest, source frontier, or target history changed after authorization")
            if plan["observation_state"] == "already_recorded":
                if not _already_recorded_current(latest, plan):
                    return _blocked(plan, "the authorized already-recorded observation is no longer current")
                receipt = _event_receipt(root, latest["event"])
                if pending is not None:
                    try:
                        receipt = work_journal.recover_pending_event(root, pending[0])
                    except (OSError, RuntimeError, TypeError, ValueError, work_journal.WorkJournalError) as error:
                        return {
                            "mode": "execute", "disposition": "recording_required",
                            "pending_event_id": pending[0], "recording_requirement": str(error), **plan,
                        }
                result = {
                    "mode": "execute", "disposition": "already_recorded",
                    "event_id": latest["event"]["event_id"], **plan,
                }
                if receipt:
                    result["recording_ref"] = "journal:" + str(receipt["event_id"])
                return result
            if pending is not None:
                return {
                    "mode": "execute", "disposition": "recording_required", "pending_event_id": pending[0], **plan,
                }
            event = _build_observation_event(root, plan, authorization)
            _validate_observation_event(event, plan)
            try:
                occurred = dt.datetime.fromisoformat(str(event["occurred_at"]))
                timezone = occurred.tzname() or occurred.strftime("%z")
                append_context = work_journal.seal_append_context(
                    root, event, author=authorization.journal_author,
                    local_date=occurred.date().isoformat(), timezone=timezone,
                )
                work_journal.store_pending_event(
                    root, event, append_context,
                    result_ref=plan["manifest_ref"], effect_refs=[],
                    diagnostic=_pending_diagnostic(plan, event),
                    retry_linkage=work_journal.canonical_json_digest(dict(plan)),
                )
            except (OSError, RuntimeError, TypeError, ValueError, work_journal.WorkJournalError) as error:
                return _blocked(plan, str(error))
            try:
                receipts = work_journal.append_sealed_events(
                    root, [event], author=append_context["author"],
                    local_date=append_context["local_date"], timezone=append_context["timezone"],
                    append_context=append_context,
                )
                if not isinstance(receipts, list) or len(receipts) != 1 or receipts[0].get("event_id") != event["event_id"]:
                    raise work_journal.WorkJournalError("invalid-receipt", "observation Journal receipt is incomplete")
                receipt = dict(receipts[0])
                _pending_path(root, str(event["event_id"])).unlink(missing_ok=True)
            except (OSError, RuntimeError, TypeError, ValueError, work_journal.WorkJournalError) as error:
                return {
                    "mode": "execute", "disposition": "recording_required",
                    "pending_event_id": event["event_id"],
                    "recording_requirement": str(error), **plan,
                }
            return {
                "mode": "execute", "disposition": "observed", "event_id": event["event_id"],
                "recording_ref": "journal:" + str(receipt["event_id"]), **plan,
            }
    except ReleaseManifestReconciliationError as error:
        return _blocked(plan, str(error))


def recover_release_manifest_reconciliation(
    project_root: str | Path,
    pending_event_id: str,
    authorization: Any,
) -> dict[str, Any]:
    """Finalize one exact pending observation without creating a new event."""
    root = _root(project_root)
    if not isinstance(authorization, ReconciliationAuthorizationContext):
        _reject("reconciliation-authorization-invalid", "recovery requires an opaque host-created context")
    snapshot = _snapshot(authorization)
    if snapshot[6] != "reconciliation-recovery" or snapshot[7] != pending_event_id:
        _reject("reconciliation-context-stale", "recovery context does not bind this pending observation")
    plan = _validate_plan(dict(snapshot[1]), root)
    pending_plan, pending_event, _ = _pending_metadata(root, pending_event_id)
    if pending_plan != plan or snapshot[8] != pending_event["event_digest"]:
        _reject("reconciliation-context-stale", "pending observation differs from the authorized event")
    _recheck_context(authorization, root, plan, purpose="reconciliation-recovery")
    try:
        with _carrier_lock(root, plan["manifest_ref"]):
            facts = _read_facts(root, allow_own_pending=True)
            latest = facts["history"][-1]
            if (
                facts["observed_raw_sha256"] != plan["observed_raw_sha256"]
                or facts["git"]["commit"] != plan["git_head_commit"]
                or facts["git"]["blob_oid"] != plan["git_blob_oid"]
                or facts["git"]["sha256"] != plan["git_blob_sha256"]
                or facts["refresh_base_digest"] != plan["refresh_base_digest"]
                or facts["source_frontier_digest"] != plan["source_frontier_digest"]
            ):
                return _blocked(plan, "Git, Manifest, or source frontier changed before recording recovery")
            if latest["event"].get("event_id") == pending_event_id:
                if not _event_matches_plan(latest["event"], plan):
                    return _blocked(plan, "recorded observation does not match the sealed pending event")
            elif (
                latest["event"].get("event_id") != plan["latest_event_id"]
                or latest["event"].get("event_digest") != plan["latest_event_digest"]
                or latest["version"] != plan["latest_version"]
                or latest["sha256"] != plan["latest_result_sha256"]
            ):
                return _blocked(plan, "target history changed before recording recovery")
            try:
                receipt = work_journal.recover_pending_event(root, pending_event_id)
            except (OSError, RuntimeError, TypeError, ValueError, work_journal.WorkJournalError) as error:
                return {
                    "mode": "recover", "disposition": "recording_required",
                    "pending_event_id": pending_event_id, "recording_requirement": str(error), **plan,
                }
            return {
                "mode": "recover", "disposition": "recovered", "event_id": pending_event_id,
                "recording_ref": "journal:" + str(receipt["event_id"]), **plan,
            }
    except ReleaseManifestReconciliationError as error:
        return _blocked(plan, str(error))


__all__ = [
    "ReconciliationAuthorizationContext",
    "ReleaseManifestReconciliationError",
    "authorize_operator_reconciliation",
    "authorize_operator_reconciliation_recovery",
    "plan_release_manifest_reconciliation",
    "reconcile_release_manifest_history",
    "recover_release_manifest_reconciliation",
]
