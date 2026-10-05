"""Private, non-consuming recovery state for one Draft promotion.

This module deliberately retains only a sealed transition binding below the
Project control root.  It is neither retained Draft history nor a Journal:
``draft_history`` remains the only component that consumes a Draft head.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from atom_operations import ToolError, atom_digest, atom_from_path, canonical_json, control_root, safe_path
from draft_history import (
    DraftHistoryError,
    append_promotion_successor,
    history_entry_ref,
    load_history_entry,
    validate_current_draft_head,
)


class PendingPromotionError(ValueError):
    """The private promotion handoff is unsafe, stale, or belongs elsewhere."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


_SCHEMA_VERSION = 1
_ATOM_ID = re.compile(r"CA-[CAPRMEDO]-[1-9][0-9]*\Z")
_DIGEST = re.compile(r"[0-9a-f]{64}\Z")
_RUNTIME_DIRECTORY = ".draft_promotion_runtime"
_CURRENT = "current.json"


def _digest(value: object) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _runtime_directory(root: Path, *, create: bool) -> Path:
    """Return the per-Project ephemeral carrier without following symlinks."""

    directory = control_root(root) / _RUNTIME_DIRECTORY
    if directory.exists() and directory.is_symlink():
        raise PendingPromotionError("runtime-unsafe", "pending promotion runtime cannot be a symlink")
    if create:
        directory.mkdir(mode=0o700, parents=False, exist_ok=True)
        if directory.is_symlink() or not directory.is_dir():
            raise PendingPromotionError("runtime-unsafe", "pending promotion runtime is not a directory")
    return directory


def pending_promotion_path(root: Path) -> Path:
    """Expose the active ephemeral reservation location for diagnostics only."""

    return _runtime_directory(root.resolve(), create=False) / _CURRENT


def _record_path(root: Path, reservation_digest: str, *, create: bool) -> Path:
    if _DIGEST.fullmatch(reservation_digest) is None:
        raise PendingPromotionError("reservation-invalid", "reservation digest is malformed")
    directory = _runtime_directory(root, create=create) / "terminal"
    if directory.exists() and directory.is_symlink():
        raise PendingPromotionError("runtime-unsafe", "pending promotion terminal directory cannot be a symlink")
    if create:
        directory.mkdir(mode=0o700, exist_ok=True)
        if directory.is_symlink() or not directory.is_dir():
            raise PendingPromotionError("runtime-unsafe", "pending promotion terminal directory is unsafe")
    return directory / f"{reservation_digest}.json"


def _read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    if path.is_symlink() or not path.is_file():
        raise PendingPromotionError("runtime-unsafe", "pending promotion state is not a regular file")
    try:
        value = json.loads(path.read_bytes())
    except (OSError, json.JSONDecodeError) as error:
        raise PendingPromotionError("reservation-corrupt", "pending promotion state is unreadable") from error
    if not isinstance(value, dict):
        raise PendingPromotionError("reservation-corrupt", "pending promotion state must be a JSON object")
    return value


def _write_new_json(path: Path, value: Mapping[str, Any]) -> None:
    data = canonical_json(dict(value)).encode("utf-8")
    try:
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        raise
    except OSError as error:
        raise PendingPromotionError("runtime-write-failed", "cannot create pending promotion state") from error
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
    except OSError as error:
        raise PendingPromotionError("runtime-write-failed", "cannot seal pending promotion state") from error


def _relative_control_path(root: Path, value: object, *, must_exist: bool) -> str:
    if not isinstance(value, str) or not value or "\x00" in value:
        raise PendingPromotionError("path-invalid", "promotion paths must be non-empty relative strings")
    raw = Path(value)
    if raw.is_absolute() or ".." in raw.parts:
        raise PendingPromotionError("path-invalid", "promotion paths must stay below the Project control root")
    root = root.resolve()
    lexical = root / raw
    cursor = root
    for component in raw.parts:
        cursor /= component
        if cursor.exists() and cursor.is_symlink():
            raise PendingPromotionError("path-unsafe", "promotion paths cannot traverse a symlink")
    try:
        path = safe_path(root, raw.as_posix(), must_exist=must_exist)
    except ToolError as error:
        raise PendingPromotionError("path-invalid", "promotion path is not a safe Project carrier") from error
    if lexical.exists() and lexical.resolve() != path:
        raise PendingPromotionError("path-unsafe", "promotion path has an unexpected resolved target")
    return path.relative_to(root).as_posix()


