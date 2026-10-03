"""Golden and real-file safety tests for evidence-backed missing-field migration."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DIRECTORY))


class BackfillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("backfill", DIRECTORY / "backfill_required_atom_properties.py")
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def setUp(self):
        # Retain disposable fixtures: managed desktops can prohibit rmdir.
        self.root = Path(tempfile.mkdtemp(prefix="backfill-test-", dir=DIRECTORY.parents[3] / ".caprmedio_tmp"))
        self.path = self.root / "CA-R-1.md"
        self.raw = b'---\nversion: 2\nupdated_at: "2026-09-25T00:00:00Z"\nsubjects: {governs: Atom}\n---\n# Same claim\n'
        self.path.write_bytes(self.raw)
        self.fields = {"atom_id": {"value": "CA-R-1", "evidence": "legacy explicit filename identity"}}
        self.report = {"carriers": [{"path": str(self.path), "sha256": self.module.safe._digest(self.raw)}],
                       "findings": [{"path": str(self.path), "code": "PROPERTY_REQUIRED", "property": "atom_id"}]}
        self.evidence = {"carriers": {str(self.path): self.fields}}

    def plan(self):
        return self.module.build_plan(self.report, self.root, b"report", self.evidence)

    def test_golden_preserves_body_timestamp_and_old_metadata(self):
        actual = self.module.add_properties(self.raw, {"atom_id": "CA-R-1"})
        expected = self.raw.replace(b'---\n# Same claim', b'atom_id: "CA-R-1"\n---\n# Same claim')
        self.assertEqual(actual, expected)
        self.assertEqual(self.module.add_properties(actual, {}), actual)

    def test_crlf_unicode(self):
        raw = self.raw.replace(b"\n", b"\r\n")
        result = self.module.add_properties(raw, {"author": "Anatoly Масленников"})
        self.assertNotIn(b"\n", result.replace(b"\r\n", b""))
        self.assertIn('Масленников'.encode(), result)

    def test_never_overwrites_existing_even_null(self):
        for value in ("null", "CA-R-2", '""'):
            raw = self.raw.replace(b"version:", f"atom_id: {value}\nversion:".encode())
            with self.assertRaises(ValueError):
                self.module.add_properties(raw, {"atom_id": "CA-R-1"})

    def test_unsupported_or_invalid_value(self):
        for fields in ({"surprise": "yes"}, {"global_tier": True}, {"type": ""},
                       {"author": ["one", "two"]}, {"global_tier": "9"}, {"status": None}):
            with self.subTest(fields=fields), self.assertRaises(ValueError):
                self.module.add_properties(self.raw, fields)

    def test_ambiguous_yaml_and_draft_identity_refused(self):
        for raw in (self.raw.replace(b"version: 2", b"version: 2\nversion: 3"),
                    self.raw.replace(b"version: 2", b"version: &v 2"),
                    self.raw.replace(b"version: 2", b"status: Draft\nversion: 2")):
            with self.assertRaises(ValueError):
                self.module.add_properties(raw, {"atom_id": "CA-R-1"})

    def test_preview_apply_archive_and_repeat(self):
        plan = self.plan()
        self.assertEqual(self.path.read_bytes(), self.raw)
        self.assertFalse(plan["blockers"])
        receipt = self.module.apply_plan(plan, self.root)
        self.assertEqual(receipt["counts"]["applied"], 1)
        expected = self.module.add_properties(self.raw, {"atom_id": "CA-R-1"}).replace(b"version: 2", b"version: 3")
        self.assertEqual(self.path.read_bytes(), expected)
        self.assertEqual((self.root / "archive/CA-R-1@2.md").read_bytes(), self.raw)
        self.assertEqual(self.module.apply_plan(plan, self.root)["counts"]["applied"], 0)

    def test_unknown_value_stays_missing(self):
        self.report["findings"].append({"path": str(self.path), "code": "PROPERTY_REQUIRED", "property": "global_tier"})
        plan = self.plan()
        self.assertEqual(plan["unresolved"], [{"path": str(self.path), "property": "global_tier"}])
        self.assertNotIn("global_tier:", plan["changes"][0]["after"])

    def test_evidence_must_be_nonempty_and_reported_missing(self):
        self.fields["atom_id"]["evidence"] = ""
        self.assertTrue(self.plan()["blockers"])
        self.fields["atom_id"]["evidence"] = "legacy"
        self.fields["author"] = {"value": "Anatoly", "evidence": "default"}
        self.assertTrue(self.plan()["blockers"])

    def test_stale_report_or_entire_baseline_aborts(self):
        self.path.write_bytes(self.raw + b"changed")
        self.assertTrue(self.plan()["blockers"])
        self.path.write_bytes(self.raw)
        other = self.root / "other.md"
        other.write_bytes(self.raw)
        self.report["carriers"].append({"path": str(other), "sha256": self.module.safe._digest(self.raw)})
        plan = self.plan()
        other.write_bytes(self.raw + b"changed")
        with self.assertRaises(ValueError):
            self.module.apply_plan(plan, self.root)
        self.assertEqual(self.path.read_bytes(), self.raw)
        self.assertFalse((self.root / "archive").exists())

    def test_tampered_after_cannot_write(self):
        plan = copy.deepcopy(self.plan())
        change = plan["changes"][0]
        change["after"] = change["after"].replace("Same claim", "Another claim")
        change["after_sha256"] = self.module.safe._digest(change["after"].encode())
        with self.assertRaises(ValueError):
            self.module.apply_plan(plan, self.root)
        self.assertEqual(self.path.read_bytes(), self.raw)

    def test_archive_collision_refuses_entire_plan(self):
        (self.root / "archive").mkdir()
        (self.root / "archive/CA-R-1@2.md").write_text("different history")
        self.assertTrue(self.plan()["blockers"])

    def test_plan_round_trip(self):
        plan = json.loads(json.dumps(self.plan()))
        self.assertEqual(self.module.apply_plan(plan, self.root)["counts"]["applied"], 1)

    def test_real_cli_and_existing_output_refusal(self):
        report = self.root / "report.json"
        evidence = self.root / "evidence.json"
        plan = self.root / "plan.json"
        receipt = self.root / "receipt.json"
        report.write_text(json.dumps(self.report))
        evidence.write_text(json.dumps(self.evidence))
        command = [sys.executable, "-B", str(DIRECTORY / "backfill_required_atom_properties.py")]
        preview = subprocess.run(command + ["--report", str(report), "--source-root", str(self.root),
                                 "--evidence", str(evidence), "--output", str(plan)], capture_output=True, text=True)
        self.assertEqual(preview.returncode, 0, preview.stderr)
        refused = subprocess.run(command + ["--apply", str(plan), "--output", str(plan)], capture_output=True)
        self.assertNotEqual(refused.returncode, 0)
        self.assertEqual(self.path.read_bytes(), self.raw)
        applied = subprocess.run(command + ["--apply", str(plan), "--output", str(receipt)], capture_output=True, text=True)
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertEqual(json.loads(receipt.read_text())["counts"]["applied"], 1)


if __name__ == "__main__":
    unittest.main()
