"""Read-only, complete-frontier checks for the RMEDO migration preparer."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "prepare_active_rmedo_migration.py"
SPEC = importlib.util.spec_from_file_location("prepare_active_rmedo_migration", SCRIPT)
assert SPEC and SPEC.loader
migration = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(migration)


class PreparationTests(unittest.TestCase):
    def setUp(self) -> None:
        # Some managed sandboxes permit unlink but prohibit rmdir on fixture
        # role directories; that must not turn passing logic tests into errors.
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.repository = Path(self.temporary.name)
        self.control = self.repository / ".caprmedio_caprmedio"
        self.control.mkdir()
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            '[artifacts.identity]\nproject_prefix = "CA"\n', encoding="utf-8"
        )
        self.requirement = self._atom(
            "04_requirement/CAPRMEDIO-REQU-030-REQUIREMENT--old-rule.md",
            "---\nversion: 2\nupdated_at: 2026-09-01 00:00:00 +0400\n---\n# Old rule\nLegacy body.\n",
        )
        self.current = self._atom(
            "05_method/CA-M-100-CORE-METHOD--new-rule.md",
            "---\nversion: 1\ncce_version: cce_1\ncce_form: method\nsubjects:\n  governs: []\n---\n# New rule\n**to** act, do this.\n",
        )
        self._atom(
            "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/04_requirement/CA-R-101-REQUIREMENT--projection.md",
            "---\nversion: 1\n---\nGenerated projection.\n",
        )
        self.source = self.requirement.relative_to(self.repository).as_posix()

    def _atom(self, relative: str, content: str) -> Path:
        path = self.control / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def _decision(self, report: dict) -> dict:
        result = migration.decision_template(report)
        row = result["decisions"][0]
        row["new_atom_id"] = "CA-R-200"
        row["destination_path"] = ".caprmedio_caprmedio/04_requirement/CA-R-200-REQUIREMENT--old-rule.md"
        row["cce_disposition"] = "separate_one_atom_cce_migration"
        row["relation_disposition"] = "review_and_rebind"
        return result

    def test_inventory_is_authoritative_and_complete(self) -> None:
        report = migration.inventory(self.repository)
        self.assertEqual(report["active_rmedo_count"], 2)
        self.assertEqual(report["candidate_count"], 1)
        self.assertEqual([item["source_path"] for item in report["carriers"]], [self.source, self.current.relative_to(self.repository).as_posix()])
        self.assertEqual(report["counts_by_role"]["R"], 1)
        self.assertEqual(report["counts_by_role"]["M"], 1)
        self.assertEqual(report["carriers"][0]["filename_identity"], "CAPRMEDIO-REQU-030")
        self.assertFalse(migration._is_source(self.control / "04_requirement/archive/archived.md", self.control))

    def test_validated_plan_changes_no_carrier(self) -> None:
        report = migration.inventory(self.repository)
        before = self.requirement.read_bytes()
        result = migration.validate_decisions(report, self._decision(report), self.repository)
        self.assertFalse(result["apply_supported"])
        self.assertEqual(result["candidate_count"], 1)
        self.assertEqual(self.requirement.read_bytes(), before)
        self.assertFalse((self.control / "04_requirement/CA-R-200-REQUIREMENT--old-rule.md").exists())

    def test_frontier_drift_refuses(self) -> None:
        report = migration.inventory(self.repository)
        decisions = self._decision(report)
        self.requirement.write_text(self.requirement.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")
        with self.assertRaisesRegex(migration.MigrationPreparationError, "frontier changed"):
            migration.validate_decisions(migration.inventory(self.repository), decisions, self.repository)

    def test_incomplete_decision_and_collision_refuse(self) -> None:
        report = migration.inventory(self.repository)
        decisions = self._decision(report)
        decisions["decisions"] = []
        with self.assertRaisesRegex(migration.MigrationPreparationError, "coverage incomplete"):
            migration.validate_decisions(report, decisions, self.repository)
        decisions = self._decision(report)
        decisions["decisions"][0]["new_atom_id"] = "CA-M-100"
        with self.assertRaisesRegex(migration.MigrationPreparationError, "invalid or colliding"):
            migration.validate_decisions(report, decisions, self.repository)

    def test_semantic_migration_cannot_be_claimed_as_current(self) -> None:
        report = migration.inventory(self.repository)
        decisions = self._decision(report)
        decisions["decisions"][0]["cce_disposition"] = "already_current"
        with self.assertRaisesRegex(migration.MigrationPreparationError, "separate one-Atom migration"):
            migration.validate_decisions(report, decisions, self.repository)

    def test_destination_escape_refuses(self) -> None:
        report = migration.inventory(self.repository)
        decisions = self._decision(report)
        decisions["decisions"][0]["destination_path"] = ".caprmedio_caprmedio/../outside/CA-R-200-REQUIREMENT--old-rule.md"
        with self.assertRaisesRegex(migration.MigrationPreparationError, "normalized repository-relative"):
            migration.validate_decisions(report, decisions, self.repository)

    def test_template_can_round_trip_as_json(self) -> None:
        report = migration.inventory(self.repository)
        template = migration.decision_template(report)
        self.assertEqual(json.loads(json.dumps(template))["frontier_sha256"], report["frontier_sha256"])


if __name__ == "__main__":
    unittest.main()
