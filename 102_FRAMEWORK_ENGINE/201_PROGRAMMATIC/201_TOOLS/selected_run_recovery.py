"""Read-only reconstruction of selected-Run Journal evidence.

This module deliberately has no append, pending-event recovery, executor, or
dispatch function.  It can only prove what an already accepted selected Run
recorded, then hand that evidence to :class:`RunExecutionSession` for state
reconstruction.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

import work_journal
from workflow_run_support import RunExecutionSession, SelectedRunError, _validate_common


MAX_JOURNAL_CARRIERS = 2_048
MAX_JOURNAL_CARRIER_BYTES = 16 * 1024 * 1024
MAX_JOURNAL_BYTES = 256 * 1024 * 1024
MAX_JOURNAL_EVENTS = 100_000
_PART_NAME = re.compile(r"^(?P<author>[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?)-(?P<date>\d{4}-\d{2}-\d{2})-part-(?P<part>[1-9][0-9]*)\.ndjson$")
_RECEIPT_DIGEST = hashlib.sha256(b"").hexdigest()


def canonical_dispatch_bytes(request: Mapping[str, Any]) -> bytes:
    """Return the exact immutable request bytes recorded before dispatch."""
    parsed = _validate_common(request)
    if parsed["mode"] != "execute":
        raise SelectedRunError("invalid-recovery", "only an execute request has dispatch recovery evidence")
    return work_journal.canonical_json_bytes({key: parsed[key] for key in sorted(parsed) if key != "mode"})


def inspect_selected_run_dispatch(root: str | Path, request: Mapping[str, Any]) -> dict[str, Any]:
    """Read and bind one accepted dispatch carrier without changing it."""
    root_path = _root(root)
    expected_bytes = canonical_dispatch_bytes(request)
    parsed = _validate_common(request)
    try:
        runtime_root = work_journal.configured_runtime_root(root_path)
        work_journal.configured_journal_root(root_path)
    except (OSError, RuntimeError) as error:
        raise SelectedRunError("invalid-recovery", f"configured recovery roots are unavailable: {error}") from error
    path = (
        root_path
        / runtime_root
        / "state"
        / "work_journal"
        / "selected_runs"
        / "requests"
        / f"{_sha256(parsed['request_id'].encode('utf-8'))}.json"
    )
    _require_regular_file(path, root_path / runtime_root)
    try:
        raw = path.read_bytes()
        value = json.loads(raw)
    except FileNotFoundError as error:
        raise SelectedRunError("dispatch-not-found", "accepted dispatch evidence does not exist") from error
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise SelectedRunError("invalid-dispatch-evidence", "cannot read accepted dispatch evidence") from error
    expected_fields = {
        "schema_version", "request_id", "canonical_request_bytes",
        "canonical_request_bytes_digest", "state",
    }
    if (
        not isinstance(value, dict)
        or set(value) != expected_fields
        or value.get("schema_version") != 1
        or value.get("request_id") != parsed["request_id"]
        or value.get("state") != "accepted"
        or not isinstance(value.get("canonical_request_bytes"), str)
    ):
        raise SelectedRunError("invalid-dispatch-evidence", "accepted dispatch evidence has invalid fields")
    encoded = value["canonical_request_bytes"].encode("utf-8")
    if (
        value.get("canonical_request_bytes_digest") != _sha256(encoded)
        or encoded != expected_bytes
    ):
        raise SelectedRunError("dispatch-mismatch", "accepted dispatch evidence does not bind this exact execute request")
    try:
        decoded = json.loads(encoded)
    except json.JSONDecodeError as error:
        raise SelectedRunError("invalid-dispatch-evidence", "accepted dispatch bytes are not JSON") from error
    if work_journal.canonical_json_bytes(decoded) != encoded:
        raise SelectedRunError("invalid-dispatch-evidence", "accepted dispatch bytes are not canonical")
    return {**value, "carrier": path.relative_to(root_path).as_posix()}


def validate_selected_run_events(
    request: Mapping[str, Any],
    events: Iterable[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Purely validate canonical started/terminal evidence.

    The iterable interface deliberately needs no repository, Journal carrier,
    temporary directory, executor, or writer.  It rejects ambiguous lineage
    rather than guessing which repeated requested Run an event represents.
    """
    collected = [dict(event) for event in events]
    evidence = [
        {
            "event": event,
            "receipt": {
                "event_id": event.get("event_id"),
                "action_id": event.get("action_id"),
                "event_digest": event.get("event_digest"),
                "carrier": f"memory/{index}.ndjson",
                "line": 1,
                "previous_carrier_digest": _RECEIPT_DIGEST,
                "appended_carrier_digest": _RECEIPT_DIGEST,
            },
        }
        for index, event in enumerate(collected, start=1)
    ]
    RunExecutionSession.restore(_NoEffectTracker(), request, evidence)
    return collected


