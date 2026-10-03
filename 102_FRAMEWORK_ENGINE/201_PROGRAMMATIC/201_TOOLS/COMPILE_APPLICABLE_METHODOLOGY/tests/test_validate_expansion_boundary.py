from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


TOOL = Path(__file__).resolve().parents[1] / "validate_expansion_boundary.py"
SPEC = importlib.util.spec_from_file_location("validate_expansion_boundary", TOOL)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def carrier(atom_id: str, relations: str = "{}", cce_form: str = "obligation", subjects: str = "") -> str:
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        f"cce_form: {cce_form}\n"
        f"{subjects}"
        "version: 1\n"
        "updated_at: 2026-09-03 00:00:00 +0400\n"
        f"relations: {relations}\n"
        "---\n"
        f"# {atom_id}\n\nclaim\n"
    )


class ExpansionBoundaryTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = Path.cwd() / ".caprmedio_tmp/expansion-boundary-tests"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temp = Path(tempfile.mkdtemp(prefix="case-", dir=temporary))
        self.source = self.temp / module.compiler.SOURCE_RELATIVE
        for _, directory in module.LAYER_DIRECTORIES:
            (self.source / directory / "04_requirement").mkdir(parents=True)
        self.write("001_CORE_META_MODEL", "CA-R-1375--boundary.md", carrier("CA-R-1375"))

    def tearDown(self) -> None:
        shutil.rmtree(self.temp, ignore_errors=True)

    def write(self, layer: str, name: str, data: str) -> Path:
        path = self.source / layer / "04_requirement" / name
        path.write_text(data)
        return path

    def invoke(self) -> tuple[int, dict[str, object]]:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = module.run(["--root", str(self.temp)])
        return code, json.loads(stream.getvalue())

    def test_accepts_non_mutating_local_expansion(self) -> None:
        self.write("003_PROJECT_CONFIGURATION", "CA-R-200--local.md", carrier("CA-R-200"))
        code, report = self.invoke()
        self.assertEqual(0, code)
        self.assertTrue(report["can_conform"])
        self.assertEqual(1, report["source_counts"]["PROJECT_CONFIGURATION"])
        self.assertEqual("EXPANSION_CANDIDATE", report["external_members"][0]["classification"])

    def test_core_only_selection_excludes_local_members(self) -> None:
        self.write("003_PROJECT_CONFIGURATION", "CA-R-200--local.md", carrier("CA-R-200"))
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = module.run(["--root", str(self.temp), "--include-layer", "CORE_META_MODEL"])
        report = json.loads(stream.getvalue())
        self.assertEqual(0, code)
        self.assertEqual(["CORE_META_MODEL"], report["selected_source_layers"])
        self.assertEqual(0, report["external_member_count"])

    def test_rejects_direct_mutation_of_active_core_authority(self) -> None:
        self.write("001_CORE_META_MODEL", "CA-R-001--core.md", carrier("CA-R-001"))
        self.write(
            "003_PROJECT_CONFIGURATION",
            "CA-R-200--local.md",
            carrier("CA-R-200", relations="\n  replacement_of:\n    - CA-R-001\n"),
        )
        code, report = self.invoke()
        self.assertEqual(2, code)
        self.assertFalse(report["can_conform"])
        self.assertIn(
            "external_source_mutates_active_core_authority",
            {item["type"] for item in report["hard_violations"]},
        )

    def test_reports_missing_legacy_lineage_without_treating_it_as_core_mutation(self) -> None:
        self.write(
            "003_PROJECT_CONFIGURATION",
            "CA-R-200--local.md",
            carrier("CA-R-200", relations="\n  replacement_of:\n    - CA-R-099--retired-local\n"),
        )
        code, report = self.invoke()
        self.assertEqual(0, code)
        self.assertTrue(report["can_conform"])
        self.assertEqual(1, report["stable_lineage_gap_count"])
        self.assertEqual(
            "EXPANSION_CANDIDATE_WITH_LINEAGE_GAP",
            report["external_members"][0]["classification"],
        )
