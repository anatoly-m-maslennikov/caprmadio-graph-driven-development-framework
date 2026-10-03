"""Focused acceptance tests for report-only Claim Value-Set candidate detection."""

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


SCRIPT = Path(__file__).resolve().parents[1] / "detect_claim_value_set_candidates.py"
SPEC = importlib.util.spec_from_file_location("detect_claim_value_set_candidates", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
detector = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = detector
SPEC.loader.exec_module(detector)


def atom(
    atom_id: str,
    statement: str,
    *,
    status: str = "Active",
    governed_subject: str = "Atom/Status",
) -> str:
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: obligation\n"
        "subjects:\n"
        "  governs:\n"
        "    continuant:\n"
        f"      - {governed_subject}\n"
        "  depends_on:\n"
        "    continuant:\n"
        "      - Atom\n"
        f"status: {status}\n"
        "version: 1\n"
        "updated_at: 2026-09-01 00:00:00 +0400\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\n"
        f"{statement}\n"
    )


class DetectClaimValueSetCandidatesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name) / "frontier"
        self.root.mkdir(parents=True)
        self.term_system = Path(self.temporary.name) / "term-system.json"
        self.term_system.write_text(
            json.dumps(
                {
                    "term_system": {
                        "edges": [
                            {
                                "relation": "IS_ALLOWED_VALUE_OF",
                                "source_term": value,
                                "target_subject": "Atom/Status",
                            }
                            for value in ("Active", "Draft", "Archived")
                        ]
                    }
                }
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        return path

    def test_reports_only_exact_candidates_and_preserves_source_bytes(self) -> None:
        first = self.write(
            "04_requirement/CA-R-001.md",
            atom("CA-R-001", "Atom/Status: Active **if** Atom/Content Role: Requirement."),
        )
        second = self.write(
            "04_requirement/CA-R-002.md",
            atom("CA-R-002", "Atom/Status: Draft **if** Atom/Content Role: Requirement."),
        )
        self.write(
            "04_requirement/archive/CA-R-003@1.md",
            atom("CA-R-003", "Atom/Status: Archived **if** Atom/Content Role: Requirement."),
        )
        before = {path: path.read_bytes() for path in (first, second)}

        report = detector.build_report(
            self.root,
            term_system_projection=self.term_system,
        )

        self.assertEqual("report_only", report["mode"])
        self.assertEqual(1, report["counts"]["candidate_groups"])
        group = report["candidate_groups"][0]
        self.assertEqual(["CA-R-001", "CA-R-002"], group["atom_ids"])
        self.assertEqual(
            {"scope_unit_carrier": self.root.resolve().as_posix()},
            group["fingerprint"]["atom_scope"],
        )
        self.assertNotIn("current_scope", group["fingerprint"])
        self.assertEqual(
            [{"temporal_form": "CONTINUANT", "subject_path": "Atom/Status"}],
            group["fingerprint"]["governed_subject_set"],
        )
        self.assertEqual(
            "Atom/Status: (Active, Draft) **if** Atom/Content Role: Requirement.",
            group["proposed_claim"],
        )
        self.assertEqual(before, {path: path.read_bytes() for path in (first, second)})
        self.assertEqual(1, report["counts"]["inactive_directory_carriers_skipped"])

    def test_refuses_semantic_similarity_and_any_difference_beyond_value(self) -> None:
        self.write("CA-R-010.md", atom("CA-R-010", "Atom/Status: Active **if** Atom/Content Role: Requirement."))
        self.write("CA-R-011.md", atom("CA-R-011", "Atom/Status: Draft **if** Atom/Content Role: Method."))
        self.write("CA-R-012.md", atom("CA-R-012", "Atom/Status can have Archived status."))
        self.write(
            "CA-R-013.md",
            atom("CA-R-013", "Atom/Status: Active **if** Atom/Content Role: Requirement."),
        )

        report = detector.build_report(
            self.root,
            term_system_projection=self.term_system,
        )

        self.assertEqual([], report["candidate_groups"])
        self.assertEqual(1, report["counts"]["unparseable_single_value_claim_skipped"])
        self.assertIn(
            "duplicate-value-group-not-reported",
            {row["code"] for row in report["diagnostics"]},
        )
        self.assertIn(
            "narrow-parser-boundary",
            {row["code"] for row in report["diagnostics"]},
        )

    def test_cli_is_stdout_only_by_default_and_refuses_output_inside_frontier(self) -> None:
        self.write("CA-R-020.md", atom("CA-R-020", "Atom/Status: Active."))
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--scope-unit-folder",
                str(self.root),
                "--term-system-projection",
                str(self.term_system),
            ],
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
                "--scope-unit-folder",
                str(self.root),
                "--term-system-projection",
                str(self.term_system),
                "--output",
                str(self.root / "report.json"),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(2, result.returncode)
        self.assertEqual("output-inside-source-frontier", json.loads(result.stderr)["error"]["code"])

    def test_does_not_merge_different_governed_subject_sets(self) -> None:
        self.write(
            "CA-R-030.md",
            atom("CA-R-030", "Atom/Status: Active.", governed_subject="Atom/Status"),
        )
        self.write(
            "CA-R-031.md",
            atom("CA-R-031", "Atom/Status: Draft.", governed_subject="Artifact/Status"),
        )

        report = detector.build_report(self.root, term_system_projection=self.term_system)

        self.assertEqual([], report["candidate_groups"])

    def test_fails_closed_without_allowed_value_evidence(self) -> None:
        self.write("CA-R-040.md", atom("CA-R-040", "Atom/Status: Active."))
        self.write("CA-R-041.md", atom("CA-R-041", "Atom/Status: Unknown."))

        report = detector.build_report(self.root, term_system_projection=self.term_system)

        self.assertEqual([], report["candidate_groups"])
        self.assertIn(
            "unproven-allowed-value-claim-not-reported",
            {row["code"] for row in report["diagnostics"]},
        )

    def test_excludes_atoms_owned_by_child_scope_units(self) -> None:
        self.write("04_requirement/CA-R-050.md", atom("CA-R-050", "Atom/Status: Active."))
        self.write("201_FEATURE_CHILD/04_requirement/CA-R-051.md", atom("CA-R-051", "Atom/Status: Draft."))

        report = detector.build_report(self.root, term_system_projection=self.term_system)

        self.assertEqual([], report["candidate_groups"])
        self.assertEqual(1, report["source_frontier"]["active_carrier_count"])


if __name__ == "__main__":
    unittest.main()
