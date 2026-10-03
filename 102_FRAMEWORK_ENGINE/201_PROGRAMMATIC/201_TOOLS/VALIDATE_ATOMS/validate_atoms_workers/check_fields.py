"""Source-bound scalar, identity, and collection encodings."""

from __future__ import annotations

import re
from datetime import datetime
from typing import Any

from .authority import Record
from .check_support import Check, _integer, _string, _strings


def _common(metadata: Record, body: str, check: Check) -> None:
    del body
    for field in ("content_role", "current_scope_unit"):
        check.require(metadata, field, _string)
    role = metadata.get("content_role")
    if "type" in metadata:
        check.require(metadata, "type", _string)
    elif role not in ("Requirement", "Method", "Delivery"):
        check.require(metadata, "type", _string)
    check.require(metadata, "global_tier", _integer)
    if metadata.get("type") == "Goal":
        check.gap("local_tier", "Project Goal admission is required to decide Local Tier presence.")
    else:
        check.require(metadata, "local_tier", _string)
    for field in ("operators", "identifier", "summary", "claim"):
        check.forbid(metadata, field)


def _version(metadata: Record, body: str, check: Check) -> None:
    del body
    check.require(metadata, "version", lambda value: _integer(value) and value >= 1)


_TIMESTAMP = re.compile(
    r"\d{4}-\d{2}-\d{2}(?: \d{2}:\d{2}:\d{2}(?:\.\d+)? [+-]\d{4}|T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2}))\Z"
)


def _timestamp_valid(value: Any) -> bool:
    if not isinstance(value, str) or _TIMESTAMP.fullmatch(value) is None:
        return False
    offset = re.search(r"[+-](\d{2}):?(\d{2})$", value)
    if offset and (int(offset[1]) > 23 or int(offset[2]) > 59):
        return False
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).utcoffset() is not None
    except ValueError:
        return False


def _updated(metadata: Record, body: str, check: Check) -> None:
    del body
    check.require(metadata, "updated_at", _timestamp_valid)


def _scalar(metadata: Record, body: str, check: Check) -> None:
    del body
    field = check.obligation.code.rsplit(".", 1)[1]
    check.require(metadata, field, _string)
    if field == "claim_target_scope_unit":
        check.forbid(metadata, "claim_scope")


def _identity(metadata: Record, body: str, check: Check) -> None:
    del body
    status = metadata.get("status")
    if not _string(status):
        check.gap("atom_id", "Identity applicability requires a resolved carried Status.")
        return
    draft = status == "Draft"
    if metadata.get("content_role") == "Concern":
        domain = check.context.domains.get("domain.status.concern", ())
        if "draft" not in domain:
            check.gap(
                "atom_id", "Concern Draft classification requires its supported Status model."
            )
            return
        draft = status == "draft"
    if draft:
        check.forbid(metadata, "atom_id")
    else:
        check.require(metadata, "atom_id", _string)
    check.forbid(metadata, "identifier")


def _retired(metadata: Record, body: str, check: Check) -> None:
    del body
    for field in ("cce_version", "cce_form", "llm_session_ids"):
        if field in metadata:
            check.fail(
                "PROPERTY_RETIRED", field, "Retired Atom property is present: " + field + "."
            )


def _subjects(metadata: Record, body: str, check: Check) -> None:
    del body
    check.require(metadata, "subjects", lambda value: isinstance(value, dict))
    subjects = metadata.get("subjects")
    if not isinstance(subjects, dict):
        return
    if isinstance(subjects.get("governs"), dict):
        check.gap(
            "subjects.governs",
            "Legacy Subject encoding requires explicit migration-status authority.",
        )
        return
    check.require(subjects, "governs", _string)
    if not _strings(subjects.get("depends_on", [])):
        check.fail(
            "PROPERTY_TYPE",
            "subjects.depends_on",
            "Subject dependencies must be unique nonempty strings.",
        )
    if set(subjects) - {"governs", "depends_on"}:
        check.fail("PROPERTY_UNADMITTED", "subjects", "Subjects contains an unadmitted nested key.")


def _relations(metadata: Record, body: str, check: Check) -> None:
    del body
    relations = metadata.get("relations", {})
    if not isinstance(relations, dict):
        check.fail("PROPERTY_TYPE", "relations", "Relations must be a mapping.")
        return
    for kind, targets in relations.items():
        if not _string(kind) or not _strings(targets) or not targets:
            check.fail(
                "PROPERTY_TYPE",
                "relations",
                "Each Relation Kind must carry a nonempty collection of unique string targets.",
            )
