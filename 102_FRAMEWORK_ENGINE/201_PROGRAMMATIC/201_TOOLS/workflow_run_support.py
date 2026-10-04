"""Shared, non-executable admission and evidence support for selected runs.

Route-specific policy and effects stay with injected callers.  This module only
seals the common request, rechecks declared currentness, shapes actual Run
provenance, and records it through :mod:`work_journal`.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import uuid
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import work_journal


SHA256 = "0123456789abcdef"
MODES = frozenset({"preview", "execute"})
OUTCOMES = frozenset({"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"})
RUN_KINDS = frozenset({"workflow", "step", "action"})
_COMMON_FIELDS = frozenset(
    {
        "mode",
        "request_id",
        "operation_route",
        "parameters",
        "parameters_digest",
        "target_frontier",
        "target_frontier_digest",
        "effects",
        "effects_digest",
        "definition_manifest",
        "source_freshness",
        "initiative",
        "lineage",
        "expected_definition_revisions",
        "requested_runs",
    }
)
_EXECUTE_FIELDS = _COMMON_FIELDS | frozenset(
    {
        "proposal_receipt",
        "proposal_receipt_digest",
        "assigned_action_id",
        "operator_authorization",
    }
)
_SOURCE_FIELDS = frozenset(
    {
        "selected_source_registry_ref",
        "selected_source_registry_version",
        "selected_source_registry_digest",
        "selected_binding_ref",
        "selected_binding_digest",
    }
)


class SelectedRunError(ValueError):
    """Stable, pre-effect selected-run refusal."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


def _require_string(value: Mapping[str, Any], key: str) -> str:
    item = value.get(key)
    if not isinstance(item, str) or not item:
        raise SelectedRunError("invalid-request", f"{key} must be a non-empty string")
    return item


def _require_digest(value: object, key: str) -> str:
    if not isinstance(value, str) or len(value) != 64 or any(character not in SHA256 for character in value):
        raise SelectedRunError("invalid-request", f"{key} must be a lowercase SHA-256 digest")
    return value


def _safe_ref(value: object, key: str) -> str:
    if not isinstance(value, str) or not value:
        raise SelectedRunError("invalid-request", f"{key} must be a non-empty safe reference")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise SelectedRunError("invalid-request", f"{key} must be repository-relative")
    return value


