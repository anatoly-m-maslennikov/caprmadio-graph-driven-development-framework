"""Functional contract tests for the bounded REVERT_CHANGES adapter."""
from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE))
from revert_changes import RevertChangesService  # noqa: E402

TOOLS = PACKAGE.parents[1]
sys.path.insert(0, str(TOOLS))
from work_journal import canonical_json_digest  # noqa: E402
from workflow_run_support import RunTracker  # noqa: E402
import workflow_run_support  # noqa: E402


def digest(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


class MemoryEffects:
    def __init__(self, fail_at: str | None = None, uncertain_at: str | None = None):
        self.values = {"one": "after-one", "two": "after-two"}
        self.calls: list[str] = []
        self.fail_at = fail_at
        self.uncertain_at = uncertain_at

    def observe(self, identity: str) -> str:
        return digest(self.values[identity])

    def apply(self, effect: dict) -> dict:
        effect_id = effect["effect_id"]
        self.calls.append(effect_id)
        if effect_id == self.uncertain_at:
            raise TimeoutError("completion unknown")
        if effect_id == self.fail_at:
            raise RuntimeError("adapter failed")
        self.values[effect["target_id"]] = effect["expected_after"]
        return {"before": effect["expected_before"], "after": effect["expected_after"]}


class FileEffects(MemoryEffects):
    """A governed-effect stand-in that performs a real temporary file mutation."""
    def __init__(self, root: Path):
        super().__init__()
        self.root = root
        for target, value in self.values.items():
            (root / target).write_text(value, encoding="utf-8")

    def observe(self, identity: str) -> str:
        return digest((self.root / identity).read_text(encoding="utf-8"))

    def apply(self, effect: dict) -> dict:
        effect_id = effect["effect_id"]
        self.calls.append(effect_id)
        if effect_id == self.uncertain_at:
            raise TimeoutError("completion unknown")
        if effect_id == self.fail_at:
            raise RuntimeError("adapter failed")
        (self.root / effect["target_id"]).write_text(effect["expected_after"], encoding="utf-8")
        return {"before": effect["expected_before"], "after": effect["expected_after"]}


class FakeRuns:
    def __init__(self, fail_start: bool = False, fail_finish: bool = False):
        self.fail_start, self.fail_finish = fail_start, fail_finish
        self.starts: list[dict] = []
        self.finishes: list[dict] = []

    def start(self, payload: dict) -> dict:
        self.starts.append(payload)
        if self.fail_start:
            raise OSError("journal unavailable")
        return {"event_id": payload["event_id"], "durable": True}

    def finish(self, payload: dict) -> dict:
        self.finishes.append(payload)
        if self.fail_finish:
            raise OSError("journal unavailable")
        return {"event_id": payload["event_id"], "durable": True}

    def recover(self, event: dict) -> dict:
        return {"event_id": event["event_id"], "durable": True}


def complete_request(effects: MemoryEffects) -> dict:
    ordered = [
        {"effect_id": "first", "target_id": "one", "expected_before": "after-one", "expected_after": "before-one"},
        {"effect_id": "second", "target_id": "two", "expected_before": "after-two", "expected_after": "before-two"},
    ]
    for effect in ordered:
        effect["expected_current_hash"] = digest(effect["expected_before"])
        effect["expected_result_hash"] = digest(effect["expected_after"])
        effect["before_evidence"] = f"before:{effect['effect_id']}"
        effect["after_evidence"] = f"after:{effect['effect_id']}"
        effect["capability_binding"] = {
            "capability_id": "test.memory",
            "parameters": {"effect_id": effect["effect_id"]},
            "target": {"target_id": effect["target_id"]},
            "permission_evidence": {
                "capability_id": "test.memory", "granted": True,
                "evidence_ref": f"permission:{effect['effect_id']}", "evidence_hash": "a" * 64,
            },
            "evidence_refs": [effect["before_evidence"], effect["after_evidence"]],
        }
    return {
        "selected_change_refs": ["event:accepted-1", "revision:7"],
        "targets": ["one", "two"],
        "affected_reference_hashes": {"ref:one": "r1", "ref:two": "r2"},
        "governing_definition_hash": "govern-v1",
        "operator_decision": {"decision_id": "approved-1", "approved_effect_ids": ["first", "second"], "status": "approved"},
        "cancellation_boundary": {"after_effect_ids": ["first"]},
        "executor_permission": {"capability": "governed-reversal", "granted": True},
        "durable_evidence_location": "journal://test",
        "ordered_effects": ordered,
        "expected_result": {"state": "reverted"},
        "history_reference_evidence": ["history:kept", "references:kept"],
        "current_hashes": {target: effects.observe(target) for target in ("one", "two")},
    }


class RevertChangesTests(unittest.TestCase):
    def test_admit_then_execute_real_temporary_effects_once_in_order(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            effects, runs = FileEffects(root), FakeRuns()
            service = RevertChangesService(observe=effects.observe, apply_effect=effects.apply, run_tracker=runs)
            admitted = service.handle({"operation": "admit", "reversal_request": complete_request(effects)})
            self.assertEqual("admitted", admitted["outcome"])
            result = service.handle({"operation": "execute", "approved_reversal_manifest": admitted["approved_reversal_manifest"]})
            self.assertEqual("reverted", result["outcome"])
            self.assertEqual(["first", "second"], effects.calls)
            self.assertEqual(2, result["effect_account"]["applied_effect_count"])
            self.assertEqual("before-one", (root / "one").read_text(encoding="utf-8"))
            self.assertEqual("before-two", (root / "two").read_text(encoding="utf-8"))
            self.assertEqual(1, len(runs.starts))
            self.assertEqual(1, len(runs.finishes))

    def test_rejects_altered_order_before_run_or_mutation(self) -> None:
        effects, runs = MemoryEffects(), FakeRuns()
        request = complete_request(effects)
        request["operator_decision"]["approved_effect_ids"] = ["second", "first"]
        result = RevertChangesService(effects.observe, effects.apply, runs).handle({"operation": "admit", "reversal_request": request})
        self.assertEqual("blocked", result["outcome"])
        self.assertIn("effect_order", result["missing_or_mismatched_bindings"])
        self.assertEqual([], effects.calls)
        self.assertEqual([], runs.starts)

    def test_timeout_is_partial_failure_not_failed_and_stops(self) -> None:
        effects, runs = MemoryEffects(uncertain_at="first"), FakeRuns()
        service = RevertChangesService(effects.observe, effects.apply, runs)
        admitted = service.handle({"operation": "admit", "reversal_request": complete_request(effects)})
        result = service.handle({"operation": "execute", "approved_reversal_manifest": admitted["approved_reversal_manifest"]})
        self.assertEqual("partial_failure", result["outcome"])
        self.assertEqual("uncertain", result["effect_account"]["effects"][0]["status"])
        self.assertEqual("unattempted", result["effect_account"]["effects"][1]["status"])
        self.assertEqual(["first"], effects.calls)

    def test_completed_capability_with_wrong_observed_hash_is_uncertain_partial_failure(self) -> None:
        effects, runs = MemoryEffects(), FakeRuns()
        request = complete_request(effects)
        request["ordered_effects"][0]["expected_result_hash"] = digest("not-the-applied-state")
        service = RevertChangesService(effects.observe, effects.apply, runs)
        admitted = service.handle({"operation": "admit", "reversal_request": request})
        result = service.handle({"operation": "execute", "approved_reversal_manifest": admitted["approved_reversal_manifest"]})
        self.assertEqual("partial_failure", result["outcome"])
        self.assertEqual("uncertain", result["effect_account"]["effects"][0]["status"])
        self.assertEqual(0, result["effect_account"]["applied_effect_count"])
        self.assertEqual(["first"], effects.calls)

    def test_already_satisfied_result_is_no_op_with_action_evidence(self) -> None:
        effects, runs = MemoryEffects(), FakeRuns()
        request = complete_request(effects)
        for effect in request["ordered_effects"]:
            effects.values[effect["target_id"]] = effect["expected_after"]
        request["current_hashes"] = {target: effects.observe(target) for target in effects.values}
        service = RevertChangesService(effects.observe, effects.apply, runs)
        admitted = service.handle({"operation": "admit", "reversal_request": request})
        result = service.handle({"operation": "execute", "approved_reversal_manifest": admitted["approved_reversal_manifest"]})
        self.assertEqual("no_op", result["outcome"])
        self.assertEqual(0, result["effect_account"]["applied_effect_count"])
        self.assertEqual([], effects.calls)
        self.assertEqual(1, len(runs.starts))

    def test_invalid_cancellation_boundary_is_blocked_before_effect(self) -> None:
        effects, runs = MemoryEffects(), FakeRuns()
        service = RevertChangesService(effects.observe, effects.apply, runs)
        admitted = service.handle({"operation": "admit", "reversal_request": complete_request(effects)})
        result = service.handle({"operation": "execute", "approved_reversal_manifest": admitted["approved_reversal_manifest"], "cancel_after_effect_id": "second"})
        self.assertEqual("blocked", result["outcome"])
        self.assertEqual([], effects.calls)

    def test_stale_affected_reference_blocks_before_action_run_or_mutation(self) -> None:
        effects, runs = MemoryEffects(), FakeRuns()
        service = RevertChangesService(effects.observe, effects.apply, runs, lambda _: ["affected_reference_hash:ref:one"])
        admitted = RevertChangesService(effects.observe, effects.apply, runs).handle({"operation": "admit", "reversal_request": complete_request(effects)})
        result = service.handle({"operation": "execute", "approved_reversal_manifest": admitted["approved_reversal_manifest"]})
        self.assertEqual("blocked", result["outcome"])
        self.assertEqual([], effects.calls)
        self.assertEqual([], runs.starts)

    def test_shared_run_tracker_preview_execute_and_canonical_journal(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".git").mkdir()
            control = root / ".caprmedio_caprmedio"
            control.mkdir()
            (control / "caprmedio_project_settings.toml").write_text('[paths]\ncontrol_root = ".caprmedio_caprmedio"\njournal_root = ".caprmedio_caprmedio/_journal"\nruntime_root = ".caprmedio_runtime"\n', encoding="utf-8")
            effects = FileEffects(root)
            service = RevertChangesService(effects.observe, effects.apply, FakeRuns())
            admitted = service.handle({"operation": "admit", "reversal_request": complete_request(effects)})
            parameters, frontier, declared = {"reversal": "exact"}, ["plan/CA-P-1513.md"], [{"type": "revert", "target": "one"}]
            digest = canonical_json_digest
            request = {
                "request_id": "revert-shared-1", "operation_route": "revert.changes", "parameters": parameters,
                "parameters_digest": digest(parameters), "target_frontier": frontier, "target_frontier_digest": digest(frontier),
                "effects": declared, "effects_digest": digest(declared),
                "definition_manifest": {"manifest_ref": "selected/revert.json", "manifest_digest": "c" * 64},
                "source_freshness": {"selected_source_registry_ref": "selected/registry.json", "selected_source_registry_version": 1, "selected_source_registry_digest": "a" * 64, "selected_binding_ref": "selected/revert.json", "selected_binding_digest": "b" * 64},
                "initiative": {"initiative_id": "p1513", "instruction_summary": "exact approved reversal", "initiative_ref": "plan/CA-P-1513.md"},
                "requested_runs": [
                    {"requested_run_id": "workflow", "kind": "workflow", "definition": {"atom_id": "CA-O-130", "version": 1, "path": "operations/O130.md", "digest": "d" * 64}},
                    {"requested_run_id": "action", "kind": "action", "definition": {"atom_id": "CA-O-131", "version": 2, "path": "operations/O131.md", "digest": "e" * 64}, "parent_requested_run_id": "workflow"},
                ],
            }
            def observe_selected(_: dict) -> dict:
                return {"selected": True, "current": True, "observed": {"selected_source_registry_ref": "selected/registry.json", "selected_source_registry_version": 1, "selected_source_registry_digest": "a" * 64, "selected_binding_ref": "selected/revert.json", "selected_binding_digest": "b" * 64}}
            def execute(_: dict, session: object) -> None:
                workflow = session.start_run("workflow")
                result = service.execute_with_session(admitted["approved_reversal_manifest"], session, "action")
                session.finish_run(workflow["run_id"], outcome="completed", result_ref=".caprmedio_runtime/revert_changes/workflow.json", effect_refs=[".caprmedio_runtime/revert_changes/effect"])
                self.assertEqual("reverted", result["outcome"])
            tracker = RunTracker(root, source_observer=observe_selected, executor=execute)
            preview = tracker.run_selected_operation(request)
            self.assertEqual("preview", preview["disposition"])
            authorization = {"authorization_ref": "authorizations/revert.json", "authorization_freshness": {"state": "current", "digest": "f" * 64}, "request_id": request["request_id"], "operation_route": request["operation_route"], "proposal_receipt_digest": preview["proposal_receipt_digest"], "parameters_digest": request["parameters_digest"], "target_frontier_digest": request["target_frontier_digest"], "effects_digest": request["effects_digest"], "definition_manifest": request["definition_manifest"], "source_freshness": request["source_freshness"]}
            result = tracker.run_selected_operation({**request, "mode": "execute", "proposal_receipt": preview["proposal_receipt"], "proposal_receipt_digest": preview["proposal_receipt_digest"], "assigned_action_id": "CA-O-131", "operator_authorization": authorization})
            self.assertEqual("terminal", result["disposition"])
            self.assertEqual(["first", "second"], effects.calls)
            journal = next((root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))
            self.assertEqual(4, len(journal.read_text(encoding="utf-8").splitlines()))

    def test_shared_session_recovers_canonical_pending_terminal_without_replay(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary); (root / ".git").mkdir(); control = root / ".caprmedio_caprmedio"; control.mkdir()
            (control / "caprmedio_project_settings.toml").write_text('[paths]\ncontrol_root = ".caprmedio_caprmedio"\njournal_root = ".caprmedio_caprmedio/_journal"\nruntime_root = ".caprmedio_runtime"\n', encoding="utf-8")
            effects, service, sessions = FileEffects(root), None, []
            service = RevertChangesService(effects.observe, effects.apply, FakeRuns())
            admitted = service.handle({"operation": "admit", "reversal_request": complete_request(effects)})
            d = canonical_json_digest; parameters, frontier, declared = {"reversal": "recover"}, ["plan/p1513"], [{"type": "revert"}]
            request = {"request_id": "revert-recover-1", "operation_route": "revert.changes", "parameters": parameters, "parameters_digest": d(parameters), "target_frontier": frontier, "target_frontier_digest": d(frontier), "effects": declared, "effects_digest": d(declared), "definition_manifest": {"manifest_ref": "selected/revert.json", "manifest_digest": "c" * 64}, "source_freshness": {"selected_source_registry_ref": "selected/registry.json", "selected_source_registry_version": 1, "selected_source_registry_digest": "a" * 64, "selected_binding_ref": "selected/revert.json", "selected_binding_digest": "b" * 64}, "initiative": {"initiative_id": "p1513", "instruction_summary": "recover Journal only", "initiative_ref": "plan/p1513"}, "requested_runs": [{"requested_run_id": "workflow", "kind": "workflow", "definition": {"atom_id": "CA-O-130", "version": 1, "path": "operations/O130.md", "digest": "d" * 64}}, {"requested_run_id": "action", "kind": "action", "definition": {"atom_id": "CA-O-131", "version": 2, "path": "operations/O131.md", "digest": "e" * 64}, "parent_requested_run_id": "workflow"}]}
            observe = lambda _: {"selected": True, "current": True, "observed": {"selected_source_registry_ref": "selected/registry.json", "selected_source_registry_version": 1, "selected_source_registry_digest": "a" * 64, "selected_binding_ref": "selected/revert.json", "selected_binding_digest": "b" * 64}}
            blocked: dict = {}
            def execute(_: dict, session: object) -> None:
                workflow = session.start_run("workflow"); sessions.append(session)
                blocked.update(service.execute_with_session(admitted["approved_reversal_manifest"], session, "action"))
                session.finish_run(workflow["run_id"], outcome="completed", result_ref=".caprmedio_runtime/revert_changes/workflow.json", effect_refs=[])
            tracker = RunTracker(root, source_observer=observe, executor=execute)
            preview = tracker.run_selected_operation(request)
            auth = {"authorization_ref": "authorizations/revert.json", "authorization_freshness": {"state": "current", "digest": "f" * 64}, "request_id": request["request_id"], "operation_route": request["operation_route"], "proposal_receipt_digest": preview["proposal_receipt_digest"], "parameters_digest": request["parameters_digest"], "target_frontier_digest": request["target_frontier_digest"], "effects_digest": request["effects_digest"], "definition_manifest": request["definition_manifest"], "source_freshness": request["source_freshness"]}
            original, calls = workflow_run_support.work_journal.append_sealed_events, [0]
            def fail_one(*args: object, **kwargs: object) -> object:
                calls[0] += 1
                if calls[0] == 3: raise OSError("terminal append unavailable")
                return original(*args, **kwargs)
            with mock.patch.object(workflow_run_support.work_journal, "append_sealed_events", side_effect=fail_one):
                tracker.run_selected_operation({**request, "mode": "execute", "proposal_receipt": preview["proposal_receipt"], "proposal_receipt_digest": preview["proposal_receipt_digest"], "assigned_action_id": "CA-O-131", "operator_authorization": auth})
            self.assertEqual("recording_blocked", blocked["outcome"])
            recovered = service.recover_recording_with_session(blocked["pending_recording_event"], sessions[0])
            self.assertEqual("reverted", recovered["outcome"])
            self.assertEqual(["first", "second"], effects.calls)

    def test_recording_retry_never_replays_effect(self) -> None:
        effects, runs = MemoryEffects(), FakeRuns(fail_finish=True)
        service = RevertChangesService(effects.observe, effects.apply, runs)
        admitted = service.handle({"operation": "admit", "reversal_request": complete_request(effects)})
        blocked = service.handle({"operation": "execute", "approved_reversal_manifest": admitted["approved_reversal_manifest"]})
        self.assertEqual("recording_blocked", blocked["outcome"])
        calls = list(effects.calls)
        recovered = service.handle({"operation": "recover_recording", "pending_recording_event": blocked["pending_recording_event"]})
        self.assertEqual("reverted", recovered["outcome"])
        self.assertEqual(calls, effects.calls)

    def test_cancel_at_admitted_boundary_preserves_completed_and_unattempted(self) -> None:
        effects, runs = MemoryEffects(), FakeRuns()
        service = RevertChangesService(effects.observe, effects.apply, runs)
        admitted = service.handle({"operation": "admit", "reversal_request": complete_request(effects)})
        result = service.handle({"operation": "execute", "approved_reversal_manifest": admitted["approved_reversal_manifest"], "cancel_after_effect_id": "first"})
        self.assertEqual("canceled", result["outcome"])
        self.assertEqual(["first"], effects.calls)
        self.assertEqual("completed", result["effect_account"]["effects"][0]["status"])
        self.assertEqual("unattempted", result["effect_account"]["effects"][1]["status"])


if __name__ == "__main__":
    unittest.main()
