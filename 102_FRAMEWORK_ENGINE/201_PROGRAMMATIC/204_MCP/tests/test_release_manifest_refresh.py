"""Regression proof for the narrow, source-pinned Release-admission refresh."""
from __future__ import annotations

from contextlib import contextmanager
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import types
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
APP_TESTS = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
TOOLS = MCP.parent / "201_TOOLS"
for location in (MCP, MCP / "tests", APP_TESTS, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import release_source_admission as admission_module  # noqa: E402
import test_release_source_admission as source_goldens  # noqa: E402
from release_manifest_authorization import (  # noqa: E402
    authorize_operator_publication,
    authorize_operator_publication_recovery,
    authorize_operator_refresh,
)
from release_manifest_lifecycle import ReleaseManifestLifecycle  # noqa: E402
from release_manifest_publisher import (  # noqa: E402
    ReleaseManifestPublishError,
    plan_release_manifest_refresh,
    plan_release_manifest_publish,
    publish_release_manifest,
    recover_release_manifest_publish,
    refresh_release_manifest,
)
from release_source_admission import derive_release_graph_admission  # noqa: E402
from selected_routes import (  # noqa: E402
    SelectedRouteError,
    canonical_digest,
    load_release_manifest_refresh_base,
    load_selected_manifest,
    selected_manifest_ref,
)
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402


class ReleaseManifestRefreshTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        source_goldens.ReleaseSourceAdmissionTest.setUpClass()

    def setUp(self) -> None:
        self.fixture = source_goldens.ReleaseSourceAdmissionTest()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        project = GoldenProject(REPOSITORY, self.root, GoldenCase("W04", "change_atom_status"))
        original_copy_pinned = project._copy_pinned
        old_action = Path(
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/"
            "CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md"
        )
        archive = old_action.parent / "archive" / (old_action.stem + "@3.md")

        def copy_historical_pin(relative: Path, expected_digest: object) -> None:
            if relative == old_action and expected_digest == "b5d052e97bae6ada98849380199e5c67cbf090900beb33ca202f7872d56301e8":
                source = REPOSITORY / archive
                target = self.root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
                return
            original_copy_pinned(relative, expected_digest)

        project._copy_pinned = copy_historical_pin
        project._copy_reviewed_manifest()
        for relative in (
            Path(".caprmedio_caprmedio/operators_registry.toml"),
            Path(".caprmedio_caprmedio/caprmedio_project_settings.toml"),
        ):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / relative, target)
        self.path = self.root / selected_manifest_ref(self.root)
        initial_plan = plan_release_manifest_publish(self.root)
        initial_context = authorize_operator_publication(
            self.root,
            initial_plan,
            operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "release-manifest-refresh-initial"},
            authorization_ref="authorization/release-manifest-refresh-initial.md",
        )
        self.initial_context = initial_context
        with patch(
            "release_manifest_lifecycle.subprocess.run",
            return_value=types.SimpleNamespace(returncode=0, stdout="0" * 40 + "\n"),
        ):
            initial_result = publish_release_manifest(self.root, execute=True, authorization=initial_context)
        self.assertEqual("published", initial_result["disposition"])
        self.initial_bytes = self.path.read_bytes()
        self.initial = load_selected_manifest(self.root)
        self.assertEqual(16, len(self.initial["routes"]))
        self.assertEqual(1, len(self.initial["release_source_admissions"]))

    def _authorize(self, plan: dict) -> object:
        return authorize_operator_refresh(
            self.root,
            plan,
            operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "release-manifest-refresh"},
            authorization_ref="authorization/release-manifest-refresh.md",
        )

    def _recovery_authorization(self, event_id: str) -> object:
        return authorize_operator_publication_recovery(
            self.root,
            event_id,
            operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "release-manifest-refresh"},
            authorization_ref="authorization/release-manifest-refresh-recovery.md",
        )

    def _pending_ids(self) -> list[str]:
        pending = self.root / ".caprmedio_runtime/state/work_journal/pending"
        return sorted(path.stem for path in pending.glob("release-manifest:*.json")) if pending.exists() else []

    def _resign(self, manifest: dict) -> bytes:
        manifest["source_freshness"]["selected_binding_digest"] = canonical_digest(manifest["routes"])
        unsigned = {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
        manifest["canonical_manifest_sha256"] = canonical_digest(unsigned)
        return json.dumps(manifest, separators=(",", ":")).encode("utf-8")

    def _git_evidence(self) -> object:
        return patch(
            "release_manifest_lifecycle.subprocess.run",
            return_value=types.SimpleNamespace(returncode=0, stdout="a" * 40 + "\n"),
        )

    @contextmanager
    def advanced_admission(self):
        """Advance one legal RMED pin and its D572 trust anchor in this fixture only."""
        old_admission = self.initial["release_source_admissions"][0]
        private_paths = {row["source_path"] for row in self.fixture.private_carriers}
        pin = next(pin for pin in old_admission["rmed_frontier"] if pin["source_path"] not in private_paths)
        source = self.root / pin["source_path"]
        authority = self.root / source_goldens.AUTHORITY_REF
        source_before, authority_before = source.read_bytes(), authority.read_bytes()
        updated_source = re.sub(
            rf"(?m)^version:\s*{pin['version']}\s*$",
            f"version: {pin['version'] + 1}",
            source_before.decode("utf-8"),
            count=1,
        ).encode("utf-8")
        self.assertNotEqual(source_before, updated_source)
        updated_digest = hashlib.sha256(updated_source).hexdigest()
        old_row = f"| {pin['atom_id']} | {pin['version']} | `{pin['source_path']}` | `{pin['digest']}` |"
        new_row = f"| {pin['atom_id']} | {pin['version'] + 1} | `{pin['source_path']}` | `{updated_digest}` |"
        updated_authority = authority_before.decode("utf-8").replace(old_row, new_row, 1).encode("utf-8")
        self.assertNotEqual(authority_before, updated_authority)
        source.write_bytes(updated_source)
        authority.write_bytes(updated_authority)
        trusted_authority = {
            **admission_module.AUTHORITY_PIN,
            "digest": hashlib.sha256(updated_authority).hexdigest(),
        }
        try:
            with patch.object(admission_module, "AUTHORITY_PIN", trusted_authority):
                route, admission = derive_release_graph_admission(self.root)
                yield route, admission
        finally:
            source.write_bytes(source_before)
            authority.write_bytes(authority_before)

    def test_stale_additive_sixteen_plan_is_effect_free_and_replaces_only_admission(self) -> None:
        with self.advanced_admission() as (current_route, current_admission):
            with self.assertRaises(SelectedRouteError):
                load_selected_manifest(self.root)
            base = load_release_manifest_refresh_base(self.root)
            self.assertEqual(self.initial["routes"], base["routes"])
            plan = plan_release_manifest_refresh(self.root)
            self.assertEqual("plan", plan["mode"])
            self.assertEqual("refresh", plan["publication_operation"])
            self.assertEqual([row["route"] for row in self.initial["routes"]], plan["current_route_names"])
            self.assertEqual(plan["current_route_names"], plan["candidate_route_names"])
            self.assertEqual(self.initial_bytes, self.path.read_bytes())

            result = refresh_release_manifest(self.root, execute=True, authorization=self._authorize(plan))
            loaded = load_selected_manifest(self.root)
            self.assertEqual("published", result["disposition"], result)
            self.assertEqual("refresh", result["publication_operation"])
            self.assertEqual(self.initial["routes"], loaded["routes"])
            self.assertEqual(self.initial["query_source_admissions"], loaded["query_source_admissions"])
            for field in ("selected_source_registry_ref", "selected_source_registry_version", "selected_source_registry_digest"):
                self.assertEqual(self.initial["source_freshness"][field], loaded["source_freshness"][field])
            self.assertEqual(current_route, loaded["routes"][-1])
            self.assertEqual([current_admission], loaded["release_source_admissions"])
            self.assertNotEqual(self.initial["release_source_admissions"], loaded["release_source_admissions"])

    def test_closed_registered_source_successor_uses_the_same_trusted_refresh_lifecycle(self) -> None:
        """D588 falls through the existing refresh boundary; it adds no lifecycle."""
        with self.advanced_admission() as (_, current_admission):
            candidate = copy.deepcopy(self.initial)
            candidate.pop("manifest_ref")
            candidate["release_source_admissions"] = [copy.deepcopy(current_admission)]
            candidate.pop("canonical_manifest_sha256")
            candidate["canonical_manifest_sha256"] = canonical_digest(candidate)
            payload = json.dumps(candidate, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
            derived = (copy.deepcopy(self.initial), candidate, payload, self.path)
            with patch(
                "selected_routes.load_release_manifest_refresh_base",
                side_effect=SelectedRouteError("registered historical source input"),
            ), patch("selected_source_refresh.derive_registered_source_refresh", return_value=derived), self._git_evidence():
                plan = plan_release_manifest_refresh(self.root)
                self.assertEqual(self.initial_bytes, self.path.read_bytes())
                result = refresh_release_manifest(self.root, execute=True, authorization=self._authorize(plan))
            self.assertEqual("published", result["disposition"], result)
            self.assertEqual(payload, self.path.read_bytes())
            self.assertEqual([current_admission], load_selected_manifest(self.root)["release_source_admissions"])

    def test_current_or_forged_or_wrong_operation_refresh_refuses_before_effects(self) -> None:
        with self.assertRaises(ReleaseManifestPublishError):
            plan_release_manifest_refresh(self.root)
        self.assertEqual(self.initial_bytes, self.path.read_bytes())
        with self.advanced_admission():
            plan = plan_release_manifest_refresh(self.root)
            with self.assertRaises(ReleaseManifestPublishError):
                refresh_release_manifest(self.root, execute=True, authorization=self.initial_context)
            self.assertEqual(self.initial_bytes, self.path.read_bytes())
            self.assertEqual([], self._pending_ids())
            with self.assertRaises(ReleaseManifestPublishError):
                refresh_release_manifest(self.root, execute=True, authorization={"authorized": True})
            forged = dict(plan)
            forged.pop("publication_operation")
            with self.assertRaises(ValueError):
                self._authorize(forged)
            with self.assertRaises(ReleaseManifestPublishError):
                publish_release_manifest(self.root, execute=True, authorization=self._authorize(plan))
            self.assertEqual(self.initial_bytes, self.path.read_bytes())

    def test_input_and_postseal_drift_refuse_without_a_replacement(self) -> None:
        with self.advanced_admission():
            plan = plan_release_manifest_refresh(self.root)
            context = self._authorize(plan)
            self.path.write_bytes(self.initial_bytes + b"\ninput drift\n")
            with self.assertRaises(ReleaseManifestPublishError):
                refresh_release_manifest(self.root, execute=True, authorization=context)
            self.assertEqual(self.initial_bytes + b"\ninput drift\n", self.path.read_bytes())
            self.path.write_bytes(self.initial_bytes)

            original_prepare = ReleaseManifestLifecycle.prepare_release_manifest_publication

            def seal_then_drift(lifecycle: object, sealed: dict, payload: bytes, **kwargs: object) -> str:
                event_id = original_prepare(lifecycle, sealed, payload, **kwargs)
                self.path.write_bytes(self.path.read_bytes() + b"\npost-seal drift\n")
                return event_id

            with self._git_evidence(), patch.object(
                ReleaseManifestLifecycle, "prepare_release_manifest_publication", new=seal_then_drift,
            ):
                result = refresh_release_manifest(self.root, execute=True, authorization=self._authorize(plan))
            self.assertEqual("pending_publication", result["disposition"])
            self.assertEqual(1, len(self._pending_ids()))
            self.assertEqual(self.initial_bytes + b"\npost-seal drift\n", self.path.read_bytes())

    def test_recording_recovery_finalizes_the_sealed_refresh_once_without_rewrite(self) -> None:
        with self.advanced_admission():
            plan = plan_release_manifest_refresh(self.root)
            with self._git_evidence(), patch(
                "release_manifest_lifecycle.ReleaseManifestLifecycle.record_release_manifest_publication",
                side_effect=RuntimeError("injected final recording failure"),
            ):
                result = refresh_release_manifest(self.root, execute=True, authorization=self._authorize(plan))
            self.assertEqual("recording_required", result["disposition"])
            pending = self._pending_ids()
            self.assertEqual(1, len(pending))
            published = self.path.read_bytes()
            with patch("release_manifest_publisher._atomic_write", side_effect=AssertionError("recovery rewrote manifest")):
                recovered = recover_release_manifest_publish(
                    self.root,
                    pending_event_id=pending[0],
                    authorization=self._recovery_authorization(pending[0]),
                )
            self.assertEqual("recovered", recovered["disposition"])
            self.assertEqual(published, self.path.read_bytes())
            self.assertEqual([], self._pending_ids())

    def test_refresh_base_never_admits_bad_digests_duplicates_symlinks_query_or_registry_drift(self) -> None:
        with self.advanced_admission():
            stale = self.path.read_bytes()
            manifest = json.loads(stale)
            manifest["canonical_manifest_sha256"] = "f" * 64
            self.path.write_bytes(json.dumps(manifest, separators=(",", ":")).encode("utf-8"))
            with self.assertRaises(SelectedRouteError):
                load_release_manifest_refresh_base(self.root)

            self.path.write_bytes(stale.replace(b'"schema_version":1', b'"schema_version":1,"schema_version":1', 1))
            with self.assertRaises(SelectedRouteError):
                load_release_manifest_refresh_base(self.root)

            manifest = json.loads(stale)
            manifest["query_source_admissions"] = list(reversed(manifest["query_source_admissions"]))
            self.path.write_bytes(self._resign(manifest))
            with self.assertRaises(SelectedRouteError):
                load_release_manifest_refresh_base(self.root)

            manifest = json.loads(stale)
            manifest["source_freshness"]["selected_source_registry_digest"] = "f" * 64
            self.path.write_bytes(self._resign(manifest))
            with self.assertRaises(SelectedRouteError):
                load_release_manifest_refresh_base(self.root)

            copy_path = self.root / "manifest-copy.json"
            copy_path.write_bytes(stale)
            self.path.unlink()
            self.path.symlink_to(copy_path)
            with self.assertRaises(SelectedRouteError):
                load_release_manifest_refresh_base(self.root)


if __name__ == "__main__":
    unittest.main()
