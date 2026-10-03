"""Deterministic tests for the START_BACKGROUND_SERVICES delivery."""

from __future__ import annotations

import importlib.util
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


SCRIPT = Path(__file__).resolve().parents[1] / "start_background_services.py"
TOOLS_SOURCE = SCRIPT.parents[1]
SPEC = importlib.util.spec_from_file_location("start_background_services", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
start_services = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = start_services
SPEC.loader.exec_module(start_services)
from framework_installation import install_release


class StartBackgroundServicesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.repository = Path(self.temporary.name) / "repository"
        self.repository.mkdir()
        subprocess.run(["git", "-C", str(self.repository), "init", "-q"], check=True)
        self.canonical = self.repository / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
        shutil.copytree(
            TOOLS_SOURCE,
            self.canonical,
            ignore=shutil.ignore_patterns("tests", "__pycache__", "*.pyc", ".DS_Store"),
        )
        self.pids: list[int] = []

    def tearDown(self) -> None:
        for pid in self.pids:
            try:
                os.killpg(pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                os.waitpid(pid, 0)
            except ChildProcessError:
                pass
        self.temporary.cleanup()

    def _install_release(self) -> dict[str, object]:
        return install_release(self.repository, apply=True, source_root=self.canonical)

    def test_empty_registry_is_a_successful_noop(self) -> None:
        self._install_release()
        dry = start_services.start_services(self.repository, apply=False)
        applied = start_services.start_services(self.repository, apply=True)
        status = start_services.service_status(self.repository)

        self.assertEqual(0, dry["planned_start_count"])
        self.assertEqual(0, applied["started_count"])
        self.assertEqual(0, status["service_count"])
        self.assertFalse((self.repository / ".caprmedio_runtime/services").exists())

    def test_start_is_installed_local_idempotent_and_runtime_only(self) -> None:
        service = self.canonical / "FIXTURE_SERVICE/service.py"
        service.parent.mkdir()
        service.write_text("import time\nwhile True:\n    time.sleep(1)\n", encoding="utf-8")
        (self.canonical / "background_services.toml").write_text(
            "\n".join(
                [
                    "schema_version = 1",
                    "",
                    "[[services]]",
                    'id = "fixture"',
                    "enabled = true",
                    'command = ["{python}", "-I", "-B", "{tools_root}/FIXTURE_SERVICE/service.py"]',
                    'working_directory = "."',
                    "startup_grace_seconds = 0.05",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        self._install_release()

        dry = start_services.start_services(self.repository, apply=False)
        self.assertEqual(1, dry["planned_start_count"])
        self.assertFalse((self.repository / ".caprmedio_runtime/services").exists())
        first = start_services.start_services(self.repository, apply=True)
        self.assertEqual(1, first["started_count"])
        pid = int(first["services"][0]["pid"])
        self.pids.append(pid)
        second = start_services.start_services(self.repository, apply=True)
        self.assertEqual(0, second["started_count"])
        self.assertEqual(1, second["already_running_count"])
        self.assertTrue(start_services.service_status(self.repository)["services"][0]["running"])
        self.assertTrue((self.repository / ".caprmedio_runtime/services/fixture/state.toml").is_file())
        self.assertEqual([], list((self.repository / ".caprmedio_runtime").rglob("__pycache__")))
        self.assertEqual([], list((self.repository / ".caprmedio_runtime").rglob("*.pyc")))

    def test_rejects_service_script_outside_tools_runtime(self) -> None:
        (self.canonical / "background_services.toml").write_text(
            "\n".join(
                [
                    "schema_version = 1",
                    "",
                    "[[services]]",
                    'id = "outside"',
                    "enabled = true",
                    'command = ["{python}", "-I", "-B", "{repository}/outside.py"]',
                    "",
                ]
            ),
            encoding="utf-8",
        )
        (self.repository / "outside.py").write_text("pass\n", encoding="utf-8")
        self._install_release()

        with self.assertRaisesRegex(start_services.ToolError, "outside .caprmedio_runtime/tools"):
            start_services.start_services(self.repository, apply=False)
        self.assertFalse((self.repository / ".caprmedio_runtime/services").exists())


if __name__ == "__main__":
    unittest.main()
