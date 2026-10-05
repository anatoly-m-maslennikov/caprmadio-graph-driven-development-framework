"""Execute the sealed full-suite command and retain truthful, non-promoting evidence.

The ``local-subprocess`` runner supports JUnit XML written by the command to
``CAPRMEDIO_RELEASE_SUITE_REPORT``. Each executed testcase must have one or more
``caprmedio.covered_source`` properties naming locally sealed source paths.
Coverage must include Methodology, Tools, Apps, MCP, Agentic and the ca Skill.
Other report formats, skipped tests and absent coverage remain incomplete.
"""

from __future__ import annotations

import hashlib
import os
import signal
import subprocess
import tempfile
import time
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Literal

from release_contract import ReleaseContractError, ValidatedCandidate, canonical_json
from release_handoff import CURRENT_SELECTOR_RELATIVE, SealedCandidateCompilation, _revalidate
from release_packaging import (
    RUNTIME_ROOT, ReleasePackagingError, _complete_rows, _render_manifest, _verify_release,
)


EVIDENCE_ROOT = ".caprmedio_runtime/release_suite"
REPORT_ENVIRONMENT_VARIABLE = "CAPRMEDIO_RELEASE_SUITE_REPORT"
SUPPORTED_RUNNER = "local-subprocess"
REQUIRED_COVERAGE = frozenset({"Methodology", "Tools", "Apps", "MCP", "Agentic", "Skill"})
MAX_REPORT_BYTES = 4 * 1024 * 1024
SHELLS = frozenset({"sh", "bash", "dash", "zsh", "fish", "ksh", "cmd", "cmd.exe", "powershell", "pwsh"})


@dataclass(frozen=True)
class SuiteGateEvidence:
    candidate_snapshot_manifest_sha256: str
    outcome: Literal["passed", "failed", "timed_out", "incomplete", "stale", "recording_uncertain"]
    reason: str
    runner: str
    command: tuple[str, ...]
    working_directory: str
    exit_code: int | None
    executed_tests: int
    coverage: tuple[str, ...]
    evidence_root: str
    stdout_sha256: str | None
    stderr_sha256: str | None
    report_sha256: str | None
    receipt_sha256: str | None
    elapsed_seconds: float

    @property
    def passed(self) -> bool:
        """A computed gate result, never an accepted caller success flag."""
        return self.outcome == "passed" and self.receipt_sha256 is not None


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _safe_path(root: Path, relative: str, *, create: bool = False) -> Path:
    path = Path(relative)
    if path.is_absolute() or relative != path.as_posix() or ".." in path.parts:
        raise ReleaseContractError("release-suite-path-unsafe", "suite path must be normalized within the Project")
    cursor = root
    for part in path.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ReleaseContractError("release-suite-path-unsafe", "suite path contains a symlink")
        if cursor.exists() and not cursor.is_dir():
            raise ReleaseContractError("release-suite-path-unsafe", "suite path has a non-directory component")
        if create and not cursor.exists():
            cursor.mkdir()
    if not cursor.is_dir():
        raise ReleaseContractError("release-suite-working-directory-missing", "sealed working directory is absent")
    return cursor


def _validate_bound_inputs(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation) -> Path:
    if not isinstance(candidate, ValidatedCandidate) or not isinstance(compilation, SealedCandidateCompilation):
        raise ReleaseContractError("release-suite-handoff-untrusted", "suite requires internal typed candidate and compilation")
    current = _revalidate(candidate)
    # model_copy can bypass validation: reparse every mutable nested model.
    sealed = SealedCandidateCompilation.model_validate(compilation.model_dump(mode="json"))
    if sealed.authority != current.authority or sealed.candidate_snapshot_manifest_sha256 != current.manifest.sha256:
        raise ReleaseContractError("release-suite-binding-mismatch", "compilation belongs to a different sealed candidate")
    if (sealed.expected_derived_source_copy_sha256 != current.manifest.expected_derived_source_copy_sha256
            or sealed.expected_compiled_output_sha256 != current.manifest.expected_compiled_output_sha256):
        raise ReleaseContractError("release-suite-binding-mismatch", "compiler expectations differ from the candidate")
    root = Path(current.project_root)
    identity, rows, _selector = _complete_rows(root, sealed)
    package = _safe_path(root, (RUNTIME_ROOT / "releases" / identity).as_posix())
    _verify_release(package, _render_manifest(identity, rows), rows)
    return root


