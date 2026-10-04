"""Golden tests for the shared selected-run admission and Journal boundary."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import work_journal  # noqa: E402
from work_journal import canonical_json_digest  # noqa: E402
from workflow_run_support import RunTracker, SelectedRunError  # noqa: E402


def _digest(value: object) -> str:
    return canonical_json_digest(value)


class SelectedRunSupportTest(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.root = Path(self.directory.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\n"
            'control_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        self.request = self._request()
        self.effects = 0
        self.tracker = RunTracker(
            self.root,
            source_observer=lambda request: {
                "selected": request["operation_route"] == "atom.create",
                "current": True,
                "observed": {
                    "selected_source_registry_ref": "selected/registry.json",
                    "selected_source_registry_version": 4,
                    "selected_source_registry_digest": "a" * 64,
                    "selected_binding_ref": "selected/atom.create.json",
                    "selected_binding_digest": "b" * 64,
                    "definition_manifest": request["definition_manifest"],
                },
            },
            executor=self._execute,
        )

    def tearDown(self) -> None:
        self.directory.cleanup()

    def _request(self) -> dict[str, object]:
        parameters = {"title": "bounded selected run"}
        frontier = ["03_plan/CA-P-1510.md"]
        effects = [{"type": "create", "target": "03_plan/result.md"}]
        manifest = {"manifest_ref": "selected/atom.create.manifest.json", "manifest_digest": "c" * 64}
        return {
            "request_id": "request-1510",
            "operation_route": "atom.create",
            "parameters": parameters,
            "parameters_digest": _digest(parameters),
            "target_frontier": frontier,
            "target_frontier_digest": _digest(frontier),
            "effects": effects,
            "effects_digest": _digest(effects),
            "definition_manifest": manifest,
            "source_freshness": {
                "selected_source_registry_ref": "selected/registry.json",
                "selected_source_registry_version": 4,
                "selected_source_registry_digest": "a" * 64,
                "selected_binding_ref": "selected/atom.create.json",
                "selected_binding_digest": "b" * 64,
            },
            "initiative": {
                "initiative_id": "initiative-1510",
                "instruction_summary": "execute one bounded selected run",
                "initiative_ref": "03_plan/CA-P-1510.md",
            },
            "requested_runs": [
                {
                    "requested_run_id": "caller-workflow-run-1",
                    "kind": "workflow",
                    "definition": {
                        "atom_id": "CA-O-1500",
                        "version": 1,
                        "path": "operations/CA-O-1500.md",
                        "digest": "c" * 64,
                    },
                },
                {
                    "requested_run_id": "caller-action-run-1",
                    "kind": "action",
                    "definition": {
                        "atom_id": "CA-O-1510",
                        "version": 1,
                        "path": "operations/CA-O-1510.md",
                        "digest": "d" * 64,
                    },
                    "parent_requested_run_id": "caller-workflow-run-1",
                },
                {
                    "requested_run_id": "skipped-branch-action-run",
                    "kind": "action",
                    "definition": {
                        "atom_id": "CA-O-1511",
                        "version": 1,
                        "path": "operations/CA-O-1511.md",
                        "digest": "f" * 64,
                    },
                    "parent_requested_run_id": "caller-workflow-run-1",
                }
            ],
        }

    def _execute(self, request: dict[str, object], session: object) -> None:
        workflow = session.start_run("caller-workflow-run-1")
        action = session.start_run("caller-action-run-1")
        self.effects += 1
        session.finish_run(
            action["run_id"], outcome="completed", result_ref="results/CA-R-1510.json", effect_refs=["03_plan/result.md"], report_ref="reports/CA-R-1510.md"
        )
        session.finish_run(
            workflow["run_id"], outcome="completed", result_ref="results/CA-R-1510.json", effect_refs=["03_plan/result.md"], report_ref="reports/CA-R-1510.md"
        )

    def _authorization(self, preview: dict[str, object], request: dict[str, object] | None = None) -> dict[str, object]:
        request = request or self.request
        return {
            "authorization_ref": "authorizations/CA-AUTH-1510.json",
            "authorization_freshness": {"state": "current", "digest": "e" * 64},
            "request_id": request["request_id"],
            "operation_route": request["operation_route"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "parameters_digest": request["parameters_digest"],
            "target_frontier_digest": request["target_frontier_digest"],
            "effects_digest": request["effects_digest"],
            "definition_manifest": request["definition_manifest"],
            "source_freshness": request["source_freshness"],
        }

    def _execute_request(self, tracker: RunTracker, request: dict[str, object]) -> dict[str, object]:
        preview = tracker.run_selected_operation(request)
        return tracker.run_selected_operation(
            {
                **request,
                "mode": "execute",
                "proposal_receipt": preview["proposal_receipt"],
                "proposal_receipt_digest": preview["proposal_receipt_digest"],
                "assigned_action_id": "action-1510",
                "operator_authorization": self._authorization(preview, request),
            }
        )

    def test_preview_is_read_only_and_execute_records_distinct_actual_run(self) -> None:
        preview = self.tracker.run_selected_operation(self.request)
        self.assertEqual("preview", preview["disposition"])
        self.assertNotIn("run_ids", preview)
        self.assertNotIn("event_receipts", preview)
        self.assertEqual(0, self.effects)

        execute_request = {
            **self.request,
            "mode": "execute",
            "proposal_receipt": preview["proposal_receipt"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "assigned_action_id": "action-1510",
            "operator_authorization": self._authorization(preview),
        }
        result = self.tracker.run_selected_operation(execute_request)

        self.assertEqual("terminal", result["disposition"])
        self.assertEqual(1, self.effects)
        self.assertEqual("caller-workflow-run-1", result["run_ids"][0])
        self.assertEqual(2, len(result["run_ids"]))
        self.assertEqual(4, len(result["event_receipts"]))
        journal = next((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))
        events = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(["started", "started", "completed", "completed"], [event["event"] for event in events])
        self.assertTrue(all(event["schema_version"] == 5 for event in events))
        self.assertEqual("caller-workflow-run-1", events[0]["run"]["run_id"])
        self.assertFalse(any(event["run"]["run_id"] == "skipped-branch-action-run" for event in events))

    def test_rejects_changed_request_id_and_shadow_manifest_before_effect(self) -> None:
        self.tracker.run_selected_operation(self.request)
        changed = {**self.request, "parameters": {"title": "changed"}}
        changed["parameters_digest"] = _digest(changed["parameters"])
        with self.assertRaisesRegex(SelectedRunError, "request-id-conflict"):
            self.tracker.run_selected_operation(changed)
        shadowed = {
            **self.request,
            "request_id": "request-shadow",
            "source_freshness": {**self.request["source_freshness"], "definition_manifest": self.request["definition_manifest"]},
        }
        with self.assertRaisesRegex(SelectedRunError, "unknown field"):
            self.tracker.run_selected_operation(shadowed)
        self.assertEqual(0, self.effects)

    def test_execute_can_add_required_run_identities_after_a_valid_preview(self) -> None:
        preview_request = dict(self.request)
        preview_request.pop("requested_runs")
        preview = self.tracker.run_selected_operation(preview_request)
        result = self.tracker.run_selected_operation(
            {
                **self.request,
                "mode": "execute",
                "proposal_receipt": preview["proposal_receipt"],
                "proposal_receipt_digest": preview["proposal_receipt_digest"],
                "assigned_action_id": "action-1510",
                "operator_authorization": self._authorization(preview),
            }
        )
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual(1, self.effects)

    def test_stale_source_blocks_without_start(self) -> None:
        self.tracker = RunTracker(
            self.root,
            source_observer=lambda _: {"selected": True, "current": False, "observed": {"reason": "binding drift"}},
            executor=self._execute,
        )
        result = self.tracker.run_selected_operation(self.request)
        self.assertEqual("blocked", result["disposition"])
        self.assertNotIn("run_ids", result)
        self.assertEqual(0, self.effects)

    def test_executor_exception_interrupts_only_started_run(self) -> None:
        def failing_executor(_: dict[str, object], session: object) -> None:
            session.start_run("caller-workflow-run-1")
            raise RuntimeError("route execution failed after start")

        self.tracker = RunTracker(
            self.root,
            source_observer=self.tracker.source_observer,
            executor=failing_executor,
        )
        preview = self.tracker.run_selected_operation(self.request)
        result = self.tracker.run_selected_operation(
            {
                **self.request,
                "mode": "execute",
                "proposal_receipt": preview["proposal_receipt"],
                "proposal_receipt_digest": preview["proposal_receipt_digest"],
                "assigned_action_id": "action-1510",
                "operator_authorization": self._authorization(preview),
            }
        )
        self.assertEqual("started", result["disposition"])
        self.assertEqual("RuntimeError", result["execution_error"])
        self.assertEqual(["caller-workflow-run-1"], result["run_ids"])
        self.assertEqual("interrupted_pending", result["terminal_runs"][0]["outcome"])
        self.assertEqual(2, len(result["event_receipts"]))

    def test_terminal_outcome_matrix_writes_actual_v5_receipts(self) -> None:
        cases = (
            ("no_op", [], "completed"),
            ("failed", [], "failed"),
            ("cancelled", [], "abandoned"),
            ("partial", ["03_plan/partial-result.md"], "failed"),
        )
        for number, (outcome, effect_refs, expected_event) in enumerate(cases, start=1):
            request = {**self.request, "request_id": f"outcome-{number}"}

            def executor(_: dict[str, object], session: object, *, outcome: str = outcome, effect_refs: list[str] = effect_refs) -> None:
                workflow = session.start_run("caller-workflow-run-1")
                session.finish_run(
                    workflow["run_id"],
                    outcome=outcome,
                    result_ref=f"results/{outcome}.json",
                    effect_refs=effect_refs,
                    report_ref=f"reports/{outcome}.md",
                )

            tracker = RunTracker(self.root, source_observer=self.tracker.source_observer, executor=executor)
            result = self._execute_request(tracker, request)
            self.assertEqual("terminal", result["disposition"])
            self.assertEqual(outcome, result["terminal_runs"][0]["outcome"])
            self.assertEqual(2, len(result["event_receipts"]))
            self.assertEqual(expected_event, result["event_receipts"][-1]["carrier"] and self._terminal_event(request["request_id"])["event"])
            self.assertEqual(effect_refs, self._terminal_event(request["request_id"])["effect_refs"])

    def test_exception_after_effect_records_partial_and_restart_recovery_never_reexecutes(self) -> None:
        effects = {"count": 0}
        request = {**self.request, "request_id": "request-recording-pending"}

        def executor(_: dict[str, object], session: object) -> None:
            workflow = session.start_run("caller-workflow-run-1")
            effects["count"] += 1
            session.note_effects(
                workflow["run_id"], result_ref="results/exception-after-effect.json", effect_refs=["03_plan/effect-before-exception.md"]
            )
            raise RuntimeError("effect happened before exception")

        tracker = RunTracker(self.root, source_observer=self.tracker.source_observer, executor=executor)
        result = self._execute_request(tracker, request)
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual("partial", result["terminal_runs"][0]["outcome"])
        self.assertEqual(["03_plan/effect-before-exception.md"], self._terminal_event(request["request_id"])["effect_refs"])
        self.assertEqual(1, effects["count"])

        pending_request = {**self.request, "request_id": "request-pending-recovery"}
        original_atomic = work_journal._atomic_json
        receipt_writes = {"count": 0}

        def fail_receipt(path: Path, value: dict[str, object]) -> None:
            if path.parent.name == "receipts":
                receipt_writes["count"] += 1
                if receipt_writes["count"] == 2:
                    raise OSError("terminal receipt persistence interrupted")
            original_atomic(path, value)

        with mock.patch.object(work_journal, "_atomic_json", side_effect=fail_receipt):
            pending = self._execute_request(tracker, pending_request)
        self.assertEqual("recording_pending", pending["disposition"])
        self.assertEqual(2, effects["count"])
        event_id = pending["pending_event_ids"][0]

        restarted = RunTracker(self.root, source_observer=self.tracker.source_observer, executor=executor)
        replay = self._execute_request(restarted, pending_request)
        self.assertEqual("blocked", replay["disposition"])
        self.assertEqual(2, effects["count"])
        receipt = restarted.recover_recording(event_id)
        self.assertEqual(event_id, receipt["event_id"])
        self.assertEqual(2, effects["count"])
        self.assertEqual(1, sum(1 for event in self._events() if event["event_id"] == event_id))
        replay_after_recovery = self._execute_request(restarted, pending_request)
        self.assertEqual("blocked", replay_after_recovery["disposition"])
        self.assertEqual(2, effects["count"])

    def _events(self) -> list[dict[str, object]]:
        return [
            json.loads(line)
            for path in (self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")
            for line in path.read_text(encoding="utf-8").splitlines()
        ]

    def _terminal_event(self, request_id: str) -> dict[str, object]:
        return next(event for event in reversed(self._events()) if event["llm_session"]["uuid"] == request_id and event["event"] != "started")


if __name__ == "__main__":
    unittest.main()
