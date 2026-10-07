"""Disposable selector/Skill effects with explicitly mocked Docker CLI output.

Production-shaped CLI receipts and patched image gate observations are not
actual image or Project promotion proof. Selector/Skill/receipt files are real.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
import tempfile
import tomllib
import unittest
import xml.etree.ElementTree as ET
from contextlib import contextmanager
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_contract import ReleaseContractError
import release_e2e_gate as _release_e2e_gate
from release_e2e_gate import (
    E2EExecutionResult,
    ExecutableIdentity,
    FrozenHostE2ECapability,
    HostE2EExecutor,
    run_candidate_e2e_gate,
)
from release_full_gate import aggregate_bound_release_gates
from release_compilation import build_preflight_validated_candidate, render_release_candidate
from release_handoff import CURRENT_SELECTOR_RELATIVE, PackageRow
from release_packaging import RUNTIME_ROOT, _render_manifest, stage_framework_package
from release_promotion import promote_bound_release, verify_bound_promotion_evidence
import release_promotion as _release_promotion
from selector_publication_lock import SelectorPublicationLockError, selector_publication_lock
import test_release_image as image_test


_RECORDED_HOST_CAPABILITIES: dict[str, FrozenHostE2ECapability] = {}
_REAL_FREEZE_CAPABILITY = HostE2EExecutor.freeze_capability


def _recorded_host_capability(candidate, suite) -> FrozenHostE2ECapability:
    """Build a schema-valid host capability for command-only Unit fixtures.

    The Docker carrier is a disposable executable-shaped file under the
    candidate fixture and is never invoked.  This keeps receipt readers on
    the production capability schema without making Unit evidence claim live
    Docker or Candidate E2E proof.
    """
    python = Path(sys.executable).resolve()
    n_driver = (
        Path(candidate.project_root) / RUNTIME_ROOT / "releases" / candidate.authority.executing_release
        / "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_e2e.py"
    )
    docker = Path(candidate.project_root) / ".caprmedio_tmp/mock-docker"
    docker.parent.mkdir(parents=True, exist_ok=True)
    docker.write_bytes(b"#!/bin/false\n# MOCK DATA ONLY: never executed by this Unit fixture\n")
    docker.chmod(0o755)

    def identity(role, path):
        return ExecutableIdentity(role, str(path), hashlib.sha256(path.read_bytes()).hexdigest())

    return FrozenHostE2ECapability(
        suite.executing_selector_sha256,
        suite.executing_release_package_sha256,
        suite.executing_skill_sha256,
        identity("n_host_controller", n_driver),
        identity("python", python),
        identity("driver", n_driver),
        identity("docker", docker),
        str(docker.parent),
    )


def _recorded_freeze(root, candidate):
    capability = _RECORDED_HOST_CAPABILITIES.get(str(Path(root).resolve()))
    if capability is None:
        return _REAL_FREEZE_CAPABILITY(root, candidate)
    # Keep the production freeze/reopen checks for N, Python and the N driver;
    # only select the disposable fixture Docker carrier in this Unit process.
    with patch.object(_release_e2e_gate, "_DOCKER_CANDIDATES", (capability.docker.path,)):
        return _REAL_FREEZE_CAPABILITY(root, candidate)


@contextmanager
def recorded_host_patches():
    """Bind the Unit-only capability seam for all later receipt reopenings."""
    with patch.object(HostE2EExecutor, "freeze_capability", side_effect=_recorded_freeze):
        yield


def recorded_gate_fixtures(candidate, compilation, suite, build, verification):
    """Retain mocked host command reports while reopening all receipt bytes.

    The capability has the production schema but uses a disposable, never
    executed Docker carrier. Only host command execution is replaced; this
    fixture is never live Docker or Candidate E2E proof.
    """
    capability = _recorded_host_capability(candidate, suite)
    _RECORDED_HOST_CAPABILITIES[str(Path(candidate.project_root).resolve())] = capability

    def command(argv, *, cwd, environment, timeout_seconds):
        if argv[:3] == ("docker", "image", "inspect"):
            return E2EExecutionResult(0, (verification.candidate_image_digest + "\n").encode(), b"")
        pattern = argv[argv.index("--pattern") + 1]
        report = ET.Element("testsuite", tests="1", failures="0", errors="0", skipped="0")
        ET.SubElement(report, "testcase", classname=Path(pattern).stem + ".MockGoldenHarness", name="test_mocked_host_command")
        Path(argv[argv.index("--junit") + 1]).write_bytes(ET.tostring(report))
        return E2EExecutionResult(0, b"MOCK DATA ONLY: E2E report\n", b"")

    with recorded_host_patches(), patch.object(HostE2EExecutor, "run", side_effect=command):
        e2e = run_candidate_e2e_gate(candidate, compilation, suite, verification,
                                     image_build=build, executor=HostE2EExecutor())
    if not e2e.passed:
        raise AssertionError(e2e.reason)
    full_gate = aggregate_bound_release_gates(candidate, compilation, suite, build, verification, e2e)
    if not full_gate.passed:
        raise AssertionError(full_gate.reason)
    return {"e2e": e2e, "full_gate": full_gate}


class ReleasePromotionTests(unittest.TestCase):
    def setUp(self):
        self.fixture = image_test.ReleaseImageTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.candidate, self.compilation, self.suite = self.fixture.candidate, self.fixture.compilation, self.fixture.suite
        # CLI execution is mocked by this fixture producer, never live Docker.
        self.build, self.verification = self.fixture.recorded_command_fixtures()
        self.args = (self.candidate, self.compilation, self.suite, self.build, self.verification)
        self._host_patches = recorded_host_patches()
        self._host_patches.__enter__()
        self.addCleanup(self._host_patches.__exit__, None, None, None)
        self.gates = recorded_gate_fixtures(*self.args)
        self.selector = self.root / CURRENT_SELECTOR_RELATIVE
        self.public = self.root / ".agents/skills/ca"
        self.gate = patch("release_promotion.verify_bound_image_evidence", return_value=self.root)

    def promote(self):
        # Admission and artifact readers run normally on recorded mocked CLI
        # data; only fixture construction above replaces Docker execution.
        return promote_bound_release(*self.args, **self.gates)

    def test_recorded_host_revalidation_refuses_mutated_mock_docker_carrier(self):
        capability = _RECORDED_HOST_CAPABILITIES[str(self.root.resolve())]
        Path(capability.docker.path).write_bytes(b"#!/bin/false\n# MUTATED MOCK DATA\n")
        with self.assertRaises(ReleaseContractError) as raised:
            HostE2EExecutor.revalidate_capability(self.root, self.candidate, capability)
        self.assertEqual(raised.exception.code, "release-currentness-stale")

    def test_golden_actual_selector_complete_skill_no_hooks_and_exact_retry(self):
        prior = self.selector.read_bytes()
        unrelated = self.root / ".agents/skills/other/SKILL.md"
        unrelated.parent.mkdir(parents=True)
        unrelated.write_bytes(b"unrelated")
        result = self.promote()
        self.assertEqual(result.outcome, "promoted")
        selection = tomllib.loads(self.selector.read_text())
        self.assertEqual(selection["release"], self.candidate.manifest.sha256)
        self.assertEqual(selection["candidate_snapshot_manifest_sha256"], self.candidate.manifest.sha256)
        self.assertEqual(selection["candidate_image_digest"], image_test.IMAGE_ID)
        self.assertEqual(selection["framework_engine_root"], result.framework_engine_root)
        self.assertEqual(selection["methodology_root"], result.methodology_root)
        package = self.root / result.selected_release_root / "SKILLS/ca"
        self.assertEqual({p.relative_to(self.public).as_posix(): p.read_bytes() for p in self.public.rglob("*") if p.is_file()},
                         {p.relative_to(package).as_posix(): p.read_bytes() for p in package.rglob("*") if p.is_file()})
        self.assertEqual((self.root / result.retained_prior_selector_ref).read_bytes(), prior)
        self.assertEqual(unrelated.read_bytes(), b"unrelated")
        self.assertFalse((self.root / ".git/hooks").exists())
        receipt = self.root / result.evidence_root / "receipt.json"
        self.assertEqual(hashlib.sha256(receipt.read_bytes()).hexdigest(), result.receipt_sha256)
        self.assertIsNone(result.prior_image_digest)
        selected = self.selector.read_bytes()
        again = self.promote()
        self.assertEqual(again.outcome, "promoted")
        self.assertEqual(again.intent_sha256, result.intent_sha256)
        self.assertEqual(self.selector.read_bytes(), selected)
        # The reader reopens production-shaped mocked CLI artifacts; no Docker.
        self.assertEqual(verify_bound_promotion_evidence(*self.args, result, **self.gates), self.root)

    def test_real_image_gate_refuses_test_double_before_any_exposure(self):
        prior = self.selector.read_bytes()
        prior_skill = (self.public / "SKILL.md").read_bytes()
        build = self.fixture.build()
        verified = image_test.verify_candidate_image(self.candidate, self.compilation, self.suite,
                                                      build, executor=self.fixture.docker)
        self.assertEqual(verified.execution_kind, "test-double")
        with self.assertRaises(ReleaseContractError):
            promote_bound_release(self.candidate, self.compilation, self.suite, build, verified, **self.gates)
        self.assertEqual(self.selector.read_bytes(), prior)
        self.assertEqual((self.public / "SKILL.md").read_bytes(), prior_skill)
        self.assertFalse((self.root / ".caprmedio_runtime/release_promotion").exists())

    def test_missing_forged_incomplete_or_cross_candidate_gate_refuses_before_admission(self):
        cases = (
            ("full_gate", None),
            ("full_gate", replace(self.gates["full_gate"], reason="caller-forged")),
            ("full_gate", replace(self.gates["full_gate"], outcome="incomplete")),
            ("full_gate", replace(self.gates["full_gate"], candidate_snapshot_manifest_sha256="f" * 64)),
            ("e2e", None),
            ("e2e", replace(self.gates["e2e"], reason="caller-forged")),
            ("e2e", replace(self.gates["e2e"], candidate_snapshot_manifest_sha256="f" * 64)),
        )
        before = self.fixture.fixture.fixture.snapshot()
        for member, evidence in cases:
            with self.subTest(member=member, evidence=evidence):
                with self.assertRaises(ReleaseContractError):
                    promote_bound_release(*self.args, **{**self.gates, member: evidence})
                self.assertEqual(self.fixture.fixture.fixture.snapshot(), before)
        with self.assertRaises(TypeError):
            promote_bound_release(*self.args)
        self.assertEqual(self.fixture.fixture.fixture.snapshot(), before)
        self.assertFalse((self.root / ".caprmedio_runtime/release_promotion").exists())

    def test_changed_full_gate_receipt_refuses_before_any_promotion_intent(self):
        receipt = self.root / self.gates["full_gate"].evidence_root / "receipt.json"
        receipt.write_bytes(receipt.read_bytes() + b" ")
        before = self.fixture.fixture.fixture.snapshot()
        with self.assertRaises(ReleaseContractError):
            self.promote()
        self.assertEqual(self.fixture.fixture.fixture.snapshot(), before)
        self.assertFalse((self.root / ".caprmedio_runtime/release_promotion").exists())

    def test_unknown_existing_skill_refuses_without_changing_selector_or_payload(self):
        self.public.mkdir(parents=True, exist_ok=True)
        (self.public / "SKILL.md").write_bytes(b"unknown owner")
        prior = self.selector.read_bytes()
        with self.assertRaises(ReleaseContractError) as raised:
            self.promote()
        self.assertEqual(raised.exception.code, "release-suite-evidence-mismatch")
        self.assertEqual(self.selector.read_bytes(), prior)
        self.assertEqual((self.public / "SKILL.md").read_bytes(), b"unknown owner")

    def prior_owned_skill(self):
        prior_id = "b" * 64
        package = self.root / ".caprmedio_runtime/framework/releases" / prior_id
        current = self.root / self.fixture.fixture.package["release_root"]
        shutil.copytree(current, package)
        (package / "SKILLS/ca/SKILL.md").write_bytes(b"# prior owned Skill\n")
        rows = [PackageRow.model_validate({**row.model_dump(mode="json"), "sha256": hashlib.sha256((package / row.destination_path).read_bytes()).hexdigest()})
                if row.destination_path == "SKILLS/ca/SKILL.md" else row for row in self.compilation.package_rows]
        (package / "manifest.toml").write_text(_render_manifest(prior_id, rows))
        self.public.parent.mkdir(parents=True, exist_ok=True)
        shutil.rmtree(self.public)
        shutil.copytree(package / "SKILLS/ca", self.public)
        self.selector.write_text(f'release = "{prior_id}"\nselected_release_root = ".caprmedio_runtime/framework/releases/{prior_id}"\ncandidate_image_digest = "sha256:{"c" * 64}"\n')
        preflight, self.candidate = build_preflight_validated_candidate(
            self.root, candidate_release="N+1", full_suite_environment=self.candidate.intent.full_suite_environment.model_dump(mode="json"),
            candidate_image_reference="disposable:N+1")
        self.compilation = render_release_candidate(self.candidate, preflight)
        stage_framework_package(self.root, self.compilation)
        self.suite = self.fixture.fixture.execute_suite(self.candidate, self.compilation)
        self.fixture.candidate, self.fixture.compilation, self.fixture.suite = self.candidate, self.compilation, self.suite
        self.build, self.verification = self.fixture.recorded_command_fixtures()
        self.args = (self.candidate, self.compilation, self.suite, self.build, self.verification)
        self.gates = recorded_gate_fixtures(*self.args)
        return package

    def test_exact_retained_prior_package_proves_owned_skill_and_preserves_it(self):
        package = self.prior_owned_skill()
        old = (self.public / "SKILL.md").read_bytes()
        result = self.promote()
        self.assertEqual(result.outcome, "promoted")
        self.assertEqual(result.prior_image_digest, "sha256:" + "c" * 64)
        self.assertIsNotNone(result.retained_prior_skill_ref)
        self.assertEqual((self.root / result.retained_prior_skill_ref / "SKILL.md").read_bytes(), old)
        self.assertEqual((package / "SKILLS/ca/SKILL.md").read_bytes(), old)
        self.assertNotEqual((self.public / "SKILL.md").read_bytes(), old)
        self.assertEqual(verify_bound_promotion_evidence(*self.args, result, **self.gates), self.root)
        (self.root / result.retained_prior_skill_ref / "SKILL.md").write_bytes(b"changed retained prior Skill")
        with self.assertRaises(ReleaseContractError) as caught:
            verify_bound_promotion_evidence(*self.args, result, **self.gates)
        self.assertEqual(caught.exception.code, "release-promotion-evidence-stale")

    def test_owned_prior_skill_gap_is_pending_then_exact_retry_recovers(self):
        self.prior_owned_skill()
        with self.gate, patch("release_promotion._publish_skill", side_effect=OSError("failure after prior retention")):
            result = promote_bound_release(*self.args, **self.gates)
        self.assertEqual(result.outcome, "pending")
        self.assertFalse(self.public.exists())
        self.assertTrue((self.root / result.retained_prior_skill_ref / "SKILL.md").is_file())
        self.assertEqual(self.promote().outcome, "promoted")

    def test_selector_publication_failure_remains_n_and_exact_retry_completes(self):
        prior = self.selector.read_bytes()
        with self.gate, patch("release_promotion._publish_selector", side_effect=OSError("deliberate failure")):
            result = promote_bound_release(*self.args, **self.gates)
        self.assertEqual(result.outcome, "pending")
        self.assertEqual(self.selector.read_bytes(), prior)
        self.assertTrue((self.public / "SKILL.md").is_file())
        self.assertEqual(self.promote().outcome, "promoted")

    def test_skill_publication_failure_has_candidate_selector_and_supported_exact_recovery(self):
        with self.gate, patch("release_promotion._publish_skill", side_effect=OSError("deliberate failure")):
            result = promote_bound_release(*self.args, **self.gates)
        self.assertEqual(result.outcome, "pending")
        self.assertEqual(tomllib.loads(self.selector.read_text())["release"], self.candidate.manifest.sha256)
        self.assertFalse(self.public.exists())
        # This must not invoke the old-N currentness image gate on recovery.
        with patch("release_promotion.verify_bound_image_evidence", side_effect=AssertionError("fresh replay forbidden")):
            recovered = promote_bound_release(*self.args, **self.gates)
        self.assertEqual(recovered.outcome, "promoted")
        self.assertTrue((self.public / "agents/openai.yaml").is_file())

    def test_completed_reader_and_retry_use_artifact_reader_without_old_n_or_docker_replay(self):
        result = self.promote()
        calls = len(self.fixture.docker.calls)
        with patch("release_promotion.verify_bound_image_evidence", side_effect=AssertionError("old-N admission replayed")), \
                patch("release_promotion.read_image_execution_artifacts", wraps=image_test.read_image_execution_artifacts) as reader:
            self.assertEqual(verify_bound_promotion_evidence(*self.args, result, **self.gates), self.root)
            self.assertEqual(promote_bound_release(*self.args, **self.gates).outcome, "promoted")
        self.assertGreaterEqual(reader.call_count, 3)
        self.assertEqual(len(self.fixture.docker.calls), calls)

    def test_artifact_reader_refusal_after_selection_keeps_skill_recovery_pending(self):
        with self.gate, patch("release_promotion._publish_skill", side_effect=OSError("deliberate publication failure")):
            result = promote_bound_release(*self.args, **self.gates)
        selected = self.selector.read_bytes()
        with patch("release_promotion.read_image_execution_artifacts",
                   side_effect=ReleaseContractError("release-image-evidence-untrusted", "retained image proof changed")) as reader:
            recovered = promote_bound_release(*self.args, **self.gates)
        self.assertEqual(recovered.outcome, "pending")
        self.assertIn("release-image-evidence-untrusted", recovered.reason)
        self.assertEqual(reader.call_count, 1)
        self.assertEqual(self.selector.read_bytes(), selected)
        self.assertFalse(self.public.exists())

    def test_completed_reader_refuses_changed_canary_package_source_skill_and_prior_selector(self):
        for changed in ("canary", "package", "source", "skill", "prior-selector"):
            with self.subTest(changed=changed):
                fixture = ReleasePromotionTests("run")
                fixture.setUp()
                try:
                    result = fixture.promote()
                    self.assertEqual(verify_bound_promotion_evidence(*fixture.args, result, **fixture.gates), fixture.root)
                    if changed == "canary":
                        path = fixture.root / fixture.verification.evidence_root / "command-1.stdout"
                    elif changed == "package":
                        path = fixture.root / result.selected_release_root / "SKILLS/ca/SKILL.md"
                    elif changed == "source":
                        path = fixture.fixture.fixture.fixture.core
                    elif changed == "skill":
                        path = fixture.public / "SKILL.md"
                    else:
                        path = fixture.root / result.retained_prior_selector_ref
                    path.write_bytes(path.read_bytes() + b"changed")
                    with self.assertRaises((ReleaseContractError, RuntimeError)):
                        verify_bound_promotion_evidence(*fixture.args, result, **fixture.gates)
                finally:
                    fixture.doCleanups()

    def test_retry_rejects_changed_typed_inputs_and_changed_pending_receipt(self):
        with self.gate, patch("release_promotion._publish_skill", side_effect=OSError("deliberate failure")):
            result = promote_bound_release(*self.args, **self.gates)
        with self.assertRaises(ReleaseContractError) as raised:
            promote_bound_release(self.candidate, self.compilation, self.suite,
                                  replace(self.build, reason="different intent"), self.verification, **self.gates)
        self.assertEqual(raised.exception.code, "release-promotion-retry-mismatch")
        intent = self.root / ".caprmedio_runtime/release_promotion" / self.candidate.manifest.sha256 / "intent.json"
        intent.write_bytes(intent.read_bytes() + b" ")
        with self.assertRaises(ReleaseContractError) as raised:
            self.promote()
        self.assertEqual(raised.exception.code, "release-promotion-intent-untrusted")

    def test_recovery_stale_source_or_gates_never_publishes_skill(self):
        for changed in ("source", "gate", "selector", "staged-skill"):
            with self.subTest(changed=changed):
                fixture = ReleasePromotionTests("run")
                fixture.setUp()
                try:
                    with fixture.gate, patch("release_promotion._publish_skill", side_effect=OSError("failure")):
                        result = promote_bound_release(*fixture.args, **fixture.gates)
                    if changed == "source":
                        fixture.fixture.fixture.fixture.core.write_bytes(b"stale source")
                    elif changed == "gate":
                        (fixture.root / fixture.suite.evidence_root / "stdout.bin").write_bytes(b"changed")
                    elif changed == "selector":
                        fixture.selector.write_bytes(b'release = "other"\n')
                    else:
                        (fixture.root / ".caprmedio_runtime/release_promotion" / fixture.candidate.manifest.sha256
                         / "candidate-skill/SKILL.md").write_bytes(b"changed")
                    recovered = fixture.promote()
                    self.assertEqual(recovered.outcome, "pending")
                    self.assertFalse(fixture.public.exists())
                finally:
                    fixture.doCleanups()

    def test_recording_uncertainty_does_not_claim_promoted_and_reconciles_same_effect(self):
        import release_promotion
        original = release_promotion._write
        def failing_receipt(path, payload, mode=0o644):
            if path.name == "receipt.json":
                raise OSError("deliberate observation failure")
            return original(path, payload, mode)
        with self.gate, patch("release_promotion._write", side_effect=failing_receipt):
            result = promote_bound_release(*self.args, **self.gates)
        self.assertEqual(result.outcome, "recording_uncertain")
        self.assertIsNone(result.receipt_sha256)
        self.assertTrue(self.public.is_dir())
        self.assertEqual(self.promote().outcome, "promoted")

    def test_symlinked_public_ancestor_refuses_before_selector_change(self):
        outside = self.root / "unknown"
        outside.mkdir()
        shutil.rmtree(self.root / ".agents")
        (self.root / ".agents").symlink_to(outside, target_is_directory=True)
        prior = self.selector.read_bytes()
        with self.assertRaises(ReleaseContractError):
            self.promote()
        self.assertEqual(self.selector.read_bytes(), prior)
        self.assertEqual(list(outside.iterdir()), [])


class PromotionPublicationLockTests(unittest.TestCase):
    """Public promotion ABI lock ownership; gate behavior remains in the corpus above."""

    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="promotion-publication-lock-")).resolve()
        self.candidate = SimpleNamespace(project_root=str(self.root))
        self.selector = self.root / CURRENT_SELECTOR_RELATIVE
        self.selector.parent.mkdir(parents=True)
        self.selector.write_bytes(b"retained selector bytes")
        self.args = (self.candidate, None, None, None, None)
        self.gates = {"e2e": None, "full_gate": None}

    def test_promotion_refuses_shared_lock_held_by_restoration_before_body(self):
        prior = self.selector.read_bytes()
        with selector_publication_lock(self.root, timeout_seconds=0):
            with patch.object(_release_promotion, "selector_publication_lock",
                              side_effect=lambda root: selector_publication_lock(root, timeout_seconds=0)):
                with patch.object(_release_promotion, "_promote_bound_release_locked") as body:
                    with self.assertRaises(SelectorPublicationLockError) as busy:
                        promote_bound_release(*self.args, **self.gates)
                    self.assertEqual("selector-publication-lock-busy", busy.exception.code)
                    body.assert_not_called()
        self.assertEqual(prior, self.selector.read_bytes())

    def test_public_promotion_owns_same_lock_until_body_observation_returns(self):
        observed = object()

        def body(*args, **gates):
            self.assertEqual(self.args, args)
            self.assertEqual(self.gates, gates)
            # The body encompasses the existing prior/intent reads, effects,
            # and receipt observation. Restoration uses this identical helper.
            with self.assertRaises(SelectorPublicationLockError):
                with selector_publication_lock(self.root, timeout_seconds=0):
                    self.fail("restoration crossed live promotion ownership")
            return observed

        with patch.object(_release_promotion, "_promote_bound_release_locked", side_effect=body):
            self.assertIs(observed, promote_bound_release(*self.args, **self.gates))
        with selector_publication_lock(self.root, timeout_seconds=0):
            pass


if __name__ == "__main__":
    unittest.main()
