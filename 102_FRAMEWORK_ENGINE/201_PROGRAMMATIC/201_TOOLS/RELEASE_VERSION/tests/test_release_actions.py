"""Actual disposable early effects; later Docker CLI output is explicitly mocked.

Private Run identities and declared receipt references are fixtures, not actual
shared-Session Journal receipts. These tests establish no Project release proof.
"""

from __future__ import annotations

import copy
import json
import sys
import unittest
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_actions import (
    PHASES, AdmittedImageExecutor, SelectedReleaseActionContext,
    ReleaseActionRun, ReleasePhaseResult, _invoke, _retirement_recording_handoff, begin_release_action_run, execute_release_action,
)
from release_compilation import build_preflight_validated_candidate
from release_contract import ReleaseContractError
from release_image import (
    CANDIDATE_LABEL, CONTEXT_LABEL, DockerCommandResult, DockerSubprocessExecutor,
    ImageRetirementEvidence,
)
from release_packaging import stage_framework_package
from release_full_gate import FullGateEvidence
from release_e2e_gate import CandidateE2EGateEvidence
from release_promotion import PromotionEvidence
from release_handoff import FRAMEWORK_SETTINGS_RELATIVE
import test_release_image as image_test
import test_release_suite as suite_test


class SelectedNSuiteDocker(image_test.FakeDocker):
    """Mocked Docker admission plus sandboxed suite run for the selected N image."""

    def __init__(self, root: Path, suite_executor: suite_test.FixtureSandboxExecutor):
        super().__init__()
        self.root = root
        self.suite_executor = suite_executor
        self.selected_release = "N"
        self.source_context_sha256 = "b" * 64

    def run(self, argv, *, cwd, timeout_seconds):
        argv = tuple(argv)
        if argv[:3] == ("docker", "image", "inspect"):
            if self.labels:
                return super().run(argv, cwd=cwd, timeout_seconds=timeout_seconds)
            self.calls.append(argv)
            payload = [{"Id": argv[3], "Config": {"Labels": {
                CANDIDATE_LABEL: self.selected_release,
                CONTEXT_LABEL: self.source_context_sha256,
            }, "Env": ["PATH=/usr/bin:/bin"]}}]
            return DockerCommandResult(0, json.dumps(payload).encode(), b"", False)
        if argv[:2] == ("docker", "run") and "--read-only" in argv and "--mount" in argv:
            self.calls.append(argv)
            image_index = argv.index("sha256:" + "a" * 64)
            command = (argv[argv.index("--entrypoint") + 1], *argv[image_index + 1:])
            mounts = [argv[index + 1] for index, value in enumerate(argv) if value == "--mount"]
            workspace = Path(next(value.split("src=", 1)[1].split(",", 1)[0] for value in mounts if "dst=/workspace" in value))
            output = Path(next(value.split("src=", 1)[1].split(",", 1)[0] for value in mounts if "dst=/output" in value))
            environment = {
                value.split("=", 1)[0]: value.split("=", 1)[1]
                for index, value in enumerate(argv) if index and argv[index - 1] == "--env"
            }
            result = self.suite_executor.run(
                command, workspace=workspace, output_root=output,
                working_directory=("." if argv[argv.index("--workdir") + 1] == "/workspace"
                                   else argv[argv.index("--workdir") + 1].removeprefix("/workspace/")),
                environment=environment, timeout_seconds=timeout_seconds,
            )
            return DockerCommandResult(result.exit_code, result.stdout, result.stderr, result.timed_out)
        return super().run(argv, cwd=cwd, timeout_seconds=timeout_seconds)


