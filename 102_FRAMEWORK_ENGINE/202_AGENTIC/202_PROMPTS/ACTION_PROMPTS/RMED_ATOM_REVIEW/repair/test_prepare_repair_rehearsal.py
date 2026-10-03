"""Regression tests for deterministic, optional-Type repair rehearsal inputs."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE / "tests"), str(HERE.parent)]
from prepare_repair_rehearsal import (  # noqa: E402
    CASES, FIXTURE_ROOT, REPAIR_AUTHORITY_IDS, REPOSITORY_ROOT, build, rewrite_fixture,
)
from context_builder import markdown, metadata  # noqa: E402


class PrepareRepairRehearsalTests(unittest.TestCase):
    def test_rewrite_elides_only_generic_type_and_known_formatting_normalization(self):
        for spec in CASES:
            original, raw = rewrite_fixture(spec)
            before = metadata(original)
            expected = dict(before)
            expected.update({
                "atom_id": spec["atom_id"],
                "version": spec["version"],
                "updated_at": "2026-09-26T12:00:00Z",
                "current_scope_unit": "SYNTHETIC",
                "claim_target_scope_unit": "SYNTHETIC",
                "author": "Synthetic Fixture Operator",
            })
            expected["subjects"] = {**expected["subjects"], "depends_on": spec["depends_on"]}
            expected.pop("type")
            with self.subTest(case=spec["id"]):
                self.assertEqual(metadata(raw), expected)
                expected_body = markdown(original)
                if spec["id"] == "unbold_must_formatting":
                    expected_body = expected_body.replace(
                        "the Color of a Widget in a public display.",
                        "the Color of a Widget **in** a public display.",
                    ).replace(
                        "the Color of a Widget MUST be Blue.",
                        "the Color of a Widget must be Blue.",
                    )
                self.assertEqual(markdown(raw), expected_body)

    def test_build_emits_untyped_carriers_with_matching_permissions(self):
        before = {spec["fixture"]: hashlib.sha256((FIXTURE_ROOT / spec["fixture"]).read_bytes()).hexdigest()
                  for spec in CASES}
        temporary_root = REPOSITORY_ROOT / ".caprmedio_tmp"
        with tempfile.TemporaryDirectory(dir=temporary_root, ignore_cleanup_errors=True) as temporary:
            output = Path(temporary) / "rehearsal"
            build(output)
            repair_inputs = json.loads((output / "repair-inputs.json").read_text())
            packets = [json.loads((output / "packets" / f"{ordinal:04}.json").read_text())
                       for ordinal in range(1, len(CASES) + 1)]
            self.assertEqual([row["case_id"] for row in repair_inputs["cases"]],
                             [spec["id"] for spec in CASES])
            for spec, packet, repair_case in zip(CASES, packets, repair_inputs["cases"], strict=True):
                with self.subTest(case=spec["id"]):
                    self.assertEqual(packet["source"]["path"], spec["carrier_path"])
                    self.assertEqual(repair_case["permission"]["paths"], spec["permission_paths"])
                    self.assertIn(spec["carrier_path"], repair_case["permission"]["paths"])
                    self.assertNotIn("type", packet["properties"])
                    self.assertEqual(packet["properties"]["content_role"], "Requirement")
                    self.assertNotIn("-REQUIREMENT--", Path(spec["carrier_path"]).name)
                    self.assertEqual((output / spec["carrier_path"]).read_text(), packet["raw"])
        self.assertEqual(before, {
            spec["fixture"]: hashlib.sha256((FIXTURE_ROOT / spec["fixture"]).read_bytes()).hexdigest()
            for spec in CASES
        })

    def test_repair_authority_binds_optional_type_and_identity_boundaries(self):
        self.assertTrue({"CA-R-1766", "CA-R-1700", "CA-D-276", "CA-D-283"}
                        <= set(REPAIR_AUTHORITY_IDS))


if __name__ == "__main__":
    unittest.main()
