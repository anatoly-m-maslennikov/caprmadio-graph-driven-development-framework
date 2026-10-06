"""Golden, subprocess-level contract tests for the Release full-suite driver.

The fixture project is deliberately copied into a disposable input tree.  The
driver receives only D579's sealed environment variables.  Its private fixture
seam exists solely because the production CLI admits only fixed container paths.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import xml.etree.ElementTree as ET


RELEASE_VERSION_ROOT = Path(__file__).resolve().parent.parent
RUNNER = RELEASE_VERSION_ROOT / "run_release_suite.py"
GOLDEN_ROOT = Path(__file__).with_name("full_suite_golden")
ENGINE_ROOT = "102_FRAMEWORK_ENGINE"
RULE_PATH = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/"
    "release_suite_bindings.json"
)
CANDIDATE_PATH = f"{ENGINE_ROOT}/299_COMPILED_CANDIDATE/candidate.json"
COMPILED_CANDIDATE_PATHS = (
    f"{ENGINE_ROOT}/299_COMPILED_CANDIDATE/000_first.json",
    CANDIDATE_PATH,
)
COMPILED_PROBE_PATH = COMPILED_CANDIDATE_PATHS[0]
CASKILL_PATHS = ("SKILLS/ca/SKILL.md", "SKILLS/ca/agents/openai.yaml")
COMPILATION_TEST_PATH = f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/tests/test_release_compilation.py"
DEFAULT_EXTRA_PROBE = f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/tool_probe.py"
MODULE_PROBES = {
    f"{ENGINE_ROOT}/101_METHODOLOGY/test_methodology.py": ["METHODOLOGY/methodology_probe.md"],
    f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/test_tools.py": [
        f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/tool_probe.py",
    ],
    COMPILATION_TEST_PATH: [f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/tool_probe.py"],
    f"{ENGINE_ROOT}/202_AGENTIC/test_agentic.py": [f"{ENGINE_ROOT}/202_AGENTIC/agentic_probe.py"],
    f"{ENGINE_ROOT}/201_PROGRAMMATIC/203_APPS/test_apps.py": [f"{ENGINE_ROOT}/201_PROGRAMMATIC/203_APPS/app_probe.py"],
    f"{ENGINE_ROOT}/201_PROGRAMMATIC/204_MCP/test_mcp.py": [f"{ENGINE_ROOT}/201_PROGRAMMATIC/204_MCP/mcp_probe.py"],
    f"{ENGINE_ROOT}/206_SKILL/test_skill.py": list(CASKILL_PATHS),
}
CANDIDATE_DIGEST = "a" * 64

sys.path.insert(0, str(RELEASE_VERSION_ROOT))
import run_release_suite as suite_driver  # noqa: E402
from release_test_phases import (  # noqa: E402
    CANDIDATE_E2E_MODULES,
    ReleaseTestPhaseMap,
    derive_test_phase_map_from_rows,
)
from release_suite_reference_context import capture_context  # noqa: E402
from full_suite_golden.control_fixture import copy_control_closure  # noqa: E402


REPOSITORY = RELEASE_VERSION_ROOT.parents[3]
CONTROL_BINDINGS = {
    "candidate_snapshot_manifest_sha256": CANDIDATE_DIGEST,
    "compiled_candidate_root": f"{ENGINE_ROOT}/299_COMPILED_CANDIDATE",
    "selected_n_identity": "golden-selected-n",
    "selected_n_image_context": "sha256:" + "b" * 64,
}


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _materialize_golden_test_payloads(project_root: Path) -> None:
    """Restore declared test names only in the disposable golden Project."""

    for fixture in sorted(project_root.rglob("fixture_test_*.py")):
        target = fixture.with_name(fixture.name.removeprefix("fixture_"))
        if target.exists():
            raise AssertionError(f"golden payload target already exists: {target}")
        fixture.rename(target)


def _golden_case(name: str) -> Path:
    return GOLDEN_ROOT / "cases" / f"fixture_{name}"


class ReleaseSuiteGoldenCorpusTests(unittest.TestCase):
    """Stored fixtures must not be mistaken for declared Framework tests."""

    def test_stored_payloads_are_not_declared_test_modules(self) -> None:
        self.assertEqual(list(GOLDEN_ROOT.rglob("test_*.py")), [])
        self.assertEqual(len(list(GOLDEN_ROOT.rglob("fixture_test_*.py"))), 17)


class ReleaseSuiteUnitPartitionTests(unittest.TestCase):
    """The isolated suite process may not execute host-gated candidate E2E rows."""

    def test_execute_bound_runs_only_sealed_unit_paths_and_marks_unit_report(self) -> None:
        unit_path = f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/test_tools.py"
        phase_rows = tuple(
            sorted(
                [(unit_path, "a" * 64, "unit")]
                + [(path, "b" * 64, "candidate_e2e") for path in CANDIDATE_E2E_MODULES]
            )
        )
        phase_map = ReleaseTestPhaseMap(
            rows=phase_rows,
            sha256=hashlib.sha256(_canonical_json(list(phase_rows))).hexdigest(),
            unit_paths=(unit_path,),
            candidate_e2e_paths=tuple(sorted(CANDIDATE_E2E_MODULES)),
        )
        scratch = Path(tempfile.mkdtemp(prefix="caprmedio-unit-partition-"))
        inputs = suite_driver.BoundInputs(
            root=scratch,
            compiled_root=f"{ENGINE_ROOT}/299_COMPILED_CANDIDATE",
            candidate_manifest_sha256=CANDIDATE_DIGEST,
            report_path=scratch / "coverage.xml",
            envelope_sha256="c" * 64,
            rows={},
            reference_rows=(),
            control_context_digest="d" * 64,
            phase_map=phase_map,
            probes=suite_driver.ModuleProbeRules("rules.json", "e" * 64, {}),
        )
        invoked: list[str] = []

        def record_module(_inputs, module_path, _results_root):
            invoked.append(module_path)
            return [], []

        with mock.patch.object(suite_driver, "_run_module", side_effect=record_module):
            self.assertEqual(suite_driver._execute_bound(inputs), 1)

        self.assertEqual(invoked, [unit_path])
        report = ET.parse(inputs.report_path).getroot()
        self.assertEqual(report.get("caprmedio.phase"), "unit")
        self.assertEqual(report.get("caprmedio.phase_map_sha256"), phase_map.sha256)


class ReleaseSuiteGoldenTests(unittest.TestCase):
    """Exercise complete source discovery and JUnit evidence via the CLI only."""

    maxDiff = None

    def setUp(self) -> None:
        self.scratch = Path(tempfile.mkdtemp(prefix="caprmedio-release-suite-golden-"))
        self.project_root = self.scratch / "project"
        self.output_root = self.scratch / "output"
        self.candidate_root = self.project_root / ENGINE_ROOT / "299_COMPILED_CANDIDATE"
        shutil.copytree(GOLDEN_ROOT / "project", self.project_root)
        _materialize_golden_test_payloads(self.project_root)
        # The disposable selector binds the accepted D572 graph using actual
        # retained source bytes.  Capture/validation still run the real D580
        # reader against this Project, without requiring a fresh live selector.
        copy_control_closure(REPOSITORY, self.project_root)
        self.output_root.mkdir()

    def _control_context(self):
        """Capture this fixture's actual selected-source closure, not caller rows."""
        return capture_context(self.project_root, CONTROL_BINDINGS)

    def _test_paths(self) -> list[str]:
        return sorted(
            path.relative_to(self.project_root).as_posix()
            for path in self.project_root.glob(f"{ENGINE_ROOT}/**/test_*.py")
        )

    def _write_rules_and_envelope(
        self,
        *,
        probes: dict[str, list[str]] | None = None,
        compiled_candidate_flags: dict[str, object] | None = None,
        package_rows: list[dict[str, object]] | None = None,
        reference_rows: list[dict[str, object]] | None = None,
        control_context_digest: str | None = None,
        envelope_override: object | None = None,
    ) -> tuple[Path, Path, str]:
        test_paths = self._test_paths()
        if probes is None:
            probes = {path: MODULE_PROBES.get(path, [DEFAULT_EXTRA_PROBE]) for path in test_paths}
        if compiled_candidate_flags is None:
            compiled_candidate_flags = {COMPILATION_TEST_PATH: True}

        rule_carrier = self.project_root / RULE_PATH
        rule_carrier.parent.mkdir(parents=True, exist_ok=True)
        rule_carrier.write_bytes(
            _canonical_json(
                {
                    "schema_version": 1,
                    "module_probes": [
                        {
                            "test_module_source_path": test_path,
                            "source_paths": probes[test_path],
                            **(
                                {"compiled_candidate_probe": compiled_candidate_flags[test_path]}
                                if test_path in compiled_candidate_flags
                                else {}
                            ),
                        }
                        for test_path in test_paths
                    ],
                }
            )
        )

        if package_rows is None:
            package_paths = sorted(
                set(
                    test_paths
                    + [probe for module_probes in MODULE_PROBES.values() for probe in module_probes]
                    + [*COMPILED_CANDIDATE_PATHS, RULE_PATH, *CASKILL_PATHS]
                )
            )
            package_rows = [
                {
                    "resource": (
                        "METHODOLOGY"
                        if source_path in COMPILED_CANDIDATE_PATHS
                        else "SKILL"
                        if source_path in CASKILL_PATHS
                        else "FRAMEWORK_ENGINE"
                    ),
                    "source_path": source_path,
                    "destination_path": (
                        f"METHODOLOGY/compiled/{Path(source_path).name}"
                        if source_path in COMPILED_CANDIDATE_PATHS
                        else source_path
                        if source_path in CASKILL_PATHS
                        else f"METHODOLOGY/{Path(source_path).name}"
                        if source_path.startswith("METHODOLOGY/")
                        else f"FRAMEWORK_ENGINE/{source_path.removeprefix(f'{ENGINE_ROOT}/')}"
                    ),
                    "sha256": _sha256(self.project_root / source_path),
                    "mode": 0o644,
                }
                for source_path in package_paths
            ]

        context = self._control_context()
        envelope: object = {
            "schema_version": 2,
            "candidate_snapshot_manifest_sha256": CANDIDATE_DIGEST,
            "mapping_rules": {
                "source_path": RULE_PATH,
                "sha256": _sha256(rule_carrier),
            },
            "package_rows": package_rows,
            "reference_rows": (
                reference_rows
                if reference_rows is not None
                else [row.as_dict() for row in context.reference_rows]
            ),
            "control_context_digest": (
                control_context_digest
                if control_context_digest is not None
                else context.control_context_digest
            ),
        }
        if envelope_override is not None:
            envelope = envelope_override

        envelope_path = self.project_root / ".caprmedio_release" / "source_bindings.json"
        envelope_path.parent.mkdir(parents=True, exist_ok=True)
        encoded = _canonical_json(envelope)
        envelope_path.write_bytes(encoded)
        return rule_carrier, envelope_path, hashlib.sha256(encoded).hexdigest()

    def _fixture_environment(
        self,
        *,
        envelope_path: Path,
        envelope_sha256: str,
        report_path: Path,
        include_report: bool,
    ) -> dict[str, str]:
        environment = os.environ.copy()
        environment.update(
            {
                "CAPRMEDIO_RELEASE_PROJECT_ROOT": str(self.project_root),
                "CAPRMEDIO_RELEASE_COMPILED_CANDIDATE_ROOT": str(self.candidate_root.relative_to(self.project_root)),
                "CAPRMEDIO_RELEASE_CANDIDATE_MANIFEST_SHA256": CANDIDATE_DIGEST,
                "CAPRMEDIO_RELEASE_SOURCE_BINDINGS": str(envelope_path),
                "CAPRMEDIO_RELEASE_SOURCE_BINDINGS_SHA256": envelope_sha256,
            }
        )
        if include_report:
            environment["CAPRMEDIO_RELEASE_SUITE_REPORT"] = str(report_path)
        else:
            environment.pop("CAPRMEDIO_RELEASE_SUITE_REPORT", None)
        return environment

    def _run(
        self,
        *,
        report_path: Path | None = None,
        envelope_sha256: str | None = None,
        include_report: bool = True,
        make_workspace_read_only: bool = False,
        preserve_bindings: bool = False,
    ) -> tuple[subprocess.CompletedProcess[str], Path]:
        envelope_path = self.project_root / ".caprmedio_release" / "source_bindings.json"
        if preserve_bindings:
            self.assertTrue(envelope_path.is_file(), "the test must prepare its sealed binding envelope")
            calculated_sha256 = _sha256(envelope_path)
        else:
            _, envelope_path, calculated_sha256 = self._write_rules_and_envelope()
        if envelope_sha256 is None:
            envelope_sha256 = calculated_sha256
        report_path = report_path or self.output_root / "coverage.xml"
        environment = self._fixture_environment(
            envelope_path=envelope_path,
            envelope_sha256=envelope_sha256,
            report_path=report_path,
            include_report=include_report,
        )

        if make_workspace_read_only:
            for path in sorted(self.project_root.rglob("*"), reverse=True):
                if path.is_dir():
                    path.chmod(stat.S_IREAD | stat.S_IEXEC)
            # Retain the sealed file modes: schema-2 checks attest them.  A
            # non-writable directory still proves the driver writes reports
            # only to its separate output scratch.
            self.project_root.chmod(stat.S_IREAD | stat.S_IEXEC)

        try:
            result = subprocess.CompletedProcess(("fixture",), suite_driver._run_fixture_frame(environment), "", "")
        except (KeyError, OSError, ValueError, suite_driver.SuiteError) as error:
            result = subprocess.CompletedProcess(("fixture",), 1, "", str(error))
        return result, report_path

    def _run_public_cli(self, environment: dict[str, str]) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(RUNNER)],
            cwd=self.project_root,
            env=environment,
            text=True,
            capture_output=True,
            check=False,
        )

    def _assert_non_passing(self, result: subprocess.CompletedProcess[str]) -> None:
        self.assertNotEqual(result.returncode, 0, msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}")

    def _junit_cases(self, report_path: Path) -> dict[str, list[ET.Element]]:
        self.assertTrue(report_path.is_file(), "the driver must emit its declared JUnit report")
        root = ET.parse(report_path).getroot()
        cases = root.findall(".//testcase")
        by_identifier: dict[str, list[ET.Element]] = {}
        for case in cases:
            properties = {
                item.get("name"): item.get("value")
                for item in case.findall("./properties/property")
            }
            test_id = properties.get("caprmedio.test_id")
            self.assertIsNotNone(test_id, "each JUnit row must carry its discovered unittest ID")
            by_identifier.setdefault(test_id or "", []).append(case)
        return by_identifier

    def test_complete_six_group_suite_passes_with_one_attested_row_per_case(self) -> None:
        result, report_path = self._run()

        self.assertEqual(result.returncode, 0, msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}")
        context = self._control_context()
        envelope = json.loads((self.project_root / ".caprmedio_release/source_bindings.json").read_text(encoding="utf-8"))
        self.assertEqual(envelope["schema_version"], 2)
        self.assertEqual(envelope["reference_rows"], [row.as_dict() for row in context.reference_rows])
        self.assertEqual(envelope["control_context_digest"], context.control_context_digest)
        self.assertEqual(
            ET.parse(report_path).getroot().get("caprmedio.control_context_digest"),
            context.control_context_digest,
        )
        phase_map = derive_test_phase_map_from_rows(envelope["package_rows"])
        report = ET.parse(report_path).getroot()
        self.assertEqual(report.get("caprmedio.phase"), "unit")
        self.assertEqual(report.get("caprmedio.phase_map_sha256"), phase_map.sha256)
        expected_count = 7
        cases = self._junit_cases(report_path)
        self.assertEqual(sum(map(len, cases.values())), expected_count)
        self.assertEqual(len(cases), expected_count)
        observed_source_paths: set[str] = set()
        for test_id, rows in cases.items():
            self.assertEqual(len(rows), 1, test_id)
            properties = rows[0].findall("./properties/property")
            values = {item.get("name"): item.get("value") for item in properties}
            self.assertEqual(values["caprmedio.test_id"], test_id)
            self.assertEqual(len(values["caprmedio.source_bindings_sha256"]), 64)
            probes = [item.get("value") for item in properties if item.get("name") == "caprmedio.source_probe"]
            self.assertGreaterEqual(len(probes), 1)
            for probe in probes:
                parsed = json.loads(probe or "")
                self.assertEqual(set(parsed), {"source_path", "sha256"})
                self.assertFalse(Path(parsed["source_path"]).is_absolute())
                self.assertEqual(len(parsed["sha256"]), 64)
                observed_source_paths.add(parsed["source_path"])
        self.assertTrue(set(MODULE_PROBES[f"{ENGINE_ROOT}/101_METHODOLOGY/test_methodology.py"]) <= observed_source_paths)
        self.assertTrue(set(MODULE_PROBES[f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/test_tools.py"]) <= observed_source_paths)
        self.assertTrue(set(MODULE_PROBES[f"{ENGINE_ROOT}/202_AGENTIC/test_agentic.py"]) <= observed_source_paths)
        self.assertTrue(set(MODULE_PROBES[f"{ENGINE_ROOT}/201_PROGRAMMATIC/203_APPS/test_apps.py"]) <= observed_source_paths)
        self.assertTrue(set(MODULE_PROBES[f"{ENGINE_ROOT}/201_PROGRAMMATIC/204_MCP/test_mcp.py"]) <= observed_source_paths)
        self.assertTrue(set(CASKILL_PATHS) <= observed_source_paths)
        self.assertIn(COMPILED_PROBE_PATH, observed_source_paths)
        self.assertNotIn(CANDIDATE_PATH, observed_source_paths)
        self.assertFalse(
            set(CANDIDATE_E2E_MODULES).intersection(
                case.get("classname") for rows in cases.values() for case in rows
            ),
            "candidate E2E modules are reserved for the host E2E gate",
        )

    def test_failure_error_skip_and_subtest_failure_cannot_pass(self) -> None:
        variants = ("test_failure.py", "test_error.py", "test_skipped.py", "test_subtest_failure.py")
        target = self.project_root / f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/test_tools.py"
        for variant in variants:
            with self.subTest(variant=variant):
                shutil.copyfile(_golden_case(variant), target)
                result, _ = self._run()
                self._assert_non_passing(result)

    def test_zero_case_module_and_duplicate_test_identity_cannot_pass(self) -> None:
        target = self.project_root / f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/test_tools.py"
        shutil.copyfile(_golden_case("test_zero.py"), target)
        result, _ = self._run()
        self._assert_non_passing(result)

        self.setUp()
        duplicate = self.project_root / f"{ENGINE_ROOT}/401_A/test_duplicate.py"
        duplicate.parent.mkdir(parents=True)
        shutil.copyfile(_golden_case("test_duplicate_id.py"), duplicate)
        duplicate = self.project_root / f"{ENGINE_ROOT}/402_B/test_duplicate.py"
        duplicate.parent.mkdir(parents=True)
        shutil.copyfile(_golden_case("test_duplicate_id.py"), duplicate)
        result, _ = self._run()
        self._assert_non_passing(result)

    def test_duplicate_basenames_with_distinct_test_ids_pass_in_fresh_children(self) -> None:
        self.setUp()
        for parent, fixture in (("401_A", "test_duplicate_basename_a.py"), ("402_B", "test_duplicate_basename_b.py")):
            duplicate = self.project_root / f"{ENGINE_ROOT}/{parent}/test_collision.py"
            duplicate.parent.mkdir(parents=True)
            shutil.copyfile(_golden_case(fixture), duplicate)
        result, report_path = self._run()

        self.assertEqual(result.returncode, 0, msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}")
        cases = self._junit_cases(report_path)
        self.assertEqual(sum(map(len, cases.values())), 9)
        expected = {
            "test_collision.DuplicateBasenameATests.test_a",
            "test_collision.DuplicateBasenameBTests.test_b",
        }
        self.assertTrue(expected <= set(cases))
        for test_id, expected_module in (
            ("test_collision.DuplicateBasenameATests.test_a", f"{ENGINE_ROOT}/401_A/test_collision.py"),
            ("test_collision.DuplicateBasenameBTests.test_b", f"{ENGINE_ROOT}/402_B/test_collision.py"),
        ):
            row = cases[test_id][0]
            self.assertEqual(row.get("classname"), expected_module)
            source_paths = {
                json.loads(item.get("value") or "")["source_path"]
                for item in row.findall("./properties/property")
                if item.get("name") == "caprmedio.source_probe"
            }
            self.assertIn(expected_module, source_paths)

    def test_flat_module_imports_are_isolated_by_the_sealed_module_parent(self) -> None:
        self.setUp()
        for parent, marker, class_name in (("401_A", "first", "FlatImportFirstTests"), ("402_B", "second", "FlatImportSecondTests")):
            directory = self.project_root / ENGINE_ROOT / parent
            directory.mkdir(parents=True)
            (directory / "helper.py").write_text(f"MARKER = {marker!r}\n", encoding="utf-8")
            (directory / "test_flat_import.py").write_text(
                "import unittest\nimport helper\n\n"
                f"class {class_name}(unittest.TestCase):\n"
                f"    def test_marker(self):\n        self.assertEqual(helper.MARKER, {marker!r})\n",
                encoding="utf-8",
            )

        result, report_path = self._run()

        self.assertEqual(result.returncode, 0, msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}")
        cases = self._junit_cases(report_path)
        self.assertEqual(sum(map(len, cases.values())), 9)
        self.assertIn("test_flat_import.FlatImportFirstTests.test_marker", cases)
        self.assertIn("test_flat_import.FlatImportSecondTests.test_marker", cases)

    def test_child_scratch_is_fixed_and_not_inherited_from_the_caller(self) -> None:
        inputs = suite_driver.BoundInputs(
            root=self.project_root,
            compiled_root=f"{ENGINE_ROOT}/299_COMPILED_CANDIDATE",
            candidate_manifest_sha256=CANDIDATE_DIGEST,
            report_path=self.output_root / "coverage.xml",
            envelope_sha256="c" * 64,
            rows={},
            reference_rows=(),
            control_context_digest="d" * 64,
            phase_map=ReleaseTestPhaseMap((), "e" * 64, (), ()),
            probes=suite_driver.ModuleProbeRules("rules.json", "f" * 64, {}),
        )
        module = f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/test_tools.py"
        carrier = self.project_root / module
        carrier.parent.mkdir(parents=True, exist_ok=True)
        carrier.write_text("# sealed test carrier\n", encoding="utf-8")
        results_root = self.output_root / "results"
        results_root.mkdir()
        observed_environment: dict[str, str] = {}

        def capture(command, **kwargs):
            observed_environment.update(kwargs["env"])
            result_path = Path(command[-1])
            result_path.write_bytes(_canonical_json({"loader_errors": [], "cases": []}))
            return subprocess.CompletedProcess(command, 0, "", "")

        with mock.patch.dict(os.environ, {"TMPDIR": "/caller/tmp", "TEMP": "/caller/temp", "TMP": "/caller/TMP"}):
            with mock.patch.object(suite_driver.subprocess, "run", side_effect=capture):
                _cases, errors = suite_driver._run_module(inputs, module, results_root)

        self.assertEqual(errors, [f"{module}: discovery returned no test cases"])
        self.assertEqual(observed_environment["TMPDIR"], str(suite_driver._CHILD_SCRATCH))
        self.assertEqual(observed_environment["TEMP"], str(suite_driver._CHILD_SCRATCH))
        self.assertEqual(observed_environment["TMP"], str(suite_driver._CHILD_SCRATCH))

    def test_execute_bound_uses_fixed_driver_scratch_not_report_parent(self) -> None:
        scratch = self.scratch / "fixed-child-scratch"
        scratch.mkdir()
        module = f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/test_tools.py"
        inputs = suite_driver.BoundInputs(
            root=self.project_root,
            compiled_root=f"{ENGINE_ROOT}/299_COMPILED_CANDIDATE",
            candidate_manifest_sha256=CANDIDATE_DIGEST,
            report_path=self.output_root / "coverage.xml",
            envelope_sha256="c" * 64,
            rows={},
            reference_rows=(),
            control_context_digest="d" * 64,
            phase_map=ReleaseTestPhaseMap(((module, "e" * 64, "unit"),), "e" * 64, (module,), ()),
            probes=suite_driver.ModuleProbeRules("rules.json", "f" * 64, {}),
        )
        captured: list[Path] = []

        def capture(_inputs, _module_path, results_root):
            captured.append(results_root)
            return [], []

        with mock.patch.object(suite_driver, "_prepare_child_scratch", return_value=scratch):
            with mock.patch.object(suite_driver, "_run_module", side_effect=capture):
                suite_driver._execute_bound(inputs)

        self.assertTrue(scratch.is_dir())
        self.assertTrue(all(path.is_relative_to(scratch) for path in captured))

    def test_load_tests_repeating_one_testcase_id_cannot_collapse_to_a_passing_gate(self) -> None:
        duplicate = self.project_root / f"{ENGINE_ROOT}/401_A/test_repeated.py"
        duplicate.parent.mkdir(parents=True)
        shutil.copyfile(_golden_case("test_duplicate_same_id_load_tests.py"), duplicate)

        result, _ = self._run()

        self._assert_non_passing(result)

    def test_missing_declared_module_cannot_pass(self) -> None:
        _, _, _ = self._write_rules_and_envelope()
        missing = self.project_root / f"{ENGINE_ROOT}/206_SKILL/test_skill.py"
        missing.unlink()
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

    def test_malformed_or_tampered_envelope_and_unsafe_or_unknown_probes_cannot_pass(self) -> None:
        _, envelope_path, _ = self._write_rules_and_envelope(envelope_override={"schema_version": 1})
        result, _ = self._run(envelope_sha256=_sha256(envelope_path), preserve_bindings=True)
        self._assert_non_passing(result)

        self.setUp()
        _, _, digest = self._write_rules_and_envelope()
        result, _ = self._run(envelope_sha256="0" * 64, preserve_bindings=True)
        self._assert_non_passing(result)

        self.setUp()
        unsafe = {path: [] for path in self._test_paths()}
        unsafe[next(iter(unsafe))] = ["../outside.py"]
        self._write_rules_and_envelope(probes=unsafe)
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

        self.setUp()
        unknown = {path: [] for path in self._test_paths()}
        unknown[next(iter(unknown))] = [f"{ENGINE_ROOT}/201_PROGRAMMATIC/unknown.py"]
        self._write_rules_and_envelope(probes=unknown)
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

        self.setUp()
        malformed_probes: dict[str, object] = {path: [] for path in self._test_paths()}
        malformed_probes[next(iter(malformed_probes))] = "not-a-list"
        self._write_rules_and_envelope(probes=malformed_probes)  # type: ignore[arg-type]
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

        # The public driver sees an opaque context digest.  It must still
        # reject a missing or widened closed reference list rather than let a
        # syntactically valid opaque SHA stand in for the source closure.
        self.setUp()
        _, envelope_path, _ = self._write_rules_and_envelope()
        missing_reference = json.loads(envelope_path.read_text(encoding="utf-8"))
        missing_reference["reference_rows"].pop()
        missing_reference["control_context_digest"] = "f" * 64
        envelope_path.write_bytes(_canonical_json(missing_reference))
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

        self.setUp()
        _, envelope_path, _ = self._write_rules_and_envelope()
        altered_mode = json.loads(envelope_path.read_text(encoding="utf-8"))
        altered_mode["reference_rows"][0]["mode"] ^= 0o100
        envelope_path.write_bytes(_canonical_json(altered_mode))
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

        for label in ("reordered", "duplicated", "wrong_digest"):
            with self.subTest(reference_rows=label):
                self.setUp()
                _, envelope_path, _ = self._write_rules_and_envelope()
                noncanonical = json.loads(envelope_path.read_text(encoding="utf-8"))
                if label == "reordered":
                    noncanonical["reference_rows"].reverse()
                elif label == "duplicated":
                    noncanonical["reference_rows"].append(
                        dict(noncanonical["reference_rows"][0])
                    )
                else:
                    noncanonical["reference_rows"][0]["sha256"] = "0" * 64
                envelope_path.write_bytes(_canonical_json(noncanonical))
                result, _ = self._run(preserve_bindings=True)
                self._assert_non_passing(result)

        self.setUp()
        _, envelope_path, _ = self._write_rules_and_envelope()
        stale_reference = json.loads(envelope_path.read_text(encoding="utf-8"))
        selected = stale_reference["reference_rows"][0]
        carrier = self.project_root / selected["source_path"]
        carrier.write_bytes(carrier.read_bytes() + b"\nfixture mutation\n")
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

    def test_missing_report_and_missing_compiled_candidate_evidence_cannot_pass(self) -> None:
        result, _ = self._run(include_report=False)
        self._assert_non_passing(result)

        self.setUp()
        result, _ = self._run(report_path=self.output_root / "not-coverage.xml")
        self._assert_non_passing(result)

        self.setUp()
        _, _, _ = self._write_rules_and_envelope()
        rows = json.loads((self.project_root / ".caprmedio_release/source_bindings.json").read_text(encoding="utf-8"))["package_rows"]
        rows = [row for row in rows if row["source_path"] not in COMPILED_CANDIDATE_PATHS]
        self._write_rules_and_envelope(package_rows=rows)
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

    def test_compiled_candidate_probe_is_derived_and_its_rule_is_closed(self) -> None:
        self.setUp()
        self._write_rules_and_envelope(compiled_candidate_flags={})
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

        self.setUp()
        self._write_rules_and_envelope(compiled_candidate_flags={COMPILATION_TEST_PATH: "true"})
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

        self.setUp()
        self._write_rules_and_envelope(
            compiled_candidate_flags={
                COMPILATION_TEST_PATH: True,
                f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/test_tools.py": True,
            }
        )
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

        self.setUp()
        self._write_rules_and_envelope(
            compiled_candidate_flags={f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/test_tools.py": True}
        )
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

        self.setUp()
        wrong_probe = {path: list(MODULE_PROBES.get(path, [DEFAULT_EXTRA_PROBE])) for path in self._test_paths()}
        wrong_probe[COMPILATION_TEST_PATH].append(CANDIDATE_PATH)
        wrong_probe[COMPILATION_TEST_PATH].sort()
        self._write_rules_and_envelope(probes=wrong_probe)
        result, _ = self._run(preserve_bindings=True)
        self._assert_non_passing(result)

    def test_read_only_input_and_separate_output_scratch_are_required(self) -> None:
        target = self.project_root / f"{ENGINE_ROOT}/201_PROGRAMMATIC/201_TOOLS/test_tools.py"
        shutil.copyfile(_golden_case("test_workspace_write.py"), target)
        result, report_path = self._run(make_workspace_read_only=True)

        self.assertEqual(result.returncode, 0, msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}")
        self.assertTrue(report_path.is_file())
        self.assertTrue(report_path.is_relative_to(self.output_root))
        self.assertFalse((self.project_root / "must-not-be-written.txt").exists())

    def test_public_cli_refuses_portable_fixture_paths_before_creating_a_report(self) -> None:
        _, envelope_path, envelope_sha256 = self._write_rules_and_envelope()
        report_path = self.output_root / "coverage.xml"
        environment = self._fixture_environment(
            envelope_path=envelope_path,
            envelope_sha256=envelope_sha256,
            report_path=report_path,
            include_report=True,
        )

        result = self._run_public_cli(environment)

        self._assert_non_passing(result)
        self.assertFalse(report_path.exists(), "production CLI must refuse non-sandbox paths before output creation")


if __name__ == "__main__":
    unittest.main()
