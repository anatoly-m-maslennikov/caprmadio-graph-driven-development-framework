"""Private, receipt-bound aggregation of the completed Release gates.

This module makes no release selection, image build, host command, or
promotion effect.  It reopens the durable Unit, image, and candidate-E2E
receipts and retains a small aggregate receipt only after their test reports
form one exact, non-overlapping phase partition.
"""

from __future__ import annotations

import hashlib
import os
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, replace
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Literal

from release_contract import ReleaseContractError, ValidatedCandidate, canonical_json
from release_handoff import SealedCandidateCompilation
from release_suite import SuiteGateEvidence, verify_bound_suite_evidence
from release_test_phases import ReleaseTestPhaseMap, derive_test_phase_map, derive_test_phase_map_from_rows

if TYPE_CHECKING:
    from release_e2e_gate import CandidateE2EGateEvidence
    from release_image import ImageBuildEvidence, ImageVerificationEvidence


EVIDENCE_ROOT = ".caprmedio_runtime/release_full_gate"
_SHA256_LENGTH = 64
_MAX_REPORT_BYTES = 8 * 1024 * 1024


@dataclass(frozen=True)
class FullGateEvidence:
    candidate_snapshot_manifest_sha256: str
    candidate_image_digest: str
    phase_map_sha256: str
    suite_receipt_sha256: str
    build_receipt_sha256: str
    image_receipt_sha256: str
    e2e_receipt_sha256: str
    outcome: Literal["passed", "failed", "incomplete", "stale", "recording_uncertain"]
    reason: str
    evidence_root: str
    receipt_sha256: str | None
    executed_tests: int

    @property
    def passed(self) -> bool:
        return self.outcome == "passed" and self.receipt_sha256 is not None


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _error(code: str, message: str) -> ReleaseContractError:
    return ReleaseContractError(code, message)


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and len(value) == _SHA256_LENGTH and all(character in "0123456789abcdef" for character in value)


def _root(candidate: ValidatedCandidate) -> Path:
    root = Path(candidate.project_root).resolve()
    if root.is_symlink() or not root.is_dir():
        raise _error("release-full-gate-project-missing", "candidate Project root is unavailable")
    return root


def _path(root: Path, relative: str, *, label: str, create: bool = False) -> Path:
    parsed = PurePosixPath(relative)
    if (not relative or parsed.is_absolute() or parsed.as_posix() != relative
            or any(part in {"", ".", ".."} for part in parsed.parts)):
        raise _error("release-full-gate-path-unsafe", f"{label} is not a safe Project-relative path")
    target = root.joinpath(*parsed.parts)
    if create:
        target.mkdir(parents=True, exist_ok=True)
    if target.is_symlink() or (not create and not target.exists()):
        raise _error("release-full-gate-path-unsafe", f"{label} is absent or unsafe")
    try:
        target.resolve(strict=True).relative_to(root.resolve(strict=True))
    except ValueError as error:
        raise _error("release-full-gate-path-unsafe", f"{label} escapes the Project root") from error
    return target


def _write_new(path: Path, payload: bytes) -> None:
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())


def _phase_map(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation) -> ReleaseTestPhaseMap:
    """Use the shared package-row partition and require its inventory twin."""

    package_map = derive_test_phase_map_from_rows(compilation.package_rows)
    inventory_map = derive_test_phase_map(candidate)
    if package_map != inventory_map:
        raise _error("release-full-gate-phase-map-mismatch", "candidate inventory and compiled package rows have different phase maps")
    if not package_map.unit_paths or not package_map.candidate_e2e_paths:
        raise _error("release-full-gate-phase-map-invalid", "sealed phase map lacks a required Unit or candidate-E2E partition")
    return package_map


