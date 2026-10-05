#!/usr/bin/env python3
"""Run the sealed Framework Release suite and write source-bound JUnit XML.

This is a private carrier of the ``RELEASE_VERSION`` Tool.  Its public
invocation is deliberately argument-free: the sealed executor supplies the
complete environment defined by CA-D-579.  It never selects a test subset,
accepts caller coverage, or mutates the mounted workspace.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Mapping

from release_suite_reference_context import (
    ReleaseSuiteReferenceContextError,
    ReferenceRow,
    validate_reference_rows,
)


PROJECT_ROOT_ENV = "CAPRMEDIO_RELEASE_PROJECT_ROOT"
COMPILED_ROOT_ENV = "CAPRMEDIO_RELEASE_COMPILED_CANDIDATE_ROOT"
CANDIDATE_MANIFEST_ENV = "CAPRMEDIO_RELEASE_CANDIDATE_MANIFEST_SHA256"
REPORT_ENV = "CAPRMEDIO_RELEASE_SUITE_REPORT"
SOURCE_BINDINGS_ENV = "CAPRMEDIO_RELEASE_SOURCE_BINDINGS"
SOURCE_BINDINGS_SHA256_ENV = "CAPRMEDIO_RELEASE_SOURCE_BINDINGS_SHA256"

_REQUIRED_ENVIRONMENT = (
    PROJECT_ROOT_ENV,
    COMPILED_ROOT_ENV,
    CANDIDATE_MANIFEST_ENV,
    REPORT_ENV,
    SOURCE_BINDINGS_ENV,
    SOURCE_BINDINGS_SHA256_ENV,
)
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_TEST_MODULE = re.compile(r"^102_FRAMEWORK_ENGINE(?:/[^/]+)*/test_[^/]+\.py$")
_REQUIRED_COVERAGE = frozenset({"Methodology", "Tools", "Apps", "MCP", "Agentic", "Skill"})
_REQUIRED_SKILL_DESTINATIONS = frozenset({"SKILLS/ca/SKILL.md", "SKILLS/ca/agents/openai.yaml"})
_SANDBOX_PROJECT_ROOT = Path("/workspace")
_SANDBOX_SOURCE_BINDINGS = _SANDBOX_PROJECT_ROOT / ".caprmedio_release/source_bindings.json"
_SANDBOX_REPORT = Path("/output/coverage.xml")
_COMPILED_PROBE_MODULE = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/"
    "tests/test_release_compilation.py"
)


class SuiteError(ValueError):
    """A deterministic refusal that must leave a non-passing JUnit report."""


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise SuiteError("duplicate JSON key")
        value[key] = item
    return value


def _load_canonical_json(path: Path, *, label: str) -> tuple[dict[str, Any], bytes]:
    if path.is_symlink() or not path.is_file():
        raise SuiteError(f"{label} must be one regular file")
    payload = path.read_bytes()
    try:
        value = json.loads(payload.decode("utf-8"), object_pairs_hook=_reject_duplicates)
    except (UnicodeDecodeError, json.JSONDecodeError, SuiteError) as error:
        raise SuiteError(f"{label} is not valid JSON") from error
    if not isinstance(value, dict) or _canonical_json(value) != payload:
        raise SuiteError(f"{label} is not canonical JSON")
    return value, payload


def _exact_object(value: object, keys: set[str], *, label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != keys:
        raise SuiteError(f"{label} has an unsupported shape")
    return value


def _relative(value: object, *, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip() or "\\" in value:
        raise SuiteError(f"{label} must be a normalized relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts) or path.as_posix() != value:
        raise SuiteError(f"{label} must be a normalized relative path")
    return value


def _digest(value: object, *, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise SuiteError(f"{label} must be a lowercase SHA-256")
    return value


def _project_path(root: Path, relative: str, *, label: str) -> Path:
    path = root.joinpath(*PurePosixPath(relative).parts)
    if path.is_symlink() or not path.is_file():
        raise SuiteError(f"{label} is not a regular sealed carrier")
    try:
        path.resolve(strict=True).relative_to(root.resolve(strict=True))
    except ValueError as error:
        raise SuiteError(f"{label} escapes the sealed workspace") from error
    return path


def _coverage_group(destination_path: str) -> str | None:
    prefixes = {
        "METHODOLOGY/": "Methodology",
        "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/": "Tools",
        "FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/": "Apps",
        "FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/": "MCP",
        "FRAMEWORK_ENGINE/202_AGENTIC/": "Agentic",
        "SKILLS/ca/": "Skill",
    }
    return next((group for prefix, group in prefixes.items() if destination_path.startswith(prefix)), None)


@dataclass(frozen=True)
class PackageRow:
    resource: str
    source_path: str
    destination_path: str
    sha256: str
    mode: int


@dataclass(frozen=True)
class ModuleProbeRules:
    source_path: str
    sha256: str
    probes: dict[str, tuple[str, ...]]


@dataclass(frozen=True)
class BoundInputs:
    root: Path
    compiled_root: str
    candidate_manifest_sha256: str
    report_path: Path
    envelope_sha256: str
    rows: dict[str, PackageRow]
    reference_rows: tuple[ReferenceRow, ...]
    control_context_digest: str
    test_modules: tuple[str, ...]
    probes: ModuleProbeRules


def _environment() -> dict[str, str]:
    if len(sys.argv) != 1:
        raise SuiteError("Release suite accepts no command-line arguments")
    return _validated_environment(os.environ)


def _validated_environment(values: Mapping[str, str]) -> dict[str, str]:
    """Copy only the six declared environment values into a sealed frame."""

    environment: dict[str, str] = {}
    for key in _REQUIRED_ENVIRONMENT:
        value = values.get(key)
        if not isinstance(value, str) or not value or value != value.strip() or "\x00" in value:
            raise SuiteError(f"missing or invalid {key}")
        environment[key] = value
    return environment


def _parse_rows(value: object, *, root: Path) -> dict[str, PackageRow]:
    if not isinstance(value, list) or not value:
        raise SuiteError("source bindings package_rows must be nonempty")
    rows: dict[str, PackageRow] = {}
    destinations: set[str] = set()
    for item in value:
        row = _exact_object(item, {"resource", "source_path", "destination_path", "sha256", "mode"}, label="package row")
        resource = row["resource"]
        if resource not in {"FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL"}:
            raise SuiteError("package row resource is unsupported")
        source_path = _relative(row["source_path"], label="package row source_path")
        destination_path = _relative(row["destination_path"], label="package row destination_path")
        sha256 = _digest(row["sha256"], label="package row sha256")
        mode = row["mode"]
        if type(mode) is not int or not 0 <= mode <= 0o777:
            raise SuiteError("package row mode is invalid")
        if source_path in rows or destination_path in destinations:
            raise SuiteError("source bindings package rows are not unique")
        carrier = _project_path(root, source_path, label="package row")
        # Package rows retain the established D579 content-digest check.  The
        # Suite Owner validates their source mode while materializing the
        # workspace; D580 additionally requires this driver to validate the
        # exact bytes *and mode* of copied private reference rows below.
        if _sha256(carrier.read_bytes()) != sha256:
            raise SuiteError("sealed package-row digest changed")
        rows[source_path] = PackageRow(resource, source_path, destination_path, sha256, mode)
        destinations.add(destination_path)
    return rows


def _parse_reference_rows(root: Path, value: object) -> tuple[ReferenceRow, ...]:
    """Validate D579 schema-2 control rows against copied sealed bytes.

    The private Suite Owner binds the opaque control-context digest before the
    workspace becomes read-only.  The driver independently proves that the
    envelope's typed rows are the current, complete D580 closure and that
    their copied bytes and modes still agree with each declaration.
    """

    if not isinstance(value, list):
        raise SuiteError("source bindings reference_rows must be an ordered array")
    try:
        return validate_reference_rows(root, value)
    except ReleaseSuiteReferenceContextError as error:
        raise SuiteError("source bindings reference rows are not the sealed control closure") from error


def _parse_rules(
    root: Path,
    value: dict[str, Any],
    rows: dict[str, PackageRow],
    *,
    compiled_root: str,
) -> ModuleProbeRules:
    rule_ref = _exact_object(value, {"source_path", "sha256"}, label="source bindings mapping_rules")
    source_path = _relative(rule_ref["source_path"], label="mapping rule source_path")
    sha256 = _digest(rule_ref["sha256"], label="mapping rule sha256")
    row = rows.get(source_path)
    if row is None or row.sha256 != sha256:
        raise SuiteError("mapping rules are not a sealed package row")
    carrier = _project_path(root, source_path, label="mapping rules")
    rules, payload = _load_canonical_json(carrier, label="mapping rules")
    if _sha256(payload) != sha256:
        raise SuiteError("mapping rule digest changed")
    _exact_object(rules, {"schema_version", "module_probes"}, label="mapping rules")
    if rules["schema_version"] != 1 or not isinstance(rules["module_probes"], list):
        raise SuiteError("mapping rule schema is unsupported")
    compiled_prefix = compiled_root + "/"
    compiled_rows = tuple(sorted(
        row.source_path
        for row in rows.values()
        if row.resource == "METHODOLOGY" and row.source_path.startswith(compiled_prefix)
    ))
    probes: dict[str, tuple[str, ...]] = {}
    compiled_probe_modules: list[str] = []
    previous = ""
    for item in rules["module_probes"]:
        if not isinstance(item, dict) or set(item) not in (
            {"test_module_source_path", "source_paths"},
            {"test_module_source_path", "source_paths", "compiled_candidate_probe"},
        ):
            raise SuiteError("module probe has an unsupported shape")
        probe = item
        test_module = _relative(probe["test_module_source_path"], label="module probe test path")
        if _TEST_MODULE.fullmatch(test_module) is None or test_module not in rows:
            raise SuiteError("module probe does not name a sealed test module")
        source_paths = probe["source_paths"]
        if not isinstance(source_paths, list) or not source_paths:
            raise SuiteError("module probe source_paths must be nonempty")
        normalized = tuple(_relative(item, label="module probe source path") for item in source_paths)
        if tuple(sorted(normalized)) != normalized or len(set(normalized)) != len(normalized):
            raise SuiteError("module probe source paths are not canonical")
        if test_module in normalized or any(path not in rows for path in normalized):
            raise SuiteError("module probe names a non-package source")
        if any(path.startswith(compiled_prefix) for path in normalized):
            raise SuiteError("module probe cannot statically name a compiled candidate carrier")
        if test_module <= previous or test_module in probes:
            raise SuiteError("module probes are not source-path sorted and unique")
        compiled_candidate_probe = probe.get("compiled_candidate_probe", False)
        if type(compiled_candidate_probe) is not bool:
            raise SuiteError("compiled_candidate_probe must be a boolean")
        if compiled_candidate_probe:
            if test_module != _COMPILED_PROBE_MODULE:
                raise SuiteError("compiled_candidate_probe is allowed only for the Release compilation test")
            compiled_probe_modules.append(test_module)
            if not compiled_rows:
                raise SuiteError("compiled candidate has no sealed Methodology carrier")
            normalized = tuple(sorted((*normalized, compiled_rows[0])))
        probes[test_module] = normalized
        previous = test_module
    if compiled_probe_modules != [_COMPILED_PROBE_MODULE]:
        raise SuiteError("exactly one Release compilation module must request compiled candidate evidence")
    return ModuleProbeRules(source_path, sha256, probes)


def _bound_inputs_from_frame(environment: dict[str, str], *, require_sandbox_paths: bool) -> BoundInputs:
    environment = _validated_environment(environment)
    root = Path(environment[PROJECT_ROOT_ENV])
    if require_sandbox_paths and root != _SANDBOX_PROJECT_ROOT:
        raise SuiteError("Release suite project root must be /workspace")
    if root.is_symlink() or not root.is_dir():
        raise SuiteError("project root is not a sealed workspace")
    candidate = _digest(environment[CANDIDATE_MANIFEST_ENV], label="candidate manifest")
    compiled_root = _relative(environment[COMPILED_ROOT_ENV], label="compiled candidate root")
    report_path = Path(environment[REPORT_ENV])
    if require_sandbox_paths and report_path != _SANDBOX_REPORT:
        raise SuiteError("Release suite report must be /output/coverage.xml")
    if not report_path.is_absolute() or report_path.name != "coverage.xml" or report_path.is_symlink():
        raise SuiteError("report path must be the declared coverage.xml output")
    binding_path = Path(environment[SOURCE_BINDINGS_ENV])
    if require_sandbox_paths and binding_path != _SANDBOX_SOURCE_BINDINGS:
        raise SuiteError("Release suite source bindings must be /workspace/.caprmedio_release/source_bindings.json")
    try:
        binding_path.relative_to(root)
    except ValueError as error:
        raise SuiteError("source bindings must be inside the sealed workspace") from error
    envelope, payload = _load_canonical_json(binding_path, label="source bindings")
    envelope_sha256 = _digest(environment[SOURCE_BINDINGS_SHA256_ENV], label="source bindings SHA-256")
    if _sha256(payload) != envelope_sha256:
        raise SuiteError("source bindings SHA-256 does not match its bytes")
    _exact_object(
        envelope,
        {
            "schema_version",
            "candidate_snapshot_manifest_sha256",
            "mapping_rules",
            "package_rows",
            "reference_rows",
            "control_context_digest",
        },
        label="source bindings",
    )
    if envelope["schema_version"] != 2 or _digest(envelope["candidate_snapshot_manifest_sha256"], label="source bindings candidate") != candidate:
        raise SuiteError("source bindings do not belong to this candidate")
    rows = _parse_rows(envelope["package_rows"], root=root)
    reference_rows = _parse_reference_rows(root, envelope["reference_rows"])
    for reference in reference_rows:
        package = rows.get(reference.source_path)
        if package is not None and (package.sha256 != reference.sha256 or package.mode != reference.mode):
            raise SuiteError("source bindings package and reference rows conflict")
    control_context_digest = _digest(envelope["control_context_digest"], label="source bindings control context")
    rules = _parse_rules(root, envelope["mapping_rules"], rows, compiled_root=compiled_root)
    test_modules = tuple(sorted(path for path in rows if _TEST_MODULE.fullmatch(path) is not None))
    if not test_modules:
        raise SuiteError("sealed package has no in-tree Framework test modules")
    return BoundInputs(
        root,
        compiled_root,
        candidate,
        report_path,
        envelope_sha256,
        rows,
        reference_rows,
        control_context_digest,
        test_modules,
        rules,
    )


def _bound_inputs() -> BoundInputs:
    """Build public-CLI inputs from the one fixed sandbox environment."""

    return _bound_inputs_from_frame(_environment(), require_sandbox_paths=True)


_CHILD_HARNESS = r'''
import json
import sys
import unittest

module_parent, pattern, result_path = sys.argv[1:]

class RecordingResult(unittest.TestResult):
    def __init__(self):
        super().__init__()
        self.records = []
        self.current = {}

    def startTest(self, test):
        super().startTest(test)
        record = {"id": test.id(), "status": "success", "detail": ""}
        self.records.append(record)
        self.current[test.id()] = record

    def _mark(self, test, status, detail=""):
        record = self.current.get(test.id())
        if record is None:
            record = {"id": test.id(), "status": status, "detail": ""}
            self.records.append(record)
            self.current[test.id()] = record
        record["status"] = status
        record["detail"] = detail

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self._mark(test, "failure", self._exc_info_to_string(err, test))

    def addError(self, test, err):
        super().addError(test, err)
        self._mark(test, "error", self._exc_info_to_string(err, test))

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self._mark(test, "skipped", str(reason))

    def addExpectedFailure(self, test, err):
        super().addExpectedFailure(test, err)
        self._mark(test, "expected_failure", self._exc_info_to_string(err, test))

    def addUnexpectedSuccess(self, test):
        super().addUnexpectedSuccess(test)
        self._mark(test, "unexpected_success", "")

    def addSubTest(self, test, subtest, err):
        super().addSubTest(test, subtest, err)
        if err is not None:
            self._mark(test, "error", self._exc_info_to_string(err, test))

loader = unittest.TestLoader()
suite = loader.discover(start_dir=module_parent, pattern=pattern)
result = RecordingResult()
suite.run(result)
payload = {
    "loader_errors": list(loader.errors),
    "cases": result.records,
}
with open(result_path, "w", encoding="utf-8", newline="\n") as stream:
    stream.write(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
'''


@dataclass
class ObservedCase:
    test_id: str
    module_path: str
    status: str
    detail: str
    source_paths: tuple[str, ...]


def _run_module(inputs: BoundInputs, module_path: str, results_root: Path) -> tuple[list[ObservedCase], list[str]]:
    carrier = _project_path(inputs.root, module_path, label="test module")
    result_path = results_root / (_sha256(module_path.encode("utf-8")) + ".json")
    environment = {
        "PATH": os.environ.get("PATH", os.defpath),
        "PYTHONDONTWRITEBYTECODE": "1",
        "TMPDIR": "/tmp",
    }
    child = subprocess.run(
        (sys.executable, "-c", _CHILD_HARNESS, str(carrier.parent), carrier.name, str(result_path)),
        cwd=inputs.root,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    if child.returncode != 0 or result_path.is_symlink() or not result_path.is_file():
        detail = (child.stderr or child.stdout or "child test discovery failed").strip()
        return [], [f"{module_path}: {detail[:2000]}"]
    try:
        result, _payload = _load_canonical_json(result_path, label="child test result")
        _exact_object(result, {"loader_errors", "cases"}, label="child test result")
        if not isinstance(result["loader_errors"], list) or not isinstance(result["cases"], list):
            raise SuiteError("child result has invalid collections")
        source_paths = (module_path, *inputs.probes.probes.get(module_path, ()))
        cases: list[ObservedCase] = []
        for item in result["cases"]:
            record = _exact_object(item, {"id", "status", "detail"}, label="child testcase")
            if not isinstance(record["id"], str) or not record["id"] or not isinstance(record["status"], str) or not isinstance(record["detail"], str):
                raise SuiteError("child testcase is invalid")
            cases.append(ObservedCase(record["id"], module_path, record["status"], record["detail"], source_paths))
        errors = [str(item) for item in result["loader_errors"]]
        if not cases:
            errors.append(f"{module_path}: discovery returned no test cases")
        return cases, errors
    except SuiteError as error:
        return [], [f"{module_path}: {error}"]


def _source_probes(inputs: BoundInputs, paths: tuple[str, ...]) -> tuple[list[dict[str, str]], str | None]:
    probes: list[dict[str, str]] = []
    for path in paths:
        row = inputs.rows.get(path)
        if row is None:
            return [], f"unbound source path: {path}"
        carrier = _project_path(inputs.root, path, label="source probe")
        actual = _sha256(carrier.read_bytes())
        if actual != row.sha256:
            return [], f"changed source digest: {path}"
        probes.append({"sha256": row.sha256, "source_path": path})
    return probes, None


def _attach_properties(case: ET.Element, inputs: BoundInputs, probes: list[dict[str, str]]) -> None:
    properties = ET.SubElement(case, "properties")
    ET.SubElement(properties, "property", name="caprmedio.test_id", value=case.attrib["name"])
    ET.SubElement(properties, "property", name="caprmedio.source_bindings_sha256", value=inputs.envelope_sha256)
    for probe in probes:
        ET.SubElement(properties, "property", name="caprmedio.source_probe", value=_canonical_json(probe).decode("utf-8"))


def _write_report(inputs: BoundInputs, cases: list[ObservedCase], module_errors: list[str]) -> tuple[bool, str]:
    seen: set[str] = set()
    failures = errors = skipped = 0
    covered_groups: set[str] = set()
    covered_destinations: set[str] = set()
    compiled_covered = False
    suite = ET.Element(
        "testsuite",
        name="caprmedio.release_suite",
        **{"caprmedio.control_context_digest": inputs.control_context_digest},
    )
    for observed in cases:
        case = ET.SubElement(suite, "testcase", classname=observed.module_path, name=observed.test_id)
        if observed.test_id in seen:
            observed.status = "error"
            observed.detail = "duplicate discovered test ID"
        seen.add(observed.test_id)
        probes, probe_error = _source_probes(inputs, observed.source_paths)
        if probe_error:
            observed.status = "error"
            observed.detail = probe_error
        else:
            _attach_properties(case, inputs, probes)
            for probe in probes:
                row = inputs.rows[probe["source_path"]]
                covered_destinations.add(row.destination_path)
                group = _coverage_group(row.destination_path)
                if group is not None:
                    covered_groups.add(group)
                if probe["source_path"].startswith(inputs.compiled_root + "/"):
                    compiled_covered = True
        if observed.status == "failure" or observed.status in {"expected_failure", "unexpected_success"}:
            failures += 1
            ET.SubElement(case, "failure", message=observed.status).text = observed.detail
        elif observed.status == "skipped":
            skipped += 1
            ET.SubElement(case, "skipped", message=observed.detail)
        elif observed.status != "success":
            errors += 1
            ET.SubElement(case, "error", message=observed.status).text = observed.detail
    complete = not module_errors and failures == 0 and errors == 0 and skipped == 0 and len(seen) == len(cases)
    missing_groups = sorted(_REQUIRED_COVERAGE - covered_groups)
    if missing_groups or not compiled_covered:
        complete = False
        detail = "missing coverage: " + ", ".join(missing_groups + ([] if compiled_covered else ["Compiled Candidate"]))
        module_errors.append(detail)
    missing_skill_controls = sorted(_REQUIRED_SKILL_DESTINATIONS - covered_destinations)
    if missing_skill_controls:
        complete = False
        module_errors.append("missing Skill control probes: " + ", ".join(missing_skill_controls))
    for detail in module_errors:
        errors += 1
        ET.SubElement(suite, "error", message="release-suite-incomplete").text = detail
    suite.set("tests", str(len(cases)))
    suite.set("failures", str(failures))
    suite.set("errors", str(errors))
    suite.set("skipped", str(skipped))
    inputs.report_path.parent.mkdir(parents=True, exist_ok=True)
    if inputs.report_path.exists() or inputs.report_path.is_symlink():
        raise SuiteError("report path already exists")
    ET.ElementTree(suite).write(inputs.report_path, encoding="utf-8", xml_declaration=True)
    return complete, "; ".join(module_errors)


def _execute_bound(inputs: BoundInputs) -> int:
    """Execute one already-validated frame without changing its bindings."""

    temporary = Path(tempfile.mkdtemp(prefix="release-suite-", dir=inputs.report_path.parent))
    cases: list[ObservedCase] = []
    module_errors: list[str] = []
    for module_path in inputs.test_modules:
        observed, errors = _run_module(inputs, module_path, temporary)
        cases.extend(observed)
        module_errors.extend(errors)
    complete, _reason = _write_report(inputs, cases, module_errors)
    return 0 if complete else 1


def _run_fixture_frame(environment: Mapping[str, str]) -> int:
    """Private disposable-test seam; public CLI paths remain fixed.

    Tests may supply a complete sealed fixture frame, but cannot enable an
    alternate public command-line selector or relax package-row validation.
    """

    return _execute_bound(_bound_inputs_from_frame(dict(environment), require_sandbox_paths=False))


def _failure_report(environment: dict[str, str] | None, detail: str) -> None:
    if environment is None:
        return
    if environment.get(REPORT_ENV) != str(_SANDBOX_REPORT):
        return
    path = _SANDBOX_REPORT
    if path.exists() or path.is_symlink():
        return
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        suite = ET.Element("testsuite", name="caprmedio.release_suite", tests="0", failures="0", errors="1", skipped="0")
        ET.SubElement(suite, "error", message="release-suite-refused").text = detail
        ET.ElementTree(suite).write(path, encoding="utf-8", xml_declaration=True)
    except OSError:
        return


def main() -> int:
    environment: dict[str, str] | None = None
    try:
        environment = _environment()
        inputs = _bound_inputs()
        return _execute_bound(inputs)
    except (OSError, SuiteError, ValueError) as error:
        _failure_report(environment, str(error))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
