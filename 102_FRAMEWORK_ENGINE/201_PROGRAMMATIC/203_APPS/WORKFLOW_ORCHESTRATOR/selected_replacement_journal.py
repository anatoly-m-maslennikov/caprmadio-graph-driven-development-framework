"""Record verified selected-replacement provenance in the canonical Work Journal."""

from __future__ import annotations

import hashlib
from collections.abc import Mapping
from pathlib import Path
import sys
from typing import Any


TOOLS = Path(__file__).resolve().parents[2] / "201_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from work_journal import (  # noqa: E402
    WorkJournalError,
    append_sealed_events,
    store_pending_event,
    validate_append_context,
    validate_sealed_event,
)


class ReplacementJournalError(RuntimeError):
    """The caller cannot prove or record selected-replacement provenance."""


def _replacement_event(
    root: Path,
    canonical_event: Mapping[str, Any],
    append_context: Mapping[str, Any],
) -> dict[str, Any]:
    """Validate all evidence required before a caller performs native effects."""

    try:
        event = validate_sealed_event(canonical_event)
        context = validate_append_context(root, append_context)
    except (TypeError, WorkJournalError) as error:
        raise ReplacementJournalError("canonical event or append context is invalid") from error

    result = event.get("result")
    if (
        event.get("schema_version") != 3
        or event.get("event") != "completed"
        or event.get("kind") != "governed_project_change"
        or event.get("subject_kind") != "file"
        or event.get("action_type") not in {"MOVE", "MOVE+UPDATE"}
        or not isinstance(event.get("predecessor_atom_id"), str)
        or not event["predecessor_atom_id"]
        or not isinstance(event.get("successor_atom_ids"), list)
        or not event["successor_atom_ids"]
        or not all(isinstance(atom_id, str) and atom_id for atom_id in event["successor_atom_ids"])
        or len(event["successor_atom_ids"]) != len(set(event["successor_atom_ids"]))
        or not isinstance(result, dict)
        or not isinstance(result.get("path"), str)
        or not isinstance(result.get("sha256"), str)
        or context["author"] != event["author"]
    ):
        raise ReplacementJournalError("canonical event is not replacement provenance")
    return event


def preflight(
    root: Path,
    canonical_event: Mapping[str, Any],
    append_context: Mapping[str, Any],
) -> dict[str, Any]:
    """Public preflight for callers before native replacement effects occur."""

    return _replacement_event(Path(root), canonical_event, append_context)


def _read_verified_result(root: Path, result: Mapping[str, Any]) -> Path:
    """Return a regular in-root result file after rejecting symlink traversal."""

    relative = Path(str(result["path"]))
    if relative.is_absolute() or ".." in relative.parts or not relative.parts:
        raise ReplacementJournalError("replacement readback path is unsafe")

    canonical_root = root.resolve()
    candidate = root / relative
    current = root
    for component in relative.parts:
        current = current / component
        if current.is_symlink():
            raise ReplacementJournalError("replacement readback path is unsafe")
    try:
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(canonical_root)
    except (OSError, RuntimeError, ValueError) as error:
        raise ReplacementJournalError("replacement readback path is unsafe") from error
    if not resolved.is_file() or resolved.is_symlink():
        raise ReplacementJournalError("replacement readback path is unsafe")
    if hashlib.sha256(resolved.read_bytes()).hexdigest() != result["sha256"]:
        raise ReplacementJournalError("replacement readback differs from sealed result")
    return resolved


def _pending(
    root: Path,
    event: Mapping[str, Any],
    append_context: Mapping[str, Any],
    result_path: str,
    diagnostic: str,
) -> Mapping[str, Any]:
    try:
        pending = store_pending_event(
            root,
            event,
            append_context,
            result_ref=None,
            effect_refs=[result_path],
            diagnostic=diagnostic,
        )
    except (OSError, WorkJournalError) as error:
        raise ReplacementJournalError("could not preserve pending replacement evidence") from error
    return {"state": "recording_pending", "pending": pending}


def record_selected_replacement(
    root: Path,
    *,
    canonical_event: Mapping[str, Any],
    append_context: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Append a canonical replacement event after exact on-disk readback.

    A failed or unconfirmed append becomes retry-only pending evidence; it never
    reports a completed replacement record without a matching Journal receipt.
    """

    project_root = Path(root)
    event = _replacement_event(project_root, canonical_event, append_context)
    result = event["result"]
    _read_verified_result(project_root, result)
    try:
        receipts = append_sealed_events(
            project_root,
            [event],
            author=append_context["author"],
            local_date=append_context["local_date"],
            timezone=append_context["timezone"],
            append_context=append_context,
        )
    except (KeyError, OSError, WorkJournalError) as error:
        return _pending(project_root, event, append_context, result["path"], type(error).__name__)

    if len(receipts) != 1:
        return _pending(project_root, event, append_context, result["path"], "unconfirmed-append")
    receipt = receipts[0]
    if (
        not isinstance(receipt, Mapping)
        or receipt.get("event_id") != event["event_id"]
        or receipt.get("event_digest") != event["event_digest"]
    ):
        return _pending(project_root, event, append_context, result["path"], "unconfirmed-append")
    return {"state": "completed", "event": event, "receipt": receipt}