def _reopen_constituents(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation,
    suite: SuiteGateEvidence,
    build: ImageBuildEvidence,
    verification: ImageVerificationEvidence,
    e2e: CandidateE2EGateEvidence,
) -> Path:
    """Reopen every predecessor reader; no fields are trusted by themselves."""

    # Image retirement consumes this module through promotion.  These imports
    # are delayed until the concrete readers exist, keeping that cycle private.
    from release_e2e_gate import verify_bound_candidate_e2e_evidence
    from release_image import verify_bound_image_evidence

    root = _root(candidate)
    suite_root = verify_bound_suite_evidence(candidate, compilation, suite)
    verify_bound_image_evidence(candidate, compilation, suite, build, verification)
    e2e_root = verify_bound_candidate_e2e_evidence(
        candidate, compilation, suite, verification, e2e, image_build=build,
    )
    if suite_root != root or e2e_root != root:
        raise _error("release-full-gate-root-mismatch", "a reopened predecessor does not belong to the candidate Project")
    return root


def _constituent_receipts(
    candidate: ValidatedCandidate,
    suite: SuiteGateEvidence,
    build: ImageBuildEvidence,
    verification: ImageVerificationEvidence,
    e2e: CandidateE2EGateEvidence,
) -> tuple[str, str, str, str]:
    values = (suite.receipt_sha256, build.receipt_sha256, verification.receipt_sha256, e2e.receipt_sha256)
    if (not all(_is_sha256(value) for value in values)
            or build.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
            or verification.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
            or e2e.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
            or build.candidate_image_digest != verification.candidate_image_digest
            or verification.candidate_image_digest != e2e.candidate_image_digest):
        raise _error("release-full-gate-binding-mismatch", "constituent receipts do not share one candidate and immutable image")
    return values  # type: ignore[return-value]


def _reopen_retained_constituents(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation,
    suite: SuiteGateEvidence,
    build: ImageBuildEvidence,
    verification: ImageVerificationEvidence,
    e2e: CandidateE2EGateEvidence,
) -> Path:
    """Read original evidence after selection; later effects admit currentness."""

    from release_e2e_gate import read_candidate_e2e_execution_artifacts
    from release_image import read_image_execution_artifacts

    root = _root(candidate)
    image_attempt = read_image_execution_artifacts(candidate, compilation, suite, build, verification)
    e2e_root = read_candidate_e2e_execution_artifacts(
        candidate, compilation, suite, verification, e2e, image_build=build,
    )
    if image_attempt != _path(root, verification.evidence_root, label="retained image attempt") or e2e_root != root:
        raise _error("release-full-gate-root-mismatch", "a retained predecessor does not belong to the candidate Project")
    return root


def _read_xml(path: Path, *, label: str) -> ET.Element:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > _MAX_REPORT_BYTES:
        raise _error("release-full-gate-report-invalid", f"{label} report is missing, unsafe or too large")
    with path.open("rb") as stream:
        payload = stream.read(_MAX_REPORT_BYTES + 1)
    if len(payload) > _MAX_REPORT_BYTES or b"<!DOCTYPE" in payload.upper() or b"<!ENTITY" in payload.upper():
        raise _error("release-full-gate-report-invalid", f"{label} report is unsupported")
    try:
        report = ET.fromstring(payload)
    except ET.ParseError as error:
        raise _error("release-full-gate-report-invalid", f"{label} report is malformed") from error
    if report.tag not in {"testsuite", "testsuites"}:
        raise _error("release-full-gate-report-invalid", f"{label} report has an unsupported root")
    return report


