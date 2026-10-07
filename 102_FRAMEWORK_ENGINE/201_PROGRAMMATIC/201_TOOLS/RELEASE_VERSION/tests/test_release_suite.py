"""Actual disposable compiler/package/subprocess gates; no Project release proof."""

from __future__ import annotations

import hashlib
import errno
import json
import os
import signal
import shutil
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET
from dataclasses import asdict, replace
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_compilation import build_preflight_validated_candidate, render_release_candidate  # noqa: E402
from release_contract import ReleaseContractError, canonical_json  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE, tree_sha256  # noqa: E402
from release_inventory import ReleaseInventoryError  # noqa: E402
from release_packaging import ReleasePackagingError, _render_manifest, stage_framework_package  # noqa: E402
from release_suite import (  # noqa: E402
    CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE,
    COMPILED_PROBE_TEST_MODULE,
    COMPILED_ROOT_ENVIRONMENT_VARIABLE,
    MODULE_RULES_RELATIVE,
    PROJECT_ROOT_ENVIRONMENT_VARIABLE,
    REPORT_ENVIRONMENT_VARIABLE,
    SOURCE_BINDINGS_ENVIRONMENT_VARIABLE,
    SOURCE_BINDINGS_RELATIVE,
    SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE,
    SUITE_DRIVER_COMMAND,
    SUITE_DRIVER_RELATIVE,
    SUITE_DRIVER_WORKING_DIRECTORY,
    SuiteExecutionResult,
    _refuse_secret_relative,
    _suite_process_environment,
    execute_bound_release_suite,
    verify_bound_suite_evidence,
)
from release_test_phases import CANDIDATE_E2E_MODULES, derive_test_phase_map_from_rows  # noqa: E402
from release_e2e_gate import (  # noqa: E402
    DEFAULT_RELEASE_E2E_LIMITS,
    DRIVER_RELATIVE as E2E_DRIVER_RELATIVE,
    GRAMMAR_RELATIVE as E2E_GRAMMAR_RELATIVE,
)
from full_suite_golden.control_fixture import copy_control_closure  # noqa: E402
import test_release_compilation as compilation_test  # noqa: E402


SCRIPT = '''import hashlib, json, os, sys, time, subprocess
from pathlib import Path
import xml.etree.ElementTree as ET
root, mode, literal = Path(os.environ["CAPRMEDIO_RELEASE_PROJECT_ROOT"]), sys.argv[1], sys.argv[2]
compiled_root = root / os.environ["CAPRMEDIO_RELEASE_COMPILED_CANDIDATE_ROOT"]
assert compiled_root.is_dir()
assert compiled_root.name == os.environ["CAPRMEDIO_RELEASE_CANDIDATE_MANIFEST_SHA256"]
bindings_path = Path(os.environ["CAPRMEDIO_RELEASE_SOURCE_BINDINGS"])
bindings_bytes = bindings_path.read_bytes()
assert hashlib.sha256(bindings_bytes).hexdigest() == os.environ["CAPRMEDIO_RELEASE_SOURCE_BINDINGS_SHA256"]
bindings = json.loads(bindings_bytes)
assert bindings == json.loads(json.dumps(bindings, sort_keys=True, separators=(",", ":")))
rows = {row["source_path"]: row for row in bindings["package_rows"]}
assert bindings["schema_version"] == 2
candidate_e2e_modules = {
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py",
}
test_modules = {
    path for path in rows if Path(path).name.startswith("test_") and path.endswith(".py")
}
assert candidate_e2e_modules <= test_modules
phase_rows = [
    [path, rows[path]["sha256"], "candidate_e2e" if path in candidate_e2e_modules else "unit"]
    for path in sorted(test_modules)
]
phase_map_sha256 = hashlib.sha256(json.dumps(phase_rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
assert len(bindings["control_context_digest"]) == 64
for reference in bindings["reference_rows"]:
    assert (root / reference["source_path"]).read_bytes()
    assert hashlib.sha256((root / reference["source_path"]).read_bytes()).hexdigest() == reference["sha256"]
rules_ref = bindings["mapping_rules"]
rules_path = root / rules_ref["source_path"]
assert hashlib.sha256(rules_path.read_bytes()).hexdigest() == rules_ref["sha256"]
rules = json.loads(rules_path.read_bytes())
assert rules == json.loads(json.dumps(rules, sort_keys=True, separators=(",", ":")))
module_probes = rules["module_probes"]
assert {item["test_module_source_path"] for item in module_probes} == test_modules - candidate_e2e_modules
print("actual stdout:" + literal, flush=True)
print("actual stderr", file=sys.stderr, flush=True)
if mode == "timeout":
    time.sleep(5)
if mode == "descendant":
    subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
if mode == "unsupported":
    Path(os.environ["CAPRMEDIO_RELEASE_SUITE_REPORT"]).write_text('{"passed":true}')
    sys.exit(0)
if mode == "missing":
    sys.exit(0)
if mode == "engine-only":
    module_probes = module_probes[:3]
if mode == "compiled-omitted":
    module_probes = [
        item for item in module_probes
        if not item.get("compiled_candidate_probe", False)
    ]
report = ET.Element(
    "testsuite", tests=str(len(module_probes)), failures="0", errors="0", skipped="0",
    **{
        "caprmedio.phase": "unit",
        "caprmedio.phase_map_sha256": phase_map_sha256,
        "caprmedio.control_context_digest": bindings["control_context_digest"],
    },
)
sources = []
for item in module_probes:
    module_path = item["test_module_source_path"]
    source_paths = [module_path, *item["source_paths"]]
    if item.get("compiled_candidate_probe", False):
        source_paths.append(next(
            path for path, row in sorted(rows.items())
            if row["resource"] == "METHODOLOGY"
            and path.startswith(os.environ["CAPRMEDIO_RELEASE_COMPILED_CANDIDATE_ROOT"] + "/")
        ))
    sources.extend(source_paths)
    for source in source_paths:
        assert source in rows
        assert (root / source).is_file()
        assert (root / source).read_bytes()
    case_name = "read sealed " + module_path
    case = ET.SubElement(report, "testcase", name=case_name, classname=module_path)
    props = ET.SubElement(case, "properties")
    ET.SubElement(props, "property", name="caprmedio.test_id", value=case_name)
    ET.SubElement(props, "property", name="caprmedio.source_bindings_sha256", value=os.environ["CAPRMEDIO_RELEASE_SOURCE_BINDINGS_SHA256"])
    for source in source_paths:
        ET.SubElement(props, "property", name="caprmedio.source_probe", value=json.dumps({"source_path": source, "sha256": rows[source]["sha256"]}, sort_keys=True, separators=(",", ":")))
if mode == "report-failure":
    ET.SubElement(case, "failure", message="deliberate failure")
if mode == "skipped":
    ET.SubElement(case, "skipped")
if mode == "summary":
    report.set("tests", "999")
if mode == "unbound":
    props[0].set("value", "unsealed test id")
ET.ElementTree(report).write(os.environ["CAPRMEDIO_RELEASE_SUITE_REPORT"], encoding="utf-8")
if mode == "stale":
    (root / sources[-1]).write_bytes(b"changed during actual command")
if mode == "selection":
    (root / ".caprmedio_runtime/framework/current.toml").write_text('release = "other"\\n')
if mode == "runtime":
    (root / ".caprmedio_runtime/framework/releases/N/runtime.txt").parent.mkdir(parents=True, exist_ok=True)
    (root / ".caprmedio_runtime/framework/releases/N/runtime.txt").write_text("changed active N")
if mode == "skill":
    (root / ".agents/skills/ca/SKILL.md").parent.mkdir(parents=True, exist_ok=True)
    (root / ".agents/skills/ca/SKILL.md").write_text("changed active Skill")
if mode == "settings":
    (root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text("changed settings")
if mode == "journal":
    journal = root / ".caprmedio_caprmedio/_journal/release.jsonl"
    journal.parent.mkdir(parents=True, exist_ok=True)
    journal.write_text('{"forged":true}\\n')
if mode == "fail":
    sys.exit(17)
'''


