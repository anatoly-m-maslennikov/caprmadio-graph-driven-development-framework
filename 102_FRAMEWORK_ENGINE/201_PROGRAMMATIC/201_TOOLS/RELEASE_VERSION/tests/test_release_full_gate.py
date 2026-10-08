"""Receipt-backed aggregate checks using synthetic presealed Release evidence.

Host command observations are MOCK DATA ONLY.  All predecessor receipt readers
remain real; these tests do not prove Docker execution or promote a Release.
"""
from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET


RELEASE_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = RELEASE_ROOT.parents[3]
TEST_ROOT = Path(__file__).resolve().parent
for directory in (RELEASE_ROOT, TEST_ROOT):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

from release_contract import ReleaseContractError, canonical_json  # noqa: E402
from release_e2e_gate import (  # noqa: E402
    E2EExecutionResult,
    ExecutableIdentity,
    FrozenHostE2ECapability,
    HostE2EExecutor,
    run_candidate_e2e_gate,
)
from release_e2e_golden.fixture import materialize  # noqa: E402
from release_full_gate import aggregate_bound_release_gates, verify_bound_full_gate_evidence  # noqa: E402
from release_packaging import RUNTIME_ROOT  # noqa: E402
from release_test_phases import derive_test_phase_map  # noqa: E402


