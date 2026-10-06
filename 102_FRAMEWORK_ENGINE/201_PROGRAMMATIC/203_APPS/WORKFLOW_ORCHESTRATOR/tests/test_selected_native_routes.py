"""Native selected-route proof through one real shared-recorder session.

The fixture is deliberately disposable.  This suite does not use the queue,
MCP image, a synthetic Action result, or an independently manufactured Run
receipt: a SelectedRouteAdapter makes the preview and SelectedExecution uses
its current native handlers and shared Run recorder to execute the frozen
request.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from typing import Any, Mapping


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
TESTS = Path(__file__).resolve().parent
MCP = APP.parents[1] / "204_MCP"
for location in (TESTS, MCP, APP):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_execution import SelectedExecution  # noqa: E402
from selected_routes import SelectedRouteAdapter  # noqa: E402
from selected_workflows_docker_fixture import FixtureLease, GoldenCase, GoldenProject  # noqa: E402


# W09's Agent path and W10's governed reversal service have separately declared
# gates.  The two query routes are W14 and W15 even though the fixture's legacy
# ROUTE_CASES collection is restricted to the thirteen mutation/projection rows.
READY_CASES = (
    ("W01", "create_atom"),
    ("W02", "update_atom"),
    ("W03", "replace_atom"),
    ("W04", "change_atom_status"),
    ("W05", "create_scope_unit"),
    ("W06", "rename_scope_unit"),
    ("W07", "move_scope_unit"),
    ("W08", "remove_scope_unit"),
    ("W11", "build_entities_graph"),
    ("W12", "build_terms_graph"),
    ("W13", "build_applicable_methodology"),
    ("W14", "find_and_fetch_artifacts"),
    ("W15", "find_and_fetch_journal_events"),
)


class SelectedNativeRoutesTest(unittest.TestCase):
    """Each subtest is one current source-bound Project and recorder lineage."""

    def _fixture(self, case_id: str, route: str) -> tuple[FixtureLease, GoldenProject]:
        parent = ROOT / ".caprmedio_tmp" / "tests" / "selected-native-routes"
        parent.mkdir(parents=True, exist_ok=True)
        project_root = Path(tempfile.mkdtemp(dir=parent))
        project = GoldenProject(ROOT, project_root, GoldenCase(case_id, route))
        project.prepare()
        return FixtureLease(project_root), project

    @staticmethod
    def _route_binding(project: GoldenProject) -> dict[str, Any]:
        if project.manifest is None:
            raise AssertionError("GoldenProject did not retain its source-pinned manifest")
        route = next(
            (row for row in project.manifest["routes"] if row.get("route") == project.case.route),
            None,
        )
        if not isinstance(route, dict):
            raise AssertionError(f"manifest has no binding for {project.case.route}")
        return route

    def _read_json(self, path: Path, label: str) -> dict[str, Any]:
        self.assertTrue(path.is_file(), f"{label} is absent: {path}")
        value = json.loads(path.read_text(encoding="utf-8"))
        self.assertIsInstance(value, dict, f"{label} is not an object: {path}")
        return value

    def _source_bytes(self, root: Path, reference: object, label: str) -> bytes:
        self.assertIsInstance(reference, str, f"{label} must be a source-relative reference")
        relative = Path(reference)
        self.assertFalse(relative.is_absolute() or ".." in relative.parts, f"{label} escapes Project")
        path = root / relative
        self.assertTrue(path.is_file(), f"{label} does not exist: {reference}")
        value = path.read_bytes()
        self.assertTrue(value, f"{label} is empty: {reference}")
        return value

    def _events(self, root: Path, request_id: str) -> list[dict[str, Any]]:
        journal = root / ".caprmedio_caprmedio" / "_journal"
        return [
            json.loads(line)
            for path in sorted(journal.glob("*.ndjson"))
            for line in path.read_text(encoding="utf-8").splitlines()
            if line and json.loads(line).get("llm_session", {}).get("uuid") == request_id
        ]

    @staticmethod
    def _definition(pin: Mapping[str, Any]) -> dict[str, Any]:
        return {
            "atom_id": pin["atom_id"],
            "version": pin["version"],
            "path": pin["source_path"],
            "digest": pin["digest"],
        }

    def _assert_shared_lineage(
        self,
        root: Path,
        request_id: str,
        route: Mapping[str, Any],
        result: Mapping[str, Any],
        graph: Mapping[str, Any],
    ) -> None:
        """Verify actual Workflow/Step/Action facts, not marker-file presence."""
        rows = graph.get("step_results")
        self.assertIsInstance(rows, list, graph)
        self.assertTrue(rows, graph)
        expected: dict[str, tuple[dict[str, Any], str | None]] = {
            request_id: (self._definition(route["workflow"]), None),
        }
        by_step = {item["step"]["atom_id"]: item for item in route["ordered_steps"]}
        for row in rows:
            self.assertIsInstance(row, dict, graph)
            binding = by_step.get(row.get("step_definition_id"))
            self.assertIsInstance(binding, dict, row)
            self.assertEqual(binding["action"]["atom_id"], row.get("action_definition_id"), row)
            step_id, action_id = row.get("step_run_id"), row.get("action_run_id")
            self.assertIsInstance(step_id, str, row)
            self.assertIsInstance(action_id, str, row)
            expected[step_id] = (self._definition(binding["step"]), request_id)
            expected[action_id] = (self._definition(binding["action"]), step_id)

        self.assertEqual(set(expected), set(result.get("run_ids", [])), result)
        terminal = result.get("terminal_runs")
        self.assertIsInstance(terminal, list, result)
        terminals = {item.get("run_id"): item for item in terminal if isinstance(item, Mapping)}
        self.assertEqual(set(expected), set(terminals), terminal)
        for run_id, (definition, parent) in expected.items():
            receipt = terminals[run_id]
            self.assertEqual("terminal", receipt.get("disposition"), receipt)
            self.assertEqual("completed", receipt.get("outcome"), receipt)
            self._source_bytes(root, receipt.get("result_ref"), "terminal result")
            for effect in receipt.get("effect_refs", []):
                self._source_bytes(root, effect, "terminal effect")

            facts = [item for item in self._events(root, request_id) if item.get("run", {}).get("run_id") == run_id]
            self.assertEqual(["started", "completed"], [item.get("event") for item in facts], facts)
            self.assertEqual([None, "completed"], [item.get("outcome") for item in facts], facts)
            for fact in facts:
                self.assertEqual(definition, fact["run"].get("definition"), fact)
                if parent is None:
                    self.assertNotIn("parent_run_id", fact["run"], fact)
                else:
                    self.assertEqual(parent, fact["run"].get("parent_run_id"), fact)

        events = self._events(root, request_id)
        self.assertEqual(2 * len(expected), len(events), events)
        self.assertEqual(len(events), len({item.get("event_id") for item in events}), events)

    def _assert_declared_path_and_progress(
        self, root: Path, runner: SelectedExecution, request_id: str, route: Mapping[str, Any], graph: Mapping[str, Any],
    ) -> list[dict[str, Any]]:
        self.assertEqual(request_id, graph.get("workflow_run_id"), graph)
        self.assertEqual(route["workflow"]["atom_id"], graph.get("workflow_definition_id"), graph)
        rows = graph.get("step_results")
        self.assertIsInstance(rows, list, graph)
        self.assertTrue(rows, graph)
        self.assertEqual(route["entry_step"], rows[0].get("step_definition_id"), rows)
        transitions = {(edge["from"], edge["condition"]): edge["to"] for edge in route["on_result"]}
        progress_rows: list[dict[str, Any]] = []
        for index, row in enumerate(rows):
            self.assertIsInstance(row, dict, graph)
            progress = self._read_json(
                runner.run_directory(request_id) / f"{row['action_run_id']}.json", "native Action progress",
            )
            progress_rows.append(progress)
            self.assertEqual(row["action_run_id"], progress.get("action_run_id"), progress)
            self.assertEqual(row["result"], progress.get("result"), progress)
            for effect in row.get("effect_refs", []):
                self._source_bytes(root, effect, "native Action effect")
            transition = transitions.get((row["step_definition_id"], row["result"]))
            if index + 1 < len(rows):
                self.assertEqual(rows[index + 1]["step_definition_id"], transition, {"row": row, "route": route})
            elif transition is not None:
                self.assertEqual("complete", transition, {"row": row, "route": route})
            else:
                # The frozen source binding has no edge for this final native
                # result.  It may only be terminal because the real adapter
                # supplied a terminal outcome; it can never infer a successor.
                self.assertEqual(index + 1, len(rows), {"row": row, "route": route})
        self.assertEqual(
            "completed", graph.get("outcome"),
            {"graph": graph, "terminal_native_result": progress_rows[-1].get("native_result")},
        )
        return rows

    def _assert_route_effect(
        self,
        project: GoldenProject,
        runner: SelectedExecution,
        request_id: str,
        before: Mapping[str, str],
        rows: list[dict[str, Any]],
    ) -> None:
        root, case = project.root, project.case.case_id
        effects = sorted({effect for row in rows for effect in row.get("effect_refs", [])})
        progress = self._read_json(
            runner.run_directory(request_id) / f"{rows[-1]['action_run_id']}.json", "terminal native Action progress",
        )
        native = progress.get("native_result")
        if case in {"W01", "W02", "W03", "W04"}:
            self.assertIsInstance(native, dict, progress)
            self.assertEqual("applied", native.get("outcome"), native)
            self.assertTrue(native.get("effects"), native)
            self.assertTrue(effects, rows)
            self.assertNotEqual(before, project.snapshot(), "lifecycle success did not alter source authority")
        elif case in {"W05", "W06", "W07", "W08"}:
            self.assertTrue(effects, rows)
            self.assertNotEqual(before, project.snapshot(), "structure success did not alter its source authority")
            self.assertIn("scope_units", (root / ".caprmedio_caprmedio/project_structure.toml").read_text(encoding="utf-8"))
        elif case in {"W11", "W12"}:
            self.assertTrue(effects, rows)
            for effect in effects:
                projection = json.loads(self._source_bytes(root, effect, "graph projection"))
                self.assertIs(True, projection.get("non_authoritative"), projection)
                self.assertTrue(projection.get("source_frontier_evidence"), projection)
        elif case == "W13":
            self.assertTrue(effects, rows)
            for effect in effects:
                self._source_bytes(root, effect, "compiled methodology projection")
            self.assertIsInstance(native, dict, progress)
            self.assertTrue(native.get("source_frontier_digest"), native)
            self.assertTrue(
                (root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
                 "000_APPLICABLE_MTHD_sources/002_INSTALLED_EXTENSIONS/example/v2/05_method/CA-M-302--extension.md").read_bytes()
            )
            self.assertTrue(
                (root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
                 "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-303--project.md").read_bytes()
            )
        elif case == "W14":
            self.assertEqual([], effects, rows)
            self.assertEqual(before, project.snapshot(), "artifact query mutated authority")
            self.assertIsInstance(native, dict, progress)
            self.assertTrue(native.get("snapshot", {}).get("digest"), native)
            self.assertTrue(native.get("coverage", {}).get("complete"), native)
            self.assertTrue(all(set(item) == {"artifact_id"} for item in native.get("results", [])), native)
        elif case == "W15":
            self.assertEqual([], effects, rows)
            self.assertEqual(before, project.snapshot(), "Journal query mutated authority")
            self.assertIsInstance(native, dict, progress)
            self.assertIn(native.get("status"), {"complete", "incomplete"}, native)
            snapshot = native.get("snapshot")
            self.assertIsInstance(snapshot, dict, native)
            own_event_ids = {item.get("event_id") for item in self._events(root, request_id)}
            self.assertTrue(set(snapshot.get("event_ids", [])).isdisjoint(own_event_ids), native)
            self.assertTrue(all(isinstance(item, str) for item in native.get("results", [])), native)
        else:  # pragma: no cover - a route addition must receive explicit evidence rules.
            self.fail(f"no route-specific native effect assertion exists for {case}")

    def test_ready_native_routes_preview_freeze_and_record_actual_effects(self) -> None:
        for case_id, route_name in READY_CASES:
            with self.subTest(case=case_id):
                lease, project = self._fixture(case_id, route_name)
                try:
                    before = project.snapshot()
                    adapter = SelectedRouteAdapter(project.root)
                    request_id = f"selected-native-{case_id.lower()}"
                    preview = adapter.invoke(route_name, project.request(request_id=request_id))
                    self.assertEqual("preview", preview.get("disposition"), preview)
                    self.assertEqual(before, project.snapshot(), "preview changed source authority")

                    execute = project.request(
                        request_id=request_id,
                        mode="execute",
                        receipt=preview["proposal_receipt"],
                        receipt_digest=preview["proposal_receipt_digest"],
                    )
                    runner = SelectedExecution(project.root)
                    frozen = runner.freeze({
                        "operation": "enqueue_selected", "run_id": request_id, "execution": execute,
                    })
                    result = runner.dispatch(frozen)
                    graph = self._read_json(
                        runner.run_directory(request_id) / "graph_result.json", "selected graph result",
                    )
                    route = self._route_binding(project)
                    rows = self._assert_declared_path_and_progress(project.root, runner, request_id, route, graph)
                    self.assertEqual("terminal", result.get("disposition"), {"result": result, "graph": graph})
                    self._assert_shared_lineage(project.root, request_id, route, result, graph)
                    self._assert_route_effect(project, runner, request_id, before, rows)
                    if case_id == "W02":
                        self.assertEqual(["CA-O-145", "CA-O-129"], [row["step_definition_id"] for row in rows])
                        assessment = self._read_json(
                            runner.run_directory(request_id) / f"{rows[0]['action_run_id']}.json",
                            "O145 assessment progress",
                        )["native_result"].get("assessment")
                        self.assertIsInstance(assessment, dict)
                        self.assertRegex(assessment.get("request_digest", ""), r"^[0-9a-f]{64}$")
                        self.assertEqual("semantic_revision", assessment.get("admitted_change_class"))
                        comparison = assessment.get("comparison")
                        self.assertIsInstance(comparison, dict)
                        self.assertEqual("CA-R-100", comparison.get("target", {}).get("atom_id"))
                        self.assertTrue(comparison.get("report", {}).get("digest"))
                        self.assertTrue(comparison.get("primary_claim_identity_preserved"))
                        applied = self._read_json(
                            runner.run_directory(request_id) / f"{rows[1]['action_run_id']}.json",
                            "O129 update progress",
                        )["native_result"]
                        self.assertEqual(assessment, applied.get("assessment"))
                finally:
                    lease.cleanup()

    def test_graph_effect_is_retained_when_its_action_terminal_recording_is_pending(self) -> None:
        """W11 shares the W11/W12 recorder boundary without replaying an effect."""
        lease, project = self._fixture("W11", "build_entities_graph")
        try:
            tools_root = APP.parents[1] / "201_TOOLS"
            if str(tools_root) not in sys.path:
                sys.path.insert(0, str(tools_root))
            import work_journal

            request_id = "selected-native-w11-terminal-pending"
            adapter = SelectedRouteAdapter(project.root)
            preview = adapter.invoke("build_entities_graph", project.request(request_id=request_id))
            execute = project.request(
                request_id=request_id,
                mode="execute",
                receipt=preview["proposal_receipt"],
                receipt_digest=preview["proposal_receipt_digest"],
            )
            runner = SelectedExecution(project.root)
            frozen = runner.freeze({
                "operation": "enqueue_selected", "run_id": request_id, "execution": execute,
            })
            append = work_journal.append_sealed_events

            def fail_only_action_terminal(*args: object, **kwargs: object) -> object:
                events = args[1]
                assert isinstance(events, list) and len(events) == 1
                event = events[0]
                if event["run"]["kind"] == "action" and event["event"] != "started":
                    raise OSError("fixture Action terminal Journal failure")
                return append(*args, **kwargs)

            with patch.object(work_journal, "append_sealed_events", side_effect=fail_only_action_terminal):
                pending = runner.dispatch(frozen)

            self.assertEqual("recording_pending", pending.get("disposition"), pending)
            graph = self._read_json(runner.run_directory(request_id) / "graph_result.json", "selected graph result")
            self.assertEqual("interrupted_pending", graph.get("outcome"), graph)
            row = graph["step_results"][0]
            self.assertEqual("recording_pending", row.get("result"), row)
            self.assertTrue(row.get("effect_refs"), row)
            for effect in row["effect_refs"]:
                self._source_bytes(project.root, effect, "retained graph effect")
            self.assertEqual(pending, runner.dispatch(frozen), "pending effect must not be replayed")
        finally:
            lease.cleanup()


if __name__ == "__main__":
    unittest.main()
