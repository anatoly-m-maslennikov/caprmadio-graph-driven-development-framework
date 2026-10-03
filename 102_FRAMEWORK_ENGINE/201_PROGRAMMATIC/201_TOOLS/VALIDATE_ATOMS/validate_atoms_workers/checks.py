"""Stable carrier-check facade; unresolved meaning remains a coverage gap."""

from __future__ import annotations

from .authority import AuthorityContext, Record
from .check_dispatch import ADAPTER_CODES as ADAPTER_CODES
from .check_dispatch import ADAPTERS as ADAPTERS
from .check_dispatch import _execute


def validate_carrier(
    metadata: Record, body: str, context: AuthorityContext, inputs: Record | None = None
) -> Record:
    findings: list[Record] = []
    gaps = list(context.gaps)
    outcomes = []
    for obligation in context.obligations:
        outcome, found, missing = _execute(obligation, metadata, body, context, inputs)
        outcome["finding_indexes"] = list(range(len(findings), len(findings) + len(found)))
        findings.extend(found)
        gaps.extend(missing)
        outcomes.append(outcome)
    return {"outcomes": outcomes, "findings": findings, "gaps": gaps}