def _coverage_group(destination: str) -> str | None:
    prefixes = {
        "METHODOLOGY/": "Methodology",
        "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/": "Tools",
        "FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/": "Apps",
        "FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/": "MCP",
        "FRAMEWORK_ENGINE/202_AGENTIC/": "Agentic",
        "SKILLS/ca/": "Skill",
    }
    return next((group for prefix, group in prefixes.items() if destination.startswith(prefix)), None)


def _observe_report(path: Path, compilation: SealedCandidateCompilation) -> tuple[int, tuple[str, ...], str]:
    """Extract actual execution counts and bound coverage; no caller pass field."""
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_REPORT_BYTES:
        return 0, (), "coverage report missing, unsafe or too large"
    payload = path.read_bytes()
    if b"<!DOCTYPE" in payload.upper() or b"<!ENTITY" in payload.upper():
        return 0, (), "unsupported coverage report declarations"
    try:
        report = ET.fromstring(payload)
    except ET.ParseError:
        return 0, (), "unsupported coverage report format"
    if report.tag not in {"testsuite", "testsuites"}:
        return 0, (), "unsupported coverage report format"
    cases = list(report.iter("testcase"))
    if not cases:
        return 0, (), "coverage report has no executed testcases"
    sources = {row.source_path: _coverage_group(row.destination_path) for row in compilation.package_rows}
    covered: set[str] = set()
    for case in cases:
        if list(case.iter("failure")) or list(case.iter("error")):
            return len(cases), tuple(sorted(covered)), "coverage report contains failed testcases"
        if list(case.iter("skipped")):
            return len(cases), tuple(sorted(covered)), "coverage report contains skipped testcases"
        properties = [item.get("value") for item in case.findall("./properties/property")
                      if item.get("name") == "caprmedio.covered_source"]
        if not properties or any(source not in sources for source in properties):
            return len(cases), tuple(sorted(covered)), "testcase lacks locally bound source coverage"
        covered.update(sources[source] for source in properties if sources[source] is not None)
    for suite in (item for item in report.iter() if item.tag in {"testsuite", "testsuites"}):
        actual = len(list(suite.iter("testcase")))
        for key, observed in (("tests", actual), ("failures", 0), ("errors", 0), ("skipped", 0)):
            if key in suite.attrib:
                try:
                    if int(suite.attrib[key]) != observed:
                        return len(cases), tuple(sorted(covered)), "coverage report summary is inconsistent"
                except ValueError:
                    return len(cases), tuple(sorted(covered)), "coverage report summary is invalid"
    if covered != REQUIRED_COVERAGE:
        return len(cases), tuple(sorted(covered)), "full suite coverage is incomplete"
    return len(cases), tuple(sorted(covered)), ""


def _durable_bytes(path: Path, payload: bytes) -> None:
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())


