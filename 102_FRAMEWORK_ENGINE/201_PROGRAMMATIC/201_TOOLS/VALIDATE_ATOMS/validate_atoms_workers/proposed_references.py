"""Bounded, source-bound inventory of explicit proposed-carrier targets.

This module deliberately does not infer Atom identity from a filename.  It is a
small pre-write helper: callers supply only direct IDs mentioned by a proposed
carrier and the already-verified Project Structure mapping.  For a nested Plan
it additionally resolves the one-way ``is_decomposition_of`` parent chain.
It does *not* claim to inventory the project's complete graph.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

from .parsing import CarrierError, parse_carrier
from .read_io import LimitReached, ReadContext, ReadFailure
from .settings import CEILINGS


class ProposedReferenceError(ValueError):
    """An explicit target cannot be safely and completely inventoried."""


@dataclass(frozen=True)
class TargetCarrier:
    """Authenticated carrier facts retained for a direct reference or Plan parent."""

    atom_id: str
    status: str
    version: int
    path: str
    sha256: str
    metadata: dict[str, Any]


@dataclass(frozen=True)
class ProposedReferenceInventory:
    """Complete only for ``direct_targets`` and the returned Plan-parent chain."""

    direct_targets: tuple[TargetCarrier, ...]
    plan_parent_closure: tuple[TargetCarrier, ...]


def _relative(root: Path, value: str | Path) -> Path:
    path = Path(value)
    if path.is_absolute() or any(part == ".." for part in path.parts):
        raise ProposedReferenceError("reference path is outside the project")
    absolute = root / path
    if not absolute.is_relative_to(root):
        raise ProposedReferenceError("reference path is outside the project")
    return absolute


def _authority_roots(root: Path, structure: Mapping[str, Any]) -> list[Path]:
    units = structure.get("scope_units")
    if not isinstance(units, list) or not units:
        raise ProposedReferenceError("Project Structure authority paths are unavailable")
    roots: set[Path] = set()
    for unit in units:
        path = unit.get("authority_path") if isinstance(unit, Mapping) else None
        if not isinstance(path, str) or not path:
            raise ProposedReferenceError("Project Structure authority path is invalid")
        candidate = _relative(root, path)
        # Applicable Methodology delivery/projection copies are never authority.
        upper_parts = {part.upper() for part in candidate.relative_to(root).parts}
        if "_PROJECTION" in upper_parts or "APPLICABLE_METHODOLOGY" in upper_parts:
            continue
        roots.add(candidate)
    if not roots:
        raise ProposedReferenceError("Project Structure has no authoritative carrier frontier")
    # Nested scope units are already covered by an ancestor.  This also keeps a
    # multiple-scope structure from spending read budget on the same tree twice.
    return [item for item in sorted(roots) if not any(parent != item and item.is_relative_to(parent) for parent in roots)]


def _is_derived(path: Path, root: Path) -> bool:
    parts = {part.upper() for part in path.relative_to(root).parts}
    return "_PROJECTION" in parts or "APPLICABLE_METHODOLOGY" in parts


def _carrier(reader: ReadContext, root: Path, path: Path) -> TargetCarrier | None:
    if _is_derived(path, root):
        return None
    try:
        raw = reader.read(path)
        parsed = parse_carrier(raw, path)
    except (OSError, CarrierError, ReadFailure, LimitReached) as error:
        raise ProposedReferenceError("authoritative target carrier is unsafe or malformed") from error
    metadata = parsed.metadata
    atom_id, status, version = metadata.get("atom_id"), metadata.get("status"), metadata.get("version")
    if (
        not isinstance(atom_id, str)
        or not atom_id
        or not isinstance(status, str)
        or type(version) is not int
        or version < 1
    ):
        raise ProposedReferenceError("authoritative target carrier lacks explicit identity, status, or version")
    return TargetCarrier(
        atom_id=atom_id,
        status=status,
        version=version,
        path=str(path.relative_to(root)),
        sha256=hashlib.sha256(raw).hexdigest(),
        metadata=dict(metadata),
    )


def _is_archive(path: Path, root: Path) -> bool:
    return any(part.lower() == "archive" for part in path.relative_to(root).parts)


def _parent_id(metadata: Mapping[str, Any]) -> str | None:
    relations = metadata.get("relations", {})
    if not isinstance(relations, Mapping):
        raise ProposedReferenceError("Plan parent relation is malformed")
    parents = relations.get("is_decomposition_of", [])
    if parents is None:
        parents = []
    if not isinstance(parents, list) or len(parents) > 1 or any(not isinstance(item, str) or not item for item in parents):
        raise ProposedReferenceError("Plan parent relation is malformed")
    return parents[0] if parents else None


def _plan_container(
    parent_path: Path,
    child_status: object,
    admitted_plan_status_folders: Mapping[str, str] | None,
) -> Path:
    """Return the source-admitted local container for a child Plan status."""
    if not isinstance(child_status, str):
        raise ProposedReferenceError("nested Plan status is malformed")
    container = parent_path.with_suffix("")
    if child_status == "Active":
        return container
    if admitted_plan_status_folders is None:
        raise ProposedReferenceError("nested Plan status-folder authority is unavailable")
    folder = admitted_plan_status_folders.get(child_status)
    folder_path = Path(folder) if isinstance(folder, str) else None
    if (
        folder_path is None
        or not folder
        or folder_path.is_absolute()
        or len(folder_path.parts) != 1
        or folder_path.parts[0] in {".", ".."}
    ):
        raise ProposedReferenceError("nested Plan status-folder authority is invalid")
    return container / folder_path


def inventory_proposed_references(
    root: Path,
    project_structure: Mapping[str, Any],
    direct_atom_ids: Iterable[str],
    *,
    candidate_metadata: Mapping[str, Any] | None = None,
    candidate_path: str | Path | None = None,
    admitted_plan_status_folders: Mapping[str, str] | None = None,
) -> ProposedReferenceInventory:
    """Return exact current facts for named targets and a nested Plan parent chain.

    ``direct_atom_ids`` is finite and explicit.  Every returned direct target is
    an active, non-archive carrier found exactly once in Project Structure's
    authority frontier.  If ``candidate_metadata`` is a Plan with a parent,
    ``candidate_path`` is required and each child is checked to reside below the
    *actual authenticated parent carrier*.  A non-Active child Plan additionally
    requires its container folder from ``admitted_plan_status_folders``; callers
    must derive that finite mapping from validated CA-D-461 source evidence.
    Atom IDs never come from filenames.  A changed frontier, unsafe file,
    duplicate, missing or inactive named target raises
    ``ProposedReferenceError``.
    """
    root = root.resolve()
    ids = tuple(direct_atom_ids)
    if not ids or any(not isinstance(item, str) or not item for item in ids) or len(set(ids)) != len(ids):
        raise ProposedReferenceError("direct target IDs must be a finite unique nonempty set")
    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
    try:
        paths = reader.discover([str(item) for item in _authority_roots(root, project_structure)])
    except (OSError, ReadFailure, LimitReached) as error:
        raise ProposedReferenceError("authoritative carrier frontier is unavailable") from error

    requested = set(ids)
    active: dict[str, TargetCarrier] = {}
    inactive: set[str] = set()
    for path in paths:
        # Archives are scanned only to refuse an explicitly named non-active
        # target; they can never satisfy a target request.
        item = _carrier(reader, root, path)
        if item is None or item.atom_id not in requested:
            continue
        if _is_archive(path, root) or item.status != "Active":
            inactive.add(item.atom_id)
            continue
        if item.atom_id in active:
            raise ProposedReferenceError("named authoritative target is ambiguous")
        active[item.atom_id] = item
    missing = requested - set(active)
    if missing:
        if missing & inactive:
            raise ProposedReferenceError("named authoritative target is inactive or archived")
        raise ProposedReferenceError("named authoritative target is missing")

    closure: list[TargetCarrier] = []
    if candidate_metadata is not None:
        if candidate_metadata.get("content_role") == "Plan":
            parent = _parent_id(candidate_metadata)
            if parent is not None:
                if candidate_path is None:
                    raise ProposedReferenceError("nested Plan requires its actual carrier path")
                child_path = _relative(root, candidate_path)
                child_status = candidate_metadata.get("status")
                seen: set[str] = set()
                while parent is not None:
                    if parent in seen:
                        raise ProposedReferenceError("Plan parent closure contains a cycle")
                    seen.add(parent)
                    if parent not in active:
                        # Resolve only the newly named parent, retaining the same
                        # bounded frontier and then repeat the ordinary admission.
                        requested.add(parent)
                        matches = []
                        for path in paths:
                            item = _carrier(reader, root, path)
                            if item is not None and item.atom_id == parent:
                                matches.append((path, item))
                        admitted = [(path, item) for path, item in matches if not _is_archive(path, root) and item.status == "Active"]
                        if len(admitted) != 1:
                            raise ProposedReferenceError("Plan parent is missing, inactive, or ambiguous")
                        active[parent] = admitted[0][1]
                    item = active[parent]
                    if item.metadata.get("content_role") != "Plan":
                        raise ProposedReferenceError("Plan parent is not a Plan carrier")
                    closure.append(item)
                    parent = _parent_id(item.metadata)
                # Resolve the entire identity closure before physical checks, so
                # a genuine cycle cannot be hidden by an incidental bad layout.
                for item in closure:
                    parent_path = root / item.path
                    if child_path.parent != _plan_container(
                        parent_path, child_status, admitted_plan_status_folders,
                    ):
                        raise ProposedReferenceError("nested Plan path does not use the authenticated Markdown parent carrier")
                    child_path = parent_path
                    child_status = item.status
    current = reader.currentness()
    if current.get("state") != "unchanged":
        raise ProposedReferenceError("authoritative target frontier changed during inventory")
    return ProposedReferenceInventory(tuple(active[item] for item in ids), tuple(closure))
