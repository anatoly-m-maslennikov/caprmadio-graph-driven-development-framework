"""Private Release-suite control-reference context tests.

The fixtures copy the current, admitted source closure into a disposable
Project.  They never turn the fixture into a candidate input or a public
request field.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = RELEASE_ROOT.parents[3]
MCP_ROOT = REPOSITORY / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP"
for path in (RELEASE_ROOT, MCP_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import release_source_admission  # noqa: E402
from release_source_admission import AUTHORITY_REF, derive_release_private_carriers, derive_release_source_admission  # noqa: E402
import release_suite_reference_context as reference_context  # noqa: E402
import selected_routes  # noqa: E402
from release_suite_reference_context import (  # noqa: E402
    ReferenceRow,
    ReleaseSuiteReferenceContext,
    ReleaseSuiteReferenceContextError,
    capture_context,
    copy_verified_bytes,
    revalidate_context,
    validate_reference_rows,
    validate_schema2_context,
)
from selected_routes import PROJECT_SETTINGS_REF, canonical_json, load_selected_manifest, selected_manifest_ref  # noqa: E402
from full_suite_golden.control_fixture import copy_control_closure  # noqa: E402


def _source_paths(value: object) -> set[str]:
    if isinstance(value, dict):
        paths = {value["source_path"]} if isinstance(value.get("source_path"), str) else set()
        for child in value.values():
            paths |= _source_paths(child)
        return paths
    if isinstance(value, list):
        paths: set[str] = set()
        for child in value:
            paths |= _source_paths(child)
        return paths
    return set()


def _replace_first_source_path(value: object) -> bool:
    if isinstance(value, dict):
        if isinstance(value.get("source_path"), str):
            value["source_path"] = ".env"
            return True
        return any(_replace_first_source_path(child) for child in value.values())
    if isinstance(value, list):
        return any(_replace_first_source_path(child) for child in value)
    return False


class ReleaseSuiteReferenceContextTests(unittest.TestCase):
    """Capture derives a current closure and never trusts a supplied one."""

    def setUp(self) -> None:
        temporary_root = REPOSITORY / ".caprmedio_tmp/tests/release-suite-reference-context"
        temporary_root.mkdir(parents=True, exist_ok=True)
        # This managed macOS profile can refuse removal of nested fixture
        # directories; retain these tiny, disposable test inputs like the
        # neighbouring release tests rather than turning cleanup into a test
        # outcome.
        self.root = Path(tempfile.mkdtemp(prefix="release-suite-reference-", dir=temporary_root))
        copy_control_closure(REPOSITORY, self.root)
        self.manifest_ref = selected_manifest_ref(REPOSITORY)
        self.bindings = {
            "candidate_snapshot_manifest_sha256": "a" * 64,
            "compiled_candidate_root": ".caprmedio_caprmedio/_release_materialized/a",
            "selected_n_identity": "selected-N-fixture",
            "selected_n_image_context": "sha256:" + "b" * 64,
        }

    def capture(self) -> ReleaseSuiteReferenceContext:
        return capture_context(self.root, self.bindings)

    def project_structure_ref(self) -> str:
        return reference_context._project_structure_ref(
            (self.root / PROJECT_SETTINGS_REF).read_bytes()
        )

    def admitted_control_roots(self) -> dict[str, str]:
        """The D580/E587 roots plus one actually admitted transitive pin."""
        manifest = load_selected_manifest(self.root)
        project_structure_ref = self.project_structure_ref()
        roots = {
            "selected_manifest": self.manifest_ref,
            "operators_registry": ".caprmedio_caprmedio/operators_registry.toml",
            "project_settings": PROJECT_SETTINGS_REF.as_posix(),
            "project_structure": project_structure_ref,
            "source_registry": manifest["source_freshness"]["selected_source_registry_ref"],
            "d572_carrier": AUTHORITY_REF,
        }
        excluded = set(roots.values())
        transitive = next(
            path for path in sorted(_source_paths(derive_release_source_admission(self.root)))
            if path not in excluded
        )
        return {**roots, "transitive_pin": transitive}

    def assert_mutation_blocks_rederivation(self, *, phase: str, copy_before_mutation: bool) -> None:
        context = self.capture()
        if copy_before_mutation:
            workspace = Path(tempfile.mkdtemp(prefix="release-suite-phase-workspace-"))
            copy_verified_bytes(context, workspace)
        for name, relative in self.admitted_control_roots().items():
            with self.subTest(phase=phase, root=name):
                path = self.root / relative
                original = path.read_bytes()
                path.write_bytes(original + f"\n{phase}-{name}-changed\n".encode("utf-8"))
                try:
                    with self.assertRaises(Exception):
                        revalidate_context(self.root, context, self.bindings)
                finally:
                    path.write_bytes(original)

    def test_each_admitted_root_mutation_blocks_before_execution_rederivation(self) -> None:
        self.assert_mutation_blocks_rederivation(
            phase="before_execution", copy_before_mutation=False,
        )

    def test_each_admitted_root_mutation_blocks_after_execution_rederivation(self) -> None:
        # The workspace copy represents inputs already issued to the suite;
        # post-run rederivation must still refuse changed live authority.
        self.assert_mutation_blocks_rederivation(
            phase="after_execution", copy_before_mutation=True,
        )

    def test_capture_contains_current_roots_transitive_pins_and_canonical_digest(self) -> None:
        context = self.capture()
        paths = [row.source_path for row in context.reference_rows]
        self.assertEqual(sorted(paths), paths)
        self.assertEqual(len(paths), len(set(paths)))
        self.assertTrue({
            self.manifest_ref,
            ".caprmedio_caprmedio/operators_registry.toml",
            PROJECT_SETTINGS_REF.as_posix(),
            self.project_structure_ref(),
            AUTHORITY_REF,
        }.issubset(paths))
        self.assertTrue(_source_paths(derive_release_source_admission(self.root)).issubset(paths))
        self.assertTrue(_source_paths(derive_release_private_carriers(self.root)).issubset(paths))
        for row in context.reference_rows:
            source = self.root / row.source_path
            self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), row.sha256)
            self.assertEqual(source.stat().st_mode & 0o777, row.mode)
        # Independently reconstruct D580's flat, self-excluding preimage;
        # this must not call the helper's digest implementation.
        payload = {
            "schema_version": 1,
            **dict(context.trusted_binding_values),
            "reference_rows": [row.as_dict() for row in context.reference_rows],
        }
        self.assertEqual(hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest(),
                         context.control_context_digest)

    def test_copy_preserves_only_captured_bytes_at_identical_relative_paths(self) -> None:
        context = self.capture()
        workspace = Path(tempfile.mkdtemp(prefix="release-suite-workspace-"))
        copy_verified_bytes(context, workspace)
        self.assertFalse((workspace / "arbitrary-caller-file").exists())
        for row in context.reference_rows:
            self.assertEqual((workspace / row.source_path).read_bytes(), (self.root / row.source_path).read_bytes())
            self.assertEqual((workspace / row.source_path).stat().st_mode & 0o777, row.mode)
        structure = self.project_structure_ref()
        self.assertEqual((workspace / structure).read_bytes(), (self.root / structure).read_bytes())
        self.assertEqual(
            (workspace / structure).stat().st_mode & 0o777,
            (self.root / structure).stat().st_mode & 0o777,
        )

    def test_capture_refuses_missing_project_structure_before_execution(self) -> None:
        structure = self.root / self.project_structure_ref()
        original = structure.read_bytes()
        mode = structure.stat().st_mode & 0o777
        structure.unlink()
        try:
            with self.assertRaises(ReleaseSuiteReferenceContextError):
                self.capture()
        finally:
            structure.write_bytes(original)
            structure.chmod(mode)

    def test_revalidation_refuses_mutated_transitive_pin_before_or_after_execution(self) -> None:
        context = self.capture()
        transitive = next(path for path in _source_paths(derive_release_source_admission(self.root))
                          if path != AUTHORITY_REF)
        source = self.root / transitive
        original = source.read_bytes()
        source.write_bytes(original + b"\nchanged\n")
        with self.assertRaises(Exception):
            revalidate_context(self.root, context, self.bindings)
        source.write_bytes(original)
        self.assertEqual(context, revalidate_context(self.root, context, self.bindings))
        (self.root / self.manifest_ref).write_bytes((self.root / self.manifest_ref).read_bytes() + b"\n")
        with self.assertRaises(Exception):
            revalidate_context(self.root, context, self.bindings)

    def test_capture_refuses_symlinked_or_secret_shaped_injected_reference_without_reading_it(self) -> None:
        target = self.root / AUTHORITY_REF
        saved = target.read_bytes()
        target.unlink()
        target.symlink_to(self.root / ".caprmedio_caprmedio/operators_registry.toml")
        with self.assertRaises(Exception):
            self.capture()
        target.unlink()
        target.write_bytes(saved)

        context = self.capture()
        forged = ReleaseSuiteReferenceContext(
            root=context.root,
            trusted_binding_values=context.trusted_binding_values,
            reference_rows=(ReferenceRow(".env", hashlib.sha256(b"secret").hexdigest(), 0o600),),
            control_context_digest=context.control_context_digest,
            _verified_bytes=((".env", b"secret"),),
        )
        workspace = Path(tempfile.mkdtemp(prefix="release-suite-secret-"))
        with self.assertRaises(ReleaseSuiteReferenceContextError):
            copy_verified_bytes(forged, workspace)
        self.assertFalse((workspace / ".env").exists())

    def test_schema2_requires_exact_reference_rows_and_context_digest(self) -> None:
        context = self.capture()
        envelope = {
            "schema_version": 2,
            "candidate_snapshot_manifest_sha256": self.bindings["candidate_snapshot_manifest_sha256"],
            "reference_rows": [row.as_dict() for row in context.reference_rows],
            "control_context_digest": context.control_context_digest,
        }
        self.assertEqual(envelope, dict(validate_schema2_context(envelope, context)))
        envelope["control_context_digest"] = "0" * 64
        with self.assertRaises(ReleaseSuiteReferenceContextError):
            validate_schema2_context(envelope, context)

    def test_secret_shaped_envelope_row_refuses_before_any_reader_access(self) -> None:
        with patch("release_suite_reference_context._read_regular", side_effect=AssertionError("must not read")):
            with self.assertRaises(ReleaseSuiteReferenceContextError):
                validate_reference_rows(self.root, [{
                    "source_path": ".env",
                    "sha256": "a" * 64,
                    "mode": 0o600,
                }])

    def test_capture_refuses_bytes_mode_race_from_one_control_file(self) -> None:
        target = self.root / ".caprmedio_caprmedio/operators_registry.toml"
        target_inode = target.stat().st_ino
        original_read = os.read
        raced = False

        def read_then_change_mode(fd: int, size: int) -> bytes:
            nonlocal raced
            if os.fstat(fd).st_ino == target_inode and not raced:
                raced = True
                target.chmod(0o600)
            return original_read(fd, size)

        with patch("release_suite_reference_context.os.read", side_effect=read_then_change_mode):
            with self.assertRaises(ReleaseSuiteReferenceContextError):
                self.capture()
        self.assertTrue(raced)

    def test_revalidation_requires_fresh_suite_owner_bindings_not_context_copy(self) -> None:
        context = self.capture()
        self.assertEqual(context, revalidate_context(self.root, context, self.bindings))
        cases = {
            "candidate_snapshot_manifest_sha256": "c" * 64,
            "compiled_candidate_root": ".caprmedio_caprmedio/_release_materialized/c",
            "selected_n_identity": "selected-N-other",
            "selected_n_image_context": "sha256:" + "c" * 64,
        }
        for field, changed in cases.items():
            with self.subTest(field=field):
                fresh = dict(self.bindings)
                fresh[field] = changed
                with self.assertRaises(ReleaseSuiteReferenceContextError):
                    revalidate_context(self.root, context, fresh)

    def test_reader_race_uses_preflight_snapshot_and_never_reads_injected_secret_path(self) -> None:
        """A root-backed reread after preflight must not gain a new source path."""
        manifest_path = self.root / self.manifest_ref
        original_preflight = reference_context._preflight_reader_paths
        original_read_regular = reference_context._read_regular
        raced = False

        def preflight_then_mutate(root: Path) -> object:
            nonlocal raced
            result = original_preflight(root)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertTrue(_replace_first_source_path(manifest))
            manifest_path.write_text(json.dumps(manifest, sort_keys=True, separators=(",", ":")), encoding="utf-8")
            raced = True
            return result

        def guard_secret_read(root: Path, relative: str) -> tuple[bytes, int]:
            if relative == ".env":
                raise AssertionError("reader attempted forbidden secret-shaped path")
            return original_read_regular(root, relative)

        with patch.object(reference_context, "_preflight_reader_paths", side_effect=preflight_then_mutate), \
                patch.object(reference_context, "_read_regular", side_effect=guard_secret_read):
            context = self.capture()
        self.assertTrue(raced)
        self.assertIn(self.manifest_ref, [row.source_path for row in context.reference_rows])

    def test_capture_keeps_other_control_reader_path_bindings_unchanged(self) -> None:
        """Snapshot isolation is local; it must not patch shared reader modules."""
        selected_path_type = selected_routes.Path
        admission_path_type = release_source_admission.Path
        original_preflight = reference_context._preflight_reader_paths
        observed = False

        def observe_shared_readers(root: Path) -> object:
            nonlocal observed
            self.assertIs(selected_routes.Path, selected_path_type)
            self.assertIs(release_source_admission.Path, admission_path_type)
            self.assertEqual(self.manifest_ref, selected_routes.selected_manifest_ref(root))
            observed = True
            return original_preflight(root)

        with patch.object(reference_context, "_preflight_reader_paths", side_effect=observe_shared_readers):
            self.capture()
        self.assertTrue(observed)
        self.assertIs(selected_routes.Path, selected_path_type)
        self.assertIs(release_source_admission.Path, admission_path_type)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
