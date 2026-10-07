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
import json
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
from release_suite_reference_context import (
    ReleaseSuiteReferenceContext, ReleaseSuiteReferenceContextError,
    capture_context, copy_verified_bytes, revalidate_context, validate_schema2_context,
)
from release_suite_limits import MAX_UNIT_TIMEOUT_SECONDS, resolve_unit_deadline
from release_test_phases import ReleaseTestPhaseMap, derive_test_phase_map_from_rows


EVIDENCE_ROOT = ".caprmedio_runtime/release_suite"
REPORT_ENVIRONMENT_VARIABLE = "CAPRMEDIO_RELEASE_SUITE_REPORT"
PROJECT_ROOT_ENVIRONMENT_VARIABLE = "CAPRMEDIO_RELEASE_PROJECT_ROOT"
COMPILED_ROOT_ENVIRONMENT_VARIABLE = "CAPRMEDIO_RELEASE_COMPILED_CANDIDATE_ROOT"
CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE = "CAPRMEDIO_RELEASE_CANDIDATE_MANIFEST_SHA256"
SOURCE_BINDINGS_ENVIRONMENT_VARIABLE = "CAPRMEDIO_RELEASE_SOURCE_BINDINGS"
SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE = "CAPRMEDIO_RELEASE_SOURCE_BINDINGS_SHA256"
MODULE_RULES_RELATIVE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_suite_bindings.json"
SOURCE_BINDINGS_RELATIVE = ".caprmedio_release/source_bindings.json"
SUITE_DRIVER_RELATIVE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_suite.py"
SUITE_DRIVER_COMMAND = ("python", SUITE_DRIVER_RELATIVE)
SUITE_DRIVER_WORKING_DIRECTORY = "."
COMPILED_PROBE_TEST_MODULE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/tests/test_release_compilation.py"
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
    control_context_digest: str | None = None
    phase_map_sha256: str | None = None

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


def require_declared_suite_command(environment: object) -> None:
    """Admit only D579's fixed private driver at both suite boundaries."""

    if (getattr(environment, "runner", None) != SUPPORTED_RUNNER
            or tuple(getattr(environment, "command", ())) != SUITE_DRIVER_COMMAND
            or getattr(environment, "working_directory", None) != SUITE_DRIVER_WORKING_DIRECTORY):
        raise ReleaseContractError("release-suite-command-untrusted", "suite invocation is not the declared Release driver command")


