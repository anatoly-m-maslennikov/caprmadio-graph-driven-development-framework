"""Native W13 compiler golden inputs in a disposable Project."""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
COMPILER_ROOT = APP.parents[1] / "201_TOOLS" / "COMPILE_APPLICABLE_METHODOLOGY"
if str(COMPILER_ROOT) not in sys.path:
    sys.path.insert(0, str(COMPILER_ROOT))
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

import compile_applicable_methodology as compiler  # noqa: E402
from selected_workflows_docker_fixture import FixtureLease, GoldenCase, GoldenProject  # noqa: E402


class SelectedCompilerGoldenInputsTest(unittest.TestCase):
    """CA-O-011 source selection and publication, without Run/Journaling claims."""

    def _fixture(self) -> tuple[FixtureLease, GoldenProject]:
        parent = ROOT / ".caprmedio_tmp" / "tests" / "selected-compiler-golden-inputs"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent))
        fixture = GoldenProject(ROOT, root, GoldenCase("W13", "build_applicable_methodology"))
        fixture.prepare()
        return FixtureLease(root), fixture

    @staticmethod
    def _source_bytes(fixture: GoldenProject) -> dict[str, str]:
        return {
            path.relative_to(fixture.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(fixture.compiler_source_dir.rglob("*")) if path.is_file()
        }

    @staticmethod
    def _output_bytes(fixture: GoldenProject) -> dict[str, bytes]:
        places = compiler.methodology_paths(fixture.root)
        output, source = fixture.root / places.output, fixture.root / places.source
        return {
            path.relative_to(output).as_posix(): path.read_bytes()
            for path in sorted(output.rglob("*"))
            if path.is_file() and not path.is_relative_to(source)
        }

    def test_w13_selects_sourceful_layers_and_publishes_deterministically(self) -> None:
        lease, fixture = self._fixture()
        try:
            before = self._source_bytes(fixture)
            assessed = compiler.run_request(fixture.native_compiler_parameters())
            self.assertEqual("assessed", assessed["outcome"], assessed)
            layers = {row["source_layer"] for row in assessed["source_frontier"]}
            self.assertTrue({"CORE_META_MODEL", "INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION"} <= layers)
            selected_paths = {row["source_carrier_path"] for row in assessed["source_frontier"]}
            self.assertIn(
                ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/"
                "002_INSTALLED_EXTENSIONS/example/v2/05_method/CA-M-302--extension.md",
                selected_paths,
            )
            applied = compiler.run_request(fixture.native_compiler_parameters(
                "apply", expected_source_frontier_digest=assessed["source_frontier_digest"]
            ))
            self.assertEqual("pending_recording", applied["outcome"], applied)
            self.assertEqual([], applied["run_receipt_refs"])
            self.assertEqual(before, self._source_bytes(fixture))
            first = self._output_bytes(fixture)
            self.assertIn("04_requirement/CA-R-301--core.md", first)
            self.assertIn(b"source_atom_id: CA-R-301", first["04_requirement/CA-R-301--core.md"])
            reassessed = compiler.run_request(fixture.native_compiler_parameters())
            repeated = compiler.run_request(fixture.native_compiler_parameters(
                "apply", expected_source_frontier_digest=reassessed["source_frontier_digest"]
            ))
            self.assertEqual("pending_recording", repeated["outcome"], repeated)
            self.assertEqual(first, self._output_bytes(fixture))
        finally:
            lease.cleanup()

    def test_w13_stale_and_unapproved_inputs_preserve_prior_projection(self) -> None:
        lease, fixture = self._fixture()
        try:
            assessed = compiler.run_request(fixture.native_compiler_parameters())
            compiler.run_request(fixture.native_compiler_parameters(
                "apply", expected_source_frontier_digest=assessed["source_frontier_digest"]
            ))
            prior = self._output_bytes(fixture)
            source = fixture.compiler_source_dir / "001_CORE_META_MODEL/04_requirement/CA-R-301--core.md"
            source.write_text(source.read_text(encoding="utf-8") + "\nChanged after assessment.\n", encoding="utf-8")
            stale = compiler.run_request(fixture.native_compiler_parameters(
                "apply", expected_source_frontier_digest=assessed["source_frontier_digest"]
            ))
            self.assertEqual("blocked", stale["outcome"], stale)
            self.assertEqual("assessment-frontier-stale", stale["blocking_findings"][0]["code"])
            self.assertEqual("preserved", stale["publication"]["prior_output_state"])
            self.assertEqual(prior, self._output_bytes(fixture))

            duplicate = fixture.compiler_source_dir / "003_PROJECT_CONFIGURATION/04_requirement/CA-R-301--project.md"
            duplicate.parent.mkdir(parents=True, exist_ok=True)
            duplicate.write_text(source.read_text(encoding="utf-8").replace("version: 1", "version: 2"), encoding="utf-8")
            conflicted = compiler.run_request(fixture.native_compiler_parameters())
            self.assertEqual("blocked", conflicted["outcome"], conflicted)
            unapproved = compiler.run_request(fixture.native_compiler_parameters(
                "apply", expected_source_frontier_digest=conflicted["source_frontier_digest"]
            ))
            self.assertEqual("blocked", unapproved["outcome"], unapproved)
            self.assertEqual("conflict-unresolved", unapproved["blocking_findings"][-1]["code"])
            self.assertEqual("preserved", unapproved["publication"]["prior_output_state"])
            self.assertEqual(prior, self._output_bytes(fixture))
        finally:
            lease.cleanup()


if __name__ == "__main__":
    unittest.main()
