"""Mock retained artifacts, validated by the real selector-independent readers."""
from __future__ import annotations

from dataclasses import asdict, replace
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = RELEASE_ROOT.parents[3]
for directory in (RELEASE_ROOT, Path(__file__).resolve().parent):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import release_e2e_gate as gate
from release_contract import ReleaseContractError, canonical_json
from release_e2e_golden.fixture import materialize
from release_handoff import CURRENT_SELECTOR_RELATIVE


class RetainedE2EArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        retained = PROJECT_ROOT / ".caprmedio_tmp/tests/release-e2e-retained"
        retained.mkdir(parents=True, exist_ok=True)
        cls.fixture = materialize(Path(tempfile.mkdtemp(prefix="golden-", dir=retained)))
        # Unit-only host boundary: retained-reader validation still reopens the
        # real N/package/Skill/source carriers, but must not discover or invoke
        # a host Docker executable in the socket-free Unit container.
        cls._mock_docker = cls.fixture.root / ".caprmedio_tmp/mock-docker"
        cls._mock_docker.parent.mkdir(parents=True, exist_ok=True)
        cls._mock_docker.write_bytes(b"#!/bin/false\n# MOCK DATA ONLY: never executed by this Unit fixture\n")
        cls._mock_docker.chmod(0o755)
        cls._host_boundary = patch.object(
            gate.HostE2EExecutor, "freeze_capability", side_effect=cls._unit_capability,
        )
        cls._host_boundary.start()
        try:
            cls.evidence = cls._seed_e2e(cls.fixture)
        except BaseException:
            cls._host_boundary.stop()
            raise

    @staticmethod
    def _unit_capability(root: Path, candidate) -> gate.FrozenHostE2ECapability:
        n_state = gate._active_n_state(root, candidate)
        n_root = root / gate.RUNTIME_ROOT / "releases" / candidate.authority.executing_release
        controller = gate._regular(n_root, gate._N_DRIVER_RELATIVE, label="fixture N host controller")
        python = Path(sys.executable).resolve()
        docker = root / ".caprmedio_tmp/mock-docker"
        if docker.is_symlink() or not docker.is_file():
            raise gate.ReleaseContractError("release-e2e-host-executable-missing", "fixture Docker carrier changed")

        def identity(role: str, path: Path) -> gate.ExecutableIdentity:
            return gate.ExecutableIdentity(role, str(path), gate._digest(path.read_bytes()))

        return gate.FrozenHostE2ECapability(
            *n_state,
            identity("n_host_controller", controller),
            identity("python", python),
            identity("driver", controller),
            identity("docker", docker),
            str(docker.parent),
        )

    @classmethod
    def tearDownClass(cls) -> None:
        boundary = getattr(cls, "_host_boundary", None)
        if boundary is not None:
            boundary.stop()

    @staticmethod
    def _seed_e2e(fixture):
        """Create explicit mock receipt bytes; no command or reader is replaced."""

        root, candidate = fixture.root, fixture.candidate
        capability = gate.HostE2EExecutor.freeze_capability(root, candidate)
        grammar, _, grammar_sha, _ = gate._load_grammar(root)
        phase_map = gate._bound_phase_map(candidate, grammar)
        attempt = root / gate.EVIDENCE_ROOT / candidate.manifest.sha256 / "attempt-mock-retained"
        reports = attempt / "scratch/reports"
        reports.mkdir(parents=True)
        relative = attempt.relative_to(root).as_posix()
        context, harnesses = gate._context_bytes(
            root, attempt / "scratch", reports, candidate, fixture.image, grammar_sha, phase_map.sha256, grammar,
        )
        (attempt / "scratch/context.json").write_bytes(context)
        settings = gate._release_e2e_settings(root, candidate)
        settings_path = f"{relative}/{gate._SETTINGS_SNAPSHOT_FILENAME}"
        (root / settings_path).write_bytes(settings.snapshot)
        capability_path = f"{relative}/host-identities.json"
        capability_bytes = gate._host_identities_bytes(capability)
        (root / capability_path).write_bytes(capability_bytes)
        (attempt / "inspect.stdout.bin").write_bytes((fixture.image.candidate_image_digest + "\n").encode())
        (attempt / "inspect.stderr.bin").write_bytes(b"")
        sources = {path: digest for path, digest, phase in phase_map.rows if phase == "candidate_e2e"}
        receipts = []
        for index, (row, harness) in enumerate(zip(grammar["harnesses"], harnesses, strict=True)):
            stdout, stderr = b"MOCK DATA ONLY: retained E2E artifact\n", b""
            junit = b"<testsuite tests='1' failures='0' errors='0' skipped='0'><testcase name='mock'/></testsuite>"
            stdout_path, stderr_path, junit_path = (
                f"{relative}/harness-{index}.{suffix}" for suffix in ("stdout.bin", "stderr.bin", "junit.xml")
            )
            for path, payload in ((stdout_path, stdout), (stderr_path, stderr), (junit_path, junit)):
                (root / path).write_bytes(payload)
            receipts.append(gate.HarnessReceipt(
                row["source_path"], sources[row["source_path"]],
                (capability.python.path, capability.n_host_controller.path, *row["argv"][2:7], harness["junit_path"]),
                "2026-10-06T00:00:00.000000Z", "2026-10-06T00:00:01.000000Z", 0, False,
                stdout_path, gate._digest(stdout), stderr_path, gate._digest(stderr),
                junit_path, gate._digest(junit), 1, 1.0, "",
            ))
        bare = gate.CandidateE2EGateEvidence(
            candidate.manifest.sha256, fixture.image.candidate_image_digest, phase_map.sha256, grammar_sha,
            "passed", "MOCK DATA ONLY: no E2E process invoked", tuple(receipts), relative, None,
            settings_path, settings.sha256, capability_path, gate._digest(capability_bytes), "host-subprocess",
        )
        receipt = canonical_json(asdict(bare))
        (attempt / "receipt.json").write_bytes(receipt)
        return replace(bare, receipt_sha256=gate._digest(receipt))

    def _read(self, *, fresh=False):
        fixture = self.fixture
        reader = gate.verify_bound_candidate_e2e_evidence if fresh else gate.read_candidate_e2e_execution_artifacts
        return reader(
            fixture.candidate, fixture.compilation, fixture.unit_suite, fixture.image, self.evidence,
            image_build=fixture.image_build,
        )

    def test_retained_reader_accepts_promotion_selection_while_fresh_admission_refuses(self) -> None:
        self.assertEqual(self.fixture.root, self._read(fresh=True))
        self.assertEqual(self.fixture.root, self._read())
        selector = self.fixture.root / CURRENT_SELECTOR_RELATIVE
        original = selector.read_bytes()
        try:
            selector.write_bytes(f'release = "{self.fixture.candidate.manifest.sha256}"\n'.encode())
            with self.assertRaises(ReleaseContractError):
                self._read(fresh=True)
            self.assertEqual(self.fixture.root, self._read())
        finally:
            selector.write_bytes(original)

    def test_retained_reader_refuses_changed_controller_context_and_actual_junit(self) -> None:
        capability = gate._reopen_host_capability(self.fixture.root, self.evidence)
        carriers = (
            Path(capability.n_host_controller.path),
            self.fixture.root / self.evidence.evidence_root / "scratch/context.json",
            self.fixture.root / self.evidence.harness_receipts[0].junit_path,
        )
        for carrier in carriers:
            with self.subTest(carrier=carrier.name):
                original = carrier.read_bytes()
                try:
                    carrier.write_bytes(original + b"changed retained bytes")
                    with self.assertRaises(ReleaseContractError):
                        self._read()
                finally:
                    carrier.write_bytes(original)
        self.assertEqual(self.fixture.root, self._read())


if __name__ == "__main__":
    unittest.main()
