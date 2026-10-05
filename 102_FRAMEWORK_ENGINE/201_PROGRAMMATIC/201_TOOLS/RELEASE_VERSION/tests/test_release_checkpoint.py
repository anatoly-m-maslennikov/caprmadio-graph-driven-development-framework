"""Pure codec coverage for durable Release checkpoints.

The tests intentionally use synthetic typed evidence and the checked-out
repository root.  They do not create a temporary directory, invoke Docker, or
write a checkpoint carrier.
"""

from __future__ import annotations

import copy
import json
import sys
import unittest
from dataclasses import replace
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = str(Path(__file__).resolve().parents[5])
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_actions import (  # noqa: E402
    PHASES,
    ReleaseActionRun,
    ReleasePhaseResult,
    SelectedReleaseActionContext,
    _fingerprint,
)
from release_checkpoint import (  # noqa: E402
    RELEASE_ACTION_CHECKPOINT_SCHEMA,
    dump_release_checkpoint,
    encode_release_action_checkpoint,
    extract_pending_recordings,
    load_release_checkpoint,
    release_action_checkpoint_sha256,
    restore_release_action_checkpoint,
)
from release_compilation import ReleaseCompilationPreflight  # noqa: E402
from release_e2e_gate import CandidateE2EGateEvidence, HarnessReceipt  # noqa: E402
from release_full_gate import FullGateEvidence  # noqa: E402
from release_contract import (  # noqa: E402
    CandidateBuildRequest,
    ReleaseContractError,
    SealedAuthority,
    ValidatedCandidate,
    encode_candidate_manifest,
)
from release_handoff import CompilerEntrypoint, PackageRow, SealedCandidateCompilation, SealedSourceCopy  # noqa: E402
from release_image import ImageBuildEvidence, ImageRetirementEvidence, ImageVerificationEvidence  # noqa: E402
from release_promotion import PromotionEvidence  # noqa: E402
from release_suite import SuiteGateEvidence  # noqa: E402
from release_version import ReleaseVersionRequest  # noqa: E402


def _digest(letter: str) -> str:
    return letter * 64


def _candidate() -> ValidatedCandidate:
    rows = [
        {"resource": "FRAMEWORK_ENGINE", "source_path": "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/release.py", "source_sha256": _digest("a"), "source_mode": 0o644, "destination_path": "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/release.py"},
        {"resource": "FRAMEWORK_ENGINE", "source_path": "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py", "source_sha256": _digest("b"), "source_mode": 0o644, "destination_path": "FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py"},
        {"resource": "FRAMEWORK_ENGINE", "source_path": "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py", "source_sha256": _digest("c"), "source_mode": 0o644, "destination_path": "FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py"},
        {"resource": "FRAMEWORK_ENGINE", "source_path": "102_FRAMEWORK_ENGINE/202_AGENTIC/agent.py", "source_sha256": _digest("d"), "source_mode": 0o644, "destination_path": "FRAMEWORK_ENGINE/202_AGENTIC/agent.py"},
        {"resource": "METHODOLOGY", "source_path": "METHODOLOGY/claim.md", "source_sha256": _digest("e"), "source_mode": 0o644, "destination_path": "METHODOLOGY/sources/claim.md"},
        {"resource": "SKILL", "source_path": "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md", "source_sha256": _digest("f"), "source_mode": 0o644, "destination_path": "SKILLS/ca/SKILL.md"},
        {"resource": "SKILL", "source_path": "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml", "source_sha256": _digest("0"), "source_mode": 0o644, "destination_path": "SKILLS/ca/agents/openai.yaml"},
        {"resource": "IMAGE_INPUT", "source_path": "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile", "source_sha256": _digest("1"), "source_mode": 0o644, "destination_path": "IMAGE_INPUT/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile"},
    ]
    intent = CandidateBuildRequest(
        candidate_release="N+1",
        expected_derived_source_copy_sha256=_digest("2"),
        expected_compiled_output_sha256=_digest("3"),
        full_suite_environment={"runner": "local-subprocess", "command": ["python", "-m", "unittest"], "working_directory": "."},
        candidate_image_reference="caprmedio:N+1",
    )
    manifest = encode_candidate_manifest(
        {
            "executing_release": "N",
            "candidate_release": intent.candidate_release,
            "canonical_source_snapshot_ref": "METHODOLOGY/sources",
            "canonical_source_snapshot_digest": _digest("4"),
            "project_structure_digest": _digest("5"),
            "framework_settings_digest": _digest("6"),
            "source_frontier_digest": _digest("7"),
            "nested_source_recursive_sha256_before": _digest("4"),
            "expected_derived_source_copy_sha256": intent.expected_derived_source_copy_sha256,
            "expected_compiled_output_sha256": intent.expected_compiled_output_sha256,
            "full_suite_environment": intent.full_suite_environment.model_dump(mode="json"),
            "skill_target": ".agents/skills/ca",
            "candidate_image": {
                "dockerfile_path": "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile",
                "dockerfile_sha256": _digest("1"),
                "candidate_image_reference": intent.candidate_image_reference,
            },
            "source_inventory_rows": rows,
        }
    )
    authority = SealedAuthority(
        executing_release="N",
        candidate_release="N+1",
        canonical_source_snapshot_digest=manifest.canonical_source_snapshot_digest,
        project_structure_digest=manifest.project_structure_digest,
        framework_settings_digest=manifest.framework_settings_digest,
        source_frontier_digest=manifest.source_frontier_digest,
        nested_source_recursive_sha256_before=manifest.nested_source_recursive_sha256_before,
        expected_candidate_snapshot_manifest_sha256=manifest.sha256,
    )
    return ValidatedCandidate(PROJECT_ROOT, manifest, authority, intent)


