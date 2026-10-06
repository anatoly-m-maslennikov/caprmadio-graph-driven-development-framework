"""Behavioral contract tests for the private bounded candidate-E2E gate.

Every command result here is synthetic MOCK DATA ONLY.  The presealed golden
fixture uses real readers, but these tests neither run Docker nor publish or
promote a Release.
"""
from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
import inspect
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

RELEASE_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = RELEASE_ROOT.parents[3]
TEST_ROOT = Path(__file__).resolve().parent
for directory in (RELEASE_ROOT, TEST_ROOT):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import release_e2e_gate as gate  # noqa: E402
from release_contract import ReleaseContractError, canonical_json  # noqa: E402
from release_e2e_gate import (  # noqa: E402
    CandidateE2EGateEvidence,
    DEFAULT_RELEASE_E2E_LIMITS,
    E2EExecutionResult,
    ExecutableIdentity,
    FrozenHostE2ECapability,
    HostE2EExecutor,
    run_candidate_e2e_gate,
    verify_bound_candidate_e2e_evidence,
)
from release_e2e_golden.fixture import HARNESS_BASENAMES, materialize  # noqa: E402


_PASSING_JUNIT = b"<testsuite tests='1' failures='0' errors='0' skipped='0'><testcase name='ok'/></testsuite>"


class _RecordingExecutor:
    """A marked double that observes only the gate's fixed command vectors."""

    execution_kind = "test-double"

    def __init__(self, image_digest: str, *, junit_payloads: tuple[bytes | None, ...] = (_PASSING_JUNIT,),
                 inspect_result: E2EExecutionResult | None = None,
                 harness_results: tuple[E2EExecutionResult, ...] = (), after_harness=None) -> None:
        self.image_digest = image_digest
        self.junit_payloads = junit_payloads
        self.inspect_result = inspect_result
        self.harness_results = harness_results
        self.after_harness = after_harness
        self.calls: list[tuple[tuple[str, ...], Path, dict[str, str], float]] = []
        self.harness_count = 0

    def run(self, argv, *, cwd, environment, timeout_seconds):
        self.calls.append((tuple(argv), cwd, dict(environment), timeout_seconds))
        if tuple(argv[:3]) == ("docker", "image", "inspect"):
            return self.inspect_result or E2EExecutionResult(0, (self.image_digest + "\n").encode(), b"")
        ordinal = self.harness_count
        self.harness_count += 1
        report = Path(argv[argv.index("--junit") + 1])
        junit_payload = self.junit_payloads[min(ordinal, len(self.junit_payloads) - 1)]
        if junit_payload is not None:
            report.write_bytes(junit_payload)
        if self.after_harness is not None:
            self.after_harness(ordinal)
        if self.harness_results:
            return self.harness_results[min(ordinal, len(self.harness_results) - 1)]
        return E2EExecutionResult(0, b"MOCK DATA ONLY: harness observation\n", b"")