class ReleaseActionsTests(unittest.TestCase):
    def setUp(self):
        self.fixture = suite_test.ReleaseSuiteTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root.resolve(strict=True)
        writer = self.fixture.fixture.write
        writer("pyproject.toml", b"[project]\nname = 'fixture'\nversion = '0.0.0'\n")
        writer("uv.lock", b"version = 1\n")
        writer("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile",
               b"FROM scratch\nCOPY pyproject.toml uv.lock ./\nCOPY 102_FRAMEWORK_ENGINE ./102_FRAMEWORK_ENGINE\n")
        writer(suite_test.SUITE_DRIVER_RELATIVE, suite_test.SCRIPT.encode())
        _, self.candidate = build_preflight_validated_candidate(
            self.root, candidate_release="N+1",
            full_suite_environment={"runner": "local-subprocess", "command": list(suite_test.SUITE_DRIVER_COMMAND),
                                    "working_directory": "."}, candidate_image_reference="fixture:N+1")
        manifest = self.candidate.manifest.model_dump(mode="json", by_alias=True)
        self.request = {"operation": "apply", "project_root": str(self.root), "candidateSnapshotManifest": manifest,
                        "expected_executing_release": manifest["executing_release"],
                        "expected_project_structure_digest": manifest["project_structure_digest"],
                        "expected_framework_settings_digest": manifest["framework_settings_digest"],
                        "expected_source_frontier_digest": manifest["source_frontier_digest"],
                        "run_receipt_refs": ["fixture-declared-workflow-receipt"]}
        self.run_id = "fixture-workflow-run"
        self.checkpoints = []

        def checkpoint(run):
            self.checkpoints.append((run.in_progress, run.next_phase, run.stopped))

        self.run = begin_release_action_run(
            self.request,
            workflow_run_id=self.run_id,
            checkpoint_callback=checkpoint,
        )
        self.docker = SelectedNSuiteDocker(self.root, self.fixture.executor)
        self.run.image_executor = AdmittedImageExecutor(str(self.root), self.run_id, self.docker)

    def install_selected_n(self) -> None:
        """Install the frozen N fixture and its label-proven immutable image."""
        self.assertIsNotNone(self.run.compilation)
        self.fixture._install_active_n(self.run.compilation)
        selector = self.root / ".caprmedio_runtime/framework/current.toml"
        selector.write_text(
            "schema_version = 1\n"
            'candidate_snapshot_manifest_sha256 = "N"\n'
            'release = "N"\n'
            f'candidate_release = "{self.candidate.manifest.candidate_release}"\n'
            'selected_release_root = ".caprmedio_runtime/framework/releases/N"\n'
            'framework_engine_root = ".caprmedio_runtime/framework/releases/N/FRAMEWORK_ENGINE"\n'
            'methodology_root = ".caprmedio_runtime/framework/releases/N/METHODOLOGY"\n'
            'candidate_image_digest = "sha256:' + "a" * 64 + '"\n'
            'candidate_image_context_sha256 = "' + self.docker.source_context_sha256 + '"\n',
            encoding="utf-8",
        )

    def context(self, index, **changes):
        step, action, _phase = PHASES[index]
        value = SelectedReleaseActionContext(str(self.root), self.run_id, f"fixture-step-{index}", f"fixture-action-{index}",
                                            self.run_id, f"fixture-step-{index}", step, action,
                                            self.run.frozen_parameters_sha256, workflow_version=6)
        return replace(value, **changes)

    def execute(self, index, request=None, context=None):
        if index == 4 and self.run.compilation is not None and not (self.root / ".agents/skills/ca").exists():
            self.install_selected_n()
        return execute_release_action(self.request if request is None else request,
                                      context=self.context(index) if context is None else context, run=self.run)

    def prefix(self, count, *, prepared_package=False):
        results = []
        for index in range(count):
            if index == 4 and prepared_package:
                # Explicit disposable preparation, not an adapter phase effect.
                stage_framework_package(self.root, self.run.compilation)
            result = self.execute(index)
            self.assertEqual(result.outcome, "completed", result.reason)
            results.append(result)
        return results

    def test_fixture_root_matches_retained_private_run_and_action_context(self):
        # On macOS, /tmp and /private/tmp name the same directory. Context
        # identity must use the same canonical spelling as retained candidates.
        self.assertEqual(self.root, self.root.resolve(strict=True))
        self.assertEqual(self.candidate.project_root, str(self.root))
        self.assertEqual(self.run.project_root, str(self.root))
        self.assertEqual(self.context(0).project_root, self.run.project_root)

    def test_prepare_all_selected_pairs_is_effect_free_and_does_not_advance(self):
        before = self.fixture.fixture.snapshot()
        request = {**self.request, "operation": "prepare"}
        for index, (_step, _action, phase) in enumerate(PHASES):
            result = self.execute(index, request)
            self.assertEqual(result.phase, phase)
            self.assertEqual(result.outcome, "prepared")
            self.assertEqual(result.attempted_effects, ())
            self.assertEqual(result.effect_evidence_refs, ())
        self.assertEqual(self.fixture.fixture.snapshot(), before)
        self.assertEqual(self.run.next_phase, 0)
        self.assertEqual(self.run.results, {})

    def test_actual_freeze_validate_delivery_child_compile_retains_typed_bound_refs(self):
        selector = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        results = self.prefix(4)
        self.assertEqual([result.phase for result in results], [pair[2] for pair in PHASES[:4]])
        self.assertTrue((self.root / self.run.source_copy.source_copy_root).is_dir())
        self.assertTrue((self.root / self.run.compilation.child_materialization_root).is_dir())
        self.assertEqual(self.run.compilation.candidate_snapshot_manifest_sha256, self.candidate.manifest.sha256)
        self.assertEqual(results[3].output, self.run.compilation)
        self.assertIn(self.run.compilation.actual_compiled_output_sha256, results[3].effect_evidence_refs[0])
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector)
        self.assertFalse((self.root / ".agents/skills/ca").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/framework/releases").exists())
        self.assertEqual(results[3].recording_state, "shared_session_provider_pending")
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())

    def test_actual_suite_then_staging_keeps_n_and_uses_same_candidate(self):
        results = self.prefix(6, prepared_package=True)
        self.assertTrue(self.run.suite.passed)
        self.assertEqual(self.run.suite.exit_code, 0)
        self.assertEqual(self.run.suite.executed_tests, self.fixture.canonical_testcase_count())
        self.assertEqual(results[4].output, self.run.suite)
        self.assertEqual(self.run.package["candidate_snapshot_manifest_sha256"], self.candidate.manifest.sha256)
        self.assertFalse(self.run.package["staged"])
        self.assertIn("manifest.toml", results[5].effect_evidence_refs[0])
        self.assertTrue((self.root / ".agents/skills/ca").exists())
        selector = (self.root / ".caprmedio_runtime/framework/current.toml").read_text(encoding="utf-8")
        self.assertIn('candidate_image_digest = "sha256:' + "a" * 64 + '"', selector)
        self.assertIn('candidate_image_context_sha256 = "' + self.docker.source_context_sha256 + '"', selector)
        inspections = [call for call in self.docker.calls if call[:3] == ("docker", "image", "inspect")]
        self.assertGreaterEqual(len(inspections), 2)  # admission plus pre-execution reinspection
        self.assertEqual(self.docker.selected_release, self.candidate.authority.executing_release)

    def test_closed_unit_image_and_canary_phases_compose_before_host_e2e(self):
        results = self.prefix(6)
        self.assertTrue(self.run.package["staged"])
        # The producer builds real command/receipt structures from mocked CLI
        # bytes. No Docker daemon, image or canary container is executed here.
        with patch.object(DockerSubprocessExecutor, "run", side_effect=self.docker.run):
            self.run.image_executor = AdmittedImageExecutor(str(self.root), self.run_id, DockerSubprocessExecutor())
            for index in range(6, 8):
                results.append(self.execute(index))
        self.assertEqual([result.phase for result in results], [pair[2] for pair in PHASES[:8]])
        self.assertTrue(all(result.outcome == "completed" for result in results))
        self.assertIsNotNone(self.run.verification)
        self.assertFalse(self.run.stopped)
        self.assertFalse(any("rm" in command or "prune" in command for command in self.docker.calls))
        self.assertTrue(all(result.recording_state == "shared_session_provider_pending" for result in results))

    def test_retired_image_effect_stays_pending_until_shared_recording_is_durable(self):
        # Retirement is deliberately downstream of host E2E and aggregate
        # evidence.  Its exact recording handoff remains independently
        # checkable without creating a fake aggregate producer here.
        self.run.build = SimpleNamespace(candidate_image_digest="sha256:" + "a" * 64)
        self.run.promotion = SimpleNamespace(receipt_sha256="e" * 64)
        retired = ImageRetirementEvidence(
            self.candidate.manifest.sha256, "retired", "exact prior image removal and immutable absence observed",
            self.run.build.candidate_image_digest, "sha256:" + "c" * 64, self.run.promotion.receipt_sha256,
            (), (), (), "until_verified_promotion", self.candidate.manifest.framework_settings_digest,
            "tmp/release-intent.json", 0, True, "tmp/release-retirement", "0" * 64,
            "docker-subprocess", "f" * 64,
        )
        self.assertEqual(_retirement_recording_handoff(retired), {
            "on_recorded_result": "complete exact prior N-image disposition",
            "candidate_snapshot_manifest_sha256": self.candidate.manifest.sha256,
            "prior_image_digest": "sha256:" + "c" * 64,
            "retirement_receipt_ref": "tmp/release-retirement/receipt.json",
            "retirement_receipt_sha256": "f" * 64,
        })

    def test_fresh_suite_precedes_actual_staging_without_implicit_package_preparation(self):
        self.prefix(4)
        releases = self.root / ".caprmedio_runtime/framework/releases"
        self.assertFalse(releases.exists())
        suite = self.execute(4)
        self.assertEqual(suite.outcome, "completed", suite.reason)
        self.assertTrue(self.run.suite.passed)
        self.assertFalse((releases / self.candidate.manifest.sha256).exists())
        staged = self.execute(5)
        self.assertEqual(staged.outcome, "completed", staged.reason)
        self.assertTrue(self.run.package["staged"])
        self.assertTrue((self.root / self.run.package["release_root"] / "manifest.toml").is_file())

    def test_unadmitted_image_executor_stops_without_docker(self):
        self.prefix(6, prepared_package=True)
        self.docker.calls.clear()
        self.run.image_executor = None
        result = self.execute(6)
        self.assertEqual(result.outcome, "blocked")
        self.assertIn("executor-unadmitted", result.reason)
        self.assertEqual(self.docker.calls, [])
        self.assertIsNone(self.run.build)
        self.assertEqual(result.attempted_effects, ())

    def test_test_double_image_result_cannot_advance_to_proof_or_promotion(self):
        self.run.image_executor = AdmittedImageExecutor(str(self.root), self.run_id, self.docker)
        self.prefix(6, prepared_package=True)
        result = self.execute(6)
        self.assertEqual(result.outcome, "pending")
        self.assertEqual(self.run.build.execution_kind, "test-double")
        self.assertTrue(result.effect_evidence_refs)
        self.assertEqual(self.execute(7).outcome, "blocked")
        self.assertTrue((self.root / ".agents/skills/ca").exists())

    def test_skip_unknown_phase_and_wrong_action_refuse_without_effects(self):
        self.assertEqual(self.execute(3).outcome, "blocked")
        self.assertEqual(self.run.next_phase, 0)
        with self.assertRaises(ReleaseContractError):
            self.execute(0, context=self.context(0, action_atom_id="CA-O-169"))
        with self.assertRaises(ReleaseContractError):
            self.execute(0, context=self.context(0, step_atom_id="CA-O-999"))
        with self.assertRaises(ReleaseContractError):
            self.execute(0, {**self.request, "phase": "promote"})
        self.assertFalse((self.root / "101_LAYER_1_FRAMEWORK_METHODOLOGY").exists())

    def test_root_request_run_parent_and_occurrence_identity_mismatches_refuse(self):
        for changes in ({"workflow_run_id": "other"}, {"parent_workflow_run_id": "other"},
                        {"parent_step_run_id": "other"}, {"project_root": "/different"},
                        {"workflow_version": 2}, {"frozen_parameters_sha256": "0" * 64}):
            with self.subTest(changes=changes), self.assertRaises(ReleaseContractError):
                self.execute(0, context=self.context(0, **changes))
        with self.assertRaises(ReleaseContractError):
            self.execute(0, {**self.request, "run_receipt_refs": ["different"]})
        self.execute(0)
        with self.assertRaises(ReleaseContractError):
            self.execute(0, context=self.context(0, action_run_id="different"))
        with self.assertRaises(ReleaseContractError):
            self.execute(1, context=self.context(1, action_run_id=self.context(0).action_run_id))

    def test_stale_sources_stop_and_exact_repeat_returns_retained_observation(self):
        self.prefix(2)
        self.fixture.fixture.core.write_bytes(b"stale")
        result = self.execute(2)
        self.assertEqual(result.outcome, "blocked")
        self.assertIn("stale", result.reason)
        self.assertIs(self.execute(2), result)
        self.assertEqual(self.execute(3).outcome, "blocked")
        self.assertFalse((self.root / "101_LAYER_1_FRAMEWORK_METHODOLOGY/sources").exists())

    def test_interrupted_or_unknown_phase_is_never_implicitly_replayed(self):
        self.prefix(2)
        with patch("release_actions.deliver_release_sources", side_effect=KeyboardInterrupt) as helper:
            result = self.execute(2)
            self.assertEqual(result.outcome, "effect_uncertain")
            self.assertIs(self.execute(2), result)
            self.assertEqual(helper.call_count, 1)
        self.run.results.pop(2)
        self.run.in_progress = self.context(2)
        with patch("release_actions.deliver_release_sources", side_effect=AssertionError("replay forbidden")):
            self.assertEqual(self.execute(2).outcome, "effect_uncertain")

    def test_recording_recovery_is_blocked_and_does_not_invent_receipts(self):
        before = self.fixture.fixture.snapshot()
        result = self.execute(0, {**self.request, "operation": "recover_recording", "failed_recording_ref": "fixture-failed-recording"})
        self.assertEqual(result.outcome, "blocked")
        self.assertEqual(result.attempted_effects, ())
        self.assertEqual(result.effect_evidence_refs, ())
        self.assertEqual(result.declared_run_receipt_refs, ("fixture-declared-workflow-receipt",))
        self.assertEqual(self.fixture.fixture.snapshot(), before)

    def test_mutated_private_frontier_and_foreign_retained_result_refuse(self):
        self.run.next_phase = 2
        self.assertEqual(self.execute(2).outcome, "blocked")
        self.run.next_phase = 0
        self.prefix(3)
        foreign = replace(self.run.source_copy, candidate=replace(self.candidate, project_root="/different"))
        # Same manifest alone is not this exact local candidate/root binding.
        self.run.source_copy = foreign
        self.run.candidate = replace(self.candidate, project_root="/different")
        self.assertEqual(self.execute(3).outcome, "blocked")
        self.assertIsNone(self.run.compilation)

    def test_unknown_exception_and_system_exit_seal_observation_against_replay(self):
        for error in (TypeError("unknown result"), SystemExit(1)):
            with self.subTest(error=type(error).__name__):
                fixture = ReleaseActionsTests("run")
                fixture.setUp()
                try:
                    fixture.prefix(2)
                    with patch("release_actions.deliver_release_sources", side_effect=error) as helper:
                        result = fixture.execute(2)
                        self.assertEqual(result.outcome, "effect_uncertain")
                        self.assertIs(fixture.execute(2), result)
                        self.assertEqual(helper.call_count, 1)
                finally:
                    fixture.doCleanups()