def execute_bound_release_suite(
    candidate: ValidatedCandidate, compilation: SealedCandidateCompilation, *, timeout_seconds: float = 900,
) -> SuiteGateEvidence:
    """Run exact sealed argv once; keep N and return no promotion authority.

    Invalid admission raises before execution. Once execution is attempted all
    process, coverage, currentness and recording failures return non-pass evidence.
    Evidence is retained at a fixed, unique Project-relative attempt directory.
    """
    if not isinstance(timeout_seconds, (int, float)) or isinstance(timeout_seconds, bool) or not 0 < timeout_seconds <= 900:
        raise ReleaseContractError("release-suite-timeout-invalid", "suite timeout must be within (0, 900] seconds")
    root = _validate_bound_inputs(candidate, compilation)
    environment = candidate.manifest.full_suite_environment
    if environment.runner != SUPPORTED_RUNNER:
        raise ReleaseContractError("release-suite-runner-unsupported", "sealed suite runner is unsupported")
    if os.name != "posix":
        raise ReleaseContractError("release-suite-runner-unsupported", "runner requires POSIX process-group timeout cleanup")
    if Path(environment.command[0]).name.lower() in SHELLS:
        raise ReleaseContractError("release-suite-shell-unsupported", "suite runner does not admit shell interpreters")
    cwd = _safe_path(root, environment.working_directory)
    selector_before = (root / CURRENT_SELECTOR_RELATIVE).read_bytes()
    parent = _safe_path(root, f"{EVIDENCE_ROOT}/{candidate.manifest.sha256}", create=True)
    attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=parent))
    relative = attempt.relative_to(root).as_posix()
    report_path = attempt / "coverage.xml"
    process_environment = dict(os.environ)
    process_environment[REPORT_ENVIRONMENT_VARIABLE] = str(report_path)
    started = time.monotonic()
    outcome, reason, exit_code = "incomplete", "suite command did not complete", None
    tests, coverage = 0, ()
    stdout_sha = stderr_sha = report_sha = receipt_sha = None
    evidence: SuiteGateEvidence | None = None
    try:
        with (attempt / "stdout.bin").open("xb") as stdout, (attempt / "stderr.bin").open("xb") as stderr:
            try:
                process = subprocess.Popen(tuple(environment.command), cwd=cwd, env=process_environment,
                                           stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                           shell=False, start_new_session=True)
                try:
                    exit_code = process.wait(timeout=timeout_seconds)
                    outcome = "failed" if exit_code else "incomplete"
                    reason = "suite command failed" if exit_code else "coverage evidence is incomplete"
                except subprocess.TimeoutExpired:
                    # Stop the whole invocation, including report-writing descendants.
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    exit_code = process.wait()
                    outcome, reason = "timed_out", "suite command timed out"
                else:
                    try:
                        os.killpg(process.pid, 0)
                    except ProcessLookupError:
                        pass
                    else:
                        os.killpg(process.pid, signal.SIGKILL)
                        outcome, reason = "incomplete", "suite left running descendant processes"
            except OSError as error:
                outcome, reason = "failed", f"suite process could not start: {type(error).__name__}"
            for stream in (stdout, stderr):
                stream.flush()
                os.fsync(stream.fileno())
        _safe_path(root, relative)
        for output in (attempt / "stdout.bin", attempt / "stderr.bin"):
            if output.is_symlink() or not output.is_file():
                raise OSError("captured suite output carrier is unsafe")
        stdout_sha = _digest((attempt / "stdout.bin").read_bytes())
        stderr_sha = _digest((attempt / "stderr.bin").read_bytes())
        if report_path.is_file() and not report_path.is_symlink() and report_path.stat().st_size <= MAX_REPORT_BYTES:
            report_sha = _digest(report_path.read_bytes())
            with report_path.open("rb") as report_stream:
                os.fsync(report_stream.fileno())
        tests, coverage, coverage_reason = _observe_report(report_path, compilation)
        if exit_code == 0 and reason != "suite left running descendant processes":
            outcome, reason = ("incomplete", coverage_reason) if coverage_reason else ("passed", "complete bound suite execution")
        try:
            _validate_bound_inputs(candidate, compilation)
            if (root / CURRENT_SELECTOR_RELATIVE).read_bytes() != selector_before:
                raise ReleaseContractError("release-currentness-stale", "executing N selector bytes changed during suite")
            if _safe_path(root, environment.working_directory) != cwd:
                raise ReleaseContractError("release-currentness-stale", "suite working directory changed")
        except (ReleaseContractError, ReleasePackagingError, OSError, ValueError) as error:
            outcome, reason = "stale", f"post-suite bindings no longer validate: {getattr(error, 'code', type(error).__name__)}"
        evidence = SuiteGateEvidence(candidate.manifest.sha256, outcome, reason, environment.runner,
                                     tuple(environment.command), environment.working_directory, exit_code,
                                     tests, coverage, relative, stdout_sha, stderr_sha, report_sha, None,
                                     time.monotonic() - started)
        receipt = canonical_json(asdict(evidence))
        _durable_bytes(attempt / "receipt.json", receipt)
        directory_descriptor = os.open(attempt, os.O_RDONLY)
        try:
            os.fsync(directory_descriptor)
        finally:
            os.close(directory_descriptor)
        receipt_sha = _digest(receipt)
    except (OSError, ValueError) as error:
        outcome, reason = "recording_uncertain", f"suite evidence could not be durably recorded: {type(error).__name__}"
    if evidence is not None:
        return replace(evidence, outcome=outcome, reason=reason, receipt_sha256=receipt_sha)
    return SuiteGateEvidence(candidate.manifest.sha256, outcome, reason, environment.runner,
                             tuple(environment.command), environment.working_directory, exit_code,
                             tests, coverage, relative, stdout_sha, stderr_sha, report_sha, receipt_sha,
                             time.monotonic() - started)


