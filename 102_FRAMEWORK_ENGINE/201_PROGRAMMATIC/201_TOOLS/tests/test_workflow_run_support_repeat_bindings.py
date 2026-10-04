"""Regression coverage for repeated selected-Run definition bindings."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import work_journal  # noqa: E402
from workflow_run_support import RunTracker, SelectedRunError  # noqa: E402


def _digest(value: object) -> str:
    return work_journal.canonical_json_digest(value)


def _definition(atom_id: str, path: str, digest: str) -> dict[str, object]:
    return {"atom_id": atom_id, "version": 1, "path": path, "digest": digest * 64}


class WorkflowRunSupportRepeatBindingsTest(unittest.TestCase):
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
        self.started: list[str] = []

    def tearDown(self) -> None:
        self.directory.cleanup()

    def _request(self, *, second_step_digest: str = "b") -> dict[str, object]:
        parameters = {"repeat": 2}
        frontier = ["03_plan/CA-P-1541.md"]
        effects: list[object] = []
        manifest = {"manifest_ref": "selected/repeat.manifest.json", "manifest_digest": "c" * 64}
        workflow = _definition("CA-O-1541", "operations/workflow.md", "a")
        step_first = _definition("CA-O-1542", "operations/repeated-step.md", "b")
        step_second = _definition("CA-O-1542", "operations/repeated-step.md", second_step_digest)
        action = _definition("CA-O-1543", "operations/repeated-action.md", "d")
        return {
            "request_id": "repeat-bindings",
            "operation_route": "selected.repeat",
            "parameters": parameters,
            "parameters_digest": _digest(parameters),
            "target_frontier": frontier,
            "target_frontier_digest": _digest(frontier),
            "effects": effects,
            "effects_digest": _digest(effects),
            "definition_manifest": manifest,
            "source_freshness": {
                "selected_source_registry_ref": "selected/registry.json",
                "selected_source_registry_version": 1,
                "selected_source_registry_digest": "e" * 64,
                "selected_binding_ref": "selected/repeat.json",
                "selected_binding_digest": "f" * 64,
            },
            "initiative": {
                "initiative_id": "initiative-1541",
                "instruction_summary": "run a bounded repeated selected Step",
                "initiative_ref": "03_plan/CA-P-1541.md",
            },
            "requested_runs": [
                {"requested_run_id": "workflow-run", "kind": "workflow", "definition": workflow},
                {"requested_run_id": "step-run:1", "kind": "step", "definition": step_first,
                 "parent_requested_run_id": "workflow-run"},
                {"requested_run_id": "action-run:1", "kind": "action", "definition": action,
                 "parent_requested_run_id": "step-run:1"},
                {"requested_run_id": "step-run:2", "kind": "step", "definition": step_second,
                 "parent_requested_run_id": "workflow-run"},
                {"requested_run_id": "action-run:2", "kind": "action", "definition": action,
                 "parent_requested_run_id": "step-run:2"},
            ],
        }

    @staticmethod
    def _observer(request: dict[str, object]) -> dict[str, object]:
        return {
            "selected": request["operation_route"] == "selected.repeat",
            "current": True,
            "observed": {
                "selected_source_registry_ref": "selected/registry.json",
                "selected_source_registry_version": 1,
                "selected_source_registry_digest": "e" * 64,
                "selected_binding_ref": "selected/repeat.json",
                "selected_binding_digest": "f" * 64,
                "definition_manifest": request["definition_manifest"],
            },
        }

    def _executor(self, _request: dict[str, object], session: object) -> None:
        workflow = session.start_run("workflow-run")
        for visit in (1, 2):
            step = session.start_run(f"step-run:{visit}")
            action = session.start_run(f"action-run:{visit}")
            self.started.append(action["run_id"])
            session.finish_run(action["run_id"], outcome="completed",
                               result_ref=f"results/action-{visit}.json", effect_refs=[])
            session.finish_run(step["run_id"], outcome="completed",
                               result_ref=f"results/step-{visit}.json", effect_refs=[])
        session.finish_run(workflow["run_id"], outcome="completed",
                           result_ref="results/workflow.json", effect_refs=[])

    @staticmethod
    def _authorization(preview: dict[str, object], request: dict[str, object]) -> dict[str, object]:
        return {
            "authorization_ref": "authorizations/CA-AUTH-1541.json",
            "authorization_freshness": {"state": "current", "digest": "a" * 64},
            "request_id": request["request_id"],
            "operation_route": request["operation_route"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "parameters_digest": request["parameters_digest"],
            "target_frontier_digest": request["target_frontier_digest"],
            "effects_digest": request["effects_digest"],
            "definition_manifest": request["definition_manifest"],
            "source_freshness": request["source_freshness"],
        }

    def _execute_request(self, request: dict[str, object]) -> dict[str, object]:
        tracker = RunTracker(self.root, source_observer=self._observer, executor=self._executor)
        preview = tracker.run_selected_operation(request)
        return tracker.run_selected_operation({
            **request,
            "mode": "execute",
            "proposal_receipt": preview["proposal_receipt"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "assigned_action_id": "action-1541",
            "operator_authorization": self._authorization(preview, request),
        })

    def test_repeated_run_ids_keep_lineage_while_workflow_binding_is_unique(self) -> None:
        result = self._execute_request(self._request())

        self.assertEqual("terminal", result["disposition"])
        self.assertEqual(5, len(result["run_ids"]))
        self.assertEqual(2, len(self.started))
        events = [
            json.loads(line)
            for path in (self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")
            for line in path.read_text(encoding="utf-8").splitlines()
        ]
        starts = [event for event in events if event["event"] == "started"]
        self.assertEqual({"workflow-run", "step-run:1", "action-run:1", "step-run:2", "action-run:2"},
                         {event["run"]["run_id"] for event in starts})
        second_visit = next(event for event in starts if event["run"]["run_id"] == "action-run:2")
        self.assertEqual("step-run:2", second_visit["run"]["parent_run_id"])
        workflow_start = next(event for event in starts if event["run"]["run_id"] == "workflow-run")
        bindings = workflow_start["definition_bindings"]
        self.assertEqual(3, len(bindings))
        self.assertEqual(
            len(bindings),
            len({(item["kind"], item["atom_id"], item["version"], item["path"]) for item in bindings}),
        )

    def test_conflicting_same_definition_identity_is_rejected_before_dispatch(self) -> None:
        with self.assertRaisesRegex(SelectedRunError, "conflicting exact Workflow bindings"):
            self._execute_request(self._request(second_step_digest="c"))

        self.assertEqual([], self.started)
        self.assertFalse(any((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")))


if __name__ == "__main__":
    unittest.main()
