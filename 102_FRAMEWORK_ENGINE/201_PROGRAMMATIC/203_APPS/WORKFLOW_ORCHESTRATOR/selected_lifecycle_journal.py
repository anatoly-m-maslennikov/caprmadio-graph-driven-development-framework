"""Canonical Journal admission for observed lifecycle carrier changes."""

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
    _all_journal_parts,
    _carrier_records,
    append_sealed_events,
    store_pending_event,
    validate_append_context,
    validate_sealed_event,
    with_event_digest,
)


class LifecycleJournalError(RuntimeError):
    """Lifecycle provenance is absent, ambiguous, stale, or unrecordable."""


def _result(facts: Mapping[str, Any], current_bytes: bytes) -> dict[str, Any]:
    value = dict(facts)
    if set(value) != {"filename", "version", "path", "sha256"}:
        raise LifecycleJournalError("carrier facts must be exactly filename, version, path, and sha256")
    path = Path(value["path"]) if isinstance(value["path"], str) else None
    if (
        not isinstance(value["filename"], str)
        or not value["filename"]
        or type(value["version"]) is not int
        or value["version"] < 1
        or path is None
        or path.is_absolute()
        or ".." in path.parts
        or not isinstance(value["sha256"], str)
        or len(value["sha256"]) != 64
        or not isinstance(current_bytes, bytes)
        or hashlib.sha256(current_bytes).hexdigest() != value["sha256"]
    ):
        raise LifecycleJournalError("carrier facts do not bind the observed bytes")
    return {"state": "present", **value}


def _pin(action_pin: Mapping[str, Any], run_id: str) -> dict[str, Any]:
    value = dict(action_pin)
    if (
        set(value) != {"action_id", "structural_scope", "occurred_at", "llm_session"}
        or not isinstance(value["action_id"], str)
        or not value["action_id"]
        or not isinstance(value["structural_scope"], str)
        or not value["structural_scope"]
        or not isinstance(value["occurred_at"], str)
        or not isinstance(value["llm_session"], dict)
        or set(value["llm_session"]) != {"app", "uuid"}
        or not isinstance(run_id, str)
        or not run_id
    ):
        raise LifecycleJournalError("lifecycle action pin or run identity is invalid")
    return value


def _readback(root: Path, result: Mapping[str, Any]) -> None:
    relative = Path(result["path"])
    candidate = root / relative
    current = root
    for component in relative.parts:
        current = current / component
        if current.is_symlink():
            raise LifecycleJournalError("carrier readback path is unsafe")
    try:
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(root.resolve())
    except (OSError, RuntimeError, ValueError) as error:
        raise LifecycleJournalError("carrier readback path is unsafe") from error
    if not resolved.is_file() or hashlib.sha256(resolved.read_bytes()).hexdigest() != result["sha256"]:
        raise LifecycleJournalError("carrier readback differs from prepared Journal result")


def _matching_prior(root: Path, result: Mapping[str, Any]) -> tuple[dict[str, Any], dict[str, Any]] | None:
    matches: list[dict[str, Any]] = []
    try:
        for carrier in _all_journal_parts(root):
            _bytes, records = _carrier_records(carrier)
            for raw in records:
                event = validate_sealed_event(raw)
                recorded = event.get("result")
                if (
                    event.get("schema_version") in {2, 3}
                    and event.get("event") in {"completed", "recovered"}
                    and isinstance(recorded, Mapping)
                    and all(recorded.get(key) == result.get(key) for key in ("path", "version", "sha256"))
                ):
                    matches.append(event)
    except (OSError, WorkJournalError) as error:
        raise LifecycleJournalError("canonical lifecycle Journal is unavailable") from error
    if len(matches) > 1:
        raise LifecycleJournalError("carrier has ambiguous canonical prior state")
    if not matches:
        return None
    event = matches[0]
    for carrier in _all_journal_parts(root):
        data, records = _carrier_records(carrier)
        for line, raw in enumerate(records, start=1):
            candidate = validate_sealed_event(raw)
            if candidate.get("event_id") == event["event_id"]:
                if candidate.get("event_digest") != event["event_digest"]:
                    raise LifecycleJournalError("canonical lifecycle prior identity changed")
                lines = data.splitlines(keepends=True)
                receipt = {
                    "event_id": event["event_id"],
                    "action_id": event["action_id"],
                    "event_digest": event["event_digest"],
                    "carrier": carrier.relative_to(root).as_posix(),
                    "line": line,
                    "previous_carrier_digest": hashlib.sha256(b"".join(lines[: line - 1])).hexdigest(),
                    "appended_carrier_digest": hashlib.sha256(b"".join(lines[:line])).hexdigest(),
                }
                return event, receipt
    raise LifecycleJournalError("canonical lifecycle prior has no verified receipt")


def _fresh_prior_receipt(root: Path, event: Mapping[str, Any]) -> dict[str, Any]:
    """Re-scan the Journal; cached receipts cannot admit a lifecycle effect."""

    found = _matching_prior(root, event["result"])
    if found is None:
        raise LifecycleJournalError("lifecycle prior is absent from the canonical Journal")
    current, receipt = found
    if (
        current.get("event_id") != event["event_id"]
        or current.get("event_digest") != event["event_digest"]
    ):
        raise LifecycleJournalError("lifecycle prior identity is not currently canonical")
    return receipt


