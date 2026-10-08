"""Observed, recoverable selector-first full-Framework and local ca promotion.

A durable private intent precedes exposure. Selector and Skill are separate
effects: a partial publication stays pending and only the exact intent resumes.
No hooks, configuration, Docker command, rollback or image removal is performed.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
import tomllib
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Literal

from release_contract import PROJECT_SKILL_TARGET, REQUIRED_ENGINE_SOURCE_PREFIXES, ReleaseContractError, ValidatedCandidate, canonical_json
from release_handoff import (
    CANONICAL_SOURCE_RELATIVE, CURRENT_SELECTOR_RELATIVE, PackageRow, SealedCandidateCompilation,
    _file, build_validated_candidate, tree_sha256,
)
from release_image import (
    IMAGE_ID, ImageBuildEvidence, ImageVerificationEvidence,
    read_image_execution_artifacts, verify_bound_image_evidence,
)
from release_e2e_gate import CandidateE2EGateEvidence
from release_full_gate import FullGateEvidence, verify_bound_full_gate_evidence
from release_inventory import persistent_regular_files, refuse_secret_path
from selector_publication_lock import selector_publication_lock
from release_packaging import RUNTIME_ROOT, _read_row, _render_manifest, _verify_release
from release_suite import (
    SuiteGateEvidence, _bootstrap_prior_manifest_is_exact,
    _bootstrap_source_context_is_valid, _safe_path,
)


PROMOTION_ROOT = ".caprmedio_runtime/release_promotion"
INTENT_SCHEMA = "caprmedio.release_version.pending_promotion.v1"


@dataclass(frozen=True)
class PromotionEvidence:
    candidate_snapshot_manifest_sha256: str
    outcome: Literal["promoted", "pending", "recording_uncertain"]
    reason: str
    candidate_image_digest: str
    prior_image_digest: str | None
    prior_release: str
    selected_release_root: str
    framework_engine_root: str
    methodology_root: str
    skill_target: str
    intent_sha256: str
    evidence_root: str
    retained_prior_selector_ref: str
    retained_prior_skill_ref: str | None
    receipt_sha256: str | None = None


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sync(directory: Path) -> None:
    descriptor = os.open(directory, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _write(path: Path, payload: bytes, mode: int = 0o644) -> None:
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    path.chmod(mode)


def _sync_skill(folder: Path) -> None:
    for path in folder.rglob("*"):
        if path.name != ".DS_Store" and path.is_file():
            with path.open("rb") as stream:
                os.fsync(stream.fileno())
    for path in sorted((item for item in folder.rglob("*") if item.is_dir()),
                       key=lambda item: len(item.parts), reverse=True):
        _sync(path)
    _sync(folder)


def _records(root: Path, folder: Path) -> list[dict]:
    _safe_path(root, folder.relative_to(root).as_posix())
    rows = []
    for path in persistent_regular_files(root, folder):
        rows.append({"path": path.relative_to(folder).as_posix(), "sha256": _digest(path.read_bytes()),
                     "mode": path.stat().st_mode & 0o777})
    return rows


def _skill_records(root: Path, folder: Path) -> list[dict]:
    rows = _records(root, folder)
    expected_directories = {str(parent) for row in rows for parent in Path(row["path"]).parents if str(parent) != "."}
    actual_directories = {path.relative_to(folder).as_posix() for path in folder.rglob("*") if path.is_dir()}
    if actual_directories != expected_directories:
        raise ReleaseContractError("release-promotion-skill-ownership-unknown", "Skill contains undeclared directories")
    return rows


def _inputs(candidate, compilation, suite, build, verification, e2e, full_gate) -> str:
    if (not isinstance(candidate, ValidatedCandidate) or not isinstance(compilation, SealedCandidateCompilation)
            or not isinstance(suite, SuiteGateEvidence) or not isinstance(build, ImageBuildEvidence)
            or not isinstance(verification, ImageVerificationEvidence)
            or not isinstance(e2e, CandidateE2EGateEvidence)
            or not isinstance(full_gate, FullGateEvidence)):
        raise ReleaseContractError("release-promotion-input-untrusted", "promotion requires typed internal gate evidence")
    return _digest(canonical_json({"candidate": candidate.manifest.model_dump(mode="json", by_alias=True),
          "authority": candidate.authority.model_dump(mode="json"), "intent": candidate.intent.model_dump(mode="json"),
          "compilation": compilation.model_dump(mode="json"), "suite": asdict(suite),
          "build": asdict(build), "verification": asdict(verification),
          "e2e": asdict(e2e), "full_gate": asdict(full_gate)}))


def _selector(candidate, image: str, context_sha256: str) -> bytes:
    if IMAGE_ID.fullmatch(image) is None or not _bootstrap_source_context_is_valid(context_sha256):
        raise ReleaseContractError("release-promotion-input-untrusted", "promotion requires a verified immutable image context")
    package = f"{RUNTIME_ROOT.as_posix()}/releases/{candidate.manifest.sha256}"
    members = {"candidate_snapshot_manifest_sha256": candidate.manifest.sha256,
               "release": candidate.manifest.sha256, "candidate_release": candidate.manifest.candidate_release,
               "selected_release_root": package, "framework_engine_root": package + "/FRAMEWORK_ENGINE",
               "methodology_root": package + "/METHODOLOGY", "candidate_image_digest": image,
               "candidate_image_context_sha256": context_sha256}
    return ("schema_version = 1\n" + "".join(f"{key} = {json.dumps(value)}\n" for key, value in members.items())).encode()


def _prior_image(selector: bytes) -> str | None:
    parsed = tomllib.loads(selector.decode())
    values = {mapping[key] for mapping in (parsed, parsed.get("selection", {})) if isinstance(mapping, dict)
              for key in ("candidate_image_digest", "image_digest") if isinstance(mapping.get(key), str)}
    return next(iter(values)) if len(values) == 1 and IMAGE_ID.fullmatch(next(iter(values))) else None


def _prove_prior_skill(root: Path, candidate: ValidatedCandidate, prior_selector: bytes, skill: Path) -> list[dict]:
    actual = _skill_records(root, skill)
    parsed = tomllib.loads(prior_selector.decode())
    expected_root = f"{RUNTIME_ROOT.as_posix()}/releases/{candidate.authority.executing_release}"
    declared = parsed.get("selected_release_root", parsed.get("release_root", expected_root))
    if declared != expected_root:
        raise ReleaseContractError("release-promotion-skill-ownership-unknown", "prior selector has no exact retained package")
    try:
        package = _safe_path(root, expected_root)
        manifest_bytes = _file(root, f"{expected_root}/manifest.toml").read_bytes()
        manifest = manifest_bytes.decode("utf-8")
        data = tomllib.loads(manifest)
        bootstrap_prior = _bootstrap_prior_manifest_is_exact(
            parsed, manifest_bytes, candidate.authority.executing_release
        )
        if (set(data) != {"schema_version", "candidate_snapshot_manifest_sha256", "package", "files"}
                or data["schema_version"] != 2 or data["package"] != "caprmedio-framework"
                or (data["candidate_snapshot_manifest_sha256"] != candidate.authority.executing_release
                    and not (bootstrap_prior and _bootstrap_source_context_is_valid(
                        data["candidate_snapshot_manifest_sha256"]
                    )))):
            raise ValueError("retained prior manifest is not selected N")
        rows = [PackageRow.model_validate({"resource": row["resource"], "source_path": row["source_path"],
                "destination_path": row["destination"], "sha256": row["sha256"], "mode": row["mode"]}) for row in data["files"]]
        if ({row.resource for row in rows} != {"FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL"}
                or not any(row.destination_path.startswith("METHODOLOGY/compiled/") for row in rows)
                or not any(row.destination_path.startswith("METHODOLOGY/sources/") for row in rows)
                or not {"SKILLS/ca/SKILL.md", "SKILLS/ca/agents/openai.yaml"} <= {row.destination_path for row in rows}
                or any(not any(row.source_path.startswith(prefix) for row in rows if row.resource == "FRAMEWORK_ENGINE")
                       for prefix in REQUIRED_ENGINE_SOURCE_PREFIXES)):
            raise ValueError("retained prior package is incomplete")
        _verify_release(
            package,
            manifest if bootstrap_prior else _render_manifest(candidate.authority.executing_release, rows),
            rows,
        )
        expected = _skill_records(root, package / "SKILLS/ca")
        if actual != expected:
            raise ValueError("public Skill differs from retained N")
    except (OSError, ValueError, RuntimeError) as error:
        raise ReleaseContractError("release-promotion-skill-ownership-unknown", "existing Skill is not proven by the exact retained N package") from error
    return actual


def _gate_artifacts(root, suite, build, verification, e2e, full_gate):
    return {item.evidence_root: _records(root, root / item.evidence_root)
            for item in (suite, build, verification, e2e, full_gate)}


def _pending(root: Path, directory: Path, input_sha: str) -> tuple[dict, str]:
    payload = _file(root, f"{directory.relative_to(root).as_posix()}/intent.json").read_bytes()
    checksum = _file(root, f"{directory.relative_to(root).as_posix()}/intent.sha256").read_text()
    if _digest(payload) != checksum or canonical_json(json.loads(payload)) != payload:
        raise ReleaseContractError("release-promotion-intent-untrusted", "private pending intent is changed or unsealed")
    intent = json.loads(payload)
    if intent.get("schema") != INTENT_SCHEMA or intent.get("inputs_sha256") != input_sha:
        raise ReleaseContractError("release-promotion-retry-mismatch", "only the exact admitted promotion may resume")
    return intent, checksum


def _resume_currentness(root, candidate, compilation, suite, build, verification, e2e, full_gate, intent):
    # Observe current source bytes without pretending the selector still names N.
    observed = build_validated_candidate(root, candidate.intent,
                                        observed_source_frontier_digest=candidate.authority.source_frontier_digest)
    previous = candidate.manifest.model_dump(mode="json", by_alias=True)
    current = observed.manifest.model_dump(mode="json", by_alias=True)
    for key in ("executing_release", "sha256"):
        previous.pop(key)
        current.pop(key)
    if previous != current or compilation.authority != candidate.authority:
        raise ReleaseContractError("release-promotion-currentness-stale", "candidate source or compilation binding changed after admission")
    if (tree_sha256(root, compilation.source_copy_root) != compilation.actual_derived_source_copy_sha256
            or tree_sha256(root, compilation.child_materialization_root) != compilation.actual_compiled_output_sha256):
        raise ReleaseContractError("release-promotion-currentness-stale", "source copy or compiled materialization changed")
    for row in compilation.package_rows:
        _read_row(root, row)
    package = _safe_path(root, intent["selected_release_root"])
    _verify_release(package, _render_manifest(candidate.manifest.sha256, compilation.package_rows), compilation.package_rows)
    verify_bound_full_gate_evidence(candidate, compilation, suite, build, verification, e2e, full_gate)
    if _gate_artifacts(root, suite, build, verification, e2e, full_gate) != intent["gate_artifacts"]:
        raise ReleaseContractError("release-promotion-gates-stale", "original admitted suite or image artifacts changed")
    if _skill_records(root, package / "SKILLS/ca") != intent["candidate_skill"]:
        raise ReleaseContractError("release-promotion-skill-stale", "planned complete Skill changed")
    # Original execution proof is reopened independently of active selection;
    # the current source/package checks above remain this consumer's duty.
    read_image_execution_artifacts(candidate, compilation, suite, build, verification)


def _publish_selector(staged: Path, target: Path) -> None:
    os.replace(staged, target)
    _sync(target.parent)


def _publish_skill(staged: Path, target: Path) -> None:
    if os.path.lexists(target):
        raise ReleaseContractError("release-promotion-skill-ownership-unknown", "public Skill target appeared before publication")
    os.replace(staged, target)
    _sync(target.parent)


def promote_bound_release(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation,
                          suite: SuiteGateEvidence, build: ImageBuildEvidence,
                          verification: ImageVerificationEvidence, *, e2e: CandidateE2EGateEvidence,
                          full_gate: FullGateEvidence) -> PromotionEvidence:
    """Admit once, retain N, then publish selector and exact project Skill."""
    with selector_publication_lock(candidate.project_root):
        return _promote_bound_release_locked(candidate, compilation, suite, build, verification,
                                             e2e=e2e, full_gate=full_gate)


def _promote_bound_release_locked(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation,
                                 suite: SuiteGateEvidence, build: ImageBuildEvidence,
                                 verification: ImageVerificationEvidence, *, e2e: CandidateE2EGateEvidence,
                                 full_gate: FullGateEvidence) -> PromotionEvidence:
    """The existing promotion sequence runs under the sole selector lock."""
    # Typed evidence and the exact input digest are checked before a retry can
    # reopen its admitted intent. Its gates are reopened below before effects;
    # a stale original artifact remains an observed pending recovery.
    input_sha = _inputs(candidate, compilation, suite, build, verification, e2e, full_gate)
    root = Path(candidate.project_root)
    relative = f"{PROMOTION_ROOT}/{candidate.manifest.sha256}"
    directory = root / relative
    target = root / PROJECT_SKILL_TARGET
    selector = root / CURRENT_SELECTOR_RELATIVE
    if directory.exists() or directory.is_symlink():
        _safe_path(root, relative)
        intent, checksum = _pending(root, directory, input_sha)
    else:
        # Image/Unit evidence alone can never create a promotable intent.
        verify_bound_full_gate_evidence(candidate, compilation, suite, build, verification, e2e, full_gate)
        verify_bound_image_evidence(candidate, compilation, suite, build, verification)
        prior = _file(root, CURRENT_SELECTOR_RELATIVE).read_bytes()
        # Refuse unsafe ancestors even when the public target is absent.
        for parent in (root / ".agents", root / ".agents/skills", target):
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                raise ReleaseContractError("release-promotion-skill-ownership-unknown", "public Skill path is unsafe")
        old_skill = _prove_prior_skill(root, candidate, prior, target) if target.exists() else None
        package_relative = f"{RUNTIME_ROOT.as_posix()}/releases/{candidate.manifest.sha256}"
        package = _safe_path(root, package_relative)
        planned = _skill_records(root, package / "SKILLS/ca")
        intent = {"schema": INTENT_SCHEMA, "inputs_sha256": input_sha,
                  "candidate_snapshot_manifest_sha256": candidate.manifest.sha256,
                  "prior_release": candidate.authority.executing_release, "prior_selector_sha256": _digest(prior),
                  "candidate_selector_sha256": _digest(_selector(
                      candidate, verification.candidate_image_digest, build.context_sha256
                  )),
                  "candidate_image_digest": verification.candidate_image_digest, "prior_image_digest": _prior_image(prior),
                  "selected_release_root": package_relative, "prior_skill": old_skill, "candidate_skill": planned,
                  "e2e_receipt_sha256": e2e.receipt_sha256,
                  "e2e_evidence_root": e2e.evidence_root,
                  "full_gate_receipt_sha256": full_gate.receipt_sha256,
                  "full_gate_evidence_root": full_gate.evidence_root,
                  "gate_artifacts": _gate_artifacts(root, suite, build, verification, e2e, full_gate)}
        parent = _safe_path(root, PROMOTION_ROOT, create=True)
        staging = Path(tempfile.mkdtemp(prefix=".admission-", dir=parent))
        try:
            _write(staging / "prior-selector.toml", prior)
            _write(staging / "candidate-selector.toml", _selector(
                candidate, verification.candidate_image_digest, build.context_sha256
            ))
            shutil.copytree(package / "SKILLS/ca", staging / "candidate-skill", copy_function=shutil.copy2)
            if _skill_records(root, staging / "candidate-skill") != planned:
                raise ReleaseContractError("release-promotion-skill-stale", "private staged Skill differs from admitted package")
            _sync_skill(staging / "candidate-skill")
            payload = canonical_json(intent)
            checksum = _digest(payload)
            _write(staging / "intent.json", payload)
            _write(staging / "intent.sha256", checksum.encode())
            _sync(staging)
            os.rename(staging, directory)
            _sync(parent)
        except Exception:
            # Keep any incomplete private admission for inspection; expose nothing.
            raise
    outcome, reason = "pending", "promotion effects remain incomplete"
    try:
        prior = _file(root, f"{relative}/prior-selector.toml").read_bytes()
        planned_selector = _selector(candidate, verification.candidate_image_digest, build.context_sha256)
        if (_digest(prior) != intent["prior_selector_sha256"]
                or _digest(planned_selector) != intent["candidate_selector_sha256"]):
            raise ReleaseContractError("release-promotion-intent-untrusted", "retained selection bytes changed")
        active = _file(root, CURRENT_SELECTOR_RELATIVE).read_bytes()
        if active not in (prior, planned_selector):
            raise ReleaseContractError("release-promotion-selection-stale", "selector is neither the exact prior nor admitted candidate")
        _resume_currentness(root, candidate, compilation, suite, build, verification, e2e, full_gate, intent)
        backup = directory / "prior-skill"
        if target.exists() or target.is_symlink():
            active_skill = _skill_records(root, target)
            if active_skill not in (intent["prior_skill"], intent["candidate_skill"]):
                raise ReleaseContractError("release-promotion-skill-ownership-unknown", "public Skill changed after admission")
        else:
            active_skill = None
        if backup.exists() and _skill_records(root, backup) != intent["prior_skill"]:
            raise ReleaseContractError("release-promotion-skill-ownership-unknown", "retained prior Skill changed")
        if active == prior:
            if active_skill != intent["prior_skill"] or backup.exists():
                raise ReleaseContractError("release-promotion-selection-stale", "prior selection no longer has its exact Skill")
            verify_bound_full_gate_evidence(candidate, compilation, suite, build, verification, e2e, full_gate)
            _publish_selector(directory / "candidate-selector.toml", selector)
        if active_skill != intent["candidate_skill"]:
            if active_skill is not None:
                if backup.exists():
                    raise ReleaseContractError("release-promotion-skill-ownership-unknown", "prior Skill recovery carrier already exists")
                os.rename(target, backup)
                _sync(directory)
                _sync(target.parent)
            elif intent["prior_skill"] is not None and not backup.exists():
                raise ReleaseContractError("release-promotion-skill-ownership-unknown", "missing public prior Skill has no retained recovery copy")
            _safe_path(root, ".agents/skills", create=True)
            staged_skill = directory / "candidate-skill"
            if _skill_records(root, staged_skill) != intent["candidate_skill"]:
                raise ReleaseContractError("release-promotion-skill-stale", "staged candidate Skill changed")
            _publish_skill(staged_skill, target)
        _resume_currentness(root, candidate, compilation, suite, build, verification, e2e, full_gate, intent)
        if (_file(root, CURRENT_SELECTOR_RELATIVE).read_bytes() != planned_selector
                or _skill_records(root, target) != intent["candidate_skill"]):
            raise ReleaseContractError("release-promotion-observation-incomplete", "candidate selector or public Skill is not observed")
        outcome, reason = "promoted", "exact candidate selector and complete project Skill observed"
    except (OSError, ValueError, RuntimeError) as error:
        reason = f"promotion pending: {getattr(error, 'code', type(error).__name__)}"
    evidence = PromotionEvidence(candidate.manifest.sha256, outcome, reason, intent["candidate_image_digest"],
               intent["prior_image_digest"], intent["prior_release"], intent["selected_release_root"],
               intent["selected_release_root"] + "/FRAMEWORK_ENGINE", intent["selected_release_root"] + "/METHODOLOGY",
               PROJECT_SKILL_TARGET, checksum, f"{relative}/observations/recording-unavailable", f"{relative}/prior-selector.toml",
               f"{relative}/prior-skill" if (directory / "prior-skill").exists() else None)
    try:
        observations = _safe_path(root, f"{relative}/observations", create=True)
        attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=observations))
        evidence = replace(evidence, evidence_root=attempt.relative_to(root).as_posix())
        payload = canonical_json(asdict(evidence))
        _write(attempt / "receipt.json", payload)
        _sync(attempt)
        return replace(evidence, receipt_sha256=_digest(payload))
    except (OSError, ReleaseContractError):
        return replace(evidence, outcome="recording_uncertain", reason="promotion observation recording is uncertain")


def verify_bound_promotion_evidence(candidate, compilation, suite, build, verification,
                                    evidence: PromotionEvidence, *, e2e: CandidateE2EGateEvidence,
                                    full_gate: FullGateEvidence) -> Path:
    """Reopen exact observed promotion for later, independently gated retirement."""
    verify_bound_full_gate_evidence(candidate, compilation, suite, build, verification, e2e, full_gate)
    input_sha = _inputs(candidate, compilation, suite, build, verification, e2e, full_gate)
    if not isinstance(evidence, PromotionEvidence) or evidence.outcome != "promoted" or not evidence.receipt_sha256:
        raise ReleaseContractError("release-promotion-evidence-untrusted", "retirement requires a recorded observed promotion")
    if build.execution_kind != "docker-subprocess" or verification.execution_kind != "docker-subprocess":
        raise ReleaseContractError("release-promotion-evidence-untrusted", "mock image admission is never actual promotion proof")
    root = Path(candidate.project_root)
    directory = _safe_path(root, f"{PROMOTION_ROOT}/{candidate.manifest.sha256}")
    intent, checksum = _pending(root, directory, input_sha)
    expected_prefix = directory.relative_to(root).as_posix() + "/observations/attempt-"
    if (not evidence.evidence_root.startswith(expected_prefix) or "/" in evidence.evidence_root[len(expected_prefix):]
            or evidence.intent_sha256 != checksum or evidence.prior_image_digest != intent["prior_image_digest"]
            or evidence.candidate_image_digest != intent["candidate_image_digest"]
            or evidence.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
            or evidence.prior_release != intent["prior_release"]
            or evidence.selected_release_root != intent["selected_release_root"]
            or evidence.framework_engine_root != intent["selected_release_root"] + "/FRAMEWORK_ENGINE"
            or evidence.methodology_root != intent["selected_release_root"] + "/METHODOLOGY"
            or evidence.skill_target != PROJECT_SKILL_TARGET
            or evidence.retained_prior_selector_ref != directory.relative_to(root).as_posix() + "/prior-selector.toml"
            or intent.get("e2e_receipt_sha256") != e2e.receipt_sha256
            or intent.get("e2e_evidence_root") != e2e.evidence_root
            or intent.get("full_gate_receipt_sha256") != full_gate.receipt_sha256
            or intent.get("full_gate_evidence_root") != full_gate.evidence_root):
        raise ReleaseContractError("release-promotion-evidence-untrusted", "promotion receipt is outside the exact admitted observation")
    receipt = _file(root, f"{evidence.evidence_root}/receipt.json").read_bytes()
    if (_digest(receipt) != evidence.receipt_sha256
            or receipt != canonical_json(asdict(replace(evidence, receipt_sha256=None)))):
        raise ReleaseContractError("release-promotion-evidence-untrusted", "promotion receipt is changed or caller-forged")
    _resume_currentness(root, candidate, compilation, suite, build, verification, e2e, full_gate, intent)
    backup = directory / "prior-skill"
    if evidence.retained_prior_skill_ref is not None:
        if (evidence.retained_prior_skill_ref != backup.relative_to(root).as_posix()
                or _skill_records(root, backup) != intent["prior_skill"]):
            raise ReleaseContractError("release-promotion-evidence-stale", "retained prior Skill no longer matches the admitted recovery carrier")
    elif backup.exists() or backup.is_symlink():
        raise ReleaseContractError("release-promotion-evidence-stale", "promotion receipt does not identify its retained prior Skill")
    prior = _file(root, evidence.retained_prior_selector_ref).read_bytes()
    if (_digest(prior) != intent["prior_selector_sha256"] or _prior_image(prior) != evidence.prior_image_digest
            or _file(root, CURRENT_SELECTOR_RELATIVE).read_bytes() != _selector(
                candidate, evidence.candidate_image_digest, build.context_sha256
            )
            or _skill_records(root, root / PROJECT_SKILL_TARGET) != intent["candidate_skill"]):
        raise ReleaseContractError("release-promotion-evidence-stale", "recorded promotion or retained prior identity is no longer observed")
    return root


__all__ = ["PromotionEvidence", "promote_bound_release", "verify_bound_promotion_evidence"]
