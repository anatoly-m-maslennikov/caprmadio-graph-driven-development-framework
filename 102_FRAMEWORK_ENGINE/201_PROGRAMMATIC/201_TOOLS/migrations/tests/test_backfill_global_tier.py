"""Tier derivation and end-to-end safe migration regression tests."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DIRECTORY))


class TierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("tier_fixer", DIRECTORY / "backfill_global_tier.py")
        cls.tool = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.tool)

    def setUp(self):
        self.context = {"project": "project", "parents": {"project": None, "L1": "project",
                        "SOURCES": "L1", "CORE": "SOURCES", "CONFIG": "SOURCES"},
                        "operators": ["Anatoly"], "evidence": "Explicit migration context"}

    def test_project_and_nonproject_golden_values(self):
        golden = {"project": {"Principle": 0, "Core": 1, "Standard": 2},
                  "L1": {"Core": 3, "General": 4, "Standard": 5},
                  "SOURCES": {"Core": 6, "General": 7, "Standard": 8},
                  "CORE": {"Core": 9, "General": 10, "Standard": 11},
                  "CONFIG": {"Core": 9, "General": 10, "Standard": 11}}
        for unit, tiers in golden.items():
            for local, expected in tiers.items():
                with self.subTest(unit=unit, local=local):
                    self.assertEqual(self.tool.derive_tier({"current_scope_unit": unit, "local_tier": local}, self.context), expected)

    def test_owner_not_claim_target(self):
        self.assertEqual(self.tool.derive_tier({"current_scope_unit": "SOURCES", "local_tier": "Standard",
                         "claim_target_scope_unit": "CORE", "type": "Goal"}, self.context), 8)

    def test_external_project_goal(self):
        atom = {"current_scope_unit": "Anatoly", "content_role": "Requirement", "type": "Goal",
                "claim_target_scope_unit": "project"}
        self.assertEqual(self.tool.derive_tier(atom, self.context), -1)
        with self.assertRaises(ValueError):
            self.tool.derive_tier(dict(atom, local_tier="Standard"), self.context)

    def test_no_location_or_omission_defaults(self):
        for metadata in ({"local_tier": "Core"}, {"current_scope_unit": "CORE"},
                         {"current_scope_unit": "missing", "local_tier": "Core"},
                         {"current_scope_unit": "CORE", "local_tier": "Principle"},
                         {"current_scope_unit": "project", "local_tier": "General"},
                         {"current_scope_unit": "CORE", "local_tier": None}):
            with self.subTest(metadata=metadata), self.assertRaises(ValueError):
                self.tool.derive_tier(metadata, self.context)

    def test_cycles_missing_parents_and_wrong_root_rejected(self):
        for parents in ({"project": None, "A": "A"}, {"project": None, "A": "missing"},
                        {"project": "A", "A": None}, {"project": None, "A": None}):
            with self.subTest(parents=parents), self.assertRaises(ValueError):
                self.tool.validate_context(dict(self.context, parents=parents))

    def test_double_digit_depth(self):
        context = copy.deepcopy(self.context)
        context["parents"] = {"project": None}
        for number in range(1, 13):
            context["parents"][f"L{number}"] = "project" if number == 1 else f"L{number-1}"
        self.assertEqual(self.tool.derive_tier({"current_scope_unit": "L12", "local_tier": "Standard"}, context), 38)

    def test_real_cli_and_idempotency(self):
        root = Path(tempfile.mkdtemp(prefix="global-tier-test-", dir=DIRECTORY.parents[3] / ".caprmedio_tmp"))
        atom = root / "arbitrary-name.md"
        before = b'---\nversion: 1\ncurrent_scope_unit: CORE\nlocal_tier: General\nstatus: Active\nupdated_at: "2026-09-25T00:00:00Z"\n---\n# Untouched body\n'
        atom.write_bytes(before)
        request = {"source_root": str(root), "scope_context": self.context,
                   "carriers": [{"path": str(atom), "sha256": self.tool.safe._digest(before)}]}
        request_file = root / "request.json"
        request_file.write_text(json.dumps(request))
        plan = root / "plan.json"
        command = [sys.executable, "-B", str(DIRECTORY / "backfill_global_tier.py")]
        def run(*args):
            result = subprocess.run(command + list(args), capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            return result
        run("--input", str(request_file), "--output", str(plan))
        self.assertEqual(atom.read_bytes(), before)
        run("--apply", str(plan), "--output", str(root / "receipt.json"))
        after = atom.read_bytes()
        self.assertEqual(after, before.replace(b"version: 1", b"version: 2").replace(b"---\n# Untouched", b"global_tier: 10\n---\n# Untouched"))
        self.assertEqual((root / "archive/arbitrary-name@1.md").read_bytes(), before)
        run("--apply", str(plan), "--output", str(root / "repeat.json"))
        self.assertEqual(atom.read_bytes(), after)
        self.assertEqual(json.loads((root / "repeat.json").read_text())["counts"]["applied"], 0)

    def test_existing_tier_mismatch_refuses_overwrite(self):
        with self.assertRaises(ValueError):
            self.tool.missing_tier({"current_scope_unit": "CORE", "local_tier": "Core", "global_tier": 1}, self.context)
        self.assertIsNone(self.tool.missing_tier({"current_scope_unit": "CORE", "local_tier": "Core", "global_tier": 9}, self.context))

    def test_existing_boolean_not_integer(self):
        with self.assertRaises(ValueError):
            self.tool.missing_tier({"current_scope_unit": "project", "local_tier": "Core", "global_tier": True}, self.context)

    def fixture_plan(self):
        root = Path(tempfile.mkdtemp(prefix="tier-safety-", dir=DIRECTORY.parents[3] / ".caprmedio_tmp"))
        atom = root / "atom.md"
        before = b'---\nversion: 1\ncurrent_scope_unit: CORE\nlocal_tier: Core\nstatus: Active\n---\nBody\n'
        atom.write_bytes(before)
        request = {"source_root": str(root), "scope_context": self.context,
                   "carriers": [{"path": str(atom), "sha256": self.tool.safe._digest(before)}]}
        raw = json.dumps(request).encode()
        request_path = root / "request.json"
        request_path.write_bytes(raw)
        return self.tool.build_plan(request, request_path, raw), atom, before, request_path

    def test_altered_request_blocks_apply(self):
        plan, atom, before, request = self.fixture_plan()
        request.write_text(request.read_text() + " ")
        with self.assertRaises(ValueError):
            self.tool.apply_plan(plan)
        self.assertEqual(atom.read_bytes(), before)

    def test_stale_atom_blocks_apply(self):
        plan, atom, before, _ = self.fixture_plan()
        atom.write_bytes(before + b"Concurrent change")
        with self.assertRaises(ValueError):
            self.tool.apply_plan(plan)
        self.assertFalse((atom.parent / "archive").exists())

    def test_wrong_planned_tier_is_rederived_and_rejected(self):
        plan, atom, before, _ = self.fixture_plan()
        plan["property_plan"]["changes"][0]["fields"]["global_tier"]["value"] = 11
        with self.assertRaises(ValueError):
            self.tool.apply_plan(plan)
        self.assertEqual(atom.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
