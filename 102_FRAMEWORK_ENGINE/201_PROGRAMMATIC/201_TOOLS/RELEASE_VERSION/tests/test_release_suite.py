"""Actual disposable compiler/package/subprocess gates; no Project release proof."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_compilation import build_preflight_validated_candidate, render_release_candidate  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE, tree_sha256  # noqa: E402
from release_packaging import ReleasePackagingError, stage_framework_package  # noqa: E402
from release_suite import execute_bound_release_suite, verify_bound_suite_evidence  # noqa: E402
import test_release_compilation as compilation_test  # noqa: E402


SCRIPT = '''import os, sys, time, subprocess
from pathlib import Path
import xml.etree.ElementTree as ET
root, mode, literal = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
print("actual stdout:" + literal, flush=True)
print("actual stderr", file=sys.stderr, flush=True)
sources = [
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py",
    "102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md",
    "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md",
    %r,
]
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
if mode == "fail":
    sys.exit(17)
''' % f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/04_requirement/CA-R-001--core.md"


class ReleaseSuiteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = compilation_test.ReleaseCompilationTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        (self.root / "suite-work").mkdir()

    def bound(self, mode: str = "success", runner: str = "local-subprocess", working_directory: str = "suite-work"):
        script = self.fixture.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/suite_command.py", SCRIPT.encode())
        self.command = [sys.executable, str(script), str(self.root), mode, "$HOME;$(should-stay-literal)"]
        preflight, candidate = build_preflight_validated_candidate(
            self.root, candidate_release="N+1",
            full_suite_environment={"runner": runner, "command": self.command, "working_directory": working_directory},
            candidate_image_reference="disposable:N+1",
        )
        self.fixture.copy_source()
        compilation = render_release_candidate(candidate, preflight)
        self.package = stage_framework_package(self.root, compilation)
        return candidate, compilation

    def test_golden_actual_exact_command_complete_coverage_durable_outputs_preserves_n(self) -> None:
        candidate, compilation = self.bound()
        before = tree_sha256(self.root, CANONICAL_SOURCE_RELATIVE)
        selector = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        result = execute_bound_release_suite(candidate, compilation)
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
        self.assertEqual(json.loads(receipt)["exit_code"], 0)
        self.assertEqual(tree_sha256(self.root, CANONICAL_SOURCE_RELATIVE), before)
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector)
        self.assertFalse((self.root / ".agents/skills/ca").exists())
        self.assertEqual(verify_bound_suite_evidence(candidate, compilation, result), self.root)

    def test_downstream_verifier_reopens_evidence_and_refuses_forged_or_changed_receipts(self) -> None:
        candidate, compilation = self.bound()
        result = execute_bound_release_suite(candidate, compilation)
        self.assertEqual(verify_bound_suite_evidence(candidate, compilation, result), self.root)
        with self.assertRaises(ReleaseContractError):
            verify_bound_suite_evidence(candidate, compilation, replace(result, executed_tests=999))
        (self.root / result.evidence_root / "stdout.bin").write_bytes(b"changed")
        with self.assertRaises(ReleaseContractError) as raised:
            verify_bound_suite_evidence(candidate, compilation, result)
        self.assertEqual(raised.exception.code, "release-suite-evidence-mismatch")

    def test_actual_nonzero_exit_never_passes_even_with_complete_report(self) -> None:
        candidate, compilation = self.bound("fail")
        result = execute_bound_release_suite(candidate, compilation)
        self.assertEqual(result.outcome, "failed")
        self.assertEqual(result.exit_code, 17)
        self.assertFalse(result.passed)
        self.assertIsNotNone(result.receipt_sha256)

    def test_actual_timeout_retains_output_and_never_passes(self) -> None:
        candidate, compilation = self.bound("timeout")
        result = execute_bound_release_suite(candidate, compilation, timeout_seconds=0.1)
        self.assertEqual(result.outcome, "timed_out")
        self.assertEqual(result.exit_code, -9)
        self.assertFalse(result.passed)
        self.assertIn(b"actual stdout", (self.root / result.evidence_root / "stdout.bin").read_bytes())

    def test_actual_background_descendant_cannot_continue_or_pass(self) -> None:
        candidate, compilation = self.bound("descendant")
        result = execute_bound_release_suite(candidate, compilation)
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.outcome, "incomplete")
        self.assertIn("descendant", result.reason)
        self.assertFalse(result.passed)

    def test_unsupported_missing_engine_only_failed_skipped_inconsistent_unbound_reports_incomplete(self) -> None:
        for mode in ("unsupported", "missing", "engine-only", "report-failure", "skipped", "summary", "unbound"):
            with self.subTest(mode=mode):
                fixture = ReleaseSuiteTests("run")
                fixture.setUp()
                try:
                    candidate, compilation = fixture.bound(mode)
                    result = execute_bound_release_suite(candidate, compilation)
                    self.assertEqual(result.outcome, "incomplete")
                    self.assertEqual(result.exit_code, 0)
                    self.assertFalse(result.passed)
                finally:
                    fixture.doCleanups()

    def test_stale_source_before_execution_refuses_without_process_or_evidence(self) -> None:
        candidate, compilation = self.bound()
        self.fixture.core.write_bytes(b"stale")
        with self.assertRaises(ReleaseContractError) as raised:
            execute_bound_release_suite(candidate, compilation)
        self.assertEqual(raised.exception.code, "release-currentness-stale")
        self.assertFalse((self.root / ".caprmedio_runtime/release_suite").exists())

    def test_incomplete_or_tampered_retained_package_refuses_before_execution(self) -> None:
        candidate, compilation = self.bound()
        (self.root / self.package["release_root"] / "SKILLS/ca/SKILL.md").unlink()
        with self.assertRaises(ReleasePackagingError) as raised:
            execute_bound_release_suite(candidate, compilation)
        self.assertEqual(raised.exception.code, "release-collision")
        self.assertFalse((self.root / ".caprmedio_runtime/release_suite").exists())

    def test_actual_source_mutation_and_selection_change_make_gate_stale(self) -> None:
        for mode in ("stale", "selection"):
            with self.subTest(mode=mode):
                fixture = ReleaseSuiteTests("run")
                fixture.setUp()
                try:
                    candidate, compilation = fixture.bound(mode)
                    result = execute_bound_release_suite(candidate, compilation)
                    self.assertEqual(result.outcome, "stale")
                    self.assertFalse(result.passed)
                    self.assertIsNotNone(result.receipt_sha256)
                finally:
                    fixture.doCleanups()

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
            execute_bound_release_suite(candidate, compilation)
        self.assertEqual(raised.exception.code, "release-suite-runner-unsupported")
        candidate, compilation = self.bound_again_in_fresh_fixture()
        (self.root / "suite-work").rmdir()
        (self.root / "suite-work").symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ReleaseContractError) as raised:
            execute_bound_release_suite(candidate, compilation)
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
        stage_framework_package(self.root, compilation)
        result = execute_bound_release_suite(candidate, compilation)
        self.assertEqual(result.outcome, "failed")
        self.assertFalse(result.passed)
        self.assertIsNotNone(result.receipt_sha256)

    def test_recording_failure_after_actual_success_never_passes(self) -> None:
        candidate, compilation = self.bound()
        with patch("release_suite._durable_bytes", side_effect=OSError("deliberate receipt failure")):
            result = execute_bound_release_suite(candidate, compilation)
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.executed_tests, 6)
        self.assertEqual(result.outcome, "recording_uncertain")
        self.assertFalse(result.passed)
        self.assertIsNone(result.receipt_sha256)


if __name__ == "__main__":
    unittest.main()