class RetirementRecordingHandoffTests(unittest.TestCase):
    """Pure contract checks; they do not create or clean a fixture directory."""

    CANDIDATE = "a" * 64
    SETTINGS = "d" * 64

    def evidence(self, outcome, *, receipt="f" * 64):
        return ImageRetirementEvidence(
            self.CANDIDATE, outcome, "fixture retirement observation",
            "sha256:" + "b" * 64, "sha256:" + "c" * 64, "e" * 64,
            (), (), (), "until_verified_promotion", self.SETTINGS,
            "tmp/release-retirement/removal.json", 0, outcome == "retired",
            "tmp/release-retirement", "0" * 64, "docker-subprocess", receipt,
        )

    def test_retirement_recording_handoff_is_absent_without_exact_retired_effect(self):
        self.assertIsNone(_retirement_recording_handoff(self.evidence("pending")))

    def test_retirement_recording_handoff_rejects_incomplete_retired_evidence(self):
        with self.assertRaises(ReleaseContractError) as raised:
            _retirement_recording_handoff(self.evidence("retired", receipt=None))
        self.assertEqual(raised.exception.code, "release-action-retirement-recording-invalid")

    def test_retirement_recording_handoff_is_closed_and_bound_to_retired_evidence(self):
        self.assertEqual(_retirement_recording_handoff(self.evidence("retired")), {
            "on_recorded_result": "complete exact prior N-image disposition",
            "candidate_snapshot_manifest_sha256": self.CANDIDATE,
            "prior_image_digest": "sha256:" + "c" * 64,
            "retirement_receipt_ref": "tmp/release-retirement/receipt.json",
            "retirement_receipt_sha256": "f" * 64,
        })


