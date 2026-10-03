"""Lossless scoped frontmatter edits for CA-R-1049 and CA-M-156."""

from __future__ import annotations

import re
from collections.abc import Mapping

from .models import RebindError, Request


TOP_LEVEL = re.compile(r"^([a-z][a-z0-9_]*):(?:[ \t]*(.*))?\n?$")
RELATION = re.compile(r"^  ([a-z][a-z0-9_]*):\s*\n?$")
TARGET = re.compile(r"^    - (\S.*?)\s*\n?$")


def split_document(source: bytes) -> tuple[str, str]:
    """Split UTF-8 CCE frontmatter while keeping the Markdown body untouched."""
    try:
        text = source.decode("utf-8")
    except UnicodeDecodeError as error:
        raise RebindError("source-encoding-invalid", "source carrier must be UTF-8") from error
    if not text.startswith("---\n"):
        raise RebindError("frontmatter-invalid", "source carrier must begin with YAML frontmatter")
    boundary = text.find("\n---\n", 4)
    if boundary < 0:
        raise RebindError("frontmatter-invalid", "source carrier has no closed YAML frontmatter")
    return text[4:boundary], text[boundary + 5 :]


def fields(frontmatter: str) -> dict[str, tuple[int, int, str]]:
    """Locate complete top-level YAML blocks without re-rendering untouched data."""
    lines = frontmatter.splitlines(keepends=True)
    starts = [(match.group(1), index) for index, line in enumerate(lines) if (match := TOP_LEVEL.fullmatch(line))]
    names = [name for name, _ in starts]
    if len(names) != len(set(names)):
        raise RebindError("frontmatter-duplicate-field", "frontmatter contains duplicate top-level fields")
    return {
        name: (start, starts[index + 1][1] if index + 1 < len(starts) else len(lines), "".join(lines[start:(starts[index + 1][1] if index + 1 < len(starts) else len(lines))]))
        for index, (name, start) in enumerate(starts)
    }


def validate_revision(frontmatter: str, request: Request) -> None:
    """Require an exact source version and an existing declared update timestamp."""
    blocks = fields(frontmatter)
    if _scalar(blocks, "version") != str(request.expected_version):
        raise RebindError("source-version-mismatch", "source version differs from expected_source_version")
    _scalar(blocks, "updated_at")


def rebind_relations(frontmatter: str, request: Request, active_ids: frozenset[str]) -> str:
    """Apply only declared target replacements and removals to one relations block."""
    blocks = fields(frontmatter)
    if "relations" not in blocks:
        raise RebindError("relation-mismatch", "source has no relations field")
    _validate_new_targets(request, active_ids)
    start, end, raw = blocks["relations"]
    lines = raw.splitlines(keepends=True)
    entries, headers = _relation_entries(lines)
    _validate_requested_targets(entries, request)
    deleted = _delete_indexes(entries, headers, request)
    rewritten = _rewrite_lines(lines, entries, request)
    replacement = _retained_relation_block(rewritten, deleted)
    document_lines = frontmatter.splitlines(keepends=True)
    document_lines[start:end] = [replacement] if replacement else []
    return "".join(document_lines)


def update_revision(frontmatter: str, request: Request) -> str:
    """Change exactly version and updated_at, each once, in their existing fields."""
    blocks = fields(frontmatter)
    lines = frontmatter.splitlines(keepends=True)
    replacements = {"version": str(request.expected_version + 1), "updated_at": request.updated_at}
    for name, value in replacements.items():
        start, end, _ = blocks[name]
        lines[start:end] = [f"{name}: {value}\n"]
    return "".join(lines)


def assert_declared_delta(before: str, after: str, body: str, request: Request) -> None:
    """Fail if the plan changed body or any frontmatter beyond declared fields."""
    if not isinstance(body, str):
        raise RebindError("undeclared-mutation", "source body is not preserved")
    original, revised = fields(before), fields(after)
    for name in set(original) | set(revised):
        if name not in {"relations", "version", "updated_at"} and original.get(name) != revised.get(name):
            raise RebindError("undeclared-mutation", f"undeclared frontmatter mutation: {name}")
    if _scalar(revised, "version") != str(request.expected_version + 1) or _scalar(revised, "updated_at") != request.updated_at:
        raise RebindError("undeclared-mutation", "revision metadata differs from the sealed request")