def verify_bound_suite_evidence(
    candidate: ValidatedCandidate, compilation: SealedCandidateCompilation, evidence: SuiteGateEvidence,
) -> Path:
    """Reopen durable successful evidence before any later effect admission."""
    root = _validate_bound_inputs(candidate, compilation)
    if not isinstance(evidence, SuiteGateEvidence) or not evidence.passed:
        raise ReleaseContractError("release-suite-evidence-untrusted", "later admission requires actual successful typed suite evidence")
    environment = candidate.manifest.full_suite_environment
    prefix = f"{EVIDENCE_ROOT}/{candidate.manifest.sha256}/"
    if (evidence.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
            or evidence.runner != environment.runner or evidence.command != tuple(environment.command)
            or evidence.working_directory != environment.working_directory or evidence.exit_code != 0
            or not evidence.evidence_root.startswith(prefix)
            or not evidence.evidence_root[len(prefix):].startswith("attempt-")
            or "/" in evidence.evidence_root[len(prefix):]):
        raise ReleaseContractError("release-suite-evidence-mismatch", "suite receipt is outside the exact sealed invocation")
    _safe_path(root, environment.working_directory)
    attempt = _safe_path(root, evidence.evidence_root)
    try:
        files = {}
        for name in ("receipt.json", "stdout.bin", "stderr.bin", "coverage.xml"):
            path = attempt / name
            if path.is_symlink() or not path.is_file():
                raise ValueError("durable suite carrier is missing or unsafe")
            files[name] = path.read_bytes()
        if (_digest(files["receipt.json"]) != evidence.receipt_sha256
                or files["receipt.json"] != canonical_json(asdict(replace(evidence, receipt_sha256=None)))
                or _digest(files["stdout.bin"]) != evidence.stdout_sha256
                or _digest(files["stderr.bin"]) != evidence.stderr_sha256
                or _digest(files["coverage.xml"]) != evidence.report_sha256):
            raise ValueError("durable suite bytes differ from the typed receipt")
        tests, coverage, reason = _observe_report(attempt / "coverage.xml", compilation)
        if reason or tests != evidence.executed_tests or coverage != evidence.coverage:
            raise ValueError("actual suite report no longer establishes complete successful coverage")
    except (OSError, ValueError) as error:
        raise ReleaseContractError("release-suite-evidence-mismatch", "successful suite evidence is missing, changed or incomplete") from error
    return root


__all__ = ["SuiteGateEvidence", "execute_bound_release_suite", "verify_bound_suite_evidence", "SUPPORTED_RUNNER", "REPORT_ENVIRONMENT_VARIABLE"]
