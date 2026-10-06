"""Executor-local path binding for the selected applicable-methodology compiler."""
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_execution import SelectedExecution, SelectedExecutionError  # noqa: E402


class CompilerExecutionRootTest(unittest.TestCase):
    """The frozen carrier is retained; only its executor-local root is translated."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.host_root = Path(self.temporary.name).resolve()
        self.calls: list[dict[str, object]] = []

        def action(request: dict[str, object]) -> dict[str, object]:
            self.calls.append(request)
            return {"outcome": "assessed"}

        module = types.ModuleType("compile_applicable_methodology")
        module.ACTION_ADAPTERS = {"CA-O-004": action}
        with patch.dict(sys.modules, {"compile_applicable_methodology": module}):
            self.runner = SelectedExecution(self.host_root)
        self.handler = self.runner.handlers["CA-O-004"]

    def _context(self, *, parameters: object, project_root: object) -> dict[str, object]:
        return {
            "workflow_definition_id": "CA-O-011",
            "step_definition_id": "CA-O-152",
            "action_definition_id": "CA-O-004",
            "parameters": parameters,
            "project_root": project_root,
        }

    def test_host_executor_replaces_only_project_root_without_mutating_frozen_parameters(self) -> None:
        frozen = {
            "operation": "dry_run",
            "project_root": "/sealed/host/root",
            "governed_bindings": {"authority.md": "a" * 64},
            "opaque_authorization": {"digest": "b" * 64},
        }
        original = {
            **frozen,
            "governed_bindings": dict(frozen["governed_bindings"]),
            "opaque_authorization": dict(frozen["opaque_authorization"]),
        }

        output = self.handler(self._context(parameters=frozen, project_root=self.host_root))

        self.assertEqual("complete exact selection", output["result"])
        self.assertEqual([{
            **original,
            "project_root": self.host_root.as_posix(),
        }], self.calls)
        self.assertEqual(original, frozen)

    def test_docker_executor_uses_container_visible_project_root(self) -> None:
        frozen = {
            "operation": "dry_run",
            "project_root": self.host_root.as_posix(),
            "governed_bindings": {"authority.md": "a" * 64},
        }
        # The wrapper is created in the host test process, then models the
        # worker's already-validated Docker-visible Project root.
        self.runner.root = Path("/project")

        self.handler(self._context(parameters=frozen, project_root=Path("/project")))

        self.assertEqual("/project", self.calls[0]["project_root"])
        self.assertEqual(self.host_root.as_posix(), frozen["project_root"])
        self.assertEqual({"authority.md": "a" * 64}, self.calls[0]["governed_bindings"])

    def test_missing_or_mismatched_executor_root_refuses_before_compiler_call(self) -> None:
        frozen = {"operation": "dry_run", "project_root": self.host_root.as_posix()}
        with self.assertRaisesRegex(SelectedExecutionError, "execution Project root is invalid"):
            self.handler(self._context(parameters=frozen, project_root=None))
        with self.assertRaisesRegex(SelectedExecutionError, "execution Project root is invalid"):
            self.handler(self._context(parameters=frozen, project_root=self.host_root / "other"))
        self.assertEqual([], self.calls)

    def test_missing_frozen_project_root_refuses_before_compiler_call(self) -> None:
        with self.assertRaisesRegex(SelectedExecutionError, "frozen Project root is invalid"):
            self.handler(self._context(parameters={"operation": "dry_run"}, project_root=self.host_root))
        self.assertEqual([], self.calls)


if __name__ == "__main__":
    unittest.main()
