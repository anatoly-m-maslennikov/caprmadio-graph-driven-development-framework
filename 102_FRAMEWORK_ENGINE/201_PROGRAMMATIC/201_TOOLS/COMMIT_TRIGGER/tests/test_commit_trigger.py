"""Deterministic acceptance tests for COMMIT_TRIGGER Evaluations E169, E186, E194."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import stat
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "commit_trigger.py"
SPEC = importlib.util.spec_from_file_location("commit_trigger", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
commit_trigger = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = commit_trigger
SPEC.loader.exec_module(commit_trigger)
from framework_installation import install_release


class CommitTriggerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.repository = Path(self.temporary.name) / "repository"
        self.codex_home = Path(self.temporary.name) / "codex-home"
        self.codex_home.mkdir()
        self.previous_codex_home = os.environ.get("CODEX_HOME")
        os.environ["CODEX_HOME"] = str(self.codex_home)
        self.repository.mkdir()
        self._git("init", "-q")
        self._git("config", "user.name", "CAPRMEDIO Test")
        self._git("config", "user.email", "test@example.invalid")
        (self.repository / "README.md").write_text("fixture\n", encoding="utf-8")
        (self.repository / ".caprmedio_caprmedio").mkdir()
        (self.repository / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            "[artifact_timestamps]\ntimezone = \"Asia/Tbilisi\"\n\n"
            "[paths]\ncontrol_root = \".caprmedio_caprmedio\"\n"
            "framework_root = \".caprmedio_framework\"\n"
            "journal_root = \".caprmedio_caprmedio/work_journal\"\n"
            "runtime_root = \".caprmedio_runtime\"\n"
            "temporary_root = \".caprmedio_tmp\"\n"
            "legacy_migration_roots = [\".caprmedio\"]\n",
            encoding="utf-8",
        )
        self._git("add", "README.md", ".caprmedio_caprmedio/caprmedio_project_settings.toml")
        self._git("commit", "-qm", "fixture")
        self.adapter = commit_trigger.AdapterSpec(
            "codex-file-events",
            "codex",
            "CODEX_THREAD_ID",
            "CODEX_SESSION_ID",
            True,
        )
        commit_trigger.adapter_operation(self.repository, "install", adapter=self.adapter, apply=True)
        self.environment = {"CODEX_THREAD_ID": "019f591f-04f6-70f2-8de7-828b7cccc69d"}

    def tearDown(self) -> None:
        if self.previous_codex_home is None:
            os.environ.pop("CODEX_HOME", None)
        else:
            os.environ["CODEX_HOME"] = self.previous_codex_home
        self.temporary.cleanup()

    def _git(self, *arguments: str) -> str:
        completed = subprocess.run(
            ["git", "-C", str(self.repository), *arguments],
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout

    def _observation(self, **overrides: object) -> dict[str, object]:
        observation: dict[str, object] = {
            "adapter_id": self.adapter.adapter_id,
            "source_event_id": "host-event-001",
            "observed_at": "2026-08-20T20:21:22+00:00",
            "before_path": None,
            "after_path": ".caprmedio_caprmedio/04_requirement/CA-R-001.md",
        }
        observation.update(overrides)
        return observation

    def _write_atom(self, path: str, *, version: int, body: str) -> None:
        target = self.repository / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            f"---\nversion: {version}\nrelations:\n---\n# {target.stem}\n\n{body}\n",
            encoding="utf-8",
        )

    def _snapshot(self) -> dict[str, object]:
        def files(root: Path) -> dict[str, str]:
            if not root.exists():
                return {}
            return {
                path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in sorted(root.rglob("*"))
                if path.is_file()
            }

        runtime = self.repository / ".caprmedio_runtime"
        journals = self.repository / ".caprmedio_caprmedio" / "work_journal"
        return {
            "status": self._git("status", "--porcelain=v1"),
            "index": (self.repository / ".git" / "index").read_bytes(),
            "head": self._git("rev-parse", "HEAD").strip(),
            "runtime": files(runtime),
            "journals": files(journals),
        }

    def test_e169_emit_one_stable_trigger_without_mutation(self) -> None:
        """Noisy delivery coalesces to one stable trigger and changes no state."""

        observation = self._observation()
        before = self._snapshot()
        triggers = commit_trigger.emit_from_registered_adapter(
            [observation, dict(observation), dict(observation)],
            repository=self.repository,
            adapter_id=self.adapter.adapter_id,
            environment=self.environment,
        )
        after = self._snapshot()

        self.assertEqual(len(triggers), 1)
        trigger = triggers[0]
        self.assertEqual(trigger["schema_version"], 1)
        self.assertEqual(trigger["adapter"], {"id": "codex-file-events"})
        self.assertEqual(trigger["source_event_id"], "host-event-001")
        self.assertEqual(trigger["observed_at"], "2026-08-20T20:21:22Z")
        self.assertEqual(trigger["before_path"], None)
        self.assertEqual(trigger["after_path"], ".caprmedio_caprmedio/04_requirement/CA-R-001.md")
        self.assertEqual(
            trigger["llm_session"],
            {"app": "codex", "uuid": "019f591f-04f6-70f2-8de7-828b7cccc69d"},
        )
        self.assertNotIn("occurred_at", trigger["llm_session"])
        self.assertEqual(before, after)

    def test_e186_adapter_lifecycle_preserves_existing_hook_bytes_and_behavior(self) -> None:
        """Runtime registration chains and preserves the default Git Hook."""

        commit_trigger.adapter_operation(self.repository, "uninstall", adapter_id=self.adapter.adapter_id, apply=True)
        hook = self.repository / ".git" / "hooks" / "pre-commit"
        sentinel = self.repository / "hook-sentinel.log"
        hook.write_text(f"#!/bin/sh\nprintf 'sentinel\\n' >> {sentinel}\n", encoding="utf-8")
        hook.chmod(0o751)
        original_bytes = hook.read_bytes()
        original_mode = stat.S_IMODE(hook.stat().st_mode)
        install_release(self.repository, apply=True, source_root=commit_trigger.PACKAGE_ROOT)
        status_before = commit_trigger.adapter_operation(self.repository, "status")
        self.assertEqual(status_before["adapters"], [])

        installed = commit_trigger.adapter_operation(
            self.repository,
            "install",
            adapter=self.adapter,
            apply=True,
            manage_host_hooks=True,
        )
        self.assertTrue(installed["host_hooks"]["git"]["registered"])
        self.assertEqual(commit_trigger.MANAGED_GIT_HOOKS_PATH, commit_trigger._local_git_hooks_path(self.repository))
        for name in commit_trigger.GIT_HOOK_NAMES:
            carrier = self.repository / commit_trigger.MANAGED_GIT_HOOKS_PATH / name
            self.assertTrue(carrier.is_file())
            self.assertTrue(os.access(carrier, os.X_OK))
        managed_change = self.repository / "managed-change.txt"
        managed_change.write_text("managed\n", encoding="utf-8")
        self._git("add", managed_change.name)
        rejected = subprocess.run(
            ["git", "-C", str(self.repository), "commit", "-qm", "ordinary managed commit"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(0, rejected.returncode)
        self._git("reset", "-q", "--", managed_change.name)
        enabled = commit_trigger.emit_from_registered_adapter(
            [self._observation()], repository=self.repository, adapter_id=self.adapter.adapter_id, environment=self.environment
        )
        self.assertEqual(len(enabled), 1)

        commit_trigger.adapter_operation(self.repository, "disable", adapter_id=self.adapter.adapter_id, apply=True)
        disabled = commit_trigger.emit_from_registered_adapter(
            [self._observation()], repository=self.repository, adapter_id=self.adapter.adapter_id, environment=self.environment
        )
        self.assertEqual(disabled, [])

        commit_trigger.adapter_operation(
            self.repository,
            "uninstall",
            adapter_id=self.adapter.adapter_id,
            apply=True,
            manage_host_hooks=True,
        )
        uninstalled = commit_trigger.emit_from_registered_adapter(
            [self._observation()], repository=self.repository, adapter_id=self.adapter.adapter_id, environment=self.environment
        )
        self.assertEqual(uninstalled, [])
        self.assertIsNone(commit_trigger._local_git_hooks_path(self.repository))
        default_change = self.repository / "default-change.txt"
        default_change.write_text("default\n", encoding="utf-8")
        self._git("add", default_change.name)
        self._git("commit", "-qm", "ordinary default commit")
        self.assertEqual(hook.read_bytes(), original_bytes)
        self.assertEqual(stat.S_IMODE(hook.stat().st_mode), original_mode)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "sentinel\nsentinel\n")
        self.assertFalse((self.repository / ".caprmedio_runtime" / "commit_trigger" / "backup").exists())

    def test_e194_suppress_correlated_journal_and_runtime_events(self) -> None:
        """Correlated pipeline side effects cannot recursively produce a trigger."""

        original = self._observation(source_event_id="subject-change")
        journal = self._observation(
            source_event_id="journal-write",
            before_path=None,
            after_path=".caprmedio_caprmedio/work_journal/alice-2026-08-20-part-1.ndjson",
            pipeline={"owned": True, "action_id": "action-001", "kind": "journal"},
        )
        runtime = self._observation(
            source_event_id="runtime-write",
            before_path=None,
            after_path=".caprmedio_runtime/state/commit_change_set/action-001.json",
            pipeline={"owned": True, "action_id": "action-001", "kind": "runtime-state"},
        )
        triggers = commit_trigger.emit_from_registered_adapter(
            [original, journal, runtime],
            repository=self.repository,
            adapter_id=self.adapter.adapter_id,
            environment=self.environment,
        )

        self.assertEqual([trigger["source_event_id"] for trigger in triggers], ["subject-change"])

    def test_native_codex_watch_detects_one_edit_and_suppresses_correlated_pipeline_write(self) -> None:
        """The non-invasive native adapter polls a source boundary without Hooks."""

        control_root = self.repository / ".caprmedio_caprmedio"
        control_root.mkdir(exist_ok=True)
        atom = control_root / "04_requirement" / "CA-R-001.md"

        def write_atom() -> None:
            time.sleep(0.04)
            atom.parent.mkdir(parents=True)
            atom.write_text("first revision\n", encoding="utf-8")

        writer = threading.Thread(target=write_atom)
        writer.start()
        batches = list(
            commit_trigger.watch_triggers(
                repository=self.repository,
                adapter=self.adapter,
                environment=self.environment,
                poll_interval=0.01,
                maximum_polls=12,
            )
        )
        writer.join()
        triggers = [trigger for batch in batches for trigger in batch]
        self.assertEqual(len(triggers), 1)
        self.assertEqual(triggers[0]["before_path"], None)
        self.assertEqual(triggers[0]["after_path"], ".caprmedio_caprmedio/04_requirement/CA-R-001.md")
        self.assertTrue(str(triggers[0]["source_event_id"]).startswith("watch-"))

        previous = commit_trigger.scan_governed_files(self.repository)
        journal = control_root / "work_journal" / "alice-2026-08-20-part-1.ndjson"
        journal.parent.mkdir()
        journal.write_text('{"event_id":"fixture"}\n', encoding="utf-8")
        current = commit_trigger.scan_governed_files(self.repository)
        carrier = ".caprmedio_caprmedio/work_journal/alice-2026-08-20-part-1.ndjson"
        state = current[carrier]
        transition = {
            "event_id": "event-001",
            "event_digest": hashlib.sha256(b"event").hexdigest(),
            "carrier": carrier,
            "line": state.line_count,
            "previous_carrier_digest": hashlib.sha256(b"").hexdigest(),
            "appended_carrier_digest": state.sha256,
        }
        correlation_id = commit_trigger._sha256({"action_id": "action-001", "transition": transition})
        observations = commit_trigger.detect_watch_observations(
            previous,
            current,
            adapter_id=self.adapter.adapter_id,
            repository=self.repository,
            observed_at="2026-08-20T20:21:22Z",
            correlations={
                carrier: (
                    commit_trigger.PipelineCorrelation(
                        correlation_id=correlation_id,
                        action_id="action-001",
                        **transition,
                    ),
                )
            },
        )
        self.assertEqual(len(observations), 1)
        self.assertEqual(observations[0]["pipeline"], {"owned": True, "action_id": "action-001", "kind": "journal"})
        self.assertEqual(
            commit_trigger.emit_triggers(
                observations,
                adapter=self.adapter,
                repository=self.repository,
                environment=self.environment,
            ),
            [],
        )

    def test_native_watch_pairs_move_and_update_by_stable_carrier_identity(self) -> None:
        control_root = self.repository / ".caprmedio_caprmedio"
        old = control_root / "04_requirement" / "CA-R-001-REQUIREMENT--old-summary.md"
        old.parent.mkdir(parents=True)
        old.write_text("---\nversion: 1\nrelations: {}\n---\n# Old\n", encoding="utf-8")
        previous = commit_trigger.scan_governed_files(self.repository)

        new = control_root / "METAMODEL" / "04_requirement" / "CA-R-001-REQUIREMENT--new-summary.md"
        new.parent.mkdir(parents=True)
        old.replace(new)
        new.write_text("---\nversion: 2\nrelations: {}\n---\n# New\n", encoding="utf-8")
        current = commit_trigger.scan_governed_files(self.repository)

        observations = commit_trigger.detect_watch_observations(
            previous,
            current,
            adapter_id=self.adapter.adapter_id,
            repository=self.repository,
            observed_at="2026-08-20T20:21:22Z",
        )
        affected = [
            observation
            for observation in observations
            if observation.get("before_path") == old.relative_to(self.repository).as_posix()
            or observation.get("after_path") == new.relative_to(self.repository).as_posix()
        ]
        self.assertEqual(len(affected), 1)
        self.assertEqual(affected[0]["before_path"], old.relative_to(self.repository).as_posix())
        self.assertEqual(affected[0]["after_path"], new.relative_to(self.repository).as_posix())

    def test_digest_bound_correlation_replay_and_retirement(self) -> None:
        carrier = ".caprmedio_caprmedio/work_journal/alice-2026-08-20-part-1.ndjson"
        transition = {
            "event_id": "event-001",
            "event_digest": hashlib.sha256(b"event").hexdigest(),
            "carrier": carrier,
            "line": 1,
            "previous_carrier_digest": hashlib.sha256(b"").hexdigest(),
            "appended_carrier_digest": hashlib.sha256(b"record\n").hexdigest(),
        }
        action_id = "action-001"
        correlation_id = commit_trigger._sha256({"action_id": action_id, "transition": transition})
        path = self.repository / ".caprmedio_runtime/state/commit_trigger/pipeline_correlations.ndjson"
        path.parent.mkdir(parents=True, exist_ok=True)
        registered = {
            "schema_version": 1,
            "event": "registered",
            "correlation_id": correlation_id,
            "action_id": action_id,
            "transition": transition,
        }
        path.write_text(json.dumps(registered, sort_keys=True) + "\n", encoding="utf-8")
        active = commit_trigger._read_pipeline_correlations(path)
        self.assertEqual([item.correlation_id for item in active[carrier]], [correlation_id])
        retired = {
            "schema_version": 1,
            "event": "retired",
            "correlation_id": correlation_id,
            "action_id": action_id,
        }
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(retired, sort_keys=True) + "\n")
        self.assertEqual(commit_trigger._read_pipeline_correlations(path), {})

    def test_codex_host_resolution_prefers_thread_then_falls_back(self) -> None:
        self.assertEqual(
            commit_trigger.resolve_codex_session(
                environment={
                    "CODEX_THREAD_ID": "019f591f-04f6-70f2-8de7-828b7cccc69d",
                    "CODEX_SESSION_ID": "019f5920-04f6-70f2-8de7-828b7cccc69d",
                }
            ),
            {"app": "codex", "uuid": "019f591f-04f6-70f2-8de7-828b7cccc69d"},
        )
        self.assertEqual(
            commit_trigger.resolve_codex_session(environment={"CODEX_SESSION_ID": "019f5920-04f6-70f2-8de7-828b7cccc69d"}),
            {"app": "codex", "uuid": "019f5920-04f6-70f2-8de7-828b7cccc69d"},
        )

    def test_codex_hook_admits_all_project_paths_and_excludes_other_dot_directories(self) -> None:
        self.assertTrue(
            commit_trigger._hook_eligible(
                self.repository,
                {
                    "before_path": ".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--subject.md",
                    "after_path": ".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--subject.md",
                }
            )
        )
        for path in (
            ".caprmedio_runtime/state.json",
            ".caprmedio_tmp/cache.json",
            ".github/workflows/test.yml",
            ".f4f/config.toml",
        ):
            self.assertFalse(commit_trigger._hook_eligible(self.repository, {"before_path": path, "after_path": path}), path)
        for path in (
            "README.md",
            "src/application.py",
            ".gitignore",
            ".caprmedio_framework/04_requirement/CA-R-001-REQUIREMENT--framework.md",
            ".caprmedio_caprmedio/stg_requirements_subjects.md",
            ".caprmedio_caprmedio/04_requirement/archive/CA-R-001-REQUIREMENT--subject.md",
        ):
            self.assertTrue(commit_trigger._hook_eligible(self.repository, {"before_path": path, "after_path": path}), path)

    def test_current_hook_carrier_does_not_require_a_rewrite(self) -> None:
        carrier = self.repository / "already-current-hooks.json"
        carrier.write_text("{}\n", encoding="utf-8")
        with mock.patch.object(commit_trigger, "_atomic_write", side_effect=AssertionError("must not rewrite current Carrier")):
            self.assertFalse(commit_trigger._atomic_write_if_changed(carrier, "{}\n"))

    def test_hook_control_stops_before_scan_trips_on_failure_and_reloads_transients(self) -> None:
        payload = {
            "session_id": self.environment["CODEX_THREAD_ID"],
            "tool_use_id": "tool-use-control",
            "cwd": str(self.repository),
        }
        stopped = commit_trigger.hook_control(self.repository, "stop", apply=True, reason="operator-stop")
        self.assertEqual("stopped", stopped["control"]["mode"])
        with mock.patch.object(commit_trigger, "scan_governed_files", side_effect=AssertionError("scan must not run")):
            skipped = commit_trigger.codex_hook(self.repository, "pre", self.adapter.adapter_id, payload)
        self.assertEqual("circuit-open", skipped["effect"])

        started = commit_trigger.hook_control(self.repository, "start", apply=True)
        self.assertEqual("running", started["control"]["mode"])
        with mock.patch.object(
            commit_trigger,
            "scan_governed_files",
            side_effect=commit_trigger.ToolError("fixture-hook-failure", "fixture failure"),
        ):
            failed = commit_trigger.codex_hook(self.repository, "pre", self.adapter.adapter_id, payload)
        self.assertEqual("circuit-tripped", failed["effect"])
        self.assertEqual("fixture-hook-failure", failed["diagnostic"]["code"])
        self.assertEqual("tripped", commit_trigger.hook_control(self.repository, "status")["control"]["mode"])

        runtime = self.repository / commit_trigger.RUNTIME_DIRECTORY
        for directory in (runtime / "hook_snapshots", runtime / "session_baselines"):
            directory.mkdir(parents=True, exist_ok=True)
            (directory / "stale.json").write_text("{}\n", encoding="utf-8")
        reloaded = commit_trigger.hook_control(self.repository, "reload", apply=True)
        self.assertEqual(2, reloaded["removed_transient_files"])
        self.assertEqual("running", reloaded["control"]["mode"])
        self.assertEqual(0, commit_trigger.hook_control(self.repository, "status")["transient_file_count"])

    def test_managed_codex_hooks_have_a_short_external_timeout(self) -> None:
        for phase in ("pre", "post", "start", "stop"):
            handler = commit_trigger._managed_hook_group(phase, self.adapter.adapter_id)["hooks"][0]
            self.assertEqual(5, handler["timeout"])

    def test_hook_watchdog_automatically_trips_a_hung_invocation(self) -> None:
        payload = {
            "session_id": self.environment["CODEX_THREAD_ID"],
            "tool_use_id": "tool-use-watchdog",
            "cwd": str(self.repository),
        }

        def delayed_hook(*args: object, **kwargs: object) -> dict[str, object]:
            time.sleep(0.05)
            return {"phase": "pre", "effect": "fixture-finished", "commit_count": 0}

        with (
            mock.patch.object(commit_trigger, "CODEX_HOOK_BUDGET_SECONDS", 0.01),
            mock.patch.object(commit_trigger, "_run_codex_hook", side_effect=delayed_hook),
        ):
            commit_trigger.codex_hook(self.repository, "pre", self.adapter.adapter_id, payload)
        control = commit_trigger.hook_control(self.repository, "status")["control"]
        self.assertEqual("tripped", control["mode"])
        self.assertEqual("hook-time-budget-exceeded", control["reason"])

    def test_project_frontier_uses_git_ignore_and_groups_one_folder_action(self) -> None:
        (self.repository / ".gitignore").write_text("/.caprmedio_runtime/\n/ignored/\n", encoding="utf-8")
        (self.repository / ".caprmedio_caprmedio/settings.toml").write_text("enabled = true\n", encoding="utf-8")
        (self.repository / "src").mkdir()
        (self.repository / "src/a.py").write_text("a = 1\n", encoding="utf-8")
        (self.repository / "src/b.py").write_text("b = 1\n", encoding="utf-8")
        (self.repository / "ignored").mkdir()
        (self.repository / "ignored/value.txt").write_text("ignored\n", encoding="utf-8")
        (self.repository / ".github").mkdir()
        (self.repository / ".github/workflow.yml").write_text("ignored\n", encoding="utf-8")
        previous = commit_trigger.scan_governed_files(self.repository)
        self.assertIn("README.md", previous)
        self.assertIn(".caprmedio_caprmedio/settings.toml", previous)
        self.assertNotIn("ignored/value.txt", previous)
        self.assertNotIn(".github/workflow.yml", previous)

        (self.repository / "src/a.py").write_text("a = 2\n", encoding="utf-8")
        (self.repository / "src/b.py").write_text("b = 2\n", encoding="utf-8")
        current = commit_trigger.scan_governed_files(self.repository)
        observations = commit_trigger.detect_watch_observations(
            previous,
            current,
            adapter_id=self.adapter.adapter_id,
            repository=self.repository,
            observed_at="2026-08-21T02:00:00Z",
        )
        self.assertEqual(1, len(observations))
        self.assertEqual("src", observations[0]["before_path"])
        self.assertEqual("src", observations[0]["after_path"])

    def test_cli_exposes_machine_readable_contract_and_unchanged_handoff(self) -> None:
        observation_path = self.repository / "observation.json"
        observation_path.write_text(json.dumps(self._observation()), encoding="utf-8")
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--repository",
                str(self.repository),
                "observe",
                "--adapter-id",
                self.adapter.adapter_id,
                "--input",
                str(observation_path),
            ],
            check=True,
            capture_output=True,
            text=True,
            env={**os.environ, **self.environment},
        )
        envelope = json.loads(completed.stdout)
        self.assertTrue(envelope["ok"])
        self.assertEqual(envelope["tool"], {"capability_id": "COMMIT_TRIGGER", "kind": "hook"})
        handoff = envelope["result"]["handoffs"][0]
        self.assertEqual(handoff["interface"], "COMMIT_CHANGE_SET")
        self.assertEqual(handoff["trigger"]["llm_session"]["app"], "codex")

    def test_runtime_install_is_content_addressed_and_self_contained(self) -> None:
        status = install_release(self.repository, apply=True, source_root=commit_trigger.PACKAGE_ROOT)

        self.assertTrue(status["installed"])
        self.assertTrue(status["verified"])
        release_root = self.repository / str(status["package_root"])
        self.assertTrue((release_root.parent / "manifest.toml").is_file())
        self.assertGreater(status["file_count"], 10)
        for relative in (
            "COMMIT_TRIGGER/commit_trigger.py",
            "COMMIT_CONTEXT/commit_context.py",
            "APPEND_CHANGE_RECORDS/append_change_records.py",
            "COMMIT_CHANGE_SET/commit_change_set.py",
        ):
            completed = subprocess.run(
                [sys.executable, "-I", "-B", str(release_root / relative), "--repository", str(self.repository), "describe"],
                check=True,
                capture_output=True,
                text=True,
                cwd=self.repository,
                env={"PATH": os.environ.get("PATH", "")},
            )
            self.assertTrue(json.loads(completed.stdout)["ok"], relative)

    def test_user_codex_hook_runs_installed_pipeline_and_commits_one_atom(self) -> None:
        (self.repository / ".gitignore").write_text(
            "/.caprmedio_runtime/\n/.caprmedio_tmp/\n/.codex/hooks.json\n",
            encoding="utf-8",
        )
        subject = ".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--subject.md"
        self._write_atom(subject, version=1, body="first")
        self._git("config", "github.username", "anatoly-m-maslennikov")
        self._git("add", ".gitignore", ".caprmedio_caprmedio")
        self._git("commit", "-qm", "governed fixture")

        installed = install_release(self.repository, apply=True, source_root=commit_trigger.PACKAGE_ROOT)
        entrypoint = self.repository / str(installed["package_root"]) / "COMMIT_TRIGGER/commit_trigger.py"
        subprocess.run(
            [
                sys.executable,
                "-I",
                "-B",
                str(entrypoint),
                "--repository",
                str(self.repository),
                "adapter",
                "install",
                "--adapter-id",
                self.adapter.adapter_id,
                "--application",
                "codex",
                "--host-session-env",
                "CODEX_THREAD_ID",
                "--fallback-session-env",
                "CODEX_SESSION_ID",
                "--apply",
            ],
            check=True,
            capture_output=True,
            text=True,
            cwd=self.repository,
        )
        hook_config = self.codex_home / "hooks.json"
        self.assertTrue(hook_config.is_file())
        self.assertFalse((self.repository / ".codex/hooks.json").exists())
        hook_document = json.loads(hook_config.read_text(encoding="utf-8"))
        self.assertEqual({"PreToolUse", "PostToolUse", "SessionStart", "Stop"}, set(hook_document["hooks"]))
        for event in hook_document["hooks"].values():
            command = event[-1]["hooks"][0]["command"]
            self.assertIn(commit_trigger.CODEX_ACTIVATION_KEY, command)
            self.assertNotIn(str(self.repository), command)
            self.assertNotIn(".caprmedio_runtime/tools/releases/", command)
        self.assertEqual(commit_trigger.MANAGED_GIT_HOOKS_PATH, commit_trigger._local_git_hooks_path(self.repository))
        for name in commit_trigger.GIT_HOOK_NAMES:
            self.assertTrue(os.access(self.repository / commit_trigger.MANAGED_GIT_HOOKS_PATH / name, os.X_OK))
        payload = {
            "session_id": self.environment["CODEX_THREAD_ID"],
            "tool_use_id": "tool-use-001",
            "cwd": str(self.repository),
        }

        for phase in ("pre", "post"):
            if phase == "post":
                self._write_atom(subject, version=2, body="second")
            completed = subprocess.run(
                [
                    sys.executable,
                    "-I",
                    "-B",
                    str(entrypoint),
                    "--repository",
                    str(self.repository),
                    "codex-hook",
                    phase,
                    "--adapter-id",
                    self.adapter.adapter_id,
                ],
                input=json.dumps(payload),
                check=True,
                capture_output=True,
                text=True,
                cwd=self.repository,
            )
            envelope = json.loads(completed.stdout)
            self.assertTrue(envelope["ok"], completed.stdout)

        self.assertEqual("committed", envelope["result"]["effect"], envelope)
        self.assertEqual(1, envelope["result"]["commit_count"])
        changed = self._git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").splitlines()
        self.assertIn(subject, changed)
        journals = [path for path in changed if path.startswith(".caprmedio_caprmedio/work_journal/")]
        self.assertEqual(1, len(journals))
        record = json.loads((self.repository / journals[0]).read_text(encoding="utf-8").splitlines()[-1])
        self.assertEqual(
            {"app": "codex", "uuid": self.environment["CODEX_THREAD_ID"]},
            record["llm_session"],
        )
        observations = list((self.repository / ".caprmedio_runtime/logs/git_hooks").glob("*.ndjson"))
        self.assertEqual(1, len(observations))
        observed = json.loads(observations[0].read_text(encoding="utf-8").splitlines()[-1])
        self.assertTrue(observed["governed"])
        self.assertTrue(observed["valid"])
        self.assertEqual(self._git("rev-parse", "HEAD").strip(), observed["commit"])
        self.assertEqual("", self._git("status", "--porcelain=v1"))

    def test_stop_reconciles_one_missed_change_and_rejects_ambiguous_session_ownership(self) -> None:
        (self.repository / ".gitignore").write_text(
            "/.caprmedio_runtime/\n/.caprmedio_tmp/\n/.codex/hooks.json\n",
            encoding="utf-8",
        )
        subject = ".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--subject.md"
        self._write_atom(subject, version=1, body="first")
        self._git("config", "github.username", "anatoly-m-maslennikov")
        self._git("add", ".gitignore", ".caprmedio_caprmedio")
        self._git("commit", "-qm", "governed fixture")
        install_release(self.repository, apply=True, source_root=commit_trigger.PACKAGE_ROOT)
        commit_trigger.adapter_operation(
            self.repository,
            "install",
            adapter=self.adapter,
            apply=True,
            manage_host_hooks=True,
        )
        payload = {"session_id": self.environment["CODEX_THREAD_ID"], "cwd": str(self.repository)}
        started = commit_trigger.codex_hook(self.repository, "start", self.adapter.adapter_id, payload)
        self.assertEqual("baseline-created", started["effect"])
        self._write_atom(subject, version=2, body="second")
        stopped = commit_trigger.codex_hook(self.repository, "stop", self.adapter.adapter_id, payload)
        self.assertEqual("reconciled", stopped["effect"])
        self.assertEqual(1, stopped["commit_count"])
        self.assertEqual("", self._git("status", "--porcelain=v1"))

        second_payload = {"session_id": "019f5920-04f6-70f2-8de7-828b7cccc69d", "cwd": str(self.repository)}
        commit_trigger.codex_hook(self.repository, "start", self.adapter.adapter_id, payload)
        commit_trigger.codex_hook(self.repository, "start", self.adapter.adapter_id, second_payload)
        self._write_atom(subject, version=3, body="third")
        ambiguous = commit_trigger.codex_hook(self.repository, "stop", self.adapter.adapter_id, payload)
        self.assertEqual("ambiguous-session-ownership", ambiguous["effect"])
        self.assertEqual(0, ambiguous["commit_count"])
        self.assertIn(subject, self._git("status", "--porcelain=v1"))

        missing_payload = {"session_id": "019f5930-04f6-70f2-8de7-828b7cccc69d", "cwd": str(self.repository)}
        missing = commit_trigger.codex_hook(self.repository, "stop", self.adapter.adapter_id, missing_payload)
        self.assertEqual("no-session-baseline", missing["effect"])

    @staticmethod
    def _run_hook(hook: Path) -> None:
        subprocess.run([str(hook)], check=True, capture_output=True, text=True)


if __name__ == "__main__":
    unittest.main()