def _scalar(blocks: Mapping[str, tuple[int, int, str]], name: str) -> str:
    """Read one unambiguous scalar without accepting nested YAML."""
    if name not in blocks:
        raise RebindError("frontmatter-invalid", f"frontmatter field is absent: {name}")
    lines = blocks[name][2].splitlines()
    match = TOP_LEVEL.fullmatch((lines[0] if len(lines) == 1 else "") + "\n")
    if not match or not match.group(2):
        raise RebindError("frontmatter-invalid", f"{name} must be a one-line scalar")
    return match.group(2).strip().strip('"')


def _validate_new_targets(request: Request, active_ids: frozenset[str]) -> None:
    """Require each requested replacement target to be a unique active Atom ID."""
    missing = sorted({new for targets in request.rewrite_map.values() for new in targets.values()} - active_ids)
    if missing:
        raise RebindError("new-target-not-active", f"new relation targets are not unique active canonical Atoms: {', '.join(missing)}")


def _relation_entries(lines: list[str]) -> tuple[dict[tuple[str, str], list[int]], dict[str, int]]:
    """Parse only the canonical nested relation-list form used by active Atoms."""
    if not lines or lines[0] != "relations:\n":
        raise RebindError("relations-invalid", "relations must use a canonical nested target-list YAML block")
    entries: dict[tuple[str, str], list[int]] = {}
    headers: dict[str, int] = {}
    current: str | None = None
    for index, line in enumerate(lines[1:], 1):
        header, target = RELATION.fullmatch(line), TARGET.fullmatch(line)
        if header:
            current = header.group(1)
            if current in headers:
                raise RebindError("relations-invalid", "relations must not repeat a relation name")
            headers[current] = index
        elif target and current:
            entries.setdefault((current, target.group(1)), []).append(index)
        elif line.strip():
            raise RebindError("relations-invalid", "relations must use canonical nested target-list YAML")
    if set(headers) - {relation for relation, _ in entries}:
        raise RebindError("relations-invalid", "relations must not contain an empty relation header")
    return entries, headers


def _validate_requested_targets(entries: Mapping[tuple[str, str], list[int]], request: Request) -> None:
    """Require each named old target to occur exactly once under its relation."""
    requested = {(relation, old) for relation, targets in request.rewrite_map.items() for old in targets}
    requested |= {(relation, old) for relation, targets in request.removal_map.items() for old in targets}
    for relation, old in sorted(requested):
        count = len(entries.get((relation, old), []))
        if count != 1:
            code = "relation-target-missing" if count == 0 else "relation-target-repeated"
            raise RebindError(code, f"relation target must occur exactly once: {relation} -> {old}")


def _delete_indexes(entries: Mapping[tuple[str, str], list[int]], headers: Mapping[str, int], request: Request) -> set[int]:
    """Select removals and now-empty relation headers without touching other targets."""
    deleted = {entries[(relation, old)][0] for relation, targets in request.removal_map.items() for old in targets}
    retained = {relation: 0 for relation in headers}
    for (relation, _), indexes in entries.items():
        retained[relation] += sum(index not in deleted for index in indexes)
    deleted |= {headers[relation] for relation, count in retained.items() if count == 0}
    return deleted


def _rewrite_lines(lines: list[str], entries: Mapping[tuple[str, str], list[int]], request: Request) -> list[str]:
    """Replace each named target in place, keeping untouched source lines unchanged."""
    output = list(lines)
    for relation, targets in request.rewrite_map.items():
        for old, new in targets.items():
            output[entries[(relation, old)][0]] = f"    - {new}\n"
    return output


def _retained_relation_block(lines: list[str], deleted: set[int]) -> str:
    """Drop empty relation headers and remove the entire field when now empty."""
    retained = [line for index, line in enumerate(lines) if index not in deleted]
    return "" if len(retained) == 1 else "".join(retained)
