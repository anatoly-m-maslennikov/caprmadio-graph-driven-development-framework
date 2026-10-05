"""Execute the sealed full-suite command and retain truthful, non-promoting evidence.

The ``local-subprocess`` runner names the sealed command contract, not a
permission to execute it in the Project process.  An approved isolated
executor writes JUnit XML to ``CAPRMEDIO_RELEASE_SUITE_REPORT``. Each executed
testcase must have one or more ``caprmedio.covered_source`` properties naming
locally sealed source paths.
Coverage must include Methodology, Tools, Apps, MCP, Agentic and the ca Skill.
Other report formats, skipped tests and absent coverage remain incomplete.
The suite accepts the exact sealed source/compiled candidate before candidate
package staging. An already prepared candidate package is verified strictly;
its absence never implies installation or causes package or Skill creation.
The already selected N package and public Skill, however, must be complete and
remain unchanged throughout every later gate.
"""

from __future__ import annotations

import hashlib
import os
import re
import signal
import subprocess
import tempfile
import time
import tomllib
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Literal, Protocol

from release_contract import (
    PROJECT_SKILL_TARGET, REQUIRED_ENGINE_SOURCE_PREFIXES, ReleaseContractError,
    ValidatedCandidate, canonical_json,
)
from release_handoff import (
    CURRENT_SELECTOR_RELATIVE, PackageRow, SealedCandidateCompilation, _revalidate,
    tree_sha256,
)
from release_inventory import ReleaseInventoryError, refuse_secret_path
from release_packaging import (
    REQUIRED_SKILL_FILES, RUNTIME_ROOT, ReleasePackagingError, _complete_rows,
    _render_manifest, _verify_release,
)


EVIDENCE_ROOT = ".caprmedio_runtime/release_suite"
REPORT_ENVIRONMENT_VARIABLE = "CAPRMEDIO_RELEASE_SUITE_REPORT"
PROJECT_ROOT_ENVIRONMENT_VARIABLE = "CAPRMEDIO_RELEASE_PROJECT_ROOT"
COMPILED_ROOT_ENVIRONMENT_VARIABLE = "CAPRMEDIO_RELEASE_COMPILED_CANDIDATE_ROOT"
CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE = "CAPRMEDIO_RELEASE_CANDIDATE_MANIFEST_SHA256"
SUPPORTED_RUNNER = "local-subprocess"
REQUIRED_COVERAGE = frozenset({"Methodology", "Tools", "Apps", "MCP", "Agentic", "Skill"})
MAX_REPORT_BYTES = 4 * 1024 * 1024
SHELLS = frozenset({"sh", "bash", "dash", "zsh", "fish", "ksh", "cmd", "cmd.exe", "powershell", "pwsh"})
SANDBOX_WORKSPACE_PATH = Path("/workspace")
SANDBOX_OUTPUT_PATH = Path("/output")


@dataclass(frozen=True)
class SuiteExecutionResult:
    """Observed result returned by an already approved isolation boundary.

    This is deliberately smaller than ``SuiteGateEvidence``: an executor can
    report process facts, but it cannot select a candidate, claim coverage, or
    declare the Release gate passed.
    """

    exit_code: int | None
    stdout: bytes
    stderr: bytes
    timed_out: bool = False
    left_descendants: bool = False


class SuiteSandboxExecutor(Protocol):
    """Run a sealed suite outside the authoritative Project filesystem.

    A production implementation must make ``workspace`` the only source
    mount (read-only), make ``output_root`` the only writable host mount, and
    not inherit host credentials or undeclared mounts.  ``environment`` uses
    the fixed in-sandbox ``/workspace`` and ``/output`` paths; it must not be
    rewritten to authority-carrier paths.  The caller retains all admission,
    coverage, and currentness decisions.
    """

    def run(
        self,
        command: tuple[str, ...],
        *,
        workspace: Path,
        output_root: Path,
        working_directory: str,
        environment: dict[str, str],
        timeout_seconds: float,
    ) -> SuiteExecutionResult:
        """Execute the exact sealed argv in an isolated boundary."""


