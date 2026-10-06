"""Merge evidence from focused prompts; this module does not evaluate Atom meaning."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from review_evidence import (ReviewContext, probability, strings, text,
                            validate_obligations, validate_subject_inventory)
from report_quality import validate_report_quality
from semantic_boundaries import validate_boundaries

GROUPS = {
    "cce": ("cce",),
    "properties": ("properties",),
    "coherence": ("subjects", "scope", "claim", "details", "governed_entity",
                  "content_role", "alignment", "summary"),
}

# Contracts 4/5 retain their full-audit meaning for historical evidence.
LOCAL_GROUPS = {
    "cce": ("cce",),
    "properties": ("properties",),
    "coherence": ("scope", "claim", "details", "summary"),
}


def groups_for(contract_version: int) -> dict[str, tuple[str, ...]]:
    return LOCAL_GROUPS if contract_version == 6 else GROUPS


def _result(checks: list[dict[str, Any]]) -> str:
    statuses = {row["status"] for row in checks}
    return "failed" if "failed" in statuses else "blocked" if "blocked" in statuses else "passed"


def _validate_binding(part: dict[str, Any]) -> None:
    source = part.get("source")
    if not isinstance(source, dict) or not {"atom_id", "version", "path", "sha256"} <= source.keys():
        raise ValueError("missing source binding")
    for digest in (source.get("sha256"), part.get("context_sha256")):
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            raise ValueError("invalid source/context digest")
    if not isinstance(source["path"], str) or not source["path"]:
        raise ValueError("missing source path")


def _validate_finding(finding: Any, threshold: float) -> None:
    required = ("location", "excerpt", "reason", "proposed_fix")
    if not isinstance(finding, dict) or any(not text(finding.get(k)) for k in required):
        raise ValueError("incomplete finding")
    confidence = finding.get("confidence")
    if not probability(confidence):
        raise ValueError("invalid finding confidence")
    if confidence < threshold:
        raise ValueError("finding is below the caller confidence threshold")
    if finding.get("kind") not in ("violation", "omission"):
        raise ValueError("finding must identify violation or omission")


def _validate_check_evidence(row: dict[str, Any], authorities: dict[str, str]) -> None:
    for key in ("evidence", "authority", "findings"):
        if not isinstance(row.get(key), list):
            raise ValueError("invalid check evidence")
    if not strings(row["evidence"]):
        raise ValueError("unsupported conclusion")
    if not strings(row["authority"], empty=True) or any(ref not in authorities for ref in row["authority"]):
        raise ValueError("invalid or unbound check authority")


def _validate_check(row: dict[str, Any], threshold: float, authorities: dict[str, str]) -> None:
    if row.get("status") not in ("passed", "failed", "blocked"):
        raise ValueError("unknown check result")
    _validate_check_evidence(row, authorities)
    if row["status"] != "blocked" and not row["authority"]:
        raise ValueError("non-blocked conclusion without authority")
    if row["status"] == "failed" and not row["findings"]:
        raise ValueError("failure without a finding")
    if row["status"] == "passed" and row["findings"]:
        raise ValueError("pass with unresolved findings")
    for finding in row["findings"]:
        _validate_finding(finding, threshold)
    if row["findings"] and not row["authority"]:
        raise ValueError("known findings need authority even on a blocked check")
    validate_obligations(row, authorities)


def _part_checks(part: dict[str, Any]) -> list[dict[str, Any]]:
    if not isinstance(part, dict):
        raise ValueError("expected evaluation object")
    if type(part.get("contract_version")) is not int or part["contract_version"] not in (4, 5, 6):
        raise ValueError("contract_version 4, 5 or 6 required; preserve legacy reports without upgrading them")
    if part['contract_version'] == 6 and part.get('review_profile') != 'atom_local':
        raise ValueError('contract 6 requires the atom_local review profile')
    groups = groups_for(part['contract_version'])
    group = part.get("evaluator")
    if not isinstance(group, str) or group not in groups:
        raise ValueError("unknown evaluator")
    checks = part.get("checks")
    if not isinstance(checks, list) or any(not isinstance(row, dict) for row in checks):
        raise ValueError("invalid checklist")
    ids = [row.get("id") for row in checks]
    if any(not isinstance(key, str) for key in ids) or sorted(ids) != sorted(groups[group]):
        raise ValueError("incomplete, duplicate, or foreign checks")
    for key in ("authority_sources", "coverage_gaps", "mechanical_evidence"):
        if not isinstance(part.get(key), list):
            raise ValueError("missing evidence collection: " + key)
    return checks


def _validate_gaps(part: dict[str, Any], checks: list[dict[str, Any]], context: ReviewContext) -> None:
    gap_ids = set()
    for gap in part["coverage_gaps"]:
        if not isinstance(gap, dict) or not text(gap.get("reason")) or not text(gap.get("check_id")):
            raise ValueError("gap needs check_id and reason")
        if gap.get('kind') not in ('missing_context', 'unresolved_interpretation', 'reviewer_incomplete',
                                   'layout_dependency', 'conflicting_authority'):
            raise ValueError('gap must distinguish context, interpretation, unfinished review, layout or conflict')
        if gap['kind'] == 'missing_context':
            key = gap.get('context_key')
            if not isinstance(key, str) or key not in context.preflight:
                raise ValueError('missing context must name a caller preflight record')
            if context.preflight[key]['state'] == 'available':
                raise ValueError('available context cannot be reported missing')
        gap_ids.add(gap["check_id"])
    blocked = {row["id"] for row in checks if row["status"] == "blocked"}
    if gap_ids != blocked:
        raise ValueError("coverage gaps and blocked checks disagree")


def validate_part(part: dict[str, Any], *, context: ReviewContext,
                  allow_layout_gaps: bool = False) -> None:
    """Reject missing, contradictory, or unsupported structured conclusions."""
    checks = _part_checks(part)
    if part['contract_version'] != context.report_contract:
        raise ValueError('report contract does not match caller context; perform a fresh review')
    _validate_binding(part)
    if part["context_sha256"] != context.sha256:
        raise ValueError("response does not match caller context")
    source_text = context.candidate_text(part["source"])
    authorities = context.authorities(part["authority_sources"], candidate=part['source'])
    admitted_principles = context.admitted_principle_references(
        part["authority_sources"], candidate=part['source'])
    for row in checks:
        _validate_check(row, context.confidence_threshold, authorities)
        if part['contract_version'] == 6 and 'subject_inventory' in row:
            raise ValueError('Subject inventories are outside the atom_local profile')
        if row["id"] == "subjects":
            validate_subject_inventory(row, source_text, authorities, context.authority_targets(authorities),
                                       candidate_binding=part['source'],
                                       admitted_legacy_principles=admitted_principles,
                                       authority_paths=context.authority_paths(
                                           part['authority_sources'], candidate=part['source']))
            if not row['subject_inventory']['complete']:
                gaps = [g for g in part['coverage_gaps'] if isinstance(g, dict) and g.get('check_id') == 'subjects']
                if not gaps:
                    raise ValueError('incomplete inventory needs a subjects gap')
    _validate_gaps(part, checks, context)
    validate_report_quality(part, source_text, authorities=authorities)
    if context.operator_precheck is not None:
        from operator_precheck import validate_operator_coverage
        for check in part['checks']:
            if check['id'] == 'cce':
                validate_operator_coverage(check, source_text, context.operator_precheck)
    validate_boundaries(part, source_text, allow_layout_gaps=allow_layout_gaps)
    if part.get("result") != _result(checks):
        raise ValueError("overall result contradicts checklist")


def merge_evaluations(parts: list[dict[str, Any]], *, context: ReviewContext,
                      allow_layout_gaps: bool = False) -> dict[str, Any]:
    """Return one report evaluation, retaining each part and every blocker.

    The caller must compare bindings to actual current bytes before and after
    review. Equality here cannot establish filesystem freshness or truth.
    """
    groups = groups_for(context.report_contract)
    if len(parts) != len(groups):
        raise ValueError("one result from every evaluator is required")
    for part in parts:
        validate_part(part, context=context, allow_layout_gaps=allow_layout_gaps)
    if {part["evaluator"] for part in parts} != set(groups):
        raise ValueError("missing or repeated evaluator")
    first = parts[0]
    for part in parts[1:]:
        if part["source"] != first["source"] or part["context_sha256"] != first["context_sha256"]:
            raise ValueError("mixed source revisions or context snapshots")
    ordered = [next(part for part in parts if part["evaluator"] == group) for group in groups]
    checks = [row for part in ordered for row in part["checks"]]
    result = {"contract_version": first['contract_version'], "source": first["source"], "context_sha256": first["context_sha256"],
              "checks": checks, "result": _result(checks), "parts": ordered}
    if context.report_contract == 6:
        result['review_profile'] = 'atom_local'
    for field in ("authority_sources", "coverage_gaps", "mechanical_evidence"):
        values: list[Any] = []
        for part in ordered:
            for value in part[field]:
                if value not in values:
                    values.append(value)
        result[field] = values
    return deepcopy(result)


def summarize_evaluations(evaluations: list[dict[str, Any]], *, context: ReviewContext,
                          allow_layout_gaps: bool = False) -> dict[str, Any]:
    """Summarize validated records, not truth; reviewers must confirm findings.

    A blocked check can contain known defects. Count them separately from gaps
    instead of turning partial coverage into either a pass or invented errors.
    Require one evaluation per source; callers select the intended attempt.
    """
    summary: dict[str, Any] = {
        "atoms": 0, "fully_passed_atoms": 0, "atoms_with_confirmed_findings": 0,
        "atoms_with_coverage_gaps": 0, "check_counts": {
            check: {"passed": 0, "failed": 0, "blocked": 0,
                    "atoms_with_findings": 0, "findings": 0}
            for checks in groups_for(context.report_contract).values() for check in checks
        },
    }
    if context.report_contract == 6:
        summary['review_profile'] = 'atom_local'
    seen: set[str] = set()
    for evaluation in evaluations:
        if not isinstance(evaluation, dict) or not isinstance(evaluation.get("parts"), list):
            raise ValueError("summary requires merged evaluation records")
        merged = merge_evaluations(evaluation["parts"], context=context,
                                   allow_layout_gaps=allow_layout_gaps)
        if any(evaluation.get(key) != value for key, value in merged.items()):
            raise ValueError("merged evaluation contradicts its raw parts")
        path = merged["source"]["path"]
        if path in seen:
            raise ValueError("summary contains repeated source path")
        seen.add(path)
        summary["atoms"] += 1
        summary["fully_passed_atoms"] += merged["result"] == "passed"
        summary["atoms_with_coverage_gaps"] += bool(merged["coverage_gaps"])
        summary["atoms_with_confirmed_findings"] += any(c["findings"] for c in merged["checks"])
        for check in merged["checks"]:
            counts = summary["check_counts"][check["id"]]
            counts[check["status"]] += 1
            counts["atoms_with_findings"] += bool(check["findings"])
            counts["findings"] += len(check["findings"])
    return summary