def _request(candidate: ValidatedCandidate) -> ReleaseVersionRequest:
    manifest = candidate.manifest
    return ReleaseVersionRequest.model_validate(
        {
            "operation": "apply",
            "project_root": PROJECT_ROOT,
            "candidateSnapshotManifest": manifest.model_dump(mode="json", by_alias=True),
            "expected_executing_release": manifest.executing_release,
            "expected_project_structure_digest": manifest.project_structure_digest,
            "expected_framework_settings_digest": manifest.framework_settings_digest,
            "expected_source_frontier_digest": manifest.source_frontier_digest,
            "run_receipt_refs": ["journal-event-1"],
        }
    )


def _preflight(candidate: ValidatedCandidate) -> ReleaseCompilationPreflight:
    return ReleaseCompilationPreflight(
        candidate_release=candidate.manifest.candidate_release,
        expected_derived_source_copy_sha256=candidate.manifest.expected_derived_source_copy_sha256,
        expected_compiled_output_sha256=candidate.manifest.expected_compiled_output_sha256,
        compiler_entrypoint=CompilerEntrypoint(path="102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/compile.py", sha256=_digest("8")),
        canonical_source_snapshot_digest=candidate.manifest.canonical_source_snapshot_digest,
        compiler_frontier_digest=candidate.authority.source_frontier_digest,
        nested_source_recursive_sha256_before=candidate.manifest.nested_source_recursive_sha256_before,
        output_files={"04_requirement/CA-R-1.md": b"# Claim\n"},
        child_manifest_bytes=b"candidate = 'N+1'\n",
    )


