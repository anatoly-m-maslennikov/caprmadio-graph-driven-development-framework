"""Focused acceptance tests for restricted, report-only CCE canonical signatures."""

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


SCRIPT = Path(__file__).resolve().parents[1] / "derive_cce_canonical_signatures.py"
SPEC = importlib.util.spec_from_file_location("derive_cce_canonical_signatures", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
signatures = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = signatures
SPEC.loader.exec_module(signatures)


def atom(atom_id: str, statement: str, *, status: str = "Active") -> str:
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
        f"{statement}\n"
    )


class DeriveCceCanonicalSignaturesTests(unittest.TestCase):
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

    def test_flattens_deduplicates_and_orders_one_pure_and_group_without_mutation(self) -> None:
        carrier = self.write(
            "CA-R-001.md",
            atom(
                "CA-R-001",
                "the Evaluation **must** accept ((Atom/Status: Draft **and** Atom/Status: Active) **and** Atom/Status: Draft).",
            ),
        )
        before = carrier.read_bytes()

        report = signatures.build_report(self.root)

        self.assertEqual("report_only", report["mode"])
        self.assertEqual(1, report["counts"]["canonical_signatures"])
        self.assertEqual(
            {"operator": "and", "atomic_predicates": ["Atom/Status: Active", "Atom/Status: Draft"]},
            report["signatures"][0]["canonical_signature"],
        )
        self.assertEqual(before, carrier.read_bytes())

    def test_keeps_or_distinct_and_reports_same_signature_across_carriers(self) -> None:
        self.write(
            "CA-R-002.md",
            atom("CA-R-002", "the Evaluation **must** accept (Atom/Status: Active **or** Atom/Status: Draft)."),
        )
        self.write(
            "CA-R-003.md",
            atom("CA-R-003", "the Evaluation **must** accept (Atom/Status: Draft **or** Atom/Status: Active)."),
        )
        self.write(
            "CA-R-004.md",
            atom("CA-R-004", "the Evaluation **must** accept (Atom/Status: Active **and** Atom/Status: Draft)."),
        )

        report = signatures.build_report(self.root)

        self.assertEqual(3, report["counts"]["canonical_signatures"])
        self.assertEqual(1, report["counts"]["duplicate_signature_groups"])
        self.assertEqual(["CA-R-002", "CA-R-003"], report["duplicate_signature_groups"][0]["atom_ids"])
        self.assertNotEqual(
            report["signatures"][0]["canonical_signature"],
            report["signatures"][2]["canonical_signature"],
        )

    def test_excludes_mixed_temporal_negation_and_unparseable_prose(self) -> None:
        self.write(
            "CA-R-005.md",
            atom("CA-R-005", "the Evaluation **must** accept (Atom/Status: Active **and** (Atom/Status: Draft **or** Atom/Status: Archived))."),
        )
        self.write(
            "CA-R-006.md",
            atom("CA-R-006", "the Evaluation **must** accept (Atom/Status: Active **and** **not** Atom/Status: Draft)."),
        )
        self.write(
            "CA-R-007.md",
            atom("CA-R-007", "the Evaluation **must** accept (Atom/Status: Active **before** Atom/Status: Draft)."),
        )
        self.write(
            "CA-R-008.md",
            atom("CA-R-008", "the Evaluation **must** accept (ordinary prose **and** more ordinary prose)."),
        )

        report = signatures.build_report(self.root)

        self.assertEqual([], report["signatures"])
        codes = {row["code"] for row in report["diagnostics"]}
        self.assertIn("mixed-operator", codes)
        self.assertIn("operator-excluded", codes)
        self.assertIn("atomic-predicate-invalid", codes)

    def test_cli_never_writes_inside_selected_frontier(self) -> None:
        self.write(
            "CA-R-009.md",
            atom("CA-R-009", "the Evaluation **must** accept (Atom/Status: Active **and** Atom/Status: Draft)."),
        )
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
