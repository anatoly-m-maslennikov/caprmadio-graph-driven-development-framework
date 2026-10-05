"""Accepted D566/D567/E572@2 v2 contract tests using real local evidence.

Disposable local fixtures prove validation, not a full release or actual image.
"""

from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path

from pydantic import ValidationError


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_contract import (  # noqa: E402
    CandidateSnapshotManifest,
    CandidateBuildRequest,
    ReleaseContractError,
    candidate_snapshot_manifest_sha256,
)
from release_handoff_fixture import (  # noqa: E402
    ReleaseFixture,
    canonical_bytes,
    independent_checksum,
    reseal,
)


class ReleaseContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.fixture = ReleaseFixture(Path(self.temporary.name))
        self.manifest = copy.deepcopy(self.fixture.manifest)

    def _parse(self, manifest: dict | None = None):
        return CandidateSnapshotManifest.model_validate(self.manifest if manifest is None else manifest)

    def _reject(self, manifest: dict) -> None:
        with self.assertRaises((ValidationError, ReleaseContractError)):
            self._parse(manifest)

    def test_complete_v2_input_has_exact_members_and_observed_source_modes(self) -> None:
        before = self.fixture.snapshot()
        parsed = self._parse()
        encoded = parsed.model_dump(mode="json", by_alias=True)
        self.assertEqual(set(encoded), {
            "schema", "sha256", "executing_release", "candidate_release",
            "canonical_source_snapshot_ref", "canonical_source_snapshot_digest",
            "project_structure_digest", "framework_settings_digest", "source_frontier_digest",
            "nested_source_recursive_sha256_before", "expected_derived_source_copy_sha256",
            "expected_compiled_output_sha256", "full_suite_environment", "skill_target",
            "candidate_image", "source_inventory_rows",
        })
        self.assertEqual(encoded["schema"], "caprmedio.release_version.candidate.v2")
        self.assertEqual({row["resource"] for row in encoded["source_inventory_rows"]}, {
            "FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL", "IMAGE_INPUT",
        })
        for row in encoded["source_inventory_rows"]:
            self.assertEqual(set(row), {
                "resource", "source_path", "source_sha256", "source_mode", "destination_path",
            })
            self.assertEqual(row["source_mode"], (self.fixture.root / row["source_path"]).stat().st_mode & 0o777)
        self.assertEqual(self.fixture.snapshot(), before)

    def test_checksum_is_independent_canonical_utf8_and_excludes_itself(self) -> None:
        expected = independent_checksum(self.manifest)
        self.assertEqual(candidate_snapshot_manifest_sha256(self.manifest), expected)
        self.assertIn("λ".encode("utf-8"), canonical_bytes(self.manifest))
        self.assertNotIn(b"\\u03bb", canonical_bytes(self.manifest))
        normalized = self._parse().model_dump(mode="json", by_alias=True)
        self.assertEqual(normalized["sha256"], expected)
        self.assertEqual(normalized["source_inventory_rows"], sorted(
            self.manifest["source_inventory_rows"],
            key=lambda row: (row["destination_path"], row["source_path"], row["source_sha256"]),
        ))

    def test_checksum_and_normalization_ignore_dictionary_and_inventory_order(self) -> None:
        reversed_manifest = dict(reversed(list(self.manifest.items())))
        reversed_manifest["source_inventory_rows"] = list(reversed(self.manifest["source_inventory_rows"]))
        self.assertEqual(candidate_snapshot_manifest_sha256(reversed_manifest), independent_checksum(self.manifest))
        first = self._parse().model_dump(mode="json", by_alias=True)
        second = self._parse(reversed_manifest).model_dump(mode="json", by_alias=True)
        self.assertEqual(first, second)

    def test_missing_or_forged_checksum_is_rejected(self) -> None:
        for checksum in (None, "0" * 64, "A" * 64, "a" * 63):
            with self.subTest(checksum=checksum):
                changed = copy.deepcopy(self.manifest)
                if checksum is None:
                    del changed["sha256"]
                else:
                    changed["sha256"] = checksum
                self._reject(changed)

    def test_all_required_manifest_fields_are_required(self) -> None:
        for field in self.manifest:
            with self.subTest(field=field):
                changed = copy.deepcopy(self.manifest)
                del changed[field]
                self._reject(changed)

    def test_future_expectations_do_not_admit_actual_or_gate_fields(self) -> None:
        self._parse()
        for field in (
            "actual_derived_source_copy_sha256", "actual_compiled_output_sha256",
            "nested_source_recursive_sha256_after", "package_rows", "compiler_result",
            "installed_selection", "image_execution", "gate_evidence_refs", "rows",
        ):
            with self.subTest(field=field):
                self._reject(reseal({**self.manifest, field: "forged success"}))

    def test_substituted_bindings_with_old_checksum_are_rejected(self) -> None:
        for field in (
            "executing_release", "candidate_release", "canonical_source_snapshot_ref",
            "canonical_source_snapshot_digest", "project_structure_digest", "framework_settings_digest",
            "source_frontier_digest", "nested_source_recursive_sha256_before",
            "expected_derived_source_copy_sha256", "expected_compiled_output_sha256",
        ):
            with self.subTest(field=field):
                changed = copy.deepcopy(self.manifest)
                changed[field] = "0" * 64 if field.endswith(("digest", "sha256", "before")) else "substituted"
                self._reject(changed)

    def test_source_and_destination_paths_refuse_unsafe_or_noncanonical_forms(self) -> None:
        for field in ("source_path", "destination_path"):
            for path in ("../escape", "/absolute", "a/../b", "a//b", "a/./b", "a\\b", "a/", " a", ".", ""):
                with self.subTest(field=field, path=path):
                    changed = copy.deepcopy(self.manifest)
                    changed["source_inventory_rows"][0][field] = path
                    self._reject(reseal(changed))

    def test_modes_are_strict_masked_permission_bits_not_caller_policy(self) -> None:
        for mode in (-1, 0o1000, 0o100644, True, "644", None):
            with self.subTest(mode=mode):
                changed = copy.deepcopy(self.manifest)
                changed["source_inventory_rows"][0]["source_mode"] = mode
                self._reject(reseal(changed))

    def test_duplicate_inventory_and_destination_collision_are_rejected(self) -> None:
        changed = copy.deepcopy(self.manifest)
        changed["source_inventory_rows"].append(copy.deepcopy(changed["source_inventory_rows"][0]))
        self._reject(reseal(changed))
        changed = copy.deepcopy(self.manifest)
        changed["source_inventory_rows"][7]["destination_path"] = changed["source_inventory_rows"][6]["destination_path"]
        self._reject(reseal(changed))

    def test_tools_only_missing_framework_resources_and_ca_files_are_rejected(self) -> None:
        for resources in ({"FRAMEWORK_ENGINE"}, {"METHODOLOGY"}, {"SKILL"}, {"IMAGE_INPUT"}):
            with self.subTest(resources=resources):
                changed = copy.deepcopy(self.manifest)
                changed["source_inventory_rows"] = [row for row in changed["source_inventory_rows"] if row["resource"] not in resources]
                self._reject(reseal(changed))
        for missing in ("SKILLS/ca/SKILL.md", "SKILLS/ca/agents/openai.yaml"):
            with self.subTest(missing=missing):
                changed = copy.deepcopy(self.manifest)
                changed["source_inventory_rows"] = [row for row in changed["source_inventory_rows"] if row["destination_path"] != missing]
                self._reject(reseal(changed))
        changed = copy.deepcopy(self.manifest)
        changed["source_inventory_rows"] = [row for row in changed["source_inventory_rows"] if row["resource"] != "FRAMEWORK_ENGINE" or "/201_TOOLS/" in row["source_path"]]
        self._reject(reseal(changed))

    def test_suite_skill_and_image_targets_are_bound_and_safe(self) -> None:
        for field, replacement in (
            ("full_suite_environment", {"runner": "full-suite", "command": [], "working_directory": "."}),
            ("full_suite_environment", {"runner": "full-suite", "command": ["test"], "working_directory": "../escape"}),
            ("skill_target", ".agents/skills/other"),
            ("candidate_image", {**self.manifest["candidate_image"], "dockerfile_path": "other/Dockerfile"}),
        ):
            with self.subTest(field=field):
                self._reject(reseal({**self.manifest, field: replacement}))

    def test_build_intent_refuses_missing_fields_and_effect_authority_overrides(self) -> None:
        intent = {
            key: self.manifest[key]
            for key in ("candidate_release", "expected_derived_source_copy_sha256", "expected_compiled_output_sha256", "full_suite_environment")
        }
        intent["candidate_image_reference"] = self.manifest["candidate_image"]["candidate_image_reference"]
        CandidateBuildRequest.model_validate(intent)
        for field in intent:
            with self.subTest(missing=field):
                changed = copy.deepcopy(intent)
                del changed[field]
                with self.assertRaises(ValidationError):
                    CandidateBuildRequest.model_validate(changed)
        for field in ("source_root", "output_path", "source_patch", "journal_payload", "run_event", "image_prune", "sealed_authority", "package_rows", "source_inventory_rows", "actual_compiled_output_sha256"):
            with self.subTest(forbidden=field), self.assertRaises(ValidationError):
                CandidateBuildRequest.model_validate({**intent, field: "forged"})

    def test_same_executing_and_candidate_release_is_not_a_release(self) -> None:
        self._reject(reseal({**self.manifest, "candidate_release": "N"}))


if __name__ == "__main__":
    unittest.main()