def _report_cases(report: ET.Element, *, label: str) -> tuple[tuple[str, str], ...]:
    cases = list(report.iter("testcase"))
    if not cases:
        raise _error("release-full-gate-report-invalid", f"{label} report has no executed testcases")
    identities: list[tuple[str, str]] = []
    for case in cases:
        classname, name = case.get("classname"), case.get("name")
        if (not isinstance(classname, str) or not classname or not isinstance(name, str) or not name
                or list(case.iter("failure")) or list(case.iter("error")) or list(case.iter("skipped"))):
            raise _error("release-full-gate-report-invalid", f"{label} report has an ambiguous or non-passing testcase")
        identities.append((classname, name))
    if len(identities) != len(set(identities)):
        raise _error("release-full-gate-report-invalid", f"{label} report has duplicate testcase identities")
    for suite in (node for node in report.iter() if node.tag in {"testsuite", "testsuites"}):
        actual = len(list(suite.iter("testcase")))
        for key, expected in (("tests", actual), ("failures", 0), ("errors", 0), ("skipped", 0)):
            if key in suite.attrib:
                try:
                    if int(suite.attrib[key]) != expected:
                        raise _error("release-full-gate-report-invalid", f"{label} report summary is inconsistent")
                except ValueError as error:
                    raise _error("release-full-gate-report-invalid", f"{label} report summary is invalid") from error
    return tuple(identities)


def _observe_partition(
    root: Path,
    suite: SuiteGateEvidence,
    e2e: CandidateE2EGateEvidence,
    phase_map: ReleaseTestPhaseMap,
) -> int:
    """Require one complete Unit/E2E test partition with globally unique cases."""

    if suite.phase_map_sha256 != phase_map.sha256:
        raise _error("release-full-gate-phase-map-mismatch", "Unit receipt does not bind the sealed phase map")
    suite_report = _read_xml(
        _path(root, f"{suite.evidence_root}/coverage.xml", label="retained Unit"), label="Unit",
    )
    if (suite_report.get("caprmedio.phase") != "unit"
            or suite_report.get("caprmedio.phase_map_sha256") != phase_map.sha256):
        raise _error("release-full-gate-phase-map-mismatch", "Unit report does not bind the exact Unit phase map")
    unit_cases = _report_cases(suite_report, label="Unit")
    if {classname for classname, _name in unit_cases} != set(phase_map.unit_paths):
        raise _error("release-full-gate-partition-invalid", "Unit report does not cover the exact declared Unit modules")
    if suite.executed_tests != len(unit_cases):
        raise _error("release-full-gate-report-invalid", "Unit receipt testcase count does not match its retained report")

    expected_e2e_paths = phase_map.candidate_e2e_paths
    if (len(e2e.harness_receipts) != len(expected_e2e_paths)
            or tuple(sorted(row.source_path for row in e2e.harness_receipts)) != expected_e2e_paths):
        raise _error("release-full-gate-partition-invalid", "candidate E2E receipt does not cover the exact declared E2E modules")
    identities = set(unit_cases)
    total = len(unit_cases)
    for row in e2e.harness_receipts:
        report = _read_xml(_path(root, row.junit_path, label="retained candidate E2E"), label="candidate E2E")
        observed = _report_cases(report, label="candidate E2E")
        module_name = PurePosixPath(row.source_path).stem
        if any(classname != module_name and not classname.startswith(module_name + ".")
               for classname, _name in observed):
            raise _error("release-full-gate-partition-invalid", "candidate E2E report does not cover its declared E2E module")
        if row.executed_tests != len(observed):
            raise _error("release-full-gate-report-invalid", "candidate E2E receipt testcase count does not match its retained report")
        if identities.intersection(observed):
            raise _error("release-full-gate-partition-invalid", "Unit and candidate E2E reports share a testcase identity")
        identities.update(observed)
        total += len(observed)
    return total