class CheckpointCallbackTests(unittest.TestCase):
    """Pure callback ordering tests; no fixture, filesystem, or Tool runs."""

    def setUp(self):
        self.request = SimpleNamespace(
            candidate_snapshot_manifest=SimpleNamespace(sha256="a" * 64),
            run_receipt_refs=(),
            operation="apply",
        )
        self.context = SelectedReleaseActionContext(
            "/fixture", "workflow", "step", "action", "workflow", "step",
            "CA-O-170", "CA-O-165", "f" * 64, workflow_version=6,
        )

    def execute(self, run, invoke):
        with patch("release_actions._request", return_value=self.request), \
             patch("release_actions._selection", return_value=(0, "freeze")), \
             patch("release_actions._invoke", return_value=invoke):
            return execute_release_action({}, context=self.context, run=run)

    def test_callback_sees_in_progress_before_invoke_and_completed_frontier_after(self):
        observations = []

        def checkpoint(run):
            observations.append((run.in_progress, run.results.get(0), run.next_phase, run.stopped))

        run = ReleaseActionRun("/fixture", "workflow", "f" * 64, self.request, checkpoint_callback=checkpoint)
        result = self.execute(run, ("completed", "frozen", (), {"frozen": True}))
        self.assertEqual(result.outcome, "completed")
        self.assertEqual(observations[0], (self.context, None, 0, False))
        self.assertEqual(observations[1], (None, result, 1, False))

    def test_missing_callback_refuses_before_any_phase_invocation(self):
        run = ReleaseActionRun("/fixture", "workflow", "f" * 64, self.request)
        with patch("release_actions._request", return_value=self.request), \
             patch("release_actions._selection", return_value=(0, "freeze")), \
             patch("release_actions._invoke", side_effect=AssertionError("invoke must not run")) as invoke:
            result = execute_release_action({}, context=self.context, run=run)
        self.assertEqual(result.outcome, "blocked")
        self.assertIn("checkpoint recorder is required", result.reason)
        self.assertEqual(invoke.call_count, 0)
        self.assertEqual(run.contexts, {})
        self.assertEqual(run.results, {})
        self.assertIsNone(run.in_progress)
        self.assertFalse(run.stopped)

    def test_pre_effect_checkpoint_failure_refuses_without_invocation(self):
        callbacks = []

        def fail_checkpoint(run):
            callbacks.append(run.in_progress)
            raise OSError("checkpoint unavailable")

        run = ReleaseActionRun("/fixture", "workflow", "f" * 64, self.request, checkpoint_callback=fail_checkpoint)
        with patch("release_actions._request", return_value=self.request), \
             patch("release_actions._selection", return_value=(0, "freeze")), \
             patch("release_actions._invoke", side_effect=AssertionError("invoke must not run")) as invoke:
            result = execute_release_action({}, context=self.context, run=run)
        self.assertEqual(invoke.call_count, 0)
        self.assertEqual(result.outcome, "blocked")
        self.assertIn("before phase invocation", result.reason)
        self.assertTrue(run.stopped)
        self.assertIsNone(run.in_progress)
        self.assertEqual(callbacks, [self.context])

    def test_post_effect_checkpoint_failure_is_uncertain_and_never_replays(self):
        calls = []

        def fail_second_checkpoint(run):
            calls.append(run.in_progress)
            if len(calls) == 2:
                raise OSError("terminal checkpoint unavailable")

        run = ReleaseActionRun("/fixture", "workflow", "f" * 64, self.request,
                               checkpoint_callback=fail_second_checkpoint)
        result = self.execute(run, ("completed", "frozen", (), {"frozen": True}))
        self.assertEqual(result.outcome, "effect_uncertain")
        self.assertIn("after phase invocation", result.reason)
        self.assertTrue(run.stopped)
        self.assertEqual(run.next_phase, 0)
        self.assertIs(run.results[0], result)
        repeated = self.execute(run, AssertionError("effect replayed"))
        self.assertIs(repeated, result)
        self.assertEqual(calls, [self.context, None])


