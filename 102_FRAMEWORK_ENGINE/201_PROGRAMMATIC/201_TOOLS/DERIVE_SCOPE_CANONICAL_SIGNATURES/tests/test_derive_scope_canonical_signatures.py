"""Focused acceptance tests for restricted, report-only Scope canonical signatures."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


SCRIPT = Path(__file__).resolve().parents[1] / "derive_scope_canonical_signatures.py"
SPEC = importlib.util.spec_from_file_location("derive_scope_canonical_signatures", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
signatures = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = signatures
SPEC.loader.exec_module(signatures)


def atom(atom_id: str, scope: str | None = None, *, status: str = "Active") -> str:
    scope_section = "" if scope is None else f"\n## Scope\n\n{scope}\n"
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: obligation\n"
        f"status: {status}\n"
        "version: 1\n"
        "updated_at: 2026-09-01 00:00:00 +0400\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\n"
        "the Task **must** complete one bounded action.\n"
        f"{scope_section}"
    )


class DeriveScopeCanonicalSignaturesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name) / "frontier"
        self.root.mkdir(parents=True)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        return path

    def test_flattens_deduplicates_and_orders_one_static_union_without_mutation(self) -> None:
        first = self.write(
            "CA-P-001.md",
            atom("CA-P-001", "((CA-P-003 **or** CA-P-002) **or** CA-P-003)"),
        )
        self.write("CA-P-002.md", atom("CA-P-002"))
        self.write("CA-P-003.md", atom("CA-P-003"))
        before = first.read_bytes()

        report = signatures.build_report(self.root)

        self.assertEqual("report_only", report["mode"])
        self.assertEqual(1, report["counts"]["canonical_signatures"])
        self.assertEqual(
            {"operator": "or", "atomic_identities": ["CA-P-002", "CA-P-003"]},
            report["signatures"][0]["canonical_scope_signature"],
        )
        self.assertEqual(before, first.read_bytes())

    def test_preserves_intersection_and_reports_only_matching_signatures(self) -> None:
        self.write("CA-P-010.md", atom("CA-P-010", "(CA-P-012 **or** CA-P-011)"))
        self.write("CA-P-011.md", atom("CA-P-011", "(CA-P-011 **or** CA-P-012)"))
        self.write("CA-P-012.md", atom("CA-P-012", "(CA-P-011 **and** CA-P-012)"))

        report = signatures.build_report(self.root)

        self.assertEqual(3, report["counts"]["canonical_signatures"])
        self.assertEqual(1, report["counts"]["duplicate_signature_groups"])
        self.assertEqual(
            ["CA-P-010", "CA-P-011"],
            report["duplicate_canonical_scope_signature_groups"][0]["atom_ids"],
        )
        self.assertNotEqual(
            report["signatures"][0]["canonical_scope_signature"],
            report["signatures"][2]["canonical_scope_signature"],
        )

    def test_excludes_dynamic_mixed_and_unresolved_scope_expressions(self) -> None:
        self.write(
            "CA-P-020.md",
            atom("CA-P-020", "(CA-P-021 **and** (CA-P-022 **or** CA-P-021))"),
        )
        self.write("CA-P-021.md", atom("CA-P-021", "(**all** Atom **where** Status: Active)"))
        self.write("CA-P-022.md", atom("CA-P-022", "(CA-P-020 **without** CA-P-021)"))
        self.write("CA-P-023.md", atom("CA-P-023", "(CA-P-999 **or** CA-P-021)"))
        self.write("CA-P-024.md", atom("CA-P-024", "(CA-P-020 **future_extension** CA-P-021)"))

        report = signatures.build_report(self.root)

        self.assertEqual([], report["signatures"])
        codes = {row["code"] for row in report["diagnostics"]}
        self.assertIn("mixed-operator", codes)
        self.assertIn("operator-excluded", codes)
        self.assertIn("atomic-identity-unresolved", codes)

    def test_cli_never_writes_inside_selected_frontier(self) -> None:
        self.write("CA-P-030.md", atom("CA-P-030", "(CA-P-030 **or** CA-P-031)"))
        self.write("CA-P-031.md", atom("CA-P-031"))
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--source-folder", str(self.root)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("report_only", json.loads(result.stdout)["mode"])

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--source-folder",
                str(self.root),
                "--output",
                str(self.root / "report.json"),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(2, result.returncode)
        self.assertEqual("output-inside-source-frontier", json.loads(result.stderr)["error"]["code"])


if __name__ == "__main__":
    unittest.main()