class FixtureSandboxExecutor:
    """Test-only local stand-in for the production isolated executor.

    It rewrites fixture-root argv paths into the disposable workspace and
    makes that source tree read-only for the child process, matching the
    production ``/workspace:ro`` mount.  Output remains a separate writable
    carrier; production never installs this executor.
    """

    def __init__(self, root: Path):
        self.root = root
        self.source_context_sha256 = "0" * 64
        self.mode = "success"
        self.literal = "$HOME;$(should-stay-literal)"
        self.start_error = False
        self.timeout_calls: list[float] = []

    @staticmethod
    def _freeze_workspace(workspace: Path) -> list[tuple[Path, int]]:
        """Remove child write permission without leaving retained evidence unusable."""

        paths = [workspace, *sorted(workspace.rglob("*"), key=lambda path: len(path.parts))]
        original_modes: list[tuple[Path, int]] = []
        for path in paths:
            if path.is_symlink():
                continue
            mode = path.stat().st_mode & 0o777
            original_modes.append((path, mode))
            path.chmod(mode & ~0o222)
        return original_modes

    @staticmethod
    def _thaw_workspace(original_modes: list[tuple[Path, int]]) -> None:
        for path, mode in reversed(original_modes):
            path.chmod(mode)

    def run(self, command, *, workspace, output_root, working_directory, environment, timeout_seconds):
        self.timeout_calls.append(timeout_seconds)
        self.last_environment = dict(environment)
        rewritten = []
        for value in command:
            path = Path(value)
            if path.is_absolute():
                try:
                    value = str(workspace / path.relative_to(self.root))
                except ValueError:
                    pass
            rewritten.append(value)
        local_environment = dict(environment)
        local_environment[PROJECT_ROOT_ENVIRONMENT_VARIABLE] = str(workspace)
        local_environment[REPORT_ENVIRONMENT_VARIABLE] = str(output_root / "coverage.xml")
        local_environment[SOURCE_BINDINGS_ENVIRONMENT_VARIABLE] = str(workspace / SOURCE_BINDINGS_RELATIVE)
        if self.start_error:
            raise FileNotFoundError("deliberate fixture start failure")
        if tuple(command) == SUITE_DRIVER_COMMAND:
            # The explicit local fixture uses the test interpreter; the sealed
            # production argv still names the interpreter in the verified N
            # image, which is unavailable from the stripped host fixture PATH.
            rewritten[0] = sys.executable
            rewritten.extend((self.mode, self.literal))
        stdout_path, stderr_path = output_root / "fixture.stdout", output_root / "fixture.stderr"
        original_modes = self._freeze_workspace(workspace)
        try:
            with stdout_path.open("xb") as stdout, stderr_path.open("xb") as stderr:
                process = subprocess.Popen(
                    tuple(rewritten),
                    cwd=workspace / working_directory,
                    env=local_environment,
                    stdin=subprocess.DEVNULL,
                    stdout=stdout,
                    stderr=stderr,
                    shell=False,
                    start_new_session=True,
                )
                try:
                    exit_code = process.wait(timeout=timeout_seconds)
                    left_descendants = False
                    try:
                        os.killpg(process.pid, 0)
                    except ProcessLookupError:
                        pass
                    else:
                        os.killpg(process.pid, signal.SIGKILL)
                        left_descendants = True
                    timed_out = False
                except subprocess.TimeoutExpired:
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    exit_code = process.wait()
                    left_descendants, timed_out = False, True
        finally:
            self._thaw_workspace(original_modes)
        return SuiteExecutionResult(exit_code, stdout_path.read_bytes(), stderr_path.read_bytes(), timed_out, left_descendants)


