"""Pure continuation routing for caller-owned, already reconciled Run state.

This is not evidence admission or semantic verification. It does not read or
write files, spawn agents, retry operations, or authorize mutations. In
particular, ``validate_completion`` is a request for the existing full-request
gates, never proof that any review is correct or complete.
"""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import hashlib
import json
from pathlib import PurePosixPath
import re


STAGES = {"queued", "review", "propose_repair", "verify_proposal", "apply_repair",
          "verify_saved", "verified"}


def checkpoint_sha256(checkpoint: Mapping) -> str:
    """Digest canonical JSON; the caller must persist and reopen these bytes."""
    raw = json.dumps(checkpoint, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def _pin(binding: Mapping) -> None:
    if not isinstance(binding, Mapping):
        raise ValueError("binding must be a mapping")
    path, digest = binding.get("path"), binding.get("sha256")
    if (not isinstance(path, str) or not path or PurePosixPath(path).is_absolute()
            or ".." in PurePosixPath(path).parts or not isinstance(digest, str)
            or not re.fullmatch(r"[a-f0-9]{64}", digest)):
        raise ValueError("binding needs a relative path and SHA-256")


def _pins(rows: list, *, nonempty: bool = True) -> None:
    if not isinstance(rows, list) or (nonempty and not rows):
        raise ValueError("binding lists must be present and nonempty when required")
    for row in rows:
        _pin(row)


def _source(binding: Mapping) -> None:
    _pin(binding)
    if not {"atom_id", "version"} <= binding.keys():
        raise ValueError("source must retain identity and version, including explicit absence")


def _integer(value, *, minimum: int = 0) -> bool:
    return type(value) is int and value >= minimum


def _validate(checkpoint: Mapping) -> dict[int, Mapping]:
    if checkpoint.get("schema_version") != 1 or not checkpoint.get("request_id"):
        raise ValueError("schema_version 1 and request_id are required")
    selection, items = checkpoint.get("selection"), checkpoint.get("items")
    if not isinstance(selection, list) or not isinstance(items, list):
        raise ValueError("original selection and every work item are required")
    ordinals = []
    for row in selection:
        if not isinstance(row, Mapping) or not _integer(row.get("ordinal"), minimum=1):
            raise ValueError("selection needs positive integer ordinals")
        ordinals.append(row["ordinal"])
        _source(row.get("source"))
    if len(ordinals) != len(set(ordinals)):
        raise ValueError("duplicate original selection ordinal")
    by_ordinal = {}
    for item in items:
        if not isinstance(item, Mapping) or not _integer(item.get("ordinal"), minimum=1):
            raise ValueError("work item needs an ordinal")
        ordinal = item["ordinal"]
        if ordinal in by_ordinal or item.get("stage") not in STAGES:
            raise ValueError("duplicate work item or unknown stage")
        by_ordinal[ordinal] = item
        _source(item.get("source"))
        bindings = item.get("bindings", {})
        for group in ("authority", "settings", "prompts"):
            _pins(bindings.get(group))
        _pins(item.get("evidence"), nonempty=item["stage"] == "verified")
        used, limit = item.get("retries_used"), item.get("retry_limit")
        if not _integer(used) or not _integer(limit) or used > limit:
            raise ValueError("invalid repair retry accounting")
        effects, seen = item.get("completed_effects"), set()
        if not isinstance(effects, list):
            raise ValueError("completed_effects must be explicit")
        for effect in effects:
            effect_id = effect.get("effect_id")
            if not isinstance(effect_id, str) or not effect_id or effect_id in seen:
                raise ValueError("completed effects need unique effect_id values")
            seen.add(effect_id)
            _source(effect.get("before_source"))
            _source(effect.get("after_source"))
            _pins(effect.get("evidence"))
        if item["stage"] == "apply_repair" and not item.get("pending_effect_id"):
            raise ValueError("apply_repair needs a stable pending_effect_id")
    if set(by_ordinal) != set(ordinals):
        raise ValueError("items must cover the entire original selection exactly")
    resume = checkpoint.get("resume_ordinal")
    if resume is not None and (not _integer(resume, minimum=1) or resume not in by_ordinal):
        raise ValueError("resume_ordinal must belong to the original selection")
    if not _integer(checkpoint.get("max_handoffs_without_progress"), minimum=1):
        raise ValueError("a positive no-progress handoff bound is required")
    history = checkpoint.get("handoffs")
    if not isinstance(history, list):
        raise ValueError("successful handoff history must be explicit")
    dispatches = set()
    for entry in history:
        if (entry.get("ordinal") not in by_ordinal
                or not re.fullmatch(r"[a-f0-9]{64}", entry.get("progress_sha256", ""))
                or not isinstance(entry.get("dispatch_id"), str)
                or not entry["dispatch_id"] or entry["dispatch_id"] in dispatches):
            raise ValueError("invalid or duplicate successful handoff")
        dispatches.add(entry["dispatch_id"])
    blocker = checkpoint.get("blocker")
    if blocker is not None and (not isinstance(blocker, Mapping)
                               or not blocker.get("kind") or not blocker.get("reason")):
        raise ValueError("blocker needs its actual kind and reason")
    return by_ordinal


def progress_sha256(item: Mapping) -> str:
    """Fingerprint retained work, not token counters or repair retry changes.

    The caller admits the referenced artifacts and reconciles effects before
    supplying them; changing a hash is not itself meaningful semantic progress.
    """
    return checkpoint_sha256({key: item[key] for key in
                              ("stage", "source", "evidence", "completed_effects")})


def next_action(checkpoint: Mapping, *, durable_sha256: str | None = None,
                available_slots: int, active_ordinals: tuple[int, ...] = ()) -> dict:
    """Route explicitly trusted caller state, returning no execution side effects.

    ``durable_sha256`` acknowledges the checkpoint actually saved and reopened.
    The caller records a successful dispatch in ``handoffs`` once, and records
    an actual host refusal in ``blocker`` before routing again. Active workers
    stay active until stopped/finished; available_slots is host capacity, not
    a guessed context budget. No action consumes a repair retry.
    """
    base = {"completion_verified": False, "source_mutation_authorized": False}
    try:
        items = _validate(checkpoint)
        if (not _integer(available_slots) or len(set(active_ordinals)) != len(active_ordinals)
                or any(type(o) is not int or o not in items for o in active_ordinals)):
            raise ValueError("invalid host slot or active-assignment state")
        state = deepcopy(dict(checkpoint))
        pending = [row["ordinal"] for row in state["selection"]
                   if items[row["ordinal"]]["stage"] != "verified"]
        if (state.get("blocker") or {}).get("kind") == "context_capacity":
            if state.get("resume_ordinal") not in pending:
                raise ValueError("context_capacity requires its exact unfinished resume_ordinal")
            state["continuation_reason"] = state["blocker"]
            state["blocker"] = None
        ordinal = state.get("resume_ordinal")
        if ordinal not in pending or ordinal in active_ordinals:
            ordinal = next((o for o in pending if o not in active_ordinals), None)
        item = items.get(ordinal)
        stage = item["stage"] if item else None
        if item and not state.get("blocker"):
            matching = 0
            progress = progress_sha256(item)
            for entry in reversed(state["handoffs"]):
                if entry["ordinal"] != ordinal:
                    continue
                if entry["progress_sha256"] != progress:
                    break
                matching += 1
            if matching >= state["max_handoffs_without_progress"]:
                state["blocker"] = {"kind": "no_progress", "reason":
                    f"ordinal {ordinal} reached its handoff bound without durable progress"}
            if stage == "apply_repair":
                effect = next((e for e in item["completed_effects"]
                               if e["effect_id"] == item["pending_effect_id"]), None)
                if effect:
                    if effect["after_source"] != item["source"]:
                        state["blocker"] = {"kind": "effect_reconciliation", "reason":
                            "completed effect differs from saved source; reconcile before dispatch"}
                    else:
                        stage = "verify_saved"
        digest = checkpoint_sha256(state)
        if durable_sha256 != digest:
            return dict(base, action="checkpoint_required", checkpoint=state,
                        checkpoint_sha256=digest)
        if state.get("blocker"):
            if (state["blocker"]["kind"] in {"host_spawn_denied", "host_spawn_refused"}
                    and active_ordinals):
                return dict(base, action="wait_for_slot", reason=state["blocker"],
                            pending_ordinals=pending, checkpoint_sha256=digest)
            return dict(base, action="blocked", reason=state["blocker"], checkpoint_sha256=digest)
        if not pending and not active_ordinals:
            return dict(base, action="validate_completion", ordinals=[r["ordinal"] for r in state["selection"]],
                        checkpoint_sha256=digest)
        if ordinal is None or available_slots == 0:
            return dict(base, action="wait_for_slot", pending_ordinals=pending,
                        checkpoint_sha256=digest)
        return dict(base, action="spawn_subagent", ordinal=ordinal,
                    stage="review" if stage == "queued" else stage,
                    model="gpt-5.6-terra", reasoning_effort="high", fresh_context=True,
                    independent=stage in {"verify_proposal", "verify_saved"},
                    checkpoint_sha256=digest, dispatch_id=f"{digest}:{ordinal}",
                    progress_sha256=progress_sha256(item))
    except (AttributeError, KeyError, TypeError, ValueError) as error:
        return dict(base, action="blocked", reason={"kind": "invalid_state", "reason": str(error)})