class ReleaseE2EGateContractTests(unittest.TestCase):
    def _fixture(self):
        retained = PROJECT_ROOT / ".caprmedio_tmp/tests/release-e2e"
        retained.mkdir(parents=True, exist_ok=True)
        fixture = materialize(Path(tempfile.mkdtemp(prefix="golden-", dir=retained)))
        fixture.verify_receipts()
        return fixture

    @staticmethod
    def _digest(payload: bytes) -> str:
        return hashlib.sha256(payload).hexdigest()

    @staticmethod
    def _golden_host_capability() -> FrozenHostE2ECapability:
        """Schema-valid fake freeze used only while HostE2EExecutor.run is patched."""

        path = Path(sys.executable).resolve()
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        controller = ExecutableIdentity("n_host_controller", str(path), digest)
        python = ExecutableIdentity("python", str(path), digest)
        driver = ExecutableIdentity("driver", str(path), digest)
        docker = ExecutableIdentity("docker", str(path), digest)
        return FrozenHostE2ECapability(
            "a" * 64, "b" * 64, "c" * 64,
            controller, python, driver, docker, str(path.parent),
        )

    def _run_double(self, fixture, executor: _RecordingExecutor):
        return run_candidate_e2e_gate(
            fixture.candidate, fixture.compilation, fixture.unit_suite, fixture.image,
            image_build=fixture.image_build, executor=executor,
        )

    def _run_patched_host(self, fixture, executor: _RecordingExecutor):
        capability = self._golden_host_capability()
        with (
            patch.object(HostE2EExecutor, "freeze_capability", return_value=capability) as freeze,
            patch.object(HostE2EExecutor, "revalidate_capability", return_value=None),
            patch.object(HostE2EExecutor, "run", side_effect=executor.run),
        ):
            evidence = run_candidate_e2e_gate(
                fixture.candidate, fixture.compilation, fixture.unit_suite, fixture.image,
                image_build=fixture.image_build, executor=HostE2EExecutor(),
            )
        return evidence, capability, freeze

    def _verify_host_evidence(self, fixture, evidence: CandidateE2EGateEvidence):
        with patch.object(HostE2EExecutor, "revalidate_capability", return_value=None):
            return verify_bound_candidate_e2e_evidence(
                fixture.candidate, fixture.compilation, fixture.unit_suite, fixture.image, evidence,
                image_build=fixture.image_build,
            )

    def _host_evidence(self):
        fixture = self._fixture()
        executor = _RecordingExecutor(fixture.image.candidate_image_digest)
        evidence, _capability, _freeze = self._run_patched_host(fixture, executor)
        self.assertEqual("passed", evidence.outcome, evidence.reason)
        self.assertEqual("host-subprocess", evidence.execution_kind)
        return fixture, evidence, executor

    def _rewrite_evidence_receipt(self, fixture, evidence: CandidateE2EGateEvidence) -> CandidateE2EGateEvidence:
        bare = replace(evidence, receipt_sha256=None)
        payload = canonical_json(asdict(bare))
        (fixture.root / bare.evidence_root / "receipt.json").write_bytes(payload)
        return replace(bare, receipt_sha256=self._digest(payload))

    def test_confirmed_private_gate_signature_and_evidence_fields(self) -> None:
        signature = inspect.signature(run_candidate_e2e_gate)
        self.assertEqual(("candidate", "compilation", "unit_suite", "image", "image_build", "executor"), tuple(signature.parameters))
        self.assertIn(signature.parameters["image"].kind, (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD))
        self.assertTrue(signature.parameters["image_build"].kind is inspect.Parameter.KEYWORD_ONLY)
        self.assertTrue(signature.parameters["executor"].kind is inspect.Parameter.KEYWORD_ONLY)
        self.assertTrue({
            "candidate_snapshot_manifest_sha256", "candidate_image_digest", "phase_map_sha256", "grammar_sha256",
            "outcome", "reason", "harness_receipts", "evidence_root", "receipt_sha256", "execution_kind",
            "settings_snapshot_path", "settings_snapshot_sha256", "host_capability_path", "host_capability_sha256",
        }.issubset(CandidateE2EGateEvidence.__dataclass_fields__))

    def test_static_grammar_has_only_the_three_pinned_harnesses_and_closed_environment(self) -> None:
        grammar = json.loads((RELEASE_ROOT / "release_e2e_bindings.json").read_bytes())
        self.assertEqual(1, grammar["schema_version"])
        self.assertEqual(("PATH", "TMPDIR", "CAPRMEDIO_RELEASE_E2E_CONTEXT", "CAPRMEDIO_CANDIDATE_IMAGE_DIGEST"), tuple(grammar["environment_keys"]))
        self.assertEqual(HARNESS_BASENAMES, tuple(Path(row["source_path"]).name for row in grammar["harnesses"]))
        for row in grammar["harnesses"]:
            self.assertEqual("run_release_e2e.py", Path(row["argv"][1]).name)
            self.assertEqual(("--start-directory", "--pattern", "--junit"), tuple(item for item in row["argv"] if item.startswith("--")))

    def test_full_three_junit_test_double_is_explicitly_incomplete_and_cannot_promote(self) -> None:
        fixture = self._fixture()
        before_selector = (fixture.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        executor = _RecordingExecutor(fixture.image.candidate_image_digest)

        evidence = self._run_double(fixture, executor)

        self.assertEqual("incomplete", evidence.outcome)
        self.assertEqual("test-double", evidence.execution_kind)
        self.assertFalse(evidence.passed)
        self.assertEqual(3, len(evidence.harness_receipts))
        self.assertTrue(all(receipt.executed_tests == 1 and receipt.junit_sha256 for receipt in evidence.harness_receipts))
        self.assertEqual(before_selector, (fixture.root / ".caprmedio_runtime/framework/current.toml").read_bytes())
        self.assertFalse((fixture.root / ".caprmedio_runtime/releases/N+1").exists())
        self.assertEqual(4, len(executor.calls))

    def test_patched_host_freeze_proves_fixed_command_boundary_and_bound_receipt(self) -> None:
        fixture = self._fixture()
        executor = _RecordingExecutor(fixture.image.candidate_image_digest)

        evidence, capability, freeze = self._run_patched_host(fixture, executor)

        self.assertEqual("passed", evidence.outcome, evidence.reason)
        self.assertTrue(evidence.passed)
        self.assertIsNotNone(evidence.host_capability_path)
        freeze.assert_called_once_with(fixture.root, fixture.candidate)
        self.assertEqual(4, len(executor.calls))
        inspect, *harnesses = executor.calls
        self.assertEqual(
            ("docker", "image", "inspect", "--format", "{{.Id}}", fixture.image.candidate_image_digest),
            inspect[0],
        )
        grammar = json.loads((fixture.root / gate.GRAMMAR_RELATIVE).read_bytes())
        self.assertEqual(3, len(harnesses))
        for call, row in zip(harnesses, grammar["harnesses"], strict=True):
            argv, cwd, environment, timeout = call
            self.assertEqual(fixture.root, cwd)
            self.assertEqual((capability.python.path, capability.n_host_controller.path), argv[:2])
            self.assertEqual(tuple(row["argv"][2:7]), argv[2:7])
            self.assertTrue(argv[-1].startswith(str(fixture.root / evidence.evidence_root / "scratch/reports")))
            self.assertEqual(DEFAULT_RELEASE_E2E_LIMITS.harness_timeout_seconds, timeout)
            self.assertEqual(
                {"PATH", "TMPDIR", "CAPRMEDIO_RELEASE_E2E_CONTEXT", "CAPRMEDIO_CANDIDATE_IMAGE_DIGEST"},
                set(environment),
            )
            self.assertEqual(capability.closed_path, environment["PATH"])
            self.assertEqual(fixture.image.candidate_image_digest, environment["CAPRMEDIO_CANDIDATE_IMAGE_DIGEST"])
        self.assertEqual(DEFAULT_RELEASE_E2E_LIMITS.inspect_timeout_seconds, inspect[3])
        self.assertEqual(fixture.root, self._verify_host_evidence(fixture, evidence))

    def test_tampered_suite_and_image_predecessors_are_refused_before_any_command(self) -> None:
        for label, evidence_name in (("suite", "unit_suite"), ("image", "image")):
            with self.subTest(predecessor=label):
                fixture = self._fixture()
                predecessor = getattr(fixture, evidence_name)
                receipt = fixture.root / predecessor.evidence_root / "receipt.json"
                receipt.write_bytes(receipt.read_bytes() + b"tampered mock receipt")
                executor = _RecordingExecutor(fixture.image.candidate_image_digest)
                with self.assertRaises(ReleaseContractError):
                    self._run_double(fixture, executor)
                self.assertEqual([], executor.calls)

    def test_returned_receipt_host_identity_output_and_junit_mutations_are_rejected(self) -> None:
        fixture, evidence, _executor = self._host_evidence()
        self.assertEqual(fixture.root, self._verify_host_evidence(fixture, evidence))
        paths = {
            "receipt": fixture.root / evidence.evidence_root / "receipt.json",
            "host identities": fixture.root / evidence.host_capability_path,
            "stdout": fixture.root / evidence.evidence_root / "harness-0.stdout.bin",
            "junit": fixture.root / evidence.evidence_root / "harness-0.junit.xml",
        }
        for label, path in paths.items():
            with self.subTest(artifact=label):
                original = path.read_bytes()
                try:
                    if label == "junit":
                        path.unlink()
                    else:
                        path.write_bytes(original + b"tampered")
                    with self.assertRaises(ReleaseContractError):
                        self._verify_host_evidence(fixture, evidence)
                finally:
                    path.write_bytes(original)

    def test_harness_receipt_metadata_is_source_pinned_timed_and_path_bound(self) -> None:
        fixture, evidence, _executor = self._host_evidence()
        first, *rest = evidence.harness_receipts
        self.assertTrue({
            "source_path", "source_sha256", "argv", "started_at", "finished_at",
            "stdout_path", "stdout_sha256", "stderr_path", "stderr_sha256",
            "junit_path", "junit_sha256",
        }.issubset(type(first).__dataclass_fields__))
        self.assertIn(Path(first.source_path).name, HARNESS_BASENAMES)
        self.assertTrue(first.source_sha256)
        self.assertLessEqual(first.started_at, first.finished_at)
        self.assertTrue(first.stdout_path.startswith(evidence.evidence_root + "/"))
        self.assertTrue(first.stderr_path.startswith(evidence.evidence_root + "/"))
        self.assertTrue(first.junit_path.startswith(evidence.evidence_root + "/"))
        receipt_path = fixture.root / evidence.evidence_root / "receipt.json"
        original = receipt_path.read_bytes()
        mutations = {
            "source SHA": {"source_sha256": "f" * 64},
            "timestamps": {"started_at": "2099-01-01T00:00:00+00:00"},
            "stdout path": {"stdout_path": first.stderr_path},
            "JUnit path": {"junit_path": first.stdout_path},
            "full argv": {"argv": (*first.argv[:-1], first.argv[-1] + ".other")},
        }
        try:
            for label, fields in mutations.items():
                with self.subTest(binding=label):
                    altered = replace(evidence, harness_receipts=(replace(first, **fields), *rest))
                    forged = self._rewrite_evidence_receipt(fixture, altered)
                    with self.assertRaises(ReleaseContractError):
                        self._verify_host_evidence(fixture, forged)
                    receipt_path.write_bytes(original)
        finally:
            receipt_path.write_bytes(original)

    def test_cross_candidate_and_phase_map_receipts_are_rejected_even_when_self_consistent(self) -> None:
        fixture, evidence, _executor = self._host_evidence()
        receipt_path = fixture.root / evidence.evidence_root / "receipt.json"
        original = receipt_path.read_bytes()
        try:
            for label, changed in (
                ("candidate", replace(evidence, candidate_snapshot_manifest_sha256="f" * 64)),
                ("phase map", replace(evidence, phase_map_sha256="e" * 64)),
            ):
                with self.subTest(binding=label):
                    forged = self._rewrite_evidence_receipt(fixture, changed)
                    with self.assertRaises(ReleaseContractError):
                        self._verify_host_evidence(fixture, forged)
                    receipt_path.write_bytes(original)
        finally:
            receipt_path.write_bytes(original)

    def test_zero_skipped_failed_and_errored_junit_are_nonpassing(self) -> None:
        fixture = self._fixture()
        cases = {
            "zero": b"<testsuite tests='0' failures='0' errors='0' skipped='0'/>",
            "skipped": b"<testsuite tests='1' failures='0' errors='0' skipped='1'><testcase><skipped/></testcase></testsuite>",
            "failed": b"<testsuite tests='1' failures='1' errors='0' skipped='0'><testcase><failure/></testcase></testsuite>",
            "errored": b"<testsuite tests='1' failures='0' errors='1' skipped='0'><testcase><error/></testcase></testsuite>",
            "malformed": b"<testsuite>",
            "empty": b"",
        }
        for label, junit in cases.items():
            with self.subTest(junit=label):
                evidence = self._run_double(
                    fixture, _RecordingExecutor(fixture.image.candidate_image_digest, junit_payloads=(junit,)),
                )
                self.assertEqual("incomplete", evidence.outcome)
                self.assertEqual(1, len(evidence.harness_receipts))
                receipt = evidence.harness_receipts[0]
                self.assertEqual(self._digest(junit), receipt.junit_sha256)
                self.assertEqual(junit, (fixture.root / receipt.junit_path).read_bytes())
                self.assertTrue(receipt.reason)

        missing = self._run_double(
            fixture, _RecordingExecutor(fixture.image.candidate_image_digest, junit_payloads=(None,)),
        )
        self.assertEqual("incomplete", missing.outcome)
        missing_receipt = missing.harness_receipts[0]
        self.assertIsNone(missing_receipt.junit_sha256)
        self.assertFalse((fixture.root / missing_receipt.junit_path).exists())

    def test_default_six_limits_bound_byte_caps_timeouts_and_cleanup_uncertainty(self) -> None:
        fixture = self._fixture()
        limit = DEFAULT_RELEASE_E2E_LIMITS.max_stdout_bytes
        timeout = self._run_double(
            fixture,
            _RecordingExecutor(
                fixture.image.candidate_image_digest,
                inspect_result=E2EExecutionResult(0, (fixture.image.candidate_image_digest + "\n").encode(), b"", timed_out=True),
            ),
        )
        self.assertEqual("timed_out", timeout.outcome)
        self.assertEqual(DEFAULT_RELEASE_E2E_LIMITS.inspect_timeout_seconds, 60.0)
        self.assertEqual(DEFAULT_RELEASE_E2E_LIMITS.harness_timeout_seconds, 900.0)
        self.assertEqual(DEFAULT_RELEASE_E2E_LIMITS.cleanup_timeout_seconds, 60.0)
        self.assertEqual((8 * 1024 * 1024,) * 3, (
            DEFAULT_RELEASE_E2E_LIMITS.max_stdout_bytes,
            DEFAULT_RELEASE_E2E_LIMITS.max_stderr_bytes,
            DEFAULT_RELEASE_E2E_LIMITS.max_junit_bytes,
        ))

        overflowing = self._run_double(
            fixture,
            _RecordingExecutor(
                fixture.image.candidate_image_digest,
                harness_results=(E2EExecutionResult(0, b"x" * (limit + 1), b""),),
            ),
        )
        self.assertEqual("incomplete", overflowing.outcome)
        self.assertEqual(limit, (fixture.root / overflowing.evidence_root / "harness-0.stdout.bin").stat().st_size)

        junit_overflow = self._run_double(
            fixture,
            _RecordingExecutor(
                fixture.image.candidate_image_digest,
                junit_payloads=(_PASSING_JUNIT + b" " * DEFAULT_RELEASE_E2E_LIMITS.max_junit_bytes,),
            ),
        )
        self.assertEqual("incomplete", junit_overflow.outcome)
        overflow_receipt = junit_overflow.harness_receipts[0]
        self.assertIsNone(overflow_receipt.junit_sha256)
        self.assertFalse((fixture.root / overflow_receipt.junit_path).exists())
        self.assertIn("too large", overflow_receipt.reason)

        cleanup_uncertain = self._run_double(
            fixture,
            _RecordingExecutor(
                fixture.image.candidate_image_digest,
                harness_results=(E2EExecutionResult(0, b"", b"", cleanup_uncertain=True),),
            ),
        )
        self.assertEqual("incomplete", cleanup_uncertain.outcome)
        self.assertIn("cleanup", cleanup_uncertain.reason)

        settings = json.loads((fixture.root / timeout.settings_snapshot_path).read_bytes())
        self.assertEqual({
            "inspect_timeout_seconds": 60.0,
            "harness_timeout_seconds": 900.0,
            "cleanup_timeout_seconds": 60.0,
            "max_stdout_bytes": 8 * 1024 * 1024,
            "max_stderr_bytes": 8 * 1024 * 1024,
            "max_junit_bytes": 8 * 1024 * 1024,
        }, settings["limits"])

    def test_source_and_framework_settings_drift_after_observation_make_evidence_stale(self) -> None:
        for label in ("source", "settings"):
            with self.subTest(drift=label):
                fixture = self._fixture()
                if label == "source":
                    source_path = next(
                        row.source_path for row in fixture.candidate.manifest.source_inventory_rows
                        if row.source_path.endswith(".py")
                    )
                    target = fixture.root / source_path
                else:
                    target = fixture.root / gate.FRAMEWORK_SETTINGS_RELATIVE
                original = target.read_bytes()

                def drift(_ordinal: int) -> None:
                    target.write_bytes(original + b"\n# synthetic drift after observation\n")

                evidence = self._run_double(
                    fixture,
                    _RecordingExecutor(fixture.image.candidate_image_digest, after_harness=drift),
                )
                self.assertEqual("stale", evidence.outcome)
                self.assertTrue(evidence.reason)


if __name__ == "__main__":
    unittest.main()
