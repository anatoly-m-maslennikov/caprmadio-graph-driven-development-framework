"""Bounded refresh for the reviewed carrier-authority source pins."""

from __future__ import annotations

import hashlib
from copy import deepcopy
from pathlib import Path
from typing import Any, Iterable

from .parsing import CarrierError, parse_carrier


Record = dict[str, Any]

# Refreshing an obligation source is review-sensitive.  This helper deliberately
# cannot be used as a registry-wide updater.
APPROVED_REFRESH_IDS = frozenset(
    {
        "CA-D-276",
        "CA-D-269",
        "CA-D-268",
        "CA-D-270",
        "CA-D-274",
        "CA-D-446",
        "CA-D-479",
        "CA-D-482",
        "CA-D-483",
    }
)


def _source_for(root: Path, atom_id: str, entry: Record) -> tuple[Path, Record]:
    source_path = entry.get("source_path")
    if not isinstance(source_path, str) or not source_path:
        raise ValueError("source path is invalid: " + atom_id)
    parent = (root / source_path).parent.resolve()
    if parent != root and root not in parent.parents:
        raise ValueError("source path escapes project root: " + atom_id)
    if not parent.is_dir() or parent.is_symlink():
        raise ValueError("source directory is unavailable: " + atom_id)
    candidates: list[tuple[Path, Record]] = []
    for candidate in sorted(parent.glob("*.md")):
        if candidate.is_symlink() or not candidate.is_file():
            continue
        try:
            parsed = parse_carrier(candidate.read_bytes(), candidate)
        except (OSError, CarrierError):
            continue
        if parsed.metadata.get("atom_id") == atom_id and parsed.metadata.get("status") in {"Active", "active"}:
            candidates.append((candidate, parsed.metadata))
    if len(candidates) != 1:
        noun = "ambiguous" if candidates else "absent"
        raise ValueError("active source is " + noun + ": " + atom_id)
    return candidates[0]


def refresh_entries(root: Path, entries: Record, atom_ids: Iterable[str]) -> Record:
    """Return a copy with only approved, uniquely active source pins refreshed."""

    root = root.resolve()
    requested = tuple(atom_ids)
    if len(set(requested)) != len(requested):
        raise ValueError("refresh identifiers must be unique")
    if set(requested) - APPROVED_REFRESH_IDS:
        raise ValueError("requested source is not approved for refresh")
    result = deepcopy(entries)
    for atom_id in requested:
        entry = result.get(atom_id)
        if not isinstance(entry, dict):
            raise ValueError("registry entry is absent: " + atom_id)
        source, metadata = _source_for(root, atom_id, entry)
        version = metadata.get("version")
        if type(version) is not int or version < 1:
            raise ValueError("active source version is invalid: " + atom_id)
        try:
            relative = source.resolve().relative_to(root)
        except ValueError as error:
            raise ValueError("source path escapes project root: " + atom_id) from error
        entry["source_path"] = relative.as_posix()
        entry["version"] = version
        entry["sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    return result
