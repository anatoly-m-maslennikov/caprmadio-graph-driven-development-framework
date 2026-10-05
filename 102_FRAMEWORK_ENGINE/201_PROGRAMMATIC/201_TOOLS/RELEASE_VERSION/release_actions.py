"""Private O164@3 phase composition behind the shared Session recorder.

Phases are selected only by private Step/Action identity. The adapter retains
typed observations and requires the shared durable checkpoint callback before
invocation; it never creates its own Journal receipts. The checkpoint codec and
shared selected executor own restart recovery. Missing, interrupted or uncertain
effects stop without implicit replay.
"""

from __future__ import annotations

import hashlib
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal, Mapping

from release_compilation import ReleaseCompilationPreflight, preflight_release_compilation, render_release_candidate
from release_contract import SHA256, ReleaseContractError, ValidatedCandidate, canonical_json
from release_delivery import deliver_release_sources
from release_handoff import SealedCandidateCompilation, SealedSourceCopy, _revalidate
from release_image import (
    DockerExecutor, ImageBuildEvidence, ImageVerificationEvidence, ImageRetirementEvidence,
    build_candidate_image, verify_candidate_image, retire_prior_image,
)
from release_packaging import stage_framework_package
from release_promotion import PromotionEvidence, promote_bound_release
from release_suite import SuiteGateEvidence, execute_bound_release_suite, verify_bound_suite_evidence
from release_suite_execution import installed_n_suite_executor
from release_version import ReleaseVersionRequest, _locally_observed_candidate


PHASES = (
    ("CA-O-170", "CA-O-165", "freeze"),
    ("CA-O-171", "CA-O-165", "validate"),
    ("CA-O-172", "CA-O-166", "deliver_sources"),
    ("CA-O-173", "CA-O-166", "compile"),
    ("CA-O-174", "CA-O-168", "run_tests"),
    ("CA-O-175", "CA-O-167", "stage_candidate"),
    ("CA-O-176", "CA-O-168", "build_image"),
    ("CA-O-177", "CA-O-168", "prove_candidate"),
    ("CA-O-178", "CA-O-169", "promote"),
    ("CA-O-179", "CA-O-169", "retire"),
)


@dataclass(frozen=True)
class SelectedReleaseActionContext:
    """Provider-owned identity; never parsed from D560 client parameters."""
    project_root: str
    workflow_run_id: str
    step_run_id: str
    action_run_id: str
    parent_workflow_run_id: str
    parent_step_run_id: str
    step_atom_id: str
    action_atom_id: str
    frozen_parameters_sha256: str
    workflow_atom_id: str = "CA-O-164"
    workflow_version: int = 3


@dataclass(frozen=True)
class AdmittedImageExecutor:
    """Private executor associated with this already-selected Run and root."""
    project_root: str
    workflow_run_id: str
    executor: DockerExecutor


@dataclass(frozen=True)
class ReleasePhaseResult:
    workflow_run_id: str
    step_run_id: str
    action_run_id: str
    step_atom_id: str
    action_atom_id: str
    phase: str
    outcome: Literal["prepared", "completed", "blocked", "failed", "pending", "effect_uncertain"]
    reason: str
    candidate_snapshot_manifest_sha256: str
    attempted_effects: tuple[str, ...]
    effect_evidence_refs: tuple[str, ...]
    declared_run_receipt_refs: tuple[str, ...]
    recording_state: Literal["shared_session_provider_pending"] = "shared_session_provider_pending"
    output: Any = None
    # A successful terminal effect is not a completed Action Run until the
    # shared Session provider records it durably.  Keep that distinction
    # explicit for the only terminal phase whose producer has its own outcome
    # vocabulary.
    effect_outcome: str | None = None
    # This is an inter-layer handoff, not a receipt.  The private Release
    # adapter remains pending until the shared Session records the exact
    # Action terminal result.  Only the shared dispatcher may use this packet
    # to request that receipt and expose the frozen O164 result transition.
    shared_action_recording: Mapping[str, str] | None = None


