"""Closed request models bound to CA-D-492@5."""

from __future__ import annotations

from typing import Literal, Self
from pydantic import Field, JsonValue, field_validator, model_validator

from .shared_models import (
    AtomBinding,
    FileBinding,
    NonemptySet,
    Path,
    Positive,
    RequestObject,
    SchemaVersion,
    SetList,
    String,
)


class Methodology(RequestObject):
    kind: Literal["sources", "projection"]
    roots: NonemptySet[Path]
    frontier: NonemptySet[AtomBinding] | None = None


class AtomSelector(RequestObject):
    atom_id: String | None = None
    version: Positive | None = None
    carrier_path: Path | None = None

    @model_validator(mode="after")
    def validate_identity(self) -> Self:
        if self.atom_id is None and (self.carrier_path is None or self.version is not None):
            raise ValueError("a selector needs an ID or path; a version needs an ID")
        return self


class Selection(RequestObject):
    scope_unit: String | None = None
    include_descendants: bool = False
    global_tiers: NonemptySet[int] | None = None
    local_tiers: NonemptySet[String] | None = None
    atoms: NonemptySet[AtomSelector] | None = None
    statuses: Literal["active", "all"] | NonemptySet[String] | None = None

    @model_validator(mode="after")
    def validate_criteria(self) -> Self:
        if not self.model_fields_set.intersection(
            {"scope_unit", "global_tiers", "local_tiers", "atoms"}
        ):
            raise ValueError("at least one selection criterion is required")
        if "include_descendants" in self.model_fields_set and self.scope_unit is None:
            raise ValueError("include_descendants requires scope_unit")
        return self


class Limits(RequestObject):
    max_candidates: Positive | None = None
    max_file_bytes: Positive | None = None
    max_total_read_bytes: Positive | None = None
    timeout_seconds: Positive | None = None
    max_findings: Positive | None = None


class RunContext(RequestObject):
    workflow_run_id: String | None = None
    step_run_id: String | None = None


class CheckBinding(RequestObject):
    code: String
    adapter_id: String
    authority: NonemptySet[AtomBinding]
    parameters: dict[str, JsonValue]


class RuleBundle(RequestObject):
    schema_version: SchemaVersion
    authority: NonemptySet[AtomBinding]
    checks: list[CheckBinding]

    @field_validator("checks")
    @classmethod
    def unique_codes(cls, values: list[CheckBinding]) -> list[CheckBinding]:
        if len({check.code for check in values}) != len(values):
            raise ValueError("duplicate check code")
        return sorted(values, key=lambda check: check.code)


class Request(RequestObject):
    schema_version: SchemaVersion
    source_roots: NonemptySet[Path]
    allowed_read_roots: NonemptySet[Path]
    methodology: Methodology
    selection: Selection
    action_binding: AtomBinding | None = None
    project_structure: FileBinding | None = None
    operators_registry: FileBinding | None = None
    reference_roots: SetList[Path] = Field(default_factory=list)
    exclude_paths: SetList[Path] = Field(default_factory=list)
    limits: Limits = Field(default_factory=Limits)
    framework_settings: FileBinding | None = None
    default_settings: FileBinding | None = None
    run_context: RunContext = Field(default_factory=RunContext)
    rule_bundle: RuleBundle | None = None
