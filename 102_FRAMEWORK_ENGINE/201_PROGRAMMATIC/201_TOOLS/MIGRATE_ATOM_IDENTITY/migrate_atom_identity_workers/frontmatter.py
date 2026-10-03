"""Lossless-enough YAML frontmatter edits for CA-R-1048 and CA-M-155."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping
from typing import Any

from .models import MigrationError


TOP_LEVEL = re.compile(r"^([a-z][a-z0-9_]*):(?:[ \t]*(.*))?\n?$")
RELATION = re.compile(r"^  ([a-z][a-z0-9_]*):\s*\n?$")
TARGET = re.compile(r"^    - (\S.*?)\s*\n?$")
TIMESTAMP = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")


def split_document(source: bytes) -> tuple[str, str]:
    """Split canonical YAML frontmatter without rewriting the Markdown body."""
    try:
        text = source.decode("utf-8")
    except UnicodeDecodeError as error:
        raise MigrationError("source-encoding-invalid", "source carrier must be UTF-8") from error
    if not text.startswith("---\n"):
        raise MigrationError("frontmatter-invalid", "source carrier must begin with YAML frontmatter")
    boundary = text.find("\n---\n", 4)
    if boundary < 0:
        raise MigrationError("frontmatter-invalid", "source carrier has no closed YAML frontmatter")
    return text[4:boundary], text[boundary + 5 :]


def fields(frontmatter: str) -> dict[str, tuple[int, int, str]]:
    """Locate top-level YAML blocks while preserving all untouched blocks verbatim."""
    lines = frontmatter.splitlines(keepends=True)
    starts: list[tuple[str, int]] = []
    for index, line in enumerate(lines):
        match = TOP_LEVEL.fullmatch(line)
        if match:
            starts.append((match.group(1), index))
    names = [name for name, _ in starts]
    if len(names) != len(set(names)):
        raise MigrationError("frontmatter-duplicate-field", "frontmatter contains duplicate top-level fields")
    result: dict[str, tuple[int, int, str]] = {}
    for index, (name, start) in enumerate(starts):
        end = starts[index + 1][1] if index + 1 < len(starts) else len(lines)
        result[name] = start, end, "".join(lines[start:end])
    return result


def scalar(block: str, field: str) -> str:
    """Read one required scalar field and reject nested or ambiguous YAML."""
    lines = block.splitlines()
    if len(lines) != 1:
        raise MigrationError("frontmatter-invalid", f"{field} must be a one-line scalar")
    match = TOP_LEVEL.fullmatch(lines[0] + "\n")
    if not match or match.group(1) != field or not match.group(2):
        raise MigrationError("frontmatter-invalid", f"{field} must be a non-empty scalar")
    return match.group(2).strip().strip('"')


def render_value(value: Any, indent: str = "") -> list[str]:
    """Render only JSON-compatible scalar, list, and object update values."""
    if value is None:
        return [indent + "null"]
    if isinstance(value, bool):
        return [indent + str(value).lower()]
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return [indent + str(value)]
    if isinstance(value, str):
        return [indent + json.dumps(value, ensure_ascii=False)]
    if isinstance(value, list):
        if any(isinstance(item, (list, Mapping)) for item in value):
            raise MigrationError("frontmatter-value-invalid", "frontmatter lists may contain scalars only")
        return [indent + "- " + render_value(item)[0] for item in value]
    if isinstance(value, Mapping):
        rows: list[str] = []
        for key, item in value.items():
            if not isinstance(key, str) or not TOP_LEVEL.fullmatch(key + ":\n"):
                raise MigrationError("frontmatter-value-invalid", "frontmatter mapping keys are invalid")
            rows.append(indent + key + ":")
            rows.extend(render_value(item, indent + "  "))
        return rows
    raise MigrationError("frontmatter-value-invalid", "frontmatter update values must be JSON-compatible")


def edit_fields(frontmatter: str, removals: tuple[str, ...], updates: Mapping[str, Any]) -> str:
    """Apply declared field changes only; relations have a separate exact map."""
    if "relations" in removals or "relations" in updates:
        raise MigrationError("frontmatter-invalid", "relations must use the exact relation maps")
    blocks = fields(frontmatter)
    for name in removals:
        if name not in blocks:
            raise MigrationError("frontmatter-removal-mismatch", f"frontmatter field is absent: {name}")
    lines = frontmatter.splitlines(keepends=True)
    for name, (start, end, _) in sorted(blocks.items(), key=lambda item: item[1][0], reverse=True):
        if name in removals:
            lines[start:end] = []
        elif name in updates:
            lines[start:end] = [name + ":\n", *[line + "\n" for line in render_value(updates[name], "  ")]] if isinstance(updates[name], (list, Mapping)) else [name + ": " + render_value(updates[name])[0] + "\n"]
    absent = [name for name in updates if name not in blocks]
    if absent and lines and lines[-1].strip():
        lines.append("\n")
    for name in sorted(absent):
        value = updates[name]
        lines.extend([name + ":\n", *[line + "\n" for line in render_value(value, "  ")]] if isinstance(value, (list, Mapping)) else [name + ": " + render_value(value)[0] + "\n"])
    return "".join(lines)


def edit_relations(frontmatter: str, rewrites: Mapping[str, Mapping[str, str]], removals: Mapping[str, tuple[str, ...]]) -> str:
    """Rewrite or remove only explicitly named relation targets in-place."""
    if not rewrites and not removals:
        return frontmatter
    blocks = fields(frontmatter)
    if "relations" not in blocks:
        raise MigrationError("relation-mismatch", "relation map names relations but source has none")
    start, end, raw = blocks["relations"]
    lines = raw.splitlines(keepends=True)
    entries, headers = _relation_entries(lines)
    requested = _requested_relation_targets(rewrites, removals)
    for _, relation, target in requested:
        matches = entries.get((relation, target), [])
        if len(matches) != 1:
            raise MigrationError("relation-mismatch", f"relation target must occur exactly once: {relation} -> {target}")
    deleted: set[int] = set()
    for relation, mapping in rewrites.items():
        for old, new in mapping.items():
            index = entries[(relation, old)][0]
            lines[index] = f"    - {new}\n"
    for relation, targets in removals.items():
        for target in targets:
            deleted.add(entries[(relation, target)][0])
    active_targets = _active_relation_targets(entries, headers, deleted)
    deleted |= {headers[relation] for relation, count in active_targets.items() if count == 0}
    if not any(active_targets.values()):
        all_lines = frontmatter.splitlines(keepends=True)
        all_lines[start:end] = []
        return "".join(all_lines)
    lines = [line for index, line in enumerate(lines) if index not in deleted]
    replacement = "".join(lines)
    all_lines = frontmatter.splitlines(keepends=True)
    all_lines[start:end] = [replacement]
    return "".join(all_lines)


def _relation_entries(lines: list[str]) -> tuple[dict[tuple[str, str], list[int]], dict[str, int]]:
    """Parse one conventional nested relations block without accepting extras."""
    entries: dict[tuple[str, str], list[int]] = {}
    headers: dict[str, int] = {}
    current: str | None = None
    for index, line in enumerate(lines[1:], 1):
        header = RELATION.fullmatch(line)
        target = TARGET.fullmatch(line)
        if header:
            current, headers[current] = header.group(1), index
        elif target and current:
            entries.setdefault((current, target.group(1)), []).append(index)
        elif line.strip():
            raise MigrationError("relations-invalid", "relations must use canonical nested target-list YAML")
    return entries, headers


def _requested_relation_targets(rewrites: Mapping[str, Mapping[str, str]], removals: Mapping[str, tuple[str, ...]]) -> set[tuple[str, str, str]]:
    """Create one exact request set for mismatch checks."""
    rewritten = {("rewrite", relation, target) for relation, mapping in rewrites.items() for target in mapping}
    removed = {("remove", relation, target) for relation, targets in removals.items() for target in targets}
    return rewritten | removed


def _active_relation_targets(entries: Mapping[tuple[str, str], list[int]], headers: Mapping[str, int], deleted: set[int]) -> dict[str, int]:
    """Count retained targets per relation after declared removals."""
    counts = {relation: 0 for relation in headers}
    for (relation, _), indexes in entries.items():
        counts[relation] += sum(index not in deleted for index in indexes)
    return counts


def validate_revision(frontmatter: str, expected: int, removals: tuple[str, ...], updates: Mapping[str, Any]) -> None:
    """Require the declared revision update and removal of present derived fields."""
    if {"atom_id", "tier"} & set(updates):
        raise MigrationError("frontmatter-derived-update-invalid", "atom_id and tier are derived from the destination filename and must not be updated")
    blocks = fields(frontmatter)
    if "version" not in blocks or scalar(blocks["version"][2], "version") != str(expected):
        raise MigrationError("source-version-mismatch", "source version differs from expected_source_version")
    for field in ("atom_id", "tier"):
        present = field in blocks
        declared = field in removals
        if present and not declared:
            raise MigrationError("frontmatter-derived-removal-required", f"present derived field must be removed: {field}")
        if declared and not present:
            raise MigrationError("frontmatter-derived-removal-invalid", f"absent derived field must not be removed: {field}")
    if updates.get("version") != expected + 1:
        raise MigrationError("frontmatter-version-invalid", "frontmatter_updates.version must advance source version by exactly one")
    stamp = updates.get("updated_at")
    if not isinstance(stamp, str) or not TIMESTAMP.fullmatch(stamp):
        raise MigrationError("frontmatter-timestamp-invalid", "frontmatter_updates.updated_at must be YYYY-MM-DD HH:MM:SS")
