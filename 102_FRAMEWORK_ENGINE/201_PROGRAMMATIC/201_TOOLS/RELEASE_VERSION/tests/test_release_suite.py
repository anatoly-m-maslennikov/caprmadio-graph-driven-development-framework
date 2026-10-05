"""Actual disposable compiler/package/subprocess gates; no Project release proof."""

from __future__ import annotations

import hashlib
import json
import os
import signal
import shutil
import subprocess
import sys
import unittest
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_compilation import build_preflight_validated_candidate, render_release_candidate  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE, tree_sha256  # noqa: E402
from release_inventory import ReleaseInventoryError  # noqa: E402
from release_packaging import ReleasePackagingError, _render_manifest, stage_framework_package  # noqa: E402
from release_suite import (  # noqa: E402
    CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE,
    COMPILED_ROOT_ENVIRONMENT_VARIABLE,
    PROJECT_ROOT_ENVIRONMENT_VARIABLE,
    REPORT_ENVIRONMENT_VARIABLE,
    SuiteExecutionResult,
    _refuse_secret_relative,
    _suite_process_environment,
    execute_bound_release_suite,
    verify_bound_suite_evidence,
)
import test_release_compilation as compilation_test  # noqa: E402


SCRIPT = '''import os, sys, time, subprocess
from pathlib import Path
import xml.etree.ElementTree as ET
root, mode, literal = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
compiled_root = root / os.environ["CAPRMEDIO_RELEASE_COMPILED_CANDIDATE_ROOT"]
assert compiled_root.is_dir()
assert compiled_root.name == os.environ["CAPRMEDIO_RELEASE_CANDIDATE_MANIFEST_SHA256"]
print("actual stdout:" + literal, flush=True)
print("actual stderr", file=sys.stderr, flush=True)
sources = [
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py",
    "102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md",
    "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md",
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-001--core.md",
]
sources.extend(
    path.relative_to(root).as_posix()
    for path in sorted(compiled_root.rglob("*"))
    if path.is_file()
)
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
    sources = sources[:3]
if mode == "compiled-omitted":
    sources = [source for source in sources if not source.startswith(os.environ["CAPRMEDIO_RELEASE_COMPILED_CANDIDATE_ROOT"] + "/")]
report = ET.Element("testsuite", tests=str(len(sources)), failures="0", errors="0", skipped="0")
for source in sources:
    assert (root / source).is_file()
    assert (root / source).read_bytes()
    case = ET.SubElement(report, "testcase", name="read actual " + source)
    props = ET.SubElement(case, "properties")
    ET.SubElement(props, "property", name="caprmedio.covered_source", value=source)
if mode == "report-failure":
    ET.SubElement(case, "failure", message="deliberate failure")
if mode == "skipped":
    ET.SubElement(case, "skipped")
if mode == "summary":
    report.set("tests", "999")
if mode == "unbound":
    props[0].set("value", "unsealed.py")
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
    journal.write_text('{"forged":true}\n')
if mode == "fail":
    sys.exit(17)
'''


class FixtureSandboxExecutor:
    """Test-only local stand-in for the production isolated executor.

    It rewrites fixture-root argv paths into the disposable workspace.  This
    proves that attempts to mutate a selector, retained N, or public Skill
    reach only the workspace; production never installs this executor.
    """

    def __init__(self, root: Path):
        self.root = root

    def run(self, command, *, workspace, output_root, working_directory, environment, timeout_seconds):
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
        stdout_path, stderr_path = output_root / "fixture.stdout", output_root / "fixture.stderr"
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
        return SuiteExecutionResult(exit_code, stdout_path.read_bytes(), stderr_path.read_bytes(), timed_out, left_descendants)