def read_selected_run_evidence(root: str | Path, request: Mapping[str, Any]) -> dict[str, Any]:
    """Read bounded canonical Journal evidence for one accepted dispatch.

    The function reads only configured runtime dispatch evidence and canonical
    Journal part carriers.  It does not inspect pending evidence, append a
    recovery event, or execute an Action.
    """
    root_path = _root(root)
    dispatch = inspect_selected_run_dispatch(root_path, request)
    parsed = _validate_common(request)
    try:
        journal_root = root_path / work_journal.configured_journal_root(root_path)
    except (OSError, RuntimeError) as error:
        raise SelectedRunError("invalid-recovery", f"configured Journal root is unavailable: {error}") from error
    parts = _journal_parts(root_path, journal_root)
    records_seen = 0
    bytes_read = 0
    evidence: list[dict[str, Any]] = []
    for path in parts:
        try:
            raw = path.read_bytes()
        except OSError as error:
            raise SelectedRunError("invalid-recovery", f"cannot read canonical Journal carrier {path.name}") from error
        if len(raw) > MAX_JOURNAL_CARRIER_BYTES:
            raise SelectedRunError("recovery-limit", "a canonical Journal carrier exceeds the read limit")
        bytes_read += len(raw)
        if bytes_read > MAX_JOURNAL_BYTES:
            raise SelectedRunError("recovery-limit", "Journal scan exceeds the total byte read limit")
        if raw and not raw.endswith(b"\n"):
            raise SelectedRunError("invalid-recovery", f"canonical Journal carrier lacks terminal newline: {path.name}")
        lines = raw.splitlines(keepends=True)
        for line_number, line in enumerate(lines, start=1):
            if records_seen >= MAX_JOURNAL_EVENTS:
                raise SelectedRunError("recovery-limit", "Journal event scan exceeds the configured limit")
            try:
                event = json.loads(line)
            except json.JSONDecodeError as error:
                raise SelectedRunError("invalid-recovery", f"invalid JSON in canonical Journal carrier {path.name}:{line_number}") from error
            if not isinstance(event, dict):
                raise SelectedRunError("invalid-recovery", f"non-object Journal event in {path.name}:{line_number}")
            records_seen += 1
            if not _possibly_selected_event(event, parsed):
                continue
            if event.get("schema_version") != 5 or event.get("kind") != "workflow_execution":
                raise SelectedRunError("recovery-request-mismatch", "selected request identity occurs in non-canonical workflow evidence")
            session = event.get("llm_session")
            if not isinstance(session, Mapping) or session.get("uuid") != parsed["request_id"] or event.get("action_id") != parsed["assigned_action_id"]:
                raise SelectedRunError("recovery-request-mismatch", "Journal evidence has a partial selected-request identity match")
            try:
                sealed = work_journal.validate_sealed_event(event)
            except work_journal.WorkJournalError as error:
                raise SelectedRunError("invalid-recovery", f"invalid sealed selected Run evidence: {error}") from error
            previous = b"".join(lines[: line_number - 1])
            appended = b"".join(lines[:line_number])
            evidence.append(
                {
                    "event": sealed,
                    "receipt": {
                        "event_id": sealed["event_id"],
                        "action_id": sealed["action_id"],
                        "event_digest": sealed["event_digest"],
                        "carrier": path.relative_to(root_path).as_posix(),
                        "line": line_number,
                        "previous_carrier_digest": _sha256(previous),
                        "appended_carrier_digest": _sha256(appended),
                    },
                }
            )
    # Restore validates the reconstructed records with their real receipts,
    # including exact lifecycle, lineage, definition, outcome, and reference
    # bindings.  It is state-only and cannot replay an unfinished Run.
    RunExecutionSession.restore(_NoEffectTracker(), parsed, evidence)
    return {"dispatch": dispatch, "events": evidence}


class _NoEffectTracker:
    """Sentinel used only by pure reconstruction validation."""


def _root(root: str | Path) -> Path:
    path = Path(root)
    try:
        resolved = path.resolve(strict=True)
    except OSError as error:
        raise SelectedRunError("invalid-recovery", "recovery root does not exist") from error
    if not resolved.is_dir():
        raise SelectedRunError("invalid-recovery", "recovery root must be a directory")
    return resolved


def _journal_parts(root: Path, journal_root: Path) -> list[Path]:
    if not journal_root.exists():
        return []
    _require_regular_directory(journal_root, root)
    parts_by_partition: dict[tuple[str, str], list[tuple[int, Path]]] = {}
    for path in journal_root.iterdir():
        if path.is_symlink() or not path.is_file() or path.suffix != ".ndjson":
            continue
        match = _PART_NAME.fullmatch(path.name)
        if match is None:
            continue
        author, local_date, part = match["author"], match["date"], int(match["part"])
        try:
            work_journal.validate_partition(author, local_date, "recovery-read-only")
        except work_journal.WorkJournalError as error:
            raise SelectedRunError("invalid-recovery", f"invalid canonical Journal partition {path.name}: {error}") from error
        _require_regular_file(path, journal_root)
        parts_by_partition.setdefault((author, local_date), []).append((part, path))
    ordered: list[Path] = []
    for partition in sorted(parts_by_partition):
        entries = sorted(parts_by_partition[partition])
        if [part for part, _ in entries] != list(range(1, len(entries) + 1)):
            raise SelectedRunError("invalid-recovery", "canonical Journal partition parts are not contiguous")
        ordered.extend(path for _, path in entries)
    if len(ordered) > MAX_JOURNAL_CARRIERS:
        raise SelectedRunError("recovery-limit", "canonical Journal carrier count exceeds the read limit")
    return ordered


def _possibly_selected_event(event: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    session = event.get("llm_session")
    request_matches = isinstance(session, Mapping) and session.get("uuid") == request["request_id"]
    action_matches = event.get("action_id") == request["assigned_action_id"]
    return request_matches or action_matches


def _require_regular_directory(path: Path, root: Path) -> None:
    if path.is_symlink() or not path.is_dir() or root not in (path.resolve(), *path.resolve().parents):
        raise SelectedRunError("invalid-recovery", "configured Journal root is not a safe directory")


def _require_regular_file(path: Path, boundary: Path) -> None:
    if path.is_symlink() or not path.is_file():
        raise SelectedRunError("dispatch-not-found", "required recovery evidence is not a regular file")
    try:
        path.resolve(strict=True).relative_to(boundary.resolve(strict=True))
    except (OSError, ValueError) as error:
        raise SelectedRunError("invalid-recovery", "recovery evidence escapes its configured root") from error


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()