class ReleaseSuiteBoundaryTests(unittest.TestCase):
    """No-fixture boundary checks for the process and secret-read policies."""

    def test_suite_process_environment_is_exact_and_has_no_ambient_identity_or_credentials(self) -> None:
        root = Path("/sealed/project")
        report = Path("/sealed/project/.caprmedio_runtime/release_suite/coverage.xml")
        compilation = SimpleNamespace(child_materialization_root="sealed/compiled")
        candidate = SimpleNamespace(manifest=SimpleNamespace(sha256="a" * 64))

        environment = _suite_process_environment(
            root, report, compilation, candidate, source_bindings_sha256="a" * 64,
        )

        self.assertEqual(
            environment,
            {
                "PATH": os.defpath,
                PROJECT_ROOT_ENVIRONMENT_VARIABLE: str(root),
                REPORT_ENVIRONMENT_VARIABLE: str(report),
                COMPILED_ROOT_ENVIRONMENT_VARIABLE: "sealed/compiled",
                CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE: "a" * 64,
                SOURCE_BINDINGS_ENVIRONMENT_VARIABLE: "/workspace/.caprmedio_release/source_bindings.json",
                SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE: "a" * 64,
            },
        )
        self.assertFalse({"HOME", "USER", "LOGNAME", "SSH_AUTH_SOCK", "AWS_ACCESS_KEY_ID", "GITHUB_TOKEN"} & set(environment))

    def test_secret_refusal_becomes_the_release_contract_error_before_read(self) -> None:
        inventory_error = ReleaseInventoryError("release-inventory-secret-refused", "secret-shaped fixture")
        with patch("release_suite.refuse_secret_path", side_effect=inventory_error):
            with self.assertRaises(ReleaseContractError) as raised:
                _refuse_secret_relative(".caprmedio_runtime/framework/releases/N/SKILLS/ca/.env")
        self.assertEqual(raised.exception.code, "release-inventory-secret-refused")


class ReleaseSuiteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = compilation_test.ReleaseCompilationTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        # These pinned controls and synthetic module bytes exist only in the
        # disposable Project.  Real readers validate the resulting context;
        # this setup does not constitute live Unit or candidate E2E proof.
        copy_control_closure(RELEASE_ROOT.parents[3], self.root)
        self._seed_phase_modules()
        # Every test suite invocation explicitly receives this approved
        # disposable executor.  The production path has no host-process or
        # implicit global-executor fallback.
        self.executor = FixtureSandboxExecutor(self.root)
        (self.root / "suite-work").mkdir()

    def _seed_phase_modules(self) -> None:
        methodology_control = self.fixture.core.relative_to(self.root).as_posix()
        self.fixture.write(
            f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml",
            ("[release_suite]\nunit_timeout_seconds = 3600\n\n[release_e2e]\n" + "".join(
                f"{name} = {value}\n" for name, value in asdict(DEFAULT_RELEASE_E2E_LIMITS).items()
            )).encode(),
        )
        probes = {
            COMPILED_PROBE_TEST_MODULE: [methodology_control],
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_fixture_tools.py": [
                methodology_control, "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py",
            ],
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/tests/test_fixture_apps.py": [
                "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py",
            ],
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_fixture_mcp.py": [
                "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py",
            ],
            "102_FRAMEWORK_ENGINE/202_AGENTIC/tests/test_fixture_agentic.py": [
                "102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md",
                "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md",
                "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml",
            ],
        }
        for module in sorted(probes):
            self.fixture.write(module, b"# Synthetic sealed carrier, never live Release proof.\ndef test_fixture():\n    assert True\n")
        for relative in (*CANDIDATE_E2E_MODULES, E2E_DRIVER_RELATIVE, E2E_GRAMMAR_RELATIVE):
            source = RELEASE_ROOT.parents[3] / relative
            target = self.root / relative
            if not target.exists():
                self.fixture.write(relative, source.read_bytes(), source.stat().st_mode & 0o777)
            else:
                self.assertEqual(target.read_bytes(), source.read_bytes())
                self.assertEqual(target.stat().st_mode & 0o777, source.stat().st_mode & 0o777)
        rules = []
        for module, sources in sorted(probes.items()):
            rule = {"test_module_source_path": module, "source_paths": sorted(sources)}
            if module == COMPILED_PROBE_TEST_MODULE:
                rule["compiled_candidate_probe"] = True
            rules.append(rule)
        self.fixture.write(MODULE_RULES_RELATIVE, canonical_json({"schema_version": 1, "module_probes": rules}))

    def execute_suite(self, candidate, compilation, *, timeout_seconds: float | None = None):
        kwargs = {"executor": self.executor}
        if timeout_seconds is not None:
            kwargs["timeout_seconds"] = timeout_seconds
        return execute_bound_release_suite(candidate, compilation, **kwargs)

    def _default_settings_path(self) -> Path:
        return self.root / CANONICAL_SOURCE_RELATIVE / "001_CORE_META_MODEL" / "caprmedio_framework_default_settings.toml"

    def _instance_settings_path(self) -> Path:
        return self.root / CANONICAL_SOURCE_RELATIVE / "003_PROJECT_CONFIGURATION" / "caprmedio_framework_settings.toml"

    @staticmethod
    def _release_suite_settings(value: object, *, section: bool = True) -> bytes:
        prefix = "[release_suite]\n" if section else ""
        if isinstance(value, bytes):
            return prefix.encode() + value
        return (prefix + f"unit_timeout_seconds = {value}\n").encode()

    def canonical_testcase_count(self) -> int:
        """Read the sealed fixture's actual D579 module-rule carrier."""

        payload = json.loads((self.root / MODULE_RULES_RELATIVE).read_text(encoding="utf-8"))
        return len(payload["module_probes"])

    def bound(self, mode: str = "success", runner: str = "local-subprocess", working_directory: str = SUITE_DRIVER_WORKING_DIRECTORY,
              *, stage_package: bool = True):
        self.fixture.write(SUITE_DRIVER_RELATIVE, SCRIPT.encode())
        self.executor.mode = mode
        self.command = list(SUITE_DRIVER_COMMAND)
        preflight, candidate = build_preflight_validated_candidate(
            self.root, candidate_release="N+1",
            full_suite_environment={"runner": runner, "command": self.command, "working_directory": working_directory},
            candidate_image_reference="disposable:N+1",
        )
        self.fixture.copy_source()
        compilation = render_release_candidate(candidate, preflight)
        self._install_active_n(compilation)
        self.package = stage_framework_package(self.root, compilation) if stage_package else None
        return candidate, compilation

    def _install_active_n(self, compilation) -> None:
        """Materialize an exact retained N package and its matching public Skill.

        This is test-only setup. It models a genuine prior full Framework
        release rather than accepting a selector-only placeholder as N.
        """

        package = self.root / ".caprmedio_runtime/framework/releases/N"
        for row in compilation.package_rows:
            target = package / row.destination_path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(self.root / row.source_path, target)
            target.chmod(row.mode)
        (package / "manifest.toml").write_text(_render_manifest("N", compilation.package_rows), encoding="utf-8")
        active_skill = self.root / ".agents/skills/ca"
        if active_skill.exists():
            shutil.rmtree(active_skill)
        shutil.copytree(package / "SKILLS/ca", active_skill)

    def test_golden_suite_before_staging_preserves_active_n_and_creates_no_candidate_package_or_skill(self) -> None:
        candidate, compilation = self.bound(stage_package=False)
        releases = self.root / ".caprmedio_runtime/framework/releases"
        candidate_package = releases / candidate.manifest.sha256
        selector = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        source_sha = tree_sha256(self.root, CANONICAL_SOURCE_RELATIVE)
        compiled_sha = tree_sha256(self.root, compilation.child_materialization_root)
        n_package_sha = tree_sha256(self.root, releases / "N")
        n_skill_sha = tree_sha256(self.root, ".agents/skills/ca")
        self.assertTrue((releases / "N").is_dir())
        self.assertFalse(candidate_package.exists())
        result = self.execute_suite(candidate, compilation)
        self.assertTrue(result.passed)
        self.assertEqual(result.executed_tests, self.canonical_testcase_count())
        self.assertEqual(result.coverage, ("Agentic", "Apps", "MCP", "Methodology", "Skill", "Tools"))
        self.assertEqual(result.command, tuple(self.command))
        self.assertEqual(verify_bound_suite_evidence(candidate, compilation, result), self.root)
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector)
        self.assertEqual(tree_sha256(self.root, CANONICAL_SOURCE_RELATIVE), source_sha)
        self.assertEqual(tree_sha256(self.root, compilation.child_materialization_root), compiled_sha)
        self.assertEqual(tree_sha256(self.root, releases / "N"), n_package_sha)
        self.assertEqual(tree_sha256(self.root, ".agents/skills/ca"), n_skill_sha)
        self.assertFalse(candidate_package.exists())
        receipt = (self.root / result.evidence_root / "receipt.json").read_bytes()
        self.assertEqual(hashlib.sha256(receipt).hexdigest(), result.receipt_sha256)
        # O175 can stage these exact already-tested candidate bytes later.
        staged = stage_framework_package(self.root, compilation)
        package = self.root / staged["release_root"]
        self.assertEqual((package / "manifest.toml").read_text(), _render_manifest(candidate.manifest.sha256, compilation.package_rows))
        for row in compilation.package_rows:
            target = package / row.destination_path
            self.assertEqual(target.read_bytes(), (self.root / row.source_path).read_bytes())
            self.assertEqual(target.stat().st_mode & 0o777, row.mode)
        self.assertEqual(verify_bound_suite_evidence(candidate, compilation, result), self.root)
        self.assertEqual((self.root / result.evidence_root / "receipt.json").read_bytes(), receipt)
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector)
        self.assertEqual(tree_sha256(self.root, releases / "N"), n_package_sha)
        self.assertEqual(tree_sha256(self.root, ".agents/skills/ca"), n_skill_sha)

    def test_bound_suite_passes_the_executor_admitted_image_path(self) -> None:
        self.executor.image_path = "/verified/immutable-image/bin"
        candidate, compilation = self.bound(stage_package=False)

        result = self.execute_suite(candidate, compilation)

        self.assertTrue(result.passed)
        self.assertEqual(self.executor.last_environment["PATH"], "/verified/immutable-image/bin")

    def test_unstaged_candidate_stale_source_or_forged_rows_refuse_before_execution(self) -> None:
        candidate, compilation = self.bound(stage_package=False)
        row = compilation.package_rows[0].model_copy(update={"sha256": "f" * 64})
        forged = compilation.model_copy(update={"package_rows": [row, *compilation.package_rows[1:]]})
        with patch("release_suite.subprocess.Popen") as process:
            with self.assertRaises((ReleaseContractError, ReleasePackagingError)):
                execute_bound_release_suite(candidate, forged)
            process.assert_not_called()
        self.fixture.core.write_bytes(b"stale authority before suite")
        with patch("release_suite.subprocess.Popen") as process:
            with self.assertRaises(ReleaseContractError):
                self.execute_suite(candidate, compilation)
            process.assert_not_called()
        self.assertFalse((self.root / ".caprmedio_runtime/release_suite").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/framework/releases" / candidate.manifest.sha256).exists())

    def test_missing_active_n_package_refuses_without_process_or_candidate_package(self) -> None:
        candidate, compilation = self.bound(stage_package=False)
        releases = self.root / ".caprmedio_runtime/framework/releases"
        shutil.rmtree(releases / "N")
        with patch("release_suite.subprocess.Popen") as process:
            with self.assertRaises(ReleaseContractError):
                self.execute_suite(candidate, compilation)
            process.assert_not_called()
        self.assertFalse((releases / "N").exists())
        self.assertFalse((releases / candidate.manifest.sha256).exists())
        self.assertFalse((self.root / ".caprmedio_runtime/release_suite").exists())

    def test_incomplete_active_n_package_refuses_before_execution(self) -> None:
        candidate, compilation = self.bound(stage_package=False)
        package = self.root / ".caprmedio_runtime/framework/releases/N"
        (package / "SKILLS/ca/SKILL.md").unlink()
        with patch("release_suite.subprocess.Popen") as process:
            with self.assertRaises(ReleaseContractError):
                self.execute_suite(candidate, compilation)
            process.assert_not_called()
        self.assertFalse((package / "SKILLS/ca/SKILL.md").exists())

    def test_candidate_package_symlink_refuses_even_when_target_is_absent(self) -> None:
        candidate, compilation = self.bound(stage_package=False)
        releases = self.root / ".caprmedio_runtime/framework/releases"
        self.assertTrue(releases.is_dir())
        package = releases / candidate.manifest.sha256
        package.symlink_to(self.root / "unsealed-package", target_is_directory=True)
        with patch("release_suite.subprocess.Popen") as process:
            with self.assertRaises(ReleaseContractError):
                self.execute_suite(candidate, compilation)
            process.assert_not_called()
        self.assertTrue(package.is_symlink())
        self.assertFalse((self.root / "unsealed-package").exists())

    def test_unstaged_candidate_missing_compiled_output_refuses_before_execution(self) -> None:
        candidate, compilation = self.bound(stage_package=False)
        compiled = self.root / compilation.child_materialization_root
        next(path for path in compiled.rglob("*") if path.is_file()).unlink()
        with patch("release_suite.subprocess.Popen") as process:
            with self.assertRaises((ReleaseContractError, ReleasePackagingError)):
                self.execute_suite(candidate, compilation)
            process.assert_not_called()
        self.assertFalse((self.root / ".caprmedio_runtime/release_suite").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/framework/releases" / candidate.manifest.sha256).exists())

    def test_suite_receipt_does_not_admit_tampered_package_created_after_tests(self) -> None:
        candidate, compilation = self.bound(stage_package=False)
        result = self.execute_suite(candidate, compilation)
        self.assertTrue(result.passed)
        staged = stage_framework_package(self.root, compilation)
        (self.root / staged["release_root"] / "SKILLS/ca/SKILL.md").write_bytes(b"tampered retained Skill")
        with self.assertRaises(ReleasePackagingError):
            verify_bound_suite_evidence(candidate, compilation, result)
        self.assertTrue((self.root / ".agents/skills/ca/SKILL.md").is_file())

    def test_passing_unstaged_suite_does_not_admit_image_build_without_full_package(self) -> None:
        from release_image import build_candidate_image
        candidate, compilation = self.bound(stage_package=False)
        result = self.execute_suite(candidate, compilation)
        self.assertTrue(result.passed)
        with patch("release_image.DockerSubprocessExecutor.run") as docker:
            from release_image import DockerSubprocessExecutor
            with self.assertRaises(ReleaseContractError):
                build_candidate_image(candidate, compilation, result, executor=DockerSubprocessExecutor())
            docker.assert_not_called()
        self.assertFalse((self.root / ".caprmedio_runtime/framework/releases" / candidate.manifest.sha256).exists())
        self.assertTrue((self.root / ".agents/skills/ca/SKILL.md").is_file())

    def test_golden_actual_exact_command_complete_coverage_durable_outputs_preserves_n(self) -> None:
        candidate, compilation = self.bound()
        before = tree_sha256(self.root, CANONICAL_SOURCE_RELATIVE)
        selector = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        result = self.execute_suite(candidate, compilation)
        self.assertTrue(result.passed)
        self.assertEqual(result.outcome, "passed")
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.executed_tests, self.canonical_testcase_count())
        self.assertEqual(result.coverage, ("Agentic", "Apps", "MCP", "Methodology", "Skill", "Tools"))
        self.assertEqual(result.command, tuple(self.command))
        evidence = self.root / result.evidence_root
        phase_map = derive_test_phase_map_from_rows(compilation.package_rows)
        report = ET.fromstring((evidence / "coverage.xml").read_bytes())
        self.assertEqual(phase_map.candidate_e2e_paths, CANDIDATE_E2E_MODULES)
        self.assertEqual({case.get("classname") for case in report.iter("testcase")}, set(phase_map.unit_paths))
        self.assertEqual(report.get("caprmedio.phase"), "unit")
        self.assertEqual(report.get("caprmedio.phase_map_sha256"), phase_map.sha256)
        self.assertEqual(result.phase_map_sha256, phase_map.sha256)
        stdout = (evidence / "stdout.bin").read_bytes()
        self.assertIn(b"$HOME;$(should-stay-literal)", stdout)
        self.assertEqual(hashlib.sha256(stdout).hexdigest(), result.stdout_sha256)
        self.assertEqual(hashlib.sha256((evidence / "stderr.bin").read_bytes()).hexdigest(), result.stderr_sha256)
        self.assertEqual(hashlib.sha256((evidence / "coverage.xml").read_bytes()).hexdigest(), result.report_sha256)
        receipt = (evidence / "receipt.json").read_bytes()
        self.assertEqual(hashlib.sha256(receipt).hexdigest(), result.receipt_sha256)
        receipt_payload = json.loads(receipt)
        self.assertEqual(receipt_payload["exit_code"], 0)
        self.assertEqual(receipt_payload["executing_selector_sha256"], result.executing_selector_sha256)
        self.assertEqual(receipt_payload["executing_release_package_sha256"], result.executing_release_package_sha256)
        self.assertEqual(receipt_payload["executing_skill_sha256"], result.executing_skill_sha256)
        self.assertEqual(tree_sha256(self.root, CANONICAL_SOURCE_RELATIVE), before)
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector)
        self.assertTrue((self.root / ".agents/skills/ca/SKILL.md").is_file())
        self.assertEqual(verify_bound_suite_evidence(candidate, compilation, result), self.root)

    def test_downstream_verifier_reopens_evidence_and_refuses_forged_or_changed_receipts(self) -> None:
        candidate, compilation = self.bound()
        result = self.execute_suite(candidate, compilation)
        self.assertEqual(verify_bound_suite_evidence(candidate, compilation, result), self.root)
        with self.assertRaises(ReleaseContractError):
            verify_bound_suite_evidence(candidate, compilation, replace(result, executed_tests=999))
        with self.assertRaises(ReleaseContractError):
            verify_bound_suite_evidence(candidate, compilation, replace(result, phase_map_sha256="0" * 64))
        (self.root / result.evidence_root / "stdout.bin").write_bytes(b"changed")
        with self.assertRaises(ReleaseContractError) as raised:
            verify_bound_suite_evidence(candidate, compilation, result)
        self.assertEqual(raised.exception.code, "release-suite-evidence-mismatch")

    def test_downstream_verifier_refuses_n_skill_mutated_after_successful_suite(self) -> None:
        candidate, compilation = self.bound()
        result = self.execute_suite(candidate, compilation)
        self.assertTrue(result.passed)
        (self.root / ".agents/skills/ca/SKILL.md").write_bytes(b"changed after suite")
        with self.assertRaises(ReleaseContractError) as raised:
            verify_bound_suite_evidence(candidate, compilation, result)
        self.assertEqual(raised.exception.code, "release-suite-evidence-mismatch")

    def test_actual_nonzero_exit_never_passes_even_with_complete_report(self) -> None:
        candidate, compilation = self.bound("fail")
        result = self.execute_suite(candidate, compilation)
        self.assertEqual(result.outcome, "failed")
        self.assertEqual(result.exit_code, 17)
        self.assertFalse(result.passed)
        self.assertIsNotNone(result.receipt_sha256)

    def test_actual_timeout_retains_output_and_never_passes(self) -> None:
        candidate, compilation = self.bound("timeout")
        result = self.execute_suite(candidate, compilation, timeout_seconds=0.1)
        self.assertEqual(result.outcome, "timed_out")
        self.assertEqual(result.exit_code, -9)
        self.assertFalse(result.passed)
        self.assertEqual(self.executor.timeout_calls[-1], 0.1)
        self.assertIn(b"actual stdout", (self.root / result.evidence_root / "stdout.bin").read_bytes())

    def test_source_default_deadline_is_finite_and_propagated_to_executor(self) -> None:
        candidate, compilation = self.bound("success")
        result = self.execute_suite(candidate, compilation)
        self.assertTrue(result.passed)
        self.assertEqual(self.executor.timeout_calls, [3600])

    def test_instance_deadline_overrides_default_and_is_propagated_exactly(self) -> None:
        self.fixture.write(
            f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml",
            b"[release_suite]\nunit_timeout_seconds = 4800\n",
        )
        candidate, compilation = self.bound("success")
        result = self.execute_suite(candidate, compilation)
        self.assertTrue(result.passed)
        self.assertEqual(self.executor.timeout_calls, [4800])

    def test_missing_instance_deadline_falls_back_to_source_default(self) -> None:
        self.fixture.write(
            f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml",
            b"[interaction]\nreporting_mode = 'silent'\n",
        )
        candidate, compilation = self.bound("success")
        result = self.execute_suite(candidate, compilation)
        self.assertTrue(result.passed)
        self.assertEqual(self.executor.timeout_calls, [3600])

    def test_empty_instance_release_suite_table_falls_back_to_source_default(self) -> None:
        self.fixture.write(
            f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml",
            b"[release_suite]\n",
        )
        candidate, compilation = self.bound("success")
        result = self.execute_suite(candidate, compilation)
        self.assertTrue(result.passed)
        self.assertEqual(self.executor.timeout_calls, [3600])

    def test_invalid_source_deadline_settings_never_pass_or_invoke_executor(self) -> None:
        invalid = (
            ("malformed", self._release_suite_settings('"3600"'), "default"),
            ("bool", self._release_suite_settings("true"), "default"),
            ("nonfinite", self._release_suite_settings("nan"), "default"),
            ("huge-integer", self._release_suite_settings("1000000000000000000000000000000"), "default"),
            ("zero", self._release_suite_settings("0"), "default"),
            ("negative", self._release_suite_settings("-1"), "default"),
            ("above-hard-maximum", self._release_suite_settings("7201"), "default"),
            ("unknown-key", b"[release_suite]\nother_deadline_seconds = 3600\n", "default"),
            ("missing", b"[interaction]\nreporting_mode = 'silent'\n", "default"),
            ("instance-invalid-does-not-fallback", self._release_suite_settings("true"), "instance"),
        )
        for label, payload, carrier in invalid:
            with self.subTest(label=label):
                fixture = ReleaseSuiteTests("run")
                fixture.setUp()
                try:
                    target = fixture._default_settings_path() if carrier == "default" else fixture._instance_settings_path()
                    target.write_bytes(payload)
                    candidate, compilation = fixture.bound("success")
                    result = fixture.execute_suite(candidate, compilation)
                    self.assertFalse(result.passed)
                    self.assertEqual(fixture.executor.timeout_calls, [])
                finally:
                    fixture.doCleanups()

    def test_stale_instance_deadline_settings_never_pass(self) -> None:
        candidate, compilation = self.bound("success")
        self._instance_settings_path().write_bytes(b"[release_suite]\nunit_timeout_seconds = 4800\n")
        with self.assertRaises(ReleaseContractError) as raised:
            self.execute_suite(candidate, compilation)
        self.assertEqual(raised.exception.code, "release-currentness-stale")
        self.assertEqual(self.executor.timeout_calls, [])

    def test_explicit_fixture_timeout_can_only_shorten_source_deadline(self) -> None:
        self.fixture.write(
            f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml",
            b"[release_suite]\nunit_timeout_seconds = 4800\n",
        )
        candidate, compilation = self.bound("timeout")
        result = self.execute_suite(candidate, compilation, timeout_seconds=0.1)
        self.assertEqual(result.outcome, "timed_out")
        self.assertFalse(result.passed)
        self.assertEqual(self.executor.timeout_calls, [0.1])

    def test_explicit_fixture_timeout_cannot_lengthen_source_deadline(self) -> None:
        self.fixture.write(
            f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml",
            b"[release_suite]\nunit_timeout_seconds = 3600\n",
        )
        candidate, compilation = self.bound("success")
        result = self.execute_suite(candidate, compilation, timeout_seconds=4800)
        self.assertFalse(result.passed)
        self.assertNotEqual(result.outcome, "passed")
        self.assertEqual(self.executor.timeout_calls, [])

    def test_successful_unit_deadline_carrier_tamper_or_removal_refuses_reverification(self) -> None:
        candidate, compilation = self.bound("success")
        result = self.execute_suite(candidate, compilation)
        self.assertTrue(result.passed)
        deadline_path = self.root / result.evidence_root / "unit-deadline.json"
        original = deadline_path.read_bytes()
        for label, replacement in (("tampered", original + b"\n"), ("missing", None)):
            with self.subTest(label=label):
                try:
                    if replacement is None:
                        deadline_path.unlink()
                    else:
                        deadline_path.write_bytes(replacement)
                    with self.assertRaises(ReleaseContractError) as raised:
                        verify_bound_suite_evidence(candidate, compilation, result)
                    self.assertEqual(raised.exception.code, "release-suite-evidence-mismatch")
                finally:
                    deadline_path.write_bytes(original)

    def test_unit_deadline_settings_mode_change_refuses_before_executor(self) -> None:
        candidate, compilation = self.bound("success")
        settings_path = self._default_settings_path()
        original_mode = settings_path.stat().st_mode & 0o777
        try:
            settings_path.chmod(original_mode ^ 0o100)
            with self.assertRaises(ReleaseContractError):
                self.execute_suite(candidate, compilation)
        finally:
            settings_path.chmod(original_mode)
        self.assertEqual(self.executor.timeout_calls, [])

    def test_actual_background_descendant_cannot_continue_or_pass(self) -> None:
        candidate, compilation = self.bound("descendant")
        result = self.execute_suite(candidate, compilation)
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.outcome, "incomplete")
        self.assertIn("descendant", result.reason)
        self.assertFalse(result.passed)

    def test_unsupported_missing_engine_only_failed_skipped_inconsistent_unbound_reports_incomplete(self) -> None:
        for mode in ("unsupported", "missing", "engine-only", "compiled-omitted", "report-failure", "skipped", "summary", "unbound"):
            with self.subTest(mode=mode):
                fixture = ReleaseSuiteTests("run")
                fixture.setUp()
                try:
                    if mode == "runtime":
                        fixture.fixture.write(".caprmedio_runtime/framework/releases/N/runtime.txt", b"prior active N")
                    if mode == "skill":
                        fixture.fixture.write(".agents/skills/ca/SKILL.md", b"prior active Skill")
                    candidate, compilation = fixture.bound(mode)
                    result = fixture.execute_suite(candidate, compilation)
                    self.assertEqual(result.outcome, "incomplete")
                    self.assertEqual(result.exit_code, 0)
                    self.assertFalse(result.passed)
                    if mode == "compiled-omitted":
                        self.assertEqual(result.reason, "suite did not report compiled candidate coverage")
                finally:
                    fixture.doCleanups()

    def test_stale_source_before_execution_refuses_without_process_or_evidence(self) -> None:
        candidate, compilation = self.bound()
        self.fixture.core.write_bytes(b"stale")
        with self.assertRaises(ReleaseContractError) as raised:
            self.execute_suite(candidate, compilation)
        self.assertEqual(raised.exception.code, "release-currentness-stale")
        self.assertFalse((self.root / ".caprmedio_runtime/release_suite").exists())

    def test_incomplete_or_tampered_retained_package_refuses_before_execution(self) -> None:
        candidate, compilation = self.bound()
        (self.root / self.package["release_root"] / "SKILLS/ca/SKILL.md").unlink()
        with self.assertRaises(ReleasePackagingError) as raised:
            self.execute_suite(candidate, compilation)
        self.assertEqual(raised.exception.code, "release-collision")
        self.assertFalse((self.root / ".caprmedio_runtime/release_suite").exists())

    def test_workspace_mutation_cannot_change_authoritative_source_n_skill_or_selector(self) -> None:
        for mode in ("stale", "selection", "runtime", "skill", "settings", "journal"):
            with self.subTest(mode=mode):
                fixture = ReleaseSuiteTests("run")
                fixture.setUp()
                try:
                    candidate, compilation = fixture.bound(mode)
                    before_source = tree_sha256(fixture.root, CANONICAL_SOURCE_RELATIVE)
                    before_selector = (fixture.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
                    before_package = tree_sha256(fixture.root, ".caprmedio_runtime/framework/releases/N")
                    before_skill = tree_sha256(fixture.root, ".agents/skills/ca")
                    settings = fixture.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
                    journal = fixture.root / ".caprmedio_caprmedio/_journal/release.jsonl"
                    before_settings = settings.read_bytes()
                    self.assertFalse(journal.exists())
                    result = fixture.execute_suite(candidate, compilation)
                    self.assertEqual(result.outcome, "failed")
                    self.assertNotEqual(result.exit_code, 0)
                    self.assertFalse(result.passed)
                    self.assertIsNotNone(result.receipt_sha256)
                    workspace = fixture.root / result.evidence_root / "workspace"
                    self.assertFalse((workspace / ".git").exists())
                    self.assertFalse((workspace / ".caprmedio_runtime/framework/current.toml").exists())
                    self.assertFalse((workspace / ".caprmedio_runtime/framework/releases/N").exists())
                    self.assertFalse((workspace / ".agents/skills/ca").exists())
                    self.assertEqual(tree_sha256(fixture.root, CANONICAL_SOURCE_RELATIVE), before_source)
                    self.assertEqual((fixture.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), before_selector)
                    self.assertEqual(tree_sha256(fixture.root, ".caprmedio_runtime/framework/releases/N"), before_package)
                    self.assertEqual(tree_sha256(fixture.root, ".agents/skills/ca"), before_skill)
                    self.assertEqual(settings.read_bytes(), before_settings)
                    self.assertFalse(journal.exists())
                finally:
                    fixture.doCleanups()

    def test_missing_approved_executor_records_incomplete_and_never_runs_host_command(self) -> None:
        candidate, compilation = self.bound()
        with patch("release_suite.subprocess.Popen") as process:
            result = execute_bound_release_suite(candidate, compilation, executor=None)
        self.assertEqual(result.outcome, "incomplete")
        self.assertIn("isolated suite executor", result.reason)
        process.assert_not_called()
        self.assertFalse(result.passed)

    def test_raw_or_mismatched_typed_handoffs_are_not_authority(self) -> None:
        candidate, compilation = self.bound()
        with self.assertRaises(ReleaseContractError):
            execute_bound_release_suite(candidate, compilation.model_dump())
        forged = compilation.model_copy(update={"candidate_snapshot_manifest_sha256": "0" * 64})
        with self.assertRaises(ReleaseContractError) as raised:
            execute_bound_release_suite(candidate, forged)
        self.assertEqual(raised.exception.code, "release-suite-binding-mismatch")
        changed_intent = candidate.intent.model_copy(update={"full_suite_environment": candidate.intent.full_suite_environment.model_copy(update={"command": ["true"]})})
        with self.assertRaises(ReleaseContractError) as raised:
            execute_bound_release_suite(replace(candidate, intent=changed_intent), compilation)
        self.assertEqual(raised.exception.code, "release-currentness-stale")

    def test_unsupported_runner_and_symlinked_bound_working_directory_refuse(self) -> None:
        candidate, compilation = self.bound(runner="fixture")
        with self.assertRaises(ReleaseContractError) as raised:
            self.execute_suite(candidate, compilation)
        self.assertEqual(raised.exception.code, "release-suite-command-untrusted")
        self.fixture.doCleanups()
        self.setUp()
        candidate, compilation = self.bound(working_directory="suite-work")
        with self.assertRaises(ReleaseContractError) as raised:
            self.execute_suite(candidate, compilation)
        self.assertEqual(raised.exception.code, "release-suite-command-untrusted")

    def bound_again_in_fresh_fixture(self):
        self.fixture.doCleanups()
        self.setUp()
        return self.bound()

    def test_actual_start_failure_retains_evidence(self) -> None:
        candidate, compilation = self.bound()
        self.executor.start_error = True
        result = self.execute_suite(candidate, compilation)
        self.assertEqual(result.outcome, "failed")
        self.assertFalse(result.passed)
        self.assertIsNotNone(result.receipt_sha256)

    def test_recording_failure_after_actual_success_never_passes(self) -> None:
        candidate, compilation = self.bound()
        from release_suite import _durable_bytes

        def fail_receipt_only(path, payload):
            if Path(path).name == "receipt.json":
                raise OSError("deliberate receipt failure")
            return _durable_bytes(path, payload)

        # Context is now durably recorded before process execution.  This
        # fixture targets the intended post-success receipt failure only.
        with patch("release_suite._durable_bytes", side_effect=fail_receipt_only):
            result = self.execute_suite(candidate, compilation)
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.executed_tests, self.canonical_testcase_count())
        self.assertEqual(result.outcome, "recording_uncertain")
        self.assertFalse(result.passed)
        self.assertIsNone(result.receipt_sha256)

    def test_recording_enospc_retains_only_errno_and_never_passes(self) -> None:
        candidate, compilation = self.bound()
        from release_suite import _durable_bytes

        def fail_receipt_only(path, payload):
            if Path(path).name == "receipt.json":
                raise OSError(errno.ENOSPC, "sensitive host path must not be retained", "/private/host/path")
            return _durable_bytes(path, payload)

        with patch("release_suite._durable_bytes", side_effect=fail_receipt_only):
            result = self.execute_suite(candidate, compilation)

        self.assertEqual(result.outcome, "recording_uncertain")
        self.assertFalse(result.passed)
        self.assertIn("OSError[errno=28]", result.reason)
        self.assertNotIn("sensitive host path", result.reason)
        self.assertNotIn("/private/host/path", result.reason)


if __name__ == "__main__":
    unittest.main()
