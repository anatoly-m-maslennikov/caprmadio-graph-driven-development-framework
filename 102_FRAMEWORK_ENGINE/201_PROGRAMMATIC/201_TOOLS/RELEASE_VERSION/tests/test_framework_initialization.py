"""First-installation fixtures for the Framework Runtime boundary.

These fixtures deliberately retain their temporary project roots.  The
managed host can deny directory cleanup, and the retained carriers make any
failed publication inspectable instead of disguising it as a successful test
cleanup.
"""

from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from framework_initialization import (  # noqa: E402
    FrameworkInitializationError,
    PACKAGE_IMAGE_LABEL,
    SOURCE_CONTEXT_IMAGE_LABEL,
    initialize_framework_runtime,
    plan_initial_framework_installation,
)
import framework_initialization as initialization  # noqa: E402
from release_handoff import _selector_release  # noqa: E402
from release_image import DockerCommandResult  # noqa: E402
from release_packaging import _current_release, _verify_release  # noqa: E402


IMAGE_ID = "sha256:" + "a" * 64


class RecordingSession:
    """A strict stand-in for the one shared direct-Action Journal writer."""

    def __init__(self) -> None:
        self.started: list[str] = []
        self.observed: list[tuple[str, str, list[str]]] = []
        self.finished: list[dict[str, object]] = []

    def begin_action(self, *, action_id: str, requested_run_id: str, intent: dict[str, object]) -> dict[str, str]:
        self.action_id = action_id
        self.intent = dict(intent)
        self.started.append(requested_run_id)
        return {"run_id": f"actual-{requested_run_id}", "disposition": "started"}

    def record_effects(self, run_id: str, *, result_ref: str, effect_refs: list[str]) -> None:
        self.observed.append((run_id, result_ref, list(effect_refs)))

    def finish_action(self, run_id: str, *, outcome: str, result_ref: str, effect_refs: list[str], report_ref=None):
        record = {
            "run_id": run_id,
            "outcome": outcome,
            "result_ref": result_ref,
            "effect_refs": list(effect_refs),
            "report_ref": report_ref,
            "disposition": "terminal",
            "event_id": "event-terminal",
        }
        self.finished.append(record)
        return record


class InspectingDocker:
    def __init__(
        self,
        *,
        manifest_sha256: str | None = None,
        source_context_sha256: str | None = None,
        exit_code: int = 0,
    ) -> None:
        self.manifest_sha256 = manifest_sha256
        self.source_context_sha256 = source_context_sha256
        self.exit_code = exit_code
        self.calls: list[tuple[str, ...]] = []

    def run(self, argv, *, cwd: Path, timeout_seconds: float) -> DockerCommandResult:
        self.calls.append(tuple(argv))
        assert argv[:3] == ("docker", "image", "inspect")
        labels = {
            PACKAGE_IMAGE_LABEL: self.manifest_sha256,
            SOURCE_CONTEXT_IMAGE_LABEL: self.source_context_sha256,
        }
        payload = json.dumps([{"Id": IMAGE_ID, "Config": {"Labels": labels}}]).encode()
        return DockerCommandResult(self.exit_code, payload, b"")


class PendingTerminalSession(RecordingSession):
    def finish_action(self, *args, **kwargs):
        record = super().finish_action(*args, **kwargs)
        record["disposition"] = "pending"
        return record


class DirectActionRecoveryRequired(Exception):
    code = "direct-action-recovery-required"


class RecoveryRequiredSession(RecordingSession):
    def begin_action(self, **kwargs):
        raise DirectActionRecoveryRequired("existing direct Action must be recovered before retry")


class BoundaryChangedSession(RecordingSession):
    """Simulate a distinct invocation publishing after this Action starts."""

    def __init__(self, root: Path) -> None:
        super().__init__()
        self.root = root

    def begin_action(self, **kwargs):
        started = super().begin_action(**kwargs)
        selector = self.root / ".caprmedio_runtime/framework/current.toml"
        selector.parent.mkdir(parents=True, exist_ok=True)
        selector.write_text('release = "other"\n', encoding="utf-8")
        return started


class FrameworkInitializationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="caprmedio-framework-initialization-")).resolve()
        self._write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool\n")
        self._write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py", b"app\n")
        self._write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py", b"server\n")
        self._write("102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md", b"prompt\n")
        self._write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md", b"# ca\n")
        self._write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml", b"name: ca\n")
        self._write(
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/source.md",
            b"source\n",
        )
        self._write(
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "04_requirement/compiled.md",
            b"compiled\n",
        )
        self.session = RecordingSession()

    def _write(self, relative: str, payload: bytes) -> Path:
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        return target

    def _initialize(self, docker: InspectingDocker, *, emulate_directory_rename: bool = False):
        def invoke():
            return initialize_framework_runtime(
                self.root,
                journal=self.session,
                requested_run_id="bootstrap-action",
                image_digest=IMAGE_ID,
                image_executor=docker,
            )

        if not emulate_directory_rename:
            return invoke()

        real_replace = os.replace

        def retained_fixture_replace(source, target):
            source_path = Path(source)
            target_path = Path(target)
            if source_path.is_dir():
                # The managed macOS host denies the production atomic
                # directory rename even in retained fixtures.  Simulate only
                # that OS primitive in this fixture; source staging remains
                # inspectable and production still calls os.replace directly.
                shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                return None
            return real_replace(source, target)

        with patch("framework_initialization.os.replace", side_effect=retained_fixture_replace):
            return invoke()

    def test_initializes_complete_content_addressed_package_selector_skill_and_canonical_terminal(self) -> None:
        plan = plan_initial_framework_installation(self.root)
        result = self._initialize(
            InspectingDocker(
                manifest_sha256=plan.manifest_sha256,
                source_context_sha256=plan.source_context_sha256,
            ),
            emulate_directory_rename=True,
        )

        package = self.root / result["release_root"]
        selector = self.root / ".caprmedio_runtime/framework/current.toml"
        public_skill = self.root / ".agents/skills/ca"
        self.assertEqual(result["state"], "installed")
        self.assertTrue((package / "manifest.toml").is_file())
        self.assertTrue((package / "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py").is_file())
        self.assertTrue((package / "METHODOLOGY/sources/001_CORE_META_MODEL/source.md").is_file())
        self.assertTrue((package / "METHODOLOGY/compiled/04_requirement/compiled.md").is_file())
        self.assertFalse((package / "METHODOLOGY/compiled/000_APPLICABLE_MTHD_sources").exists())
        self.assertTrue((package / "SKILLS/ca/SKILL.md").is_file())
        self.assertEqual((public_skill / "SKILL.md").read_bytes(), (package / "SKILLS/ca/SKILL.md").read_bytes())
        self.assertFalse((self.root / ".git/hooks").exists())
        self.assertIn(plan.release, selector.read_text(encoding="utf-8"))
        self.assertEqual(self.session.started, ["bootstrap-action"])
        self.assertEqual(self.session.action_id, "FRAMEWORK_INITIALIZATION")
        self.assertEqual(self.session.intent["manifest_sha256"], plan.manifest_sha256)
        self.assertEqual(self.session.intent["source_context_sha256"], plan.source_context_sha256)
        self.assertEqual(self.session.intent["image_digest"], IMAGE_ID)
        self.assertEqual(self.session.finished[-1]["outcome"], "completed")
        self.assertIn(result["result_ref"], self.session.finished[-1]["effect_refs"])

        # The initial package is not a Release Version promotion, but it must
        # be a real N carrier that the established read-only helpers can
        # reopen without a bootstrap-only selector exception.
        selected, selector_bytes = _current_release(self.root)
        self.assertEqual(selected, plan.manifest_sha256)
        self.assertEqual(_selector_release(self.root), plan.manifest_sha256)
        self.assertIn(plan.manifest_sha256.encode("utf-8"), selector_bytes)
        _verify_release(package, plan.manifest_bytes.decode("utf-8"), initialization._release_rows(plan.rows))

    def test_refuses_existing_framework_state_without_replacing_it(self) -> None:
        selector = self._write(".caprmedio_runtime/framework/current.toml", b'release = "old"\n')
        before = selector.read_bytes()
        with self.assertRaises(FrameworkInitializationError) as raised:
            plan_initial_framework_installation(self.root)
        self.assertEqual(raised.exception.code, "initial-runtime-not-empty")
        self.assertEqual(selector.read_bytes(), before)

    def test_refuses_the_retired_compiled_copy_when_canonical_role_folders_are_absent(self) -> None:
        # Use an independent retained fixture rather than deleting a role
        # folder; this host intentionally does not guarantee fixture cleanup.
        retired_root = Path(
            tempfile.mkdtemp(prefix="caprmedio-framework-obsolete-", dir=self.root.parent)
        )
        target = retired_root / ".caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY/compiled.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b"retired\n")
        with self.assertRaises(FrameworkInitializationError) as raised:
            initialization._compiled_methodology_files(retired_root)
        self.assertEqual(raised.exception.code, "initial-methodology-compiled-obsolete")

    def test_ignores_an_empty_legacy_compiled_role_sibling(self) -> None:
        """Empty retained role directories do not make the whole inventory empty."""
        legacy_role = self.root / (
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/09_ops"
        )
        legacy_role.mkdir()

        files = initialization._compiled_methodology_files(self.root)

        self.assertEqual(
            files,
            [
                self.root / (
                    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
                    "04_requirement/compiled.md"
                )
            ],
        )

    def test_refuses_when_all_compiled_role_directories_are_empty(self) -> None:
        empty_root = Path(
            tempfile.mkdtemp(prefix="caprmedio-framework-empty-compiled-", dir=self.root.parent)
        )
        compiled_root = empty_root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"
        (compiled_root / "04_requirement").mkdir(parents=True)
        (compiled_root / "09_ops").mkdir()

        with self.assertRaises(FrameworkInitializationError) as raised:
            initialization._compiled_methodology_files(empty_root)

        self.assertEqual(raised.exception.code, "initial-methodology-compiled-missing")

    def test_refuses_a_symlinked_compiled_role_sibling(self) -> None:
        safe_target = self.root / "retained-compiled-role"
        safe_target.mkdir()
        legacy_role = self.root / (
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/09_ops"
        )
        legacy_role.symlink_to(safe_target, target_is_directory=True)

        with self.assertRaises(FrameworkInitializationError) as raised:
            initialization._compiled_methodology_files(self.root)

        self.assertEqual(raised.exception.code, "initial-methodology-compiled-invalid")

    def test_preserves_direct_action_recovery_refusal_without_any_publication(self) -> None:
        self.session = RecoveryRequiredSession()
        plan = plan_initial_framework_installation(self.root)
        with self.assertRaises(FrameworkInitializationError) as raised:
            self._initialize(
                InspectingDocker(
                    manifest_sha256=plan.manifest_sha256,
                    source_context_sha256=plan.source_context_sha256,
                )
            )
        self.assertEqual(raised.exception.code, "direct-action-recovery-required")
        self.assertFalse((self.root / ".caprmedio_runtime/framework/current.toml").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/framework/releases").exists())
        self.assertFalse((self.root / ".agents/skills/ca").exists())

    def test_rechecks_the_empty_boundary_after_started_evidence_before_any_effect(self) -> None:
        self.session = BoundaryChangedSession(self.root)
        plan = plan_initial_framework_installation(self.root)
        result = self._initialize(
            InspectingDocker(
                manifest_sha256=plan.manifest_sha256,
                source_context_sha256=plan.source_context_sha256,
            )
        )
        self.assertEqual(result["state"], "blocked")
        self.assertEqual(result["reason"], "initial-runtime-not-empty")
        self.assertEqual(
            (self.root / ".caprmedio_runtime/framework/current.toml").read_text(encoding="utf-8"),
            'release = "other"\n',
        )
        self.assertFalse((self.root / ".caprmedio_runtime/framework/releases").exists())
        self.assertFalse((self.root / ".agents/skills/ca").exists())

    def test_refuses_a_zero_byte_selector_as_existing_framework_state(self) -> None:
        selector = self._write(".caprmedio_runtime/framework/current.toml", b"")
        with self.assertRaises(FrameworkInitializationError) as raised:
            plan_initial_framework_installation(self.root)
        self.assertEqual(raised.exception.code, "initial-runtime-not-empty")
        self.assertEqual(selector.read_bytes(), b"")

    def test_accepts_only_empty_regular_release_and_skill_directories(self) -> None:
        (self.root / ".caprmedio_runtime/framework/releases").mkdir(parents=True)
        (self.root / ".agents/skills/ca").mkdir(parents=True)
        plan = plan_initial_framework_installation(self.root)
        result = self._initialize(
            InspectingDocker(
                manifest_sha256=plan.manifest_sha256,
                source_context_sha256=plan.source_context_sha256,
            ),
            emulate_directory_rename=True,
        )
        self.assertEqual(result["state"], "installed")
        self.assertTrue((self.root / ".agents/skills/ca/SKILL.md").is_file())

    def test_refuses_existing_project_local_ca_without_overwriting_it(self) -> None:
        skill = self._write(".agents/skills/ca/SKILL.md", b"existing project skill\n")
        with self.assertRaises(FrameworkInitializationError) as raised:
            plan_initial_framework_installation(self.root)
        self.assertEqual(raised.exception.code, "initial-skill-not-empty")
        self.assertEqual(skill.read_bytes(), b"existing project skill\n")

    def test_refuses_a_symlinked_agents_ancestor_before_any_staging_or_copy(self) -> None:
        safe_target = self.root / "retained-outside-agents"
        safe_target.mkdir()
        (self.root / ".agents").symlink_to(safe_target, target_is_directory=True)
        with self.assertRaises(FrameworkInitializationError) as raised:
            plan_initial_framework_installation(self.root)
        self.assertEqual(raised.exception.code, "initial-path-unsafe")
        self.assertFalse((safe_target / "skills").exists())

    def test_rejects_image_that_does_not_bind_the_exact_manifest_before_package_or_skill_effects(self) -> None:
        plan = plan_initial_framework_installation(self.root)
        docker = InspectingDocker(manifest_sha256="0" * 64, source_context_sha256=plan.source_context_sha256)
        result = self._initialize(docker)
        self.assertEqual(result["state"], "blocked")
        self.assertEqual(result["reason"], "image-package-binding-invalid")
        self.assertFalse((self.root / ".caprmedio_runtime/framework/current.toml").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/framework/releases").exists())
        self.assertFalse((self.root / ".agents/skills/ca").exists())
        self.assertEqual(self.session.finished[-1]["outcome"], "failed")

    def test_rejects_image_with_wrong_sealed_source_context_before_package_or_skill_effects(self) -> None:
        plan = plan_initial_framework_installation(self.root)
        result = self._initialize(
            InspectingDocker(manifest_sha256=plan.manifest_sha256, source_context_sha256="0" * 64)
        )
        self.assertEqual(result["state"], "blocked")
        self.assertEqual(result["reason"], "image-source-context-binding-invalid")
        self.assertFalse((self.root / ".caprmedio_runtime/framework/current.toml").exists())
        self.assertFalse((self.root / ".agents/skills/ca").exists())

    def test_directory_rename_failure_is_truthful_partial_without_selector_or_public_skill(self) -> None:
        plan = plan_initial_framework_installation(self.root)
        docker = InspectingDocker(
            manifest_sha256=plan.manifest_sha256,
            source_context_sha256=plan.source_context_sha256,
        )
        real_replace = os.replace

        def deny_directory_rename(source, target):
            if Path(source).is_dir():
                raise PermissionError("fixture denies directory rename")
            return real_replace(source, target)

        with patch("framework_initialization.os.replace", side_effect=deny_directory_rename):
            result = self._initialize(docker)
        self.assertEqual(result["state"], "partial")
        self.assertEqual(result["reason"], "initial-package-publication-failed")
        self.assertFalse((self.root / ".caprmedio_runtime/framework/current.toml").exists())
        self.assertFalse((self.root / ".agents/skills/ca").exists())
        self.assertEqual(self.session.finished[-1]["outcome"], "partial")

    def test_skill_publication_failure_never_activates_the_selector(self) -> None:
        plan = plan_initial_framework_installation(self.root)
        docker = InspectingDocker(
            manifest_sha256=plan.manifest_sha256,
            source_context_sha256=plan.source_context_sha256,
        )
        real_replace = os.replace

        def publish_skill_failure(source, target):
            source_path = Path(source)
            target_path = Path(target)
            if source_path.is_dir() and target_path == self.root / ".agents/skills/ca":
                raise PermissionError("fixture denies Skill publication")
            if source_path.is_dir():
                shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                return None
            return real_replace(source, target)

        with patch("framework_initialization.os.replace", side_effect=publish_skill_failure):
            result = self._initialize(docker)
        self.assertEqual(result["state"], "partial")
        self.assertEqual(result["reason"], "initial-skill-publication-failed")
        self.assertTrue((self.root / ".caprmedio_runtime/framework/releases" / plan.manifest_sha256).is_dir())
        self.assertFalse((self.root / ".caprmedio_runtime/framework/current.toml").exists())
        self.assertFalse((self.root / ".agents/skills/ca").exists())

    def test_selector_publication_failure_leaves_the_complete_skill_unselected(self) -> None:
        plan = plan_initial_framework_installation(self.root)
        docker = InspectingDocker(
            manifest_sha256=plan.manifest_sha256,
            source_context_sha256=plan.source_context_sha256,
        )
        real_replace = os.replace

        def publish_selector_failure(source, target):
            source_path = Path(source)
            target_path = Path(target)
            if target_path == self.root / ".caprmedio_runtime/framework/current.toml":
                raise PermissionError("fixture denies selector publication")
            if source_path.is_dir():
                shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                return None
            return real_replace(source, target)

        with patch("framework_initialization.os.replace", side_effect=publish_selector_failure):
            result = self._initialize(docker)
        self.assertEqual(result["state"], "partial")
        self.assertEqual(result["reason"], "initial-selector-publication-failed")
        self.assertFalse((self.root / ".caprmedio_runtime/framework/current.toml").exists())
        self.assertTrue((self.root / ".agents/skills/ca/SKILL.md").is_file())
        self.assertEqual(self.session.finished[-1]["outcome"], "partial")

    def test_nonterminal_journal_receipt_retains_actual_published_carriers_as_recording_pending(self) -> None:
        self.session = PendingTerminalSession()
        plan = plan_initial_framework_installation(self.root)
        result = self._initialize(
            InspectingDocker(
                manifest_sha256=plan.manifest_sha256,
                source_context_sha256=plan.source_context_sha256,
            ),
            emulate_directory_rename=True,
        )
        self.assertEqual(result["state"], "recording_pending")
        self.assertTrue((self.root / ".caprmedio_runtime/framework/current.toml").is_file())
        self.assertTrue((self.root / ".agents/skills/ca/SKILL.md").is_file())
        self.assertEqual(result["terminal"]["disposition"], "pending")

    def test_rejects_hook_carrier_before_publication(self) -> None:
        self._write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/hooks/pre-commit", b"#!/bin/sh\n")
        with self.assertRaises(FrameworkInitializationError) as raised:
            plan_initial_framework_installation(self.root)
        self.assertEqual(raised.exception.code, "initial-skill-hook-forbidden")
        self.assertFalse((self.root / ".agents/skills/ca").exists())


if __name__ == "__main__":
    unittest.main()
