"""Retained integration tests for direct first-framework initialization.

The initializer uses the real canonical Work Journal and
``DirectActionSession``.  The only substituted boundary is immutable image
inspection; no test invokes Docker.  Fixture roots intentionally remain on
disk so a host cleanup refusal cannot conceal the evidence under test.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = RELEASE_ROOT.parent
for location in (RELEASE_ROOT, TOOLS_ROOT):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import framework_initialization as initialization  # noqa: E402
import work_journal  # noqa: E402
from direct_action_session import (  # noqa: E402
    ACTION_ATOM_RELATIVE,
    DirectActionJournalError,
    DirectActionSession,
    INITIALIZATION_ACTION_ID,
)
from framework_initialization import (  # noqa: E402
    FrameworkInitializationError,
    PACKAGE_IMAGE_LABEL,
    SOURCE_CONTEXT_IMAGE_LABEL,
    initialize_framework_runtime,
    plan_initial_framework_installation,
)
from release_image import DockerCommandResult, DockerSubprocessExecutor  # noqa: E402
from bootstrap_image import produce_initial_framework_image  # noqa: E402
from framework_compiler_currentness_fixture import ConfiguredCompilerFixture  # noqa: E402


IMAGE_ID = "sha256:" + "a" * 64
AUTHORIZATION = {
    "operator": "Anatoly Maslennikov",
    "authorization_ref": "tmp/operator-authorizations/initialize-framework.md",
}


def _repository_root() -> Path:
    for candidate in RELEASE_ROOT.parents:
        if (candidate / ".caprmedio_caprmedio/caprmedio_project_settings.toml").is_file():
            return candidate
    raise RuntimeError("repository root is unavailable")


REPOSITORY_ROOT = _repository_root()


class FakeImageInspectionExecutor:
    """Retained Docker protocol fixture; subprocess identity is patched at the boundary."""

    def __init__(self, *, manifest_sha256: str, source_context_sha256: str) -> None:
        self.manifest_sha256 = manifest_sha256
        self.source_context_sha256 = source_context_sha256
        self.calls: list[tuple[str, ...]] = []

    def run(self, argv, *, cwd: Path, timeout_seconds: float) -> DockerCommandResult:
        del cwd, timeout_seconds
        self.calls.append(tuple(argv))
        if argv[1] == "build":
            self.labels = {}
            for index, value in enumerate(argv):
                if value == "--label":
                    key, label = argv[index + 1].split("=", 1)
                    self.labels[key] = label
            Path(argv[argv.index("--iidfile") + 1]).write_text(IMAGE_ID + "\n", encoding="utf-8")
            self.canary = json.loads((Path(argv[-1]) / "bootstrap-canary.json").read_bytes())
            return DockerCommandResult(0, b"build\n", b"")
        if argv[1] == "run":
            return DockerCommandResult(0, json.dumps({
                "schema": "caprmedio.bootstrap_image_canary.v1",
                "manifest_sha256": self.canary["manifest_sha256"],
                "source_context_sha256": self.canary["source_context_sha256"],
                "verified_files": len(self.canary["package_rows"]),
                "mcp_tools": ["get_mcp_reload_status"],
            }).encode("utf-8"), b"")
        if tuple(argv[:3]) != ("docker", "image", "inspect"):
            raise AssertionError("unexpected Docker protocol command")
        payload = json.dumps([{
            "Id": IMAGE_ID,
            "Config": {
                "Labels": {
                    PACKAGE_IMAGE_LABEL: self.manifest_sha256,
                    SOURCE_CONTEXT_IMAGE_LABEL: self.source_context_sha256,
                },
            },
        }]).encode("utf-8")
        return DockerCommandResult(0, payload, b"")


class FrameworkInitializationJournalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.compiler_fixture = ConfiguredCompilerFixture.create()
        self.root = self.compiler_fixture.root
        (self.root / ".git").mkdir()
        self._write(
            ".caprmedio_caprmedio/caprmedio_project_settings.toml",
            b"[paths]\ncontrol_root = '.caprmedio_caprmedio'\n"
            b"journal_root = '.caprmedio_caprmedio/_journal'\n"
            b"runtime_root = '.caprmedio_runtime'\n",
        )
        self._write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool\n")
        self._write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py", b"app\n")
        self._write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py", b"server\n")
        self._write("102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md", b"prompt\n")
        self._write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md", b"# ca\n")
        self._write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml", b"name: ca\n")
        self._write("pyproject.toml", b"[project]\nname = 'bootstrap-fixture'\nversion = '0'\n")
        self._write("uv.lock", b"version = 1\n")
        self._write(
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile",
            (RELEASE_ROOT.parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile").read_bytes(),
        )
        source = REPOSITORY_ROOT / ACTION_ATOM_RELATIVE
        target = self.root / ACTION_ATOM_RELATIVE
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        shutil.copyfile(
            REPOSITORY_ROOT / ".caprmedio_caprmedio/operators_registry.toml",
            self.root / ".caprmedio_caprmedio/operators_registry.toml",
        )
        # The Journal settings are part of the compiler's current input view;
        # rebuild the retained canonical projection after adding them.
        self.compiler_fixture.materialize_current_projection()

    def _write(self, relative: str, payload: bytes) -> Path:
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        return target

    def _session(self) -> DirectActionSession:
        return DirectActionSession(
            self.root,
            author="anatoly-m",
            operator_authorization=AUTHORIZATION,
            now=lambda: dt.datetime(2026, 10, 5, 18, 0, tzinfo=dt.UTC),
        )

    def _events(self) -> list[dict[str, object]]:
        journal = self.root / ".caprmedio_caprmedio/_journal"
        events: list[dict[str, object]] = []
        for path in sorted(journal.glob("*.ndjson")):
            events.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines())
        return events

    def _initialize(
        self,
        session: DirectActionSession,
        *,
        requested_run_id: str = "initialize-framework-001",
    ) -> tuple[dict[str, object], FakeImageInspectionExecutor]:
        plan = plan_initial_framework_installation(self.root)
        inspector = FakeImageInspectionExecutor(
            manifest_sha256=plan.manifest_sha256,
            source_context_sha256=plan.source_context_sha256,
        )
        executor = DockerSubprocessExecutor()
        real_replace = os.replace

        def retained_fixture_replace(source: str | bytes | os.PathLike[str] | os.PathLike[bytes],
                                     target: str | bytes | os.PathLike[str] | os.PathLike[bytes]) -> None:
            source_path = Path(source)
            target_path = Path(target)
            if source_path.is_dir():
                # The host may deny the production atomic directory rename.
                # Retained fixtures emulate only that OS primitive; the
                # initializer still invokes its normal publication path.
                shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                return
            real_replace(source, target)

        executor = DockerSubprocessExecutor()
        with patch.object(DockerSubprocessExecutor, "run", side_effect=inspector.run):
            evidence = produce_initial_framework_image(plan, executor=executor)
            self.assertEqual("docker-subprocess", evidence.execution_kind)
            with patch("framework_initialization.os.replace", side_effect=retained_fixture_replace):
                value = initialize_framework_runtime(
                    self.root, journal=session, requested_run_id=requested_run_id,
                    image_digest=IMAGE_ID, image_executor=executor,
                )
        return value, inspector

    def test_initialization_records_one_real_direct_action_with_exact_effects(self) -> None:
        session = self._session()
        result, inspector = self._initialize(session)

        self.assertEqual("installed", result["state"])
        self.assertEqual(["build", "image", "run", "image"], [call[1] for call in inspector.calls])
        events = self._events()
        self.assertEqual(["started", "completed"], [event["event"] for event in events])
        started, terminal = events
        self.assertEqual(INITIALIZATION_ACTION_ID, started["action_id"])
        self.assertEqual(INITIALIZATION_ACTION_ID, terminal["action_id"])
        self.assertEqual("action", started["run"]["kind"])
        self.assertEqual(started["run"]["run_id"], terminal["run"]["run_id"])
        self.assertEqual(started["event_id"], next(iter(session.actual.values()))["event_id"])
        self.assertEqual(terminal["event_id"], result["terminal"]["event_id"])
        self.assertEqual(
            {"action_id", "kind", "manifest_sha256", "source_context_sha256", "image_digest"},
            set(next(iter(session.actual.values()))["intent"]),
        )
        expected_effects = [
            result["release_root"],
            ".caprmedio_runtime/framework/current.toml",
            ".agents/skills/ca",
            result["result_ref"],
        ]
        self.assertEqual(expected_effects, terminal["effect_refs"])
        self.assertEqual(expected_effects, result["terminal"]["effect_refs"])
        self.assertEqual(result["result_ref"], terminal["result_ref"])
        self.assertIn(str(result["manifest_sha256"]), (self.root / ".caprmedio_runtime/framework/current.toml").read_text())
        self.assertTrue((self.root / ".agents/skills/ca/SKILL.md").is_file())
        self.assertFalse((self.root / ".caprmedio_install/workflow_orchestrator").exists())

    def test_same_requested_run_is_inspection_only_and_never_creates_a_second_start(self) -> None:
        session = self._session()
        first, inspector = self._initialize(session)
        retry = self._session()
        intent = next(iter(session.actual.values()))["intent"]

        with self.assertRaises(DirectActionJournalError) as raised:
            retry.begin_action(
                action_id=INITIALIZATION_ACTION_ID,
                requested_run_id="initialize-framework-001",
                intent=intent,
            )

        self.assertEqual("direct-action-already-terminal", raised.exception.code)
        self.assertEqual(4, len(inspector.calls))
        self.assertEqual(["started", "completed"], [event["event"] for event in self._events()])
        self.assertEqual(first["release_root"], ".caprmedio_runtime/framework/releases/" + first["manifest_sha256"])

    def test_terminal_recording_failure_retains_effects_and_exact_pending_event(self) -> None:
        session = self._session()
        plan = plan_initial_framework_installation(self.root)
        inspector = FakeImageInspectionExecutor(
            manifest_sha256=plan.manifest_sha256,
            source_context_sha256=plan.source_context_sha256,
        )
        executor = DockerSubprocessExecutor()
        original_append = work_journal.append_sealed_events
        append_calls = 0
        real_replace = os.replace

        def fail_terminal_append(*args, **kwargs):
            nonlocal append_calls
            append_calls += 1
            if append_calls == 2:
                raise OSError("fixture terminal append denied")
            return original_append(*args, **kwargs)

        def retained_fixture_replace(source, target):
            source_path = Path(source)
            target_path = Path(target)
            if source_path.is_dir():
                shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                return None
            return real_replace(source, target)

        with patch.object(DockerSubprocessExecutor, "run", side_effect=inspector.run):
            evidence = produce_initial_framework_image(plan, executor=executor)
            self.assertEqual("docker-subprocess", evidence.execution_kind)
            with (
                patch("framework_initialization.os.replace", side_effect=retained_fixture_replace),
                patch.object(work_journal, "append_sealed_events", side_effect=fail_terminal_append),
            ):
                result = initialize_framework_runtime(
                    self.root, journal=session, requested_run_id="initialize-framework-pending",
                    image_digest=IMAGE_ID, image_executor=executor,
                )

        self.assertEqual("recording_pending", result["state"])
        self.assertEqual("initial-journal-terminal-unavailable", result["reason"])
        self.assertEqual(["started"], [event["event"] for event in self._events()])
        self.assertTrue((self.root / ".caprmedio_runtime/framework/current.toml").is_file())
        self.assertTrue((self.root / ".agents/skills/ca/SKILL.md").is_file())
        pending_id = next(iter(session.pending))
        _retained, pending, _context, _path = work_journal._read_pending_event(self.root, pending_id)
        self.assertEqual("completed", pending["event"])
        self.assertEqual("completed", pending["outcome"])
        self.assertIn(".caprmedio_runtime/framework/current.toml", pending["effect_refs"])
        self.assertIn(".agents/skills/ca", pending["effect_refs"])
        self.assertIn(pending["result_ref"], pending["effect_refs"])
        resumed = self._session()
        intent = next(iter(session.actual.values()))["intent"]
        with self.assertRaises(DirectActionJournalError) as recovery:
            resumed.begin_action(
                action_id=INITIALIZATION_ACTION_ID,
                requested_run_id="initialize-framework-pending",
                intent=intent,
            )
        self.assertEqual("direct-action-recovery-required", recovery.exception.code)
        self.assertEqual(["started"], [event["event"] for event in self._events()])


if __name__ == "__main__":
    unittest.main()
