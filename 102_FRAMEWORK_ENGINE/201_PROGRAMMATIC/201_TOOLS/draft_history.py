"""Trusted retained Draft-history primitives; this module has no lifecycle effects."""
from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import uuid
from collections.abc import Mapping
from contextlib import contextmanager
from pathlib import Path
from typing import Any, TypedDict

import fcntl

from atom_operations import (
    ToolError,
    atom_digest,
    atom_from_path,
    atom_version,
    control_root,
    draft_revision_lineage,
    frontmatter_scalar,
    safe_path,
)


class DraftHistoryError(ValueError):
    """A retained Draft-history reference, entry, or chain is not trustworthy."""


class HistoryEntryRef(TypedDict):
    history_revision: str
    path: str


_REVISION = re.compile(r"[0-9a-f]{32}")
_DRAFT_ORIGINS = {"never_identified", "demoted_identified", "draft_update"}
_PREDECESSOR_KEYS = {"atom_id", "version", "content_role", "summary", "digest", "immutable_locator"}
_PROMOTION_LOCK_DIRECTORY = ".draft_promotion_locks"


def _digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _directory(root: Path) -> Path:
    """The control-root archive is the only trusted retained-history location."""
    return control_root(root) / "archive" / "_draft_history"


def _history_directory(root: Path) -> Path:
    """Refuse symlinked archive components before creating any history directory."""
    directory = _directory(root)
    for component in (directory.parent, directory):
        if component.is_symlink():
            raise DraftHistoryError("trusted history archive cannot be a symlink")
    directory.mkdir(parents=True, exist_ok=True)
    if directory.is_symlink():
        raise DraftHistoryError("trusted history archive cannot be a symlink")
    return directory


@contextmanager
def _promotion_lock(root: Path, reference: HistoryEntryRef):
    """Serialize consumption of one retained Draft head across processes."""

    directory = control_root(root) / _PROMOTION_LOCK_DIRECTORY
    if directory.exists() and directory.is_symlink():
        raise DraftHistoryError("Draft promotion lock directory cannot be a symlink")
    directory.mkdir(mode=0o700, exist_ok=True)
    if directory.is_symlink() or not directory.is_dir():
        raise DraftHistoryError("Draft promotion lock directory is unsafe")
    path = directory / f"{reference['history_revision']}.lock"
    if path.exists() and path.is_symlink():
        raise DraftHistoryError("Draft promotion lock cannot be a symlink")
    flags = os.O_RDWR | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags, 0o600)
    except OSError as error:
        raise DraftHistoryError("cannot acquire Draft promotion lock") from error
    try:
        fcntl.flock(descriptor, fcntl.LOCK_EX)
        yield
    except OSError as error:
        raise DraftHistoryError("cannot hold Draft promotion lock") from error
    finally:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
        finally:
            os.close(descriptor)


def _append_history_entry(root: Path, reference: HistoryEntryRef, entry: Mapping[str, Any]) -> None:
    """Publish one immutable history entry without replacing an existing ref."""

    directory = _history_directory(root)
    target = root / reference["path"]
    if target.parent != directory or target.exists():
        raise DraftHistoryError("immutable history entry already exists")
    data = json.dumps(dict(entry), sort_keys=True, separators=(",", ":")).encode("utf-8")
    descriptor, temporary = tempfile.mkstemp(prefix=f".{reference['history_revision']}.", dir=directory)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.link(temporary, target)
        except FileExistsError as error:
            raise DraftHistoryError("immutable history entry already exists") from error
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
    except OSError as error:
        if os.path.exists(temporary):
            os.unlink(temporary)
        raise DraftHistoryError("cannot append immutable history entry") from error