@dataclass
class ReleaseActionRun:
    """Private retained frontier, not durable recovery or a Journal registry."""
    project_root: str
    workflow_run_id: str
    frozen_parameters_sha256: str
    request: ReleaseVersionRequest
    image_executor: AdmittedImageExecutor | None = None
    next_phase: int = 0
    stopped: bool = False
    in_progress: SelectedReleaseActionContext | None = None
    contexts: dict[int, SelectedReleaseActionContext] = field(default_factory=dict)
    results: dict[int, ReleasePhaseResult] = field(default_factory=dict)
    candidate: ValidatedCandidate | None = None
    preflight: ReleaseCompilationPreflight | None = None
    source_copy: SealedSourceCopy | None = None
    compilation: SealedCandidateCompilation | None = None
    suite: SuiteGateEvidence | None = None
    package: dict[str, object] | None = None
    build: ImageBuildEvidence | None = None
    verification: ImageVerificationEvidence | None = None
    promotion: PromotionEvidence | None = None
    retirement: ImageRetirementEvidence | None = None
    # The caller supplies the one shared durable checkpoint writer.  This
    # private adapter never opens a carrier or creates a second record; the
    # callback is runtime-only and the closed checkpoint codec excludes it.
    checkpoint_callback: Callable[["ReleaseActionRun"], None] | None = field(
        default=None, repr=False, compare=False,
    )


def _request(value: ReleaseVersionRequest | Mapping[str, Any]) -> ReleaseVersionRequest:
    try:
        payload = value.model_dump(mode="json", by_alias=True) if isinstance(value, ReleaseVersionRequest) else value
        return ReleaseVersionRequest.model_validate(payload)
    except (ValueError, TypeError) as error:
        raise ReleaseContractError("release-action-request-invalid", "request violates the closed D560 contract") from error


def _fingerprint(request: ReleaseVersionRequest) -> str:
    payload = request.model_dump(mode="json", by_alias=True)
    # Invocation controls may change; frozen source parameters and declared
    # receipt references may not. Recording recovery remains separately blocked.
    payload.pop("operation")
    payload.pop("failed_recording_ref")
    return hashlib.sha256(canonical_json(payload)).hexdigest()


def begin_release_action_run(request: ReleaseVersionRequest | Mapping[str, Any], *, workflow_run_id: str,
                             image_executor: AdmittedImageExecutor | None = None,
                             checkpoint_callback: Callable[[ReleaseActionRun], None] | None = None) -> ReleaseActionRun:
    """Allocate new private state only; no helper effect or Run is recorded."""
    parsed = _request(request)
    root = Path(parsed.project_root).resolve(strict=True)
    if not root.is_dir() or not isinstance(workflow_run_id, str) or not workflow_run_id.strip() or workflow_run_id != workflow_run_id.strip():
        raise ReleaseContractError("release-action-run-invalid", "private Run requires a valid root and frozen identity")
    if image_executor is not None and (not isinstance(image_executor, AdmittedImageExecutor)
            or image_executor.project_root != str(root) or image_executor.workflow_run_id != workflow_run_id
            or not callable(getattr(image_executor.executor, "run", None))):
        raise ReleaseContractError("release-action-executor-unadmitted", "image executor is not bound to this selected Run")
    if checkpoint_callback is not None and not callable(checkpoint_callback):
        raise ReleaseContractError("release-action-checkpoint-invalid", "checkpoint callback must be callable when supplied")
    return ReleaseActionRun(str(root), workflow_run_id, _fingerprint(parsed), parsed, image_executor,
                            checkpoint_callback=checkpoint_callback)


def _selection(request, context, run):
    if not isinstance(run, ReleaseActionRun) or not isinstance(context, SelectedReleaseActionContext):
        raise ReleaseContractError("release-action-context-untrusted", "dispatch requires retained private Run and selected context")
    if (context.workflow_atom_id != "CA-O-164" or type(context.workflow_version) is not int or context.workflow_version != 3
            or context.workflow_run_id != run.workflow_run_id or context.parent_workflow_run_id != run.workflow_run_id
            or context.parent_step_run_id != context.step_run_id
            or context.project_root != run.project_root or str(Path(request.project_root).resolve(strict=True)) != run.project_root
            or context.frozen_parameters_sha256 != run.frozen_parameters_sha256
            or _fingerprint(request) != run.frozen_parameters_sha256
            or _fingerprint(run.request) != run.frozen_parameters_sha256):
        raise ReleaseContractError("release-action-frozen-binding-mismatch", "root, parameters or frozen Run lineage differ")
    for identity in (context.workflow_run_id, context.step_run_id, context.action_run_id):
        if not isinstance(identity, str) or not identity or identity != identity.strip() or "\n" in identity or "\r" in identity:
            raise ReleaseContractError("release-action-context-invalid", "selected Run identities must be bounded")
    matches = [index for index, pair in enumerate(PHASES) if pair[:2] == (context.step_atom_id, context.action_atom_id)]
    if len(matches) != 1:
        raise ReleaseContractError("release-action-phase-unselected", "Step/Action pair is outside O164@2")
    index = matches[0]
    if index in run.contexts and run.contexts[index] != context:
        raise ReleaseContractError("release-action-identity-mismatch", "selected occurrence identity changed")
    if any(other != index and (saved.step_run_id == context.step_run_id or saved.action_run_id == context.action_run_id)
           for other, saved in run.contexts.items()):
        raise ReleaseContractError("release-action-identity-mismatch", "Step/Action Run identity repeats another occurrence")
    return index, PHASES[index][2]