def _suite_process_environment(
    root: Path,
    report_path: Path,
    compilation: SealedCandidateCompilation,
    candidate: ValidatedCandidate,
    *,
    source_bindings_sha256: str,
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
    if not isinstance(source_bindings_sha256, str) or _SOURCE_CONTEXT.fullmatch(source_bindings_sha256) is None:
        raise ReleaseContractError("release-suite-bindings-invalid", "suite source-bindings digest is invalid")

    return {
        "PATH": executable_path,
        PROJECT_ROOT_ENVIRONMENT_VARIABLE: str(root),
        REPORT_ENVIRONMENT_VARIABLE: str(report_path),
        COMPILED_ROOT_ENVIRONMENT_VARIABLE: compilation.child_materialization_root,
        CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE: candidate.manifest.sha256,
        SOURCE_BINDINGS_ENVIRONMENT_VARIABLE: str(SANDBOX_WORKSPACE_PATH / SOURCE_BINDINGS_RELATIVE),
        SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE: source_bindings_sha256,
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


def _unit_phase_map(rows: list[PackageRow]) -> ReleaseTestPhaseMap:
    """Derive the Unit partition from complete sealed package rows only."""

    phase_map = derive_test_phase_map_from_rows(rows)
    if not phase_map.unit_paths:
        raise ReleaseContractError("release-test-phase-unit-set-invalid", "sealed candidate has no Unit test module")
    return phase_map


def _observe_report(
    path: Path,
    root: Path,
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation,
    context: ReleaseSuiteReferenceContext,
) -> tuple[int, tuple[str, ...], str]:
    """Extract actual execution counts and admit only sealed per-case probes."""
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
    try:
        phase_map = _unit_phase_map(compilation.package_rows)
    except ReleaseContractError:
        return 0, (), "sealed Unit phase map is unavailable or invalid"
    if (report.get("caprmedio.phase") != "unit"
            or report.get("caprmedio.phase_map_sha256") != phase_map.sha256):
        return 0, (), "coverage report Unit phase binding is missing or mismatched"
    if report.get("caprmedio.control_context_digest") != context.control_context_digest:
        return 0, (), "coverage report control-context digest is missing or mismatched"
    cases = list(report.iter("testcase"))
    if not cases:
        return 0, (), "coverage report has no executed testcases"
    try:
        envelope_sha256 = _digest(_source_bindings_bytes(
            root, candidate.manifest.sha256, compilation.package_rows, compilation.child_materialization_root, context,
        ))
        _rules_row, explicit_probes = _validate_module_rules(
            root, compilation.package_rows, compilation.child_materialization_root,
        )
    except (OSError, ReleaseContractError):
        return len(cases), (), "source bindings are unavailable or changed"
    rows = {row.source_path: row for row in compilation.package_rows}
    compiled_prefix = f"{compilation.child_materialization_root}/"
    covered: set[str] = set()
    compiled_covered = False
    probed_sources: set[str] = set()
    test_ids: set[str] = set()
    for case in cases:
        if list(case.iter("failure")) or list(case.iter("error")):
            return len(cases), tuple(sorted(covered)), "coverage report contains failed testcases"
        if list(case.iter("skipped")):
            return len(cases), tuple(sorted(covered)), "coverage report contains skipped testcases"
        values: dict[str, list[str | None]] = {}
        for property_ in case.findall("./properties/property"):
            values.setdefault(property_.get("name", ""), []).append(property_.get("value"))
        test_id = values.get("caprmedio.test_id")
        if (test_id is None or len(test_id) != 1 or not isinstance(test_id[0], str)
                or test_id[0] != case.get("name") or test_id[0] in test_ids):
            return len(cases), tuple(sorted(covered)), "testcase test ID is missing, mismatched or duplicated"
        test_ids.add(test_id[0])
        module_path = case.get("classname")
        if not isinstance(module_path, str) or module_path not in set(_test_module_source_paths(compilation.package_rows)):
            return len(cases), tuple(sorted(covered)), "testcase module is not a sealed test carrier"
        binding_values = values.get("caprmedio.source_bindings_sha256")
        if binding_values != [envelope_sha256]:
            return len(cases), tuple(sorted(covered)), "testcase source-bindings digest is missing or mismatched"
        expected_paths = (module_path, *explicit_probes.get(module_path, ()))
        expected_probes = [
            canonical_json({"source_path": source_path, "sha256": rows[source_path].sha256}).decode("utf-8")
            for source_path in expected_paths
        ]
        if values.get("caprmedio.source_probe") != expected_probes:
            return len(cases), tuple(sorted(covered)), "testcase source probes do not match sealed module bindings"
        for source_path in expected_paths:
            probed_sources.add(source_path)
            group = _coverage_group(rows[source_path].destination_path)
            if group is not None:
                covered.add(group)
            compiled_covered = compiled_covered or source_path.startswith(compiled_prefix)
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
    skill_controls = {
        row.source_path for row in compilation.package_rows
        if row.destination_path in {"SKILLS/ca/SKILL.md", "SKILLS/ca/agents/openai.yaml"}
    }
    if len(skill_controls) != 2 or not skill_controls <= probed_sources:
        return len(cases), tuple(sorted(covered)), "suite did not report both sealed Skill controls"
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


def _envelope_package_rows(rows: list[PackageRow]) -> list[dict[str, object]]:
    """Render the complete typed handoff rows without sorting or projection."""

    return [
        {
            "resource": row.resource,
            "source_path": row.source_path,
            "destination_path": row.destination_path,
            "sha256": row.sha256,
            "mode": row.mode,
        }
        for row in rows
    ]


def _test_module_source_paths(rows: list[PackageRow]) -> tuple[str, ...]:
    """Return only Unit modules from the complete sealed phase assignment."""

    return _unit_phase_map(rows).unit_paths


def _validate_module_rules(
    root: Path, rows: list[PackageRow], compiled_root: str,
) -> tuple[PackageRow, dict[str, tuple[str, ...]]]:
    """Prove the sealed explicit-probe mapping references only typed rows."""

    matching = [row for row in rows if row.source_path == MODULE_RULES_RELATIVE]
    if len(matching) != 1:
        raise ReleaseContractError("release-suite-bindings-invalid", "sealed module-rules carrier is absent or duplicated")
    rules_row = matching[0]
    rules_path = _sealed_file(root, MODULE_RULES_RELATIVE)
    rules_bytes = rules_path.read_bytes()
    if _digest(rules_bytes) != rules_row.sha256 or rules_path.stat().st_mode & 0o777 != rules_row.mode:
        raise ReleaseContractError("release-currentness-stale", "sealed module-rules carrier changed")
    try:
        rules = json.loads(rules_bytes)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ReleaseContractError("release-suite-bindings-invalid", "sealed module-rules carrier is not JSON") from error
    if not isinstance(rules, dict) or set(rules) != {"schema_version", "module_probes"} or rules.get("schema_version") != 1:
        raise ReleaseContractError("release-suite-bindings-invalid", "sealed module-rules schema is invalid")
    if canonical_json(rules) != rules_bytes:
        raise ReleaseContractError("release-suite-bindings-invalid", "sealed module-rules carrier is not canonical JSON")
    probes = rules.get("module_probes")
    if not isinstance(probes, list):
        raise ReleaseContractError("release-suite-bindings-invalid", "sealed module-rules probes are invalid")
    rows_by_source = {row.source_path: row for row in rows}
    if len(rows_by_source) != len(rows):
        raise ReleaseContractError("release-suite-bindings-invalid", "sealed package rows have duplicate source paths")
    test_modules = set(_test_module_source_paths(rows))
    compiled_prefix = compiled_root + "/"
    compiled_rows = sorted(
        row.source_path for row in rows
        if row.resource == "METHODOLOGY" and row.source_path.startswith(compiled_prefix)
    )
    if not compiled_rows:
        raise ReleaseContractError("release-suite-bindings-invalid", "sealed package has no compiled-candidate probe row")
    compiled_probe = compiled_rows[0]
    module_paths: list[str] = []
    bindings: dict[str, tuple[str, ...]] = {}
    compiled_probe_modules: list[str] = []
    for probe in probes:
        if (not isinstance(probe, dict)
                or set(probe) not in ({"test_module_source_path", "source_paths"},
                                      {"test_module_source_path", "source_paths", "compiled_candidate_probe"})):
            raise ReleaseContractError("release-suite-bindings-invalid", "sealed module-rules probe is invalid")
        module_path = probe.get("test_module_source_path")
        source_paths = probe.get("source_paths")
        if not isinstance(module_path, str) or module_path not in test_modules:
            raise ReleaseContractError("release-suite-bindings-invalid", "module rule names an unsealed test module")
        if (not isinstance(source_paths, list)
                or any(not isinstance(source, str) or source not in rows_by_source for source in source_paths)
                or source_paths != sorted(set(source_paths))
                or any(source.startswith(compiled_prefix) for source in source_paths)):
            raise ReleaseContractError("release-suite-bindings-invalid", "module probe is not a sorted sealed package-row reference")
        compiled_candidate_probe = probe.get("compiled_candidate_probe", False)
        if type(compiled_candidate_probe) is not bool:
            raise ReleaseContractError("release-suite-bindings-invalid", "compiled-candidate probe flag is not boolean")
        if compiled_candidate_probe:
            if module_path != COMPILED_PROBE_TEST_MODULE:
                raise ReleaseContractError("release-suite-bindings-invalid", "compiled-candidate probe is assigned to the wrong test module")
            compiled_probe_modules.append(module_path)
        module_paths.append(module_path)
        bindings[module_path] = tuple(source_paths) + ((compiled_probe,) if compiled_candidate_probe else ())
    if module_paths != sorted(set(module_paths)):
        raise ReleaseContractError("release-suite-bindings-invalid", "module rules are not source-path sorted")
    if compiled_probe_modules != [COMPILED_PROBE_TEST_MODULE]:
        raise ReleaseContractError("release-suite-bindings-invalid", "compiled-candidate probe must occur exactly once")
    return rules_row, bindings


def _source_bindings_bytes(root: Path, candidate_snapshot_manifest_sha256: str,
                           rows: list[PackageRow], compiled_root: str,
                           context: ReleaseSuiteReferenceContext) -> bytes:
    """Build the D579 canonical envelope from complete sealed package rows."""

    if _SOURCE_CONTEXT.fullmatch(candidate_snapshot_manifest_sha256) is None:
        raise ReleaseContractError("release-suite-bindings-invalid", "candidate snapshot digest is invalid")
    rules_row, _bindings = _validate_module_rules(root, rows, compiled_root)
    envelope = {
        "schema_version": 2,
        "candidate_snapshot_manifest_sha256": candidate_snapshot_manifest_sha256,
        "mapping_rules": {"source_path": MODULE_RULES_RELATIVE, "sha256": rules_row.sha256},
        "package_rows": _envelope_package_rows(rows),
        "reference_rows": [row.as_dict() for row in context.reference_rows],
        "control_context_digest": context.control_context_digest,
    }
    return canonical_json(envelope)


def _capture_reference_context(
    root: Path, candidate: ValidatedCandidate, compilation: SealedCandidateCompilation,
    executor: SuiteSandboxExecutor, selected_n_identity: str,
) -> ReleaseSuiteReferenceContext:
    bindings = _trusted_context_bindings(candidate, compilation, executor, selected_n_identity)
    try:
        return capture_context(root, bindings)
    except ReleaseSuiteReferenceContextError as error:
        raise ReleaseContractError("release-suite-reference-context-invalid", str(error)) from error


def _trusted_context_bindings(
    candidate: ValidatedCandidate, compilation: SealedCandidateCompilation,
    executor: SuiteSandboxExecutor, selected_n_identity: str,
) -> dict[str, str]:
    image_context = getattr(executor, "source_context_sha256", None)
    if not isinstance(image_context, str) or _SOURCE_CONTEXT.fullmatch(image_context) is None:
        raise ReleaseContractError("release-suite-reference-context-untrusted", "suite executor has no trusted selected-N image context")
    return {
        "candidate_snapshot_manifest_sha256": candidate.manifest.sha256,
        "compiled_candidate_root": compilation.child_materialization_root,
        "selected_n_identity": selected_n_identity,
        "selected_n_image_context": image_context,
    }


def _context_receipt(context: ReleaseSuiteReferenceContext) -> bytes:
    return canonical_json({
        "schema_version": 1,
        **dict(context.trusted_binding_values),
        "reference_rows": [row.as_dict() for row in context.reference_rows],
        "control_context_digest": context.control_context_digest,
    })


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
    context: ReleaseSuiteReferenceContext,
) -> str:
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
    reference_rows = {row.source_path: (row.sha256, row.mode) for row in context.reference_rows}
    for relative, expected in reference_rows.items():
        if relative in rows and rows[relative] != expected:
            raise ReleaseContractError("release-suite-reference-context-invalid", "reference context conflicts with a sealed package row")
    try:
        copy_verified_bytes(context, workspace)
    except ReleaseSuiteReferenceContextError as error:
        raise ReleaseContractError("release-suite-reference-context-invalid", str(error)) from error
    for relative, (sha256, mode) in sorted(rows.items()):
        if relative in reference_rows:
            continue
        _copy_workspace_file(root, workspace, relative, sha256, mode)

    bindings = _source_bindings_bytes(
        root, candidate.manifest.sha256, compilation.package_rows, compilation.child_materialization_root, context,
    )
    try:
        validate_schema2_context(json.loads(bindings), context)
    except (ReleaseSuiteReferenceContextError, json.JSONDecodeError) as error:
        raise ReleaseContractError("release-suite-reference-context-invalid", str(error)) from error
    bindings_path = workspace / SOURCE_BINDINGS_RELATIVE
    _safe_path(workspace, ".caprmedio_release", create=True)
    _durable_bytes(bindings_path, bindings)

    # The declared working directory can be an intentionally empty carrier.
    # Creating it in the disposable workspace does not add a host source.
    _safe_path(workspace, working_directory, create=True)
    return _digest(bindings)


def _copy_report_from_output(output_root: Path, destination: Path) -> None:
    """Import one bounded report from the executor's writable output mount."""

    report = output_root / "coverage.xml"
    if report.is_symlink() or not report.is_file() or report.stat().st_size > MAX_REPORT_BYTES:
        return
    _write_capture(destination, report.read_bytes())


def _write_unit_deadline(path: Path, deadline: object) -> None:
    """Retain the exact context-derived limit before isolated execution."""

    snapshot = getattr(deadline, "snapshot", None)
    snapshot_sha256 = getattr(deadline, "snapshot_sha256", None)
    if (not isinstance(snapshot, bytes) or not isinstance(snapshot_sha256, str)
            or _SOURCE_CONTEXT.fullmatch(snapshot_sha256) is None
            or _digest(snapshot) != snapshot_sha256):
        raise ReleaseContractError("release-suite-deadline-invalid", "derived Unit deadline snapshot is invalid")
    _durable_bytes(path, snapshot)


def _verify_unit_deadline(path: Path, deadline: object) -> None:
    """Require the retained derivation to remain exact before a Unit can pass."""

    snapshot = getattr(deadline, "snapshot", None)
    snapshot_sha256 = getattr(deadline, "snapshot_sha256", None)
    if (not isinstance(snapshot, bytes) or not isinstance(snapshot_sha256, str)
            or _SOURCE_CONTEXT.fullmatch(snapshot_sha256) is None
            or _digest(snapshot) != snapshot_sha256 or path.is_symlink()
            or not path.is_file() or path.read_bytes() != snapshot):
        raise ReleaseContractError("release-suite-deadline-stale", "derived Unit deadline evidence changed or is unavailable")


def execute_bound_release_suite(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation,
    *,
    timeout_seconds: float | None = None,
    executor: SuiteSandboxExecutor | None = None,
) -> SuiteGateEvidence:
    """Run exact sealed argv once through an isolated executor.

    Invalid admission raises before execution. Once execution is attempted all
    process, coverage, currentness and recording failures return non-pass evidence.
    Evidence is retained at a fixed, unique Project-relative attempt directory.
    Direct host execution is deliberately unavailable: absence of an approved
    sandbox yields durable incomplete evidence rather than a weaker pass.
    """
    if (timeout_seconds is not None
            and (not isinstance(timeout_seconds, (int, float)) or isinstance(timeout_seconds, bool)
                 or not 0 < timeout_seconds <= MAX_UNIT_TIMEOUT_SECONDS)):
        raise ReleaseContractError("release-suite-timeout-invalid", "fixture timeout must be within the governed Unit maximum")
    root = _validate_bound_inputs(candidate, compilation)
    phase_map = _unit_phase_map(compilation.package_rows)
    environment = candidate.manifest.full_suite_environment
    require_declared_suite_command(environment)
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
    context: ReleaseSuiteReferenceContext | None = None
    deadline: object | None = None
    evidence: SuiteGateEvidence | None = None
    selected_executor: SuiteSandboxExecutor | None = None
    try:
        selected_executor = executor if executor is not None else _DEFAULT_EXECUTOR
        if selected_executor is None:
            _write_capture(attempt / "stdout.bin", b"")
            _write_capture(attempt / "stderr.bin", b"")
            outcome, reason = "incomplete", "approved isolated suite executor is not configured"
        else:
            context = _capture_reference_context(
                root, candidate, compilation, selected_executor, candidate.authority.executing_release,
            )
            _durable_bytes(attempt / "context.json", _context_receipt(context))
            deadline = resolve_unit_deadline(context, fixture_timeout_seconds=timeout_seconds)
            _write_unit_deadline(attempt / "unit-deadline.json", deadline)
            source_bindings_sha256 = _materialize_suite_workspace(
                root, workspace, candidate, compilation, environment.working_directory, context,
            )
            # The context bytes were captured before workspace assembly.  Do
            # not issue the sandbox command if a live control carrier changed
            # while those sealed copies were being prepared.
            revalidate_context(
                root, context,
                _trusted_context_bindings(candidate, compilation, selected_executor, candidate.authority.executing_release),
            )
            # The process contract names only sandbox-internal paths.  The
            # executor receives host paths separately for its mounts; source
            # code never receives an authoritative Project or output path.
            admitted_path = getattr(selected_executor, "image_path", os.defpath)
            process_environment = _suite_process_environment(
                SANDBOX_WORKSPACE_PATH,
                SANDBOX_OUTPUT_PATH / "coverage.xml",
                compilation,
                candidate,
                source_bindings_sha256=source_bindings_sha256,
                executable_path=admitted_path,
            )
            try:
                result = selected_executor.run(
                    tuple(environment.command),
                    workspace=workspace,
                    output_root=output_root,
                    working_directory=environment.working_directory,
                    environment=process_environment,
                    timeout_seconds=deadline.timeout_seconds,
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
        if context is None:
            coverage_reason = "source reference context was not captured"
        else:
            tests, coverage, coverage_reason = _observe_report(durable_report_path, root, candidate, compilation, context)
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
            # An absent approved executor is a durable incomplete outcome, not
            # a stale post-execution result: no suite process or context
            # capture was attempted.  Once an executor is selected, retain
            # the full context/currentness revalidation fail-closed boundary.
            if selected_executor is not None:
                if context is None:
                    raise ReleaseContractError("release-suite-reference-context-invalid", "reference context is absent")
                revalidate_context(
                    root, context,
                    _trusted_context_bindings(candidate, compilation, selected_executor, candidate.authority.executing_release),
                )
                if deadline is None:
                    raise ReleaseContractError("release-suite-deadline-invalid", "derived Unit deadline is absent")
                _verify_unit_deadline(attempt / "unit-deadline.json", deadline)
        except (ReleaseContractError, ReleasePackagingError, OSError, ValueError) as error:
            outcome, reason = "stale", f"post-suite bindings no longer validate: {getattr(error, 'code', type(error).__name__)}"
        evidence = SuiteGateEvidence(candidate.manifest.sha256, outcome, reason, environment.runner,
                                     tuple(environment.command), environment.working_directory, exit_code,
                                     tests, coverage, relative, stdout_sha, stderr_sha, report_sha,
                                     *active_n_before, None,
                                     time.monotonic() - started,
                                     control_context_digest=context.control_context_digest if context is not None else None,
                                     phase_map_sha256=phase_map.sha256)
        receipt = canonical_json(asdict(evidence))
        _durable_bytes(attempt / "receipt.json", receipt)
        directory_descriptor = os.open(attempt, os.O_RDONLY)
        try:
            os.fsync(directory_descriptor)
        finally:
            os.close(directory_descriptor)
        receipt_sha = _digest(receipt)
    except (OSError, ValueError, KeyError) as error:
        detail = type(error).__name__
        if isinstance(error, OSError) and type(error.errno) is int:
            detail += f"[errno={error.errno}]"
        outcome, reason = "recording_uncertain", f"suite evidence could not be durably recorded: {detail}"
    if evidence is not None:
        return replace(evidence, outcome=outcome, reason=reason, receipt_sha256=receipt_sha)
    return SuiteGateEvidence(candidate.manifest.sha256, outcome, reason, environment.runner,
                             tuple(environment.command), environment.working_directory, exit_code,
                             tests, coverage, relative, stdout_sha, stderr_sha, report_sha,
                             *active_n_before, receipt_sha,
                             time.monotonic() - started,
                             control_context_digest=context.control_context_digest if context is not None else None,
                             phase_map_sha256=phase_map.sha256)


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
    phase_map = _unit_phase_map(compilation.package_rows)
    if evidence.phase_map_sha256 != phase_map.sha256:
        raise ReleaseContractError("release-suite-evidence-mismatch", "suite evidence binds a different Unit phase map")
    environment = candidate.manifest.full_suite_environment
    require_declared_suite_command(environment)
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
        for name in ("receipt.json", "context.json", "unit-deadline.json", "stdout.bin", "stderr.bin", "coverage.xml"):
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
        context_payload = json.loads(files["context.json"])
        if canonical_json(context_payload) != files["context.json"]:
            raise ValueError("reference-context receipt is not canonical")
        bindings = {
            key: context_payload[key]
            for key in ("candidate_snapshot_manifest_sha256", "compiled_candidate_root",
                        "selected_n_identity", "selected_n_image_context")
        }
        context = capture_context(root, bindings)
        if (_context_receipt(context) != files["context.json"]
                or context.control_context_digest != evidence.control_context_digest):
            raise ValueError("reference context no longer matches the retained receipt")
        _verify_unit_deadline(attempt / "unit-deadline.json", resolve_unit_deadline(context))
        tests, coverage, reason = _observe_report(attempt / "coverage.xml", root, candidate, compilation, context)
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