# A Release cannot fall back to a host subprocess.  Engine wiring must inject
# an installed-N immutable-image executor or another governed sandbox.  Tests
# may temporarily install a fixture executor through this private seam.
_DEFAULT_EXECUTOR: SuiteSandboxExecutor | None = None


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
    executing_selector_sha256: str
    executing_release_package_sha256: str
    executing_skill_sha256: str
    receipt_sha256: str | None
    elapsed_seconds: float

    @property
    def passed(self) -> bool:
        """A computed gate result, never an accepted caller success flag."""
        return self.outcome == "passed" and self.receipt_sha256 is not None


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


_IMAGE_ID = re.compile(r"^sha256:[0-9a-f]{64}$")
_SOURCE_CONTEXT = re.compile(r"^[0-9a-f]{64}$")


def _bootstrap_source_context_is_valid(value: object) -> bool:
    return isinstance(value, str) and _SOURCE_CONTEXT.fullmatch(value) is not None


def _bootstrap_prior_manifest_is_exact(prior_selector: dict, manifest_bytes: bytes,
                                       executing_release: str) -> bool:
    """Prove the closed O180 bootstrap selector/package address pair."""
    expected_root = f"{RUNTIME_ROOT.as_posix()}/releases/{executing_release}"
    expected = {
        "schema_version": 1,
        "manifest_sha256": executing_release,
        "release": executing_release,
        "selected_release_root": expected_root,
        "framework_engine_root": expected_root + "/FRAMEWORK_ENGINE",
        "methodology_root": expected_root + "/METHODOLOGY",
    }
    return (
        set(prior_selector) == {*expected, "image_digest"}
        and type(prior_selector.get("schema_version")) is int
        and all(prior_selector.get(key) == value for key, value in expected.items())
        and isinstance(prior_selector.get("image_digest"), str)
        and _IMAGE_ID.fullmatch(prior_selector["image_digest"]) is not None
        and _digest(manifest_bytes) == executing_release
    )


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


def _refuse_secret_relative(relative: str | Path) -> None:
    """Refuse a secret-shaped carrier before any caller reads its bytes."""

    try:
        refuse_secret_path(relative)
    except ReleaseInventoryError as error:
        raise ReleaseContractError(error.code, str(error)) from error


def _suite_process_environment(
    root: Path,
    report_path: Path,
    compilation: SealedCandidateCompilation,
    candidate: ValidatedCandidate,
    *,
    executable_path: str = os.defpath,
) -> dict[str, str]:
    """Return the complete, minimal environment for one sealed suite process.

    The runner never inherits an interactive shell environment.  In
    particular, credentials, authentication homes, user homes and ambient
    configuration cannot enter the test command. ``executable_path`` is a
    trusted executor capability: absent an installed-image executor, explicit
    fixture executors use the platform's static default.
    """

    if (not isinstance(executable_path, str) or not executable_path
            or "\x00" in executable_path or "\n" in executable_path or "\r" in executable_path):
        raise ReleaseContractError("release-suite-executor-untrusted", "suite executor has no safe declared PATH")

    return {
        "PATH": executable_path,
        PROJECT_ROOT_ENVIRONMENT_VARIABLE: str(root),
        REPORT_ENVIRONMENT_VARIABLE: str(report_path),
        COMPILED_ROOT_ENVIRONMENT_VARIABLE: compilation.child_materialization_root,
        CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE: candidate.manifest.sha256,
    }


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
    # O174 tests precede O175 staging. E572 permits prior preparation but does
    # not require it: validate existing parents and any existing exact package
    # without creating directories or substituting staging for the suite.
    package = root
    for part in (RUNTIME_ROOT / "releases" / identity).parts:
        package = package / part
        if package.is_symlink() or (package.exists() and not package.is_dir()):
            raise ReleaseContractError("release-suite-path-unsafe", "optional retained package has an unsafe parent or root")
    if package.exists():
        _verify_release(package, _render_manifest(identity, rows), rows)
    return root