def _checkpoint(run: ReleaseActionRun, *, index: int, context: SelectedReleaseActionContext,
                result: ReleasePhaseResult | None = None) -> None:
    """Ask the injected shared recorder to persist exactly this private frontier.

    It writes nothing itself.  The callback must not change the retained Run;
    that would invalidate the frontier that the recorder was asked to save.
    """
    callback = run.checkpoint_callback
    if not callable(callback):
        raise ReleaseContractError(
            "release-action-checkpoint-unavailable",
            "an effectful Release phase requires the injected shared checkpoint recorder",
        )
    expected_next = run.next_phase
    expected_stopped = run.stopped
    callback(run)
    if (run.in_progress != (None if result is not None else context)
            or run.contexts.get(index) != context
            or run.results.get(index) != result
            or run.next_phase != expected_next or run.stopped != expected_stopped):
        raise ReleaseContractError(
            "release-action-checkpoint-mutated",
            "checkpoint callback changed the retained private Run frontier",
        )


def _result(run, context, phase, outcome, reason, *, attempted=(), refs=(), output=None,
            effect_outcome=None, shared_action_recording=None):
    return ReleasePhaseResult(run.workflow_run_id, context.step_run_id, context.action_run_id,
        context.step_atom_id, context.action_atom_id, phase, outcome, reason,
        run.request.candidate_snapshot_manifest.sha256, tuple(attempted), tuple(refs),
        tuple(run.request.run_receipt_refs), output=output, effect_outcome=effect_outcome,
        shared_action_recording=shared_action_recording)


def _retirement_recording_handoff(retired: ImageRetirementEvidence) -> dict[str, str] | None:
    """Describe the one receipt a shared dispatcher must record after retirement.

    The packet deliberately contains no mutable selector, caller-controlled
    terminal state, or replay instruction.  It only identifies the already
    observed exact effect and the one O164 transition that becomes available
    after the shared Action receipt is terminal and completed.
    """
    if retired.outcome != "retired":
        return None
    if (not isinstance(retired.candidate_snapshot_manifest_sha256, str)
            or SHA256.fullmatch(retired.candidate_snapshot_manifest_sha256) is None
            or not isinstance(retired.prior_image_digest, str)
            or not retired.prior_image_digest.startswith("sha256:")
            or SHA256.fullmatch(retired.prior_image_digest.removeprefix("sha256:")) is None
            or not isinstance(retired.evidence_root, str) or not retired.evidence_root
            or Path(retired.evidence_root).is_absolute() or ".." in Path(retired.evidence_root).parts
            or not isinstance(retired.receipt_sha256, str)
            or SHA256.fullmatch(retired.receipt_sha256) is None):
        raise ReleaseContractError(
            "release-action-retirement-recording-invalid",
            "retired image evidence cannot be handed to shared Action recording",
        )
    return {
        "on_recorded_result": "complete exact unused N-image retirement",
        "candidate_snapshot_manifest_sha256": retired.candidate_snapshot_manifest_sha256,
        "prior_image_digest": retired.prior_image_digest,
        "retirement_receipt_ref": f"{retired.evidence_root}/receipt.json",
        "retirement_receipt_sha256": retired.receipt_sha256,
    }


def _bound(value, candidate):
    if getattr(value, "candidate_snapshot_manifest_sha256", None) != candidate.manifest.sha256:
        raise ReleaseContractError("release-action-result-mismatch", "helper result belongs to another candidate")