def _reference(root: Path, value: object) -> dict[str, str]:
    if not isinstance(value, Mapping) or set(value) != {"history_revision", "path"}:
        raise PendingPromotionError("head-invalid", "Draft head reference has an invalid shape")
    try:
        return dict(history_entry_ref(root, value["history_revision"], value["path"]))
    except (DraftHistoryError, KeyError, TypeError) as error:
        raise PendingPromotionError("head-invalid", "Draft head reference is not trusted retained history") from error


def _request_digest(request: Mapping[str, Any]) -> str:
    if not isinstance(request, Mapping):
        raise PendingPromotionError("request-invalid", "pending promotion requires a sealed request mapping")

    def retired(value: object) -> bool:
        if isinstance(value, Mapping):
            return "draft_identity_evidence" in value or any(retired(item) for item in value.values())
        if isinstance(value, (list, tuple)):
            return any(retired(item) for item in value)
        return False

    if retired(request):
        raise PendingPromotionError("retired-evidence", "caller Draft identity evidence is not accepted")
    try:
        return _digest(dict(request))
    except (TypeError, ValueError) as error:
        raise PendingPromotionError("request-invalid", "pending promotion request is not canonical JSON") from error


def _reservation(root: Path, *, draft_path: object, head: object, request: Mapping[str, Any],
                 planned_atom_id: object, output_path: object, output_digest: object) -> dict[str, Any]:
    root = root.resolve()
    normalized_head = _reference(root, head)
    # A terminal retry can legitimately occur after the lifecycle removes the
    # consumed Draft.  Live-head validation below still requires its existence.
    normalized_draft = _relative_control_path(root, draft_path, must_exist=False)
    normalized_output = _relative_control_path(root, output_path, must_exist=False)
    if not isinstance(planned_atom_id, str) or _ATOM_ID.fullmatch(planned_atom_id) is None:
        raise PendingPromotionError("planned-identity-invalid", "planned Atom ID is invalid")
    if not isinstance(output_digest, str) or _DIGEST.fullmatch(output_digest) is None:
        raise PendingPromotionError("output-digest-invalid", "planned output digest is invalid")
    reservation = {
        "head": normalized_head,
        "draft_path": normalized_draft,
        "request_digest": _request_digest(request),
        "planned_atom_id": planned_atom_id,
        "output": {"path": normalized_output, "digest": output_digest},
    }
    reservation["reservation_digest"] = _digest(reservation)
    return reservation


def _validate_reservation(root: Path, value: object, *, draft_must_exist: bool = True) -> dict[str, Any]:
    if not isinstance(value, Mapping) or set(value) != {
        "head", "draft_path", "request_digest", "planned_atom_id", "output", "reservation_digest"
    }:
        raise PendingPromotionError("reservation-corrupt", "pending promotion reservation has unsupported fields")
    output = value.get("output")
    if not isinstance(output, Mapping) or set(output) != {"path", "digest"}:
        raise PendingPromotionError("reservation-corrupt", "pending promotion output binding is malformed")
    reservation = {
        "head": _reference(root, value.get("head")),
        "draft_path": _relative_control_path(root, value.get("draft_path"), must_exist=draft_must_exist),
        "request_digest": value.get("request_digest"),
        "planned_atom_id": value.get("planned_atom_id"),
        "output": {
            "path": _relative_control_path(root, output.get("path"), must_exist=False),
            "digest": output.get("digest"),
        },
    }
    if not isinstance(reservation["request_digest"], str) or _DIGEST.fullmatch(reservation["request_digest"]) is None:
        raise PendingPromotionError("reservation-corrupt", "pending promotion request binding is malformed")
    if not isinstance(reservation["planned_atom_id"], str) or _ATOM_ID.fullmatch(reservation["planned_atom_id"]) is None:
        raise PendingPromotionError("reservation-corrupt", "pending promotion identity binding is malformed")
    if not isinstance(reservation["output"]["digest"], str) or _DIGEST.fullmatch(reservation["output"]["digest"]) is None:
        raise PendingPromotionError("reservation-corrupt", "pending promotion output digest is malformed")
    expected = _digest(reservation)
    if value.get("reservation_digest") != expected:
        raise PendingPromotionError("reservation-corrupt", "pending promotion reservation seal does not match")
    reservation["reservation_digest"] = expected
    return reservation


