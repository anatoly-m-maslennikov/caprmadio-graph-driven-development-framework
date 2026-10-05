"""Read-only recovery evidence tests for selected Run Sessions."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import selected_run_recovery  # noqa: E402
import work_journal  # noqa: E402
from workflow_run_support import LazyRunTracker, RunExecutionSession, SelectedRunError  # noqa: E402


def _digest(value: object) -> str:
    return work_journal.canonical_json_digest(value)


def _definition(atom_id: str, path: str, digest: str) -> dict[str, object]:
    return {"atom_id": atom_id, "version": 1, "path": path, "digest": digest * 64}


class SelectedRunRecoveryTest(unittest.TestCase):
    def _request(self) -> dict[str, object]:
        parameters = {"mode": "recovery"}
        frontier = ["03_plan/CA-P-1660.md"]
        effects = [{"type": "read", "target": "03_plan/CA-P-1660.md"}]
        workflow = _definition("CA-O-1660", "operations/recovery-workflow.md", "a")
        action = _definition("CA-O-1661", "operations/recovery-action.md", "b")
        request = {
            "mode": "execute",
            "request_id": "request-recovery-1660",
            "operation_route": "selected.recovery",
            "parameters": parameters,
            "parameters_digest": _digest(parameters),
            "target_frontier": frontier,
            "target_frontier_digest": _digest(frontier),
            "effects": effects,
            "effects_digest": _digest(effects),
            "definition_manifest": {"manifest_ref": "selected/recovery.manifest.json", "manifest_digest": "c" * 64},
            "source_freshness": {
                "selected_source_registry_ref": "selected/registry.json",
                "selected_source_registry_version": 1,
                "selected_source_registry_digest": "d" * 64,
                "selected_binding_ref": "selected/recovery.json",
                "selected_binding_digest": "e" * 64,
            },
            "initiative": {
                "initiative_id": "initiative-1660",
                "instruction_summary": "reconstruct sealed evidence without effects",
                "initiative_ref": "03_plan/CA-P-1660.md",
            },
            "requested_runs": [
                {"requested_run_id": "workflow-1660", "kind": "workflow", "definition": workflow},
                {
                    "requested_run_id": "action-1660",
                    "kind": "action",
                    "definition": action,
                    "parent_requested_run_id": "workflow-1660",
                },
            ],
            "proposal_receipt": {},
            "proposal_receipt_digest": "f" * 64,
            "assigned_action_id": "action-recovery-1660",
            "operator_authorization": {},
        }
        return request

    @staticmethod
    def _event(
        request: dict[str, object],
        *,
        event_id: str,
        event_name: str,
        run: dict[str, object],
        bindings: list[dict[str, object]],
        outcome: str | None = None,
        result_ref: str | None = None,
    ) -> dict[str, object]:
        return work_journal.with_event_digest(
            {
                "schema_version": 5,
                "kind": "workflow_execution",
                "event_id": event_id,
                "action_id": request["assigned_action_id"],
                "event": event_name,
                "author": "recovery-bot",
                "occurred_at": "2026-10-05T00:00:00+00:00",
                "llm_session": {"app": "run-support", "uuid": request["request_id"]},
                "structural_scope": "TOOLS",
                "initiative": request["initiative"],
                "run": run,
                "definition_bindings": bindings,
                "input_ref": request["initiative"]["initiative_ref"],
                "outcome": outcome,
                "result_ref": result_ref,
                "effect_refs": [],
                "report_ref": None,
                "redaction": {"redacted": False, "fields": []},
            }
        )

    def _events(self, request: dict[str, object]) -> list[dict[str, object]]:
        workflow_definition = request["requested_runs"][0]["definition"]
        action_definition = request["requested_runs"][1]["definition"]
        workflow = {"run_id": "actual-workflow-1660", "kind": "workflow", "definition": workflow_definition}
        action = {
            "run_id": "actual-action-1660",
            "kind": "action",
            "definition": action_definition,
            "parent_run_id": workflow["run_id"],
        }
        workflow_bindings = sorted(
            [
                {"kind": "workflow", **workflow_definition},
                {"kind": "action", **action_definition},
            ],
            key=lambda item: (item["kind"], item["atom_id"], item["version"], item["path"]),
        )
        action_bindings = [{"kind": "action", **action_definition}]
        return [
            self._event(request, event_id="event-start-workflow", event_name="started", run=workflow, bindings=workflow_bindings),
            self._event(request, event_id="event-start-action", event_name="started", run=action, bindings=action_bindings),
            self._event(request, event_id="event-end-action", event_name="completed", run=action, bindings=action_bindings, outcome="completed", result_ref="results/action-1660.json"),
            self._event(request, event_id="event-end-workflow", event_name="completed", run=workflow, bindings=workflow_bindings, outcome="completed", result_ref="results/workflow-1660.json"),
        ]

    def _interrupted_action_events(self, request: dict[str, object]) -> list[dict[str, object]]:
        events = self._events(request)
        action = events[1]["run"]
        bindings = events[1]["definition_bindings"]
        return [
            events[0],
            events[1],
            self._event(
                request,
                event_id="event-interrupted-action",
                event_name="interrupted",
                run=action,
                bindings=bindings,
                outcome="interrupted_pending",
            ),
        ]

    @staticmethod
    def _evidence(events: list[dict[str, object]]) -> list[dict[str, object]]:
        return [
            {
                "event": event,
                "receipt": {
                    "event_id": event["event_id"],
                    "action_id": event["action_id"],
                    "event_digest": event["event_digest"],
                    "carrier": f"memory/{index}.ndjson",
                    "line": 1,
                    "previous_carrier_digest": "0" * 64,
                    "appended_carrier_digest": "0" * 64,
                },
            }
            for index, event in enumerate(events, start=1)
        ]

    def test_pure_validator_and_restore_reconstruct_terminal_state_without_effects(self) -> None:
        request = self._request()
        events = self._events(request)

        self.assertEqual(events, selected_run_recovery.validate_selected_run_events(request, events))
        evidence = self._evidence(events)
        session = RunExecutionSession.restore(object(), request, evidence)

        self.assertEqual({"workflow-1660", "action-1660"}, set(session.actual))
        self.assertEqual({"workflow-1660", "action-1660"}, set(session.terminal))
        self.assertEqual([], session.pending)
        self.assertEqual({}, session.observed_effects)

    def test_pure_validator_rejects_duplicate_terminal_evidence(self) -> None:
        request = self._request()
        events = self._events(request)
        duplicate = dict(events[-1])
        duplicate["event_id"] = "event-end-workflow-duplicate"
        events.append(work_journal.with_event_digest(duplicate))

        with self.assertRaisesRegex(SelectedRunError, "duplicate-terminal"):
            selected_run_recovery.validate_selected_run_events(request, events)

    def test_restore_rejects_recovery_evidence_out_of_causal_order(self) -> None:
        request = self._request()
        events = self._interrupted_action_events(request)
        recovered = self._event(
            request,
            event_id="event-recovered-action",
            event_name="recovered",
            run=events[1]["run"],
            bindings=events[1]["definition_bindings"],
            outcome="completed",
            result_ref="results/action-1660.json",
        )
        # The exact same facts are not lawful when the recovered fact precedes
        # the canonical interruption.  Recovery must not reorder them.
        unordered = [events[0], events[1], recovered, events[2]]

        with self.assertRaisesRegex(SelectedRunError, "invalid-recovery-order"):
            RunExecutionSession.restore(object(), request, self._evidence(unordered))

    def test_release_recovery_reuses_started_id_and_locks_final_result(self) -> None:
        request = self._request()
        request["operation_route"] = "release_version"
        evidence = self._evidence(self._interrupted_action_events(request))
        tracker = _MemoryTracker(request)
        session = RunExecutionSession.restore(tracker, request, evidence)
        action = session.actual["action-1660"]

        # No second started event is emitted for an interrupted actual Run.
        self.assertEqual(action, session.start_run("action-1660"))
        final = session.recover_run(
            action["run_id"],
            outcome="completed",
            result_ref="results/action-1660.json",
            effect_refs=[],
        )

        self.assertEqual("terminal", final["disposition"])
        self.assertEqual("event-recovered-1", final["event_id"])
        self.assertEqual("event-recovered-1", final["event_receipt"]["event_id"])
        self.assertEqual("recovered", tracker.events[-1]["event"])
        self.assertEqual("completed", session.terminal["action-1660"]["outcome"])
        self.assertEqual(1, len(tracker.events))
        with self.assertRaisesRegex(SelectedRunError, "duplicate-terminal"):
            session.recover_run(
                action["run_id"],
                outcome="completed",
                result_ref="results/action-1660-again.json",
                effect_refs=[],
            )

    def test_recovered_pending_remains_resumable_but_generic_finish_is_refused(self) -> None:
        request = self._request()
        request["operation_route"] = "release_version"
        tracker = _MemoryTracker(request)
        session = RunExecutionSession.restore(tracker, request, self._evidence(self._interrupted_action_events(request)))
        action = session.actual["action-1660"]

        pending = session.recover_run(
            action["run_id"], outcome="interrupted_pending", result_ref=None, effect_refs=[]
        )
        self.assertEqual("interrupted", pending["disposition"])
        self.assertEqual("interrupted_pending", session.interrupted["action-1660"]["outcome"])
        self.assertTrue(session.interrupted["action-1660"]["recovered"])
        with self.assertRaisesRegex(SelectedRunError, "recovery-required"):
            session.finish_run(
                action["run_id"], outcome="completed", result_ref="results/action-1660.json", effect_refs=[]
            )
        final = session.recover_run(
            action["run_id"], outcome="completed", result_ref="results/action-1660.json", effect_refs=[]
        )
        self.assertEqual("terminal", final["disposition"])
        result = LazyRunTracker._session_result(
            object(), request, {"source_freshness": {"current": True}}, session
        )
        self.assertEqual("terminal", result["disposition"])
        self.assertNotIn("interrupted_runs", result)
        self.assertEqual(["recovered", "recovered"], [event["event"] for event in tracker.events])

    def test_failed_recovery_append_allows_only_exact_pending_event_recovery(self) -> None:
        request = self._request()
        request["operation_route"] = "release_version"
        tracker = _MemoryTracker(request, fail_append=True)
        session = RunExecutionSession.restore(tracker, request, self._evidence(self._interrupted_action_events(request)))
        action = session.actual["action-1660"]

        pending = session.recover_run(
            action["run_id"], outcome="completed", result_ref="results/action-1660.json", effect_refs=[]
        )

        self.assertEqual("recording_pending", pending["disposition"])
        self.assertEqual(["event-recovered-1"], session.pending)
        self.assertEqual([], tracker.events)
        with self.assertRaisesRegex(SelectedRunError, "duplicate-terminal"):
            session.recover_run(
                action["run_id"], outcome="completed", result_ref="results/action-1660.json", effect_refs=[]
            )

    def test_recovery_is_release_only_and_session_result_reports_interruption(self) -> None:
        request = self._request()
        tracker = _MemoryTracker(request)
        session = RunExecutionSession.restore(tracker, request, self._evidence(self._interrupted_action_events(request)))
        action = session.actual["action-1660"]

        with self.assertRaisesRegex(SelectedRunError, "recovery-not-supported"):
            session.recover_run(
                action["run_id"], outcome="completed", result_ref="results/action-1660.json", effect_refs=[]
            )

        result = LazyRunTracker._session_result(
            object(), request, {"source_freshness": {"current": True}}, session
        )
        self.assertEqual("started", result["disposition"])
        self.assertEqual("inspect-or-recover-only", result["retry_disposition"])
        self.assertEqual(["actual-action-1660"], [item["run_id"] for item in result["interrupted_runs"]])


class _MemoryTracker:
    """Pure Journal recorder used by recovery state-machine tests only."""

    def __init__(self, request: dict[str, object], *, fail_append: bool = False) -> None:
        self.request = request
        self.fail_append = fail_append
        self.events: list[dict[str, object]] = []

    def _lazy_journal_event(
        self,
        request: dict[str, object],
        run: dict[str, object],
        event_name: str,
        outcome: str | None,
        result_ref: str | None,
        effect_refs: list[str],
        report_ref: str | None,
        bindings: list[dict[str, object]],
    ) -> dict[str, object]:
        return SelectedRunRecoveryTest._event(
            request,
            event_id=f"event-recovered-{len(self.events) + 1}",
            event_name=event_name,
            run=run,
            bindings=bindings,
            outcome=outcome,
            result_ref=result_ref,
        )

    def _append_one(
        self,
        event: dict[str, object],
        result_ref: str | None,
        effect_refs: list[str],
    ) -> dict[str, object]:
        if self.fail_append:
            raise OSError("simulated canonical Journal append failure")
        self.events.append(event)
        return {
            "event_id": event["event_id"],
            "action_id": event["action_id"],
            "event_digest": event["event_digest"],
            "carrier": f"memory/recovered-{len(self.events)}.ndjson",
            "line": 1,
            "previous_carrier_digest": "0" * 64,
            "appended_carrier_digest": "0" * 64,
        }


if __name__ == "__main__":
    unittest.main()