class ReleaseSuiteBoundaryTests(unittest.TestCase):
    """No-fixture boundary checks for the process and secret-read policies."""

    def test_suite_process_environment_is_exact_and_has_no_ambient_identity_or_credentials(self) -> None:
        root = Path("/sealed/project")
        report = Path("/sealed/project/.caprmedio_runtime/release_suite/coverage.xml")
        compilation = SimpleNamespace(child_materialization_root="sealed/compiled")
        candidate = SimpleNamespace(manifest=SimpleNamespace(sha256="a" * 64))

        environment = _suite_process_environment(root, report, compilation, candidate)

        self.assertEqual(
            environment,
            {
                "PATH": os.defpath,
                PROJECT_ROOT_ENVIRONMENT_VARIABLE: str(root),
                REPORT_ENVIRONMENT_VARIABLE: str(report),
                COMPILED_ROOT_ENVIRONMENT_VARIABLE: "sealed/compiled",
                CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE: "a" * 64,
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
        # Every test suite invocation explicitly receives this approved
        # disposable executor.  The production path has no host-process or
        # implicit global-executor fallback.
        self.executor = FixtureSandboxExecutor(self.root)
        (self.root / "suite-work").mkdir()

    def execute_suite(self, candidate, compilation, *, timeout_seconds: float = 900):
        return execute_bound_release_suite(
            candidate, compilation, executor=self.executor, timeout_seconds=timeout_seconds,
        )

    def bound(self, mode: str = "success", runner: str = "local-subprocess", working_directory: str = "suite-work",
              *, stage_package: bool = True):
        script = self.fixture.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/suite_command.py", SCRIPT.encode())
        self.command = [sys.executable, str(script), str(self.root), mode, "$HOME;$(should-stay-literal)"]
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
        self.assertEqual(result.executed_tests, 6)
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
        self.assertEqual(result.executed_tests, 6)
        self.assertEqual(result.coverage, ("Agentic", "Apps", "MCP", "Methodology", "Skill", "Tools"))
        self.assertEqual(result.command, tuple(self.command))
        evidence = self.root / result.evidence_root
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
        self.assertEqual(raised.exception.code, "release-active-n-invalid")

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
        self.assertIn(b"actual stdout", (self.root / result.evidence_root / "stdout.bin").read_bytes())

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
                    self.assertEqual(result.outcome, "passed")
                    self.assertTrue(result.passed)
                    self.assertIsNotNone(result.receipt_sha256)
                    workspace = fixture.root / result.evidence_root / "workspace"
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
        self.assertEqual(raised.exception.code, "release-suite-runner-unsupported")
        candidate, compilation = self.bound_again_in_fresh_fixture()
        (self.root / "suite-work").rmdir()
        (self.root / "suite-work").symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ReleaseContractError) as raised:
            self.execute_suite(candidate, compilation)
        self.assertEqual(raised.exception.code, "release-suite-path-unsafe")

    def bound_again_in_fresh_fixture(self):
        self.fixture.doCleanups()
        self.setUp()
        return self.bound()

    def test_actual_start_failure_retains_evidence(self) -> None:
        self.command = ["/definitely/missing/release-suite-executable"]
        preflight, candidate = build_preflight_validated_candidate(
            self.root, candidate_release="N+1",
            full_suite_environment={"runner": "local-subprocess", "command": self.command, "working_directory": "suite-work"},
            candidate_image_reference="disposable:N+1",
        )
        self.fixture.copy_source()
        compilation = render_release_candidate(candidate, preflight)
        self._install_active_n(compilation)
        stage_framework_package(self.root, compilation)
        result = self.execute_suite(candidate, compilation)
        self.assertEqual(result.outcome, "failed")
        self.assertFalse(result.passed)
        self.assertIsNotNone(result.receipt_sha256)

    def test_recording_failure_after_actual_success_never_passes(self) -> None:
        candidate, compilation = self.bound()
        with patch("release_suite._durable_bytes", side_effect=OSError("deliberate receipt failure")):
            result = self.execute_suite(candidate, compilation)
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.executed_tests, 6)
        self.assertEqual(result.outcome, "recording_uncertain")
        self.assertFalse(result.passed)
        self.assertIsNone(result.receipt_sha256)


if __name__ == "__main__":
    unittest.main()