def _executor(run):
    admission = run.image_executor
    if (not isinstance(admission, AdmittedImageExecutor) or admission.workflow_run_id != run.workflow_run_id
            or admission.project_root != run.project_root):
        raise ReleaseContractError("release-action-executor-unadmitted", "selected Run has no admitted image executor")
    return admission.executor


def _invoke(phase, run):
    candidate = run.candidate
    if phase == "freeze":
        candidate = _locally_observed_candidate(run.request)
        preflight = preflight_release_compilation(run.project_root, candidate_release=candidate.manifest.candidate_release)
        if (preflight.expected_derived_source_copy_sha256 != candidate.manifest.expected_derived_source_copy_sha256
                or preflight.expected_compiled_output_sha256 != candidate.manifest.expected_compiled_output_sha256
                or preflight.compiler_frontier_digest != candidate.authority.source_frontier_digest):
            raise ReleaseContractError("release-action-compiler-binding-mismatch", "sealed expectations differ from actual compiler preflight")
        run.candidate, run.preflight = candidate, preflight
        return "completed", "complete frozen N and candidate boundary observed", (), candidate
    if candidate is None or run.preflight is None:
        raise ReleaseContractError("release-action-prerequisite-missing", "frozen candidate is unavailable")
    if (not isinstance(candidate, ValidatedCandidate) or candidate.project_root != run.project_root
            or candidate.manifest != run.request.candidate_snapshot_manifest):
        raise ReleaseContractError("release-action-prerequisite-mismatch", "retained candidate differs from this frozen Run")
    if run.source_copy is not None and (not isinstance(run.source_copy, SealedSourceCopy)
            or run.source_copy.candidate != candidate):
        raise ReleaseContractError("release-action-prerequisite-mismatch", "retained source-copy result belongs to another candidate")
    for retained in (run.compilation, run.suite, run.build, run.verification, run.promotion, run.retirement):
        if retained is not None:
            _bound(retained, candidate)
    if phase == "validate":
        _revalidate(candidate)
        if preflight_release_compilation(run.project_root, candidate_release=candidate.manifest.candidate_release) != run.preflight:
            raise ReleaseContractError("release-action-currentness-stale", "compiler boundary changed after freeze")
        return "completed", "exact candidate/compiler bindings observed", (), candidate
    if phase == "deliver_sources":
        copied = deliver_release_sources(candidate)
        if not isinstance(copied, SealedSourceCopy) or copied.candidate.manifest != candidate.manifest:
            raise ReleaseContractError("release-action-result-mismatch", "source delivery is not bound to the frozen candidate")
        run.source_copy = copied
        return "completed", "complete source delivery observed", (f"{copied.source_copy_root}#sha256={copied.actual_derived_source_copy_sha256}",), copied
    if run.source_copy is None:
        raise ReleaseContractError("release-action-prerequisite-missing", "complete source delivery is unavailable")
    if phase == "compile":
        compiled = render_release_candidate(candidate, run.preflight)
        if not isinstance(compiled, SealedCandidateCompilation):
            raise ReleaseContractError("release-action-result-untrusted", "compiler result is not typed local evidence")
        _bound(compiled, candidate)
        run.compilation = compiled
        return "completed", "child-scoped compiler output observed", (f"{compiled.child_materialization_root}#sha256={compiled.actual_compiled_output_sha256}",), compiled
    if run.compilation is None:
        raise ReleaseContractError("release-action-prerequisite-missing", "accepted compilation is unavailable")
    if phase == "run_tests":
        # O174 precedes O175. Testing never stages a runtime or public Skill.
        suite = execute_bound_release_suite(
            candidate,
            run.compilation,
            executor=installed_n_suite_executor(
                candidate,
                run.compilation,
                project_root=run.project_root,
                docker=_executor(run),
            ),
        )
        if not isinstance(suite, SuiteGateEvidence):
            raise ReleaseContractError("release-action-result-untrusted", "suite result is not actual typed evidence")
        _bound(suite, candidate)
        run.suite = suite
        return ("completed" if suite.passed else "pending"), suite.reason, (f"{suite.evidence_root}/receipt.json",) if suite.receipt_sha256 else (), suite
    if run.suite is None or not run.suite.passed:
        raise ReleaseContractError("release-action-prerequisite-missing", "passing full suite is unavailable")
    if phase == "stage_candidate":
        verify_bound_suite_evidence(candidate, run.compilation, run.suite)
        package = stage_framework_package(run.project_root, run.compilation)
        if package.get("candidate_snapshot_manifest_sha256") != candidate.manifest.sha256 or package.get("verified") is not True:
            raise ReleaseContractError("release-action-result-mismatch", "retained package lacks observed same-candidate verification")
        run.package = package
        return "completed", "complete non-active package and Skill staging observed", (str(package["release_root"]) + "/manifest.toml",), package
    if run.package is None:
        raise ReleaseContractError("release-action-prerequisite-missing", "complete post-suite staging is unavailable")
    if phase == "build_image":
        build = build_candidate_image(candidate, run.compilation, run.suite, executor=_executor(run))
        if not isinstance(build, ImageBuildEvidence):
            raise ReleaseContractError("release-action-result-untrusted", "image build observation is not typed")
        _bound(build, candidate)
        run.build = build
        complete = build.outcome == "built" and build.execution_kind == "docker-subprocess" and build.receipt_sha256 is not None
        return ("completed" if complete else "pending"), build.reason if complete else "actual immutable image build proof is incomplete", (f"{build.evidence_root}/receipt.json",) if build.receipt_sha256 else (), build
    if run.build is None or run.build.outcome != "built" or run.build.execution_kind != "docker-subprocess":
        raise ReleaseContractError("release-action-prerequisite-missing", "actual same-candidate image build proof is unavailable")
    if phase == "prove_candidate":
        verified = verify_candidate_image(candidate, run.compilation, run.suite, run.build, executor=_executor(run))
        if not isinstance(verified, ImageVerificationEvidence):
            raise ReleaseContractError("release-action-result-untrusted", "image canary observation is not typed")
        _bound(verified, candidate)
        run.verification = verified
        complete = verified.outcome == "verified" and verified.execution_kind == "docker-subprocess" and verified.receipt_sha256 is not None
        return ("completed" if complete else "pending"), verified.reason, (f"{verified.evidence_root}/receipt.json",) if verified.receipt_sha256 else (), verified
    if run.verification is None or run.verification.outcome != "verified" or run.verification.execution_kind != "docker-subprocess":
        raise ReleaseContractError("release-action-prerequisite-missing", "actual candidate image proof is unavailable")
    if phase == "promote":
        promoted = promote_bound_release(candidate, run.compilation, run.suite, run.build, run.verification)
        if not isinstance(promoted, PromotionEvidence):
            raise ReleaseContractError("release-action-result-untrusted", "promotion observation is not typed")
        _bound(promoted, candidate)
        run.promotion = promoted
        return ("completed" if promoted.outcome == "promoted" and promoted.receipt_sha256 else "pending"), promoted.reason, (f"{promoted.evidence_root}/receipt.json",) if promoted.receipt_sha256 else (), promoted
    if phase == "retire":
        if run.promotion is None or run.promotion.outcome != "promoted" or not run.promotion.receipt_sha256:
            raise ReleaseContractError("release-action-prerequisite-missing", "recorded observed promotion is unavailable")
        retired = retire_prior_image(candidate, run.compilation, run.suite, run.build, run.verification,
                                     run.promotion, executor=_executor(run))
        if not isinstance(retired, ImageRetirementEvidence):
            raise ReleaseContractError("release-action-result-untrusted", "retirement observation is not typed")
        _bound(retired, candidate)
        run.retirement = retired
        reason = retired.reason
        recording = _retirement_recording_handoff(retired)
        if retired.outcome == "retired":
            reason = "exact prior image retired; shared durable Action recording is pending"
        return ("pending", reason,
                (f"{retired.evidence_root}/receipt.json",) if retired.receipt_sha256 else (),
                retired, retired.outcome, recording)
    raise ReleaseContractError("release-action-phase-unselected", "unknown selected phase")