def _compilation(candidate: ValidatedCandidate) -> SealedCandidateCompilation:
    rows = [
        PackageRow(resource="FRAMEWORK_ENGINE", source_path="102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/release.py", destination_path="FRAMEWORK_ENGINE/release.py", sha256=_digest("a"), mode=0o644),
        PackageRow(resource="METHODOLOGY", source_path="101_LAYER_1_FRAMEWORK_METHODOLOGY/sources/claim.md", destination_path="METHODOLOGY/sources/claim.md", sha256=_digest("e"), mode=0o644),
        PackageRow(resource="METHODOLOGY", source_path=".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/_release_materialized/x/claim.md", destination_path="METHODOLOGY/compiled/claim.md", sha256=_digest("9"), mode=0o644),
        PackageRow(resource="SKILL", source_path="102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md", destination_path="SKILLS/ca/SKILL.md", sha256=_digest("f"), mode=0o644),
        PackageRow(resource="SKILL", source_path="102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml", destination_path="SKILLS/ca/agents/openai.yaml", sha256=_digest("0"), mode=0o644),
    ]
    return SealedCandidateCompilation(
        candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
        authority=candidate.authority,
        source_copy_root="101_LAYER_1_FRAMEWORK_METHODOLOGY/sources",
        expected_derived_source_copy_sha256=candidate.manifest.expected_derived_source_copy_sha256,
        actual_derived_source_copy_sha256=candidate.manifest.expected_derived_source_copy_sha256,
        compiler_entrypoint=CompilerEntrypoint(path="102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/compile.py", sha256=_digest("8")),
        compiler_frontier_digest=candidate.authority.source_frontier_digest,
        expected_compiled_output_sha256=candidate.manifest.expected_compiled_output_sha256,
        actual_compiled_output_sha256=candidate.manifest.expected_compiled_output_sha256,
        child_materialization_root=f".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/_release_materialized/{candidate.manifest.sha256}",
        package_rows=rows,
    )