def _active_skill_records(root: Path, relative: str) -> tuple[dict[str, tuple[str, int]], set[str]]:
    """Read one complete non-symlink Skill carrier, including file modes."""

    folder = _safe_path(root, relative)
    files: dict[str, tuple[str, int]] = {}
    directories: set[str] = set()
    for carrier in sorted(folder.rglob("*")):
        local = carrier.relative_to(folder).as_posix()
        _refuse_secret_relative(Path(relative) / local)
        if carrier.is_symlink() or not (carrier.is_dir() or carrier.is_file()):
            raise ReleaseContractError("release-active-n-invalid", f"active Skill contains an unsafe carrier: {local}")
        if carrier.is_dir():
            directories.add(local)
        else:
            files[local] = (_digest(carrier.read_bytes()), carrier.stat().st_mode & 0o777)
    if not files:
        raise ReleaseContractError("release-active-n-invalid", "active project-local ca Skill is empty")
    return files, directories


def _active_n_state(root: Path, candidate: ValidatedCandidate) -> tuple[str, str, str]:
    """Prove and digest the actual runnable N release and its public Skill.

    Candidate testing cannot begin from a selector-only N. The package and
    project-local Skill must be the complete retained N carriers; these exact
    digests become durable suite evidence for all later gates.
    """

    _refuse_secret_relative(CURRENT_SELECTOR_RELATIVE)
    selector = root / CURRENT_SELECTOR_RELATIVE
    if selector.is_symlink() or not selector.is_file():
        raise ReleaseContractError("release-active-n-invalid", "executing N selector is missing or unsafe")
    selector_bytes = selector.read_bytes()
    package_relative = f"{RUNTIME_ROOT}/releases/{candidate.authority.executing_release}"
    package = _safe_path(root, package_relative)
    manifest_path = package / "manifest.toml"
    _refuse_secret_relative(Path(package_relative) / "manifest.toml")
    if manifest_path.is_symlink() or not manifest_path.is_file():
        raise ReleaseContractError("release-active-n-invalid", "executing N has no retained package manifest")
    try:
        manifest_bytes = manifest_path.read_bytes()
        manifest_text = manifest_bytes.decode("utf-8")
        manifest = tomllib.loads(manifest_text)
        selector_payload = tomllib.loads(selector_bytes.decode("utf-8"))
        bootstrap = (
            isinstance(selector_payload, dict)
            and _bootstrap_prior_manifest_is_exact(
                selector_payload, manifest_bytes, candidate.authority.executing_release
            )
        )
        if (
            set(manifest) != {"schema_version", "candidate_snapshot_manifest_sha256", "package", "files"}
            or manifest["schema_version"] != 2
            or manifest["package"] != "caprmedio-framework"
            or (manifest["candidate_snapshot_manifest_sha256"] != candidate.authority.executing_release
                and not (bootstrap and _bootstrap_source_context_is_valid(
                    manifest["candidate_snapshot_manifest_sha256"]
                )))
            or not isinstance(manifest["files"], list)
        ):
            raise ValueError("retained N manifest is not a complete Framework package")
        rows = [
            PackageRow.model_validate(
                {
                    "resource": row["resource"],
                    "source_path": row["source_path"],
                    "destination_path": row["destination"],
                    "sha256": row["sha256"],
                    "mode": row["mode"],
                }
            )
            for row in manifest["files"]
        ]
        # ``_verify_release`` reads every manifest-listed target.  Refuse each
        # name first, before it can open any package or Skill bytes.
        for row in rows:
            _refuse_secret_relative(Path(package_relative) / row.destination_path)
        resources = {row.resource for row in rows}
        destinations = {row.destination_path for row in rows}
        if (
            resources != {"FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL"}
            or not any(row.destination_path.startswith("METHODOLOGY/sources/") for row in rows)
            or not any(row.destination_path.startswith("METHODOLOGY/compiled/") for row in rows)
            or not REQUIRED_SKILL_FILES <= destinations
            or any(
                not any(row.source_path.startswith(prefix) for row in rows if row.resource == "FRAMEWORK_ENGINE")
                for prefix in REQUIRED_ENGINE_SOURCE_PREFIXES
            )
        ):
            raise ValueError("retained N package is incomplete")
        _verify_release(
            package,
            manifest_text if bootstrap else _render_manifest(candidate.authority.executing_release, rows),
            rows,
        )
    except (KeyError, OSError, TypeError, ValueError, ReleasePackagingError) as error:
        raise ReleaseContractError("release-active-n-invalid", "executing N package is not a complete retained Framework release") from error

    expected_skill = {
        row.destination_path.removeprefix("SKILLS/ca/"): (row.sha256, row.mode)
        for row in rows if row.resource == "SKILL"
    }
    expected_directories = {
        parent.as_posix()
        for name in expected_skill
        for parent in Path(name).parents
        if parent != Path(".")
    }
    actual_skill, actual_directories = _active_skill_records(root, PROJECT_SKILL_TARGET)
    if actual_skill != expected_skill or actual_directories != expected_directories:
        raise ReleaseContractError("release-active-n-invalid", "project-local ca Skill is not the complete retained N Skill")
    return (
        _digest(selector_bytes),
        tree_sha256(root, package_relative),
        _digest(canonical_json({"files": actual_skill, "directories": sorted(actual_directories)})),
    )


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
    compiled_prefix = f"{compilation.child_materialization_root}/"
    covered: set[str] = set()
    compiled_covered = False
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
        compiled_covered = compiled_covered or any(source.startswith(compiled_prefix) for source in properties)
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
    if not compiled_covered:
        return len(cases), tuple(sorted(covered)), "suite did not report compiled candidate coverage"
    return len(cases), tuple(sorted(covered)), ""


