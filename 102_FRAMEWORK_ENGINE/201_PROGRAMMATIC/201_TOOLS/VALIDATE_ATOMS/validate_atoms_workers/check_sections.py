"""Fence-aware checks for named Atom body Properties."""

from __future__ import annotations

import re

from .authority import Record
from .check_support import Check, _plan


# Reviewed CA-D-479@6. The resolver admits these only for its exact source bytes.
ROLE_SECTIONS = {
    "Requirement": ("Scope", "Claim", "Details"),
    "Method": ("Scope", "Claim", "Details"),
    "Evaluation": ("Scope", "Claim", "Details"),
    "Delivery": ("Scope", "Claim", "Details"),
    "Analysis": ("Question", "Scope", "Approach", "Results", "TLDR"),
    "Concern": ("Concern", "Evidences", "Blast radius"),
    "Plan": ("Objective", "Details"),
    "Operations": ("Operation", "Details"),
}


def role_sections(metadata: Record, check: Check) -> list[tuple[int, str]] | None:
    role = metadata.get("content_role")
    if not isinstance(role, str) or role not in ROLE_SECTIONS:
        check.gap(
            "content_role",
            "Body layout needs a carried Content Role with a supported section contract.",
        )
        return None
    return [(1, "Summary"), *((2, name) for name in ROLE_SECTIONS[role])]


def _headings(body: str) -> list[tuple[int, str, int]]:
    headings: list[tuple[int, str, int]] = []
    fence: tuple[str, int] | None = None
    for index, line in enumerate(body.splitlines()):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = (token[0], len(token))
            elif token[0] == fence[0] and len(token) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        heading = re.match(r"^(#{1,6}) (.+)$", line)
        if fence is None and heading:
            headings.append((len(heading[1]), heading[2], index))
    return headings


def _sections(body: str, check: Check, required: list[tuple[int, str]]) -> None:
    headings = _headings(body)
    properties = [(level, title, index) for level, title, index in headings if level <= 2]
    positions = []
    for level, title in required:
        found = [
            index
            for found_level, found_title, index in properties
            if (found_level, found_title) == (level, title)
        ]
        if len(found) != 1:
            check.fail(
                "BODY_SECTION",
                title,
                "Required body section must occur exactly once: " + "#" * level + " " + title + ".",
            )
        else:
            positions.append(found[0])
    if positions != sorted(positions):
        check.fail("BODY_SECTION", "body", "Required body sections are out of order.")
    # Missing/duplicate Summary already has a cardinality diagnostic. Placement
    # is independently actionable only when exactly one Summary exists.
    summaries = [row for row in properties if row[:2] == (1, "Summary")]
    if len(summaries) == 1 and properties[0][:2] != (1, "Summary"):
        check.fail(
            "BODY_SECTION", "Summary", "Main Content must start with the literal # Summary heading."
        )
    _section_values(body, properties, required, check)


def _section_values(
    body: str, properties: list[tuple[int, str, int]], required: list[tuple[int, str]], check: Check
) -> None:
    lines = body.splitlines()
    if properties and any(line.strip() for line in lines[: properties[0][2]]):
        check.fail("BODY_SECTION", "body", "Main Content precedes the Summary heading.")
    for position, (level, title, index) in enumerate(properties):
        if (level, title) not in required:
            continue
        end = next(
            (row[2] for row in properties[position + 1 :] if row[0] <= level or title == "Summary"),
            len(lines),
        )
        if title != "Details" and not any(line.strip() for line in lines[index + 1 : end]):
            check.fail("BODY_SECTION", title, "Body Property value is empty: " + title + ".")


def _body(metadata: Record, body: str, check: Check) -> None:
    required = role_sections(metadata, check)
    if required is not None:
        _sections(body, check, required)


def plan_definition(body: str, check: Check) -> None:
    """CA-D-470@7: one nonempty level-three Property directly inside Details."""
    headings = _headings(body)
    matches = [row for row in headings if row[1] == "Definition of Done"]
    if len(matches) != 1:
        check.fail(
            "BODY_SECTION",
            "Definition of Done",
            "Plan requires exactly one nested Definition of Done section.",
        )
    for level, _, index in matches:
        parent = next(
            (row for row in reversed(headings) if row[2] < index and row[0] < level), None
        )
        if level != 3 or parent is None or parent[:2] != (2, "Details"):
            check.fail(
                "BODY_SECTION",
                "Definition of Done",
                "Definition of Done must be a level-three section directly inside Details.",
            )
        end = next(
            (row[2] for row in headings if row[2] > index and row[0] <= level),
            len(body.splitlines()),
        )
        if not any(line.strip() for line in body.splitlines()[index + 1 : end]):
            check.fail(
                "BODY_SECTION",
                "Definition of Done",
                "Definition of Done must contain its own value.",
            )


def _plan_sections(metadata: Record, body: str, check: Check) -> None:
    if not _plan(metadata, check):
        return
    required = [(1, "Summary"), (2, "Objective"), (2, "Details")]
    _sections(body, check, required)
    plan_definition(body, check)
    for field in ("summary", "claim", "objective", "definition_of_done", "details", "scope"):
        check.forbid(metadata, field)
