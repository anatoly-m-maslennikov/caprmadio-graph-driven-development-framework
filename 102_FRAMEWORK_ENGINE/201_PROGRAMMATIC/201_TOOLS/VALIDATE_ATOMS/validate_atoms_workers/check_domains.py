"""Conditional Plan fields and source-resolved value domains."""

from __future__ import annotations

from .authority import Record
from .check_support import Check, _integer, _plan, _string, _strings


def _priority(metadata: Record, body: str, check: Check) -> None:
    del body
    if "content_role" not in metadata:
        check.gap("priority", "Priority applicability requires a carried Content Role.")
    elif metadata["content_role"] == "Concern":
        check.require(metadata, "priority", lambda value: value in ("high", "medium", "low"))
    else:
        check.forbid(metadata, "priority")


def _plan_override(metadata: Record, body: str, check: Check) -> None:
    del body
    if not _plan(metadata, check):
        return
    fields = {
        "plan.confidence_override": ("autonomous_confidence_threshold", _integer),
        "plan.assignee": ("assignee", _string),
        "plan.retry_limit": ("implementation_retry_limit", _integer),
    }
    field, predicate = fields[check.obligation.code]
    if field in metadata:
        check.require(metadata, field, predicate)
    check.forbid(metadata, "epic_overrides")


def _plan_relations(metadata: Record, body: str, check: Check) -> None:
    del body
    if not _plan(metadata, check):
        return
    relations = metadata.get("relations", {})
    if not isinstance(relations, dict):
        check.fail("PROPERTY_TYPE", "relations", "Relations must be a mapping.")
        return
    field = "is_decomposition_of" if check.obligation.code == "plan.decomposition" else "blocks"
    targets = relations.get(field, [])
    if not _strings(targets) or (field == "is_decomposition_of" and len(targets) > 1):
        check.fail(
            "PROPERTY_TYPE",
            "relations." + field,
            "Plan relation has invalid cardinality or targets.",
        )
    forbidden = (
        ("decomposes_into",) if field == "is_decomposition_of" else ("blocked_by", "depends_on")
    )
    for inverse in forbidden:
        check.forbid(relations, inverse)


def _domain_check(metadata: Record, body: str, check: Check) -> None:
    del body
    parts = check.obligation.code.split(".")
    field = parts[1]
    if len(parts) == 3 and "content_role" not in metadata:
        check.gap("content_role", "Domain applicability requires a carried Content Role.")
        return
    if len(parts) == 3 and str(metadata.get("content_role", "")).lower() != parts[2]:
        check.applicable = False
        return
    if field == "local_tier" and metadata.get("type") == "Goal":
        check.gap(field, "Project Goal admission is required to resolve Local Tier applicability.")
        return
    if (
        check.context.unclassified_sources
        and metadata.get(field) not in check.context.domains[check.obligation.code]
    ):
        check.gap(
            field, "Unclassified methodology sources prevent complete domain membership resolution."
        )
        return
    check.require(
        metadata, field, lambda value: value in check.context.domains[check.obligation.code]
    )
