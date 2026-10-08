"""Record observed W01-created file state in the canonical Work Journal."""

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
    seal_append_context,
    store_pending_event,
    validate_append_context,
    validate_sealed_event,
)


class CreationJournalError(RuntimeError):
    """The caller cannot prove or record observed creation provenance."""


def _creation_event(canonical_event: Mapping[str, Any]) -> dict[str, Any]:
    try:
        event = validate_sealed_event(canonical_event)
    except (TypeError, WorkJournalError) as error:
        raise CreationJournalError("canonical creation event is invalid") from error

    result = event.get("result")
    if (
        event.get("schema_version") != 3
        or event.get("event") != "completed"
        or event.get("kind") != "governed_project_change"
        or event.get("subject_kind") != "file"
        or event.get("action_type") != "ADD"
        or "previous_result_event" in event
        or "predecessor_atom_id" in event
        or "successor_atom_ids" in event
        or not isinstance(result, dict)
        or not isinstance(result.get("path"), str)
        or not isinstance(result.get("sha256"), str)
    ):
        raise CreationJournalError("canonical event is not observed file creation")
    return event


def preflight_creation(canonical_event: Mapping[str, Any]) -> dict[str, Any]:
    """Validate an observed W01 ADD event without constructing any history."""

    return _creation_event(canonical_event)


def seal_creation_append_context(
    root: Path,
    canonical_event: Mapping[str, Any],
    *,
    author: object,
    local_date: object,
    timezone: object,
) -> dict[str, Any]:
    """Seal the event's original Journal partition for its one append attempt."""

    event = _creation_event(canonical_event)
    try:
        return seal_append_context(root, event, author=author, local_date=local_date, timezone=timezone)
    except WorkJournalError as error:
        raise CreationJournalError("could not seal creation append context") from error


def _read_observed_result(root: Path, result: Mapping[str, Any]) -> None:
    relative = Path(str(result["path"]))
    if relative.is_absolute() or ".." in relative.parts or not relative.parts:
        raise CreationJournalError("created carrier readback path is unsafe")

    canonical_root = root.resolve()
    candidate = root / relative
    current = root
    for component in relative.parts:
        current = current / component
        if current.is_symlink():
            raise CreationJournalError("created carrier readback path is unsafe")
    try:
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(canonical_root)
    except (OSError, RuntimeError, ValueError) as error:
        raise CreationJournalError("created carrier readback path is unsafe") from error
    if not resolved.is_file() or resolved.is_symlink():
        raise CreationJournalError("created carrier readback path is unsafe")
    if hashlib.sha256(resolved.read_bytes()).hexdigest() != result["sha256"]:
        raise CreationJournalError("created carrier readback differs from sealed result")


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
        raise CreationJournalError("could not preserve pending creation evidence") from error
    return {"state": "recording_pending", "pending": pending}


def record_selected_creation(
    root: Path,
    *,
    canonical_event: Mapping[str, Any],
    append_context: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Append one observed creation event after exact source-file readback."""

    project_root = Path(root)
    event = _creation_event(canonical_event)
    try:
        context = validate_append_context(project_root, append_context)
    except (TypeError, WorkJournalError) as error:
        raise CreationJournalError("creation append context is invalid") from error
    if context["author"] != event["author"]:
        raise CreationJournalError("creation append context author differs from event author")

    result = event["result"]
    _read_observed_result(project_root, result)
    try:
        receipts = append_sealed_events(
            project_root,
            [event],
            author=context["author"],
            local_date=context["local_date"],
            timezone=context["timezone"],
            append_context=context,
        )
    except (OSError, WorkJournalError) as error:
        return _pending(project_root, event, context, result["path"], type(error).__name__)

    if len(receipts) != 1:
        return _pending(project_root, event, context, result["path"], "unconfirmed-append")
    receipt = receipts[0]
    if (
        not isinstance(receipt, Mapping)
        or receipt.get("event_id") != event["event_id"]
        or receipt.get("event_digest") != event["event_digest"]
    ):
        return _pending(project_root, event, context, result["path"], "unconfirmed-append")
    return {"state": "completed", "event": event, "receipt": receipt}
