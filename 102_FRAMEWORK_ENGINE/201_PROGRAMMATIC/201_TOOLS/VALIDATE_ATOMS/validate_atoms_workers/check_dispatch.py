"""Dispatch only adapters admitted by the resolved source inventory."""

from __future__ import annotations

from typing import Callable

from .authority import AuthorityContext, Obligation, Record
from .check_support import Check
from .check_fields import (
    _common,
    _version,
    _updated,
    _scalar,
    _identity,
    _retired,
    _subjects,
    _relations,
)
from .check_sections import _body, _plan_sections
from .check_domains import _priority, _plan_override, _plan_relations, _domain_check
from .check_schema_extended import ADAPTERS as SCHEMA_ADAPTERS
from .check_graph_extended import ADAPTERS as GRAPH_ADAPTERS
from .check_structure_extended import ADAPTERS as STRUCTURE_ADAPTERS
from .check_context_extended import ADAPTERS as CONTEXT_ADAPTERS
from .check_operators import author_membership


ADAPTERS: dict[str, Callable[[Record, str, Check], None]] = {
    "frontmatter.common_encoding": _common,
    "frontmatter.version": _version,
    "frontmatter.updated_at": _updated,
    "frontmatter.author": _scalar,
    "author.resolution": author_membership,
    "frontmatter.claim_target_scope_unit": _scalar,
    "frontmatter.status": _scalar,
    "frontmatter.atom_id": _identity,
    "property.retired_fields": _retired,
    "frontmatter.subjects": _subjects,
    "frontmatter.relations": _relations,
    "body.sections": _body,
    "plan.sections": _plan_sections,
    "concern.priority": _priority,
    "plan.confidence_override": _plan_override,
    "plan.assignee": _plan_override,
    "plan.retry_limit": _plan_override,
    "plan.decomposition": _plan_relations,
    "plan.blocking": _plan_relations,
}
for _code in (
    "domain.content_role",
    "domain.type.concern",
    "domain.type.analysis",
    "domain.type.operations",
    "domain.status.requirement",
    "domain.status.method",
    "domain.status.evaluation",
    "domain.status.delivery",
    "domain.status.plan",
    "domain.status.concern",
    "domain.local_tier",
):
    ADAPTERS[_code] = _domain_check
for _group in (SCHEMA_ADAPTERS, GRAPH_ADAPTERS, STRUCTURE_ADAPTERS, CONTEXT_ADAPTERS):
    ADAPTERS.update(_group)
ADAPTER_CODES = frozenset(ADAPTERS)


def _execute(
    obligation: Obligation,
    metadata: Record,
    body: str,
    context: AuthorityContext,
    inputs: Record | None = None,
) -> tuple[Record, list[Record], list[Record]]:
    check = Check(obligation, context, inputs)
    if obligation.supported:
        ADAPTERS[obligation.code](metadata, body, check)
    state = "not_checked"
    reason = obligation.reason
    if obligation.supported:
        state = "passed" if check.applicable else "not_applicable"
        if check.gaps:
            state, reason = (
                "not_checked",
                "Required applicability or reference authority is unresolved.",
            )
        if check.findings:
            state, reason = "failed", "Mandatory source-bound condition failed."
    record = {
        "code": obligation.code,
        "outcome": state,
        "authority": check.obligation.authority,
        "reason": reason,
        "finding_indexes": [],
    }
    return record, check.findings, check.gaps
