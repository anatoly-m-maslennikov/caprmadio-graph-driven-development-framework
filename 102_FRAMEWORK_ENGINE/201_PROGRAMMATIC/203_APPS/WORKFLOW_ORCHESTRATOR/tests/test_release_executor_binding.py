"""Pure private Docker-executor binding checks for selected Release Runs.

These tests do not create a Release request, temporary Project, image or
container. They prove only the private dependency boundary before a selected
Action begins.
"""
from __future__ import annotations

from pathlib import Path
import sys
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
RELEASE = TOOLS / "RELEASE_VERSION"
for location in (APP, TOOLS, RELEASE):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from release_image import DockerSubprocessExecutor
from selected_native_providers import SelectedNativeProviders


class ReleaseExecutorBindingTests(unittest.TestCase):
    def test_default_executor_is_program_owned_and_constructs_without_docker(self):
        with patch.object(DockerSubprocessExecutor, "run") as docker_run:
            providers = SelectedNativeProviders(Path.cwd(), implementation_agent=lambda *args: {})
            executor = providers._private_release_image_executor()

        self.assertIsInstance(executor, DockerSubprocessExecutor)
        docker_run.assert_not_called()

    def test_private_injected_executor_is_preserved_for_test_execution(self):
        injected = object()
        providers = SelectedNativeProviders(
            Path.cwd(), implementation_agent=lambda *args: {}, release_image_executor=injected,
        )

        self.assertIs(providers._private_release_image_executor(), injected)


if __name__ == "__main__":
    unittest.main()
