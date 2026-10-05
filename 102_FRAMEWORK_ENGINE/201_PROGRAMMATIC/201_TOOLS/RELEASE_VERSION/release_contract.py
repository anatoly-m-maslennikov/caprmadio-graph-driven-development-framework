"""Effect-free D566 candidate manifest encoding.

This module has no compiler, copy, package, runtime-selector, image, or
Journal effect. It defines the canonical v2 candidate boundary consumed only
by the locally observed handoff in :mod:`release_handoff`.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


CANDIDATE_SCHEMA = "caprmedio.release_version.candidate.v2"
SHA256 = re.compile(r"^[0-9a-f]{64}$")
RELEASE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._+\-]{0,127}$")
PROJECT_SKILL_TARGET = ".agents/skills/ca"
IMAGE_DOCKERFILE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile"
REQUIRED_ENGINE_SOURCE_PREFIXES = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/",
    "102_FRAMEWORK_ENGINE/202_AGENTIC/",
)


class ReleaseContractError(ValueError):
    """Stable refusal from the pure Release Version boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, populate_by_name=True)


def _safe_relative(value: str, field: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip() or "\\" in value:
        raise ValueError(f"{field} must be a non-empty slash-separated relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or value in {".", ".."} or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError(f"{field} must be a safe relative path")
    if path.as_posix() != value:
        raise ValueError(f"{field} must be normalized")
    return value


def _identifier(value: str, field: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip() or "\n" in value or "\r" in value:
        raise ValueError(f"{field} must be one non-empty identifier")
    return value


class FullSuiteEnvironment(StrictModel):
    runner: str
    command: list[str] = Field(min_length=1)
    working_directory: str

    @field_validator("runner", "command")
    @classmethod
    def bounded_identifiers(cls, value: Any, info: Any) -> Any:
        if isinstance(value, list):
            return [_identifier(item, info.field_name) for item in value]
        return _identifier(value, info.field_name)

    @field_validator("working_directory")
    @classmethod
    def bounded_working_directory(cls, value: str) -> str:
        return value if value == "." else _safe_relative(value, "working_directory")


class CandidateImageReference(StrictModel):
    dockerfile_path: Literal[IMAGE_DOCKERFILE]
    dockerfile_sha256: str = Field(pattern=SHA256.pattern)
    candidate_image_reference: str

    @field_validator("candidate_image_reference")
    @classmethod
    def bounded_reference(cls, value: str) -> str:
        return _identifier(value, "candidate_image_reference")


class SourceInventoryRow(StrictModel):
    """One locally observed source file, not a caller-selected package row."""

    resource: Literal["FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL", "IMAGE_INPUT"]
    source_path: str
    source_sha256: str = Field(pattern=SHA256.pattern)
    source_mode: int = Field(ge=0, le=0o777)
    destination_path: str

    @field_validator("source_path")
    @classmethod
    def bounded_source_path(cls, value: str) -> str:
        return _safe_relative(value, "source_path")

    @field_validator("destination_path")
    @classmethod
    def bounded_destination_path(cls, value: str) -> str:
        return _safe_relative(value, "destination_path")

    @model_validator(mode="after")
    def destination_matches_resource(self) -> "SourceInventoryRow":
        prefixes = {
            "FRAMEWORK_ENGINE": "FRAMEWORK_ENGINE/",
            "METHODOLOGY": "METHODOLOGY/sources/",
            "SKILL": "SKILLS/ca/",
            "IMAGE_INPUT": "IMAGE_INPUT/",
        }
        if not self.destination_path.startswith(prefixes[self.resource]):
            raise ValueError(f"{self.resource} destination_path is outside its required package root")
        return self


def _normalised_manifest_object(value: Mapping[str, Any]) -> dict[str, Any]:
    payload = dict(value)
    payload.pop("sha256", None)
    rows = payload.get("source_inventory_rows")
    if isinstance(rows, list):
        payload["source_inventory_rows"] = sorted(
            (dict(row) for row in rows),
            key=lambda row: (
                str(row.get("destination_path", "")),
                str(row.get("source_path", "")),
                str(row.get("source_sha256", "")),
            ),
        )
    return payload


def canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def candidate_snapshot_manifest_sha256(manifest: "CandidateSnapshotManifest | Mapping[str, Any]") -> str:
    """D566 self-excluding canonical candidate checksum."""

    if isinstance(manifest, CandidateSnapshotManifest):
        value = manifest.model_dump(mode="json", by_alias=True)
    else:
        value = dict(manifest)
    return hashlib.sha256(canonical_json(_normalised_manifest_object(value))).hexdigest()


class CandidateSnapshotManifest(StrictModel):
    """Exactly the D566 pre-effect candidateSnapshotManifest members."""

    schema_version: Literal[CANDIDATE_SCHEMA] = Field(alias="schema")
    sha256: str = Field(pattern=SHA256.pattern)
    executing_release: str
    candidate_release: str
    canonical_source_snapshot_ref: str
    canonical_source_snapshot_digest: str = Field(pattern=SHA256.pattern)
    project_structure_digest: str = Field(pattern=SHA256.pattern)
    framework_settings_digest: str = Field(pattern=SHA256.pattern)
    source_frontier_digest: str = Field(pattern=SHA256.pattern)
    nested_source_recursive_sha256_before: str = Field(pattern=SHA256.pattern)
    expected_derived_source_copy_sha256: str = Field(pattern=SHA256.pattern)
    expected_compiled_output_sha256: str = Field(pattern=SHA256.pattern)
    full_suite_environment: FullSuiteEnvironment
    skill_target: Literal[PROJECT_SKILL_TARGET]
    candidate_image: CandidateImageReference
    source_inventory_rows: list[SourceInventoryRow] = Field(min_length=1)

    @model_validator(mode="before")
    @classmethod
    def normalize_rows(cls, value: Any) -> Any:
        if not isinstance(value, Mapping):
            return value
        normalized = dict(value)
        rows = normalized.get("source_inventory_rows")
        if isinstance(rows, list):
            normalized["source_inventory_rows"] = sorted(
                rows,
                key=lambda row: (
                    str(row.get("destination_path", "")) if isinstance(row, Mapping) else "",
                    str(row.get("source_path", "")) if isinstance(row, Mapping) else "",
                    str(row.get("source_sha256", "")) if isinstance(row, Mapping) else "",
                ),
            )
        return normalized

    @field_validator("executing_release", "candidate_release")
    @classmethod
    def stable_release(cls, value: str) -> str:
        if not isinstance(value, str) or not RELEASE.fullmatch(value):
            raise ValueError("release must be a stable release identifier")
        return value

    @field_validator("canonical_source_snapshot_ref")
    @classmethod
    def bounded_snapshot_ref(cls, value: str) -> str:
        return _safe_relative(value, "canonical_source_snapshot_ref")

    @model_validator(mode="after")
    def validate_complete_locally_observable_inventory(self) -> "CandidateSnapshotManifest":
        if self.executing_release == self.candidate_release:
            raise ValueError("candidate_release must differ from executing_release")
        destinations = [row.destination_path for row in self.source_inventory_rows]
        sources = [row.source_path for row in self.source_inventory_rows]
        if len(destinations) != len(set(destinations)):
            raise ValueError("candidate manifest has a destination collision")
        if len(sources) != len(set(sources)):
            raise ValueError("candidate manifest repeats an exact source path")
        resources = {row.resource for row in self.source_inventory_rows}
        if resources != {"FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL", "IMAGE_INPUT"}:
            raise ValueError("candidate manifest must include Framework, Methodology, Skill, and image input rows")
        engine_sources = {row.source_path for row in self.source_inventory_rows if row.resource == "FRAMEWORK_ENGINE"}
        if any(not any(path.startswith(prefix) for path in engine_sources) for prefix in REQUIRED_ENGINE_SOURCE_PREFIXES):
            raise ValueError("candidate manifest is Engine-Tools-only or lacks required Framework Engine components")
        skill_destinations = {row.destination_path for row in self.source_inventory_rows if row.resource == "SKILL"}
        if not {"SKILLS/ca/SKILL.md", "SKILLS/ca/agents/openai.yaml"} <= skill_destinations:
            raise ValueError("candidate manifest must include the complete ca Skill control payload")
        if self.sha256 != candidate_snapshot_manifest_sha256(self):
            raise ValueError("candidate manifest sha256 does not match its self-excluding canonical bytes")
        return self


class SealedAuthority(StrictModel):
    """Internal local-currentness binding; never a request member."""

    executing_release: str
    candidate_release: str
    canonical_source_snapshot_digest: str = Field(pattern=SHA256.pattern)
    project_structure_digest: str = Field(pattern=SHA256.pattern)
    framework_settings_digest: str = Field(pattern=SHA256.pattern)
    source_frontier_digest: str = Field(pattern=SHA256.pattern)
    nested_source_recursive_sha256_before: str = Field(pattern=SHA256.pattern)
    expected_candidate_snapshot_manifest_sha256: str = Field(pattern=SHA256.pattern)

    @field_validator("executing_release", "candidate_release")
    @classmethod
    def stable_release(cls, value: str) -> str:
        if not isinstance(value, str) or not RELEASE.fullmatch(value):
            raise ValueError("release must be a stable release identifier")
        return value

    @model_validator(mode="after")
    def distinct_releases(self) -> "SealedAuthority":
        if self.executing_release == self.candidate_release:
            raise ValueError("sealed candidate_release must differ from executing_release")
        return self


@dataclass(frozen=True)
class ValidatedCandidate:
    """Private pre-compiler handoff created only from locally read state."""

    project_root: str
    manifest: CandidateSnapshotManifest
    authority: SealedAuthority
    intent: "CandidateBuildRequest"


class CandidateBuildRequest(StrictModel):
    """Untrusted declared candidate intent; it never supplies authority or rows."""

    candidate_release: str
    expected_derived_source_copy_sha256: str = Field(pattern=SHA256.pattern)
    expected_compiled_output_sha256: str = Field(pattern=SHA256.pattern)
    full_suite_environment: FullSuiteEnvironment
    candidate_image_reference: str

    @field_validator("candidate_release")
    @classmethod
    def stable_release(cls, value: str) -> str:
        if not isinstance(value, str) or not RELEASE.fullmatch(value):
            raise ValueError("candidate_release must be a stable release identifier")
        return value

    @field_validator("candidate_image_reference")
    @classmethod
    def bounded_image_reference(cls, value: str) -> str:
        return _identifier(value, "candidate_image_reference")


def encode_candidate_manifest(payload: Mapping[str, Any]) -> CandidateSnapshotManifest:
    """Create one canonical v2 manifest after all local observation is complete."""

    encoded = dict(payload)
    encoded["schema"] = CANDIDATE_SCHEMA
    encoded["sha256"] = "0" * 64
    encoded["sha256"] = candidate_snapshot_manifest_sha256(encoded)
    return CandidateSnapshotManifest.model_validate(encoded)


__all__ = [
    "CANDIDATE_SCHEMA",
    "IMAGE_DOCKERFILE",
    "PROJECT_SKILL_TARGET",
    "REQUIRED_ENGINE_SOURCE_PREFIXES",
    "CandidateBuildRequest",
    "CandidateImageReference",
    "CandidateSnapshotManifest",
    "FullSuiteEnvironment",
    "ReleaseContractError",
    "SealedAuthority",
    "SourceInventoryRow",
    "ValidatedCandidate",
    "candidate_snapshot_manifest_sha256",
    "canonical_json",
    "encode_candidate_manifest",
]