class ReleaseFullGateContractTests(unittest.TestCase):
    @staticmethod
    def _digest(payload: bytes) -> str:
        return hashlib.sha256(payload).hexdigest()

    def _fixture(self):
        retained = PROJECT_ROOT / ".caprmedio_tmp/tests/release-full-gate"
        retained.mkdir(parents=True, exist_ok=True)
        return materialize(Path(tempfile.mkdtemp(prefix="golden-", dir=retained)))

    def _host_e2e(self, fixture, *, duplicate_case: bool = False, wrong_module: bool = False):
        path = Path(sys.executable).resolve()
        n_driver = (fixture.root / RUNTIME_ROOT / "releases"
                    / fixture.candidate.authority.executing_release
                    / "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_e2e.py")
        docker = fixture.root / ".caprmedio_tmp/mock-docker"
        docker.parent.mkdir(parents=True, exist_ok=True)
        docker.write_bytes(b"#!/bin/false\n# MOCK DATA ONLY: never executed\n")
        docker.chmod(0o755)
        def identity(role, executable):
            return ExecutableIdentity(role, str(executable), self._digest(executable.read_bytes()))

        capability = FrozenHostE2ECapability(
            fixture.unit_suite.executing_selector_sha256,
            fixture.unit_suite.executing_release_package_sha256,
            fixture.unit_suite.executing_skill_sha256,
            identity("n_host_controller", n_driver), identity("python", path),
            identity("driver", n_driver), identity("docker", docker), str(docker.parent),
        )

        def observe(argv, *, cwd, environment, timeout_seconds):
            if tuple(argv[:3]) == ("docker", "image", "inspect"):
                return E2EExecutionResult(0, (fixture.image.candidate_image_digest + "\n").encode(), b"")
            pattern = Path(argv[argv.index("--pattern") + 1]).stem
            classname = ("unknown_module" if wrong_module else pattern) + ".MockGoldenHarness"
            count = 2 if duplicate_case else 1
            report = ET.Element("testsuite", tests=str(count), failures="0", errors="0", skipped="0")
            for _ in range(count):
                ET.SubElement(report, "testcase", classname=classname, name="test_mock_case")
            Path(argv[argv.index("--junit") + 1]).write_bytes(ET.tostring(report))
            return E2EExecutionResult(0, b"MOCK DATA ONLY: fixed host observation\n", b"")

        with (
            patch.object(HostE2EExecutor, "freeze_capability", return_value=capability),
            patch.object(HostE2EExecutor, "revalidate_capability", return_value=None),
            patch.object(HostE2EExecutor, "run", side_effect=observe),
        ):
            evidence = run_candidate_e2e_gate(
                fixture.candidate, fixture.compilation, fixture.unit_suite, fixture.image,
                image_build=fixture.image_build, executor=HostE2EExecutor(),
            )
        self.assertTrue(evidence.passed, evidence.reason)
        return evidence

    def _aggregate(self, fixture, e2e):
        with patch.object(HostE2EExecutor, "revalidate_capability", return_value=None):
            return aggregate_bound_release_gates(
                fixture.candidate, fixture.compilation, fixture.unit_suite,
                fixture.image_build, fixture.image, e2e,
            )

    def _verify(self, fixture, e2e, full_gate):
        with patch.object(HostE2EExecutor, "revalidate_capability", return_value=None):
            return verify_bound_full_gate_evidence(
                fixture.candidate, fixture.compilation, fixture.unit_suite,
                fixture.image_build, fixture.image, e2e, full_gate,
            )

    def _rewrite_e2e_receipt(self, fixture, evidence):
        bare = replace(evidence, receipt_sha256=None)
        payload = canonical_json(asdict(bare))
        (fixture.root / bare.evidence_root / "receipt.json").write_bytes(payload)
        return replace(bare, receipt_sha256=self._digest(payload))

    def test_real_receipt_readers_accept_exact_partition_without_changing_frozen_bytes(self) -> None:
        fixture = self._fixture()
        e2e = self._host_e2e(fixture)

        evidence = self._aggregate(fixture, e2e)

        self.assertTrue(evidence.passed, evidence.reason)
        self.assertEqual(fixture.root, self._verify(fixture, e2e, evidence))
        self.assertEqual(derive_test_phase_map(fixture.candidate).sha256, evidence.phase_map_sha256)
        self.assertEqual(fixture.unit_suite.executed_tests + 3, evidence.executed_tests)
        self.assertEqual(
            (fixture.unit_suite.receipt_sha256, fixture.image_build.receipt_sha256,
             fixture.image.receipt_sha256, e2e.receipt_sha256),
            (evidence.suite_receipt_sha256, evidence.build_receipt_sha256,
             evidence.image_receipt_sha256, evidence.e2e_receipt_sha256),
        )
        for entry in fixture.before_snapshot:
            path = fixture.root / entry.path
            self.assertEqual(entry.sha256, self._digest(path.read_bytes()), entry.path)
            self.assertEqual(entry.mode, path.stat().st_mode & 0o777, entry.path)

    def test_predecessor_receipt_and_report_bytes_are_reopened_at_both_boundaries(self) -> None:
        fixture = self._fixture()
        e2e = self._host_e2e(fixture)
        evidence = self._aggregate(fixture, e2e)
        relatives = (
            f"{fixture.unit_suite.evidence_root}/receipt.json",
            f"{fixture.unit_suite.evidence_root}/coverage.xml",
            f"{fixture.image_build.evidence_root}/receipt.json",
            f"{fixture.image.evidence_root}/receipt.json",
            f"{e2e.evidence_root}/receipt.json",
            e2e.harness_receipts[0].junit_path,
        )
        for relative in relatives:
            with self.subTest(carrier=relative):
                path = fixture.root / relative
                original = path.read_bytes()
                try:
                    path.write_bytes(original + b"tampered mock bytes")
                    with self.assertRaises(ReleaseContractError):
                        self._aggregate(fixture, e2e)
                    with self.assertRaises(ReleaseContractError):
                        self._verify(fixture, e2e, evidence)
                finally:
                    path.write_bytes(original)

    def test_tampered_or_caller_forged_aggregate_receipt_is_rejected(self) -> None:
        fixture = self._fixture()
        e2e = self._host_e2e(fixture)
        evidence = self._aggregate(fixture, e2e)
        with self.assertRaises(ReleaseContractError):
            self._verify(fixture, e2e, replace(evidence, phase_map_sha256="f" * 64))
        receipt = fixture.root / evidence.evidence_root / "receipt.json"
        receipt.write_bytes(receipt.read_bytes() + b"tampered mock aggregate")
        with self.assertRaises(ReleaseContractError):
            self._verify(fixture, e2e, evidence)

    def test_missing_and_duplicate_harness_receipts_cannot_form_a_partition(self) -> None:
        for duplicate in (False, True):
            with self.subTest(duplicate=duplicate):
                fixture = self._fixture()
                e2e = self._host_e2e(fixture)
                rows = e2e.harness_receipts
                rows = (rows[0], rows[0], rows[2]) if duplicate else rows[:-1]
                altered = self._rewrite_e2e_receipt(fixture, replace(e2e, harness_receipts=rows))
                with self.assertRaises(ReleaseContractError):
                    self._aggregate(fixture, altered)

    def test_duplicate_observed_cases_retain_failed_aggregate_and_block_later_admission(self) -> None:
        fixture = self._fixture()
        e2e = self._host_e2e(fixture, duplicate_case=True)
        evidence = self._aggregate(fixture, e2e)
        self.assertEqual("failed", evidence.outcome)
        self.assertIn("duplicate testcase identities", evidence.reason)
        self.assertFalse(evidence.passed)
        self.assertTrue((fixture.root / evidence.evidence_root / "receipt.json").is_file())
        with self.assertRaises(ReleaseContractError):
            self._verify(fixture, e2e, evidence)

    def test_report_from_undeclared_module_is_not_complete_e2e_partition(self) -> None:
        fixture = self._fixture()
        e2e = self._host_e2e(fixture, wrong_module=True)
        evidence = self._aggregate(fixture, e2e)
        self.assertFalse(evidence.passed)
        self.assertIn("declared E2E module", evidence.reason)

    def test_self_consistent_cross_candidate_or_phase_receipt_is_rejected(self) -> None:
        for field in ("candidate_snapshot_manifest_sha256", "candidate_image_digest", "phase_map_sha256"):
            with self.subTest(binding=field):
                fixture = self._fixture()
                e2e = self._host_e2e(fixture)
                value = "sha256:" + "f" * 64 if field == "candidate_image_digest" else "f" * 64
                altered = self._rewrite_e2e_receipt(fixture, replace(e2e, **{field: value}))
                with self.assertRaises(ReleaseContractError):
                    self._aggregate(fixture, altered)


if __name__ == "__main__":
    unittest.main()
