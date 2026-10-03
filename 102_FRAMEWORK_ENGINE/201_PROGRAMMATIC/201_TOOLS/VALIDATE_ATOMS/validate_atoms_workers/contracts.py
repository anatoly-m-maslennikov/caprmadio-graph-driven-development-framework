"""Pure JSON admission and report envelopes for CA-D-492@3/CA-D-493@3.

Paths are normalized lexically; no boundary function reads supplied paths.
"""

from __future__ import annotations

from collections import Counter
import json
import math
from typing import Any

from .request_models import Limits, Request, RunContext
from .result_models import (
    Bindings,
    Coverage,
    Currentness,
    Diagnostic,
    Execution,
    OutcomeCounts,
    Report,
    ReportSelection,
    RuleCounts,
    TargetCounts,
)


def _unique_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _request_json_values(value: Any) -> None:
    if value is None or (isinstance(value, float) and not math.isfinite(value)):
        raise ValueError("null and non-finite numbers are not admitted")
    if isinstance(value, dict):
        for child in value.values():
            _request_json_values(child)
    elif isinstance(value, list):
        for child in value:
            _request_json_values(child)


def parse_request(text: str) -> Request:
    """Admit JSON syntax or raise ValueError, without reading any supplied path."""
    try:
        payload = json.loads(text, object_pairs_hook=_unique_keys)
        _request_json_values(payload)
        return Request.model_validate(payload)
    except RecursionError as exc:
        raise ValueError("request nesting exceeds parser capacity") from exc


def _consistent_outcomes(report: Report) -> None:
    outcomes = [outcome for carrier in report.carriers for outcome in carrier.outcomes]
    totals: Counter[str] = Counter(outcome.outcome for outcome in outcomes)
    if any(totals[name] != count for name, count in report.coverage.outcomes.model_dump().items()):
        raise ValueError("outcome totals disagree with carrier assessments")
    for outcome in outcomes:
        if any(index >= len(report.findings) for index in outcome.finding_indexes):
            raise ValueError("finding index is outside the findings list")
        if outcome.outcome == "failed" and not any(
            report.findings[index].severity == "error" for index in outcome.finding_indexes
        ):
            raise ValueError("a failed check requires an error finding")
    return None


def _consistent_targets(report: Report) -> None:
    actual = {
        "selected": len(report.selection.selected),
        "assessed": sum(bool(carrier.outcomes) for carrier in report.carriers),
        "excluded": len(report.selection.excluded),
        "unresolved": len(report.selection.unresolved),
    }
    if report.coverage.targets.model_dump() != actual:
        raise ValueError("target counts disagree with selected and assessed carriers")
    return None


def _valid_requires_complete_assessment(report: Report) -> None:
    if report.result == "valid" and (
        not report.selection.selected
        or report.currentness.state != "unchanged"
        or report.coverage.gaps
        or report.coverage.rules.unsupported
        or report.coverage.outcomes.failed
        or report.coverage.outcomes.not_checked
        or report.coverage.targets.assessed != report.coverage.targets.selected
        or report.coverage.targets.unresolved
    ):
        raise ValueError("valid requires nonempty, complete, unchanged assessment")
    return None


def validate_report(report: dict[str, Any]) -> dict[str, Any]:
    """Validate the complete result boundary, preserving absent optional members."""
    accepted = Report.model_validate(report)
    _consistent_outcomes(accepted)
    _consistent_targets(accepted)
    _valid_requires_complete_assessment(accepted)
    return accepted.model_dump(mode="json", exclude_unset=True)


def empty_report() -> dict[str, Any]:
    """Return a fresh unexecuted CA-D-493 error envelope with no fabricated facts."""
    return Report(
        schema_version=1,
        result="error",
        bindings=Bindings(
            methodology=[], action=None, rules=[], context=[], workflow=None, step=None
        ),
        selection=ReportSelection(
            requested=None, source_roots=[], selected=[], excluded=[], unresolved=[]
        ),
        coverage=Coverage(
            targets=TargetCounts(selected=0, assessed=0, excluded=0, unresolved=0),
            rules=RuleCounts(required=0, supported=0, unsupported=0),
            outcomes=OutcomeCounts(passed=0, failed=0, not_applicable=0, not_checked=0),
            gaps=[],
        ),
        carriers=[],
        findings=[],
        currentness=Currentness(state="unverified", affected_inputs=[]),
        execution=Execution(
            limits=Limits(),
            limit_sources={},
            stopped_by=None,
            diagnostics=[],
            run_context=RunContext(),
        ),
    ).model_dump(mode="json", exclude_unset=True)


def request_error_report() -> dict[str, Any]:
    """Return the stable, content-free malformed-request diagnostic envelope."""
    report = empty_report()
    report["execution"]["diagnostics"] = [
        Diagnostic(
            code="REQUEST_INVALID",
            severity="error",
            path=None,
            span=None,
            property=None,
            authority=[],
            reason="Request does not conform to CA-D-492.",
            evidence=None,
        ).model_dump(mode="json")
    ]
    return report
