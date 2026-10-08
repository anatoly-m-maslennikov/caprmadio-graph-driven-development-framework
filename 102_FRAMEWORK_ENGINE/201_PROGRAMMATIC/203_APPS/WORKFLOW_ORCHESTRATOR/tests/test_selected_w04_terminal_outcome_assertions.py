"""Focused non-Docker guards for W04 terminal-outcome assertions."""
from __future__ import annotations

import asyncio
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest


TESTS = Path(__file__).resolve().parent
if str(TESTS) not in sys.path:
    sys.path.insert(0, str(TESTS))

from test_selected_workflows_docker_e2e import SelectedWorkflowsDockerEndToEnd


class _StatusFixture:
    case = SimpleNamespace(route="change_atom_status")

    @staticmethod
    def request_for_status(*_args: object, **_kwargs: object) -> dict[str, object]:
        return {"request": "status"}


class SelectedW04TerminalOutcomeAssertions(unittest.TestCase):
    _events = staticmethod(SelectedWorkflowsDockerEndToEnd._events)
    _safe_existing_ref = staticmethod(SelectedWorkflowsDockerEndToEnd._safe_existing_ref)

    def _assert_native_child_lineage(
        self, route_name: str, child_atom_id: str, *, expected_outcome: str, include_native_child: bool,
    ) -> None:
        request_id = f"{route_name}-{expected_outcome}"
        workflow = {"atom_id": "CA-O-127", "version": 1, "source_path": "definitions/workflow.md", "digest": "a" * 64}
        outer_step = {"atom_id": "CA-O-129", "version": 1, "source_path": "definitions/step.md", "digest": "b" * 64}
        outer_action = {"atom_id": "CA-O-128", "version": 1, "source_path": "definitions/action.md", "digest": "c" * 64}
        child = {"atom_id": child_atom_id, "version": 5, "source_path": f"definitions/{child_atom_id}.md", "digest": "d" * 64}
        ordered_steps = [{"step": outer_step, "action": outer_action}]
        if route_name == "update_atom":
            ordered_steps.insert(0, {
                "step": {"atom_id": "CA-O-145", "version": 1, "source_path": "definitions/update-step.md", "digest": "e" * 64},
                "action": {"atom_id": "CA-O-067", "version": 1, "source_path": "definitions/update-action.md", "digest": "f" * 64},
            })
        route = {
            "route": route_name,
            "workflow": workflow,
            "ordered_steps": ordered_steps,
            "native_action_calls": [child],
        }
        graph_rows = []
        run_pins = {request_id: workflow}
        parents = {request_id: None}
        for ordinal, binding in enumerate(ordered_steps, start=1):
            step_run_id = f"{request_id}:step:{ordinal}"
            action_run_id = f"{step_run_id}:action:1"
            graph_rows.append({
                "step_run_id": step_run_id,
                "action_run_id": action_run_id,
                "step_definition_id": binding["step"]["atom_id"],
                "action_definition_id": binding["action"]["atom_id"],
            })
            run_pins.update({step_run_id: binding["step"], action_run_id: binding["action"]})
            parents.update({step_run_id: request_id, action_run_id: step_run_id})
            if include_native_child and binding["action"]["atom_id"] == "CA-O-128":
                child_run_id = f"{action_run_id}:nested:{child_atom_id}"
                run_pins[child_run_id] = child
                parents[child_run_id] = action_run_id

        with tempfile.TemporaryDirectory(dir=Path.cwd() / ".caprmedio_tmp", ignore_cleanup_errors=True) as directory:
            root = Path(directory)
            journal = root / ".caprmedio_caprmedio/_journal"
            journal.mkdir(parents=True)
            events, terminals = [], []
            for run_id, pin in run_pins.items():
                for event_name, outcome in (("started", None), ("completed", expected_outcome)):
                    run = {"run_id": run_id, "definition": {
                        "atom_id": pin["atom_id"], "version": pin["version"],
                        "path": pin["source_path"], "digest": pin["digest"],
                    }}
                    if parents[run_id] is not None:
                        run["parent_run_id"] = parents[run_id]
                    events.append({"schema_version": 5, "kind": "workflow_execution", "event_id": f"{run_id}-{event_name}",
                                   "event": event_name, "outcome": outcome, "llm_session": {"uuid": request_id}, "run": run})
                result_ref = f"evidence/{run_id}.json"
                result = root / result_ref
                result.parent.mkdir(parents=True, exist_ok=True)
                result.write_text("{}", encoding="utf-8")
                terminals.append({"run_id": run_id, "disposition": "terminal", "outcome": expected_outcome,
                                  "result_ref": result_ref, "effect_refs": []})
            (journal / "runs.ndjson").write_text("\n".join(json.dumps(event) for event in events) + "\n", encoding="utf-8")
            selected = {"disposition": "terminal", "run_ids": list(run_pins), "terminal_runs": terminals}
            graph = {"step_results": graph_rows}
            SelectedWorkflowsDockerEndToEnd._assert_shared_run_journal(
                self, root, request_id, route, selected, graph, expected_outcome=expected_outcome,
            )

    def test_current_w02_child_pin_and_applied_lineage(self) -> None:
        repository = TESTS.parents[4]
        manifest = json.loads((repository / ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json").read_text())
        routes = {route["route"]: route for route in manifest["routes"]}
        self.assertEqual(["CA-O-030"], [item["atom_id"] for item in routes["update_atom"]["native_action_calls"]])
        self._assert_native_child_lineage(
            "update_atom", "CA-O-030", expected_outcome="completed", include_native_child=True,
        )

    def test_generic_w04_applied_status_does_not_require_archive_shortcut_child(self) -> None:
        self._assert_native_child_lineage(
            "change_atom_status", "CA-O-029", expected_outcome="completed", include_native_child=False,
        )

    def test_w04_noop_does_not_require_status_native_child(self) -> None:
        self._assert_native_child_lineage(
            "change_atom_status", "CA-O-029", expected_outcome="no_op", include_native_child=False,
        )

    def test_noop_probe_rejects_completed_terminal(self) -> None:
        harness = SelectedWorkflowsDockerEndToEnd(methodName="runTest")
        calls = iter((
            {"disposition": "preview", "proposal_receipt": "receipt", "proposal_receipt_digest": "digest"},
            {"outcome": "queued"},
        ))

        async def call(*_args: object, **_kwargs: object) -> dict[str, object]:
            return next(calls)

        async def terminal(*_args: object, **_kwargs: object) -> dict[str, object]:
            return {"disposition": "terminal", "outcome": "completed"}

        harness._call = call  # type: ignore[method-assign]
        harness._terminal_status = terminal  # type: ignore[method-assign]
        with self.assertRaises(AssertionError):
            asyncio.run(
                harness._execute_status_case(
                    None, Path.cwd(), _StatusFixture(), Path("carrier.md"), "Archived", "w04-noop",
                    expected_outcome="no_op",
                )
            )


if __name__ == "__main__":
    unittest.main()