def _active(root: Path, *, draft_must_exist: bool = True) -> dict[str, Any] | None:
    record = _read_json(pending_promotion_path(root))
    if record is None:
        return None
    if set(record) != {"schema_version", "state", "reservation", "seal"} or record.get("schema_version") != _SCHEMA_VERSION:
        raise PendingPromotionError("reservation-corrupt", "pending promotion state has unsupported fields")
    if record.get("state") != "pending":
        raise PendingPromotionError("reservation-corrupt", "active promotion state is not pending")
    reservation = _validate_reservation(root, record.get("reservation"), draft_must_exist=draft_must_exist)
    sealed = {"schema_version": _SCHEMA_VERSION, "state": "pending", "reservation": reservation}
    if record.get("seal") != _digest(sealed):
        raise PendingPromotionError("reservation-corrupt", "pending promotion state seal does not match")
    return reservation


def _terminal(root: Path, reservation: Mapping[str, Any]) -> dict[str, Any] | None:
    path = _record_path(root, str(reservation["reservation_digest"]), create=False)
    record = _read_json(path)
    if record is None:
        return None
    if set(record) != {"schema_version", "state", "reservation", "successor", "seal"} or record.get("schema_version") != _SCHEMA_VERSION:
        raise PendingPromotionError("reservation-corrupt", "terminal promotion state has unsupported fields")
    if record.get("state") != "finalized":
        raise PendingPromotionError("reservation-corrupt", "terminal promotion state is not finalized")
    observed = _validate_reservation(root, record.get("reservation"), draft_must_exist=False)
    if observed != dict(reservation):
        raise PendingPromotionError("reservation-corrupt", "terminal promotion reservation conflicts with retry")
    successor = _reference(root, record.get("successor"))
    sealed = {"schema_version": _SCHEMA_VERSION, "state": "finalized", "reservation": observed, "successor": successor}
    if record.get("seal") != _digest(sealed):
        raise PendingPromotionError("reservation-corrupt", "terminal promotion state seal does not match")
    return successor


def _write_active(root: Path, reservation: Mapping[str, Any]) -> None:
    path = _runtime_directory(root, create=True) / _CURRENT
    sealed = {"schema_version": _SCHEMA_VERSION, "state": "pending", "reservation": dict(reservation)}
    record = {**sealed, "seal": _digest(sealed)}
    _write_new_json(path, record)


def _write_terminal(root: Path, reservation: Mapping[str, Any], successor: Mapping[str, Any]) -> dict[str, str]:
    normalized_successor = _reference(root, successor)
    path = _record_path(root, str(reservation["reservation_digest"]), create=True)
    sealed = {
        "schema_version": _SCHEMA_VERSION,
        "state": "finalized",
        "reservation": dict(reservation),
        "successor": normalized_successor,
    }
    record = {**sealed, "seal": _digest(sealed)}
    try:
        _write_new_json(path, record)
    except FileExistsError:
        prior = _terminal(root, reservation)
        if prior != normalized_successor:
            raise PendingPromotionError("reservation-corrupt", "terminal promotion successor conflicts with retry")
    return normalized_successor


def _clear_active(root: Path, reservation: Mapping[str, Any]) -> None:
    path = pending_promotion_path(root)
    current = _active(root, draft_must_exist=False)
    if current is None:
        return
    if current != dict(reservation):
        raise PendingPromotionError("reservation-conflict", "active promotion belongs to another transition")
    try:
        path.unlink()
    except OSError as error:
        raise PendingPromotionError("runtime-write-failed", "cannot clear finalized promotion reservation") from error


def _matching_successor(root: Path, reservation: Mapping[str, Any]) -> dict[str, str] | None:
    """Find only a trusted successor that exactly completes this reservation."""

    directory = control_root(root) / "archive" / "_draft_history"
    if not directory.exists():
        return None
    if directory.is_symlink() or not directory.is_dir():
        raise PendingPromotionError("history-unsafe", "Draft history archive is unsafe")
    matches: list[dict[str, str]] = []
    for path in sorted(directory.glob("*.json")):
        try:
            reference = _reference(root, {"history_revision": path.stem, "path": path.relative_to(root).as_posix()})
            entry = load_history_entry(root, reference)
        except (DraftHistoryError, OSError, ValueError) as error:
            raise PendingPromotionError("history-unsafe", "Draft history cannot be trusted for recovery") from error
        if (entry.get("origin") == {"kind": "identified_promotion"}
                and entry.get("parent_history_entry_ref") == reservation["head"]
                and entry.get("draft_output") == reservation["output"]):
            matches.append(reference)
    if len(matches) > 1:
        raise PendingPromotionError("history-ambiguous", "multiple promotion successors match the pending reservation")
    return matches[0] if matches else None