def prepare_lifecycle_journal(
    root: Path,
    before_facts: Mapping[str, Any],
    current_bytes: bytes,
    action_pin: Mapping[str, Any],
    run_id: str,
    context: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Return one exact prior event or a carrier-only recovered baseline.

    This does not append or execute any lifecycle effect.
    """

    project_root = Path(root)
    result = _result(before_facts, current_bytes)
    pin = _pin(action_pin, run_id)
    prior = _matching_prior(project_root, result)
    if prior is not None:
        event, receipt = prior
        return {"state": "exact_prior", "event": event, "receipt": receipt}
    try:
        partition = validate_append_context(project_root, context)
    except (TypeError, WorkJournalError) as error:
        raise LifecycleJournalError("lifecycle append context is invalid") from error

    event = with_event_digest(
        {
            "schema_version": 3,
            "event_id": f"lifecycle-baseline:{run_id}",
            "action_id": pin["action_id"],
            "event": "recovered",
            "kind": "governed_project_state",
            "subject_kind": "file",
            "author": partition["author"],
            "occurred_at": pin["occurred_at"],
            "llm_session": pin["llm_session"],
            "structural_scope": pin["structural_scope"],
            "result": result,
            "recovery_evidence": {
                "carrier": {
                    "path": result["path"],
                    "sha256": result["sha256"],
                    "observed_at": pin["occurred_at"],
                    "observer_run_id": run_id,
                }
            },
        }
    )
    return {"state": "prepared_observed_baseline", "event": event}


def _pending(root: Path, event: Mapping[str, Any], context: Mapping[str, Any], diagnostic: str) -> Mapping[str, Any]:
    try:
        pending = store_pending_event(
            root,
            event,
            context,
            result_ref=None,
            effect_refs=[event["result"]["path"]],
            diagnostic=diagnostic,
        )
    except (OSError, WorkJournalError) as error:
        raise LifecycleJournalError("could not preserve lifecycle pending evidence") from error
    return {"state": "recording_pending", "pending": pending}


def _append_confirmed(root: Path, event: Mapping[str, Any], context: Mapping[str, Any]) -> Mapping[str, Any]:
    try:
        receipts = append_sealed_events(
            root,
            [event],
            author=context["author"],
            local_date=context["local_date"],
            timezone=context["timezone"],
            append_context=context,
        )
    except (KeyError, OSError, WorkJournalError) as error:
        return _pending(root, event, context, type(error).__name__)
    if len(receipts) != 1 or receipts[0].get("event_id") != event["event_id"] or receipts[0].get("event_digest") != event["event_digest"]:
        return _pending(root, event, context, "unconfirmed-append")
    return {"state": "admitted", "event": event, "receipt": receipts[0]}


def admit_lifecycle_prior(root: Path, prepared: Mapping[str, Any], context: Mapping[str, Any]) -> Mapping[str, Any]:
    """Read back and durably confirm the one prior state before native effects."""

    if not isinstance(prepared, Mapping) or prepared.get("state") not in {"exact_prior", "prepared_observed_baseline"}:
        raise LifecycleJournalError("prepared lifecycle prior is invalid")
    try:
        event = validate_sealed_event(prepared.get("event"))
    except (TypeError, WorkJournalError) as error:
        raise LifecycleJournalError("prepared lifecycle prior is invalid") from error
    _readback(Path(root), event["result"])
    if prepared["state"] == "exact_prior":
        receipt = _fresh_prior_receipt(Path(root), event)
        return {"state": "admitted", "event": event, "receipt": receipt}
    try:
        partition = validate_append_context(Path(root), context)
    except (TypeError, WorkJournalError) as error:
        raise LifecycleJournalError("lifecycle append context is invalid") from error
    if partition["author"] != event["author"]:
        raise LifecycleJournalError("lifecycle append context author differs from prior event author")
    return _append_confirmed(Path(root), event, partition)


def record_lifecycle_change(
    root: Path,
    *,
    prior: Mapping[str, Any],
    after_facts: Mapping[str, Any],
    current_bytes: bytes,
    action_pin: Mapping[str, Any],
    run_id: str,
    context: Mapping[str, Any],
    action_type: str,
    native_effects: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Record an observed non-ADD lifecycle change linked to an admitted prior."""

    before = validate_sealed_event(prior)
    if before.get("event") not in {"completed", "recovered"}:
        raise LifecycleJournalError("lifecycle change requires an admitted prior result")
    _fresh_prior_receipt(Path(root), before)
    after = _result(after_facts, current_bytes)
    if all(before["result"].get(key) == after.get(key) for key in ("path", "version", "sha256")):
        return {"state": "no_op"}
    if action_type not in {"UPDATE", "MOVE", "MOVE+UPDATE"}:
        raise LifecycleJournalError("lifecycle change action type is invalid")
    if not isinstance(native_effects, Mapping) or native_effects.get("result") != after:
        raise LifecycleJournalError("native lifecycle effects do not match observed after state")
    pin = _pin(action_pin, run_id)
    try:
        partition = validate_append_context(Path(root), context)
    except (TypeError, WorkJournalError) as error:
        raise LifecycleJournalError("lifecycle append context is invalid") from error
    event = with_event_digest(
        {
            "schema_version": 3,
            "event_id": f"lifecycle-change:{run_id}",
            "action_id": pin["action_id"],
            "event": "completed",
            "kind": "governed_project_change",
            "subject_kind": "file",
            "author": partition["author"],
            "occurred_at": pin["occurred_at"],
            "llm_session": pin["llm_session"],
            "structural_scope": pin["structural_scope"],
            "action_type": action_type,
            "sources": [],
            "previous_result_event": before["event_id"],
            "result": after,
        }
    )
    _readback(Path(root), after)
    return _append_confirmed(Path(root), event, partition)
