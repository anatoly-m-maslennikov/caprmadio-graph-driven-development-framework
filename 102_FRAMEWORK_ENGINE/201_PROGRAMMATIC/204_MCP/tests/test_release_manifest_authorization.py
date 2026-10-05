"""Focused proof for trusted-host Release manifest publication context."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
if str(MCP) not in sys.path:
    sys.path.insert(0, str(MCP))

from release_manifest_authorization import (  # noqa: E402
    PublicationAuthorizationContext,
    ReleaseManifestAuthorizationError,
    authorize_operator_publication,
    authorize_operator_publication_recovery,
    validate_candidate_payload,
    validate_publication_context,
)
from release_manifest_lifecycle import ReleaseManifestLifecycle  # noqa: E402
from release_manifest_publisher import _candidate, plan_release_manifest_publish  # noqa: E402
from release_source_admission import AUTHORITY_REF, derive_release_graph_admission  # noqa: E402
from selected_routes import selected_manifest_ref  # noqa: E402


def _paths(value: object) -> set[str]:
    if isinstance(value, dict):
        result = {value["source_path"]} if isinstance(value.get("source_path"), str) else set()
        for child in value.values():
            result |= _paths(child)
        return result
    if isinstance(value, list):
        return set().union(*(_paths(item) for item in value)) if value else set()
    return set()


class ReleaseManifestAuthorizationTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = REPOSITORY / ".caprmedio_tmp/tests/release-manifest-authorization"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="context-", dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        raw = json.loads((REPOSITORY / selected_manifest_ref(REPOSITORY)).read_text(encoding="utf-8"))
        _, admission = derive_release_graph_admission(REPOSITORY)
        manifest_ref = selected_manifest_ref(REPOSITORY)
        source_registry_ref = raw["source_freshness"]["selected_source_registry_ref"]
        operators_registry_ref = ".caprmedio_caprmedio/operators_registry.toml"
        project_settings_ref = ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        for relative in _paths(raw) | _paths(admission) | {
            AUTHORITY_REF, manifest_ref, source_registry_ref, operators_registry_ref, project_settings_ref,
        }:
            source, target = REPOSITORY / relative, self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        self.path = self.root / manifest_ref
        self.before = self.path.read_bytes()
        self.plan = plan_release_manifest_publish(self.root)

    def authorize(self, **overrides: object) -> PublicationAuthorizationContext:
        values: dict[str, object] = {
            "operator_name": "Anatoly Maslennikov",
            "journal_author": "anatoly-m",
            "llm_session": {"app": "codex", "uuid": "fixture-release-manifest"},
            "authorization_ref": "operator_authorization/release_manifest_fixture",
        }
        values.update(overrides)
        return authorize_operator_publication(self.root, self.plan, **values)  # type: ignore[arg-type]

    def assert_refused(self, context: object, *, root: Path | None = None, plan: object | None = None, **kwargs: object) -> None:
        with self.assertRaises(ReleaseManifestAuthorizationError):
            validate_publication_context(
                context, self.root if root is None else root, self.plan if plan is None else plan, **kwargs  # type: ignore[arg-type]
            )

    def test_registered_operator_context_is_fresh_and_opaque(self) -> None:
        context = self.authorize()
        self.assertEqual("Anatoly Maslennikov", context.operator_name)
        self.assertEqual("anatoly-m", context.journal_author)
        self.assertEqual({"app": "codex", "uuid": "fixture-release-manifest"}, dict(context.llm_session))
        self.assertEqual(context, validate_publication_context(context, self.root, self.plan))
        self.assertEqual(self.before, self.path.read_bytes())
        with self.assertRaises(TypeError):
            PublicationAuthorizationContext()
        with self.assertRaises(TypeError):
            context.__reduce__()

    def test_unregistered_operator_and_declared_journal_mapping_refuse(self) -> None:
        with self.assertRaises(ReleaseManifestAuthorizationError):
            self.authorize(operator_name="Unregistered Operator")
        registry = self.root / ".caprmedio_caprmedio/operators_registry.toml"
        registry.write_text(
            '[[operators]]\nname = "Anatoly Maslennikov"\nrole = "project owner"\njournal_author = "another-author"\n',
            encoding="utf-8",
        )
        with self.assertRaises(ReleaseManifestAuthorizationError):
            self.authorize()
        self.assertEqual(self.before, self.path.read_bytes())

    def test_stale_input_bytes_and_source_refuse_without_publication(self) -> None:
        context = self.authorize()
        self.path.write_bytes(self.before + b"\n")
        self.assert_refused(context)
        self.path.write_bytes(self.before)
        _, admission = derive_release_graph_admission(self.root)
        source = self.root / admission["workflow"]["source_path"]
        source.write_bytes(source.read_bytes() + b"\nstale\n")
        self.assert_refused(context)
        self.assertEqual(self.before, self.path.read_bytes())

    def test_root_plan_dict_callback_and_forged_or_altered_context_refuse(self) -> None:
        context = self.authorize()
        other = Path(tempfile.mkdtemp(prefix="other-release-root-", dir=self.root.parent))
        self.addCleanup(shutil.rmtree, other, ignore_errors=True)
        self.assert_refused(context, root=other)
        changed = dict(self.plan)
        changed["candidate_byte_count"] += 1
        self.assert_refused(context, plan=changed)
        self.assert_refused({"authorization": "remote-json"})
        self.assert_refused(lambda: True)
        forged = object.__new__(PublicationAuthorizationContext)
        self.assert_refused(forged)
        object.__setattr__(context, "_operator_name", "Altered Operator")
        self.assert_refused(context)
        self.assertEqual(self.before, self.path.read_bytes())

    def test_candidate_readback_requires_the_exact_sealed_candidate(self) -> None:
        context = self.authorize()
        _, _, payload, _ = _candidate(self.root)
        self.path.write_bytes(payload)
        self.assertEqual(context, validate_publication_context(context, self.root, self.plan, manifest_state="candidate"))
        self.path.write_bytes(payload + b"\n")
        self.assert_refused(context, manifest_state="candidate")

    def test_normal_context_seals_candidate_payload_without_disclosing_its_digest(self) -> None:
        context = self.authorize()
        _, _, payload, _ = _candidate(self.root)
        self.assertIsNone(validate_candidate_payload(context, self.root, self.plan, payload))
        with self.assertRaises(ReleaseManifestAuthorizationError):
            validate_candidate_payload(context, self.root, self.plan, payload + b"\n")
        self.assertEqual(self.before, self.path.read_bytes())

    def _seal_existing_candidate(self) -> tuple[str, bytes]:
        context = self.authorize()
        lifecycle = ReleaseManifestLifecycle(self.root, context)
        _, _, payload, _ = _candidate(self.root)
        lifecycle_plan = {key: value for key, value in self.plan.items() if key != "mode"}
        with patch("release_manifest_lifecycle.subprocess.run") as git:
            git.return_value.returncode, git.return_value.stdout = 0, "a" * 40 + "\n"
            event_id = lifecycle.prepare_release_manifest_publication(lifecycle_plan, payload)
        self.path.write_bytes(payload)
        return event_id, payload

    def test_cold_restart_reissues_finalization_only_context_from_sealed_pending_evidence(self) -> None:
        event_id, payload = self._seal_existing_candidate()
        import release_manifest_authorization as authorization
        authorization._issued.clear()
        recovery = authorize_operator_publication_recovery(
            self.root, event_id, operator_name="Anatoly Maslennikov", journal_author="anatoly-m",
            llm_session={"app": "codex", "uuid": "fixture-release-manifest"},
            authorization_ref="operator_authorization/release_manifest_recovery_fixture",
        )
        self.assertEqual(
            recovery,
            validate_publication_context(recovery, self.root, self.plan, manifest_state="candidate"),
        )
        with self.assertRaises(ReleaseManifestAuthorizationError):
            validate_publication_context(recovery, self.root, self.plan)
        with self.assertRaises(ReleaseManifestAuthorizationError):
            validate_candidate_payload(recovery, self.root, self.plan, payload)
        recovered = ReleaseManifestLifecycle(self.root, recovery).recover_release_manifest_publication(event_id)
        self.assertEqual("recovered", recovered["disposition"])
        self.assertEqual(payload, self.path.read_bytes())

    def test_recovery_refuses_changed_target_source_or_actor_binding(self) -> None:
        event_id, payload = self._seal_existing_candidate()
        self.path.write_bytes(payload + b"\n")
        with self.assertRaises(ReleaseManifestAuthorizationError):
            authorize_operator_publication_recovery(
                self.root, event_id, operator_name="Anatoly Maslennikov", journal_author="anatoly-m",
                llm_session={"app": "codex", "uuid": "fixture-release-manifest"},
                authorization_ref="operator_authorization/release_manifest_recovery_fixture",
            )
        self.path.write_bytes(payload)
        with self.assertRaises(ReleaseManifestAuthorizationError):
            authorize_operator_publication_recovery(
                self.root, event_id, operator_name="Anatoly Maslennikov", journal_author="other-author",
                llm_session={"app": "codex", "uuid": "fixture-release-manifest"},
                authorization_ref="operator_authorization/release_manifest_recovery_fixture",
            )
        _, admission = derive_release_graph_admission(self.root)
        source = self.root / admission["workflow"]["source_path"]
        source.write_bytes(source.read_bytes() + b"\nstale\n")
        with self.assertRaises(ReleaseManifestAuthorizationError):
            authorize_operator_publication_recovery(
                self.root, event_id, operator_name="Anatoly Maslennikov", journal_author="anatoly-m",
                llm_session={"app": "codex", "uuid": "fixture-release-manifest"},
                authorization_ref="operator_authorization/release_manifest_recovery_fixture",
            )

    def test_plan_or_context_from_another_source_frontier_refuses(self) -> None:
        context = self.authorize()
        authority = self.root / AUTHORITY_REF
        authority.write_bytes(authority.read_bytes() + b"\nsource changed\n")
        self.assert_refused(context)
        self.assertEqual(self.before, self.path.read_bytes())
        self.assertEqual(
            hashlib.sha256((REPOSITORY / selected_manifest_ref(REPOSITORY)).read_bytes()).hexdigest(),
            hashlib.sha256(self.before).hexdigest(),
        )


if __name__ == "__main__":
    unittest.main()