def match_promotion_successor(
    root: Path,
    *,
    head: Mapping[str, Any],
    output_path: str,
    output_digest: str,
) -> dict[str, str] | None:
    """Return the one exact observed successor without reading a Draft carrier.

    This is the supported recovery lookup for lifecycle wiring after a prior
    attempt may have consumed and removed the Draft.  It never writes history
    or allocates an identity.
    """

    root = root.resolve()
    if not isinstance(output_digest, str) or _DIGEST.fullmatch(output_digest) is None:
        raise PendingPromotionError("output-digest-invalid", "promotion output digest is invalid")
    return _matching_successor(root, {
        "head": _reference(root, head),
        "output": {
            "path": _relative_control_path(root, output_path, must_exist=False),
            "digest": output_digest,
        },
    })


def lookup_pending_promotion(root: Path, *, draft_path: str, head: Mapping[str, Any]) -> dict[str, Any] | None:
    """Return the sealed handoff for this head before any new identity work.

    A different active reservation is a hard refusal: callers must not choose
    a second identity while another Draft promotion remains repairable.
    """

    root = root.resolve()
    sought_head = _reference(root, head)
    sought_draft = _relative_control_path(root, draft_path, must_exist=False)
    active = _active(root, draft_must_exist=False)
    if active is not None:
        if active["head"] != sought_head or active["draft_path"] != sought_draft:
            raise PendingPromotionError("reservation-conflict", "a different Draft promotion is already pending")
        terminal = _terminal(root, active)
        if terminal is not None:
            return {"disposition": "finalized", "reservation": active, "successor": terminal}
        return {"disposition": "pending", "reservation": active}
    directory = _runtime_directory(root, create=False) / "terminal"
    if not directory.exists():
        return None
    if directory.is_symlink() or not directory.is_dir():
        raise PendingPromotionError("runtime-unsafe", "pending promotion terminal directory is unsafe")
    matches: list[tuple[dict[str, Any], dict[str, str]]] = []
    for path in sorted(directory.glob("*.json")):
        record = _read_json(path)
        if record is None:
            continue
        if not isinstance(record.get("reservation"), Mapping):
            raise PendingPromotionError("reservation-corrupt", "terminal promotion reservation is malformed")
        reservation = _validate_reservation(root, record["reservation"], draft_must_exist=False)
        if reservation["head"] != sought_head or reservation["draft_path"] != sought_draft:
            continue
        successor = _terminal(root, reservation)
        if successor is not None:
            matches.append((reservation, successor))
    if len(matches) > 1:
        raise PendingPromotionError("history-ambiguous", "multiple finalized reservations match this Draft head")
    if matches:
        reservation, successor = matches[0]
        return {"disposition": "finalized", "reservation": reservation, "successor": successor}
    return None


def recover_pending_promotion(root: Path, *, draft_path: str, head: Mapping[str, Any]) -> dict[str, Any] | None:
    """Recover a sealed exact transition before preparing another identity/output."""

    found = lookup_pending_promotion(root, draft_path=draft_path, head=head)
    if found is None or found["disposition"] == "finalized":
        return found
    return finalize_pending_promotion(root, found["reservation"])


def _pending(reservation: Mapping[str, Any], code: str, message: str) -> dict[str, Any]:
    return {
        "disposition": "pending",
        "reservation": dict(reservation),
        "repair_context": {"code": code, "message": message},
    }


def _finalized(root: Path, reservation: Mapping[str, Any], successor: Mapping[str, Any]) -> dict[str, Any]:
    try:
        successor_ref = _write_terminal(root, reservation, successor)
    except PendingPromotionError as error:
        # The retained successor is already real, but retry must remain able to
        # discover it and repair the ephemeral terminal receipt without adding a
        # second history child.
        return _pending(reservation, error.code, str(error))
    try:
        _clear_active(root, reservation)
    except PendingPromotionError as error:
        return _pending(reservation, error.code, str(error))
    return {"disposition": "finalized", "reservation": dict(reservation), "successor": successor_ref}


