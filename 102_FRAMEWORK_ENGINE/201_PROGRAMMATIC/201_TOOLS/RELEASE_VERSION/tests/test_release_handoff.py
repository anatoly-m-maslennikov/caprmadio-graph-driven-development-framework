"""D567 local-observation refusal cases; no actual compiler/release proof."""

from __future__ import annotations

import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from pydantic import ValidationError

RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import (  # noqa: E402
    CompilerSuccessEvidence,
    build_validated_candidate,
    seal_candidate_compilation,
    tree_sha256,
    validate_source_copy,
)
from release_handoff_fixture import (  # noqa: E402
    CANONICAL_SOURCE,
    COMPILER,
    MATERIALIZED,
    ReleaseFixture,
    independent_checksum,
    digest,
    observed_tree_digest,
)


class ReleaseHandoffTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.fixture = ReleaseFixture(Path(self.temporary.name))

    def candidate(self):
        return build_validated_candidate(self.fixture.root, self.fixture.intent)

    def mocked_compiler_evidence(self, candidate):
        """Typed adapter fixture only, not an actually invoked compiler."""
        return CompilerSuccessEvidence(
            candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
            outcome="completed",
            compiler_entrypoint={"path": COMPILER, "sha256": digest((self.fixture.root / COMPILER).read_bytes())},
            compiler_frontier_digest=candidate.manifest.source_frontier_digest,
            child_materialization_root=f"{MATERIALIZED}/{candidate.manifest.sha256}",
            actual_compiled_output_sha256=candidate.manifest.expected_compiled_output_sha256,
        )

    def test_locally_observed_candidate_equals_independent_manifest_oracle_without_writes(self) -> None:
        before = self.fixture.snapshot()
        candidate = self.candidate()
        manifest = candidate.manifest.model_dump(mode="json", by_alias=True)
        self.assertEqual(manifest, self.fixture.manifest | {"source_inventory_rows": sorted(self.fixture.rows, key=lambda row: (row["destination_path"], row["source_path"], row["source_sha256"]))})
        self.assertEqual(manifest["sha256"], independent_checksum(manifest))
        self.assertEqual(candidate.authority.executing_release, "N")
        self.assertEqual(tree_sha256(self.fixture.root, CANONICAL_SOURCE), observed_tree_digest(self.fixture.root / CANONICAL_SOURCE))
        self.assertEqual(self.fixture.snapshot(), before)
        self.assertNotIn("actual_compiled_output_sha256", manifest)

    def test_raw_authority_and_package_success_mappings_are_not_build_intent(self) -> None:
        for field in ("sealed_authority", "authority", "package_rows", "compiler_success", "actual_compiled_output_sha256"):
            with self.subTest(field=field), self.assertRaises((ReleaseContractError, ValidationError)):
                build_validated_candidate(self.fixture.root, {**self.fixture.intent, field: {"forged": True}})

    def test_currentness_rejects_source_config_selection_and_mode_changes(self) -> None:
        for field in ("source", "settings", "structure", "selection", "mode"):
            with self.subTest(field=field):
                candidate = self.candidate()
                path = {"source": self.fixture.root / self.fixture.rows[0]["source_path"], "settings": self.fixture.settings, "structure": self.fixture.structure, "selection": self.fixture.selection, "mode": self.fixture.root / self.fixture.rows[0]["source_path"]}[field]
                original, mode = path.read_bytes(), path.stat().st_mode & 0o777
                if field == "mode":
                    path.chmod(0o600)
                else:
                    path.write_bytes(b"release = 'changed-N'\n" if field == "selection" else original + b"changed\n")
                try:
                    with self.assertRaises(ReleaseContractError) as raised:
                        validate_source_copy(candidate)
                    self.assertEqual(raised.exception.code, "release-currentness-stale")
                finally:
                    path.write_bytes(original)
                    path.chmod(mode)

    def test_missing_partial_and_mismatched_copy_refuse_before_compiler(self) -> None:
        candidate = self.candidate()
        with self.assertRaises(ReleaseContractError) as raised:
            validate_source_copy(candidate)
        self.assertEqual(raised.exception.code, "release-copy-missing")
        destination = self.fixture.deliver_copy()
        core = next(path for path in destination.rglob("*.md"))
        original = core.read_bytes()
        core.unlink()
        with self.assertRaises(ReleaseContractError) as raised:
            validate_source_copy(candidate)
        self.assertEqual(raised.exception.code, "release-copy-digest-mismatch")
        core.write_bytes(original + b"tampered\n")
        with self.assertRaises(ReleaseContractError) as raised:
            validate_source_copy(candidate)
        self.assertEqual(raised.exception.code, "release-copy-digest-mismatch")

    def test_complete_copy_is_observed_not_prefilled_and_preserves_n_and_authority(self) -> None:
        before = self.fixture.snapshot()
        candidate = self.candidate()
        self.fixture.deliver_copy()
        copied = validate_source_copy(candidate)
        self.assertEqual(copied.actual_derived_source_copy_sha256, self.fixture.manifest["expected_derived_source_copy_sha256"])
        self.assertEqual(copied.source_copy_root, "101_LAYER_1_FRAMEWORK_METHODOLOGY/sources")
        for relative, expected in before.items():
            path = self.fixture.root / relative
            self.assertEqual((path.read_bytes(), path.stat().st_mode & 0o777), expected)

    def test_unsafe_copy_and_child_materialization_roots_are_rejected(self) -> None:
        candidate = self.candidate()
        self.fixture.deliver_copy()
        copied = validate_source_copy(candidate)
        for wrong in ("../outside", CANONICAL_SOURCE, ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"):
            with self.subTest(copy_root=wrong), self.assertRaises((ReleaseContractError, ValueError)):
                validate_source_copy(candidate, wrong)
            with self.subTest(materialized_root=wrong), self.assertRaises((ReleaseContractError, ValueError)):
                seal_candidate_compilation(copied, self.mocked_compiler_evidence(candidate), wrong)

    def test_missing_or_mismatched_compiler_output_refuses_handoff(self) -> None:
        candidate = self.candidate()
        self.fixture.deliver_copy()
        copied = validate_source_copy(candidate)
        with self.assertRaises(ReleaseContractError) as raised:
            seal_candidate_compilation(copied, self.mocked_compiler_evidence(candidate))
        self.assertEqual(raised.exception.code, "release-compiler-output-missing")
        materialized = self.fixture.materialize_bytes(candidate.manifest.sha256)
        (materialized / "compiled.md").write_bytes(b"wrong compiled bytes\n")
        with self.assertRaises(ReleaseContractError) as raised:
            seal_candidate_compilation(copied, self.mocked_compiler_evidence(candidate))
        self.assertEqual(raised.exception.code, "release-compiler-output-mismatch")

    def test_stale_copy_after_validation_refuses_compiler_handoff(self) -> None:
        candidate = self.candidate()
        destination = self.fixture.deliver_copy()
        copied = validate_source_copy(candidate)
        self.fixture.materialize_bytes(candidate.manifest.sha256)
        (destination / "unexpected.md").write_bytes(b"extra unsealed copy\n")
        with self.assertRaises(ReleaseContractError) as raised:
            seal_candidate_compilation(copied, self.mocked_compiler_evidence(candidate))
        self.assertEqual(raised.exception.code, "release-copy-digest-mismatch")

    def test_forged_typed_authority_and_raw_copy_mapping_refuse(self) -> None:
        candidate = self.candidate()
        forged = replace(candidate, authority=candidate.authority.model_copy(update={"project_structure_digest": "0" * 64}))
        with self.assertRaises(ReleaseContractError):
            validate_source_copy(forged)
        with self.assertRaises((ReleaseContractError, TypeError, ValidationError)):
            validate_source_copy({"project_root": str(self.fixture.root), "authority": candidate.authority.model_dump()})
        with self.assertRaises((ReleaseContractError, TypeError, ValidationError)):
            seal_candidate_compilation({"candidate": candidate, "source_copy_root": "101_LAYER_1_FRAMEWORK_METHODOLOGY/sources"}, None)

    def test_symlinked_inventory_and_copy_cannot_be_current_evidence(self) -> None:
        target = self.fixture.root / self.fixture.rows[0]["source_path"]
        payload = target.read_bytes()
        target.unlink()
        target.symlink_to(self.fixture.structure)
        with self.assertRaises(ReleaseContractError):
            self.candidate()
        target.unlink()
        target.write_bytes(payload)
        candidate = self.candidate()
        copied_root = self.fixture.deliver_copy()
        copied_source = next(copied_root.rglob("*.md"))
        copied_source.unlink()
        copied_source.symlink_to(self.fixture.structure)
        with self.assertRaises(ReleaseContractError):
            validate_source_copy(candidate)

    def test_matching_handwritten_output_is_not_successful_compiler_invocation_evidence(self) -> None:
        candidate = self.candidate()
        self.fixture.deliver_copy()
        copied = validate_source_copy(candidate)
        self.fixture.materialize_bytes(candidate.manifest.sha256)
        # Actual local output bytes are present, but no compiler was invoked
        # and no successful compiler result exists. D567 forbids inferring it.
        with self.assertRaises(ReleaseContractError):
            seal_candidate_compilation(copied, None)

    def test_typed_mock_handoff_binds_actual_copy_output_and_observed_package_modes(self) -> None:
        candidate = self.candidate()
        self.fixture.deliver_copy()
        copied = validate_source_copy(candidate)
        materialized = self.fixture.materialize_bytes(candidate.manifest.sha256)
        before = self.fixture.snapshot()
        handoff = seal_candidate_compilation(copied, self.mocked_compiler_evidence(candidate))
        self.assertEqual(handoff.actual_compiled_output_sha256, observed_tree_digest(materialized))
        self.assertEqual(handoff.expected_compiled_output_sha256, candidate.manifest.expected_compiled_output_sha256)
        self.assertEqual(handoff.actual_derived_source_copy_sha256, handoff.expected_derived_source_copy_sha256)
        destinations = [row.destination_path for row in handoff.package_rows]
        self.assertEqual(destinations, sorted(destinations))
        self.assertIn("SKILLS/ca/references/usage.md", destinations)
        self.assertIn("METHODOLOGY/compiled/compiled.md", destinations)
        for row in handoff.package_rows:
            path = self.fixture.root / row.source_path
            self.assertEqual(row.sha256, digest(path.read_bytes()))
            self.assertEqual(row.mode, path.stat().st_mode & 0o777)
        self.assertEqual(self.fixture.snapshot(), before)

    def test_forged_raw_or_tampered_typed_compiler_evidence_cannot_seal(self) -> None:
        candidate = self.candidate()
        self.fixture.deliver_copy()
        copied = validate_source_copy(candidate)
        self.fixture.materialize_bytes(candidate.manifest.sha256)
        valid = self.mocked_compiler_evidence(candidate)
        with self.assertRaises(ReleaseContractError):
            seal_candidate_compilation(copied, valid.model_dump())
        for field, replacement in (
            ("candidate_snapshot_manifest_sha256", "0" * 64),
            ("compiler_frontier_digest", "0" * 64),
            ("child_materialization_root", "../unsealed"),
            ("actual_compiled_output_sha256", "0" * 64),
            ("outcome", "failed"),
            ("outcome", "pending"),
            ("outcome", "uncertain"),
        ):
            with self.subTest(field=field), self.assertRaises(ReleaseContractError):
                seal_candidate_compilation(copied, valid.model_copy(update={field: replacement}))


if __name__ == "__main__":
    unittest.main()
