"""Actual source-delivery and compiler/stager checks in disposable projects."""

from __future__ import annotations

import hashlib
import shutil
import sys
import tomllib
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_compilation import build_preflight_validated_candidate, render_release_candidate  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402
from release_delivery import ReleaseDeliveryError, deliver_release_sources  # noqa: E402
from release_handoff import DERIVED_SOURCE_COPY_RELATIVE, PackageRow, SealedSourceCopy, build_validated_candidate  # noqa: E402
from release_packaging import stage_framework_package  # noqa: E402
from bootstrap_image import _source_context  # noqa: E402
import test_release_compilation as compilation_test  # noqa: E402
import release_delivery  # noqa: E402


def records(folder: Path) -> dict[str, tuple[bool, bytes, int]]:
    return {path.relative_to(folder).as_posix():
            (path.is_dir(), b"" if path.is_dir() else path.read_bytes(), path.stat().st_mode & 0o777)
            for path in (folder, *sorted(folder.rglob("*")))}


class ReleaseDeliveryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = compilation_test.ReleaseCompilationTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.target = self.root / DERIVED_SOURCE_COPY_RELATIVE
        self.fixture.write(".caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY/existing.md", b"protected projection\n")
        self.fixture.write(".caprmedio_runtime/journal/prior.jsonl", b'{"prior":"N"}\n')
        self.fixture.write(".agents/skills/ca/SKILL.md", b"prior skill\n")
        self.fixture.write(f"{self.fixture.source.relative_to(self.root)}/001_CORE_META_MODEL/04_requirement/payload/run.sh", b"#!/bin/sh\ntrue\n", 0o755)
        (self.fixture.source / "001_CORE_META_MODEL/04_requirement/empty/private").mkdir(parents=True)
        (self.fixture.source / "001_CORE_META_MODEL/04_requirement/empty/private").chmod(0o700)

    def owned_predecessor(self):
        preflight, candidate = self.fixture.build()
        deliver_release_sources(candidate)
        handoff = render_release_candidate(candidate, preflight)
        retained = stage_framework_package(self.root, handoff)
        self.fixture.write(".caprmedio_runtime/framework/current.toml", f'release = "{candidate.manifest.sha256}"\n'.encode())
        before = records(self.target)
        release_root = self.root / retained["release_root"]
        retained_before = records(release_root)
        self.fixture.core.write_bytes(compilation_test.carrier("CA-R-001", version=2))
        next_preflight, next_candidate = build_preflight_validated_candidate(
            self.root, candidate_release="N+2",
            full_suite_environment={"runner": "fixture", "command": ["python", "-m", "unittest"], "working_directory": "."},
            candidate_image_reference="fixture:N+2",
        )
        return next_preflight, next_candidate, before, release_root, retained_before

    def bootstrap_owned_predecessor(self):
        """Materialize the installed first-N selector/package shape exactly."""

        preflight, initial = self.fixture.build()
        deliver_release_sources(initial)
        staged = stage_framework_package(self.root, render_release_candidate(initial, preflight))
        original = self.root / staged["release_root"]
        manifest = tomllib.loads((original / "manifest.toml").read_text(encoding="utf-8"))
        rows = tuple(PackageRow.model_validate({
            "resource": row["resource"],
            "source_path": row["source_path"],
            "destination_path": row["destination"],
            "sha256": row["sha256"],
            "mode": row["mode"],
        }) for row in manifest["files"])
        source_context = _source_context(rows)
        bootstrap_manifest = (original / "manifest.toml").read_bytes().replace(
            f'candidate_snapshot_manifest_sha256 = "{initial.manifest.sha256}"'.encode(),
            f'candidate_snapshot_manifest_sha256 = "{source_context}"'.encode(),
        )
        bootstrap_release = hashlib.sha256(bootstrap_manifest).hexdigest()
        bootstrap = original.parent / bootstrap_release
        shutil.copytree(original, bootstrap)
        (bootstrap / "manifest.toml").write_bytes(bootstrap_manifest)
        self.assertEqual(hashlib.sha256(bootstrap_manifest).hexdigest(), bootstrap_release)
        self.assertEqual(
            tomllib.loads(bootstrap_manifest.decode())["candidate_snapshot_manifest_sha256"],
            source_context,
        )
        selected_root = f".caprmedio_runtime/framework/releases/{bootstrap_release}"
        self.fixture.write(
            ".caprmedio_runtime/framework/current.toml",
            (
                "schema_version = 1\n"
                f'manifest_sha256 = "{bootstrap_release}"\n'
                f'release = "{bootstrap_release}"\n'
                f'selected_release_root = "{selected_root}"\n'
                f'framework_engine_root = "{selected_root}/FRAMEWORK_ENGINE"\n'
                f'methodology_root = "{selected_root}/METHODOLOGY"\n'
                f'image_digest = "sha256:{"a" * 64}"\n'
            ).encode(),
        )
        self.assertNotEqual(source_context, bootstrap_release)
        prior = records(self.target)
        self.fixture.core.write_bytes(compilation_test.carrier("CA-R-001", version=2))
        next_preflight, next_candidate = build_preflight_validated_candidate(
            self.root, candidate_release="N+2",
            full_suite_environment={"runner": "fixture", "command": ["python", "-m", "unittest"], "working_directory": "."},
            candidate_image_reference="fixture:N+2",
        )
        return next_preflight, next_candidate, prior, bootstrap, records(bootstrap)

    def test_a_full_delivery_modes_empty_directories_idempotence_and_actual_pipeline(self) -> None:
        before = self.fixture.snapshot()
        source_before = records(self.fixture.source)
        preflight, candidate = self.fixture.build()
        first = deliver_release_sources(candidate)
        self.assertIsInstance(first, SealedSourceCopy)
        self.assertEqual(first.source_copy_root, DERIVED_SOURCE_COPY_RELATIVE)
        self.assertEqual(first.actual_derived_source_copy_sha256, preflight.expected_derived_source_copy_sha256)
        self.assertEqual(records(self.target), source_before)
        inode = self.target.stat().st_ino
        second = deliver_release_sources(candidate)
        self.assertEqual(first, second)
        self.assertEqual(self.target.stat().st_ino, inode)
        self.assertEqual(list(self.target.parent.glob(".release-sources-*")), [])
        handoff = render_release_candidate(candidate, preflight)
        staged = stage_framework_package(self.root, handoff)
        self.assertTrue(staged["verified"])
        self.assertTrue(staged["staged"])
        self.assertEqual(handoff.actual_derived_source_copy_sha256, first.actual_derived_source_copy_sha256)
        self.assertEqual(records(self.fixture.source), source_before)
        for path, payload in before.items():
            self.assertEqual((self.root / path).read_bytes(), payload)

    def test_owned_executing_package_replacement_retains_n_and_prior_derived_tree(self) -> None:
        preflight, candidate, prior, release, retained = self.owned_predecessor()
        # The stager has no byte rows for empty folders. Keep even an extra
        # empty predecessor folder in the retained derived tree.
        (self.target / "unknown-empty").mkdir()
        prior = records(self.target)
        selector = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        delivered = deliver_release_sources(candidate)
        self.assertEqual(records(self.target), records(self.fixture.source))
        self.assertEqual(records(release), retained)
        backups = list(self.target.parent.glob(".release-sources-prior-*"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(records(backups[0]), prior)
        self.assertEqual(delivered.actual_derived_source_copy_sha256, preflight.expected_derived_source_copy_sha256)
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector)
        stage_framework_package(self.root, render_release_candidate(candidate, preflight))
        self.assertEqual(records(release), retained)

    def test_bootstrap_executing_package_replacement_accepts_only_exact_selector_bound_shape(self) -> None:
        preflight, candidate, _prior, release, retained = self.bootstrap_owned_predecessor()
        # macOS metadata was never part of the persistent release inventory.
        (self.target / ".DS_Store").write_bytes(b"transient finder metadata\n")
        selector = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()

        delivered = deliver_release_sources(candidate)

        self.assertEqual(records(self.target), records(self.fixture.source))
        self.assertEqual(records(release), retained)
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector)
        self.assertEqual(delivered.actual_derived_source_copy_sha256, preflight.expected_derived_source_copy_sha256)

    def test_bootstrap_predecessor_refuses_corrupt_incomplete_extra_and_mismatched_carriers(self) -> None:
        _preflight, candidate, _prior, release, _retained = self.bootstrap_owned_predecessor()
        package_file = release / "FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py"
        payload, mode = package_file.read_bytes(), package_file.stat().st_mode & 0o777
        selector = self.root / ".caprmedio_runtime/framework/current.toml"
        selector_bytes = selector.read_bytes()
        for mutation in ("corrupt", "incomplete", "extra", "mismatched", "selector"):
            with self.subTest(mutation=mutation):
                extra = None
                if mutation == "corrupt":
                    package_file.write_bytes(b"tampered retained bytes\n")
                elif mutation == "incomplete":
                    package_file.unlink()
                elif mutation == "extra":
                    extra = release / "FRAMEWORK_ENGINE/extra-retained.py"
                    extra.write_bytes(b"unowned package member\n")
                else:
                    if mutation == "mismatched":
                        extra = self.target / "unowned/predecessor.md"
                        extra.parent.mkdir()
                        extra.write_bytes(b"unowned delivery member\n")
                    else:
                        selector.write_bytes(selector_bytes + b'unexpected = "selector member"\n')
                release_before = records(release)
                target_before = records(self.target)
                try:
                    with self.assertRaises(ReleaseDeliveryError) as refused:
                        deliver_release_sources(candidate)
                    expected = "release-copy-predecessor-mismatch" if mutation == "mismatched" else "release-copy-ownership-unproven"
                    self.assertEqual(refused.exception.code, expected)
                    self.assertEqual(records(release), release_before)
                    self.assertEqual(records(self.target), target_before)
                finally:
                    if mutation in {"corrupt", "incomplete"}:
                        package_file.write_bytes(payload)
                        package_file.chmod(mode)
                    elif mutation == "selector":
                        selector.write_bytes(selector_bytes)
                    elif extra is not None:
                        extra.unlink()
                        if mutation == "mismatched":
                            extra.parent.rmdir()

    def test_untrusted_and_stale_candidates_refuse_before_delivery(self) -> None:
        _preflight, candidate = self.fixture.build()
        with self.assertRaises(ReleaseDeliveryError) as raw:
            deliver_release_sources(candidate.manifest.model_dump())
        self.assertEqual(raw.exception.code, "release-candidate-untrusted")
        for mutation in ("bytes", "mode", "selector"):
            with self.subTest(mutation=mutation):
                path = self.fixture.core if mutation != "selector" else self.root / ".caprmedio_runtime/framework/current.toml"
                payload, mode = path.read_bytes(), path.stat().st_mode & 0o777
                if mutation == "mode":
                    path.chmod(0o600)
                else:
                    path.write_bytes(payload + b"changed\n" if mutation == "bytes" else b'release = "other"\n')
                try:
                    with self.assertRaises(ReleaseContractError) as stale:
                        deliver_release_sources(candidate)
                    self.assertEqual(stale.exception.code, "release-currentness-stale")
                    self.assertFalse(self.target.exists())
                finally:
                    path.write_bytes(payload)
                    path.chmod(mode)

    def test_unknown_partial_mode_changed_and_file_collision_refuse_without_overwrite(self) -> None:
        _preflight, candidate = self.fixture.build()
        self.fixture.copy_source()
        (self.target / "unowned.md").write_bytes(b"unknown bytes\n")
        original = records(self.target)
        with self.assertRaises(ReleaseDeliveryError) as unknown:
            deliver_release_sources(candidate)
        self.assertEqual(unknown.exception.code, "release-copy-ownership-unproven")
        self.assertEqual(records(self.target), original)
        shutil.rmtree(self.target)  # Disposable test-owned fixture only.
        self.target.write_bytes(b"collision\n")
        with self.assertRaises(ReleaseDeliveryError) as collision:
            deliver_release_sources(candidate)
        self.assertEqual(collision.exception.code, "release-copy-collision")
        self.assertEqual(self.target.read_bytes(), b"collision\n")

    def test_owned_partial_changed_modes_and_unknown_files_refuse(self) -> None:
        _preflight, candidate, _prior, release, retained = self.owned_predecessor()
        core = self.target / self.fixture.core.relative_to(self.fixture.source)
        payload, mode = core.read_bytes(), core.stat().st_mode & 0o777
        for mutation in ("partial", "mode", "unknown"):
            with self.subTest(mutation=mutation):
                extra = self.target / "unknown/keep.md"
                if mutation == "partial":
                    core.unlink()
                elif mutation == "mode":
                    core.chmod(0o600)
                else:
                    extra.parent.mkdir()
                    extra.write_bytes(b"keep this\n")
                original = records(self.target)
                with self.assertRaises(ReleaseDeliveryError) as refused:
                    deliver_release_sources(candidate)
                self.assertEqual(refused.exception.code, "release-copy-predecessor-mismatch")
                self.assertEqual(records(self.target), original)
                self.assertEqual(records(release), retained)
                core.write_bytes(payload)
                core.chmod(mode)
                if extra.exists():
                    extra.unlink()
                    extra.parent.rmdir()

    def test_source_and_destination_symlink_components_refuse_without_following(self) -> None:
        _preflight, candidate = self.fixture.build()
        outside = self.root / "outside"
        outside.mkdir()
        self.target.parent.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ReleaseDeliveryError) as target:
            deliver_release_sources(candidate)
        self.assertEqual(target.exception.code, "release-copy-path-unsafe")
        self.assertEqual(list(outside.iterdir()), [])
        self.target.parent.unlink()
        payload = self.fixture.core.read_bytes()
        self.fixture.core.unlink()
        self.fixture.core.symlink_to(self.fixture.compiler)
        with self.assertRaises(ReleaseDeliveryError) as source:
            deliver_release_sources(candidate)
        self.assertEqual(source.exception.code, "release-copy-path-unsafe")
        self.fixture.core.unlink()
        self.fixture.core.write_bytes(payload)
        self.assertFalse(self.target.exists())

    def test_tampered_retained_package_cannot_prove_replacement(self) -> None:
        _preflight, candidate, prior, release, _retained = self.owned_predecessor()
        (release / "FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py").write_bytes(b"tampered\n")
        with self.assertRaises(ReleaseDeliveryError) as tampered:
            deliver_release_sources(candidate)
        self.assertEqual(tampered.exception.code, "release-copy-ownership-unproven")
        self.assertEqual(records(self.target), prior)

    def test_wrong_complete_copy_expectation_refuses_before_writes(self) -> None:
        _preflight, candidate = self.fixture.build()
        wrong = build_validated_candidate(
            self.root, candidate.intent.model_copy(update={"expected_derived_source_copy_sha256": "0" * 64}),
            observed_source_frontier_digest=candidate.authority.source_frontier_digest,
        )
        with self.assertRaises(ReleaseDeliveryError) as refused:
            deliver_release_sources(wrong)
        self.assertEqual(refused.exception.code, "release-copy-digest-mismatch")
        self.assertFalse(self.target.parent.exists())

    def test_target_root_and_nested_symlink_refuse_without_overwrite(self) -> None:
        _preflight, candidate = self.fixture.build()
        self.target.parent.mkdir()
        outside = self.root / "outside-target"
        outside.mkdir()
        self.target.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ReleaseDeliveryError) as root_link:
            deliver_release_sources(candidate)
        self.assertEqual(root_link.exception.code, "release-copy-path-unsafe")
        self.assertEqual(list(outside.iterdir()), [])
        self.target.unlink()
        self.fixture.copy_source()
        nested = self.target / "linked"
        nested.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ReleaseDeliveryError) as nested_link:
            deliver_release_sources(candidate)
        self.assertEqual(nested_link.exception.code, "release-copy-path-unsafe")
        self.assertTrue(nested.is_symlink())

    def test_source_mutation_during_copy_refuses_and_retains_staged_candidate(self) -> None:
        _preflight, candidate = self.fixture.build()
        write_snapshot = release_delivery._write_snapshot
        def mutate_after_copy(folder, source_records):
            write_snapshot(folder, source_records)
            self.fixture.core.write_bytes(self.fixture.core.read_bytes() + b"concurrent fixture change\n")
        with patch("release_delivery._write_snapshot", side_effect=mutate_after_copy):
            with self.assertRaises(ReleaseDeliveryError) as stale:
                deliver_release_sources(candidate)
        self.assertEqual(stale.exception.code, "release-currentness-stale")
        self.assertFalse(self.target.exists())
        self.assertEqual(len(stale.exception.recovery_paths), 1)
        self.assertTrue((self.root / stale.exception.recovery_paths[0]).is_dir())

    def test_copy_failure_retains_repairable_staging_and_original_authority(self) -> None:
        _preflight, candidate = self.fixture.build()
        before = self.fixture.snapshot()
        def partial(folder, _records):
            (folder / "partial.md").write_bytes(b"partial\n")
            raise OSError("injected fixture write failure")
        with patch("release_delivery._write_snapshot", side_effect=partial):
            with self.assertRaises(ReleaseDeliveryError) as failed:
                deliver_release_sources(candidate)
        self.assertEqual(failed.exception.code, "release-copy-failed")
        self.assertEqual(len(failed.exception.recovery_paths), 1)
        recovery = self.root / failed.exception.recovery_paths[0]
        self.assertEqual((recovery / "partial.md").read_bytes(), b"partial\n")
        self.assertFalse(self.target.exists())
        for path, payload in before.items():
            self.assertEqual((self.root / path).read_bytes(), payload)

    def test_owned_publication_failure_restores_predecessor_and_reports_candidate_staging(self) -> None:
        _preflight, candidate, prior, release, retained = self.owned_predecessor()
        original_rename = Path.rename
        def refuse_publication(path, target):
            if path.name.startswith(f".release-sources-{candidate.manifest.sha256[:12]}-"):
                raise OSError("injected fixture publication failure")
            return original_rename(path, target)
        with patch("release_delivery.Path.rename", autospec=True, side_effect=refuse_publication):
            with self.assertRaises(ReleaseDeliveryError) as failed:
                deliver_release_sources(candidate)
        self.assertEqual(failed.exception.code, "release-copy-failed")
        self.assertEqual(records(self.target), prior)
        self.assertEqual(records(release), retained)
        self.assertTrue(any(path.startswith("101_LAYER_1_FRAMEWORK_METHODOLOGY/.release-sources-")
                            for path in failed.exception.recovery_paths))


if __name__ == "__main__":
    unittest.main()