def _durable_bytes(path: Path, payload: bytes) -> None:
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())


def _write_capture(path: Path, payload: bytes) -> None:
    """Write one executor output carrier without changing receipt semantics."""

    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())


def _sealed_file(root: Path, relative: str) -> Path:
    """Resolve one inventory file without crossing a symlinked carrier."""

    _refuse_secret_relative(relative)
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts:
        raise ReleaseContractError("release-suite-path-unsafe", "suite workspace source path is unsafe")
    cursor = root
    for part in path.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ReleaseContractError("release-suite-path-unsafe", "suite workspace source path contains a symlink")
    if not cursor.is_file():
        raise ReleaseContractError("release-suite-input-missing", "sealed suite input is missing or is not a regular file")
    return cursor


def _copy_workspace_file(root: Path, workspace: Path, relative: str, sha256: str, mode: int) -> None:
    source = _sealed_file(root, relative)
    if _digest(source.read_bytes()) != sha256 or source.stat().st_mode & 0o777 != mode:
        raise ReleaseContractError("release-currentness-stale", f"sealed suite input changed: {relative}")
    target = workspace / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() or target.is_symlink():
        raise ReleaseContractError("release-suite-workspace-invalid", "suite workspace has a duplicate input")
    with target.open("xb") as stream:
        stream.write(source.read_bytes())
        stream.flush()
        os.fsync(stream.fileno())
    target.chmod(mode)