def reserve_pending_promotion(
    root: Path,
    *,
    draft_path: str,
    head: Mapping[str, Any],
    request: Mapping[str, Any],
    planned_atom_id: str,
    output_path: str,
    output_digest: str,
) -> dict[str, Any]:
    """Create or resume the sole sealed, non-consuming Draft-promotion handoff.

    A retry must carry the same request digest, Draft head, planned Atom ID, and
    exact intended output bytes.  This function never allocates identity or
    appends retained history.
    """

    root = root.resolve()
    reservation = _reservation(
        root, draft_path=draft_path, head=head, request=request,
        planned_atom_id=planned_atom_id, output_path=output_path, output_digest=output_digest,
    )
    terminal = _terminal(root, reservation)
    if terminal is not None:
        return {"disposition": "finalized", "reservation": reservation, "successor": terminal}
    active = _active(root, draft_must_exist=False)
    if active is not None:
        # A terminal receipt may have survived a crash before active-state cleanup.
        completed = _terminal(root, active)
        if completed is not None:
            _clear_active(root, active)
            active = None
    if active is not None:
        if active != reservation:
            raise PendingPromotionError("reservation-conflict", "a different Draft promotion is already pending")
        observed_successor = _matching_successor(root, active)
        if observed_successor is not None:
            return _finalized(root, active, observed_successor)
        try:
            validate_current_draft_head(root, reservation["draft_path"], reservation["head"])
        except DraftHistoryError as error:
            raise PendingPromotionError("head-stale", "pending Draft head is no longer current") from error
        return {"disposition": "pending", "reservation": reservation}
    try:
        entry = validate_current_draft_head(root, reservation["draft_path"], reservation["head"])
    except (DraftHistoryError, OSError) as error:
        raise PendingPromotionError("head-invalid", "Draft head is not current retained history") from error
    if entry.get("draft_output", {}).get("path") != reservation["draft_path"]:
        raise PendingPromotionError("head-invalid", "Draft head does not bind the requested Draft carrier")
    try:
        _write_active(root, reservation)
    except FileExistsError:
        # Another admitted caller won the exclusive create; inspect it rather
        # than replacing or allocating beside it.
        active = _active(root, draft_must_exist=False)
        if active == reservation:
            return {"disposition": "pending", "reservation": reservation}
        raise PendingPromotionError("reservation-conflict", "a different Draft promotion is already pending")
    return {"disposition": "pending", "reservation": reservation}


def finalize_pending_promotion(root: Path, reservation: Mapping[str, Any]) -> dict[str, Any]:
    """Finalize only observed exact output, or return repairable pending context.

    The helper appends the one consuming history child only after this module
    has verified the reserved output path, digest, and Atom ID.  Every failed
    observation leaves the Draft head and reservation intact.
    """

    root = root.resolve()
    reservation = _validate_reservation(root, reservation, draft_must_exist=False)
    terminal = _terminal(root, reservation)
    if terminal is not None:
        return {"disposition": "finalized", "reservation": reservation, "successor": terminal}
    active = _active(root, draft_must_exist=False)
    if active != reservation:
        raise PendingPromotionError("reservation-missing", "no matching pending Draft promotion exists")
    observed_successor = _matching_successor(root, reservation)
    if observed_successor is not None:
        return _finalized(root, reservation, observed_successor)
    try:
        validate_current_draft_head(root, reservation["draft_path"], reservation["head"])
    except DraftHistoryError as error:
        return _pending(reservation, "head-stale", "Draft head is no longer current; repair requires an exact retained head")
    output = root / reservation["output"]["path"]
    if not output.is_file() or output.is_symlink():
        return _pending(reservation, "output-missing", "identified promotion output is not yet an exact regular file")
    observed_digest = hashlib.sha256(output.read_bytes()).hexdigest()
    if observed_digest != reservation["output"]["digest"]:
        return _pending(reservation, "output-digest-mismatch", "identified promotion output bytes differ from the reservation")
    try:
        identified = atom_from_path(root, output)
    except ToolError as error:
        return _pending(reservation, "output-invalid", "identified promotion output is not an admitted Atom carrier")
    if identified.atom_id != reservation["planned_atom_id"] or atom_digest(identified) != observed_digest:
        return _pending(reservation, "output-identity-mismatch", "identified promotion output does not carry the reserved Atom ID")
    try:
        successor = append_promotion_successor(root, reservation["head"], reservation["output"]["path"])
    except DraftHistoryError as error:
        recovered = _matching_successor(root, reservation)
        if recovered is not None:
            return _finalized(root, reservation, recovered)
        return _pending(reservation, "finalization-failed", "history successor was not appended; retry the exact pending transition")
    return _finalized(root, reservation, successor)


__all__ = [
    "PendingPromotionError",
    "finalize_pending_promotion",
    "lookup_pending_promotion",
    "match_promotion_successor",
    "pending_promotion_path",
    "recover_pending_promotion",
    "reserve_pending_promotion",
]
