"""Actual selected Step-input handoff proofs for O015 and O016."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
TESTS = Path(__file__).resolve().parent
TOOLS = APP.parents[1] / "201_TOOLS"
MCP = APP.parents[1] / "204_MCP"
PROMPTS = ROOT / "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW"
for location in (TESTS, MCP, APP, TOOLS, PROMPTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import implementation_actions  # noqa: E402
import work_journal  # noqa: E402
from selected_execution import SelectedExecution  # noqa: E402
from selected_routes import SelectedRouteAdapter  # noqa: E402
from selected_workflows_docker_fixture import FixtureLease, GoldenCase, GoldenProject  # noqa: E402


class SelectedStepInputsTest(unittest.TestCase):
    """No caller packet can supply a predecessor receipt to these Steps."""

    def _w06_fixture(self) -> tuple[FixtureLease, GoldenProject]:
        parent = ROOT / ".caprmedio_tmp" / "tests" / "selected-step-inputs"
        parent.mkdir(parents=True, exist_ok=True)
        project_root = Path(tempfile.mkdtemp(dir=parent))
        project = GoldenProject(ROOT, project_root, GoldenCase("W06", "rename_scope_unit"))
        project.prepare()
        return FixtureLease(project_root), project

    @staticmethod
    def _read(path: Path) -> dict[str, object]:
        return json.loads(path.read_text(encoding="utf-8"))

    def _frozen_w06(self, project: GoldenProject, request_id: str) -> tuple[SelectedExecution, dict[str, object]]:
        adapter = SelectedRouteAdapter(project.root)
        preview = adapter.invoke("rename_scope_unit", project.request(request_id=request_id))
        self.assertEqual("preview", preview["disposition"], preview)
        execute = project.request(
            request_id=request_id,
            mode="execute",
            receipt=preview["proposal_receipt"],
            receipt_digest=preview["proposal_receipt_digest"],
        )
        runner = SelectedExecution(project.root)
        frozen = runner.freeze({"operation": "enqueue_selected", "run_id": request_id, "execution": execute})
        return runner, frozen

    def test_w06_uses_sealed_o143_result_for_reference_changing_o144(self) -> None:
        lease, project = self._w06_fixture()
        try:
            structure = project.root / ".caprmedio_caprmedio/project_structure.toml"
            reference = project.root / "fixture/reference.txt"
            before_structure, before_reference = structure.read_bytes(), reference.read_bytes()
            runner, frozen = self._frozen_w06(project, "selected-step-inputs-w06")
            result = runner.dispatch(frozen)

            graph = self._read(runner.run_directory("selected-step-inputs-w06") / "graph_result.json")
            rows = {row["step_definition_id"]: row for row in graph["step_results"]}
            cutover = self._read(runner.run_directory("selected-step-inputs-w06") / f"{rows['CA-O-143']['action_run_id']}.json")
            reassessment = self._read(runner.run_directory("selected-step-inputs-w06") / f"{rows['CA-O-144']['action_run_id']}.json")
            terminals = {row["run_id"]: row for row in result["terminal_runs"]}
            cutover_receipt = terminals[rows["CA-O-143"]["action_run_id"]]

            self.assertEqual("terminal", result["disposition"], result)
            self.assertEqual("completed", graph["outcome"], graph)
            self.assertEqual(
                ["CA-O-139", "CA-O-140", "CA-O-141", "CA-O-142", "CA-O-143", "CA-O-144"],
                [row["step_definition_id"] for row in graph["step_results"]],
            )
            self.assertEqual("cutover completed", rows["CA-O-143"]["result"])
            self.assertEqual("checks complete", rows["CA-O-144"]["result"])
            self.assertEqual("completed", cutover_receipt["outcome"])
            self.assertEqual("terminal", cutover_receipt["disposition"])
            effects = cutover["native_result"]["actual_effects"]
            self.assertEqual(
                {".caprmedio_caprmedio/project_structure.toml", "fixture/reference.txt"},
                {effect["path"] for effect in effects},
            )
            self.assertEqual([effect["path"] for effect in effects], cutover_receipt["effect_refs"])
            structure_effect = next(effect for effect in effects if effect["path"] == ".caprmedio_caprmedio/project_structure.toml")
            self.assertEqual(cutover["native_result"]["pre_toml_revision"], structure_effect["before_sha256"])
            self.assertEqual(cutover["native_result"]["post_toml_revision"], structure_effect["after_sha256"])
            self.assertEqual("Rename", reassessment["native_result"]["operation"])
            self.assertNotEqual(before_structure, structure.read_bytes())
            self.assertNotEqual(before_reference, reference.read_bytes())
            self.assertEqual("RENAMED\n", reference.read_text(encoding="utf-8"))
        finally:
            lease.cleanup()

    def test_w06_failed_o143_seal_never_promotes_a_post_cutover_result(self) -> None:
        lease, project = self._w06_fixture()
        try:
            structure = project.root / ".caprmedio_caprmedio/project_structure.toml"
            runner, frozen = self._frozen_w06(project, "selected-step-inputs-w06-pending")
            append = work_journal.append_sealed_events

            def fail_cutover_terminal(*args: object, **kwargs: object) -> object:
                events = args[1]
                event = events[0] if isinstance(events, list) and events else {}
                if (event.get("event") == "completed"
                        and event.get("run", {}).get("definition", {}).get("atom_id") == "CA-O-014"):
                    raise OSError("fixture O143 receipt failure")
                return append(*args, **kwargs)

            with patch.object(work_journal, "append_sealed_events", side_effect=fail_cutover_terminal):
                pending = runner.dispatch(frozen)
            bytes_after_effect = structure.read_bytes()
            retry = runner.dispatch(frozen)
            graph = self._read(runner.run_directory("selected-step-inputs-w06-pending") / "graph_result.json")
            rows = {row["step_definition_id"]: row for row in graph["step_results"]}
            terminals = {row["run_id"]: row for row in pending["terminal_runs"]}

            self.assertEqual("recording_pending", pending["disposition"], pending)
            self.assertEqual("retry-recording-only", pending["retry_disposition"])
            self.assertEqual(pending, retry)
            self.assertEqual("recording_pending", terminals[rows["CA-O-143"]["action_run_id"]]["disposition"])
            self.assertEqual("completed", terminals[rows["CA-O-143"]["action_run_id"]]["outcome"])
            self.assertEqual("blocked", rows["CA-O-144"]["result"])
            self.assertEqual(bytes_after_effect, structure.read_bytes())
        finally:
            lease.cleanup()

    def test_o016_wrapper_supplies_its_selected_project_root(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "selected-project"
            for binding in implementation_actions._reviewed_binding_rows():
                source = ROOT / binding["path"]
                target = project / binding["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
            workspace = project / "disposable-workspace"
            workspace.mkdir()
            sources = implementation_actions.current_source_bindings(project)
            methods = [row["path"] for row in sources if row["atom_id"].startswith("CA-M-")]
            packet = {
                "context": "Isolated",
                "step_marker": "CA-O-093",
                "selected_project": {
                    "kind": "selected_project",
                    "source_root": ".caprmedio_caprmedio",
                    "source_references": sources,
                },
                "source_bindings": sources,
                "permissions": {"allowed": True, "implementation_workspace": {
                    "kind": "disposable_workspace", "path": str(workspace), "allow_write": True,
                }},
                "workspace": str(workspace),
                "method_projection": implementation_actions.prepare_method_projection(methods, project),
                "requirements_delivery": ["CA-R-1843", "CA-D-544"],
                "evaluations": ["CA-E-563"],
                "plan_item": {"estimated_minutes": 1},
                "handoff_complete": True,
                "retained_state": {},
            }
            calls: list[dict[str, object]] = []

            def agent(_prompt: str, supplied: dict[str, object]) -> dict[str, object]:
                calls.append(supplied)
                return {"result": "implemented", "outputs": {"candidate": "fixture", "changed_paths": ["x.py"]},
                        "evidence": ["performed"]}

            runner = SelectedExecution(project, implementation_agent=agent)
            output = runner.handlers["CA-O-019"]({"parameters": packet})

            self.assertEqual(project.resolve(), runner.root)
            self.assertNotEqual(project.resolve(), implementation_actions.ROOT.resolve())
            self.assertEqual("implementation delivered", output["result"])
            self.assertEqual([packet], calls)


if __name__ == "__main__":
    unittest.main()
