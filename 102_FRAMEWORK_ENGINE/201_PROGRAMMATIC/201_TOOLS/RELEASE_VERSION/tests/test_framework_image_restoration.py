"""Test-first retained-byte contract for CA-O-187 image restoration.

All Docker responses below are fixture data.  A ``docker-subprocess`` marker
created by a patched subprocess boundary is explicitly not a live-Docker
acceptance claim.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = RELEASE_ROOT.parents[3]
TEST_ROOT = Path(__file__).resolve().parent
TOOLS_ROOT = RELEASE_ROOT.parent
for directory in (RELEASE_ROOT, TOOLS_ROOT, TEST_ROOT):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

from bootstrap_image_golden.fixture import materialize  # noqa: E402
from bootstrap_image import (  # noqa: E402
    produce_initial_framework_image,
    produce_retained_framework_image,
    read_retained_initial_framework_image,
)
from framework_image_restoration import (  # noqa: E402
    recover_framework_image_journal,
    recover_framework_image_terminal,
    restore_framework_image,
)
from framework_initialization import (  # noqa: E402
    PACKAGE_IMAGE_LABEL,
    SOURCE_CONTEXT_IMAGE_LABEL,
    initialize_framework_runtime,
    plan_initial_framework_installation,
)
from framework_compiler_currentness import CanonicalCompilerCurrentness  # noqa: E402
import framework_initialization as initialization  # noqa: E402
import framework_image_restoration as restoration  # noqa: E402
from release_image import DockerCommandResult, DockerSubprocessExecutor  # noqa: E402
from selector_publication_lock import (  # noqa: E402
    SelectorPublicationLockError,
    selector_publication_lock,
)
import work_journal  # noqa: E402
from direct_action_session import DirectActionJournalError, DirectActionSession  # noqa: E402


OLD_IMAGE = "sha256:" + "a" * 64
NEW_IMAGE = "sha256:" + "b" * 64
O187 = (
    "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/"
    "003_PROJECT_CONFIGURATION/09_operations/"
    "CA-O-187-PROJECT_CONFIGURATION-ACTION--restore-the-selected-missing-bootstrap-image.md"
)
O187_SHA256 = "6e0320a7026f37c6e0e4199051d47a4c597cdbe22bb5fb1bfb7b0626258852c1"


class RecordingJournal:
    def __init__(self) -> None:
        self.intents: list[dict] = []
        self.effects: list[list[str]] = []
        self.terminal = "terminal"
        self.trace: list[str] = []

    def begin_action(self, *, action_id, requested_run_id, intent):
        self.trace.append("started")
        self.intents.append(dict(intent))
        return {"run_id": f"run:{requested_run_id}", "disposition": "started"}

    def record_effects(self, _run_id, *, result_ref, effect_refs):
        del result_ref
        self.trace.append("effects")
        self.effects.append(list(effect_refs))

    def finish_action(self, run_id, *, outcome, result_ref, effect_refs, report_ref=None):
        del result_ref, effect_refs, report_ref
        self.trace.append("terminal")
        return {"run_id": run_id, "outcome": outcome, "disposition": self.terminal}


class RefusingJournal(RecordingJournal):
    def begin_action(self, **kwargs):
        del kwargs
        self.trace.append("refused")
        raise PermissionError("fixture authorization refused")


class FixtureDocker:
    """Recorded fixture transport; it is never treated as a live Docker proof."""

    def __init__(self, manifest, source_context, *, replacement=NEW_IMAGE) -> None:
        self.manifest = manifest
        self.source_context = source_context
        self.replacement = replacement
        self.calls: list[tuple[str, ...]] = []
        self.old_state = "absent"
        self.old_inspections = 0
        self.fail = None
        self.labels = {
            PACKAGE_IMAGE_LABEL: manifest,
            SOURCE_CONTEXT_IMAGE_LABEL: source_context,
        }

    def run(self, argv, *, cwd, timeout_seconds):
        del cwd, timeout_seconds
        call = tuple(argv)
        self.calls.append(call)
        if call[:3] == ("docker", "image", "inspect") and call[-1] == OLD_IMAGE:
            self.old_inspections += 1
            if self.old_state == "absent" and self.old_inspections == 1:
                return DockerCommandResult(1, b"", b"No such image", False)
            if self.old_state == "daemon-error":
                raise OSError("fixture daemon unavailable")
        if self.fail == "timeout":
            return DockerCommandResult(1, b"", b"fixture timeout", True)
        if "build" in call:
            Path(call[call.index("--iidfile") + 1]).write_text(self.replacement + "\n", encoding="utf-8")
            self.canary = json.loads((Path(call[-1]) / "bootstrap-canary.json").read_bytes())
            return DockerCommandResult(0, b"build\n", b"", False)
        if call[:3] == ("docker", "image", "inspect"):
            return DockerCommandResult(0, json.dumps([{"Id": self.replacement, "Config": {"Labels": self.labels}}]).encode(), b"", False)
        if self.fail == "canary":
            return DockerCommandResult(1, b"", b"fixture canary failed", False)
        return DockerCommandResult(0, json.dumps({
            "schema": "caprmedio.bootstrap_image_canary.v1",
            "image_digest": self.replacement,
            "manifest_sha256": self.manifest,
            "source_context_sha256": self.source_context,
            "verified_files": len(self.canary["package_rows"]),
            "mcp_tools": ["get_mcp_reload_status", "query_artifact"],
        }).encode(), b"", False)


class FrameworkImageRestorationTests(unittest.TestCase):
    def setUp(self) -> None:
        retained = PROJECT_ROOT / ".caprmedio_tmp/tests/framework-image-restoration"
        retained.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="case-", dir=retained)).resolve()
        materialize(self.root)
        (self.root / ".git").mkdir(exist_ok=True)
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        settings.parent.mkdir(parents=True, exist_ok=True)
        settings.write_text(
            "[paths]\ncontrol_root = '.caprmedio_caprmedio'\n"
            "journal_root = '.caprmedio_caprmedio/_journal'\nruntime_root = '.caprmedio_runtime'\n",
            encoding="utf-8",
        )
        shutil.copyfile(
            PROJECT_ROOT / ".caprmedio_caprmedio/operators_registry.toml",
            self.root / ".caprmedio_caprmedio/operators_registry.toml",
        )
        source = PROJECT_ROOT / ".caprmedio_caprmedio" / O187
        self.assertEqual(O187_SHA256, hashlib.sha256(source.read_bytes()).hexdigest())
        target = self.root / ".caprmedio_caprmedio" / O187
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        self.currentness = CanonicalCompilerCurrentness(
            compiled_root=".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY",
            source_root=".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources",
            compiler_entrypoint="102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py",
            compiler_entrypoint_sha256="c" * 64, source_frontier_digest="d" * 64,
            output_tree_digest="e" * 64, output_plan_sha256="f" * 64,
            source_snapshot=(("fixture", "a" * 64),),
        )
        with patch.object(initialization, "verify_canonical_compiler_currentness", return_value=self.currentness):
            self.plan = plan_initial_framework_installation(self.root)
        self.docker = FixtureDocker(self.plan.manifest_sha256, self.plan.source_context_sha256, replacement=OLD_IMAGE)
        # First-installation reopens its fresh image proof.  The restoration
        # scenario starts only after this fixture-only old image is absent.
        self.docker.old_state = "available"
        self.journal = RecordingJournal()
        self._install_old_n()
        self.docker.replacement = NEW_IMAGE
        self.docker.old_state = "absent"
        self.docker.old_inspections = 0
        self.docker.calls.clear()
        self.journal.trace.clear()
        self.journal.intents.clear()
        self.journal.effects.clear()
        self.selector = self.root / ".caprmedio_runtime/framework/current.toml"
        self.selector_before = self.selector.read_bytes()
        self.package_before = self._inventory(self.root / ".caprmedio_runtime/framework/releases" / self.plan.release)
        self.skill_before = self._inventory(self.root / ".agents/skills/ca")

    def _install_old_n(self) -> None:
        real_replace = os.replace

        def retained_replace(source, target):
            if Path(source).is_dir():
                shutil.copytree(source, target, dirs_exist_ok=True)
                return None
            return real_replace(source, target)

        executor = DockerSubprocessExecutor()
        with patch.object(DockerSubprocessExecutor, "run", side_effect=self.docker.run):
            proof = produce_initial_framework_image(self.plan, executor=executor)
            self.assertEqual("docker-subprocess", proof.execution_kind)  # fixture marker, not live proof
            with (
                patch.object(initialization, "verify_canonical_compiler_currentness", return_value=self.currentness),
                patch("framework_initialization.os.replace", side_effect=retained_replace),
            ):
                result = initialize_framework_runtime(
                    self.root, journal=self.journal, requested_run_id="bootstrap-fixture",
                    image_digest=OLD_IMAGE, image_executor=executor,
                )
        self.assertEqual("installed", result["state"])
        self.assertEqual(OLD_IMAGE, read_retained_initial_framework_image(self.root, self.plan.release, OLD_IMAGE).image_digest)

    @staticmethod
    def _inventory(root: Path) -> dict[str, tuple[bytes, int]]:
        return {path.relative_to(root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
                for path in root.rglob("*") if path.is_file()}

    def restore(self):
        return self.restore_with(self.journal)

    def restore_with(self, journal, *, requested_run_id="restore-fixture", retry_of_terminal_event_id=None):
        # Preserve the real executor type gate.  Only its process boundary is
        # patched, so this remains fixture evidence rather than live proof.
        with patch.object(DockerSubprocessExecutor, "run", side_effect=self.docker.run):
            return restore_framework_image(
                self.root, journal=journal, requested_run_id=requested_run_id,
                expected_selector_sha256=hashlib.sha256(self.selector_before).hexdigest(),
                image_executor=DockerSubprocessExecutor(),
                retry_of_terminal_event_id=retry_of_terminal_event_id,
            )

    def restoration_session(self):
        return DirectActionSession(
            self.root,
            author="anatoly-m",
            operator_authorization={
                "operator": "Anatoly Maslennikov",
                "authorization_ref": "tmp/operator-authorizations/restoration.md",
            },
            action_id="FRAMEWORK_IMAGE_RESTORATION",
        )

    def test_same_image_id_restores_without_rewriting_selector_package_skill_or_original_proof(self):
        self.docker.replacement = OLD_IMAGE
        original = read_retained_initial_framework_image(self.root, self.plan.release, OLD_IMAGE)
        proof_before = (self.root / original.evidence_root / "evidence.toml").read_bytes()
        result = self.restore()
        self.assertEqual("restored", result["state"], result)
        self.assertEqual(self.selector_before, self.selector.read_bytes())
        self.assertEqual(self.package_before, self._inventory(self.root / ".caprmedio_runtime/framework/releases" / self.plan.release))
        self.assertEqual(self.skill_before, self._inventory(self.root / ".agents/skills/ca"))
        self.assertEqual(proof_before, (self.root / original.evidence_root / "evidence.toml").read_bytes())
        self.assertEqual(OLD_IMAGE, read_retained_initial_framework_image(self.root, self.plan.release, OLD_IMAGE).image_digest)
        self.assertEqual(["started", "effects", "terminal"], self.journal.trace)

    def test_different_image_id_restores_only_image_digest_and_new_proof_reopens_in_retained_reader(self):
        result = self.restore()
        self.assertEqual("restored", result["state"])
        self.assertEqual(self.selector_before.replace(OLD_IMAGE.encode(), NEW_IMAGE.encode()), self.selector.read_bytes())
        self.assertEqual(self.package_before, self._inventory(self.root / ".caprmedio_runtime/framework/releases" / self.plan.release))
        self.assertEqual(self.skill_before, self._inventory(self.root / ".agents/skills/ca"))
        self.assertEqual(NEW_IMAGE, read_retained_initial_framework_image(self.root, self.plan.release, NEW_IMAGE).image_digest)
        self.assertTrue(any("build" in call for call in self.docker.calls))
        self.assertGreaterEqual(sum(call[:3] == ("docker", "image", "inspect") for call in self.docker.calls), 2)
        self.assertTrue(any(call[:2] == ("docker", "run") for call in self.docker.calls))
        restoration = self.root / ".caprmedio_runtime/framework_image_restoration"
        self.assertTrue(any(path.is_file() for path in restoration.rglob("result.json")))

    def test_real_session_different_image_terminal_has_unique_effect_references(self):
        with self.restoration_session() as session:
            restored = self.restore_with(session, requested_run_id="restore-different-real-session")
        self.assertEqual("restored", restored["state"], restored)
        self.assertEqual("terminal", restored["terminal"]["disposition"])
        self.assertEqual(NEW_IMAGE, restored["image_digest"])
        direct_action = __import__("direct_action_session")
        event, _receipt = direct_action._reopen_event(self.root, restored["terminal"]["event_id"])
        self.assertEqual("completed", event["event"])
        self.assertEqual(len(event["effect_refs"]), len(set(event["effect_refs"])))
        self.assertIn(restored["result_ref"], event["effect_refs"])
        self.assertEqual(self.selector_before.replace(OLD_IMAGE.encode(), NEW_IMAGE.encode()), self.selector.read_bytes())

    def test_reopened_session_records_historical_duplicate_result_without_replaying_effects(self):
        """A fixture-only legacy alias may be terminalized, but never replayed.

        The patched normalizer models the pre-repair raw result shape.  Its
        Docker transcript is still fixture data, not evidence of a live run.
        """
        def historical_duplicate(values):
            # Before the repair, the producer passed its two canonical aliases
            # through unchanged.  Do not forge a novel duplicate shape.
            return list(values)

        with patch.object(restoration, "_stable_effect_refs", side_effect=historical_duplicate):
            with self.restoration_session() as original_session:
                pending = self.restore_with(
                    original_session,
                    requested_run_id="restore-historical-duplicate",
                )
        self.assertEqual("recording_pending", pending["state"], pending)
        self.assertEqual("direct-action-invalid-effects", pending["reason"])
        self.assertIsNone(pending["terminal"])

        result_path = self.root / pending["result_ref"]
        original_result_bytes = result_path.read_bytes()
        original_result = json.loads(original_result_bytes)
        self.assertEqual("restored", original_result["state"])
        self.assertEqual(
            original_result["attempt_evidence_root"],
            original_result["canonical_proof_root"],
        )
        command_history = (
            self.root / original_result["attempt_evidence_root"] / "commands.json"
        )
        command_history_bytes = command_history.read_bytes()
        selector_after_effect = self.selector.read_bytes()
        calls_before_recovery = list(self.docker.calls)
        direct_action = __import__("direct_action_session")
        original_started_id = f"{pending['run_id']}:started"
        original_started, original_started_receipt = direct_action._reopen_event(
            self.root, original_started_id,
        )

        with self.restoration_session() as recovery_session:
            with patch.object(DockerSubprocessExecutor, "run", side_effect=self.docker.run):
                recovered = recover_framework_image_terminal(
                    self.root,
                    journal=recovery_session,
                    result_ref=pending["result_ref"],
                    image_executor=DockerSubprocessExecutor(),
                )

        self.assertEqual("restored", recovered["state"], recovered)
        self.assertTrue(recovered["recording_recovered"])
        self.assertEqual(pending["run_id"], recovered["run_id"])
        self.assertEqual(pending["result_ref"], recovered["result_ref"])
        self.assertEqual(original_result_bytes, result_path.read_bytes())
        self.assertEqual(command_history_bytes, command_history.read_bytes())
        self.assertEqual(selector_after_effect, self.selector.read_bytes())
        self.assertEqual(
            (original_started, original_started_receipt),
            direct_action._reopen_event(self.root, original_started_id),
        )
        recovery_calls = self.docker.calls[len(calls_before_recovery):]
        self.assertFalse(any("build" in call for call in recovery_calls))
        self.assertFalse(any(call[:2] == ("docker", "run") for call in recovery_calls))

        event, _receipt = direct_action._reopen_event(self.root, recovered["terminal"]["event_id"])
        self.assertEqual("completed", event["event"])
        self.assertEqual(len(event["effect_refs"]), len(set(event["effect_refs"])))
        self.assertEqual(pending["run_id"], event["run"]["run_id"])

    def test_recovery_refuses_fixture_forged_unique_effect_set_without_new_journal_events(self):
        """A unique list is insufficient: the successful result shape is exact."""
        def historical_duplicate(values):
            return list(values)

        with patch.object(restoration, "_stable_effect_refs", side_effect=historical_duplicate):
            with self.restoration_session() as original_session:
                pending = self.restore_with(
                    original_session,
                    requested_run_id="restore-forged-unique-effects",
                )
        self.assertEqual("recording_pending", pending["state"], pending)
        result_path = self.root / pending["result_ref"]
        forged = json.loads(result_path.read_bytes())
        forged["effect_refs"] = list(dict.fromkeys(
            ref for ref in forged["effect_refs"]
            if ref != ".caprmedio_runtime/framework/current.toml"
        ))
        self.assertEqual(len(forged["effect_refs"]), len(set(forged["effect_refs"])))
        # Fixture-only forged legacy carrier; no real retained result is edited.
        result_path.write_text(json.dumps(forged, sort_keys=True, separators=(",", ":")), encoding="utf-8")
        journal_root = self.root / ".caprmedio_caprmedio/_journal"
        journal_before = self._inventory(journal_root)
        calls_before = list(self.docker.calls)

        with self.restoration_session() as recovery_session:
            with patch.object(DockerSubprocessExecutor, "run", side_effect=self.docker.run):
                refused = recover_framework_image_terminal(
                    self.root,
                    journal=recovery_session,
                    result_ref=pending["result_ref"],
                    image_executor=DockerSubprocessExecutor(),
                )

        self.assertEqual("recovery_required", refused["state"], refused)
        self.assertEqual("framework-image-restoration-terminal-invalid", refused["reason"])
        self.assertEqual(journal_before, self._inventory(journal_root))
        self.assertEqual(calls_before, self.docker.calls)

    def test_available_old_image_is_no_op_before_any_build(self):
        self.docker.replacement = OLD_IMAGE
        self.docker.old_state = "available"
        result = self.restore()
        self.assertEqual("no_op", result["state"])
        self.assertEqual(self.selector_before, self.selector.read_bytes())
        self.assertFalse(any("build" in call for call in self.docker.calls))

    def test_excluded_metadata_is_unchanged_and_omitted_from_retained_context_build_input(self):
        evidence = read_retained_initial_framework_image(self.root, self.plan.release, OLD_IMAGE)
        context = self.root / evidence.evidence_root / "context"
        metadata = context / ".DS_Store"
        metadata.write_bytes(b"fixture finder metadata\n")
        metadata.chmod(0o600)
        self.docker.replacement = OLD_IMAGE
        result = self.restore()
        self.assertEqual("restored", result["state"], result)
        self.assertEqual(b"fixture finder metadata\n", metadata.read_bytes())
        self.assertEqual(0o600, metadata.stat().st_mode & 0o777)
        self.assertEqual(self.package_before, self._inventory(self.root / ".caprmedio_runtime/framework/releases" / self.plan.release))

    def test_ds_store_in_retained_package_and_public_skill_is_ignored_and_preserved(self):
        package_metadata = self.root / ".caprmedio_runtime/framework/releases" / self.plan.release / ".DS_Store"
        skill_metadata = self.root / ".agents/skills/ca/.DS_Store"
        for path in (package_metadata, skill_metadata):
            path.write_bytes(b"fixture finder metadata\n")
            path.chmod(0o600)
        self.docker.replacement = OLD_IMAGE
        result = self.restore()
        self.assertEqual("restored", result["state"], result)
        for path in (package_metadata, skill_metadata):
            self.assertEqual(b"fixture finder metadata\n", path.read_bytes())
            self.assertEqual(0o600, path.stat().st_mode & 0o777)

    def test_retained_real_file_change_refuses_before_build(self):
        package = self.root / ".caprmedio_runtime/framework/releases" / self.plan.release
        changed = package / "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        changed.write_bytes(b"retained package mutation\n")
        before = list(self.docker.calls)
        result = self.restore()
        self.assertEqual("blocked", result["state"])
        self.assertEqual(before, self.docker.calls)

    def test_explicit_fresh_run_retries_one_canonical_unpublished_partial_without_rewriting_original_result(self):
        self.docker.replacement = OLD_IMAGE
        self.docker.fail = "canary"
        with self.restoration_session() as first:
            partial = self.restore_with(first, requested_run_id="restore-partial-fixture")
        self.assertEqual("partial", partial["state"], partial)
        terminal_event_id = partial["terminal"]["event_id"]
        original_result = self.root / partial["result_ref"]
        original_bytes = original_result.read_bytes()

        before = list(self.docker.calls)
        with self.restoration_session() as same_original_run:
            original_replay = self.restore_with(
                same_original_run,
                requested_run_id="restore-partial-fixture",
            )
        self.assertEqual("recovery_required", original_replay["state"])
        self.assertEqual(before, self.docker.calls)

        self.docker.fail = None
        self.docker.old_inspections = 0
        with self.restoration_session() as retried:
            restored = self.restore_with(
                retried,
                requested_run_id="restore-retry-fixture",
                retry_of_terminal_event_id=terminal_event_id,
            )
        self.assertEqual("restored", restored["state"], restored)
        self.assertEqual(original_bytes, original_result.read_bytes())
        intent_root = original_result.parent
        retry_root = intent_root / "attempts" / hashlib.sha256(b"restore-retry-fixture").hexdigest()
        self.assertTrue((retry_root / "retry.json").is_file())
        self.assertTrue((retry_root / "result.json").is_file())

        before = list(self.docker.calls)
        with self.restoration_session() as same_run:
            denied = self.restore_with(
                same_run,
                requested_run_id="restore-partial-fixture",
                retry_of_terminal_event_id=terminal_event_id,
            )
        self.assertEqual("blocked", denied["state"])
        self.assertEqual(before, self.docker.calls)
        with self.restoration_session() as after_success:
            success_replay = self.restore_with(
                after_success,
                requested_run_id="restore-after-success-fixture",
                retry_of_terminal_event_id=restored["terminal"]["event_id"],
            )
        self.assertEqual("blocked", success_replay["state"])
        self.assertEqual(before, self.docker.calls)

    def test_proof_tamper_refuses_before_build(self):
        evidence = read_retained_initial_framework_image(self.root, self.plan.release, OLD_IMAGE)
        proof = self.root / evidence.evidence_root / "evidence.toml"
        proof.write_bytes(proof.read_bytes() + b"tampered = true\n")
        before = list(self.docker.calls)
        result = self.restore()
        self.assertEqual("blocked", result["state"])
        self.assertEqual(before, self.docker.calls)

    def test_old_image_absence_is_an_admitted_precondition_but_daemon_failure_blocks_before_started_or_build(self):
        self.docker.old_state = "daemon-error"
        result = self.restore()
        self.assertEqual("blocked", result["state"])
        self.assertEqual([], self.journal.intents)
        self.assertEqual(self.selector_before, self.selector.read_bytes())
        self.assertFalse(any("build" in call for call in self.docker.calls))

    def test_timeout_is_uncertain_without_replay_or_publication(self):
        self.docker.fail = "timeout"
        result = self.restore()
        self.assertEqual("effect_uncertain", result["state"])
        self.assertEqual(self.selector_before, self.selector.read_bytes())
        calls = list(self.docker.calls)
        self.restore()
        self.assertEqual(calls, self.docker.calls)

    def test_failed_canary_is_partial_without_replay_or_publication(self):
        self.docker.fail = "canary"
        result = self.restore()
        self.assertEqual("partial", result["state"])
        self.assertEqual(self.selector_before, self.selector.read_bytes())
        calls = list(self.docker.calls)
        self.restore()
        self.assertEqual(calls, self.docker.calls)

    def test_pending_terminal_retains_exact_recovery_evidence_without_a_second_build(self):
        self.docker.replacement = OLD_IMAGE
        self.journal.terminal = "pending"
        result = self.restore()
        self.assertEqual("recording_pending", result["state"])
        self.assertEqual("pending", result["terminal"]["disposition"])
        before = list(self.docker.calls)
        repeat = self.restore()
        self.assertEqual("recovery_required", repeat["state"], repeat)
        self.assertEqual(before, self.docker.calls)

    def test_exact_o187_pending_started_event_recovers_without_any_image_redispatch(self):
        original = read_retained_initial_framework_image(self.root, self.plan.release, OLD_IMAGE)
        intent = {
            "action_id": "FRAMEWORK_IMAGE_RESTORATION",
            "kind": "retained_selected_framework_image_restoration",
            "manifest_sha256": self.plan.release,
            "source_context_sha256": original.source_context_sha256,
            "selected_selector_sha256": hashlib.sha256(self.selector_before).hexdigest(),
            "old_image_digest": OLD_IMAGE,
            "retained_proof_receipt_sha256": original.receipt_sha256,
            "retained_context_sha256": original.context_sha256,
        }
        session = DirectActionSession(
            self.root,
            author="anatoly-m",
            operator_authorization={
                "operator": "Anatoly Maslennikov",
                "authorization_ref": "tmp/operator-authorizations/restoration.md",
            },
            action_id="FRAMEWORK_IMAGE_RESTORATION",
        )
        with patch.object(work_journal, "append_sealed_events", side_effect=OSError("fixture append denied")):
            with self.assertRaises(DirectActionJournalError) as raised:
                session.begin_action(
                    action_id="FRAMEWORK_IMAGE_RESTORATION",
                    requested_run_id="restore-pending-fixture",
                    intent=intent,
                )
        self.assertEqual("direct-action-recording-pending", raised.exception.code)
        event_id = next(iter(session.pending))
        before = list(self.docker.calls)
        recovered = session.recover_pending(event_id)
        self.assertEqual("recovered", recovered["disposition"])
        self.assertEqual(before, self.docker.calls)
        with self.assertRaises(DirectActionJournalError):
            session.recover_pending("not-the-original-restoration-event")

    def test_coordinator_recovers_only_its_exact_pending_terminal_without_image_redispatch(self):
        self.docker.replacement = OLD_IMAGE
        session = DirectActionSession(
            self.root,
            author="anatoly-m",
            operator_authorization={
                "operator": "Anatoly Maslennikov",
                "authorization_ref": "tmp/operator-authorizations/restoration.md",
            },
            action_id="FRAMEWORK_IMAGE_RESTORATION",
        )
        original_append = work_journal.append_sealed_events

        def deny_only_terminal(root, events, **kwargs):
            event = events[0] if len(events) == 1 else {}
            if event.get("event") == "completed":
                raise OSError("fixture terminal append denied")
            return original_append(root, events, **kwargs)

        with patch.object(work_journal, "append_sealed_events", side_effect=deny_only_terminal):
            pending = self.restore_with(session)
        self.assertEqual("recording_pending", pending["state"])
        event_id = pending["pending_event_id"]
        before = list(self.docker.calls)
        with self.restoration_session() as retry_pending:
            denied = self.restore_with(
                retry_pending,
                requested_run_id="restore-pending-retry-fixture",
                retry_of_terminal_event_id=event_id,
            )
        self.assertEqual("blocked", denied["state"])
        self.assertEqual(before, self.docker.calls)
        recovered = recover_framework_image_journal(self.root, journal=session, pending_event_id=event_id)
        self.assertEqual("recovered", recovered["state"])
        self.assertEqual(event_id, recovered["pending_event_id"])
        self.assertEqual(before, self.docker.calls)
        wrong = recover_framework_image_journal(self.root, journal=session, pending_event_id="direct-action:not-owned")
        self.assertEqual("recovery_required", wrong["state"])

    def test_tamper_and_shared_publication_lock_refuse_before_selector_replacement(self):
        self.selector.write_bytes(self.selector_before + b"# changed\n")
        result = self.restore()
        self.assertEqual("blocked", result["state"])
        self.assertEqual(self.selector_before + b"# changed\n", self.selector.read_bytes())
        with selector_publication_lock(self.root, timeout_seconds=0):
            with self.assertRaises(SelectorPublicationLockError):
                with selector_publication_lock(self.root, timeout_seconds=0):
                    pass

    def test_locked_publication_and_journal_admission_refusal_never_build(self):
        # The coordinator's fixed production lock timeout is intentionally not
        # shortened here; model a busy lock at its acquisition seam instead.
        with patch(
            "framework_image_restoration.selector_publication_lock",
            side_effect=SelectorPublicationLockError("selector-publication-lock-busy", "fixture lock held"),
        ):
            result = self.restore()
        self.assertEqual("blocked", result["state"])
        self.assertFalse(any("build" in call for call in self.docker.calls))

        self.journal = RefusingJournal()
        result = self.restore()
        self.assertEqual("blocked", result["state"])
        self.assertEqual(["refused"], self.journal.trace)
        self.assertFalse(any("build" in call for call in self.docker.calls))


if __name__ == "__main__":
    unittest.main()
