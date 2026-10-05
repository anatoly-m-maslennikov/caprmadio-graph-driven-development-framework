"""Functional W09 proof through the selected preview, queue, and shared recorder."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock
from typing import Any, Callable


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
MCP = APP.parents[1] / "204_MCP"
PROMPTS = APP.parents[2] / "202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW"
for location in (APP, APP / "tests", MCP, PROMPTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import implementation_actions  # noqa: E402
from implementation_mock_agent import CANDIDATE, CANDIDATE_TEXT, TEST, ImplementationMockAgent, TRANSPORT  # noqa: E402
from selected_execution import SelectedExecution  # noqa: E402
from selected_routes import SelectedRouteAdapter, canonical_digest  # noqa: E402
from selected_workflows_docker_fixture import FixtureLease, GoldenCase, GoldenProject  # noqa: E402


class SelectedNativeImplementationRouteTest(unittest.TestCase):
    """W09 is a disposable mock transport proof, never a live model invocation."""

    def _fixture(self) -> tuple[FixtureLease, GoldenProject]:
        parent = ROOT / ".caprmedio_tmp/tests/selected-native-implementation-route"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent))
        fixture = GoldenProject(ROOT, root, GoldenCase("W09", "run_implementation_workflow"))
        fixture.prepare()
        return FixtureLease(root), fixture

    @staticmethod
    def _json(path: Path) -> dict[str, object]:
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise AssertionError(f"expected object at {path}")
        return value

    @staticmethod
    def _digest(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def _preview_and_execute(
        self,
        fixture: GoldenProject,
        request_id: str,
        *,
        mutate_parameters: Callable[[dict[str, Any]], None] | None = None,
    ) -> tuple[dict[str, object], dict[str, object]]:
        adapter = SelectedRouteAdapter(fixture.root)
        preview_request = fixture.request(request_id=request_id)
        if mutate_parameters is not None:
            mutate_parameters(preview_request["parameters"])
            preview_request["parameters_digest"] = canonical_digest(preview_request["parameters"])
        preview = adapter.invoke("run_implementation_workflow", preview_request)
        self.assertEqual("preview", preview.get("disposition"), preview)

        execute = fixture.request(
            request_id=request_id,
            mode="execute",
            receipt=preview["proposal_receipt"],
            receipt_digest=preview["proposal_receipt_digest"],
        )
        if mutate_parameters is not None:
            execute["parameters"] = copy.deepcopy(preview_request["parameters"])
            execute["parameters_digest"] = preview_request["parameters_digest"]
            execute["operator_authorization"]["parameters_digest"] = execute["parameters_digest"]
        return preview, execute

    def _journal_events(self, fixture: GoldenProject, request_id: str) -> list[dict[str, object]]:
        events: list[dict[str, object]] = []
        for path in sorted((fixture.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")):
            for line in path.read_text(encoding="utf-8").splitlines():
                if line:
                    event = json.loads(line)
                    if event.get("llm_session", {}).get("uuid") == request_id:
                        events.append(event)
        return events

    def test_w09_runs_test_first_mock_workflow_through_preview_freeze_dispatch_and_shared_recorder(self) -> None:
        lease, fixture = self._fixture()
        try:
            request_id = "selected-native-w09"
            preview_request = fixture.request(request_id=request_id)
            before_preview = fixture.snapshot()
            adapter = SelectedRouteAdapter(fixture.root)
            preview = adapter.invoke("run_implementation_workflow", preview_request)
            self.assertEqual("preview", preview.get("disposition"), preview)
            self.assertEqual(before_preview, fixture.snapshot(), "preview changed the selected Project")

            execute = fixture.request(
                request_id=request_id,
                mode="execute",
                receipt=preview["proposal_receipt"],
                receipt_digest=preview["proposal_receipt_digest"],
            )
            parameters = execute["parameters"]
            base = parameters["base_packet"]
            self.assertEqual(
                implementation_actions.current_source_bindings(fixture.root),
                base["selected_project"]["source_references"],
            )
            for binding in base["source_bindings"]:
                source = fixture.root / binding["path"]
                self.assertTrue(source.is_file(), binding)
                self.assertEqual(binding["sha256"], self._digest(source), binding)

            runner = SelectedExecution(fixture.root, implementation_agent=ImplementationMockAgent(fixture.root))
            frozen = runner.freeze({"operation": "enqueue_selected", "run_id": request_id, "execution": execute})
            declared_o091 = [
                row for row in execute["requested_runs"]
                if row.get("kind") == "step" and row.get("definition", {}).get("atom_id") == "CA-O-091"
            ]
            self.assertEqual(
                [f"{request_id}:step:1", *(f"{request_id}:step:1:visit:{visit}" for visit in range(2, 5))],
                [row["requested_run_id"] for row in declared_o091],
            )

            with mock.patch("implementation_agent._run", side_effect=AssertionError("live CLI must not run")):
                result = runner.dispatch(frozen)
            self.assertEqual("terminal", result.get("disposition"), result)
            self.assertNotIn("execution_error", result)

            run_dir = runner.run_directory(request_id)
            graph = self._json(run_dir / "graph_result.json")
            rows = graph["step_results"]
            self.assertEqual("completed", graph["outcome"])
            self.assertEqual(
                [("CA-O-091", "evaluation ready"), ("CA-O-092", "tests prepared"),
                 ("CA-O-093", "implementation delivered"), ("CA-O-094", "checks pass")],
                [(row["step_definition_id"], row["result"]) for row in rows],
            )
            progress = {row["action_definition_id"]: self._json(run_dir / f"{row['action_run_id']}.json") for row in rows}
            prepared = progress["CA-O-018"]["native_result"]
            baseline = next(item for item in prepared["evidence"] if isinstance(item, dict) and "returncode" in item)
            self.assertEqual(TRANSPORT, baseline["transport"])
            self.assertNotEqual(0, baseline["returncode"], "test-first baseline unexpectedly passed")
            workspace = Path(base["workspace"])
            self.assertEqual(CANDIDATE_TEXT, (workspace / CANDIDATE).read_text(encoding="utf-8"))
            self.assertTrue((workspace / TEST).is_file())
            passed = progress["CA-O-020"]["native_result"]
            self.assertEqual(0, passed["outputs"]["checks"][0]["returncode"])

            expected_runs = {row["requested_run_id"]: row for row in execute["requested_runs"]}
            actual_run_ids = {graph["workflow_run_id"]}
            for row in rows:
                actual_run_ids.update({row["step_run_id"], row["action_run_id"]})
            events = self._journal_events(fixture, request_id)
            self.assertEqual(2 * len(actual_run_ids), len(events))
            all_bindings = {
                json.dumps({"kind": row["kind"], **row["definition"]}, sort_keys=True)
                for row in expected_runs.values()
            }
            for run_id in actual_run_ids:
                receipts = [event for event in events if event["run"]["run_id"] == run_id]
                self.assertEqual({"started", "completed"}, {event["event"] for event in receipts}, receipts)
                expected = expected_runs[run_id]
                own_binding = {"kind": expected["kind"], **expected["definition"]}
                for receipt in receipts:
                    self.assertEqual(expected["definition"], receipt["run"]["definition"], receipt)
                    if expected["kind"] == "workflow":
                        self.assertEqual(all_bindings, {json.dumps(item, sort_keys=True) for item in receipt["definition_bindings"]})
                    else:
                        self.assertEqual([own_binding], receipt["definition_bindings"], receipt)
                    self.assertEqual(None if receipt["event"] == "started" else "completed", receipt["outcome"], receipt)
            self.assertEqual({"completed"}, {row["outcome"] for row in result["terminal_runs"]})
        finally:
            lease.cleanup()

    def test_w09_denies_missing_permission_before_mock_transport(self) -> None:
        lease, fixture = self._fixture()
        try:
            _, execute = self._preview_and_execute(
                fixture, "selected-native-w09-permission",
                mutate_parameters=lambda parameters: parameters["base_packet"]["permissions"].update(allowed=False),
            )
            runner = SelectedExecution(
                fixture.root,
                implementation_agent=lambda *_args: (_ for _ in ()).throw(AssertionError("mock must not run")),
            )
            result = runner.dispatch(runner.freeze({
                "operation": "enqueue_selected", "run_id": "selected-native-w09-permission", "execution": execute,
            }))
            self.assertEqual("started", result.get("disposition"), result)
            workspace = Path(execute["parameters"]["base_packet"]["workspace"])
            self.assertEqual([], list(workspace.iterdir()))
        finally:
            lease.cleanup()

    def test_w09_denies_stale_selected_project_source_before_mock_transport(self) -> None:
        lease, fixture = self._fixture()
        try:
            request_id = "selected-native-w09-source"
            _, execute = self._preview_and_execute(fixture, request_id)
            runner = SelectedExecution(
                fixture.root,
                implementation_agent=lambda *_args: (_ for _ in ()).throw(AssertionError("mock must not run")),
            )
            frozen = runner.freeze({"operation": "enqueue_selected", "run_id": request_id, "execution": execute})
            binding = execute["parameters"]["base_packet"]["source_bindings"][0]
            source = fixture.root / binding["path"]
            source.write_bytes(source.read_bytes() + b"\nstale after queue admission\n")
            result = runner.dispatch(frozen)
            self.assertEqual("started", result.get("disposition"), result)
            workspace = Path(execute["parameters"]["base_packet"]["workspace"])
            self.assertEqual([], list(workspace.iterdir()))
        finally:
            lease.cleanup()


if __name__ == "__main__":
    unittest.main()
