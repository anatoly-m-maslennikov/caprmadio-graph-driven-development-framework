"""Contract coverage for read-only canonical Methodology currentness."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from framework_compiler_currentness_fixture import (  # noqa: E402
    ConfiguredCompilerFixture,
    compiler,
    source_atom,
)
from framework_initialization import (  # noqa: E402
    FrameworkInitializationError,
    plan_initial_framework_installation,
    verify_canonical_compiler_currentness,
)
import framework_compiler_currentness as currentness  # noqa: E402


class FrameworkCompilerCurrentnessTests(unittest.TestCase):
    """P1735 rejects stale output without compiling or publishing anything."""

    def setUp(self) -> None:
        self.fixture = ConfiguredCompilerFixture.create()

    def assert_rejected(self, code: str | None = None) -> None:
        with self.assertRaises(FrameworkInitializationError) as raised:
            verify_canonical_compiler_currentness(self.fixture.root)
        if code is not None:
            self.assertEqual(raised.exception.code, code)

    def assert_control_rejected_before_compiler_path_resolution(self) -> None:
        """Control-carrier symlinks must stop before their target is resolved."""

        with patch.object(currentness._COMPILER, "methodology_paths") as resolve:
            self.assert_rejected("initial-compiler-control-unsafe")
        resolve.assert_not_called()

    def test_accepts_exact_real_projection_without_effects(self) -> None:
        before = {
            path.relative_to(self.fixture.root): path.read_bytes()
            for path in self.fixture.root.rglob("*")
            if path.is_file() and not path.is_symlink()
        }

        proof = verify_canonical_compiler_currentness(self.fixture.root)

        report, _selected, snapshot = compiler.compile_report(self.fixture.root)
        self.assertEqual(proof.compiled_root, self.fixture.output.relative_to(self.fixture.root).as_posix())
        self.assertEqual(
            proof.compiler_entrypoint,
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/"
            "COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py",
        )
        self.assertEqual(proof.source_frontier_digest, report["source_frontier_digest"])
        self.assertEqual(proof.output_tree_digest, compiler.generated_tree_digest(self.fixture.root))
        self.assertEqual(proof.source_snapshot, tuple(sorted(snapshot.items())))
        after = {
            path.relative_to(self.fixture.root): path.read_bytes()
            for path in self.fixture.root.rglob("*")
            if path.is_file() and not path.is_symlink()
        }
        self.assertEqual(after, before)
        self.assertFalse((self.fixture.root / ".caprmedio_runtime/framework/current.toml").exists())

    def test_refuses_missing_or_extra_compiled_output(self) -> None:
        carrier = self.fixture.output_carrier("04_requirement", "CA-R-001--foundation.md")
        carrier.unlink()
        with self.subTest(case="missing"):
            self.assert_rejected("initial-compiler-output-pathset-mismatch")

        self.fixture.materialize_current_projection()
        extra = self.fixture.output / "04_requirement/EXTRA.md"
        extra.write_bytes(self.fixture.output_carrier("04_requirement", "CA-R-001--foundation.md").read_bytes())
        with self.subTest(case="extra"):
            self.assert_rejected("initial-compiler-output-pathset-mismatch")

    def test_ignores_ds_store_in_source_and_compiled_output(self) -> None:
        original_digest = verify_canonical_compiler_currentness(self.fixture.root).output_tree_digest
        (self.fixture.source / "001_CORE_META_MODEL/.DS_Store").write_bytes(b"finder metadata")
        (self.fixture.source / "003_PROJECT_CONFIGURATION/.DS_Store").write_bytes(b"finder metadata")
        (self.fixture.output / "04_requirement/.DS_Store").write_bytes(b"finder metadata")

        proof = verify_canonical_compiler_currentness(self.fixture.root)

        self.assertEqual(original_digest, proof.output_tree_digest)

    def test_refuses_compiled_symlink(self) -> None:
        carrier = self.fixture.output_carrier("04_requirement", "CA-R-001--foundation.md")
        carrier.unlink()
        carrier.symlink_to(self.fixture.source / "001_CORE_META_MODEL/04_requirement/CA-R-001--foundation.md")
        self.assert_rejected("initial-compiler-output-invalid")

    def test_refuses_compiled_mode_change(self) -> None:
        carrier = self.fixture.output_carrier("04_requirement", "CA-R-001--foundation.md")
        carrier.chmod(0o600)
        self.assert_rejected("initial-compiler-output-mode-mismatch")

    def test_refuses_compiled_projection_metadata_change(self) -> None:
        carrier = self.fixture.output_carrier("04_requirement", "CA-R-001--foundation.md")
        carrier.write_bytes(carrier.read_bytes().replace(b"source_atom_revision: 1", b"source_atom_revision: 9"))
        self.assert_rejected("initial-compiler-output-bytes-mismatch")

    def test_refuses_changed_source_frontier(self) -> None:
        source = self.fixture.source / "001_CORE_META_MODEL/04_requirement/CA-R-001--foundation.md"
        source.write_bytes(source_atom("CA-R-001", summary="changed after compilation"))

        self.assert_rejected("initial-compiler-output-bytes-mismatch")

    def test_refuses_source_snapshot_changed_during_verification(self) -> None:
        """This is the one explicit timing-race seam in the read-only proof."""

        with patch.object(currentness._COMPILER, "source_snapshot_is_current", side_effect=(True, False)):
            self.assert_rejected("initial-compiler-source-stale")

    def test_refuses_compiler_conflict_or_output_collision(self) -> None:
        self.fixture.write_source(
            "003_PROJECT_CONFIGURATION",
            "04_requirement",
            "CA-R-001--duplicate.md",
            source_atom("CA-R-001"),
        )
        with self.subTest(case="conflict"):
            self.assert_rejected("initial-compiler-conflict-unresolved")

        self.fixture = ConfiguredCompilerFixture.create()
        self.fixture.write_source(
            "001_CORE_META_MODEL",
            "04_requirement",
            "SHARED.md",
            source_atom("CA-R-002"),
        )
        self.fixture.write_source(
            "003_PROJECT_CONFIGURATION",
            "04_requirement",
            "SHARED.md",
            source_atom("CA-R-003"),
        )
        with self.subTest(case="collision"):
            self.assert_rejected("initial-compiler-conflict-unresolved")

    def test_packages_only_the_configured_compiled_root_when_default_tree_is_stale(self) -> None:
        configured_output = Path(".caprmedio_caprmedio/configured-compiled-methodology")
        self.fixture = ConfiguredCompilerFixture.create(output_relative=configured_output)
        stale = self.fixture.root / compiler.OUTPUT_RELATIVE / "04_requirement/STALE.md"
        stale.parent.mkdir(parents=True, exist_ok=True)
        stale.write_bytes(b"unproven default output must not be packaged\n")

        proof = verify_canonical_compiler_currentness(self.fixture.root)
        plan = plan_initial_framework_installation(self.fixture.root)
        compiled_sources = {
            row.source_path
            for row in plan.rows
            if row.destination_path.startswith("METHODOLOGY/compiled/")
        }

        self.assertEqual(proof.compiled_root, configured_output.as_posix())
        self.assertTrue(compiled_sources)
        self.assertTrue(all(path.startswith(configured_output.as_posix() + "/") for path in compiled_sources))
        self.assertNotIn(stale.relative_to(self.fixture.root).as_posix(), compiled_sources)

    def test_refuses_nonempty_unproven_sibling_of_configured_compiled_root(self) -> None:
        sibling = self.fixture.output / "unproven-legacy-output"
        sibling.mkdir()
        (sibling / "CA-R-999--unproven.md").write_bytes(b"not a deterministic projection\n")

        # Currentness proves its configured role tree.  Package planning must
        # additionally refuse a non-role sibling rather than silently omitting
        # a carrier that a consumer could mistake for compiled Methodology.
        self.assertEqual(
            verify_canonical_compiler_currentness(self.fixture.root).compiled_root,
            self.fixture.output.relative_to(self.fixture.root).as_posix(),
        )
        with self.assertRaises(FrameworkInitializationError) as raised:
            plan_initial_framework_installation(self.fixture.root)
        self.assertEqual(raised.exception.code, "initial-methodology-compiled-unknown")

    def test_refuses_project_structure_symlink_without_resolving_its_target(self) -> None:
        structure = self.fixture.root / compiler.STRUCTURE_RELATIVE
        target = self.fixture.root / "untrusted-project-structure.toml"
        target.write_text("not = [the, governed, structure]\n", encoding="utf-8")
        structure.unlink()
        structure.symlink_to(target)

        self.assert_control_rejected_before_compiler_path_resolution()

    def test_refuses_dangling_project_structure_symlink_without_resolving_it(self) -> None:
        structure = self.fixture.root / compiler.STRUCTURE_RELATIVE
        structure.unlink()
        structure.symlink_to(self.fixture.root / "missing-project-structure.toml")

        self.assert_control_rejected_before_compiler_path_resolution()

    def test_refuses_symlinked_control_root_ancestor_before_reading_settings(self) -> None:
        # Retain the fixture's existing control directory and instead make the
        # configured control-root path itself a symlink.  This avoids a rename
        # while still proving the preflight rejects a symlinked ancestor before
        # resolving any carrier beneath it.
        settings = self.fixture.root / compiler.SETTINGS_PATH
        settings.write_text('[paths]\ncontrol_root = "symlinked-control-root"\n', encoding="utf-8")
        control_root = self.fixture.root / "symlinked-control-root"
        control_root.symlink_to(self.fixture.root / compiler.SETTINGS_PATH.parent, target_is_directory=True)

        self.assert_control_rejected_before_compiler_path_resolution()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