def _relative(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def reserve_history_entry(root: Path) -> HistoryEntryRef:
    """Reserve a fresh, pre-addressable entry locator without writing history bytes."""
    root = root.resolve()
    directory = _history_directory(root)
    while True:
        revision = uuid.uuid4().hex
        candidate = directory / f"{revision}.json"
        if not candidate.exists():
            return {"history_revision": revision, "path": _relative(root, candidate)}


def history_entry_ref(root: Path, history_revision: str, path: str, *, must_exist: bool = True) -> HistoryEntryRef:
    """Validate one pre-addressable locator, optionally before its entry is appended."""
    root = root.resolve()
    if not isinstance(history_revision, str) or _REVISION.fullmatch(history_revision) is None:
        raise DraftHistoryError("invalid history revision")
    try:
        candidate = safe_path(root, path, must_exist=must_exist)
    except ToolError as error:
        raise DraftHistoryError("history path is not a safe Project carrier") from error
    expected = _directory(root) / f"{history_revision}.json"
    if candidate != expected:
        raise DraftHistoryError("history reference is not in the trusted archive")
    return {"history_revision": history_revision, "path": _relative(root, candidate)}


def _reference(root: Path, value: Mapping[str, Any], *, must_exist: bool = True) -> HistoryEntryRef:
    if not isinstance(value, Mapping) or set(value) != {"history_revision", "path"}:
        raise DraftHistoryError("invalid history reference shape")
    return history_entry_ref(root, value["history_revision"], value["path"], must_exist=must_exist)


def _predecessor(root: Path, value: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(value, Mapping) or set(value) != _PREDECESSOR_KEYS:
        raise DraftHistoryError("invalid direct predecessor")
    if not isinstance(value["atom_id"], str) or not isinstance(value["content_role"], str) or not isinstance(value["summary"], str):
        raise DraftHistoryError("invalid direct predecessor identity")
    if not isinstance(value["version"], int) or isinstance(value["version"], bool) or value["version"] < 1:
        raise DraftHistoryError("invalid direct predecessor version")
    if not isinstance(value["digest"], str) or re.fullmatch(r"[0-9a-f]{64}", value["digest"]) is None:
        raise DraftHistoryError("invalid direct predecessor digest")
    locator = value["immutable_locator"]
    if not isinstance(locator, Mapping) or set(locator) != {"history_revision", "path"}:
        raise DraftHistoryError("invalid immutable predecessor locator")
    if not isinstance(locator["history_revision"], int) or isinstance(locator["history_revision"], bool) or locator["history_revision"] < 1:
        raise DraftHistoryError("invalid immutable predecessor revision")
    try:
        archived = safe_path(root, locator["path"], must_exist=True)
    except ToolError as error:
        raise DraftHistoryError("immutable predecessor is not a Project carrier") from error
    if not archived.is_file() or "archive" not in archived.relative_to(control_root(root)).parts:
        raise DraftHistoryError("immutable predecessor is not retained in the Project archive")
    try:
        atom = atom_from_path(root, archived)
        summary_match = re.search(r"(?m)^# Summary\s*$\n(?P<body>.*?)(?=^#|\Z)", atom.content, re.DOTALL)
        summary = next((line.strip() for line in summary_match.group("body").splitlines() if line.strip()), None) if summary_match else None
    except ToolError as error:
        raise DraftHistoryError("immutable predecessor is not an authoritative Atom") from error
    if (atom.atom_id != value["atom_id"] or atom_version(atom) != value["version"]
            or not atom.role_directory.endswith("_" + value["content_role"].lower()) or atom_digest(atom) != value["digest"]
            or summary != value["summary"]):
        raise DraftHistoryError("immutable predecessor does not match observed archive bytes")
    return dict(value)


def _carrier_reference(root: Path, draft_path: str, reference: Mapping[str, Any]) -> Path:
    try:
        draft = safe_path(root, draft_path, must_exist=True)
        atom = atom_from_path(root, draft)
    except ToolError as error:
        raise DraftHistoryError("Draft output path is unsafe") from error
    if frontmatter_scalar(atom.frontmatter, "atom_id") is not None:
        raise DraftHistoryError("Draft carrier must remain ID-free")
    try:
        lineage = draft_revision_lineage(atom.frontmatter)
    except ToolError as error:
        raise DraftHistoryError("Draft lineage is malformed") from error
    if lineage != {"history_entry_ref": dict(reference)}:
        raise DraftHistoryError("Draft carrier does not name the exact retained-history reference")
    return draft


def _entry_for_draft(root: Path, draft: Path, origin: Mapping[str, Any], parent: HistoryEntryRef | None,
                     predecessor: Mapping[str, Any] | None) -> dict[str, Any]:
    if not isinstance(origin, Mapping) or set(origin) != {"kind"} or origin.get("kind") not in _DRAFT_ORIGINS:
        raise DraftHistoryError("invalid Draft origin")
    kind = origin["kind"]
    if kind == "never_identified" and (parent is not None or predecessor is not None):
        raise DraftHistoryError("never-identified Draft has no predecessor")
    if kind == "demoted_identified" and (parent is not None or predecessor is None):
        raise DraftHistoryError("demotion must carry its direct identified predecessor")
    if kind == "draft_update" and parent is None:
        raise DraftHistoryError("Draft update must carry its direct parent")
    entry: dict[str, Any] = {
        "draft_output": {"path": _relative(root, draft), "digest": _digest(draft.read_bytes())},
        "origin": {"kind": kind},
    }
    if parent is not None:
        entry["parent_history_entry_ref"] = parent
    if predecessor is not None:
        entry["direct_predecessor"] = _predecessor(root, predecessor)
    return entry


def append_draft_entry(root: Path, draft_path: str, *, reference: Mapping[str, Any], origin: Mapping[str, Any],
                       parent_history_entry_ref: Mapping[str, Any] | None = None,
                       direct_predecessor: Mapping[str, Any] | None = None) -> HistoryEntryRef:
    """Append an immutable entry for a pre-reserved locator and exact Draft bytes."""
    root = root.resolve()
    ref = _reference(root, reference, must_exist=False)
    draft = _carrier_reference(root, draft_path, ref)
    parent = _reference(root, parent_history_entry_ref) if parent_history_entry_ref is not None else None
    entry = _entry_for_draft(root, draft, origin, parent, direct_predecessor)
    if parent is not None:
        parent_entry = load_history_entry(root, parent)
        if entry["origin"]["kind"] != "draft_update" or entry.get("direct_predecessor") != parent_entry.get("direct_predecessor"):
            raise DraftHistoryError("Draft update does not preserve its original identity basis")
    _append_history_entry(root, ref, entry)
    return ref


def load_history_entry(root: Path, reference: Mapping[str, Any]) -> dict[str, Any]:
    """Resolve an exact immutable JSON entry with the admitted Draft-entry schema."""
    root = root.resolve()
    ref = _reference(root, reference)
    try:
        value = json.loads((root / ref["path"]).read_bytes())
    except (OSError, json.JSONDecodeError) as error:
        raise DraftHistoryError("malformed retained Draft history") from error
    if not isinstance(value, dict) or not isinstance(value.get("draft_output"), dict) or not isinstance(value.get("origin"), dict):
        raise DraftHistoryError("invalid retained Draft history schema")
    output = value["draft_output"]
    origin = value["origin"]
    if set(output) != {"path", "digest"} or not isinstance(output["path"], str) or not isinstance(output["digest"], str):
        raise DraftHistoryError("invalid retained Draft output")
    if set(origin) != {"kind"}:
        raise DraftHistoryError("invalid retained Draft origin")
    kind = origin["kind"]
    expected = {
        "never_identified": {"draft_output", "origin"},
        "demoted_identified": {"draft_output", "origin", "direct_predecessor"},
        "draft_update": None,
        "identified_promotion": {"draft_output", "origin", "parent_history_entry_ref"},
    }.get(kind)
    if kind == "draft_update":
        allowed = ({"draft_output", "origin", "parent_history_entry_ref"},
                   {"draft_output", "origin", "parent_history_entry_ref", "direct_predecessor"})
        if set(value) not in allowed:
            raise DraftHistoryError("retained Draft history has unsupported properties")
    elif expected is None or set(value) != expected:
        raise DraftHistoryError("retained Draft history has unsupported properties")
    if kind == "demoted_identified" or (kind == "draft_update" and "direct_predecessor" in value):
        _predecessor(root, value["direct_predecessor"])
    if kind in {"draft_update", "identified_promotion"}:
        _reference(root, value["parent_history_entry_ref"])
    return value


def _entries(root: Path) -> list[tuple[HistoryEntryRef, dict[str, Any]]]:
    directory = _directory(root)
    if not directory.exists():
        return []
    found: list[tuple[HistoryEntryRef, dict[str, Any]]] = []
    for path in sorted(directory.glob("*.json")):
        ref = history_entry_ref(root, path.stem, _relative(root, path))
        found.append((ref, load_history_entry(root, ref)))
    return found


def validate_current_draft_head(root: Path, draft_path: str, reference: Mapping[str, Any]) -> dict[str, Any]:
    """Require a unique, unbranched head with exact carrier bytes and original basis."""
    root = root.resolve()
    ref = _reference(root, reference)
    draft = _carrier_reference(root, draft_path, ref)
    entry = load_history_entry(root, ref)
    if entry.get("origin", {}).get("kind") not in _DRAFT_ORIGINS:
        raise DraftHistoryError("history head is not a Draft entry")
    expected = {"path": _relative(root, draft), "digest": _digest(draft.read_bytes())}
    if entry.get("draft_output") != expected:
        raise DraftHistoryError("history entry does not bind current Draft bytes")
    seen = {ref["history_revision"]}
    current = entry
    while "parent_history_entry_ref" in current:
        parent_ref = _reference(root, current["parent_history_entry_ref"])
        if parent_ref["history_revision"] in seen:
            raise DraftHistoryError("Draft history parent cycle")
        parent = load_history_entry(root, parent_ref)
        if current.get("origin", {}).get("kind") != "draft_update" or current.get("direct_predecessor") != parent.get("direct_predecessor"):
            raise DraftHistoryError("Draft history parent is non-direct or changes basis")
        seen.add(parent_ref["history_revision"])
        current = parent
    if current.get("origin", {}).get("kind") not in {"never_identified", "demoted_identified"}:
        raise DraftHistoryError("Draft history lacks an original basis")
    if current.get("origin", {}).get("kind") == "demoted_identified":
        _predecessor(root, current.get("direct_predecessor"))
    for candidate_ref, candidate in _entries(root):
        if candidate_ref == ref:
            continue
        if candidate.get("parent_history_entry_ref") == ref:
            raise DraftHistoryError("Draft history head already has a child")
        if candidate.get("draft_output", {}).get("path") == expected["path"] and candidate_ref["history_revision"] not in seen:
            raise DraftHistoryError("Draft history has a competing canonical locator")
    return entry


def _matching_promotion_successor(root: Path, head: HistoryEntryRef, output: Mapping[str, str]) -> HistoryEntryRef | None:
    """Resolve an existing exact consuming child while the head lock is held."""

    children = [(reference, entry) for reference, entry in _entries(root)
                if entry.get("parent_history_entry_ref") == head]
    if not children:
        return None
    exact = [reference for reference, entry in children
             if entry.get("origin") == {"kind": "identified_promotion"} and entry.get("draft_output") == dict(output)]
    if len(exact) == 1 and len(children) == 1:
        return exact[0]
    raise DraftHistoryError("Draft history head already has a different or ambiguous consuming child")


def append_promotion_successor(root: Path, head: Mapping[str, Any], output_path: str) -> HistoryEntryRef:
    """Observe exact identified output before finalizing the sole consuming successor."""
    root = root.resolve()
    head_ref = _reference(root, head)
    with _promotion_lock(root, head_ref):
        head_entry = load_history_entry(root, head_ref)
        try:
            output = safe_path(root, output_path, must_exist=True)
            identified = atom_from_path(root, output)
        except ToolError as error:
            raise DraftHistoryError("promotion output is unsafe") from error
        if identified.lifecycle == "draft" or identified.atom_id is None:
            raise DraftHistoryError("promotion successor requires observed identified output")
        observed_output = {"path": _relative(root, output), "digest": _digest(output.read_bytes())}
        existing = _matching_promotion_successor(root, head_ref, observed_output)
        if existing is not None:
            return existing
        validate_current_draft_head(root, head_entry["draft_output"]["path"], head_ref)
        reference = reserve_history_entry(root)
        entry = {
            "draft_output": observed_output,
            "origin": {"kind": "identified_promotion"},
            "parent_history_entry_ref": head_ref,
        }
        _append_history_entry(root, reference, entry)
        return reference
