"""Actual source-delivery and compiler/stager checks in disposable projects."""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
import tomllib
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
TOOLS_ROOT = RELEASE_ROOT.parent
for path in (RELEASE_ROOT, TEST_ROOT, TOOLS_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_compilation import build_preflight_validated_candidate, render_release_candidate  # noqa: E402
from release_actions import PHASES, SelectedReleaseActionContext, begin_release_action_run, execute_release_action  # noqa: E402
from release_checkpoint import dump_release_checkpoint, release_action_checkpoint_sha256  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402
from release_delivery import ReleaseDeliveryError, deliver_release_sources  # noqa: E402
from release_handoff import DERIVED_SOURCE_COPY_RELATIVE, PackageRow, SealedSourceCopy, build_validated_candidate  # noqa: E402
from release_inventory import _is_ephemeral_directory, _is_ephemeral_file, refuse_secret_path  # noqa: E402
from release_packaging import stage_framework_package  # noqa: E402
from bootstrap_image import _source_context  # noqa: E402
from work_journal import with_event_digest  # noqa: E402
import test_release_compilation as compilation_test  # noqa: E402
import release_delivery  # noqa: E402
import release_predecessor  # noqa: E402


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

    def _persistent_inventory_sha256(self, target: Path) -> str:
        """Independently render the D567 v3 persistent-tree registration."""

        directories = [{"path": ".", "mode": target.stat().st_mode & 0o777}]
        files = []
        for path in sorted(target.rglob("*")):
            relative = path.relative_to(target).as_posix()
            self.assertFalse(path.is_symlink())
            if path.is_dir():
                refuse_secret_path(relative)
                if not _is_ephemeral_directory(path.name):
                    directories.append({"path": relative, "mode": path.stat().st_mode & 0o777})
            elif path.is_file() and not _is_ephemeral_file(path.name):
                refuse_secret_path(relative)
                files.append({
                    "path": relative,
                    "mode": path.stat().st_mode & 0o777,
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                })
            else:
                self.fail(f"unexpected D567 inventory carrier: {relative}")
        payload = {
            "directories": sorted(directories, key=lambda item: item["path"]),
            "files": sorted(files, key=lambda item: item["path"]),
        }
        return hashlib.sha256(json.dumps(
            payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
        ).encode("utf-8")).hexdigest()

    def _register_d567_predecessor(self, *, candidate, source_copy: SealedSourceCopy,
                                   journal: Path, event: dict, checkpoint: Path, action: Path) -> Path:
        """Write the closed prospective D567 registration from actual bytes."""

        registration = self.root / (
            ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
            "201_FEATURE_TOOLS/07_delivery/CA-D-567-TOOLS-DELIVERY--bind-validated-compiler-and-package-handoff.md"
        )
        authorization = self.root / ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations.md"
        authorization.parent.mkdir(parents=True, exist_ok=True)
        authorization.write_text(
            "---\natom_id: CA-P-1117\ncontent_role: Plan\nstatus: Active\n---\n\n"
            "# Harvest and implement session-derived operations\n\nComplete this Epic autonomously.\n",
            encoding="utf-8",
        )
        registration.parent.mkdir(parents=True, exist_ok=True)
        digest = source_copy.actual_derived_source_copy_sha256
        record = {
            "registration_id": "fixture-d567-n10-source-copy",
            "basis": "current admission of historical delivery evidence",
            "authorization_ref": ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations.md",
            "registered_at": "2026-10-06T00:00:00+04:00",
            "journal_path": journal.relative_to(self.root).as_posix(),
            "event_id": event["event_id"],
            "event_digest": event["event_digest"],
            "effect_ref": f"{DERIVED_SOURCE_COPY_RELATIVE}#sha256={digest}",
            "action_result_path": action.relative_to(self.root).as_posix(),
            "action_result_sha256": hashlib.sha256(action.read_bytes()).hexdigest(),
            "checkpoint_path": checkpoint.relative_to(self.root).as_posix(),
            "checkpoint_sha256": hashlib.sha256(checkpoint.read_bytes()).hexdigest(),
            "candidate_snapshot_manifest_sha256": candidate.manifest.sha256,
            "executing_release": candidate.authority.executing_release,
            "source_copy_root": DERIVED_SOURCE_COPY_RELATIVE,
            "expected_derived_source_copy_sha256": digest,
            "actual_derived_source_copy_sha256": digest,
            "persistent_inventory_sha256": self._persistent_inventory_sha256(self.target),
        }
        registration.write_text(
            "# Prospective D567 predecessor registration\n\n### Current predecessor trust registrations\n\n```json\n"
            + json.dumps({"schema_version": 1, "registrations": [record]}, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            + "\n```\n",
            encoding="utf-8",
        )
        return registration

    def _registration_payload(self, registration: Path) -> dict:
        text = registration.read_text(encoding="utf-8")
        start = text.index("```json") + len("```json")
        end = text.index("```", start)
        return json.loads(text[start:end])

    def _write_registration_payload(self, registration: Path, payload: dict) -> None:
        registration.write_text(
            "# Prospective D567 predecessor registration\n\n### Current predecessor trust registrations\n\n```json\n"
            + json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            + "\n```\n",
            encoding="utf-8",
        )

    def _assert_predecessor_refusal_is_effect_free(self, *, candidate, selected_release: Path,
                                                    selected_before: dict[str, tuple[bool, bytes, int]]) -> None:
        target_before = records(self.target)
        selector_before = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        parent_before = sorted(path.name for path in self.target.parent.iterdir())
        with patch("release_delivery._write_snapshot", side_effect=AssertionError("must not stage")) as copied, \
                patch("release_delivery.tempfile.mkdtemp", side_effect=AssertionError("must not reserve staging")) as staged, \
                patch("release_delivery.Path.rename", side_effect=AssertionError("must not replace predecessor")) as renamed:
            with self.assertRaises(ReleaseDeliveryError) as refused:
                deliver_release_sources(candidate)
        self.assertEqual(refused.exception.code, "release-copy-predecessor-mismatch")
        self.assertEqual(refused.exception.recovery_paths, ())
        copied.assert_not_called()
        staged.assert_not_called()
        renamed.assert_not_called()
        self.assertEqual(records(self.target), target_before)
        self.assertEqual(records(selected_release), selected_before)
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector_before)
        self.assertEqual(sorted(path.name for path in self.target.parent.iterdir()), parent_before)

    def recorded_completed_predecessor(self, *, register: bool = True):
        """Create a real N10 delivery checkpoint and its canonical receipt.

        The old delivery is intentionally newer than the selected N package:
        that is the narrow completed-but-unpromoted shape that cannot be
        proved from N's retained package rows alone.
        """

        if self.target.exists():
            shutil.rmtree(self.target)  # Disposable test-owned delivery root only.
        run_parent = self.root / ".caprmedio_install/workflow_orchestrator"
        for name in ("runs", "runs-real"):
            stale = run_parent / name
            if stale.is_symlink():
                stale.unlink()
            elif stale.exists():
                shutil.rmtree(stale)  # Disposable test-owned proof carrier only.
        _preflight, n10_candidate, _prior, selected_release, selected_before = self.bootstrap_owned_predecessor()
        manifest = n10_candidate.manifest.model_dump(mode="json", by_alias=True)
        request = {
            "operation": "apply",
            "project_root": str(self.root),
            "candidateSnapshotManifest": manifest,
            "expected_executing_release": manifest["executing_release"],
            "expected_project_structure_digest": manifest["project_structure_digest"],
            "expected_framework_settings_digest": manifest["framework_settings_digest"],
            "expected_source_frontier_digest": manifest["source_frontier_digest"],
            "run_receipt_refs": ["fixture-declared-workflow-receipt"],
        }
        run_id = "release-epic-resume-20261006-N10"
        run = begin_release_action_run(request, workflow_run_id=run_id, checkpoint_callback=lambda _run: None)
        results = []
        for index, (step, action, _phase) in enumerate(PHASES[:3]):
            step_id = f"{run_id}:step:{index + 1}"
            action_id = f"{step_id}:action:1"
            context = SelectedReleaseActionContext(
                str(self.root), run_id, step_id, action_id, run_id, step_id,
                step, action, run.frozen_parameters_sha256, workflow_version=6,
            )
            result = execute_release_action(request, context=context, run=run)
            self.assertEqual(result.outcome, "completed", result.reason)
            results.append(result)
        self.assertIsInstance(run.source_copy, SealedSourceCopy)
        self.assertEqual(results[2].action_run_id, f"{run_id}:step:3:action:1")
        self.assertNotEqual(records(self.target), records(selected_release / "METHODOLOGY/sources"))

        runs = self.root / ".caprmedio_install/workflow_orchestrator/runs" / run_id
        if runs.exists():
            shutil.rmtree(runs)  # Reused only by this disposable test fixture.
        runs.mkdir(parents=True)
        checkpoint_path = runs / "release_action_run.json"
        checkpoint_path.write_text(
            json.dumps(dump_release_checkpoint(run), sort_keys=True, separators=(",", ":")), encoding="utf-8",
        )
        digest = run.source_copy.actual_derived_source_copy_sha256
        effect = f"{DERIVED_SOURCE_COPY_RELATIVE}#sha256={digest}"
        action_run_id = results[2].action_run_id
        action_relative = f".caprmedio_install/workflow_orchestrator/runs/{run_id}/{action_run_id}.json"
        action_path = self.root / action_relative
        action_path.write_text(json.dumps({
            "action_run_id": action_run_id,
            "native_result": {
                "action_atom_id": "CA-O-166",
                "action_run_id": action_run_id,
                "candidate_snapshot_manifest_sha256": n10_candidate.manifest.sha256,
                "effect_evidence_refs": [effect],
                "outcome": "completed",
                "output": {"actual_derived_source_copy_sha256": digest},
            },
        }, sort_keys=True, separators=(",", ":")), encoding="utf-8")
        journal = self.root / ".caprmedio_caprmedio/_journal/run-support-2026-10-06-part-2.ndjson"
        journal.parent.mkdir(parents=True, exist_ok=True)
        event = with_event_digest({
            "schema_version": 5,
            "kind": "workflow_execution",
            "event_id": "fixture-n10-delivery",
            "action_id": "fixture-n10-delivery",
            "event": "completed",
            "author": "fixture",
            "occurred_at": "2026-10-06T00:00:00+04:00",
            "llm_session": {"app": "codex", "uuid": "fixture-n10"},
            "structural_scope": "TOOLS",
            "initiative": {"initiative_id": "fixture-n10", "instruction_summary": "fixture", "initiative_ref": "03_plan/fixture.md"},
            "run": {"run_id": action_run_id, "kind": "action", "definition": {"atom_id": "CA-O-166", "version": 1, "path": "operations/CA-O-166.md", "digest": "a" * 64}},
            "definition_bindings": [{"kind": "action", "atom_id": "CA-O-166", "version": 1, "path": "operations/CA-O-166.md", "digest": "a" * 64}],
            "input_ref": "inputs/fixture-n10.json",
            "outcome": "completed",
            "result_ref": action_relative,
            "effect_refs": [effect],
            "report_ref": "reports/fixture-n10.md",
            "redaction": {"redacted": False, "fields": []},
        })
        journal.write_text(json.dumps(event, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
        self.assertFalse(release_predecessor.verify_recorded_source_predecessor(
            self.root, n10_candidate.authority.executing_release, self.target,
        ))
        registration = None
        if register:
            registration = self._register_d567_predecessor(
                candidate=n10_candidate, source_copy=run.source_copy, journal=journal,
                event=event, checkpoint=checkpoint_path, action=action_path,
            )
            self.assertTrue(release_predecessor.verify_recorded_source_predecessor(
                self.root, n10_candidate.authority.executing_release, self.target,
            ))

        self.fixture.core.write_bytes(compilation_test.carrier("CA-R-001", version=3))
        fresh_preflight, fresh_candidate = build_preflight_validated_candidate(
            self.root, candidate_release="N+3",
            full_suite_environment={"runner": "fixture", "command": ["python", "-m", "unittest"], "working_directory": "."},
            candidate_image_reference="fixture:N+3",
        )
        self.assertEqual(fresh_candidate.authority.executing_release, n10_candidate.authority.executing_release)
        return fresh_preflight, fresh_candidate, selected_release, selected_before, journal, checkpoint_path, action_path, registration

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

    def test_current_delivery_with_different_ephemeral_metadata_is_a_noop(self) -> None:
        preflight, candidate = self.fixture.build()
        first = deliver_release_sources(candidate)
        inode = self.target.stat().st_ino
        source_metadata = self.fixture.source / ".DS_Store"
        delivery_metadata = self.target / ".DS_Store"
        source_metadata.write_bytes(b"canonical finder metadata\n")
        delivery_metadata.write_bytes(b"delivery finder metadata\n")

        second = deliver_release_sources(candidate)

        self.assertEqual(second, first)
        self.assertEqual(self.target.stat().st_ino, inode)
        self.assertEqual(source_metadata.read_bytes(), b"canonical finder metadata\n")
        self.assertEqual(delivery_metadata.read_bytes(), b"delivery finder metadata\n")
        self.assertEqual(list(self.target.parent.glob(".release-sources-*")), [])

    def test_predecessor_reservation_refuses_prepopulated_backup_child(self) -> None:
        """Mocked reservation setup only; it does not exercise publication."""
        parent = self.root / "fixture-reservation-parent"
        parent.mkdir()
        destination = parent / "sources"
        wrapper = parent / ".release-sources-prior-private-fixture"
        wrapper.mkdir()
        (wrapper / destination.name).mkdir()
        with patch("release_delivery.tempfile.mkdtemp", return_value=str(wrapper)):
            with self.assertRaises(ReleaseDeliveryError) as collision:
                release_delivery._bind_reservation_identity(
                    release_delivery._reserve_predecessor(parent, destination)
                )
        self.assertEqual("release-copy-collision", collision.exception.code)
        self.assertTrue((wrapper / destination.name).is_dir())

    def test_predecessor_reservation_retains_empty_private_wrapper(self) -> None:
        """Reservation allocation leaves its wrapper intact and child absent."""
        parent = self.root / "fixture-reservation-parent"
        parent.mkdir()
        destination = parent / "sources"
        wrapper = parent / ".release-sources-prior-private-fixture"
        wrapper.mkdir()
        with patch("release_delivery.tempfile.mkdtemp", return_value=str(wrapper)):
            reservation = release_delivery._reserve_predecessor(parent, destination)
        self.assertEqual(wrapper, reservation.wrapper)
        self.assertTrue(reservation.wrapper.is_dir())
        self.assertFalse(reservation.backup.exists())

    def test_predecessor_reservation_refuses_symlink_or_substituted_wrapper(self) -> None:
        """Mocked reservation identities never authorize a substituted wrapper."""
        parent = self.root / "fixture-reservation-parent"
        parent.mkdir()
        destination = parent / "sources"
        outside = self.root / "fixture-reservation-outside"
        outside.mkdir()
        symlink_wrapper = parent / ".release-sources-prior-private-link"
        symlink_wrapper.symlink_to(outside, target_is_directory=True)
        with patch("release_delivery.tempfile.mkdtemp", return_value=str(symlink_wrapper)):
            with self.assertRaises(ReleaseDeliveryError) as unsafe_link:
                release_delivery._bind_reservation_identity(
                    release_delivery._reserve_predecessor(parent, destination)
                )
        self.assertEqual("release-copy-path-unsafe", unsafe_link.exception.code)

        wrapper = parent / ".release-sources-prior-private-owned"
        wrapper.mkdir()
        with patch("release_delivery.tempfile.mkdtemp", return_value=str(wrapper)):
            reservation = release_delivery._reserve_predecessor(parent, destination)
        release_delivery._bind_reservation_identity(reservation)
        actual_identity = release_delivery._nofollow_directory_identity
        # Boundary mock: model replacement after reservation without invoking
        # host directory cleanup, which is unavailable in this fixture host.
        with patch(
            "release_delivery._nofollow_directory_identity",
            side_effect=lambda path, *, label: (0, 0) if path == wrapper else actual_identity(path, label=label),
        ):
            with self.assertRaises(ReleaseDeliveryError) as unsafe_substitution:
                release_delivery._validate_reservation(reservation, require_absent_backup=True)
        self.assertEqual("release-copy-path-unsafe", unsafe_substitution.exception.code)

    def test_predecessor_reservation_refuses_substituted_rollback_child(self) -> None:
        """Only the inode-recorded old-tree child may be used for rollback."""
        parent = self.root / "fixture-reservation-parent"
        parent.mkdir()
        destination = parent / "sources"
        wrapper = parent / ".release-sources-prior-private-owned"
        wrapper.mkdir()
        with patch("release_delivery.tempfile.mkdtemp", return_value=str(wrapper)):
            reservation = release_delivery._reserve_predecessor(parent, destination)
        release_delivery._bind_reservation_identity(reservation)
        reservation.backup.mkdir()
        backup_identity = release_delivery._nofollow_directory_identity(
            reservation.backup, label="fixture backup",
        )
        release_delivery._record_predecessor_backup(reservation, backup_identity)
        actual_identity = release_delivery._nofollow_directory_identity
        # Boundary mock: a different backup inode is refused before rollback.
        with patch(
            "release_delivery._nofollow_directory_identity",
            side_effect=lambda path, *, label: (0, 0) if path == reservation.backup else actual_identity(path, label=label),
        ):
            with self.assertRaises(ReleaseDeliveryError) as unsafe_child:
                release_delivery._validate_reservation(reservation, require_owned_backup=True)
        self.assertEqual("release-copy-path-unsafe", unsafe_child.exception.code)

    def test_unbound_reservation_survives_binding_refusal_for_recovery(self) -> None:
        """A fixture-only identity race retains the just-created wrapper."""
        parent = self.root / "fixture-reservation-parent"
        parent.mkdir()
        destination = parent / "sources"
        wrapper = parent / ".release-sources-prior-private-owned"
        wrapper.mkdir()
        with patch("release_delivery.tempfile.mkdtemp", return_value=str(wrapper)):
            reservation = release_delivery._reserve_predecessor(parent, destination)
        actual_identity = release_delivery._nofollow_directory_identity
        wrapper_calls = 0

        def swapped_after_binding(path, *, label):
            nonlocal wrapper_calls
            if path == wrapper:
                wrapper_calls += 1
                if wrapper_calls == 2:
                    return (0, 0)
            return actual_identity(path, label=label)

        with patch("release_delivery._nofollow_directory_identity", side_effect=swapped_after_binding):
            with self.assertRaises(ReleaseDeliveryError) as unsafe:
                release_delivery._bind_reservation_identity(reservation)
        self.assertEqual("release-copy-path-unsafe", unsafe.exception.code)
        self.assertTrue(reservation.wrapper.is_dir())
        self.assertFalse(reservation.backup.exists())

    def test_record_predecessor_backup_refuses_child_swapped_before_identity_capture(self) -> None:
        """A child observed after the move must retain the pre-move inode."""
        parent = self.root / "fixture-reservation-parent"
        parent.mkdir()
        destination = parent / "sources"
        wrapper = parent / ".release-sources-prior-private-owned"
        wrapper.mkdir()
        with patch("release_delivery.tempfile.mkdtemp", return_value=str(wrapper)):
            reservation = release_delivery._reserve_predecessor(parent, destination)
        release_delivery._bind_reservation_identity(reservation)
        reservation.backup.mkdir()
        expected_identity = release_delivery._nofollow_directory_identity(
            reservation.backup, label="fixture original predecessor",
        )
        actual_identity = release_delivery._nofollow_directory_identity
        with patch(
            "release_delivery._nofollow_directory_identity",
            side_effect=lambda path, *, label: (0, 0) if path == reservation.backup else actual_identity(path, label=label),
        ):
            with self.assertRaises(ReleaseDeliveryError) as unsafe:
                release_delivery._record_predecessor_backup(reservation, expected_identity)
        self.assertEqual("release-copy-path-unsafe", unsafe.exception.code)
        self.assertIsNone(reservation.backup_identity)

    def test_secret_shaped_ephemeral_source_or_delivery_carrier_refuses_without_mutation(self) -> None:
        _preflight, candidate = self.fixture.build()
        source_secret = self.fixture.source / ".env.pyc"
        source_secret.write_bytes(b"source secret-shaped bytecode\n")
        with self.assertRaises(ReleaseDeliveryError) as source_refusal:
            release_delivery._snapshot(self.fixture.source)
        self.assertEqual(source_refusal.exception.code, "release-copy-path-unsafe")
        self.assertEqual(source_secret.read_bytes(), b"source secret-shaped bytecode\n")
        self.assertFalse(self.target.exists())

        source_secret.unlink()
        delivered = deliver_release_sources(candidate)
        target_secret = self.target / ".env.pyc"
        target_secret.write_bytes(b"delivery secret-shaped bytecode\n")
        target_before = records(self.target)
        inode = self.target.stat().st_ino
        with self.assertRaises(ReleaseDeliveryError) as delivery_refusal:
            deliver_release_sources(candidate)
        self.assertEqual(delivery_refusal.exception.code, "release-copy-path-unsafe")
        self.assertEqual(records(self.target), target_before)
        self.assertEqual(self.target.stat().st_ino, inode)
        self.assertEqual(target_secret.read_bytes(), b"delivery secret-shaped bytecode\n")
        self.assertTrue(delivered.actual_derived_source_copy_sha256)

    def test_owned_executing_package_replacement_retains_n_and_prior_derived_tree(self) -> None:
        preflight, candidate, prior, release, retained = self.owned_predecessor()
        # The stager has no byte rows for empty folders. Keep even an extra
        # empty predecessor folder in the retained derived tree.
        (self.target / "unknown-empty").mkdir()
        prior = records(self.target)
        selector = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        # The predecessor reservation is retained as the backup wrapper; its
        # old tree must move into ``sources`` without deleting the wrapper.
        with patch("release_delivery.Path.rmdir", side_effect=AssertionError("reservation cleanup is forbidden")) as removed:
            delivered = deliver_release_sources(candidate)
        removed.assert_not_called()
        self.assertEqual(records(self.target), records(self.fixture.source))
        self.assertEqual(records(release), retained)
        backups = list(self.target.parent.glob(".release-sources-prior-*"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(records(backups[0] / "sources"), prior)
        self.assertEqual(delivered.actual_derived_source_copy_sha256, preflight.expected_derived_source_copy_sha256)
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector)
        stage_framework_package(self.root, render_release_candidate(candidate, preflight))
        self.assertEqual(records(release), retained)

    def test_bootstrap_executing_package_replacement_accepts_only_exact_selector_bound_shape(self) -> None:
        preflight, candidate, _prior, release, retained = self.bootstrap_owned_predecessor()
        # Ephemeral macOS metadata is excluded by every persistent inventory,
        # including retained-package verification.  It is not deleted or
        # otherwise changed while proving the bootstrap predecessor.
        (self.target / ".DS_Store").write_bytes(b"transient finder metadata\n")
        metadata_paths = (
            release / ".DS_Store",
            release / "METHODOLOGY/.DS_Store",
            release / "METHODOLOGY/sources/.DS_Store",
            release / "METHODOLOGY/sources/001_CORE_META_MODEL/.DS_Store",
        )
        for path in metadata_paths:
            path.write_bytes(b"transient finder metadata\n")
        retained = records(release)
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

    def test_unrecorded_predecessor_proof_is_terminal_before_any_delivery_effect(self) -> None:
        """The completed-copy exception cannot create staging when proof fails."""

        _preflight, candidate, prior, release, retained = self.owned_predecessor()
        unowned = self.target / "unowned" / "predecessor.md"
        unowned.parent.mkdir()
        unowned.write_bytes(b"unrecorded predecessor proof must not be accepted\n")
        target_before = records(self.target)
        release_before = records(release)
        selector_before = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        parent_before = sorted(path.name for path in self.target.parent.iterdir())

        with patch("release_delivery.verify_recorded_source_predecessor", return_value=False) as proof, \
                patch("release_delivery._write_snapshot", side_effect=AssertionError("must not stage")) as copied, \
                patch("release_delivery.tempfile.mkdtemp", side_effect=AssertionError("must not reserve staging")) as staged, \
                patch("release_delivery.Path.rename", side_effect=AssertionError("must not replace predecessor")) as renamed:
            with self.assertRaises(ReleaseDeliveryError) as refused:
                deliver_release_sources(candidate)

        self.assertEqual(refused.exception.code, "release-copy-predecessor-mismatch")
        self.assertEqual(refused.exception.recovery_paths, ())
        proof.assert_called_once_with(self.root, candidate.authority.executing_release, self.target)
        copied.assert_not_called()
        staged.assert_not_called()
        renamed.assert_not_called()
        self.assertEqual(records(self.target), target_before)
        self.assertEqual(records(release), release_before)
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector_before)
        self.assertEqual(sorted(path.name for path in self.target.parent.iterdir()), parent_before)
        self.assertNotEqual(records(self.target), prior)

    def test_recorded_completed_unpromoted_delivery_replaces_only_after_codec_proof(self) -> None:
        """A fresh candidate may replace the authenticated N10 delivery once."""

        preflight, candidate, selected_release, selected_before, journal, checkpoint, action, registration = self.recorded_completed_predecessor()
        target_before = records(self.target)
        # The frozen N package contains an older source tree, so normal
        # package-row predecessor proof must fail before the closed receipt is
        # considered.  This establishes that the following delivery took the
        # recorded-proof branch, not a permissive retained-package branch.
        with self.assertRaises(ReleaseDeliveryError) as ordinary_proof:
            release_delivery._prove_predecessor(self.root, candidate, self.target)
        self.assertEqual(ordinary_proof.exception.code, "release-copy-predecessor-mismatch")
        self.assertFalse(release_predecessor.verify_recorded_source_predecessor(
            self.root, "0" * 64, self.target,
        ))

        backups_before = list(self.target.parent.glob(".release-sources-prior-*"))
        recorded_bytes = {path: path.read_bytes() for path in (journal, checkpoint, action)}
        delivered = deliver_release_sources(candidate)

        self.assertEqual(records(self.target), records(self.fixture.source))
        self.assertEqual(records(selected_release), selected_before)
        self.assertEqual(delivered.actual_derived_source_copy_sha256, preflight.expected_derived_source_copy_sha256)
        self.assertTrue(journal.is_file())
        self.assertTrue(checkpoint.is_file())
        self.assertTrue(action.is_file())
        self.assertTrue(registration.is_file())
        self.assertEqual({path: path.read_bytes() for path in recorded_bytes}, recorded_bytes)
        self.assertEqual(len(backups_before), 1)
        # A repeat can happen only once against the exact new target.
        self.assertEqual(deliver_release_sources(candidate), delivered)
        backups = list(self.target.parent.glob(".release-sources-prior-*"))
        self.assertEqual(len(backups), 2)
        new_backups = set(backups) - set(backups_before)
        self.assertEqual(len(new_backups), 1)
        self.assertEqual(records(new_backups.pop() / "sources"), target_before)

    def test_completed_codec_and_journal_without_d567_registration_refuse_before_effect(self) -> None:
        """A valid historical carrier becomes usable only through D567 v3."""

        _preflight, candidate, selected_release, selected_before, _journal, _checkpoint, _action, registration = (
            self.recorded_completed_predecessor(register=False)
        )
        self.assertIsNone(registration)
        self.assertFalse(release_predecessor.verify_recorded_source_predecessor(
            self.root, candidate.authority.executing_release, self.target,
        ))
        self._assert_predecessor_refusal_is_effect_free(
            candidate=candidate, selected_release=selected_release, selected_before=selected_before,
        )

    def test_d567_registration_refuses_missing_unknown_duplicate_wrong_n_and_inventory_drift(self) -> None:
        """Every registration mismatch stops before delivery can reserve staging."""

        for mutation in ("missing", "unknown", "duplicate", "wrong-n", "schema-true", "schema-false", "empty-dir-mode"):
            with self.subTest(mutation=mutation):
                _preflight, candidate, selected_release, selected_before, _journal, _checkpoint, _action, registration = (
                    self.recorded_completed_predecessor()
                )
                if mutation == "missing":
                    registration.unlink()
                elif mutation == "empty-dir-mode":
                    (self.target / "001_CORE_META_MODEL/04_requirement/empty/private").chmod(0o755)
                else:
                    payload = self._registration_payload(registration)
                    record = payload["registrations"][0]
                    if mutation == "unknown":
                        record["unadmitted"] = "fixture"
                    elif mutation == "duplicate":
                        duplicate = dict(record)
                        duplicate["registration_id"] = "fixture-d567-duplicate"
                        payload["registrations"].append(duplicate)
                    elif mutation == "schema-true":
                        payload["schema_version"] = True
                    elif mutation == "schema-false":
                        payload["schema_version"] = False
                    else:
                        record["executing_release"] = "0" * 64
                    self._write_registration_payload(registration, payload)
                self.assertFalse(release_predecessor.verify_recorded_source_predecessor(
                    self.root, candidate.authority.executing_release, self.target,
                ))
                self._assert_predecessor_refusal_is_effect_free(
                    candidate=candidate, selected_release=selected_release, selected_before=selected_before,
                )

    def test_d567_registration_refuses_parent_symlink_and_journal_effect_or_digest_mismatch(self) -> None:
        for mutation in ("proof-parent-symlink", "journal-effect", "journal-digest"):
            with self.subTest(mutation=mutation):
                _preflight, candidate, selected_release, selected_before, journal, _checkpoint, _action, registration = (
                    self.recorded_completed_predecessor()
                )
                if mutation == "proof-parent-symlink":
                    runs = self.root / ".caprmedio_install/workflow_orchestrator/runs"
                    displaced = runs.with_name("runs-real")
                    runs.rename(displaced)
                    runs.symlink_to(displaced, target_is_directory=True)
                else:
                    event = json.loads(journal.read_text(encoding="utf-8"))
                    if mutation == "journal-effect":
                        event["effect_refs"] = ["wrong-effect"]
                        journal.write_text(json.dumps(with_event_digest(event), sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
                    else:
                        event["event_digest"] = "0" * 64
                        journal.write_text(json.dumps(event, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
                self.assertFalse(release_predecessor.verify_recorded_source_predecessor(
                    self.root, candidate.authority.executing_release, self.target,
                ))
                self._assert_predecessor_refusal_is_effect_free(
                    candidate=candidate, selected_release=selected_release, selected_before=selected_before,
                )

    def test_d567_registration_refuses_quoted_or_wrong_active_plan_authorization(self) -> None:
        """Only current Plan metadata, never prose or quoted front matter, authorizes admission."""

        for mutation in ("archived-with-quoted-active", "wrong-plan-with-quoted-right-id", "duplicate-frontmatter"):
            with self.subTest(mutation=mutation):
                _preflight, candidate, selected_release, selected_before, _journal, _checkpoint, _action, registration = (
                    self.recorded_completed_predecessor()
                )
                authorization = self.root / ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations.md"
                if mutation == "archived-with-quoted-active":
                    authorization.write_text(
                        "---\natom_id: CA-P-1117\ncontent_role: Plan\nstatus: Archived\n---\n\n"
                        "> atom_id: CA-P-1117\n> status: Active\n> Complete this Epic autonomously\n",
                        encoding="utf-8",
                    )
                elif mutation == "wrong-plan-with-quoted-right-id":
                    authorization.write_text(
                        "---\natom_id: CA-P-9999\ncontent_role: Plan\nstatus: Active\n---\n\n"
                        "> atom_id: CA-P-1117\n> status: Active\n> Complete this Epic autonomously\n",
                        encoding="utf-8",
                    )
                else:
                    authorization.write_text(
                        "---\natom_id: CA-P-1117\ncontent_role: Plan\nstatus: Active\nstatus: Archived\n---\n\n"
                        "Complete this Epic autonomously.\n",
                        encoding="utf-8",
                    )
                self.assertTrue(registration.is_file())
                self.assertFalse(release_predecessor.verify_recorded_source_predecessor(
                    self.root, candidate.authority.executing_release, self.target,
                ))
                self._assert_predecessor_refusal_is_effect_free(
                    candidate=candidate, selected_release=selected_release, selected_before=selected_before,
                )

    def test_d567_registration_refuses_internally_recomputed_native_or_checkpoint_tampering(self) -> None:
        """Updating the registration hashes cannot broaden the sealed N10 evidence."""

        for mutation in ("native-outcome", "checkpoint-workflow"):
            with self.subTest(mutation=mutation):
                _preflight, candidate, selected_release, selected_before, _journal, checkpoint, action, registration = (
                    self.recorded_completed_predecessor()
                )
                payload = self._registration_payload(registration)
                record = payload["registrations"][0]
                if mutation == "native-outcome":
                    native = json.loads(action.read_text(encoding="utf-8"))
                    native["native_result"]["outcome"] = "pending"
                    action.write_text(json.dumps(native, sort_keys=True, separators=(",", ":")), encoding="utf-8")
                    record["action_result_sha256"] = hashlib.sha256(action.read_bytes()).hexdigest()
                else:
                    sealed = json.loads(checkpoint.read_text(encoding="utf-8"))
                    sealed["workflow_run_id"] = "tampered-workflow"
                    for item in sealed["contexts"]:
                        item["context"]["workflow_run_id"] = "tampered-workflow"
                        item["context"]["parent_workflow_run_id"] = "tampered-workflow"
                    for item in sealed["results"]:
                        item["result"]["workflow_run_id"] = "tampered-workflow"
                    sealed["sha256"] = release_action_checkpoint_sha256(sealed)
                    checkpoint.write_text(json.dumps(sealed, sort_keys=True, separators=(",", ":")), encoding="utf-8")
                    record["checkpoint_sha256"] = hashlib.sha256(checkpoint.read_bytes()).hexdigest()
                self._write_registration_payload(registration, payload)
                self.assertFalse(release_predecessor.verify_recorded_source_predecessor(
                    self.root, candidate.authority.executing_release, self.target,
                ))
                self._assert_predecessor_refusal_is_effect_free(
                    candidate=candidate, selected_release=selected_release, selected_before=selected_before,
                )

    def test_invalid_recorded_predecessor_carriers_refuse_before_staging(self) -> None:
        """No malformed N10 proof can convert an occupied tree into an effect."""

        for mutation in ("unrecorded", "tampered-action", "wrong-run", "changed-mode"):
            with self.subTest(mutation=mutation):
                preflight, candidate, selected_release, selected_before, journal, _checkpoint, action, _registration = self.recorded_completed_predecessor()
                if mutation == "unrecorded":
                    journal.write_text("", encoding="utf-8")
                elif mutation == "tampered-action":
                    action.write_text("{}", encoding="utf-8")
                elif mutation == "wrong-run":
                    event = json.loads(journal.read_text(encoding="utf-8"))
                    event["run"]["run_id"] = "release-epic-resume-20261006-N9:step:3:action:1"
                    journal.write_text(json.dumps(with_event_digest(event), sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
                else:
                    copied = self.target / self.fixture.core.relative_to(self.fixture.source)
                    copied.chmod(0o600)
                target_before = records(self.target)
                selector_before = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
                parent_before = sorted(path.name for path in self.target.parent.iterdir())

                with patch("release_delivery._write_snapshot", side_effect=AssertionError("must not stage")) as copied, \
                        patch("release_delivery.tempfile.mkdtemp", side_effect=AssertionError("must not reserve staging")) as staged, \
                        patch("release_delivery.Path.rename", side_effect=AssertionError("must not replace predecessor")) as renamed:
                    with self.assertRaises(ReleaseDeliveryError) as refused:
                        deliver_release_sources(candidate)

                self.assertEqual(refused.exception.code, "release-copy-predecessor-mismatch")
                self.assertEqual(refused.exception.recovery_paths, ())
                copied.assert_not_called()
                staged.assert_not_called()
                renamed.assert_not_called()
                self.assertEqual(records(self.target), target_before)
                self.assertEqual(records(selected_release), selected_before)
                self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector_before)
                self.assertEqual(sorted(path.name for path in self.target.parent.iterdir()), parent_before)
                self.assertTrue(preflight.expected_derived_source_copy_sha256)

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
        selector_before = (self.root / ".caprmedio_runtime/framework/current.toml").read_bytes()
        original_rename = Path.rename
        def refuse_publication(path, target):
            if path.name.startswith(f".release-sources-{candidate.manifest.sha256[:12]}-"):
                raise OSError("injected fixture publication failure")
            return original_rename(path, target)
        with (
            patch("release_delivery.Path.rmdir", side_effect=AssertionError("reservation cleanup is forbidden")) as removed,
            patch("release_delivery.Path.rename", autospec=True, side_effect=refuse_publication),
        ):
            with self.assertRaises(ReleaseDeliveryError) as failed:
                deliver_release_sources(candidate)
        removed.assert_not_called()
        self.assertEqual(failed.exception.code, "release-copy-failed")
        self.assertEqual(records(self.target), prior)
        self.assertEqual(records(release), retained)
        self.assertEqual((self.root / ".caprmedio_runtime/framework/current.toml").read_bytes(), selector_before)
        reservations = list(self.target.parent.glob(".release-sources-prior-*"))
        self.assertEqual(len(reservations), 1)
        self.assertFalse((reservations[0] / "sources").exists())
        self.assertIn(reservations[0].relative_to(self.root).as_posix(), failed.exception.recovery_paths)
        self.assertTrue(any(path.startswith("101_LAYER_1_FRAMEWORK_METHODOLOGY/.release-sources-")
                            for path in failed.exception.recovery_paths))


if __name__ == "__main__":
    unittest.main()
