"""Deterministic tests for the INSTALL_TOOLS delivery."""

from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


SCRIPT = Path(__file__).resolve().parents[1] / "install_tools.py"
TOOLS_SOURCE = SCRIPT.parents[1]
SPEC = importlib.util.spec_from_file_location("install_tools", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
install_tools = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = install_tools
SPEC.loader.exec_module(install_tools)


class InstallToolsTests(unittest.TestCase):
    def setUp(self) -> None:
        # Synthetic Git and CODEX_HOME carriers can be protected from deletion
        # by the execution sandbox after a passed test.
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.repository = Path(self.temporary.name) / "repository"
        self.codex_home = Path(self.temporary.name) / "codex-home"
        self.codex_home.mkdir()
        self.user_hooks = self.codex_home / "hooks.json"
        self.user_hooks.write_text(
            json.dumps(
                {
                    "description": "Existing user hooks.",
                    "hooks": {
                        "PreToolUse": [
                            {
                                "matcher": "^Bash$",
                                "hooks": [{"type": "command", "command": "true", "timeout": 3}],
                            }
                        ]
                    },
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        self.previous_codex_home = os.environ.get("CODEX_HOME")
        os.environ["CODEX_HOME"] = str(self.codex_home)
        self.repository.mkdir()
        subprocess.run(["git", "-C", str(self.repository), "init", "-q"], check=True)
        subprocess.run(["git", "-C", str(self.repository), "config", "user.name", "CAPRMEDIO Test"], check=True)
        subprocess.run(["git", "-C", str(self.repository), "config", "user.email", "test@example.invalid"], check=True)
        self.canonical = self.repository / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
        shutil.copytree(
            TOOLS_SOURCE,
            self.canonical,
            ignore=shutil.ignore_patterns("tests", "__pycache__", "*.pyc", ".DS_Store"),
        )

    def tearDown(self) -> None:
        if self.previous_codex_home is None:
            os.environ.pop("CODEX_HOME", None)
        else:
            os.environ["CODEX_HOME"] = self.previous_codex_home
        self.temporary.cleanup()

    def test_dry_run_resolves_complete_install_without_mutation(self) -> None:
        before = subprocess.run(
            ["git", "-C", str(self.repository), "config", "--local", "--list"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        user_hooks_before = self.user_hooks.read_bytes()
        result = install_tools.install(self.repository, apply=False)
        after = subprocess.run(
            ["git", "-C", str(self.repository), "config", "--local", "--list"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout

        self.assertFalse(result["installed"])
        self.assertGreater(result["file_count"], 10)
        self.assertEqual(before, after)
        self.assertFalse((self.repository / ".caprmedio_runtime/tools").exists())
        self.assertFalse((self.repository / ".caprmedio_runtime").exists())
        self.assertFalse((self.repository / ".codex").exists())
        self.assertEqual(user_hooks_before, self.user_hooks.read_bytes())

    def test_apply_installs_verified_release_launchers_and_all_hooks(self) -> None:
        result = install_tools.install(self.repository, apply=True)
        status = install_tools.tool_status(self.repository)

        self.assertTrue(result["installed"])
        self.assertTrue(status["verified"])
        self.assertTrue(status["source_matches_install"])
        self.assertTrue(status["hooks_installed"])
        self.assertTrue(status["codex_hook_carrier_verified"])
        self.assertEqual("host-controlled-unverified", status["codex_hook_activation"])
        self.assertTrue(status["launchers_verified"])
        self.assertEqual(".caprmedio_runtime/tools/hooks/git", status["hooks_path"])
        installer_temporary = self.repository / ".caprmedio_tmp/install_tools"
        self.assertFalse(any(path.is_file() for path in installer_temporary.rglob("*")))
        self.assertFalse((self.repository / ".codex/hooks.json").exists())
        hook_document = json.loads(self.user_hooks.read_text(encoding="utf-8"))
        self.assertEqual("Existing user hooks.", hook_document["description"])
        self.assertEqual("true", hook_document["hooks"]["PreToolUse"][0]["hooks"][0]["command"])
        self.assertEqual({"PreToolUse", "PostToolUse", "SessionStart", "Stop"}, set(hook_document["hooks"]))
        for event in ("PreToolUse", "PostToolUse", "SessionStart", "Stop"):
            group = hook_document["hooks"][event][-1]
            self.assertEqual(".*", group["matcher"])
            for tool_name in ("functions.exec", "apply_patch"):
                self.assertIsNotNone(re.fullmatch(group["matcher"], tool_name))
            command = group["hooks"][0]["command"]
            self.assertIn("caprmedio.codex-hooks", command)
            self.assertIn(".caprmedio_runtime/tools/bin/commit-trigger", command)
            self.assertNotIn(str(self.repository), command)
            self.assertNotIn(".caprmedio_runtime/tools/releases/", command)
        package_root = self.repository / str(status["package_root"])
        self.assertTrue(status["launchers"]["commit-trigger"])
        hook_text = (self.repository / ".caprmedio_runtime/tools/hooks/codex/hooks.json").read_text(encoding="utf-8")
        self.assertIn(".caprmedio_runtime/tools/bin/commit-trigger", hook_text)
        self.assertNotIn(str(self.repository), hook_text)
        self.assertNotIn(".caprmedio_runtime/tools/releases/", hook_text)
        for relative in (
            "INSTALL_TOOLS/install_tools.py",
            "START_BACKGROUND_SERVICES/start_background_services.py",
            "COMMIT_TRIGGER/commit_trigger.py",
            "COMMIT_CHANGE_SET/commit_change_set.py",
        ):
            completed = subprocess.run(
                [sys.executable, "-I", "-B", str(package_root / relative), "--repository", str(self.repository), "describe"],
                check=True,
                capture_output=True,
                text=True,
                env={"PATH": os.environ.get("PATH", "")},
            )
            self.assertTrue(json.loads(completed.stdout)["ok"], relative)
        entrypoints = [
            path
            for path in sorted(package_root.rglob("*.py"))
            if 'if __name__ == "__main__"' in path.read_text(encoding="utf-8")
        ]
        self.assertGreater(len(entrypoints), 10)
        for path in entrypoints:
            subprocess.run(
                [
                    sys.executable,
                    "-I",
                    "-B",
                    "-c",
                    'import runpy,sys; from pathlib import Path; sys.path.insert(0, str(Path(sys.argv[1]).parent)); runpy.run_path(sys.argv[1], run_name="caprmedio_probe")',
                    str(path),
                ],
                cwd=self.repository,
                check=True,
                capture_output=True,
                text=True,
                env={"PATH": os.environ.get("PATH", "")},
            )
        self.assertEqual([], list((self.repository / ".caprmedio_runtime").rglob("__pycache__")))
        self.assertEqual([], list((self.repository / ".caprmedio_runtime").rglob("*.pyc")))

    def test_apply_without_hooks_installs_tools_and_preserves_host_hook_state(self) -> None:
        custom = self.repository / "custom-hooks"
        custom.mkdir()
        subprocess.run(
            ["git", "-C", str(self.repository), "config", "--local", "core.hooksPath", "custom-hooks"],
            check=True,
        )
        user_hooks_before = self.user_hooks.read_bytes()

        result = install_tools.install(self.repository, apply=True, manage_host_hooks=False)

        self.assertTrue(result["installed"])
        self.assertFalse(result["hooks_installed"])
        self.assertFalse(result["host_hooks_managed"])
        self.assertEqual("custom-hooks", install_tools._git_hooks_path(self.repository))
        self.assertEqual(user_hooks_before, self.user_hooks.read_bytes())
        self.assertTrue((self.repository / ".caprmedio_runtime/tools/current.toml").is_file())
        self.assertTrue((self.repository / ".caprmedio_runtime/tools/bin/commit-trigger").is_file())
        self.assertFalse((self.repository / ".caprmedio_runtime/tools/hooks/git").exists())

    def test_custom_git_hooks_path_rejects_install_without_mutation(self) -> None:
        custom = self.repository / "custom-hooks"
        custom.mkdir()
        subprocess.run(
            ["git", "-C", str(self.repository), "config", "--local", "core.hooksPath", "custom-hooks"],
            check=True,
        )

        with self.assertRaisesRegex(install_tools.ToolError, "different local core.hooksPath"):
            install_tools.install(self.repository, apply=True)

        self.assertEqual("custom-hooks", install_tools._git_hooks_path(self.repository))
        self.assertFalse((self.repository / ".caprmedio_runtime/tools").exists())
        self.assertFalse((self.repository / ".caprmedio_runtime").exists())
        self.assertFalse((self.repository / ".codex").exists())

    def test_reinstall_selects_new_content_addressed_release_and_repoints_hooks(self) -> None:
        first = install_tools.install(self.repository, apply=True)
        codex_hooks_before = (self.repository / ".caprmedio_runtime/tools/hooks/codex/hooks.json").read_bytes()
        user_hooks_before = self.user_hooks.read_bytes()
        registry = self.canonical / "background_services.toml"
        registry.write_text("schema_version = 1\nservices = []\n# next release\n", encoding="utf-8")
        second = install_tools.install(self.repository, apply=True)

        self.assertNotEqual(first["release"], second["release"])
        status = install_tools.tool_status(self.repository)
        self.assertEqual(second["release"], status["release"])
        self.assertTrue(status["hooks_installed"])
        self.assertEqual(
            codex_hooks_before,
            (self.repository / ".caprmedio_runtime/tools/hooks/codex/hooks.json").read_bytes(),
        )
        self.assertEqual(user_hooks_before, self.user_hooks.read_bytes())
        stable_launcher = (self.repository / ".caprmedio_runtime/tools/bin/commit-trigger").read_text(encoding="utf-8")
        self.assertIn(second["release"], stable_launcher)
        self.assertNotIn(first["release"], stable_launcher)
        for name in ("pre-commit", "commit-msg", "post-commit"):
            text = (self.repository / ".caprmedio_runtime/tools/hooks/git" / name).read_text(encoding="utf-8")
            self.assertIn(second["release"], text)
            self.assertNotIn(first["release"], text)

    def test_rejects_drift_in_an_existing_content_addressed_release(self) -> None:
        installed = install_tools.install(self.repository, apply=True)
        carrier = self.repository / str(installed["package_root"]) / "background_services.toml"
        carrier.write_text("schema_version = 1\nservices = []\n# drift\n", encoding="utf-8")
        current_before = (self.repository / ".caprmedio_runtime/tools/current.toml").read_bytes()
        hooks_before = {
            name: (self.repository / ".caprmedio_runtime/tools/hooks/git" / name).read_bytes()
            for name in ("pre-commit", "commit-msg", "post-commit")
        }

        with self.assertRaisesRegex(install_tools.InstallationError, "existing release file differs"):
            install_tools.install(self.repository, apply=True)

        self.assertEqual(current_before, (self.repository / ".caprmedio_runtime/tools/current.toml").read_bytes())
        self.assertEqual(
            hooks_before,
            {
                name: (self.repository / ".caprmedio_runtime/tools/hooks/git" / name).read_bytes()
                for name in ("pre-commit", "commit-msg", "post-commit")
            },
        )

    def test_user_dispatcher_requires_local_activation_and_selects_current_repository(self) -> None:
        install_tools.install(self.repository, apply=True)
        hook_document = json.loads(self.user_hooks.read_text(encoding="utf-8"))
        command = hook_document["hooks"]["PreToolUse"][-1]["hooks"][0]["command"]
        control = self.repository / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\n"
            'control_root = ".caprmedio_caprmedio"\n'
            'framework_root = ".caprmedio_framework"\n'
            'journal_root = ".caprmedio_caprmedio/work_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n'
            'temporary_root = ".caprmedio_tmp"\n'
            'legacy_migration_roots = [".caprmedio"]\n',
            encoding="utf-8",
        )
        payload = json.dumps(
            {
                "session_id": "019f591f-04f6-70f2-8de7-828b7cccc69d",
                "tool_use_id": "tool-use-001",
                "cwd": str(self.repository),
            }
        )
        delegated = subprocess.run(
            command,
            cwd=self.repository,
            input=payload,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
            env={**os.environ, "CODEX_HOME": str(self.codex_home)},
        )
        self.assertEqual("snapshot", json.loads(delegated.stdout)["result"]["effect"])

        uninstalled = Path(self.temporary.name) / "uninstalled"
        uninstalled.mkdir()
        subprocess.run(["git", "-C", str(uninstalled), "init", "-q"], check=True)
        fake = uninstalled / ".caprmedio_runtime/tools/bin/commit-trigger"
        fake.parent.mkdir(parents=True)
        sentinel = uninstalled / "unexpected-dispatch"
        fake.write_text(f"#!/bin/sh\ntouch {sentinel}\n", encoding="utf-8")
        fake.chmod(0o755)
        skipped = subprocess.run(command, cwd=uninstalled, input=payload, shell=True, check=True, capture_output=True, text=True)
        self.assertEqual("", skipped.stdout)
        self.assertFalse(sentinel.exists())

        outside = Path(self.temporary.name) / "outside"
        outside.mkdir()
        skipped_outside = subprocess.run(command, cwd=outside, input=payload, shell=True, check=True, capture_output=True, text=True)
        self.assertEqual("", skipped_outside.stdout)

    def test_unavailable_user_hook_carrier_fails_with_current_selection_unchanged(self) -> None:
        first = install_tools.install(self.repository, apply=True)
        current_before = (self.repository / ".caprmedio_runtime/tools/current.toml").read_bytes()
        fragment_before = (self.repository / ".caprmedio_runtime/tools/hooks/codex/hooks.json").read_bytes()
        registry = self.canonical / "background_services.toml"
        registry.write_text("schema_version = 1\nservices = []\n# blocked user carrier\n", encoding="utf-8")
        unavailable = Path(self.temporary.name) / "codex-home-is-a-file"
        unavailable.write_text("not a directory\n", encoding="utf-8")
        os.environ["CODEX_HOME"] = str(unavailable)

        with self.assertRaisesRegex(install_tools.ToolError, "cannot update the Codex user Hook carrier"):
            install_tools.install(self.repository, apply=True)

        self.assertEqual(current_before, (self.repository / ".caprmedio_runtime/tools/current.toml").read_bytes())
        self.assertEqual(fragment_before, (self.repository / ".caprmedio_runtime/tools/hooks/codex/hooks.json").read_bytes())
        os.environ["CODEX_HOME"] = str(self.codex_home)
        self.assertEqual(first["release"], install_tools.tool_status(self.repository)["release"])


if __name__ == "__main__":
    unittest.main()
