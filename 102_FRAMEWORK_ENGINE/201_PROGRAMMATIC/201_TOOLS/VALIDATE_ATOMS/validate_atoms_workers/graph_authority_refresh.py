"""Refresh the finite authority closure for relation and Plan graph checks."""

from __future__ import annotations

import hashlib
from copy import deepcopy
from pathlib import Path
from typing import Any

from .parsing import CarrierError, parse_carrier


Record = dict[str, Any]

# These are the only authority sources read by relations_resolution and
# plan_resolution.  Keeping this set finite prevents an authority refresh from
# accidentally widening graph admission.
APPROVED_GRAPH_AUTHORITY_IDS = frozenset(
    {
        "CA-D-305",
        "CA-D-268",
        "CA-R-1676",
        "CA-R-1017",
        "CA-R-1016",
        "CA-R-1018",
        "CA-R-1019",
        "CA-R-1021",
        "CA-R-1026",
        "CA-R-879",
        "CA-R-796",
        "CA-R-1020",
        "CA-R-1027",
        "CA-R-1022",
        "CA-R-1040",
        "CA-D-471",
        "CA-D-481",
        "CA-R-1579",
        "CA-R-1538",
        "CA-D-460",
        "CA-D-475",
        "CA-R-1539",
        "CA-R-1593",
        "CA-R-1580",
        "CA-R-1592",
    }
)

CURRENT_SOURCE_ROOTS = (
    Path(
        ".caprmedio_caprmedio/000_CAPRMEDIO_framework/"
        "00_APPLICABLE_METHODOLOGY/04_requirement"
    ),
    Path(
        ".caprmedio_caprmedio/000_CAPRMEDIO_framework/"
        "00_APPLICABLE_METHODOLOGY/07_delivery"
    ),
)


def _source_roots(root: Path) -> tuple[Path, ...]:
    resolved_root = root.resolve()
    result: list[Path] = []
    for relative in CURRENT_SOURCE_ROOTS:
        declared_root = resolved_root / relative
        source_root = declared_root.resolve()
        if (
            declared_root.is_symlink()
            or resolved_root not in source_root.parents
            or not source_root.is_dir()
        ):
            raise ValueError("current graph authority directory is unavailable")
        result.append(source_root)
    return tuple(result)


def _active_source(root: Path, atom_id: str) -> tuple[Path, Record]:
    """Find exactly one active source in the canonical, non-projected roots."""

    candidates: list[tuple[Path, Record]] = []
    for source_root in _source_roots(root):
        for candidate in sorted(source_root.glob(atom_id + "-*.md")):
            if candidate.is_symlink() or not candidate.is_file():
                continue
            try:
                parsed = parse_carrier(candidate.read_bytes(), candidate)
            except (OSError, CarrierError) as error:
                if candidate.name.startswith(atom_id + "-"):
                    raise ValueError("active source is unreadable: " + atom_id) from error
                continue
            metadata = parsed.metadata
            if metadata.get("atom_id") != atom_id:
                continue
            if metadata.get("status") in {"Active", "active"}:
                candidates.append((candidate, metadata))
    if len(candidates) != 1:
        noun = "ambiguous" if candidates else "absent"
        raise ValueError("active source is " + noun + ": " + atom_id)
    return candidates[0]


def refresh_entries(root: Path, entries: Record) -> Record:
    """Return a copy with exactly the graph-check authority closure refreshed."""

    root = root.resolve()
    result = deepcopy(entries)
    missing = APPROVED_GRAPH_AUTHORITY_IDS - set(result)
    if missing:
        raise ValueError("graph authority entry is absent: " + sorted(missing)[0])
    for atom_id in sorted(APPROVED_GRAPH_AUTHORITY_IDS):
        entry = result[atom_id]
        if not isinstance(entry, dict):
            raise ValueError("graph authority entry is invalid: " + atom_id)
        source, metadata = _active_source(root, atom_id)
        version = metadata.get("version")
        if type(version) is not int or version < 1:
            raise ValueError("active source version is invalid: " + atom_id)
        try:
            source_path = source.resolve().relative_to(root)
        except ValueError as error:
            raise ValueError("source path escapes project root: " + atom_id) from error
        entry.update(
            {
                "version": version,
                "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "source_path": source_path.as_posix(),
            }
        )
    return result


def verify_entries(root: Path, entries: Record) -> None:
    """Refuse missing, stale, or non-canonical graph authority pins."""

    refreshed = refresh_entries(root, entries)
    for atom_id in sorted(APPROVED_GRAPH_AUTHORITY_IDS):
        if entries[atom_id] != refreshed[atom_id]:
            raise ValueError("graph authority source is stale: " + atom_id)
