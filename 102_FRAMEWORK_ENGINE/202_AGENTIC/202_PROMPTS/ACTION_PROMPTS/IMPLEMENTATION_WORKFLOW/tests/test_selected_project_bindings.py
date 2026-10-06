"""Selected-Project source admission checks for Implementation Workflow Actions."""
import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[6]


def load_actions():
    spec = importlib.util.spec_from_file_location("implementation_actions", HERE / "implementation_actions.py")
    actions = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(actions)
    return actions


class SelectedProjectBindings(unittest.TestCase):
    def project_with_reviewed_sources(self, actions: object, directory: Path) -> Path:
        project = directory / "selected-project"
        for row in actions._reviewed_binding_rows():
            source = ROOT / row["path"]
            target = project / row["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        return project

    @staticmethod
    def packet(actions: object, project: Path) -> dict:
        sources = actions.current_source_bindings(project)
        methods = [row["path"] for row in sources if row["atom_id"].startswith("CA-M-")]
        workspace = project / "disposable-workspace"
        workspace.mkdir(exist_ok=True)
        return {
            "context": "Isolated",
            "selected_project": {
                "kind": "selected_project",
                "source_root": ".caprmedio_caprmedio",
                "source_references": sources,
            },
            "source_bindings": sources,
            "permissions": {
                "allowed": True,
                "implementation_workspace": {
                    "kind": "disposable_workspace", "path": str(workspace), "allow_write": True,
                },
            },
            "workspace": str(workspace),
            "handoff_complete": True,
            "plan_item": {"estimated_minutes": 14},
            "requirements_delivery": ["R", "D"],
            "evaluations": ["E"],
            "method_projection": actions.prepare_method_projection(methods, project),
            "retained_state": {},
            "evidence": ["baseline"],
        }

    def test_selected_project_root_is_used_instead_of_immutable_code_root(self):
        actions = load_actions()
        with tempfile.TemporaryDirectory() as directory:
            project = self.project_with_reviewed_sources(actions, Path(directory))
            packet = self.packet(actions, project)
            launched = []

            def agent(_prompt, supplied):
                launched.append(supplied)
                return {"result": "implemented", "outputs": {"candidate": "mock", "changed_paths": ["x.py"]},
                        "evidence": ["mock-performed"]}

            actual = actions.implement_selected_queue(
                "CA-O-093", packet, agent, selected_project_root=project)
            self.assertNotEqual(project.resolve(), actions.ROOT.resolve())
            self.assertEqual(actual["result"], "implemented")
            self.assertEqual(launched, [packet])

    def test_stale_sources_incomplete_methods_and_workspace_mismatch_block_before_agent(self):
        actions = load_actions()
        with tempfile.TemporaryDirectory() as directory:
            project = self.project_with_reviewed_sources(actions, Path(directory))
            packet = self.packet(actions, project)
            launches = []
            agent = lambda *_: launches.append("launched")

            stale_path = project / packet["source_bindings"][0]["path"]
            stale_path.write_text(stale_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            self.assertEqual(
                actions.implement_selected_queue("CA-O-093", packet, agent, selected_project_root=project)["result"],
                "blocked")
            self.assertEqual(launches, [])

        with tempfile.TemporaryDirectory() as directory:
            project = self.project_with_reviewed_sources(actions, Path(directory))
            packet = self.packet(actions, project)
            packet["method_projection"]["sources"] = packet["method_projection"]["sources"][:-1]
            self.assertEqual(
                actions.implement_selected_queue("CA-O-093", packet, agent, selected_project_root=project)["result"],
                "blocked")
            self.assertEqual(launches, [])

        with tempfile.TemporaryDirectory() as directory:
            project = self.project_with_reviewed_sources(actions, Path(directory))
            packet = self.packet(actions, project)
            packet["permissions"]["implementation_workspace"]["path"] = str(project / "other-workspace")
            self.assertEqual(
                actions.implement_selected_queue("CA-O-093", packet, agent, selected_project_root=project)["result"],
                "blocked")
            self.assertEqual(launches, [])

    def test_handler_requires_explicit_selected_project_carrier_when_root_is_supplied(self):
        actions = load_actions()
        with tempfile.TemporaryDirectory() as directory:
            project = self.project_with_reviewed_sources(actions, Path(directory))
            packet = self.packet(actions, project)
            packet.pop("selected_project")
            launches = []
            actual = actions.ACTION_HANDLERS["CA-O-019"](
                packet, lambda *_: launches.append("launched"), selected_project_root=project)
            self.assertEqual(actual["result"], "blocked")
            self.assertEqual(launches, [])

    def test_workspace_cannot_overlap_selected_project_or_protected_authority(self):
        actions = load_actions()
        with tempfile.TemporaryDirectory() as directory:
            project = self.project_with_reviewed_sources(actions, Path(directory))
            launches = []

            for workspace in (project, project / ".caprmedio_caprmedio"):
                with self.subTest(workspace=workspace):
                    packet = self.packet(actions, project)
                    packet["workspace"] = str(workspace)
                    packet["permissions"]["implementation_workspace"]["path"] = str(workspace)
                    actual = actions.implement_selected_queue(
                        "CA-O-093", packet, lambda *_: launches.append("launched"),
                        selected_project_root=project)
                    self.assertEqual(actual["result"], "blocked")
                    self.assertEqual(launches, [])

            protected_git = project / ".git"
            protected_git.mkdir()
            packet = self.packet(actions, project)
            packet["workspace"] = str(protected_git)
            packet["permissions"]["implementation_workspace"]["path"] = str(protected_git)
            actual = actions.implement_selected_queue(
                "CA-O-093", packet, lambda *_: launches.append("launched"), selected_project_root=project)
            self.assertEqual(actual["result"], "blocked")
            self.assertEqual(launches, [])

    def test_workspace_allows_ancestor_alias_but_rejects_workspace_leaf_symlink(self):
        actions = load_actions()
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            physical_parent = parent / "physical-parent"
            physical_parent.mkdir()
            project = self.project_with_reviewed_sources(actions, physical_parent)
            alias = parent / "ancestor-alias"
            alias.symlink_to(physical_parent, target_is_directory=True)
            workspace = alias / "disposable-workspace"
            workspace.mkdir()
            packet = self.packet(actions, project)
            packet["workspace"] = str(workspace)
            packet["permissions"]["implementation_workspace"]["path"] = str(workspace)
            launched = []

            def agent(_prompt, supplied):
                launched.append(supplied)
                return {"result": "implemented", "outputs": {"candidate": "mock", "changed_paths": ["x.py"]},
                        "evidence": ["mock-performed"]}

            actual = actions.implement_selected_queue(
                "CA-O-093", packet, agent, selected_project_root=project)
            self.assertEqual(actual["result"], "implemented")
            self.assertEqual(launched, [packet])

            leaf_alias = parent / "workspace-leaf-alias"
            leaf_alias.symlink_to(workspace, target_is_directory=True)
            packet["workspace"] = str(leaf_alias)
            packet["permissions"]["implementation_workspace"]["path"] = str(leaf_alias)
            blocked = actions.implement_selected_queue(
                "CA-O-093", packet, agent, selected_project_root=project)
            self.assertEqual(blocked["result"], "blocked")
            self.assertEqual(len(launched), 1)

    def test_selected_packet_cannot_fall_back_to_code_root_without_trusted_root(self):
        actions = load_actions()
        packet = {
            "context": "Isolated", "selected_project": {"untrusted": "packet root"},
            "source_bindings": actions.current_source_bindings(), "permissions": {"allowed": True},
            "handoff_complete": True, "plan_item": {"estimated_minutes": 14},
            "requirements_delivery": ["R", "D"], "evaluations": ["E"],
            "method_projection": actions.prepare_method_projection([
                ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/"
                "202_FEATURE_PROMPTS/05_method/CA-M-326-PROMPTS--compose-short-current-"
                "implementation-step-prompts.md"
            ]),
        }
        launches = []
        actual = actions.implement_selected_queue("CA-O-093", packet, lambda *_: launches.append("launched"))
        self.assertEqual(actual["result"], "blocked")
        self.assertEqual(launches, [])


if __name__ == "__main__":
    unittest.main()
