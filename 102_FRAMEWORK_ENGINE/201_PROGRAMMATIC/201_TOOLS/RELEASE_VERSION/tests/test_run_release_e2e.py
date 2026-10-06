"""Black-box behavior coverage for the closed candidate-E2E driver."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from run_release_e2e import main  # noqa: E402


HARNESS_ROOT = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests"
HARNESS_PATHS = (
    f"{HARNESS_ROOT}/test_docker_e2e.py",
    f"{HARNESS_ROOT}/test_selected_workflows_docker_e2e.py",
    f"{HARNESS_ROOT}/test_selected_query_mcp_e2e.py",
)
GOLDEN = Path(__file__).with_name("release_e2e_driver_golden")
IMAGE = "sha256:" + "a" * 64


class ReleaseE2EDriverTests(unittest.TestCase):
    def setUp(self) -> None:
        retained = Path.cwd() / ".caprmedio_tmp/release-e2e-driver"
        retained.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="case-", dir=retained))
        self.scratch = self.root / "scratch"
        self.report_root = self.scratch / "reports"
        self.report_root.mkdir(parents=True)
        self.context_path = self.scratch / "context.json"
        self._write_context()

    def _write_context(self) -> None:
        harnesses = []
        for path in HARNESS_PATHS:
            pattern = Path(path).name
            optins = ({"CAPRMEDIO_DOCKER_E2E": "1"} if path != HARNESS_PATHS[2] else {
                "CAPRMEDIO_DOCKER_QUERY_E2E": "1",
                "CAPRMEDIO_DOCKER_QUERY_IMAGE": IMAGE,
                "CAPRMEDIO_IMAGE": IMAGE,
            })
            harnesses.append({
                "source_path": path,
                "start_directory": HARNESS_ROOT,
                "pattern": pattern,
                "junit_path": str(self.report_root / f"{pattern}.xml"),
                "context_optins": optins,
            })
        payload = {
            "schema_version": 1,
            "source_root": str(self.root),
            "scratch_root": str(self.scratch),
            "report_root": str(self.report_root),
            "candidate_snapshot_manifest_sha256": "b" * 64,
            "candidate_image_digest": IMAGE,
            "grammar_sha256": "c" * 64,
            "phase_map_sha256": "d" * 64,
            "fixed_harnesses": harnesses,
            "phase_bindings": ["image-inspect", *(Path(path).name for path in HARNESS_PATHS)],
        }
        self.context_path.write_bytes(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode())

    def _install(self, golden_name: str, *, harness: str = HARNESS_PATHS[0]) -> None:
        target = self.root / harness
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(GOLDEN / golden_name, target)

    @contextmanager
    def _driver_environment(self):
        values = {"CAPRMEDIO_RELEASE_E2E_CONTEXT": str(self.context_path), "CAPRMEDIO_CANDIDATE_IMAGE_DIGEST": IMAGE}
        previous = Path.cwd()
        try:
            os.chdir(self.root)
            with patch.dict(os.environ, values, clear=False):
                yield
        finally:
            os.chdir(previous)

    def _invoke(self, *, harness: str = HARNESS_PATHS[0], junit: Path | None = None, cwd: bool = True) -> int:
        output = junit or self.report_root / f"{Path(harness).name}.xml"
        args = ["--start-directory", HARNESS_ROOT, "--pattern", Path(harness).name, "--junit", str(output)]
        # The actual driver process is fresh for each sealed phase.  Keep this
        # in-process main() exercise equivalent instead of reusing a previous
        # disposable module under the same declared harness basename.
        sys.modules.pop(Path(harness).stem, None)
        if cwd:
            with self._driver_environment():
                return main(args)
        with patch.dict(os.environ, {"CAPRMEDIO_RELEASE_E2E_CONTEXT": str(self.context_path), "CAPRMEDIO_CANDIDATE_IMAGE_DIGEST": IMAGE}, clear=False):
            return main(args)

    def _report(self, harness: str = HARNESS_PATHS[0]) -> ET.Element:
        return ET.fromstring((self.report_root / f"{Path(harness).name}.xml").read_bytes())

    def test_terminal_success_is_real_unittest_junit(self) -> None:
        self._install("fixture_success.py")
        self.assertEqual(self._invoke(), 0)
        report = self._report()
        self.assertEqual(report.attrib, {"name": "caprmedio.release_e2e", "tests": "1", "failures": "0", "errors": "0", "skipped": "0"})
        self.assertEqual(len(report.findall("testcase")), 1)

    def test_failure_error_and_skip_are_terminal_nonpass_junit_cases(self) -> None:
        self._install("fixture_terminal_cases.py")
        self.assertEqual(self._invoke(), 1)
        report = self._report()
        self.assertEqual((report.get("tests"), report.get("failures"), report.get("errors"), report.get("skipped")), ("4", "1", "1", "1"))
        self.assertEqual(len(report.findall(".//failure")), 1)
        self.assertEqual(len(report.findall(".//error")), 1)
        self.assertEqual(len(report.findall(".//skipped")), 1)

    def test_zero_discovery_is_nonpassing_junit(self) -> None:
        self._install("fixture_zero_discovery.py")
        self.assertEqual(self._invoke(), 1)
        self.assertEqual(self._report().get("tests"), "0")

    def test_load_tests_exception_is_serialized_as_junit_error(self) -> None:
        self._install("fixture_load_tests_error.py")
        self.assertEqual(self._invoke(), 1)
        report = self._report()
        self.assertEqual(report.get("tests"), "1")
        self.assertEqual(report.get("errors"), "1")
        self.assertEqual(len(report.findall(".//error")), 1)

    def test_duplicate_case_identity_is_visible_in_actual_junit(self) -> None:
        self._install("fixture_duplicate_cases.py")
        self.assertNotEqual(self._invoke(), 0, "duplicate JUnit testcase identity must not pass the sealed E2E phase")
        cases = self._report().findall("testcase")
        self.assertEqual(len(cases), 2)
        self.assertEqual(len({(case.get("classname"), case.get("name")) for case in cases}), 1)

    def test_context_rejects_wrong_cwd_before_junit_creation(self) -> None:
        self._install("fixture_success.py")
        self.assertEqual(self._invoke(cwd=False), 2)
        self.assertFalse((self.report_root / "test_docker_e2e.py.xml").exists())

    def test_context_rejects_candidate_image_environment_mismatch_before_junit_creation(self) -> None:
        self._install("fixture_success.py")
        output = self.report_root / "test_docker_e2e.py.xml"
        args = ["--start-directory", HARNESS_ROOT, "--pattern", "test_docker_e2e.py", "--junit", str(output)]
        with self._driver_environment(), patch.dict(
            os.environ, {"CAPRMEDIO_CANDIDATE_IMAGE_DIGEST": "sha256:" + "e" * 64}, clear=False,
        ):
            self.assertEqual(main(args), 2)
        self.assertFalse(output.exists())

    def test_context_rejects_nonfixed_harness_or_junit_destination(self) -> None:
        self._install("fixture_success.py")
        wrong = self.report_root / "other.xml"
        self.assertEqual(self._invoke(junit=wrong), 2)
        self.assertFalse(wrong.exists())
