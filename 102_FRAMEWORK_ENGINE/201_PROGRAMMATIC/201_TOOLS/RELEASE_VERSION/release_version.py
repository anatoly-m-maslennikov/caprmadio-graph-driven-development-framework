"""Native D560 Release Version request boundary.

This module deliberately implements only the effect-free ``prepare`` path.
``apply`` and ``recover_recording`` return a typed blocked result until the
selected-Action provider supplies its admitted private context.  No branch
copies, compiles, stages, installs, selects, invokes an image, or records a
Journal event.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal, Mapping

from pydantic import Field, ValidationError, field_validator, model_validator

from release_contract import (
    CandidateBuildRequest,
    CandidateSnapshotManifest,
    ReleaseContractError,
    StrictModel,
    ValidatedCandidate,
)
from release_handoff import build_validated_candidate


TOOL_SCHEMA = "caprmedio.release_version.v1"
_OPERATIONS = ("prepare", "apply", "recover_recording")


class ReleaseVersionError(ReleaseContractError):
    """Stable refusal from the native D560 request/result boundary."""


def _identifier(value: str, field: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip() or "\n" in value or "\r" in value:
        raise ValueError(f"{field} must be one non-empty identifier")
    return value


class ReleaseVersionRequest(StrictModel):
    """Closed D560 request; no paths or effects are caller-overridable."""

    operation: Literal["prepare", "apply", "recover_recording"]
    project_root: str
    candidate_snapshot_manifest: CandidateSnapshotManifest = Field(alias="candidateSnapshotManifest")
    expected_executing_release: str
    expected_project_structure_digest: str
    expected_framework_settings_digest: str
    expected_source_frontier_digest: str
    run_receipt_refs: list[str] = Field(min_length=1)
    failed_recording_ref: str | None = None

    @field_validator("project_root")
    @classmethod
    def bounded_project_root(cls, value: str) -> str:
        return _identifier(value, "project_root")

    @field_validator(
        "expected_executing_release",
        "expected_project_structure_digest",
        "expected_framework_settings_digest",
        "expected_source_frontier_digest",
        "failed_recording_ref",
    )
    @classmethod
    def bounded_identifiers(cls, value: str | None, info: Any) -> str | None:
        return None if value is None else _identifier(value, info.field_name)

    @field_validator("run_receipt_refs")
    @classmethod
    def bounded_receipt_refs(cls, value: list[str]) -> list[str]:
        refs = [_identifier(item, "run_receipt_refs") for item in value]
        if len(refs) != len(set(refs)):
            raise ValueError("run_receipt_refs must not repeat a receipt reference")
        return refs

    @model_validator(mode="after")
    def exact_operation_bindings(self) -> "ReleaseVersionRequest":
        manifest = self.candidate_snapshot_manifest
        if self.expected_executing_release != manifest.executing_release:
            raise ValueError("expected_executing_release differs from candidateSnapshotManifest")
        if self.expected_project_structure_digest != manifest.project_structure_digest:
            raise ValueError("expected_project_structure_digest differs from candidateSnapshotManifest")
        if self.expected_framework_settings_digest != manifest.framework_settings_digest:
            raise ValueError("expected_framework_settings_digest differs from candidateSnapshotManifest")
        if self.expected_source_frontier_digest != manifest.source_frontier_digest:
            raise ValueError("expected_source_frontier_digest differs from candidateSnapshotManifest")
        if self.operation == "recover_recording":
            if self.failed_recording_ref is None:
                raise ValueError("recover_recording requires failed_recording_ref")
        elif self.failed_recording_ref is not None:
            raise ValueError("failed_recording_ref is only admitted for recover_recording")
        return self


class ReleaseVersionResult(StrictModel):
    """Exactly the D560 result members, with no unearned effect evidence."""

    operation: Literal["prepare", "apply", "recover_recording"]
    outcome: Literal["prepared", "blocked"]
    candidate_snapshot_manifest_sha256: str
    prior_release: str
    candidate_release: str
    runtime_selection: Literal["unchanged"]
    skill_selection: Literal["unchanged"]
    attempted_effects: list[str]
    gate_evidence_refs: list[str]
    image_refs: list[str]
    rollback_state: Literal["not_attempted"]
    run_receipt_refs: list[str]

    @model_validator(mode="after")
    def effect_free_result(self) -> "ReleaseVersionResult":
        if self.attempted_effects or self.gate_evidence_refs or self.image_refs:
            raise ValueError("effect-free native boundary cannot report effect or gate evidence")
        return self


@dataclass(frozen=True)
class _SelectedReleaseActionContext:
    """Private future provider input, never parsed from the D560 request."""

    workflow_run_id: str
    action_run_id: str


def _parse_request(value: ReleaseVersionRequest | Mapping[str, Any]) -> ReleaseVersionRequest:
    if isinstance(value, ReleaseVersionRequest):
        return value
    if not isinstance(value, Mapping):
        raise ReleaseVersionError("release-request-invalid", "release request must be an object")
    try:
        return ReleaseVersionRequest.model_validate(value)
    except ValidationError as error:
        raise ReleaseVersionError("release-request-invalid", "release request does not match the closed D560 contract") from error


def _intent_from_manifest(manifest: CandidateSnapshotManifest) -> CandidateBuildRequest:
    """Extract only declared future expectations; never caller authority rows."""

    return CandidateBuildRequest(
        candidate_release=manifest.candidate_release,
        expected_derived_source_copy_sha256=manifest.expected_derived_source_copy_sha256,
        expected_compiled_output_sha256=manifest.expected_compiled_output_sha256,
        full_suite_environment=manifest.full_suite_environment,
        candidate_image_reference=manifest.candidate_image.candidate_image_reference,
    )


def _locally_observed_candidate(request: ReleaseVersionRequest) -> ValidatedCandidate:
    """Rebuild D566 from local bytes and require total equality with the request."""

    supplied = request.candidate_snapshot_manifest
    try:
        observed = build_validated_candidate(
            request.project_root,
            _intent_from_manifest(supplied),
            observed_source_frontier_digest=request.expected_source_frontier_digest,
        )
    except ReleaseContractError:
        raise
    if observed.manifest.model_dump(mode="json", by_alias=True) != supplied.model_dump(mode="json", by_alias=True):
        raise ReleaseVersionError(
            "release-currentness-stale",
            "candidateSnapshotManifest differs from the complete locally observed candidate",
        )
    authority = observed.authority
    if (
        authority.executing_release != request.expected_executing_release
        or authority.project_structure_digest != request.expected_project_structure_digest
        or authority.framework_settings_digest != request.expected_framework_settings_digest
        or authority.source_frontier_digest != request.expected_source_frontier_digest
        or authority.expected_candidate_snapshot_manifest_sha256 != supplied.sha256
    ):
        raise ReleaseVersionError("release-currentness-stale", "locally observed authority differs from request bindings")
    return observed


def _result(candidate: ValidatedCandidate, operation: Literal["prepare", "apply", "recover_recording"],
            outcome: Literal["prepared", "blocked"], run_receipt_refs: list[str]) -> ReleaseVersionResult:
    return ReleaseVersionResult(
        operation=operation,
        outcome=outcome,
        candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
        prior_release=candidate.authority.executing_release,
        candidate_release=candidate.manifest.candidate_release,
        runtime_selection="unchanged",
        skill_selection="unchanged",
        attempted_effects=[],
        gate_evidence_refs=[],
        image_refs=[],
        rollback_state="not_attempted",
        run_receipt_refs=list(run_receipt_refs),
    )


def release_version(
    request: ReleaseVersionRequest | Mapping[str, Any], *, _selected_action_context: _SelectedReleaseActionContext | None = None,
) -> ReleaseVersionResult:
    """Prepare a locally sealed candidate or truthfully block unintegrated effects."""

    parsed = _parse_request(request)
    if _selected_action_context is not None and not isinstance(_selected_action_context, _SelectedReleaseActionContext):
        raise ReleaseVersionError("release-selected-context-invalid", "selected Action context must be private typed context")
    candidate = _locally_observed_candidate(parsed)
    if parsed.operation == "prepare":
        return _result(candidate, parsed.operation, "prepared", parsed.run_receipt_refs)
    # Provider dispatch and durable recording recovery are intentionally not
    # implemented at this native boundary.  In particular, no retry can replay
    # a possibly completed effect from a caller-provided failed_recording_ref.
    return _result(candidate, parsed.operation, "blocked", parsed.run_receipt_refs)


__all__ = ["ReleaseVersionError", "ReleaseVersionRequest", "ReleaseVersionResult", "TOOL_SCHEMA", "release_version"]