def aggregate_bound_release_gates(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation,
    suite: SuiteGateEvidence,
    build: ImageBuildEvidence,
    verification: ImageVerificationEvidence,
    e2e: CandidateE2EGateEvidence,
) -> FullGateEvidence:
    """Retain a read-only aggregate only after all bound gates and reports agree."""

    root = _reopen_constituents(candidate, compilation, suite, build, verification, e2e)
    phase_map = _phase_map(candidate, compilation)
    suite_receipt, build_receipt, image_receipt, e2e_receipt = _constituent_receipts(
        candidate, suite, build, verification, e2e,
    )
    parent = _path(root, f"{EVIDENCE_ROOT}/{candidate.manifest.sha256}", label="full-gate evidence", create=True)
    attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=parent))
    evidence_root = attempt.relative_to(root).as_posix()
    outcome: Literal["passed", "failed", "incomplete", "stale", "recording_uncertain"] = "failed"
    reason = "aggregate reports are incomplete"
    executed_tests = 0
    try:
        executed_tests = _observe_partition(root, suite, e2e, phase_map)
        outcome, reason = "passed", "all bound Unit and candidate E2E reports form one complete partition"
    except ReleaseContractError as error:
        outcome, reason = "failed", str(error)
    evidence = FullGateEvidence(
        candidate.manifest.sha256, verification.candidate_image_digest, phase_map.sha256,
        suite_receipt, build_receipt, image_receipt, e2e_receipt,
        outcome, reason, evidence_root, None, executed_tests,
    )
    try:
        receipt = canonical_json(asdict(evidence))
        _write_new(attempt / "receipt.json", receipt)
        descriptor = os.open(attempt, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        return replace(evidence, receipt_sha256=_digest(receipt))
    except OSError:
        return replace(evidence, outcome="recording_uncertain", reason="full-gate aggregate receipt could not be durably recorded")


def verify_bound_full_gate_evidence(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation,
    suite: SuiteGateEvidence,
    build: ImageBuildEvidence,
    verification: ImageVerificationEvidence,
    e2e: CandidateE2EGateEvidence,
    evidence: FullGateEvidence,
) -> Path:
    """Read exact original aggregate artifacts independently of active selection.

    This byte reader does not admit a new effect.  Promotion and recovery must
    separately establish their intent, current source/package and selection.
    """

    root = _reopen_retained_constituents(candidate, compilation, suite, build, verification, e2e)
    if not isinstance(evidence, FullGateEvidence) or not evidence.passed:
        raise _error("release-full-gate-evidence-untrusted", "later admission requires passed aggregate gate evidence")
    phase_map = _phase_map(candidate, compilation)
    suite_receipt, build_receipt, image_receipt, e2e_receipt = _constituent_receipts(
        candidate, suite, build, verification, e2e,
    )
    prefix = f"{EVIDENCE_ROOT}/{candidate.manifest.sha256}/"
    if (evidence.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
            or evidence.candidate_image_digest != verification.candidate_image_digest
            or evidence.phase_map_sha256 != phase_map.sha256
            or (evidence.suite_receipt_sha256, evidence.build_receipt_sha256,
                evidence.image_receipt_sha256, evidence.e2e_receipt_sha256)
            != (suite_receipt, build_receipt, image_receipt, e2e_receipt)
            or not _is_sha256(evidence.receipt_sha256)
            or not evidence.evidence_root.startswith(prefix)
            or not evidence.evidence_root.removeprefix(prefix).startswith("attempt-")
            or "/" in evidence.evidence_root.removeprefix(prefix)):
        raise _error("release-full-gate-evidence-mismatch", "aggregate evidence does not belong to the exact bound candidate")
    receipt = _path(root, f"{evidence.evidence_root}/receipt.json", label="full-gate receipt")
    receipt_bytes = receipt.read_bytes()
    if (_digest(receipt_bytes) != evidence.receipt_sha256
            or receipt_bytes != canonical_json(asdict(replace(evidence, receipt_sha256=None)))):
        raise _error("release-full-gate-evidence-untrusted", "full-gate aggregate receipt changed or is caller-forged")
    if _observe_partition(root, suite, e2e, phase_map) != evidence.executed_tests:
        raise _error("release-full-gate-evidence-untrusted", "aggregate executed testcase count changed")
    return root


__all__ = [
    "FullGateEvidence",
    "aggregate_bound_release_gates",
    "verify_bound_full_gate_evidence",
]