class FullGateDispatchTests(unittest.TestCase):
    """Synthetic predecessor doubles test dispatch, not actual gate proof."""

    def setUp(self):
        from test_release_checkpoint import _candidate, _compilation, _preflight, _request
        from release_handoff import SealedSourceCopy

        candidate = _candidate()
        self.run = begin_release_action_run(_request(candidate), workflow_run_id="gate-boundary",
                                           checkpoint_callback=lambda _run: None)
        self.run.candidate = candidate
        self.run.preflight = _preflight(candidate)
        self.run.compilation = _compilation(candidate)
        self.run.source_copy = SealedSourceCopy(candidate, self.run.compilation.source_copy_root,
                                               self.run.compilation.actual_derived_source_copy_sha256)
        self.run.package = {"candidate_snapshot_manifest_sha256": candidate.manifest.sha256}

        def predecessor(**values):
            return SimpleNamespace(candidate_snapshot_manifest_sha256=candidate.manifest.sha256, **values)

        self.run.suite = predecessor(passed=True)
        self.run.build = predecessor(outcome="built", execution_kind="docker-subprocess")
        self.run.verification = predecessor(outcome="verified", execution_kind="docker-subprocess")
        self.run.e2e = predecessor(passed=True)
        self.full_gate = FullGateEvidence(candidate.manifest.sha256, "sha256:" + "a" * 64,
            "b" * 64, "c" * 64, "d" * 64, "e" * 64, "f" * 64,
            "passed", "all gates passed", "tmp/full-gate", "0" * 64, 4)

    def test_failed_aggregate_retains_typed_result_and_receipt_without_pass_verification(self):
        failed = replace(self.full_gate, outcome="failed", reason="E2E partition is incomplete")
        with patch("release_actions.verify_bound_candidate_e2e_evidence"), \
             patch("release_full_gate.aggregate_bound_release_gates", return_value=failed), \
             patch("release_full_gate.verify_bound_full_gate_evidence") as verify:
            outcome, reason, refs, output = _invoke("aggregate_full_gate", self.run)
        self.assertEqual((outcome, reason), ("pending", failed.reason))
        self.assertEqual(refs, ("tmp/full-gate/receipt.json",))
        self.assertIs(output, failed)
        self.assertIs(self.run.full_gate, failed)
        verify.assert_not_called()

    def test_aggregate_pass_requires_reopened_evidence(self):
        with patch("release_actions.verify_bound_candidate_e2e_evidence"), \
             patch("release_full_gate.aggregate_bound_release_gates", return_value=self.full_gate), \
             patch("release_full_gate.verify_bound_full_gate_evidence") as verify:
            self.assertEqual(_invoke("aggregate_full_gate", self.run)[0], "completed")
        verify.assert_called_once_with(self.run.candidate, self.run.compilation, self.run.suite,
                                      self.run.build, self.run.verification, self.run.e2e, self.full_gate)

    def test_missing_failed_or_untyped_full_gate_cannot_invoke_promotion(self):
        for evidence in (None, replace(self.full_gate, outcome="failed"),
                         SimpleNamespace(candidate_snapshot_manifest_sha256=self.run.candidate.manifest.sha256,
                                         passed=True)):
            self.run.full_gate = evidence
            with self.subTest(evidence=evidence), patch("release_actions.promote_bound_release") as promote:
                with self.assertRaises(ReleaseContractError):
                    _invoke("promote", self.run)
                promote.assert_not_called()

    def test_stale_passed_aggregate_refuses_before_promotion_effect(self):
        self.run.full_gate = self.full_gate
        with patch("release_full_gate.verify_bound_full_gate_evidence",
                   side_effect=ReleaseContractError("stale", "aggregate receipt changed")) as verify, \
             patch("release_actions.promote_bound_release") as promote:
            with self.assertRaises(ReleaseContractError):
                _invoke("promote", self.run)
        verify.assert_called_once()
        promote.assert_not_called()

    def retirement_frontier(self):
        """Synthetic completed prefix; no Tool, Docker, Journal or file effect."""
        candidate = self.run.candidate
        self.run.full_gate = self.full_gate
        self.run.e2e = CandidateE2EGateEvidence(
            candidate.manifest.sha256, self.full_gate.candidate_image_digest,
            self.full_gate.phase_map_sha256, "0" * 64, "passed", "synthetic E2E dispatch receipt",
            (), "tmp/e2e", self.full_gate.e2e_receipt_sha256,
            None, None, None, None, "host-subprocess",
        )
        self.run.promotion = PromotionEvidence(
            candidate.manifest.sha256, "promoted", "synthetic promotion dispatch receipt",
            self.full_gate.candidate_image_digest, "sha256:" + "c" * 64,
            candidate.authority.executing_release, "tmp/package", "tmp/package/FRAMEWORK_ENGINE",
            "tmp/package/METHODOLOGY", ".agents/skills/ca", "a" * 64, "tmp/promotion",
            "tmp/prior-selector.toml", "tmp/prior-skill", "e" * 64,
        )
        self.docker = image_test.FakeRetirementDocker()
        self.run.image_executor = AdmittedImageExecutor(
            self.run.project_root, self.run.workflow_run_id, self.docker,
        )
        for index, (step, action, phase) in enumerate(PHASES):
            context = SelectedReleaseActionContext(
                self.run.project_root, self.run.workflow_run_id, f"step-{index}", f"action-{index}",
                self.run.workflow_run_id, f"step-{index}", step, action,
                self.run.frozen_parameters_sha256, workflow_version=6,
            )
            if phase == "retire":
                self.run.next_phase = index
                return context
            self.run.contexts[index] = context
            self.run.results[index] = ReleasePhaseResult(
                self.run.workflow_run_id, context.step_run_id, context.action_run_id,
                step, action, phase, "completed", "synthetic prior dispatch result",
                candidate.manifest.sha256, (), (), tuple(self.run.request.run_receipt_refs),
            )
        self.fail("retirement phase is absent")

    def retirement_observation(self, outcome="retained", **changes):
        retained = outcome == "retained"
        return replace(ImageRetirementEvidence(
            self.run.candidate.manifest.sha256, outcome, "synthetic exact prior-image disposition",
            self.run.promotion.candidate_image_digest, self.run.promotion.prior_image_digest,
            self.run.promotion.receipt_sha256, (), ("tmp/prior-selector.toml",),
            (f"{FRAMEWORK_SETTINGS_RELATIVE}#release_version.rollback_retention.condition",) if retained else (),
            "retain_prior" if retained else "until_verified_promotion",
            self.run.candidate.manifest.framework_settings_digest,
            None if retained else "tmp/removal-intent.json", None if retained else 0,
            None if retained else True, "tmp/retirement", "0" * 64, "docker-subprocess", "f" * 64,
        ), **changes)

    def test_retained_dispatch_completes_with_exact_run_gates_and_no_removal_handoff(self):
        context = self.retirement_frontier()
        observation = self.retirement_observation()
        with patch("release_full_gate.verify_bound_full_gate_evidence") as verify, \
             patch("release_actions.retire_prior_image", autospec=True, return_value=observation) as retire:
            result = execute_release_action(self.run.request, context=context, run=self.run)
        self.assertEqual(result.outcome, "completed", result.reason)
        self.assertEqual(result.effect_outcome, "retained")
        self.assertIs(result.output, observation)
        self.assertIsNone(result.shared_action_recording)
        self.assertEqual(result.effect_evidence_refs, ("tmp/retirement/receipt.json",))
        self.assertEqual(self.run.next_phase, len(PHASES))
        self.assertFalse(self.run.stopped)
        verify.assert_called_once_with(self.run.candidate, self.run.compilation, self.run.suite,
            self.run.build, self.run.verification, self.run.e2e, self.run.full_gate)
        retire.assert_called_once_with(self.run.candidate, self.run.compilation, self.run.suite,
            self.run.build, self.run.verification, self.run.promotion,
            e2e=self.run.e2e, full_gate=self.run.full_gate, executor=self.docker)
        self.assertEqual(self.docker.calls, [])

    def test_actual_retired_dispatch_stays_pending_for_shared_recording(self):
        context = self.retirement_frontier()
        observation = self.retirement_observation("retired")
        with patch("release_full_gate.verify_bound_full_gate_evidence"), \
             patch("release_actions.retire_prior_image", autospec=True, return_value=observation):
            result = execute_release_action(self.run.request, context=context, run=self.run)
        self.assertEqual(result.outcome, "pending", result.reason)
        self.assertEqual(result.effect_outcome, "retired")
        self.assertEqual(result.shared_action_recording, _retirement_recording_handoff(observation))
        self.assertEqual(self.run.next_phase, len(PHASES) - 1)
        self.assertTrue(self.run.stopped)
        self.assertEqual(self.docker.calls, [])

    def test_missing_failed_or_cross_candidate_gates_block_retirement_dispatch(self):
        for field, kind in (("e2e", "missing"), ("e2e", "failed"), ("e2e", "cross_candidate"),
                            ("full_gate", "missing"), ("full_gate", "failed"), ("full_gate", "cross_candidate"),
                            ("full_gate", "untyped")):
            with self.subTest(field=field, kind=kind):
                self.setUp()
                context = self.retirement_frontier()
                evidence = getattr(self.run, field)
                if kind == "missing":
                    evidence = None
                elif kind == "failed":
                    evidence = replace(evidence, outcome="failed")
                elif kind == "cross_candidate":
                    evidence = replace(evidence, candidate_snapshot_manifest_sha256="f" * 64)
                else:
                    evidence = SimpleNamespace(candidate_snapshot_manifest_sha256=self.run.candidate.manifest.sha256,
                                               passed=True)
                setattr(self.run, field, evidence)
                with patch("release_full_gate.verify_bound_full_gate_evidence"), \
                     patch("release_actions.retire_prior_image", autospec=True) as retire:
                    result = execute_release_action(self.run.request, context=context, run=self.run)
                self.assertEqual(result.outcome, "blocked", result.reason)
                retire.assert_not_called()
                self.assertEqual(self.docker.calls, [])

    def test_stale_aggregate_blocks_retirement_before_producer_call(self):
        context = self.retirement_frontier()
        with patch("release_full_gate.verify_bound_full_gate_evidence",
                   side_effect=ReleaseContractError("release-full-gate-evidence-untrusted", "receipt changed")), \
             patch("release_actions.retire_prior_image", autospec=True) as retire:
            result = execute_release_action(self.run.request, context=context, run=self.run)
        self.assertEqual(result.outcome, "blocked", result.reason)
        retire.assert_not_called()
        self.assertEqual(self.docker.calls, [])

    def test_unrecorded_or_test_double_retention_cannot_complete_dispatch(self):
        for changes in ({"receipt_sha256": None}, {"receipt_sha256": "not-a-sha256"},
                        {"execution_kind": "test-double"}):
            with self.subTest(changes=changes):
                self.setUp()
                context = self.retirement_frontier()
                observation = self.retirement_observation(**changes)
                with patch("release_full_gate.verify_bound_full_gate_evidence"), \
                     patch("release_actions.retire_prior_image", autospec=True, return_value=observation):
                    result = execute_release_action(self.run.request, context=context, run=self.run)
                self.assertEqual(result.outcome, "pending", result.reason)
                self.assertIsNone(result.shared_action_recording)
                self.assertTrue(self.run.stopped)
                self.assertEqual(self.docker.calls, [])

    def test_only_sealed_policy_retention_without_container_use_can_complete_dispatch(self):
        policy = f"{FRAMEWORK_SETTINGS_RELATIVE}#release_version.rollback_retention"
        cases = (
            {"retaining_container_refs": ("c" * 64,)},
            {"retaining_container_refs": None},
            {"retention_condition": "until_verified_promotion"},
            {"retention_condition": None},
            {"required_rollback_refs": ()},
            {"required_rollback_refs": None},
            {"required_rollback_refs": (policy + ".required_image_digests[0]",)},
            {"required_rollback_refs": ("caller-policy:retain_prior",)},
            {"framework_settings_digest": "f" * 64},
            {"removal_intent_ref": "tmp/removal-intent.json"},
            {"removal_exit_code": 0},
            {"prior_image_absent": True},
        )
        for changes in cases:
            with self.subTest(changes=changes):
                self.setUp()
                context = self.retirement_frontier()
                observation = self.retirement_observation(**changes)
                with patch("release_full_gate.verify_bound_full_gate_evidence"), \
                     patch("release_actions.retire_prior_image", autospec=True, return_value=observation):
                    result = execute_release_action(self.run.request, context=context, run=self.run)
                self.assertEqual(result.outcome, "pending", result.reason)
                self.assertIsNone(result.shared_action_recording)
                self.assertEqual(self.run.next_phase, len(PHASES) - 1)
                self.assertTrue(self.run.stopped)
                self.assertEqual(self.docker.calls, [])

    def test_unavailable_or_unverified_disposition_cannot_complete_dispatch(self):
        for outcome in ("pending", "failed", "stale", "effect_uncertain", "recording_uncertain"):
            with self.subTest(outcome=outcome):
                self.setUp()
                context = self.retirement_frontier()
                observation = replace(self.retirement_observation(), outcome=outcome,
                                      reason="synthetic unavailable or unverified proof")
                with patch("release_full_gate.verify_bound_full_gate_evidence"), \
                     patch("release_actions.retire_prior_image", autospec=True, return_value=observation):
                    result = execute_release_action(self.run.request, context=context, run=self.run)
                self.assertEqual(result.outcome, "pending", result.reason)
                self.assertIsNone(result.shared_action_recording)
                self.assertTrue(self.run.stopped)
                self.assertEqual(self.docker.calls, [])

    def test_frozen_v5_context_is_not_rebound_or_executed_by_current_v6_dispatch(self):
        context = replace(self.retirement_frontier(), workflow_version=5)
        before_contexts = dict(self.run.contexts)
        before_results = dict(self.run.results)
        with patch("release_actions._checkpoint") as checkpoint, \
             patch("release_actions.retire_prior_image", autospec=True) as retire:
            with self.assertRaises(ReleaseContractError) as caught:
                execute_release_action(self.run.request, context=context, run=self.run)
        self.assertEqual(caught.exception.code, "release-action-frozen-binding-mismatch")
        self.assertEqual(context.workflow_version, 5)
        self.assertEqual(self.run.contexts, before_contexts)
        self.assertEqual(self.run.results, before_results)
        self.assertFalse(self.run.stopped)
        checkpoint.assert_not_called()
        retire.assert_not_called()
        self.assertEqual(self.docker.calls, [])


if __name__ == "__main__":
    unittest.main()