def _materialize_suite_workspace(
    root: Path,
    workspace: Path,
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation,
    working_directory: str,
) -> None:
    """Copy only sealed candidate inputs into a disposable suite workspace.

    In particular this does *not* copy the live selector, retained N package,
    or public project Skill.  An executor therefore cannot mutate those
    carriers through the declared suite workspace.  It still needs its own
    process isolation to prevent arbitrary commands from addressing host paths
    directly; the default executor intentionally provides no host fallback.
    """

    rows: dict[str, tuple[str, int]] = {}
    for row in candidate.manifest.source_inventory_rows:
        rows[row.source_path] = (row.source_sha256, row.source_mode)
    for row in compilation.package_rows:
        observed = rows.setdefault(row.source_path, (row.sha256, row.mode))
        if observed != (row.sha256, row.mode):
            raise ReleaseContractError("release-suite-binding-mismatch", "suite input has conflicting sealed digests")
    for relative, (sha256, mode) in sorted(rows.items()):
        _copy_workspace_file(root, workspace, relative, sha256, mode)

    # The declared working directory can be an intentionally empty carrier.
    # Creating it in the disposable workspace does not add a host source.
    _safe_path(workspace, working_directory, create=True)


def _copy_report_from_output(output_root: Path, destination: Path) -> None:
    """Import one bounded report from the executor's writable output mount."""

    report = output_root / "coverage.xml"
    if report.is_symlink() or not report.is_file() or report.stat().st_size > MAX_REPORT_BYTES:
        return
    _write_capture(destination, report.read_bytes())