def execute_release_action(request: ReleaseVersionRequest | Mapping[str, Any], *,
                           context: SelectedReleaseActionContext, run: ReleaseActionRun) -> ReleasePhaseResult:
    """Observe one selected phase; never write a Journal or replay unknown work."""
    parsed = _request(request)
    index, phase = _selection(parsed, context, run)
    if parsed.operation == "recover_recording":
        return _result(run, context, phase, "blocked", "shared Session recording recovery is not integrated; no effect replay")
    if parsed.operation == "prepare":
        _locally_observed_candidate(parsed)
        return _result(run, context, phase, "prepared", "effect-free selected phase preparation")
    if not callable(run.checkpoint_callback):
        # Every non-prepare path can retain or cause an effect.  Refuse before
        # mutating the private frontier or calling a helper when the sole
        # durable checkpoint boundary was not injected by the shared Session.
        return _result(
            run, context, phase, "blocked",
            "shared checkpoint recorder is required before any Release phase invocation",
        )
    if index in run.results:
        return run.results[index]
    if run.in_progress is not None:
        run.stopped = True
        return _result(run, context, phase, "effect_uncertain", "an interrupted or unknown private phase must not be replayed")
    if run.stopped or index != run.next_phase:
        return _result(run, context, phase, "blocked", "selected phase prerequisites are skipped or stopped")
    if any(previous not in run.results or run.results[previous].outcome != "completed"
           or run.results[previous].workflow_run_id != run.workflow_run_id
           or run.results[previous].candidate_snapshot_manifest_sha256 != run.request.candidate_snapshot_manifest.sha256
           or previous not in run.contexts
           or run.results[previous].step_run_id != run.contexts[previous].step_run_id
           or run.results[previous].action_run_id != run.contexts[previous].action_run_id
           for previous in range(index)):
        return _result(run, context, phase, "blocked", "retained prerequisite observations are missing or mismatched")
    if phase in {"run_tests", "build_image", "prove_candidate", "retire"}:
        try:
            _executor(run)
        except ReleaseContractError as error:
            result = _result(run, context, phase, "blocked", f"phase stopped: {error.code}")
            run.contexts[index], run.results[index], run.stopped = context, result, True
            return result
    run.contexts[index], run.in_progress = context, context
    try:
        # Persist the selected in-progress identity before any helper may
        # observe or cause an effect.  Without this checkpoint, invocation is
        # refused rather than leaving work that recovery could replay.
        _checkpoint(run, index=index, context=context)
    except BaseException as error:
        run.contexts[index] = context
        run.in_progress = None
        run.next_phase = index
        result = _result(
            run, context, phase, "blocked",
            f"shared checkpoint failed before phase invocation: {type(error).__name__}",
        )
        run.results[index], run.stopped = result, True
        return result
    attempted = () if phase in {"freeze", "validate"} else (phase,)
    try:
        invoked = _invoke(phase, run)
        outcome, reason, refs, output = invoked[:4]
        effect_outcome = invoked[4] if len(invoked) >= 5 else None
        shared_action_recording = invoked[5] if len(invoked) == 6 else None
        result = _result(run, context, phase, outcome, reason, attempted=attempted, refs=refs, output=output,
                         effect_outcome=effect_outcome, shared_action_recording=shared_action_recording)
    except (KeyboardInterrupt, InterruptedError, SystemExit) as error:
        result = _result(run, context, phase, "effect_uncertain", f"private phase interrupted: {type(error).__name__}", attempted=attempted)
    except (OSError, ValueError, RuntimeError) as error:
        refs = tuple(getattr(error, "recovery_paths", ()))
        result = _result(run, context, phase, "blocked" if isinstance(error, ReleaseContractError) else "failed",
                         f"phase stopped: {getattr(error, 'code', type(error).__name__)}", attempted=attempted, refs=refs)
    except Exception as error:
        result = _result(run, context, phase, "effect_uncertain", f"private phase result is unknown: {type(error).__name__}", attempted=attempted)
    finally:
        run.in_progress = None
    run.results[index] = result
    if result.outcome == "completed":
        run.next_phase += 1
    else:
        run.stopped = True
    try:
        # The terminal local frontier is retained before the shared recorder
        # sees it.  A failed write after any helper invocation is uncertain:
        # it cannot be retried or converted into a completion.
        _checkpoint(run, index=index, context=context, result=result)
    except BaseException as error:
        result = _result(
            run, context, phase, "effect_uncertain",
            f"shared checkpoint failed after phase invocation: {type(error).__name__}; effect must not be replayed",
            attempted=result.attempted_effects,
            refs=result.effect_evidence_refs,
            output=result.output,
            effect_outcome=result.effect_outcome,
        )
        run.results[index] = result
        run.next_phase = index
        run.stopped = True
    return result


__all__ = ["PHASES", "SelectedReleaseActionContext", "AdmittedImageExecutor", "ReleasePhaseResult",
           "ReleaseActionRun", "begin_release_action_run", "execute_release_action"]
