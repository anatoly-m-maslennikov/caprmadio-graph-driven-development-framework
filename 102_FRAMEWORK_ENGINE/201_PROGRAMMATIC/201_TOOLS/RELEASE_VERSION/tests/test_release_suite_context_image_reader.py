"""Golden retained-suite-context checks for the post-promotion image reader."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from dataclasses import asdict, replace
from pathlib import Path
from types import SimpleNamespace


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_contract import ReleaseContractError, canonical_json
from release_image import _read_suite_artifacts
from release_suite import SUPPORTED_RUNNER, SuiteGateEvidence


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


class RetainedSuiteContextImageReaderTests(unittest.TestCase):
    """These use only durable receipt bytes; no current selector is materialized."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve(strict=True)
        self.candidate_digest = "a" * 64
        self.context_bindings = {
            "candidate_snapshot_manifest_sha256": self.candidate_digest,
            "compiled_candidate_root": ".caprmedio_caprmedio/compiled/candidate",
            "selected_n_identity": "N",
            "selected_n_image_context": "b" * 64,
        }
        self.context_rows = [{
            "source_path": ".caprmedio_caprmedio/operators_registry.toml",
            "sha256": "c" * 64,
            "mode": 0o644,
        }]
        preimage = {
            "schema_version": 1,
            **self.context_bindings,
            "reference_rows": self.context_rows,
        }
        self.context = {**preimage, "control_context_digest": _sha256(canonical_json(preimage))}
        self.candidate = SimpleNamespace(
            project_root=str(self.root),
            manifest=SimpleNamespace(
                sha256=self.candidate_digest,
                full_suite_environment=SimpleNamespace(
                    runner=SUPPORTED_RUNNER,
                    command=["python", "suite.py"],
                    working_directory="suite",
                ),
            ),
            authority=SimpleNamespace(executing_release="N"),
        )
        self.compilation = SimpleNamespace(child_materialization_root=self.context_bindings["compiled_candidate_root"])
        self.attempt_relative = f".caprmedio_runtime/release_suite/{self.candidate_digest}/attempt-golden"
        self.attempt = self.root / self.attempt_relative
        self.attempt.mkdir(parents=True)
        self.stdout = b"suite stdout\n"
        self.stderr = b"suite stderr\n"
        self.report = b"<testsuites/>\n"
        self._write_evidence()

    def _write_evidence(self) -> None:
        (self.attempt / "context.json").write_bytes(canonical_json(self.context))
        (self.attempt / "stdout.bin").write_bytes(self.stdout)
        (self.attempt / "stderr.bin").write_bytes(self.stderr)
        (self.attempt / "coverage.xml").write_bytes(self.report)
        provisional = SuiteGateEvidence(
            self.candidate_digest, "passed", "", SUPPORTED_RUNNER, ("python", "suite.py"), "suite", 0,
            1, ("Tools",), self.attempt_relative, _sha256(self.stdout), _sha256(self.stderr), _sha256(self.report),
            "d" * 64, "e" * 64, "f" * 64, None, 0.01, self.context["control_context_digest"],
        )
        receipt = canonical_json(asdict(provisional))
        self.suite = replace(provisional, receipt_sha256=_sha256(receipt))
        (self.attempt / "receipt.json").write_bytes(receipt)

    def test_accepts_exact_retained_context_without_current_selection(self) -> None:
        retained = _read_suite_artifacts(self.root, self.candidate, self.compilation, self.suite)

        self.assertEqual(retained.root, str(self.root))
        self.assertEqual(retained.trusted_binding_values, tuple(sorted(self.context_bindings.items())))
        self.assertEqual(retained.control_context_digest, self.context["control_context_digest"])

    def test_rejects_changed_retained_context_digest(self) -> None:
        self.context["control_context_digest"] = "0" * 64
        (self.attempt / "context.json").write_bytes(canonical_json(self.context))

        with self.assertRaises(ReleaseContractError):
            _read_suite_artifacts(self.root, self.candidate, self.compilation, self.suite)

    def test_rejects_changed_retained_context_probe(self) -> None:
        self.context["reference_rows"][0]["sha256"] = "0" * 64
        self.context["control_context_digest"] = _sha256(canonical_json({
            "schema_version": 1,
            **self.context_bindings,
            "reference_rows": self.context["reference_rows"],
        }))
        (self.attempt / "context.json").write_bytes(canonical_json(self.context))

        with self.assertRaises(ReleaseContractError):
            _read_suite_artifacts(self.root, self.candidate, self.compilation, self.suite)


if __name__ == "__main__":
    unittest.main()
