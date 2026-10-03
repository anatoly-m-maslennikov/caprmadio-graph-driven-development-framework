"""Closed result representations bound to CA-D-493@3."""

from __future__ import annotations

from typing import Literal, Self
from pydantic import model_validator

from .request_models import Limits, RunContext, Selection
from .shared_models import (
    AtomBinding,
    ClosedModel,
    Digest,
    FileBinding,
    LimitName,
    Nonnegative,
    Path,
    Positive,
    SchemaVersion,
    SetList,
    String,
)


class Span(ClosedModel):
    start_line: Positive
    start_column: Positive
    end_line: Positive
    end_column: Positive

    @model_validator(mode="after")
    def ordered_coordinates(self) -> Self:
        if (self.start_line, self.start_column) > (self.end_line, self.end_column):
            raise ValueError("span end precedes start")
        return self


class Diagnostic(ClosedModel):
    code: String
    severity: Literal["error", "warning", "info"]
    path: Path | None
    span: Span | None
    property: String | None
    authority: SetList[AtomBinding]
    reason: String
    evidence: String | None


class Outcome(ClosedModel):
    code: String
    outcome: Literal["passed", "failed", "not_applicable", "not_checked"]
    authority: SetList[AtomBinding]
    reason: String
    finding_indexes: list[Nonnegative]


class Bindings(ClosedModel):
    methodology: SetList[AtomBinding]
    action: AtomBinding | None
    rules: SetList[AtomBinding]
    context: SetList[FileBinding]
    workflow: AtomBinding | None
    step: AtomBinding | None


class SelectionRecord(ClosedModel):
    path: Path | None
    atom_id: String | None
    reason: String


class ReportSelection(ClosedModel):
    requested: Selection | None
    source_roots: SetList[Path]
    selected: SetList[Path]
    excluded: list[SelectionRecord]
    unresolved: list[SelectionRecord]


class CarrierAssessment(ClosedModel):
    path: Path
    atom_id: String | None
    version: Positive | None
    sha256: Digest | None
    representation: Literal["source", "projected", "unresolved"]
    source_path: Path | None
    outcomes: list[Outcome]


class TargetCounts(ClosedModel):
    selected: Nonnegative
    assessed: Nonnegative
    excluded: Nonnegative
    unresolved: Nonnegative


class RuleCounts(ClosedModel):
    required: Nonnegative
    supported: Nonnegative
    unsupported: Nonnegative

    @model_validator(mode="after")
    def complete_count(self) -> Self:
        if self.required != self.supported + self.unsupported:
            raise ValueError("required count must equal supported plus unsupported")
        return self


class OutcomeCounts(ClosedModel):
    passed: Nonnegative
    failed: Nonnegative
    not_applicable: Nonnegative
    not_checked: Nonnegative


class Coverage(ClosedModel):
    targets: TargetCounts
    rules: RuleCounts
    outcomes: OutcomeCounts
    gaps: list[Diagnostic]


class Currentness(ClosedModel):
    state: Literal["unchanged", "changed", "unverified"]
    affected_inputs: SetList[FileBinding]


class Execution(ClosedModel):
    limits: Limits
    limit_sources: dict[LimitName, Literal["request", "instance", "default"]]
    stopped_by: LimitName | None
    diagnostics: list[Diagnostic]
    run_context: RunContext


class Report(ClosedModel):
    schema_version: SchemaVersion
    result: Literal["valid", "invalid", "incomplete", "error"]
    bindings: Bindings
    selection: ReportSelection
    coverage: Coverage
    carriers: list[CarrierAssessment]
    findings: list[Diagnostic]
    currentness: Currentness
    execution: Execution
