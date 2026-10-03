"""Shared check state and primitive applicability predicates."""

from __future__ import annotations

from typing import Any, Callable

from .authority import AuthorityContext, Obligation, Record, diagnostic


class Check:
    def __init__(
        self, obligation: Obligation, context: AuthorityContext, inputs: Record | None = None
    ) -> None:
        self.obligation = obligation
        self.context = context
        self.inputs: Record = inputs or {}
        self.findings: list[Record] = []
        self.gaps: list[Record] = []
        self.applicable = True

    def fail(self, code: str, field: str, reason: str) -> None:
        self.findings.append(diagnostic(code, reason, self.obligation.authority, field))

    def gap(self, field: str, reason: str) -> None:
        self.gaps.append(
            diagnostic("AUTHORITY_UNSUPPORTED", reason, self.obligation.authority, field)
        )

    def require(self, metadata: Record, field: str, predicate: Callable[[Any], bool]) -> None:
        if field not in metadata:
            self.fail("PROPERTY_REQUIRED", field, "Required property is missing: " + field + ".")
        elif not predicate(metadata[field]):
            self.fail(
                "PROPERTY_TYPE",
                field,
                "Property has an invalid value type or encoding: " + field + ".",
            )

    def forbid(self, metadata: Record, field: str) -> None:
        if field in metadata:
            self.fail(
                "PROPERTY_UNADMITTED",
                field,
                "Property is forbidden in this location: " + field + ".",
            )


def _string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _integer(value: Any) -> bool:
    return type(value) is int


def _strings(value: Any) -> bool:
    return (
        isinstance(value, list) and all(_string(v) for v in value) and len(set(value)) == len(value)
    )


def _plan(metadata: Record, check: Check) -> bool:
    if "content_role" not in metadata:
        check.gap("content_role", "Plan applicability requires a carried Content Role.")
        return False
    check.applicable = metadata["content_role"] == "Plan"
    if check.applicable and metadata.get("type") != "Plan":
        check.gap(
            "type",
            "Plan applicability requires the admitted Plan Type or supported subtype authority.",
        )
        return False
    return check.applicable