def execute_bound_release_suite(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation,
    *,
    timeout_seconds: float = 900,
    executor: SuiteSandboxExecutor | None = None,
) -> SuiteGateEvidence:
    """Run exact sealed argv once through an isolated executor.

    Invalid admission raises before execution. Once execution is attempted all
    process, coverage, currentness and recording failures return non-pass evidence.
    Evidence is retained at a fixed, unique Project-relative attempt directory.
    Direct host execution is deliberately unavailable: absence of an approved
    sandbox yields durable incomplete evidence rather than a weaker pass.
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
    active_n_before = _active_n_state(root, candidate)
    parent = _safe_path(root, f"{EVIDENCE_ROOT}/{candidate.manifest.sha256}", create=True)
    attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=parent))
    relative = attempt.relative_to(root).as_posix()
    workspace = attempt / "workspace"
    workspace.mkdir()
    output_root = attempt / "output"
    output_root.mkdir()
    started = time.monotonic()
    outcome, reason, exit_code = "incomplete", "suite command did not complete", None
    tests, coverage = 0, ()
    stdout_sha = stderr_sha = report_sha = receipt_sha = None
    evidence: SuiteGateEvidence | None = None
    try:
        selected_executor = executor if executor is not None else _DEFAULT_EXECUTOR
        if selected_executor is None:
            _write_capture(attempt / "stdout.bin", b"")
            _write_capture(attempt / "stderr.bin", b"")
            outcome, reason = "incomplete", "approved isolated suite executor is not configured"
        else:
            _materialize_suite_workspace(root, workspace, candidate, compilation, environment.working_directory)
            # The process contract names only sandbox-internal paths.  The
            # executor receives host paths separately for its mounts; source
            # code never receives an authoritative Project or output path.
            admitted_path = getattr(selected_executor, "image_path", os.defpath)
            process_environment = _suite_process_environment(
                SANDBOX_WORKSPACE_PATH,
                SANDBOX_OUTPUT_PATH / "coverage.xml",
                compilation,
                candidate,
                executable_path=admitted_path,
            )
            try:
                result = selected_executor.run(
                    tuple(environment.command),
                    workspace=workspace,
                    output_root=output_root,
                    working_directory=environment.working_directory,
                    environment=process_environment,
                    timeout_seconds=timeout_seconds,
                )
                if not isinstance(result, SuiteExecutionResult):
                    raise TypeError("suite executor returned an untyped result")
                exit_code = result.exit_code
                _write_capture(attempt / "stdout.bin", result.stdout)
                _write_capture(attempt / "stderr.bin", result.stderr)
                if result.timed_out:
                    outcome, reason = "timed_out", "suite command timed out"
                elif result.left_descendants:
                    outcome, reason = "incomplete", "suite left running descendant processes"
                elif exit_code:
                    outcome, reason = "failed", "suite command failed"
                else:
                    outcome, reason = "incomplete", "coverage evidence is incomplete"
            except (OSError, TypeError, ValueError) as error:
                _write_capture(attempt / "stdout.bin", b"")
                _write_capture(attempt / "stderr.bin", b"")
                outcome, reason = "failed", f"suite executor could not start: {type(error).__name__}"
            _copy_report_from_output(output_root, attempt / "coverage.xml")
        _safe_path(root, relative)
        for output in (attempt / "stdout.bin", attempt / "stderr.bin"):
            if output.is_symlink() or not output.is_file():
                raise OSError("captured suite output carrier is unsafe")
        stdout_sha = _digest((attempt / "stdout.bin").read_bytes())
        stderr_sha = _digest((attempt / "stderr.bin").read_bytes())
        durable_report_path = attempt / "coverage.xml"
        if durable_report_path.is_file() and not durable_report_path.is_symlink() and durable_report_path.stat().st_size <= MAX_REPORT_BYTES:
            report_sha = _digest(durable_report_path.read_bytes())
            with durable_report_path.open("rb") as report_stream:
                os.fsync(report_stream.fileno())
        tests, coverage, coverage_reason = _observe_report(durable_report_path, compilation)
        if exit_code == 0 and reason != "suite left running descendant processes":
            outcome, reason = ("incomplete", coverage_reason) if coverage_reason else ("passed", "complete bound suite execution")
        try:
            _validate_bound_inputs(candidate, compilation)
            if (root / CURRENT_SELECTOR_RELATIVE).read_bytes() != selector_before:
                raise ReleaseContractError("release-currentness-stale", "executing N selector bytes changed during suite")
            if _active_n_state(root, candidate) != active_n_before:
                raise ReleaseContractError("release-currentness-stale", "executing N selector, runtime package or project-local ca Skill changed during suite")
            if _safe_path(root, environment.working_directory) != cwd:
                raise ReleaseContractError("release-currentness-stale", "suite working directory changed")
        except (ReleaseContractError, ReleasePackagingError, OSError, ValueError) as error:
            outcome, reason = "stale", f"post-suite bindings no longer validate: {getattr(error, 'code', type(error).__name__)}"
        evidence = SuiteGateEvidence(candidate.manifest.sha256, outcome, reason, environment.runner,
                                     tuple(environment.command), environment.working_directory, exit_code,
                                     tests, coverage, relative, stdout_sha, stderr_sha, report_sha,
                                     *active_n_before, None,
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
                             tests, coverage, relative, stdout_sha, stderr_sha, report_sha,
                             *active_n_before, receipt_sha,
                             time.monotonic() - started)


def verify_bound_suite_evidence(
    candidate: ValidatedCandidate, compilation: SealedCandidateCompilation, evidence: SuiteGateEvidence,
) -> Path:
    """Reopen durable suite evidence; this never establishes installation.

    Source/compiled bindings suffice here. Existing retained packages remain
    strict, while later package/image/promotion consumers own their package gates.
    """
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
        if _active_n_state(root, candidate) != (
            evidence.executing_selector_sha256,
            evidence.executing_release_package_sha256,
            evidence.executing_skill_sha256,
        ):
            raise ValueError("executing N no longer matches the successful suite receipt")
    except (OSError, ValueError) as error:
        raise ReleaseContractError("release-suite-evidence-mismatch", "successful suite evidence is missing, changed or incomplete") from error
    return root


__all__ = [
    "SuiteExecutionResult",
    "SuiteGateEvidence",
    "SuiteSandboxExecutor",
    "execute_bound_release_suite",
    "verify_bound_suite_evidence",
    "SUPPORTED_RUNNER",
    "REPORT_ENVIRONMENT_VARIABLE",
]