def _reject_secrets(value: object, location: str = "parameters") -> None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if not isinstance(key, str):
                raise SelectedRunError("invalid-request", f"{location} keys must be strings")
            if any(word in key.lower() for word in ("secret", "password", "token", "credential")):
                raise SelectedRunError("secret-input", f"{location}.{key} is not admitted in selected-run input")
            _reject_secrets(item, f"{location}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _reject_secrets(item, f"{location}[{index}]")


def _definition(value: object, *, location: str = "definition") -> dict[str, Any]:
    if not isinstance(value, Mapping) or set(value) != {"atom_id", "version", "path", "digest"}:
        raise SelectedRunError("invalid-request", f"{location} must contain atom_id, version, path, and digest")
    atom_id = _require_string(value, "atom_id")
    version = value.get("version")
    if type(version) is not int or version < 1:
        raise SelectedRunError("invalid-request", f"{location}.version must be a positive integer")
    return {"atom_id": atom_id, "version": version, "path": _safe_ref(value.get("path"), f"{location}.path"), "digest": _require_digest(value.get("digest"), f"{location}.digest")}


def _canonical_digest(value: object) -> str:
    return work_journal.canonical_json_digest(value)


def _validate_common(request: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(request, Mapping):
        raise SelectedRunError("invalid-request", "request must be an object")
    mode = request.get("mode", "preview")
    if mode not in MODES:
        raise SelectedRunError("invalid-mode", "mode must be literal preview or execute")
    allowed = _EXECUTE_FIELDS if mode == "execute" else _COMMON_FIELDS
    unknown = set(request) - allowed
    if unknown:
        raise SelectedRunError("unknown-field", f"request contains unknown field(s): {', '.join(sorted(unknown))}")
    required = {
        "request_id", "operation_route", "parameters", "parameters_digest", "target_frontier",
        "target_frontier_digest", "effects", "effects_digest", "definition_manifest", "source_freshness", "initiative",
    }
    if mode == "execute":
        required |= {"proposal_receipt", "proposal_receipt_digest", "assigned_action_id", "operator_authorization", "requested_runs"}
    missing = required - set(request)
    if missing:
        raise SelectedRunError("invalid-request", f"request is missing: {', '.join(sorted(missing))}")
    result = dict(request)
    result["mode"] = mode
    _require_string(result, "request_id")
    _require_string(result, "operation_route")
    if not isinstance(result["parameters"], Mapping):
        raise SelectedRunError("invalid-request", "parameters must be a typed object")
    _reject_secrets(result["parameters"])
    if _canonical_digest(result["parameters"]) != _require_digest(result.get("parameters_digest"), "parameters_digest"):
        raise SelectedRunError("digest-mismatch", "parameters_digest does not bind parameters")
    if not isinstance(result["target_frontier"], list) or not result["target_frontier"]:
        raise SelectedRunError("invalid-request", "target_frontier must be a non-empty ordered list")
    if any(_safe_ref(item, "target_frontier item") != item for item in result["target_frontier"]):
        raise AssertionError("safe reference normalization must preserve its input")
    if len(set(result["target_frontier"])) != len(result["target_frontier"]):
        raise SelectedRunError("invalid-request", "target_frontier must not contain duplicate references")
    if _canonical_digest(result["target_frontier"]) != _require_digest(result.get("target_frontier_digest"), "target_frontier_digest"):
        raise SelectedRunError("digest-mismatch", "target_frontier_digest does not bind target_frontier")
    if not isinstance(result["effects"], list):
        raise SelectedRunError("invalid-request", "effects must be an ordered typed list")
    for effect in result["effects"]:
        if not isinstance(effect, Mapping) or not isinstance(effect.get("type"), str) or not effect["type"]:
            raise SelectedRunError("invalid-request", "each effect must include a non-empty type")
    _reject_secrets(result["effects"], "effects")
    if _canonical_digest(result["effects"]) != _require_digest(result.get("effects_digest"), "effects_digest"):
        raise SelectedRunError("digest-mismatch", "effects_digest does not bind effects")
    manifest = result["definition_manifest"]
    if not isinstance(manifest, Mapping) or set(manifest) != {"manifest_ref", "manifest_digest"}:
        raise SelectedRunError("invalid-request", "definition_manifest must contain only manifest_ref and manifest_digest")
    result["definition_manifest"] = {"manifest_ref": _safe_ref(manifest["manifest_ref"], "definition_manifest.manifest_ref"), "manifest_digest": _require_digest(manifest["manifest_digest"], "definition_manifest.manifest_digest")}
    source = result["source_freshness"]
    if not isinstance(source, Mapping):
        raise SelectedRunError("invalid-request", "source_freshness must be an object")
    unknown_source = set(source) - _SOURCE_FIELDS
    if unknown_source:
        raise SelectedRunError("unknown-field", "source_freshness contains an unknown field")
    if set(source) != _SOURCE_FIELDS:
        raise SelectedRunError("invalid-request", "source_freshness has missing required fields")
    registry_version = source["selected_source_registry_version"]
    if type(registry_version) is not int or registry_version < 1:
        raise SelectedRunError("invalid-request", "selected_source_registry_version must be a positive integer")
    result["source_freshness"] = {
        "selected_source_registry_ref": _safe_ref(source["selected_source_registry_ref"], "selected_source_registry_ref"),
        "selected_source_registry_version": registry_version,
        "selected_source_registry_digest": _require_digest(source["selected_source_registry_digest"], "selected_source_registry_digest"),
        "selected_binding_ref": _safe_ref(source["selected_binding_ref"], "selected_binding_ref"),
        "selected_binding_digest": _require_digest(source["selected_binding_digest"], "selected_binding_digest"),
    }
    initiative = result["initiative"]
    if not isinstance(initiative, Mapping) or set(initiative) - {"initiative_id", "instruction_summary", "initiative_ref"}:
        raise SelectedRunError("invalid-request", "initiative has unsupported fields")
    result["initiative"] = {
        "initiative_id": _require_string(initiative, "initiative_id"),
        "instruction_summary": _require_string(initiative, "instruction_summary"),
        **({"initiative_ref": _safe_ref(initiative["initiative_ref"], "initiative.initiative_ref")} if "initiative_ref" in initiative else {}),
    }
    if "lineage" in result:
        if not isinstance(result["lineage"], list) or any(not isinstance(item, str) or not item for item in result["lineage"]):
            raise SelectedRunError("invalid-request", "lineage must contain only actual non-empty references")
    if "expected_definition_revisions" in result:
        expected = result["expected_definition_revisions"]
        if not isinstance(expected, list) or not expected:
            raise SelectedRunError("invalid-request", "expected_definition_revisions must be a non-empty ordered list when supplied")
        normalized: list[dict[str, Any]] = []
        prior: tuple[str, str, int, str] | None = None
        for item in expected:
            if not isinstance(item, Mapping) or set(item) != {"atom_id", "kind", "version", "path", "digest"}:
                raise SelectedRunError("invalid-request", "expected definition revision has invalid fields")
            if item["kind"] not in RUN_KINDS:
                raise SelectedRunError("invalid-request", "expected definition kind is invalid")
            definition = _definition(item, location="expected definition")
            normalized_item = {"kind": item["kind"], **definition}
            sort_key = (normalized_item["kind"], normalized_item["atom_id"], normalized_item["version"], normalized_item["path"])
            if prior is not None and sort_key <= prior:
                raise SelectedRunError("invalid-request", "expected_definition_revisions must be uniquely canonical")
            normalized.append(normalized_item)
            prior = sort_key
        result["expected_definition_revisions"] = normalized
    if "requested_runs" in result:
        result["requested_runs"] = _validate_requested_runs(result["requested_runs"])
    return result


def _validate_requested_runs(value: object) -> list[dict[str, Any]]:
    if not isinstance(value, list) or not value:
        raise SelectedRunError("invalid-request", "requested_runs must be a non-empty ordered list")
    normalized: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in value:
        if not isinstance(item, Mapping) or set(item) - {"requested_run_id", "kind", "definition", "parent_requested_run_id", "predecessor_requested_run_id", "successor_requested_run_ids"}:
            raise SelectedRunError("invalid-request", "requested run has unsupported fields")
        requested_id = _require_string(item, "requested_run_id")
        if requested_id in seen:
            raise SelectedRunError("invalid-request", "requested run IDs must be distinct")
        if item.get("kind") not in RUN_KINDS:
            raise SelectedRunError("invalid-request", "requested run kind is invalid")
        record = {"requested_run_id": requested_id, "kind": item["kind"], "definition": _definition(item.get("definition"), location="requested run definition")}
        for field in ("parent_requested_run_id", "predecessor_requested_run_id"):
            if field in item:
                record[field] = _require_string(item, field)
        if "successor_requested_run_ids" in item:
            successors = item["successor_requested_run_ids"]
            if not isinstance(successors, list) or any(not isinstance(value, str) or not value for value in successors) or len(set(successors)) != len(successors):
                raise SelectedRunError("invalid-request", "successor_requested_run_ids must be unique non-empty strings")
            record["successor_requested_run_ids"] = list(successors)
        normalized.append(record)
        seen.add(requested_id)
    for record in normalized:
        if record.get("parent_requested_run_id") == record["requested_run_id"]:
            raise SelectedRunError("invalid-request", "a requested run cannot parent itself")
    return normalized


def _common_bytes(request: Mapping[str, Any]) -> bytes:
    # Requested Run identities are execute-only. A valid preview can omit them
    # while its later execute supplies them without changing the preview seal.
    fields = {key: request[key] for key in _COMMON_FIELDS - {"mode", "requested_runs"} if key in request}
    return work_journal.canonical_json_bytes(fields)


def _proposal(request: Mapping[str, Any], observation: Mapping[str, Any]) -> dict[str, Any]:
    receipt = {
        "request_id": request["request_id"],
        "operation_route": request["operation_route"],
        "initiative_ref": request["initiative"].get("initiative_ref"),
        "source_freshness": {
            "declared": request["source_freshness"],
            "observed": observation.get("observed", {}),
            "selected": observation.get("selected"),
            "current": observation.get("current"),
        },
        "parameters_digest": request["parameters_digest"],
        "target_frontier_digest": request["target_frontier_digest"],
        "effects_digest": request["effects_digest"],
        "definition_manifest": request["definition_manifest"],
    }
    return receipt


class RunTracker:
    """Shared selected-run service with injected currentness and route effects.

    ``source_observer`` returns ``selected`` and ``current`` booleans plus a
    safe ``observed`` comparison. ``executor`` is invoked only after an exact
    execute admission and receives generated actual Runs.
    """

    def __init__(
        self,
        root: Path,
        *,
        source_observer: Callable[[dict[str, Any]], Mapping[str, Any]],
        executor: Callable[[dict[str, Any], list[dict[str, Any]]], Mapping[str, Any]],
        journal_context: Mapping[str, str] | None = None,
    ) -> None:
        self.root = Path(root)
        self.source_observer = source_observer
        self.executor = executor
        self.journal_context = dict(journal_context or {"author": "run-support", "timezone": "UTC"})
        self._requests: dict[str, bytes] = {}

    def run_selected_operation(self, request: Mapping[str, Any]) -> dict[str, Any]:
        parsed = _validate_common(request)
        fingerprint = _common_bytes(parsed)
        request_id = parsed["request_id"]
        recorded = self._requests.get(request_id)
        if recorded is not None and recorded != fingerprint:
            raise SelectedRunError("request-id-conflict", "request_id was already used with different canonical request bytes")
        self._requests.setdefault(request_id, fingerprint)
        observation = self._observe(parsed)
        proposal = _proposal(parsed, observation)
        proposal_digest = _canonical_digest(proposal)
        if parsed["mode"] == "preview":
            return {
                "request_id": request_id,
                "disposition": "preview" if observation["selected"] and observation["current"] else "blocked",
                "proposal_receipt": proposal,
                "proposal_receipt_digest": proposal_digest,
                "source_freshness": proposal["source_freshness"],
                "retry_disposition": "not-applicable",
            }
        if not observation["selected"] or not observation["current"]:
            return self._nonstart(parsed, observation, "blocked", "revalidation-required")
        self._validate_execute(parsed, proposal, proposal_digest)
        actual_runs = self._actual_runs(parsed["requested_runs"])
        try:
            start_receipts = self._append_events(parsed, actual_runs, "started", None, None, [], None)
        except OSError as error:
            return self._recording_pending(parsed, actual_runs, None, [], f"start evidence append failed: {error}")
        execution = self.executor(parsed, actual_runs)
        terminal = self._validate_execution(execution, actual_runs)
        event_name = {"completed": "completed", "no_op": "completed", "failed": "failed", "partial": "failed", "cancelled": "abandoned", "interrupted_pending": "interrupted"}[terminal["outcome"]]
        try:
            terminal_receipts = self._append_events(
                parsed, actual_runs, event_name, terminal["outcome"], terminal["result_ref"], terminal["effect_refs"], terminal.get("report_ref")
            )
        except OSError as error:
            return self._recording_pending(parsed, actual_runs, terminal["outcome"], terminal["effect_refs"], f"terminal evidence append failed: {error}", terminal.get("result_ref"))
        disposition = "terminal" if terminal["outcome"] != "interrupted_pending" else "started"
        return {
            "request_id": request_id,
            "disposition": disposition,
            "source_freshness": proposal["source_freshness"],
            "retry_disposition": "none",
            "run_ids": [run["run_id"] for run in actual_runs],
            "definition_bindings": [run["definition"] | {"kind": run["kind"]} for run in actual_runs],
            "outcome": terminal["outcome"],
            "result_ref": terminal["result_ref"],
            "effect_refs": terminal["effect_refs"],
            "report_ref": terminal.get("report_ref"),
            "event_receipts": [*start_receipts, *terminal_receipts],
        }

    def recover_recording(self, event_id: str) -> dict[str, Any]:
        """Retry only the stored Journal bytes; this never invokes ``executor``."""
        return work_journal.recover_pending_event(self.root, event_id)

    def _observe(self, request: dict[str, Any]) -> dict[str, Any]:
        observed = self.source_observer(request)
        if not isinstance(observed, Mapping) or type(observed.get("selected")) is not bool or type(observed.get("current")) is not bool:
            raise SelectedRunError("invalid-currentness", "source observer must return selected/current booleans")
        comparison = observed.get("observed", {})
        if not isinstance(comparison, Mapping):
            raise SelectedRunError("invalid-currentness", "source observer observed comparison must be an object")
        _reject_secrets(comparison, "source observer observed")
        return {"selected": observed["selected"], "current": observed["current"], "observed": dict(comparison)}

    def _validate_execute(self, request: dict[str, Any], proposal: dict[str, Any], proposal_digest: str) -> None:
        receipt = request["proposal_receipt"]
        if not isinstance(receipt, Mapping) or dict(receipt) != proposal:
            raise SelectedRunError("stale-preview", "proposal_receipt does not match current declared sources")
        if request["proposal_receipt_digest"] != proposal_digest:
            raise SelectedRunError("stale-preview", "proposal_receipt_digest does not match proposal_receipt")
        _require_string(request, "assigned_action_id")
        auth = request["operator_authorization"]
        required = {"authorization_ref", "authorization_freshness", "request_id", "operation_route", "proposal_receipt_digest", "parameters_digest", "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness"}
        if not isinstance(auth, Mapping) or set(auth) != required:
            raise SelectedRunError("invalid-authorization", "operator_authorization has missing or unsupported fields")
        _safe_ref(auth["authorization_ref"], "authorization_ref")
        freshness = auth["authorization_freshness"]
        if not isinstance(freshness, Mapping) or set(freshness) != {"state", "digest"} or freshness.get("state") != "current":
            raise SelectedRunError("stale-authorization", "operator authorization freshness is not current")
        _require_digest(freshness.get("digest"), "authorization_freshness.digest")
        for key in ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest", "target_frontier_digest", "effects_digest"):
            if auth[key] != request[key]:
                raise SelectedRunError("invalid-authorization", f"operator authorization does not bind {key}")
        if dict(auth["definition_manifest"]) != request["definition_manifest"] or dict(auth["source_freshness"]) != request["source_freshness"]:
            raise SelectedRunError("invalid-authorization", "operator authorization does not bind manifest/currentness")

    def _nonstart(self, request: Mapping[str, Any], observation: Mapping[str, Any], disposition: str, retry: str) -> dict[str, Any]:
        return {
            "request_id": request["request_id"],
            "disposition": disposition,
            "source_freshness": _proposal(request, observation)["source_freshness"],
            "retry_disposition": retry,
        }

    def _actual_runs(self, requested: list[dict[str, Any]]) -> list[dict[str, Any]]:
        identifiers = {item["requested_run_id"]: f"run-{uuid.uuid4()}" for item in requested}
        actual: list[dict[str, Any]] = []
        for item in requested:
            record = {"run_id": identifiers[item["requested_run_id"]], "kind": item["kind"], "definition": item["definition"]}
            if "parent_requested_run_id" in item:
                parent = item["parent_requested_run_id"]
                if parent not in identifiers:
                    raise SelectedRunError("invalid-request", "requested run parent is not in the requested run set")
                record["parent_run_id"] = identifiers[parent]
            if "predecessor_requested_run_id" in item:
                predecessor = item["predecessor_requested_run_id"]
                if predecessor not in identifiers:
                    raise SelectedRunError("invalid-request", "requested run predecessor is not in the requested run set")
                record["predecessor_run_id"] = identifiers[predecessor]
            if "successor_requested_run_ids" in item:
                if any(successor not in identifiers for successor in item["successor_requested_run_ids"]):
                    raise SelectedRunError("invalid-request", "requested run successor is not in the requested run set")
                record["successor_run_ids"] = [identifiers[successor] for successor in item["successor_requested_run_ids"]]
            actual.append(record)
        return actual

    def _validate_execution(self, value: Mapping[str, Any], actual_runs: list[dict[str, Any]]) -> dict[str, Any]:
        if not isinstance(value, Mapping) or set(value) - {"outcome", "result_ref", "effect_refs", "report_ref", "actual_runs"}:
            raise SelectedRunError("invalid-executor-result", "route executor returned unsupported fields")
        outcome = value.get("outcome")
        if outcome not in OUTCOMES:
            raise SelectedRunError("invalid-executor-result", "route executor outcome is invalid")
        result_ref = value.get("result_ref")
        if outcome != "interrupted_pending":
            result_ref = _safe_ref(result_ref, "executor result_ref")
        elif result_ref is not None:
            result_ref = _safe_ref(result_ref, "executor result_ref")
        effects = value.get("effect_refs")
        if not isinstance(effects, list) or any(_safe_ref(effect, "executor effect_ref") != effect for effect in effects) or len(set(effects)) != len(effects):
            raise SelectedRunError("invalid-executor-result", "effect_refs must be unique safe references")
        if outcome == "no_op" and effects:
            raise SelectedRunError("invalid-executor-result", "no_op must not invent an effect reference")
        report = value.get("report_ref")
        if report is not None:
            report = _safe_ref(report, "executor report_ref")
        supplied_runs = value.get("actual_runs")
        if supplied_runs != actual_runs:
            raise SelectedRunError("invalid-executor-result", "route executor must retain generated actual Run provenance")
        return {"outcome": outcome, "result_ref": result_ref, "effect_refs": list(effects), **({"report_ref": report} if report else {})}

    def _append_events(self, request: Mapping[str, Any], runs: list[dict[str, Any]], event: str, outcome: str | None, result_ref: str | None, effect_refs: list[str], report_ref: str | None) -> list[dict[str, Any]]:
        receipts: list[dict[str, Any]] = []
        for run in runs:
            journal_event = self._journal_event(request, run, event, outcome, result_ref, effect_refs, report_ref)
            context = self._context(journal_event)
            try:
                receipts.extend(work_journal.append_sealed_events(self.root, [journal_event], append_context=context, **self._partition_kwargs(context)))
            except OSError:
                work_journal.store_pending_event(self.root, journal_event, context, result_ref=result_ref, effect_refs=effect_refs, diagnostic="append failure")
                raise
        return receipts

    def _recording_pending(self, request: Mapping[str, Any], runs: list[dict[str, Any]], outcome: str | None, effects: list[str], diagnostic: str, result_ref: str | None = None) -> dict[str, Any]:
        return {
            "request_id": request["request_id"],
            "disposition": "recording_pending",
            "source_freshness": {"declared": request["source_freshness"]},
            "retry_disposition": "retry-recording-only",
            "run_ids": [run["run_id"] for run in runs],
            "outcome": outcome,
            "result_ref": result_ref,
            "effect_refs": effects,
            "recording_blocker": diagnostic,
        }

    def _context(self, event: Mapping[str, Any]) -> dict[str, Any]:
        author = self.journal_context.get("author", "run-support")
        timezone = self.journal_context.get("timezone", "UTC")
        occurred = dt.datetime.fromisoformat(str(event["occurred_at"]))
        local_date = occurred.date().isoformat()
        return work_journal.seal_append_context(self.root, event, author=author, local_date=local_date, timezone=timezone)

    @staticmethod
    def _partition_kwargs(context: Mapping[str, Any]) -> dict[str, str]:
        return {"author": str(context["author"]), "local_date": str(context["local_date"]), "timezone": str(context["timezone"])}

    def _journal_event(self, request: Mapping[str, Any], run: Mapping[str, Any], event: str, outcome: str | None, result_ref: str | None, effect_refs: list[str], report_ref: str | None) -> dict[str, Any]:
        author = self.journal_context.get("author", "run-support")
        timezone = self.journal_context.get("timezone", "UTC")
        now = dt.datetime.now(dt.UTC).astimezone(dt.timezone.utc if timezone == "UTC" else dt.timezone.utc).isoformat(timespec="seconds")
        payload: dict[str, Any] = {
            "schema_version": 5,
            "kind": "workflow_execution",
            "event_id": f"event-{uuid.uuid4()}",
            "action_id": request["assigned_action_id"],
            "event": event,
            "author": author,
            "occurred_at": now,
            "llm_session": {"app": "run-support", "uuid": request["request_id"]},
            "structural_scope": "TOOLS",
            "initiative": request["initiative"],
            "run": dict(run),
            "definition_bindings": [{"kind": item["kind"], **item["definition"]} for item in [run]],
            "input_ref": request["initiative"].get("initiative_ref", "selected-run-input"),
            "outcome": outcome,
            "result_ref": result_ref,
            "effect_refs": list(effect_refs),
            "report_ref": report_ref,
            "redaction": {"redacted": False, "fields": []},
        }
        return work_journal.with_event_digest(payload)


class RunExecutionSession:
    """Lazy, injected lifecycle recorder for one already-admitted execution.

    Route executors call ``start_run`` only when a node is actually invoked,
    then ``finish_run`` only for that invoked Run.  It deliberately never
    follows requested successor edges or executes an effect itself.
    """

    def __init__(self, tracker: "LazyRunTracker", request: dict[str, Any]) -> None:
        self.tracker = tracker
        self.request = request
        self.requested = {item["requested_run_id"]: item for item in request["requested_runs"]}
        self.actual: dict[str, dict[str, Any]] = {}
        self.terminal: dict[str, dict[str, Any]] = {}
        self.observed_effects: dict[str, dict[str, Any]] = {}
        self.receipts: list[dict[str, Any]] = []
        self.pending: list[str] = []

    def start_run(self, requested_run_id: str, *, run_id: str | None = None) -> dict[str, Any]:
        """Record one actual invocation, preserving a requested Workflow ID."""
        if requested_run_id not in self.requested:
            raise SelectedRunError("invalid-run", "route attempted to start an unrequested Run")
        existing = self.actual.get(requested_run_id)
        if existing is not None:
            return dict(existing)
        requested = self.requested[requested_run_id]
        actual_id = run_id or requested_run_id
        if not isinstance(actual_id, str) or not actual_id:
            raise SelectedRunError("invalid-run", "actual run_id must be non-empty")
        if any(item["run_id"] == actual_id for item in self.actual.values()):
            raise SelectedRunError("invalid-run", "actual run_id must remain distinct")
        record: dict[str, Any] = {"run_id": actual_id, "kind": requested["kind"], "definition": requested["definition"]}
        if "parent_requested_run_id" in requested:
            parent = self.actual.get(requested["parent_requested_run_id"])
            if parent is None:
                raise SelectedRunError("invalid-run", "an actual child Run requires its actual parent first")
            record["parent_run_id"] = parent["run_id"]
        if "predecessor_requested_run_id" in requested:
            predecessor = self.actual.get(requested["predecessor_requested_run_id"])
            if predecessor is None:
                raise SelectedRunError("invalid-run", "an actual successor requires its actual predecessor first")
            record["predecessor_run_id"] = predecessor["run_id"]
        event = self.tracker._lazy_journal_event(self.request, record, "started", None, None, [], None, self._bindings_for(record))
        try:
            self.receipts.append(self.tracker._append_one(event, None, []))
        except OSError as error:
            self.pending.append(str(event["event_id"]))
            raise SelectedRunError("recording-pending", f"Run start evidence could not be durably recorded: {error}") from error
        self.actual[requested_run_id] = record
        return dict(record)

    def finish_run(
        self,
        run_id: str,
        *,
        outcome: str,
        result_ref: str | None,
        effect_refs: list[str],
        report_ref: str | None = None,
    ) -> dict[str, Any]:
        """Record the one truthful terminal fact for an actual Run."""
        requested_id, record = self._actual_by_id(run_id)
        if requested_id in self.terminal:
            raise SelectedRunError("duplicate-terminal", "an actual Run already has terminal evidence")
        observed = self.observed_effects.get(requested_id)
        if observed is not None and (result_ref != observed["result_ref"] or effect_refs != observed["effect_refs"]):
            raise SelectedRunError("effect-observation-mismatch", "terminal evidence must retain previously observed effects")
        if outcome not in OUTCOMES:
            raise SelectedRunError("invalid-outcome", "outcome is invalid")
        if outcome != "interrupted_pending":
            result_ref = _safe_ref(result_ref, "result_ref")
        elif result_ref is not None:
            result_ref = _safe_ref(result_ref, "result_ref")
        if not isinstance(effect_refs, list) or len(set(effect_refs)) != len(effect_refs):
            raise SelectedRunError("invalid-outcome", "effect_refs must be unique")
        for effect_ref in effect_refs:
            _safe_ref(effect_ref, "effect_ref")
        if outcome == "no_op" and effect_refs:
            raise SelectedRunError("invalid-outcome", "no_op cannot invent an effect reference")
        if report_ref is not None:
            report_ref = _safe_ref(report_ref, "report_ref")
        event_name = {"completed": "completed", "no_op": "completed", "failed": "failed", "partial": "failed", "cancelled": "abandoned", "interrupted_pending": "interrupted"}[outcome]
        event = self.tracker._lazy_journal_event(self.request, record, event_name, outcome, result_ref, effect_refs, report_ref, self._bindings_for(record))
        try:
            self.receipts.append(self.tracker._append_one(event, result_ref, effect_refs))
            result = {"run_id": run_id, "disposition": "terminal", "outcome": outcome, "result_ref": result_ref, "effect_refs": list(effect_refs), "report_ref": report_ref}
        except OSError as error:
            self.pending.append(str(event["event_id"]))
            result = {"run_id": run_id, "disposition": "recording_pending", "outcome": outcome, "result_ref": result_ref, "effect_refs": list(effect_refs), "report_ref": report_ref, "recording_blocker": str(error)}
        self.terminal[requested_id] = result
        return dict(result)

    def note_effects(self, run_id: str, *, result_ref: str, effect_refs: list[str]) -> None:
        """Retain known effects so an interrupted executor cannot erase them."""
        requested_id, _ = self._actual_by_id(run_id)
        if requested_id in self.terminal or requested_id in self.observed_effects:
            raise SelectedRunError("invalid-effect-observation", "effects may be observed once before terminal evidence")
        result_ref = _safe_ref(result_ref, "result_ref")
        if not isinstance(effect_refs, list) or not effect_refs or len(set(effect_refs)) != len(effect_refs):
            raise SelectedRunError("invalid-effect-observation", "effect_refs must be a non-empty unique list")
        for effect_ref in effect_refs:
            _safe_ref(effect_ref, "effect_ref")
        self.observed_effects[requested_id] = {"result_ref": result_ref, "effect_refs": list(effect_refs)}

    # Small aliases make the lifecycle injection concise for queue and adapter callers.
    start = start_run
    finish = finish_run
    record_effects = note_effects

    def recover(self, event_id: str) -> dict[str, Any]:
        return self.tracker.recover_recording(event_id)

    def interrupt_open_runs(self) -> None:
        """Retain uncertainty after an executor exception without declaring completion."""
        for requested_id, record in list(self.actual.items()):
            if requested_id not in self.terminal:
                observed = self.observed_effects.get(requested_id)
                if observed is None:
                    self.finish_run(record["run_id"], outcome="interrupted_pending", result_ref=None, effect_refs=[])
                else:
                    self.finish_run(record["run_id"], outcome="partial", **observed)

    def _actual_by_id(self, run_id: str) -> tuple[str, dict[str, Any]]:
        for requested_id, record in self.actual.items():
            if record["run_id"] == run_id:
                return requested_id, record
        raise SelectedRunError("unknown-run", "route attempted to finish a Run that was not actually started")

    def _bindings_for(self, run: Mapping[str, Any]) -> list[dict[str, Any]]:
        if run["kind"] == "workflow":
            bindings = [{"kind": item["kind"], **item["definition"]} for item in self.requested.values()]
        else:
            bindings = [{"kind": run["kind"], **run["definition"]}]
        return sorted(bindings, key=lambda item: (item["kind"], item["atom_id"], item["version"], item["path"]))


class LazyRunTracker(RunTracker):
    """The P1510 tracker: admission is eager; Run creation is deliberately lazy."""

    def run_selected_operation(self, request: Mapping[str, Any]) -> dict[str, Any]:
        parsed = _validate_common(request)
        fingerprint = _common_bytes(parsed)
        request_id = parsed["request_id"]
        recorded = self._requests.get(request_id)
        if recorded is not None and recorded != fingerprint:
            raise SelectedRunError("request-id-conflict", "request_id was already used with different canonical request bytes")
        self._requests.setdefault(request_id, fingerprint)
        observation = self._observe(parsed)
        proposal = _proposal(parsed, observation)
        proposal_digest = _canonical_digest(proposal)
        if parsed["mode"] == "preview":
            return {
                "request_id": request_id,
                "disposition": "preview" if observation["selected"] and observation["current"] else "blocked",
                "proposal_receipt": proposal,
                "proposal_receipt_digest": proposal_digest,
                "source_freshness": proposal["source_freshness"],
                "retry_disposition": "not-applicable",
            }
        if not observation["selected"] or not observation["current"]:
            return self._nonstart(parsed, observation, "blocked", "revalidation-required")
        self._validate_execute(parsed, proposal, proposal_digest)
        try:
            dispatch, created = work_journal.register_selected_run_dispatch(
                self.root,
                request_id=request_id,
                canonical_request_bytes=self._dispatch_bytes(parsed),
            )
        except work_journal.WorkJournalError as error:
            if error.code == "request-id-conflict":
                raise SelectedRunError(error.code, str(error)) from error
            raise
        if not created:
            return {
                "request_id": request_id,
                "disposition": "blocked",
                "source_freshness": proposal["source_freshness"],
                "retry_disposition": "inspect-or-recover-only",
                "dispatch_state": dispatch["state"],
            }
        session = RunExecutionSession(self, parsed)
        try:
            self.executor(parsed, session)
        except Exception as error:
            try:
                session.interrupt_open_runs()
            except OSError:
                pass
            return self._session_result(parsed, proposal, session, execution_error=type(error).__name__)
        if not session.actual:
            return {**self._nonstart(parsed, observation, "declined", "executor-start-required"), "executor_result": "no actual Run was started"}
        session.interrupt_open_runs()
        return self._session_result(parsed, proposal, session)

    def _session_result(self, request: Mapping[str, Any], proposal: Mapping[str, Any], session: RunExecutionSession, *, execution_error: str | None = None) -> dict[str, Any]:
        terminal = list(session.terminal.values())
        if session.pending or any(item["disposition"] == "recording_pending" for item in terminal):
            disposition = "recording_pending"
        elif any(item["outcome"] == "interrupted_pending" for item in terminal):
            disposition = "started"
        else:
            disposition = "terminal"
        result: dict[str, Any] = {
            "request_id": request["request_id"],
            "disposition": disposition,
            "source_freshness": proposal["source_freshness"],
            "retry_disposition": "retry-recording-only" if disposition == "recording_pending" else "none",
            "run_ids": [record["run_id"] for record in session.actual.values()],
            "terminal_runs": terminal,
            "event_receipts": list(session.receipts),
        }
        if session.pending:
            result["pending_event_ids"] = list(session.pending)
        if execution_error is not None:
            result["execution_error"] = execution_error
        return result

    @staticmethod
    def _dispatch_bytes(request: Mapping[str, Any]) -> bytes:
        """Bind the accepted execute request, not only its preview common part."""
        return work_journal.canonical_json_bytes({key: request[key] for key in sorted(request) if key != "mode"})

    def _append_one(self, event: Mapping[str, Any], result_ref: str | None, effect_refs: list[str]) -> dict[str, Any]:
        context = self._context(event)
        try:
            return work_journal.append_sealed_events(self.root, [event], append_context=context, **self._partition_kwargs(context))[0]
        except OSError:
            work_journal.store_pending_event(self.root, event, context, result_ref=result_ref, effect_refs=effect_refs, diagnostic="append failure")
            raise

    def _lazy_journal_event(self, request: Mapping[str, Any], run: Mapping[str, Any], event: str, outcome: str | None, result_ref: str | None, effect_refs: list[str], report_ref: str | None, bindings: list[dict[str, Any]]) -> dict[str, Any]:
        author = self.journal_context.get("author", "run-support")
        timezone = self.journal_context.get("timezone", "UTC")
        try:
            now = dt.datetime.now(dt.UTC if timezone == "UTC" else ZoneInfo(timezone)).isoformat(timespec="seconds")
        except ZoneInfoNotFoundError as error:
            raise SelectedRunError("invalid-journal-context", "journal_context timezone is unknown") from error
        payload: dict[str, Any] = {
            "schema_version": 5,
            "kind": "workflow_execution",
            "event_id": f"event-{uuid.uuid4()}",
            "action_id": request["assigned_action_id"],
            "event": event,
            "author": author,
            "occurred_at": now,
            "llm_session": {"app": "run-support", "uuid": request["request_id"]},
            "structural_scope": "TOOLS",
            "initiative": request["initiative"],
            "run": dict(run),
            "definition_bindings": bindings,
            "input_ref": request["initiative"].get("initiative_ref", "selected-run-input"),
            "outcome": outcome,
            "result_ref": result_ref,
            "effect_refs": list(effect_refs),
            "report_ref": report_ref,
            "redaction": {"redacted": False, "fields": []},
        }
        return work_journal.with_event_digest(payload)


# Keep the public name stable for MCP, queue, and reversal consumers.
RunTracker = LazyRunTracker


def run_selected_operation(request: Mapping[str, Any]) -> dict[str, Any]:
    """Default-safe module entry point: no implicit route is admitted or started."""
    tracker = RunTracker(
        Path.cwd(),
        source_observer=lambda _: {"selected": False, "current": False, "observed": {"reason": "no route service injected"}},
        executor=lambda _request, _runs: (_ for _ in ()).throw(SelectedRunError("no-executor", "no selected route executor was injected")),
    )
    return tracker.run_selected_operation(request)
