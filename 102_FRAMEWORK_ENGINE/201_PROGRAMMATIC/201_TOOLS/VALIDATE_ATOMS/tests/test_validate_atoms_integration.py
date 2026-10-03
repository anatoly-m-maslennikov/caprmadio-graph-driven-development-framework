"""Real-command safety and selection tests; no live Project carrier access."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import shutil
from typing import Any
import yaml

HERE = Path(__file__).resolve().parent
COMMAND = HERE.parent / "validate_atoms.py"


class IntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(
            tempfile.mkdtemp(
                dir=HERE.parents[4] / ".caprmedio_tmp", prefix="validator-integration-"
            )
        )
        (self.root / "atoms").mkdir()
        (self.root / "authority").mkdir()
        self.target = self.root / "atoms" / "misleading-name.md"
        self.target.write_text(
            "---\natom_id: MOCK-R-1\nversion: 1\nstatus: Active\n"
            "current_scope_unit: TEST\nlocal_tier: Standard\n"
            "global_tier: 2\n---\n# Summary\n\nTest\n\n## Claim\n\nTest.\n"
        )
        self.request: dict[str, Any] = dict(
            schema_version=1,
            source_roots=[str(self.root / "atoms")],
            allowed_read_roots=[str(self.root)],
            methodology=dict(kind="sources", roots=[str(self.root / "authority")]),
            selection=dict(atoms=[dict(carrier_path=str(self.target))]),
            limits=dict(
                max_candidates=100,
                max_file_bytes=1_000_000,
                max_total_read_bytes=10_000_000,
                timeout_seconds=30,
                max_findings=1000,
            ),
        )

    def run_tool(self) -> dict[str, Any]:
        before = self.fingerprint()
        result = subprocess.run(
            [sys.executable, str(COMMAND), "--input", "-"],
            input=json.dumps(self.request),
            text=True,
            capture_output=True,
            timeout=40,
        )
        self.assertEqual(before, self.fingerprint())
        report: dict[str, Any] = json.loads(result.stdout)
        self.assertEqual(
            result.returncode,
            {"valid": 0, "invalid": 1, "incomplete": 2, "error": 3}[report["result"]],
        )
        self.assertNotIn("Traceback", result.stderr)
        return report

    def fingerprint(self) -> dict[str, str]:
        return {
            str(p): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in self.root.rglob("*")
            if p.is_file() and not p.is_symlink()
        }

    def test_absent_authority_is_not_a_pass_and_repeatable(self) -> None:
        first = self.run_tool()
        self.assertEqual(first["result"], "incomplete")
        self.assertEqual(first["selection"]["selected"], [str(self.target)])
        self.assertTrue(first["coverage"]["gaps"])
        self.assertEqual(first, self.run_tool())

    def test_bad_yaml_retains_failure_with_incomplete_authority(self) -> None:
        self.target.write_text("---\nstatus: Active\nstatus: Draft\n---\n# Summary\n")
        report = self.run_tool()
        self.assertEqual(report["result"], "incomplete")
        self.assertIn("YAML_DUPLICATE_KEY", [f["code"] for f in report["findings"]])

    def test_file_limit_never_passes(self) -> None:
        self.request["limits"]["max_file_bytes"] = 1
        report = self.run_tool()
        self.assertEqual(report["result"], "incomplete")
        self.assertEqual(report["execution"]["stopped_by"], "max_file_bytes")

    def test_empty_membership_never_passes(self) -> None:
        self.request["selection"] = {"atoms": [{"atom_id": "MISSING"}]}
        report = self.run_tool()
        self.assertEqual(report["result"], "incomplete")
        self.assertEqual(report["coverage"]["targets"]["selected"], 0)
        self.assertTrue(report["selection"]["unresolved"])

    def test_explicit_selection_intersects_tiers(self) -> None:
        self.request["selection"]["global_tiers"] = [3]
        report = self.run_tool()
        self.assertEqual(report["selection"]["selected"], [])
        self.assertEqual(len(report["selection"]["excluded"]), 1)

    def test_missing_tier_is_unresolved_not_excluded(self) -> None:
        self.target.write_text("---\natom_id: MOCK-R-1\nversion: 1\n---\n# Summary\n")
        self.request["selection"]["global_tiers"] = [2]
        report = self.run_tool()
        self.assertTrue(report["selection"]["unresolved"])

    def test_protected_locator_never_read(self) -> None:
        self.request["selection"] = {"atoms": [{"carrier_path": str(self.root / ".env")}]}
        report = self.run_tool()
        self.assertNotEqual(report["result"], "valid")
        self.assertTrue(report["coverage"]["gaps"] or report["selection"]["unresolved"])

    def test_symlink_escape_never_read(self) -> None:
        target = self.root / "atoms" / "outside.md"
        target.symlink_to("/etc/hosts")
        self.request["selection"] = {"atoms": [{"carrier_path": str(target)}]}
        report = self.run_tool()
        self.assertNotEqual(report["result"], "valid")
        self.assertTrue(report["coverage"]["gaps"] or report["selection"]["unresolved"])

    def bind_authority(self) -> None:
        frontier = []
        for source in (HERE / "fixtures" / "authority_checks").glob("*.md"):
            target = self.root / "authority" / source.name
            shutil.copyfile(source, target)
            raw = source.read_bytes()
            metadata = yaml.safe_load(raw.decode().split("---", 2)[1])
            frontier.append(
                dict(
                    atom_id=source.stem,
                    version=metadata["version"],
                    path=str(target),
                    sha256=hashlib.sha256(raw).hexdigest(),
                )
            )
        self.request["methodology"]["frontier"] = frontier

    def test_known_good_primitives_with_real_bound_authority(self) -> None:
        self.bind_authority()
        self.target.write_text(
            "---\natom_id: MOCK-R-1\nversion: 1\nstatus: Active\n"
            "content_role: Requirement\ntype: Boundary\ncurrent_scope_unit: TEST\n"
            "claim_target_scope_unit: TEST\nauthor: Test Operator\n"
            'local_tier: Standard\nglobal_tier: 2\nupdated_at: "2026-09-24T00:00:00Z"\n'
            "subjects: {governs: Test Entity, depends_on: []}\nrelations: {}\n"
            "---\n# Summary\n\nTest boundary\n\n## Scope\n\nThe selected value.\n\n## Claim\n\nthe value **must** be stable.\n## Details\n"
        )
        report = self.run_tool()
        self.assertEqual(report["result"], "incomplete")
        self.assertGreater(report["coverage"]["outcomes"]["passed"], 5)
        self.assertEqual(report["coverage"]["outcomes"]["failed"], 0)

    def test_multiple_real_carrier_errors_are_all_retained(self) -> None:
        self.bind_authority()
        self.target.write_text(
            "---\nversion: false\nauthor: [A, B]\n"
            "cce_form: obligation\nsubjects: {governs: [A, B]}\n---\n# Summary\n\nBad\n"
        )
        report = self.run_tool()
        self.assertEqual(report["result"], "incomplete")
        codes = {f["code"] for f in report["findings"]}
        self.assertIn("PROPERTY_RETIRED", codes)
        self.assertIn("PROPERTY_TYPE", codes)
        self.assertIn("PROPERTY_REQUIRED", codes)
        self.assertGreater(report["coverage"]["outcomes"]["failed"], 2)


if __name__ == "__main__":
    unittest.main()
