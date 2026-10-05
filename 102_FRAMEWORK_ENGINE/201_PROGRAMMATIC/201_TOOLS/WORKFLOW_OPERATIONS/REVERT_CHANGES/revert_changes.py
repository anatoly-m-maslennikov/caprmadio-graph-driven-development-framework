"""Guarded native adapter for CA-O-131 approved change reversals.

This module deliberately orchestrates only an already-approved, exact manifest.
Target mutation and Run/Journal persistence remain injected governed capabilities.
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from collections.abc import Callable, Mapping
from typing import Any


class RevertChangesError(ValueError):
    """Raised for a malformed public request rather than an admitted denial."""


_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_CAPABILITY_BINDING_FIELDS = {
    "capability_id", "parameters", "target", "permission_evidence", "evidence_refs",
}
_CAPABILITY_PERMISSION_FIELDS = {"capability_id", "granted", "evidence_ref", "evidence_hash"}


class RecordingPendingError(OSError):
    """The shared session saved a canonical pending event that must be retried."""

    def __init__(self, pending_event_id: str) -> None:
        self.pending_event_id = pending_event_id
        super().__init__(f"pending Journal event: {pending_event_id}")


def _canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def _manifest_id(request: Mapping[str, Any]) -> str:
    return "reversal-" + hashlib.sha256(_canonical(request).encode()).hexdigest()[:24]


def _effect_account(effects: list[Mapping[str, Any]]) -> dict[str, Any]:
    return {"effects": [dict(effect, status="unattempted") for effect in effects], "applied_effect_count": 0}


class RevertChangesService:
    """Strict request handler usable by CA-O-131 standalone or an O132 Step.

    ``observe`` returns the current hash for a target.  ``apply_effect`` applies
    one already-admitted governed effect.  ``run_tracker`` provides ``start``,
    ``finish`` and ``recover``; it is owned by the shared run support packet.
    """

    _TOP_LEVEL = {
        "admit": {"operation", "reversal_request"},
        "execute": {"operation", "approved_reversal_manifest", "cancel_after_effect_id"},
        "recover_recording": {"operation", "pending_recording_event"},
    }
    _REQUIRED = {
        "selected_change_refs", "targets", "affected_reference_hashes", "governing_definition_hash",
        "operator_decision", "cancellation_boundary", "executor_permission", "durable_evidence_location",
        "ordered_effects", "expected_result", "history_reference_evidence", "current_hashes",
    }

    def __init__(self, observe: Callable[[str], str], apply_effect: Callable[[dict[str, Any]], Mapping[str, Any]], run_tracker: Any,
                 revalidate: Callable[[Mapping[str, Any]], list[str]] | None = None,
                 capability_validator: Callable[[Mapping[str, Any]], list[str]] | None = None):
        self.observe = observe
        self.apply_effect = apply_effect
        self.run_tracker = run_tracker
        self.revalidate = revalidate or (lambda _request: [])
        self.capability_validator = capability_validator or (lambda _request: [])

    def handle(self, request: Mapping[str, Any]) -> dict[str, Any]:
        if not isinstance(request, Mapping):
            raise RevertChangesError("request must be an object")
        operation = request.get("operation")
        if operation not in self._TOP_LEVEL:
            raise RevertChangesError("operation must be admit, execute, or recover_recording")
        unknown = set(request) - self._TOP_LEVEL[operation]
        if unknown:
            raise RevertChangesError(f"unknown or mixed-mode fields: {sorted(unknown)}")
        if operation == "admit":
            return self.admit(request.get("reversal_request"))
        if operation == "execute":
            return self.execute(request.get("approved_reversal_manifest"), request.get("cancel_after_effect_id"))
        return self.recover_recording(request.get("pending_recording_event"))

    def admit(self, reversal_request: Any) -> dict[str, Any]:
        if not isinstance(reversal_request, Mapping):
            return self._blocked(["reversal_request"])
        missing = sorted(self._REQUIRED - set(reversal_request))
        if missing:
            return self._blocked(missing)
        request = dict(reversal_request)
        bindings = self._validate_request(request)
        if bindings:
            return self._blocked(bindings)
        try:
            admitted_target_hashes = {target: self.observe(target) for target in request["targets"]}
        except Exception as exc:
            return self._blocked([f"currentness_unresolved:{exc}"])
        stale_targets = [f"current_hash:{target}" for target, observed in admitted_target_hashes.items()
                         if observed != request["current_hashes"].get(target)]
        if stale_targets:
            return self._blocked(stale_targets)
        manifest = {
            "manifest_id": _manifest_id(request), "request": request,
            "admitted_target_hashes": admitted_target_hashes,
            "admitted_at": int(time.time()),
        }
        return {"outcome": "admitted", "manifest_id": manifest["manifest_id"], "approved_reversal_manifest": manifest,
                "evidence_refs": list(request["history_reference_evidence"]), "run_receipt_refs": []}

    def execute(self, manifest: Any, cancel_after_effect_id: Any = None) -> dict[str, Any]:
        if not isinstance(manifest, Mapping) or not isinstance(manifest.get("request"), Mapping):
            return self._blocked(["approved_reversal_manifest"])
        request = dict(manifest["request"])
        manifest_id = manifest.get("manifest_id")
        if manifest_id != _manifest_id(request):
            return self._blocked(["manifest_id"])
        bindings = self._validate_request(request) + self._currentness_mismatches(request, manifest) + self._external_mismatches(request)
        if bindings:
            return self._blocked(bindings, manifest_id)
        effects = request["ordered_effects"]
        account = _effect_account(effects)
        if cancel_after_effect_id is not None and cancel_after_effect_id not in request["cancellation_boundary"].get("after_effect_ids", []):
            return self._blocked(["cancellation_boundary"], manifest_id)
        if self._already_satisfied(effects):
            return self._run_terminal("no_op", manifest_id, request, account)
        event_id = f"{manifest_id}:action"
        start_payload = {"event_id": event_id, "phase": "Started", "action_id": "CA-O-131", "manifest_id": manifest_id}
        try:
            start_receipt = self.run_tracker.start(start_payload)
        except Exception as exc:  # Target effects must not start without confirmed start evidence.
            return self._recording_blocked(manifest_id, request, account, event_id, "start", exc)
        for index, effect in enumerate(effects):
            external = self._external_mismatches(request)
            if external:
                return self._terminal("blocked", manifest_id, request, account, start_receipt, external)
            current = self.observe(effect["target_id"])
            if current != effect["expected_current_hash"]:
                return self._terminal("blocked", manifest_id, request, account, start_receipt, [f"current_hash:{effect['effect_id']}"])
            try:
                receipt = self.apply_effect(dict(effect))
            except TimeoutError as exc:
                account["effects"][index]["status"] = "uncertain"
                account["effects"][index]["error"] = str(exc)
                return self._terminal("partial_failure", manifest_id, request, account, start_receipt)
            except Exception as exc:
                account["effects"][index]["status"] = "failed"
                account["effects"][index]["error"] = str(exc)
                outcome = "failed" if account["applied_effect_count"] == 0 else "partial_failure"
                return self._terminal(outcome, manifest_id, request, account, start_receipt)
            try:
                observed_result_hash = self.observe(effect["target_id"])
            except Exception as exc:
                account["effects"][index]["status"] = "uncertain"
                account["effects"][index]["error"] = f"completed capability result observation unresolved: {exc}"
                account["effects"][index]["receipt"] = dict(receipt)
                return self._terminal("partial_failure", manifest_id, request, account, start_receipt)
            if observed_result_hash != effect["expected_result_hash"]:
                account["effects"][index]["status"] = "uncertain"
                account["effects"][index]["error"] = "completed capability did not establish expected_result_hash"
                account["effects"][index]["receipt"] = dict(receipt)
                return self._terminal("partial_failure", manifest_id, request, account, start_receipt)
            account["effects"][index]["status"] = "completed"
            account["effects"][index]["receipt"] = dict(receipt)
            account["applied_effect_count"] += 1
            if cancel_after_effect_id == effect["effect_id"]:
                if effect["effect_id"] not in request["cancellation_boundary"].get("after_effect_ids", []):
                    return self._terminal("blocked", manifest_id, request, account, start_receipt, ["cancellation_boundary"])
                return self._terminal("canceled", manifest_id, request, account, start_receipt)
        return self._terminal("reverted", manifest_id, request, account, start_receipt)

    def execute_with_session(self, manifest: Mapping[str, Any], session: Any, requested_action_run_id: str,
                             cancel_after_effect_id: Any = None) -> dict[str, Any]:
        """Execute CA-O-131 through one pre-admitted shared selected-run session.

        The graph executor supplies its generated Action requested-run ID.  This
        method starts and finishes only that Action; it never creates a parent
        Workflow/Step Run or interprets continuation edges.
        """
        original = self.run_tracker
        self.run_tracker = _SessionTracker(session, requested_action_run_id)
        try:
            return self.execute(manifest, cancel_after_effect_id)
        finally:
            self.run_tracker = original

    def recover_recording_with_session(self, pending_event: Mapping[str, Any], session: Any) -> dict[str, Any]:
        """Reconcile only a canonical pending Journal event; never rerun effects."""
        original = self.run_tracker
        self.run_tracker = _SessionTracker(session, "unused-for-recording-recovery")
        try:
            return self.recover_recording(pending_event)
        finally:
            self.run_tracker = original

    def recover_recording(self, event: Any) -> dict[str, Any]:
        if not isinstance(event, Mapping) or not isinstance(event.get("event_id"), str) or not isinstance(event.get("result"), Mapping):
            return self._blocked(["pending_recording_event"])
        try:
            receipt = self.run_tracker.recover(dict(event))
        except Exception as exc:
            result = dict(event["result"])
            result.update({"outcome": "recording_blocked", "pending_recording_event": dict(event), "recording_error": str(exc)})
            return result
        result = dict(event["result"])
        result["run_receipt_refs"] = [dict(receipt)]
        return result

    def _validate_request(self, request: Mapping[str, Any]) -> list[str]:
        errors: list[str] = []
        effects = request.get("ordered_effects")
        decision = request.get("operator_decision")
        permission = request.get("executor_permission")
        if not isinstance(effects, list) or not effects:
            errors.append("ordered_effects")
            return errors
        ids = [effect.get("effect_id") for effect in effects if isinstance(effect, Mapping)]
        if len(ids) != len(effects) or len(set(ids)) != len(ids): errors.append("effect_ids")
        if not isinstance(decision, Mapping) or decision.get("status") != "approved": errors.append("operator_decision")
        elif decision.get("approved_effect_ids") != ids: errors.append("effect_order")
        if not isinstance(permission, Mapping) or permission.get("granted") is not True: errors.append("executor_permission")
        for effect in effects:
            required_effect = {
                "effect_id", "target_id", "expected_current_hash", "expected_result_hash", "expected_before",
                "expected_after", "before_evidence", "after_evidence", "capability_binding",
            }
            if not isinstance(effect, Mapping) or not required_effect <= set(effect):
                errors.append("effect_binding")
                continue
            effect_id = effect.get("effect_id")
            if not isinstance(effect_id, str) or not effect_id:
                errors.append("effect_id")
                continue
            if not isinstance(effect.get("target_id"), str) or not effect["target_id"]:
                errors.append(f"target:{effect_id}")
            if not all(isinstance(effect.get(field), str) and effect[field] for field in ("expected_before", "expected_after", "before_evidence", "after_evidence")):
                errors.append(f"effect_evidence:{effect_id}")
            if not all(isinstance(effect.get(field), str) and _SHA256.fullmatch(effect[field]) for field in ("expected_current_hash", "expected_result_hash")):
                errors.append(f"effect_hash:{effect_id}")
            errors.extend(self._capability_binding_errors(effect))
            if effect["target_id"] not in request.get("targets", []): errors.append(f"target:{effect['effect_id']}")
            supplied_current = request.get("current_hashes", {}).get(effect["target_id"])
            if supplied_current not in {effect["expected_current_hash"], effect["expected_result_hash"]}:
                errors.append(f"current_hash:{effect['effect_id']}")
        if not request.get("selected_change_refs"): errors.append("selected_change_refs")
        if not request.get("history_reference_evidence"): errors.append("history_reference_evidence")
        try:
            capability_errors = self.capability_validator(request)
        except Exception as exc:
            errors.append(f"capability_validation_unresolved:{exc}")
        else:
            if not isinstance(capability_errors, list) or not all(isinstance(item, str) for item in capability_errors):
                errors.append("capability_validation_result")
            else:
                errors.extend(capability_errors)
        return errors

    @staticmethod
    def _capability_binding_errors(effect: Mapping[str, Any]) -> list[str]:
        effect_id = str(effect.get("effect_id", "unknown"))
        binding = effect.get("capability_binding")
        if not isinstance(binding, Mapping) or set(binding) != _CAPABILITY_BINDING_FIELDS:
            return [f"capability_binding:{effect_id}"]
        capability_id = binding.get("capability_id")
        if not isinstance(capability_id, str) or not capability_id:
            return [f"capability_id:{effect_id}"]
        if not isinstance(binding.get("parameters"), Mapping) or not isinstance(binding.get("target"), Mapping):
            return [f"capability_packet:{effect_id}"]
        permission = binding.get("permission_evidence")
        if not isinstance(permission, Mapping) or set(permission) != _CAPABILITY_PERMISSION_FIELDS:
            return [f"capability_permission:{effect_id}"]
        if permission.get("capability_id") != capability_id or permission.get("granted") is not True:
            return [f"capability_permission:{effect_id}"]
        if not isinstance(permission.get("evidence_ref"), str) or not permission["evidence_ref"]:
            return [f"capability_permission:{effect_id}"]
        evidence_hash = permission.get("evidence_hash")
        if not isinstance(evidence_hash, str) or not _SHA256.fullmatch(evidence_hash):
            return [f"capability_permission:{effect_id}"]
        evidence_refs = binding.get("evidence_refs")
        if not isinstance(evidence_refs, list) or not evidence_refs or any(not isinstance(item, str) or not item for item in evidence_refs):
            return [f"capability_evidence:{effect_id}"]
        if effect["before_evidence"] not in evidence_refs or effect["after_evidence"] not in evidence_refs:
            return [f"capability_evidence:{effect_id}"]
        return []

    def _currentness_mismatches(self, request: Mapping[str, Any], manifest: Mapping[str, Any]) -> list[str]:
        observed = manifest.get("admitted_target_hashes", {})
        mismatches = []
        for target in request["targets"]:
            if self.observe(target) != observed.get(target) or self.observe(target) != request["current_hashes"].get(target):
                mismatches.append(f"current_hash:{target}")
        return mismatches

    def _external_mismatches(self, request: Mapping[str, Any]) -> list[str]:
        """Ask the governed boundary to recheck references, authority and permission.

        The adapter does not invent those observations; the caller provides the
        current capability-specific checks and their exact binding names.
        """
        try:
            mismatches = self.revalidate(request)
        except Exception as exc:
            return [f"revalidation_unresolved:{exc}"]
        return list(mismatches) if isinstance(mismatches, list) and all(isinstance(item, str) for item in mismatches) else ["revalidation_result"]

    def _already_satisfied(self, effects: list[Mapping[str, Any]]) -> bool:
        return all(self.observe(effect["target_id"]) == effect["expected_result_hash"] for effect in effects)

    def _blocked(self, bindings: list[str], manifest_id: Any = None) -> dict[str, Any]:
        return {"outcome": "blocked", "manifest": None, "manifest_id": manifest_id,
                "missing_or_mismatched_bindings": sorted(set(bindings)), "effect_account": {"effects": [], "applied_effect_count": 0},
                "evidence_refs": [], "run_receipt_refs": []}

    def _run_terminal(self, outcome: str, manifest_id: str, request: Mapping[str, Any], account: dict[str, Any]) -> dict[str, Any]:
        event_id = f"{manifest_id}:action"
        try:
            start = self.run_tracker.start({"event_id": event_id, "phase": "Started", "action_id": "CA-O-131", "manifest_id": manifest_id})
        except Exception as exc:
            return self._recording_blocked(manifest_id, request, account, event_id, "start", exc)
        return self._terminal(outcome, manifest_id, request, account, start)

    def _terminal(self, outcome: str, manifest_id: str, request: Mapping[str, Any], account: dict[str, Any], start_receipt: Mapping[str, Any], bindings: list[str] | None = None) -> dict[str, Any]:
        result = {"outcome": outcome, "manifest_id": manifest_id, "selection_and_currentness_bindings": request["current_hashes"],
                  "expected_result": request["expected_result"], "observed_result": {"outcome": outcome}, "effect_account": account,
                  "history_reference_disposition": "preserved", "evidence_refs": list(request["history_reference_evidence"]),
                  "run_receipt_refs": [dict(start_receipt)]}
        if bindings:
            result["missing_or_mismatched_bindings"] = bindings
        event_type = {"reverted": "Completed", "no_op": "Completed", "failed": "Failed", "partial_failure": "Failed", "blocked": "Interrupted", "canceled": "Abandoned"}[outcome]
        event = {"event_id": f"{manifest_id}:terminal", "phase": event_type, "result": result}
        try:
            receipt = self.run_tracker.finish(event)
        except Exception as exc:
            return self._recording_blocked(manifest_id, request, account, getattr(exc, "pending_event_id", event["event_id"]), "terminal", exc, result)
        result["run_receipt_refs"].append(dict(receipt))
        return result

    def _recording_blocked(self, manifest_id: str, request: Mapping[str, Any], account: dict[str, Any], event_id: str, phase: str, error: Exception, known: dict[str, Any] | None = None) -> dict[str, Any]:
        result = known or {"manifest_id": manifest_id, "effect_account": account, "evidence_refs": list(request["history_reference_evidence"]), "run_receipt_refs": []}
        result.update({"outcome": "recording_blocked", "recording_error": str(error), "pending_recording_event": {"event_id": event_id, "phase": phase, "result": dict(result)}})
        return result


def apply_approved_reversal(request: Mapping[str, Any], *, observe: Callable[[str], str], apply_effect: Callable[[dict[str, Any]], Mapping[str, Any]], run_tracker: Any,
                            revalidate: Callable[[Mapping[str, Any]], list[str]] | None = None) -> dict[str, Any]:
    """Standalone CA-O-131 entrypoint; caller supplies actual lineage to tracker."""
    return RevertChangesService(observe, apply_effect, run_tracker, revalidate).handle(request)


class _SessionTracker:
    """Translate the adapter's small evidence protocol to P1510's session API."""
    _OUTCOMES = {"reverted": "completed", "no_op": "no_op", "failed": "failed", "partial_failure": "partial", "blocked": "interrupted_pending", "canceled": "cancelled"}

    def __init__(self, session: Any, requested_action_run_id: str) -> None:
        self.session = session
        self.requested_action_run_id = requested_action_run_id
        self.actual: Mapping[str, Any] | None = None

    def start(self, _payload: Mapping[str, Any]) -> dict[str, Any]:
        self.actual = self.session.start_run(self.requested_action_run_id)
        return {"run_id": self.actual["run_id"], "durable": True}

    def finish(self, event: Mapping[str, Any]) -> dict[str, Any]:
        if self.actual is None:
            raise RevertChangesError("shared Action Run was not started")
        result = event.get("result", {})
        account = result.get("effect_account", {}) if isinstance(result, Mapping) else {}
        effects = account.get("effects", []) if isinstance(account, Mapping) else []
        effect_refs = [f".caprmedio_runtime/revert_changes/{event['event_id']}/{item['effect_id']}" for item in effects if item.get("status") == "completed"]
        finished = self.session.finish_run(
            self.actual["run_id"], outcome=self._OUTCOMES[result["outcome"]],
            result_ref=f".caprmedio_runtime/revert_changes/{event['event_id']}.json", effect_refs=effect_refs,
        )
        if finished.get("disposition") == "recording_pending":
            pending = getattr(self.session, "pending", [])
            if pending:
                raise RecordingPendingError(str(pending[-1]))
            raise OSError("shared terminal recording is pending")
        return {"run_id": self.actual["run_id"], "durable": finished.get("disposition") == "terminal", **dict(finished)}

    def recover(self, event: Mapping[str, Any]) -> dict[str, Any]:
        return self.session.recover(str(event["event_id"]))
