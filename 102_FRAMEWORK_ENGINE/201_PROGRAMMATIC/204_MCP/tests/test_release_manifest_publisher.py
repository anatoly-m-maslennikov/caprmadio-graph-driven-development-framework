"""Focused retained-fixture proof for the bounded Release manifest publisher."""
from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
import shutil
import sys
import types
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
APP_TESTS = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
for location in (MCP, MCP / "tests", APP_TESTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import test_release_source_admission as source_goldens  # noqa: E402
from release_manifest_authorization import (  # noqa: E402
    PublicationAuthorizationContext, authorize_operator_publication, authorize_operator_publication_recovery,
)
from release_manifest_lifecycle import ReleaseManifestLifecycle  # noqa: E402
from release_manifest_publisher import (  # noqa: E402
    ReleaseManifestPublishError, plan_release_manifest_publish, publish_release_manifest,
    recover_release_manifest_publish,
)
from release_source_admission import derive_release_graph_admission  # noqa: E402
from selected_routes import (  # noqa: E402
    SELECTED_ROUTE_NAMES, SelectedRouteError, load_selected_manifest, register_selected_routes, selected_manifest_ref,
)
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402
import work_journal  # noqa: E402


class _Server:
    def __init__(self) -> None:
        self.names: list[str] = []

    def tool(self, *, name: str, structured_output: bool, annotations: object):
        def decorate(function):
            self.names.append(name)
            return function
        return decorate


class _Annotations:
    def __init__(self, **values: object) -> None:
        pass


class ReleaseManifestPublisherTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        source_goldens.ReleaseSourceAdmissionTest.setUpClass()

    def setUp(self) -> None:
        self.root, self.path, self.before, self.original = self._fresh_project()

    def _fresh_project(self) -> tuple[Path, Path, bytes, dict]:
        self.fixture = source_goldens.ReleaseSourceAdmissionTest()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        root = self.fixture.root
        GoldenProject(REPOSITORY, root, GoldenCase("W04", "change_atom_status"))._copy_reviewed_manifest()
        for relative in (
            Path(".caprmedio_caprmedio/operators_registry.toml"),
            Path(".caprmedio_caprmedio/caprmedio_project_settings.toml"),
        ):
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / relative, target)
        path = root / selected_manifest_ref(root)
        return root, path, path.read_bytes(), load_selected_manifest(root)

    def plan(self) -> dict:
        return plan_release_manifest_publish(self.root)

    def authorization(self) -> PublicationAuthorizationContext:
        return authorize_operator_publication(
            self.root, self.plan(), operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "release-manifest-publisher"},
            authorization_ref="authorization/release-manifest-publisher.md",
        )

    def recovery_authorization(self, pending_event_id: str) -> PublicationAuthorizationContext:
        return authorize_operator_publication_recovery(
            self.root, pending_event_id, operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "release-manifest-publisher"},
            authorization_ref="authorization/release-manifest-publisher-recovery.md",
        )

    def git_evidence(self, digest: str = "a"):
        return patch(
            "release_manifest_lifecycle.subprocess.run",
            return_value=types.SimpleNamespace(returncode=0, stdout=digest * 40 + "\n"),
        )

    def pending_ids(self, root: Path | None = None) -> list[str]:
        pending = (self.root if root is None else root) / ".caprmedio_runtime/state/work_journal/pending"
        return sorted(path.stem for path in pending.glob("release-manifest:*.json")) if pending.exists() else []

    def test_plan_is_byte_preserving_and_exactly_additive(self) -> None:
        plan = self.plan()
        self.assertEqual("plan", plan["mode"])
        self.assertEqual(self.before, self.path.read_bytes())
        self.assertEqual(15, len(plan["current_route_names"]))
        self.assertEqual([*plan["current_route_names"], "release_version"], plan["candidate_route_names"])

    def test_execute_requires_opaque_trusted_authorization_and_preserves_existing_values(self) -> None:
        with self.assertRaises(ReleaseManifestPublishError):
            publish_release_manifest(self.root, execute=True)
        with self.assertRaises(ReleaseManifestPublishError):
            publish_release_manifest(self.root, execute=True, authorization={"authorized": True})
        self.assertEqual(self.before, self.path.read_bytes())
        with self.git_evidence():
            result = publish_release_manifest(self.root, execute=True, authorization=self.authorization())
        loaded = load_selected_manifest(self.root)
        self.assertEqual("published", result["disposition"])
        self.assertEqual(self.original["routes"], loaded["routes"][:-1])
        self.assertEqual(self.original["query_source_admissions"], loaded["query_source_admissions"])
        self.assertEqual(16, len(loaded["routes"]))
        self.assertTrue(result["recording_ref"].startswith("journal:release-manifest:"))

    def test_changed_input_and_stale_source_refuse_before_write(self) -> None:
        context = self.authorization()
        self.path.write_bytes(self.before + b"\n")
        with self.assertRaises(ReleaseManifestPublishError):
            publish_release_manifest(self.root, execute=True, authorization=context)
        self.assertEqual(self.before + b"\n", self.path.read_bytes())
        self.path.write_bytes(self.before)
        _, admission = derive_release_graph_admission(self.root)
        source = self.root / admission["workflow"]["source_path"]
        source.write_bytes(source.read_bytes() + b"\nstale\n")
        with self.assertRaises(ReleaseManifestPublishError):
            self.plan()
        self.assertEqual(self.before, self.path.read_bytes())

    def test_source_drift_after_real_prepare_keeps_sealed_pending_intent_and_skips_write(self) -> None:
        context = self.authorization()
        _, admission = derive_release_graph_admission(self.root)
        source = self.root / admission["workflow"]["source_path"]
        original_prepare = ReleaseManifestLifecycle.prepare_release_manifest_publication

        def seal_then_drift(
            lifecycle: ReleaseManifestLifecycle, plan: dict, payload: bytes, **kwargs: object,
        ) -> str:
            event_id = original_prepare(lifecycle, plan, payload, **kwargs)
            source.write_bytes(source.read_bytes() + b"\nsource drift after sealed intent\n")
            return event_id

        with self.git_evidence(), patch.object(
            ReleaseManifestLifecycle, "prepare_release_manifest_publication", new=seal_then_drift,
        ):
            result = publish_release_manifest(self.root, execute=True, authorization=context)
        self.assertEqual("pending_publication", result["disposition"])
        self.assertTrue(result["pending_event_id"])
        self.assertEqual(self.before, self.path.read_bytes())
        self.assertEqual(1, len(self.pending_ids()))

    def test_manifest_drift_after_real_prepare_keeps_sealed_pending_intent_and_skips_write(self) -> None:
        root, path, before, _ = self._fresh_project()
        plan = plan_release_manifest_publish(root)
        context = authorize_operator_publication(
            root, plan, operator_name="Anatoly Maslennikov", journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "release-manifest-manifest-drift"},
            authorization_ref="authorization/release-manifest-manifest-drift.md",
        )
        original_prepare = ReleaseManifestLifecycle.prepare_release_manifest_publication

        def seal_then_drift(
            lifecycle: ReleaseManifestLifecycle, sealed: dict, payload: bytes, **kwargs: object,
        ) -> str:
            event_id = original_prepare(lifecycle, sealed, payload, **kwargs)
            path.write_bytes(path.read_bytes() + b"\nmanifest drift after sealed intent\n")
            return event_id

        with self.git_evidence(), patch.object(
            ReleaseManifestLifecycle, "prepare_release_manifest_publication", new=seal_then_drift,
        ):
            result = publish_release_manifest(root, execute=True, authorization=context)
        self.assertEqual("pending_publication", result["disposition"])
        self.assertTrue(result["pending_event_id"])
        self.assertEqual(before + b"\nmanifest drift after sealed intent\n", path.read_bytes())
        self.assertEqual(1, len(self.pending_ids(root)))

    def test_append_failure_leaves_sealed_pending_evidence_and_recovery_never_replays_write(self) -> None:
        context = self.authorization()
        original_append = work_journal.append_sealed_events
        calls = 0

        def fail_final_append(*args: object, **kwargs: object):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise work_journal.WorkJournalError("injected", "final append failure")
            return original_append(*args, **kwargs)

        with self.git_evidence(), patch("release_manifest_lifecycle.work_journal.append_sealed_events", side_effect=fail_final_append):
            result = publish_release_manifest(self.root, execute=True, authorization=context)
        self.assertEqual("recording_required", result["disposition"], result)
        self.assertEqual(16, len(load_selected_manifest(self.root)["routes"]))
        pending = self.pending_ids()
        self.assertEqual(1, len(pending))
        before_recovery = self.path.read_bytes()
        recovered = recover_release_manifest_publish(
            self.root, pending_event_id=pending[0], authorization=self.recovery_authorization(pending[0]),
        )
        self.assertEqual("recovered", recovered["disposition"])
        self.assertEqual(before_recovery, self.path.read_bytes())
        self.assertEqual([], self.pending_ids())

    def test_atomic_prewrite_failure_and_postwrite_readback_failure_are_truthful(self) -> None:
        context = self.authorization()
        with self.git_evidence(), patch("release_manifest_publisher._atomic_write", side_effect=ReleaseManifestPublishError("injected")):
            result = publish_release_manifest(self.root, execute=True, authorization=context)
        self.assertEqual("pending_publication", result["disposition"])
        self.assertEqual(self.before, self.path.read_bytes())
        self.assertEqual(1, len(self.pending_ids()))
        root, path, before, original = self._fresh_project()
        plan = plan_release_manifest_publish(root)
        context = authorize_operator_publication(
            root, plan, operator_name="Anatoly Maslennikov", journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "release-manifest-readback"},
            authorization_ref="authorization/release-manifest-readback.md",
        )
        def reject_candidate_readback(project_root: Path) -> dict:
            if path.read_bytes() != before:
                raise SelectedRouteError("readback injected")
            return load_selected_manifest(project_root)

        with self.git_evidence(), patch("release_manifest_publisher.load_selected_manifest", side_effect=reject_candidate_readback):
            result = publish_release_manifest(root, execute=True, authorization=context)
        self.assertEqual("readback_required", result["disposition"])
        self.assertTrue(result["published"])

    def test_route_name_readback_mismatch_keeps_the_exact_sealed_pending_id(self) -> None:
        context = self.authorization()
        original_load = load_selected_manifest

        def mismatched_route_readback(project_root: Path) -> dict:
            loaded = original_load(project_root)
            if self.path.read_bytes() != self.before:
                loaded = dict(loaded)
                loaded["routes"] = list(loaded["routes"][:-1])
            return loaded

        with self.git_evidence(), patch(
            "release_manifest_publisher.load_selected_manifest", side_effect=mismatched_route_readback,
        ):
            result = publish_release_manifest(self.root, execute=True, authorization=context)
        pending = self.pending_ids()
        self.assertEqual("readback_required", result["disposition"])
        self.assertTrue(result["published"])
        self.assertEqual(1, len(pending))
        self.assertEqual(pending[0], result["pending_event_id"])

    def test_final_carrier_check_and_atomic_replace_share_one_carrier_lock(self) -> None:
        context = self.authorization()
        original_atomic_write = __import__("release_manifest_publisher")._atomic_write
        original_lock = ReleaseManifestLifecycle.release_manifest_publication_lock
        held = 0

        @contextmanager
        def observed_carrier_lock(lifecycle: ReleaseManifestLifecycle, plan: dict):
            nonlocal held
            with original_lock(lifecycle, plan):
                held += 1
                try:
                    yield
                finally:
                    held -= 1

        def assert_locked_atomic_write(path: Path, payload: bytes) -> None:
            self.assertGreater(held, 0, "carrier lock must cover final check through replace")
            original_atomic_write(path, payload)

        with self.git_evidence(), patch.object(
            ReleaseManifestLifecycle, "release_manifest_publication_lock", new=observed_carrier_lock,
        ), patch(
            "release_manifest_publisher._atomic_write", new=assert_locked_atomic_write,
        ):
            result = publish_release_manifest(self.root, execute=True, authorization=context)
        self.assertEqual("published", result["disposition"])

    def test_real_sixteen_registration_gate_after_journal_backed_publication(self) -> None:
        with self.git_evidence("b"):
            publish_release_manifest(self.root, execute=True, authorization=self.authorization())
        server, mcp, typed = _Server(), types.ModuleType("mcp"), types.ModuleType("mcp.types")
        typed.ToolAnnotations = _Annotations
        mcp.types = typed
        with patch.dict(sys.modules, {"mcp": mcp, "mcp.types": typed}):
            register_selected_routes(server, self.root)
        self.assertEqual([*SELECTED_ROUTE_NAMES, "release_version"], server.names[:16])


if __name__ == "__main__":
    unittest.main()