class ReleaseCheckpointTests(unittest.TestCase):
    def setUp(self) -> None:
        self.candidate = _candidate()
        self.request = _request(self.candidate)
        self.run = ReleaseActionRun(PROJECT_ROOT, "workflow-1", _fingerprint(self.request), self.request)
        self.context = SelectedReleaseActionContext(
            PROJECT_ROOT, "workflow-1", "step-0", "action-0", "workflow-1", "step-0",
            *PHASES[0][:2], self.run.frozen_parameters_sha256,
        )
        self.run.candidate = self.candidate
        self.run.preflight = _preflight(self.candidate)
        self.run.contexts[0] = self.context
        self.run.results[0] = ReleasePhaseResult(
            "workflow-1", "step-0", "action-0", *PHASES[0], "completed", "frozen",
            self.candidate.manifest.sha256, (), (), ("journal-event-1",), output=self.candidate,
        )
        self.run.next_phase = 1

    def test_closed_canonical_round_trip_restores_typed_state_without_executor(self) -> None:
        # The codec preserves the definition revision recorded by the selected
        # provider; it does not silently downgrade a newer frozen Workflow.
        self.context = SelectedReleaseActionContext(
            PROJECT_ROOT, "workflow-1", "step-0", "action-0", "workflow-1", "step-0",
            *PHASES[0][:2], self.run.frozen_parameters_sha256, workflow_version=5,
        )
        self.run.contexts[0] = self.context
        self.run.results[0] = ReleasePhaseResult(
            "workflow-1", "step-0", "action-0", *PHASES[0], "completed", "frozen",
            self.candidate.manifest.sha256, (), (), ("journal-event-1",), output=self.candidate,
        )
        self.run.checkpoint_callback = lambda _run: self.fail("codec must not invoke a runtime callback")
        encoded = encode_release_action_checkpoint(self.run)
        payload = json.loads(encoded)
        self.assertEqual(payload["schema"], RELEASE_ACTION_CHECKPOINT_SCHEMA)
        self.assertNotIn("executor", encoded.decode())
        self.assertNotIn("checkpoint_callback", encoded.decode())
        restored = restore_release_action_checkpoint(encoded)
        self.assertIsNone(restored.image_executor)
        self.assertEqual(restored.request, self.request)
        self.assertEqual(restored.candidate, self.candidate)
        self.assertEqual(restored.preflight, self.run.preflight)
        self.assertEqual(restored.contexts, self.run.contexts)
        self.assertEqual(restored.results, self.run.results)

        self.assertEqual(encode_release_action_checkpoint(restored), encoded)

    def test_round_trip_preserves_all_retained_preflight_and_evidence_types(self) -> None:
        compilation = _compilation(self.candidate)
        self.run.source_copy = SealedSourceCopy(self.candidate, compilation.source_copy_root, compilation.actual_derived_source_copy_sha256)
        self.run.compilation = compilation
        self.run.suite = SuiteGateEvidence(
            candidate_snapshot_manifest_sha256=self.candidate.manifest.sha256,
            outcome="passed",
            reason="all tests passed",
            runner="local-subprocess",
            command=("python", "-m", "unittest"),
            working_directory=".",
            exit_code=0,
            executed_tests=3,
            coverage=("Methodology", "Tools"),
            evidence_root="tmp/suite",
            stdout_sha256=_digest("a"),
            stderr_sha256=_digest("b"),
            report_sha256=_digest("c"),
            executing_selector_sha256=_digest("d"),
            executing_release_package_sha256=_digest("e"),
            executing_skill_sha256=_digest("f"),
            receipt_sha256=_digest("0"),
            elapsed_seconds=1.0,
            phase_map_sha256=_digest("d"),
        )
        self.run.package = {"staged": True, "verified": True, "candidate_snapshot_manifest_sha256": self.candidate.manifest.sha256,
                            "release_root": ".caprmedio_runtime/framework/releases/" + self.candidate.manifest.sha256, "file_count": 5}
        self.run.build = ImageBuildEvidence(
            self.candidate.manifest.sha256, "built", "image built", "sha256:" + _digest("1"),
            "tmp/image-context", _digest("2"), _digest("3"), _digest("0"), "tmp/image-build", _digest("4"),
            "docker-subprocess", _digest("5"),
        )
        self.run.verification = ImageVerificationEvidence(
            self.candidate.manifest.sha256, "verified", "image verified", self.run.build.candidate_image_digest,
            self.run.build.receipt_sha256, "tmp/image-verify", _digest("6"), "docker-subprocess", _digest("7"),
        )
        harness = HarnessReceipt(
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/tests/test_release_e2e_host.py",
            _digest("8"), ("python", "run_release_e2e.py"), "2026-10-06T00:00:00Z", "2026-10-06T00:00:01Z",
            0, False, "tmp/e2e/stdout.txt", _digest("9"), "tmp/e2e/stderr.txt", _digest("a"),
            "tmp/e2e/junit.xml", _digest("b"), 1, 1.0, "passed",
        )
        self.run.e2e = CandidateE2EGateEvidence(
            self.candidate.manifest.sha256, self.run.build.candidate_image_digest, self.run.suite.phase_map_sha256,
            _digest("c"), "passed", "host E2E passed", (harness,), "tmp/e2e", _digest("d"),
            "tmp/e2e/settings.json", _digest("e"), "tmp/e2e/capability.json", _digest("f"), "host-subprocess",
        )
        self.run.full_gate = FullGateEvidence(
            self.candidate.manifest.sha256, self.run.build.candidate_image_digest, self.run.suite.phase_map_sha256,
            self.run.suite.receipt_sha256, self.run.build.receipt_sha256, self.run.verification.receipt_sha256,
            self.run.e2e.receipt_sha256, "passed", "full gate passed", "tmp/full-gate", _digest("0"), 4,
        )
        self.run.promotion = PromotionEvidence(
            self.candidate.manifest.sha256, "promoted", "candidate promoted", self.run.build.candidate_image_digest,
            "sha256:" + _digest("8"), "N", ".caprmedio_runtime/framework/releases/N+1",
            ".caprmedio_runtime/framework/releases/N+1/FRAMEWORK_ENGINE",
            ".caprmedio_runtime/framework/releases/N+1/METHODOLOGY", ".agents/skills/ca", _digest("9"),
            "tmp/promotion", "tmp/prior-selector", None, _digest("a"),
        )
        self.run.retirement = ImageRetirementEvidence(
            self.candidate.manifest.sha256, "pending", "shared recording pending", self.run.build.candidate_image_digest,
            "sha256:" + _digest("8"), self.run.promotion.receipt_sha256, (), (), (), "until_verified_promotion",
            self.candidate.manifest.framework_settings_digest, "tmp/retirement-intent", None, None,
            "tmp/retirement", _digest("b"), "docker-subprocess", _digest("c"),
        )
        outputs = {
            0: self.candidate,
            1: self.candidate,
            2: self.run.source_copy,
            3: self.run.compilation,
            4: self.run.suite,
            5: self.run.package,
            6: self.run.build,
            7: self.run.verification,
            8: self.run.e2e,
            9: self.run.full_gate,
            10: self.run.promotion,
            11: self.run.retirement,
        }
        self.run.contexts = {
            index: SelectedReleaseActionContext(
                PROJECT_ROOT, "workflow-1", f"step-{index}", f"action-{index}", "workflow-1", f"step-{index}",
                *PHASES[index][:2], self.run.frozen_parameters_sha256,
            )
            for index in range(len(PHASES))
        }
        self.run.results = {
            index: ReleasePhaseResult(
                "workflow-1", f"step-{index}", f"action-{index}", *PHASES[index],
                "completed" if index < 11 else "pending", "observed", self.candidate.manifest.sha256,
                (), (), ("journal-event-1",), output=outputs[index],
            )
            for index in range(len(PHASES))
        }
        self.run.next_phase = 11
        self.run.stopped = True
        encoded = encode_release_action_checkpoint(self.run)
        restored = restore_release_action_checkpoint(encoded)
        self.assertIsInstance(restored.source_copy, SealedSourceCopy)
        self.assertIsInstance(restored.compilation, SealedCandidateCompilation)
        self.assertIsInstance(restored.suite, SuiteGateEvidence)
        self.assertEqual(restored.package, self.run.package)
        self.assertIsInstance(restored.build, ImageBuildEvidence)
        self.assertIsInstance(restored.verification, ImageVerificationEvidence)
        self.assertIsInstance(restored.e2e, CandidateE2EGateEvidence)
        self.assertIsInstance(restored.e2e.harness_receipts[0], HarnessReceipt)
        self.assertIsInstance(restored.e2e.harness_receipts[0].argv, tuple)
        self.assertIsInstance(restored.full_gate, FullGateEvidence)
        self.assertEqual(restored.suite.phase_map_sha256, self.run.suite.phase_map_sha256)
        self.assertIsInstance(restored.promotion, PromotionEvidence)
        self.assertIsInstance(restored.retirement, ImageRetirementEvidence)
        self.assertEqual(restored.results, self.run.results)

        # A resealed envelope cannot add caller-selected fields to the new
        # nested evidence types or promote from a failed aggregate.
        payload = json.loads(encoded)
        for state_name in ("e2e", "full_gate"):
            changed = copy.deepcopy(payload)
            changed["state"][state_name]["value"]["caller_override"] = True
            changed["sha256"] = release_action_checkpoint_sha256(changed)
            with self.subTest(state=state_name), self.assertRaises(ReleaseContractError):
                restore_release_action_checkpoint(json.dumps(changed, sort_keys=True, separators=(",", ":")).encode())
        self.run.full_gate = replace(self.run.full_gate, outcome="failed")
        self.run.results[9] = replace(self.run.results[9], output=self.run.full_gate)
        with self.assertRaises(ReleaseContractError):
            encode_release_action_checkpoint(self.run)

    def test_rejects_unknown_member_digest_root_and_phase_continuity_forgeries(self) -> None:
        payload = json.loads(encode_release_action_checkpoint(self.run))
        for mutate in (
            lambda value: value.update({"unexpected": True}),
            lambda value: value.update({"sha256": _digest("0")}),
            lambda value: value.update({"project_root": "/tmp"}),
            lambda value: value.update({"next_phase": 2}),
        ):
            with self.subTest(mutate=mutate):
                changed = copy.deepcopy(payload)
                mutate(changed)
                with self.assertRaises(Exception):
                    restore_release_action_checkpoint(json.dumps(changed, sort_keys=True, separators=(",", ":")).encode())

    def test_rejects_executable_output_and_unadmitted_executor(self) -> None:
        self.run.results[0] = ReleasePhaseResult(
            "workflow-1", "step-0", "action-0", *PHASES[0], "completed", "frozen",
            self.candidate.manifest.sha256, (), (), ("journal-event-1",), output=lambda: None,
        )
        with self.assertRaises(Exception):
            encode_release_action_checkpoint(self.run)

    def test_load_returns_only_exact_shared_terminal_receipt_records(self) -> None:
        payload = dump_release_checkpoint(
            self.run,
            shared_recordings={
                0: {
                    "terminal_outcome": "completed",
                    "receipt_refs": ("journal-event-1", "journal-event-2"),
                }
            },
        )
        restored, recordings = load_release_checkpoint(
            payload,
            expected_request=self.request,
            expected_workflow_run_id="workflow-1",
        )
        self.assertEqual(restored, restore_release_action_checkpoint(encode_release_action_checkpoint(self.run)))
        self.assertEqual(
            recordings,
            {0: {"terminal_outcome": "completed", "receipt_refs": ("journal-event-1", "journal-event-2")}},
        )

        wrong_run = copy.deepcopy(payload)
        wrong_run["workflow_run_id"] = "workflow-2"
        wrong_run["sha256"] = "0" * 64
        wrong_run["sha256"] = release_action_checkpoint_sha256(wrong_run)
        with self.assertRaises(Exception):
            load_release_checkpoint(
                wrong_run,
                expected_request=self.request,
                expected_workflow_run_id="workflow-1",
            )

    def test_pending_recording_event_identity_is_separate_from_terminal_receipts(self) -> None:
        payload = dump_release_checkpoint(
            self.run,
            pending_recordings={
                0: {"event_id": "pending-journal-event-1", "event_outcome": "completed"},
            },
        )
        restored, recordings = load_release_checkpoint(
            payload,
            expected_request=self.request,
            expected_workflow_run_id="workflow-1",
        )
        self.assertEqual(restored.results, self.run.results)
        self.assertEqual(recordings, {})
        pending = extract_pending_recordings(payload)
        self.assertEqual(
            dict(pending),
            {0: {"event_id": "pending-journal-event-1", "event_outcome": "completed"}},
        )
        with self.assertRaises(TypeError):
            pending[0] = {"event_id": "other", "event_outcome": "completed"}
        with self.assertRaises(TypeError):
            pending[0]["event_id"] = "other"

    def test_rejects_pending_recording_that_claims_a_receipt_or_invalid_original_outcome(self) -> None:
        with self.assertRaises(Exception):
            dump_release_checkpoint(
                self.run,
                shared_recordings={
                    0: {"terminal_outcome": "completed", "receipt_refs": ("journal-event-1",)},
                },
                pending_recordings={
                    0: {"event_id": "pending-journal-event-1", "event_outcome": "completed"},
                },
            )
        payload = dump_release_checkpoint(
            self.run,
            pending_recordings={
                0: {"event_id": "pending-journal-event-1", "event_outcome": "completed"},
            },
        )
        payload["pending_recordings"][0]["event_outcome"] = "invented-success"
        payload["sha256"] = release_action_checkpoint_sha256(payload)
        with self.assertRaises(Exception):
            extract_pending_recordings(payload)

    def test_rejects_reused_pending_event_identity_across_two_phases(self) -> None:
        second_context = SelectedReleaseActionContext(
            PROJECT_ROOT, "workflow-1", "step-1", "action-1", "workflow-1", "step-1",
            *PHASES[1][:2], self.run.frozen_parameters_sha256,
        )
        self.run.contexts[1] = second_context
        self.run.results[1] = ReleasePhaseResult(
            "workflow-1", "step-1", "action-1", *PHASES[1], "completed", "validated",
            self.candidate.manifest.sha256, (), (), ("journal-event-2",), output=self.candidate,
        )
        self.run.next_phase = 2
        with self.assertRaises(Exception):
            dump_release_checkpoint(
                self.run,
                pending_recordings={
                    0: {"event_id": "pending-journal-event-1", "event_outcome": "completed"},
                    1: {"event_id": "pending-journal-event-1", "event_outcome": "completed"},
                },
            )


if __name__ == "__main__":
    unittest.main()
