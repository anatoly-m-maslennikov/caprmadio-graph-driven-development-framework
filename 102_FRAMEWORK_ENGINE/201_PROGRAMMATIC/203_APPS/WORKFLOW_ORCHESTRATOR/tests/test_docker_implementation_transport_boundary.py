"""Executable proof of the explicit, permission-bound Docker mock callback."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import MagicMock, patch


APP = Path(__file__).resolve().parents[1]
REPOSITORY = APP.parents[3]
PROMPTS = REPOSITORY / "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW"
for location in (APP, APP / "tests", PROMPTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import backend  # noqa: E402
from implementation_agent import ImplementationAgent  # noqa: E402
import implementation_actions  # noqa: E402
from implementation_mock_agent import CANDIDATE, TEST, ImplementationMockAgent, TRANSPORT  # noqa: E402
from runtime_config import implementation_mock_runtime  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402


class DockerImplementationTransportBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.workspace = self.root / "disposable-implementation"
        self.workspace.mkdir()
        self.agent = ImplementationMockAgent(self.root)

    def packet(self, step: str = "CA-O-091") -> dict:
        return {"workspace": str(self.workspace), "step_marker": step,
                "context": "Isolated" if step in {"CA-O-092", "CA-O-093"} else "Integrated",
                "permissions": {"allowed": True, "implementation_workspace": {
                    "kind": "disposable_workspace", "path": str(self.workspace), "allow_write": True}},
                "prior_results": []}

    def call(self, step: str, packet: dict | None = None) -> dict:
        return self.agent((PROMPTS / f"{step}.prompt.md").read_text(), packet or self.packet(step))

    def test_explicit_mock_startup_preserves_default_live_transport_and_mount_boundary(self) -> None:
        override = (APP / "docker/mock.compose.yaml").read_text()
        self.assertIn("worker:\n    environment:\n      CAPRMEDIO_AGENT_MODE: mock", override)
        self.assertNotIn("volumes:", override)
        self.assertNotIn("secrets:", override)
        self.assertNotIn("ports:", override)
        for mode, expected in (("", False), ("codex", False), ("mock", True)):
            with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "docker", "CAPRMEDIO_AGENT_MODE": mode}):
                self.assertEqual(expected, implementation_mock_runtime())
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "", "CAPRMEDIO_AGENT_MODE": "mock"}):
            with self.assertRaisesRegex(ValueError, "explicit Docker"):
                implementation_mock_runtime()
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "docker", "CAPRMEDIO_AGENT_MODE": "arbitrary"}):
            with self.assertRaisesRegex(ValueError, "Unsupported"):
                implementation_mock_runtime()

    def test_worker_injects_mock_only_at_explicit_startup(self) -> None:
        dbos = MagicMock()
        dbos_module = types.ModuleType("dbos")
        dbos_module.DBOS = dbos
        for mode, expected in (("mock", ImplementationMockAgent), ("codex", ImplementationAgent)):
            with self.subTest(mode=mode), patch.dict(sys.modules, {"dbos": dbos_module}), \
                    patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "docker", "CAPRMEDIO_AGENT_MODE": mode}), \
                    patch.object(backend, "database", return_value=(self.root / "db.sqlite", "sqlite:///unused")), \
                    patch.object(backend, "register_execution") as register, \
                    patch.object(backend.threading, "Event", return_value=MagicMock()), \
                    patch.object(backend.signal, "signal"), \
                    patch("implementation_agent._run", side_effect=AssertionError("no live CLI")):
                backend.worker(self.root)
                providers = register.call_args.kwargs["selected_providers"]
                self.assertIsInstance(providers.implementation_agent, expected)

    def test_fixed_test_first_path_performs_real_baseline_candidate_and_assertion(self) -> None:
        self.assertEqual("evaluation_ready", self.call("CA-O-091")["result"])
        prepared = self.call("CA-O-092")
        self.assertEqual("prepared", prepared["result"], prepared)
        self.assertNotEqual(0, prepared["evidence"][-1]["returncode"])
        self.assertTrue((self.workspace / TEST).is_file())
        self.assertFalse((self.workspace / CANDIDATE).exists())
        self.assertEqual("requirement_ready", self.call("CA-O-091")["result"])
        implemented = self.call("CA-O-093")
        self.assertEqual("implemented", implemented["result"], implemented)
        self.assertEqual(hashlib.sha256((self.workspace / CANDIDATE).read_bytes()).hexdigest(),
                         implemented["outputs"]["changed_paths"][0]["after_sha256"])
        self.assertEqual("evaluation_runnable", self.call("CA-O-091")["result"])
        passed = self.call("CA-O-094")
        self.assertEqual("passed", passed["result"], passed)
        self.assertEqual(0, passed["outputs"]["checks"][0]["returncode"])
        packet = self.packet()
        packet["prior_results"] = [{"step_definition_id": "CA-O-094", "result": "checks pass"}]
        completed = self.call("CA-O-091", packet)
        self.assertEqual("complete", completed["result"], completed)
        self.assertEqual(0, completed["evidence"][-1]["returncode"])
        self.assertEqual({TEST, CANDIDATE}, {path.name for path in self.workspace.iterdir()})
        for result in (prepared, implemented, passed, completed):
            self.assertEqual(TRANSPORT, result["evidence"][0]["transport"])

    def test_mock_allows_workspace_ancestor_alias_but_refuses_workspace_leaf_symlink(self) -> None:
        physical_parent = self.root / "physical-parent"
        physical_parent.mkdir()
        alias = self.root / "ancestor-alias"
        alias.symlink_to(physical_parent, target_is_directory=True)
        workspace = alias / "disposable-workspace"
        workspace.mkdir()
        packet = self.packet("CA-O-091")
        packet["workspace"] = str(workspace)
        packet["permissions"]["implementation_workspace"]["path"] = str(workspace)
        prompt = (PROMPTS / "CA-O-091.prompt.md").read_text()
        self.assertEqual("evaluation_ready", self.agent(prompt, packet)["result"])

        leaf_alias = self.root / "workspace-leaf-alias"
        leaf_alias.symlink_to(workspace, target_is_directory=True)
        packet["workspace"] = str(leaf_alias)
        packet["permissions"]["implementation_workspace"]["path"] = str(leaf_alias)
        self.assertEqual("blocked", self.agent(prompt, packet)["result"])

    def test_denied_missing_or_mismatched_workspace_permission_has_no_effect(self) -> None:
        packets = [self.packet("CA-O-092") for _ in range(5)]
        packets[0]["permissions"]["allowed"] = False
        packets[1]["permissions"].pop("implementation_workspace")
        packets[2]["permissions"]["implementation_workspace"]["path"] = str(self.root)
        packets[3].pop("workspace")
        packets[4]["permissions"]["implementation_workspace"]["unexpected"] = True
        with patch("implementation_mock_agent.subprocess.run", side_effect=AssertionError("must not execute")):
            for packet in packets:
                self.assertEqual("blocked", self.call("CA-O-092", packet)["result"])
        self.assertEqual([], list(self.workspace.iterdir()))

    def test_refuses_unknown_prompt_and_unrelated_reserved_file_without_executing_packet_code(self) -> None:
        packet = self.packet("CA-O-092")
        packet["command"] = ["touch", str(self.root / "outside")]
        packet["candidate_code"] = "raise AssertionError('untrusted code')"
        with patch("implementation_mock_agent.subprocess.run", side_effect=AssertionError("must not execute")):
            self.assertEqual("blocked", self.agent("arbitrary prompt", packet)["result"])
            reserved = self.workspace / TEST
            reserved.write_text("unrelated existing data")
            self.assertEqual("blocked", self.call("CA-O-092", packet)["result"])
            self.assertEqual("unrelated existing data", reserved.read_text())
        self.assertFalse((self.root / "outside").exists())

    def test_missing_or_stale_governed_source_blocks_upstream_before_mock_effect(self) -> None:
        packet = self.packet("CA-O-092")
        packet["source_bindings"] = []
        packet["selected_project"] = {"kind": "selected_project", "source_root": ".caprmedio_caprmedio",
                                      "source_references": []}
        with patch("implementation_mock_agent.subprocess.run", side_effect=AssertionError("must not execute")):
            result = implementation_actions.implement_selected_queue(
                "CA-O-092", packet, self.agent, selected_project_root=self.root)
        self.assertEqual("blocked", result["result"], result)
        self.assertEqual([], list(self.workspace.iterdir()))

    def test_current_selected_project_sources_gate_every_executable_mock_action(self) -> None:
        fixture = GoldenProject(REPOSITORY, self.root, GoldenCase("W09", "run_implementation_workflow"))
        parameters = fixture.native_implementation_parameters()
        workspace = Path(parameters["base_packet"]["workspace"])
        prior = []
        sequence = [("CA-O-091", "evaluation_ready"), ("CA-O-092", "prepared"),
                    ("CA-O-091", "requirement_ready"), ("CA-O-093", "implemented"),
                    ("CA-O-091", "evaluation_runnable"), ("CA-O-094", "passed"),
                    ("CA-O-091", "complete")]
        with patch("implementation_agent._run", side_effect=AssertionError("no live CLI")):
            for step, expected in sequence:
                packet = {**parameters["base_packet"], **parameters["step_packets"][step], "prior_results": prior}
                result = implementation_actions.implement_selected_queue(
                    step, packet, self.agent, selected_project_root=self.root)
                self.assertEqual(expected, result["result"], result)
                prior.append({"step_definition_id": step, "result": result["result"],
                              "outputs": result["outputs"], "evidence": result["evidence"]})
        self.assertEqual({TEST, CANDIDATE}, {path.name for path in workspace.iterdir()})
        row = parameters["base_packet"]["source_bindings"][0]
        source = self.root / row["path"]
        source.write_bytes(source.read_bytes() + b"\nchanged after admission\n")
        packet = {**parameters["base_packet"], **parameters["step_packets"]["CA-O-094"]}
        with patch("implementation_mock_agent.subprocess.run", side_effect=AssertionError("must not execute")):
            blocked = implementation_actions.implement_selected_queue(
                "CA-O-094", packet, self.agent, selected_project_root=self.root)
        self.assertEqual("blocked", blocked["result"], blocked)


if __name__ == "__main__":
    unittest.main()
