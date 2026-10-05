"""One real native W10 selected-route proof; no MCP or image harness."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import time
import unittest


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
for path in (APP, APP / "tests", APP.parents[1] / "204_MCP"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from selected_execution import SelectedExecution
from selected_native_providers import SelectedNativeProviders
from selected_routes import SelectedRouteAdapter
from selected_workflows_docker_fixture import FixtureLease, GoldenCase, GoldenProject


class SelectedNativeRevertRouteTest(unittest.TestCase):
    def test_w10_preview_freeze_dispatch_rolls_back_exact_pinned_bytes(self) -> None:
        parent = ROOT / ".caprmedio_tmp" / "tests" / "selected-native-revert-route"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent))
        lease = FixtureLease(root)
        project = GoldenProject(ROOT, root, GoldenCase("W10", "revert_changes"))
        try:
            project.prepare()
            adapter = SelectedRouteAdapter(root)
            request_id = "selected-native-w10"
            preview_request = project.request(request_id=request_id)
            preview = adapter.invoke("revert_changes", preview_request)
            self.assertEqual("preview", preview.get("disposition"), preview)
            time.sleep(1.05)

            execute = project.request(
                request_id=request_id,
                mode="execute",
                receipt=preview["proposal_receipt"],
                receipt_digest=preview["proposal_receipt_digest"],
            )
            request = execute["parameters"]["approved_reversal_manifest"]["request"]
            boundary = request["ordered_effects"][0]["capability_binding"]["parameters"]["recovery_boundary"]
            path = root / boundary["toml"]["path"]
            before_dispatch_bytes = path.read_bytes()
            self.assertNotEqual(boundary["toml"]["before_text"].encode("utf-8"), before_dispatch_bytes)

            frozen = SelectedExecution(root).freeze(
                {"operation": "enqueue_selected", "run_id": request_id, "execution": execute}
            )
            result = SelectedNativeProviders(root).dispatch(request_id)
            self.assertEqual("terminal", result.get("disposition"), result)
            self.assertEqual(boundary["toml"]["before_text"].encode("utf-8"), path.read_bytes())

            graph_path = SelectedExecution(root).run_directory(request_id) / "graph_result.json"
            graph = json.loads(graph_path.read_text(encoding="utf-8"))
            self.assertEqual("completed", graph.get("outcome"), graph)
            self.assertEqual(["CA-O-132"], [row["step_definition_id"] for row in graph["step_results"]])
            self.assertEqual(["CA-O-131"], [row["action_definition_id"] for row in graph["step_results"]])
            self.assertEqual(["reverted"], [row["result"] for row in graph["step_results"]])

            events = []
            for journal in sorted((root / ".caprmedio_caprmedio" / "_journal").glob("*.ndjson")):
                events.extend(json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines() if line)
            events = [event for event in events if event.get("llm_session", {}).get("uuid") == request_id]
            runs = {event.get("run", {}).get("run_id"): [] for event in events}
            for event in events:
                runs[event["run"]["run_id"]].append(event)
            self.assertEqual(3, len(runs), events)
            by_definition = {facts[0]["run"]["definition"]["atom_id"]: facts for facts in runs.values()}
            self.assertEqual({"CA-O-130", "CA-O-132", "CA-O-131"}, set(by_definition), by_definition)
            workflow_run = by_definition["CA-O-130"][0]["run"]["run_id"]
            step_run = by_definition["CA-O-132"][0]["run"]["run_id"]
            self.assertNotIn("parent_run_id", by_definition["CA-O-130"][0]["run"])
            self.assertEqual(workflow_run, by_definition["CA-O-132"][0]["run"].get("parent_run_id"))
            self.assertEqual(step_run, by_definition["CA-O-131"][0]["run"].get("parent_run_id"))
            for facts in runs.values():
                self.assertEqual(["started", "completed"], [fact.get("event") for fact in facts], facts)
                self.assertEqual([None, "completed"], [fact.get("outcome") for fact in facts], facts)
        finally:
            lease.cleanup()

    def test_w10_revoked_decision_blocks_without_rollback_effect(self) -> None:
        parent = ROOT / ".caprmedio_tmp" / "tests" / "selected-native-revert-route"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent))
        lease = FixtureLease(root)
        project = GoldenProject(ROOT, root, GoldenCase("W10", "revert_changes"))
        try:
            project.prepare()
            adapter = SelectedRouteAdapter(root)
            request_id = "selected-native-w10-revoked"
            preview = adapter.invoke("revert_changes", project.request(request_id=request_id))
            self.assertEqual("preview", preview.get("disposition"), preview)
            execute = project.request(request_id=request_id, mode="execute",
                                      receipt=preview["proposal_receipt"],
                                      receipt_digest=preview["proposal_receipt_digest"])
            request = execute["parameters"]["approved_reversal_manifest"]["request"]
            rollback = root / request["ordered_effects"][0]["capability_binding"]["parameters"]["recovery_boundary"]["toml"]["path"]
            expected_partial = rollback.read_bytes()
            decision = root / request["operator_decision"]["evidence_ref"]
            record = json.loads(decision.read_text(encoding="utf-8"))
            record["status"] = "revoked"
            decision.write_text(json.dumps(record, sort_keys=True, separators=(",", ":")), encoding="utf-8")

            frozen = SelectedExecution(root).freeze(
                {"operation": "enqueue_selected", "run_id": request_id, "execution": execute}
            )
            result = SelectedNativeProviders(root).dispatch(request_id)
            self.assertEqual("started", result.get("disposition"), result)
            self.assertEqual(expected_partial, rollback.read_bytes())
            self.assertEqual(3, len(result.get("terminal_runs", [])), result)
            self.assertTrue(all(run.get("outcome") == "interrupted_pending"
                                for run in result["terminal_runs"]), result)
        finally:
            lease.cleanup()


if __name__ == "__main__":
    unittest.main()
