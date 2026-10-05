"""Focused retained-fixture proof for the Release publication lifecycle."""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
import shutil
import subprocess
import sys
import unittest
from contextlib import contextmanager
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
APP_TESTS = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
for location in (MCP, MCP / "tests", APP_TESTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import test_release_source_admission as source_goldens  # noqa: E402
from release_manifest_authorization import authorize_operator_publication  # noqa: E402
from release_manifest_lifecycle import ReleaseManifestLifecycle, ReleaseManifestLifecycleError  # noqa: E402
from release_manifest_publisher import _candidate, plan_release_manifest_publish  # noqa: E402
from selected_routes import selected_manifest_ref  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402
import work_journal  # noqa: E402


class ReleaseManifestLifecycleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        source_goldens.ReleaseSourceAdmissionTest.setUpClass()

    def setUp(self) -> None:
        self.fixture = source_goldens.ReleaseSourceAdmissionTest()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        project = GoldenProject(REPOSITORY, self.root, GoldenCase("W04", "change_atom_status"))
        project._copy_reviewed_manifest()
        for relative in (
            Path(".caprmedio_caprmedio/operators_registry.toml"),
            Path(".caprmedio_caprmedio/caprmedio_project_settings.toml"),
        ):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / relative, target)
        self.path = self.root / selected_manifest_ref(self.root)
        self.before = self.path.read_bytes()
        self.plan = plan_release_manifest_publish(self.root)
        self.assertEqual("plan", self.plan.pop("mode"))
        _, _, self.payload, _ = _candidate(self.root)
        context = authorize_operator_publication(
            self.root, self.plan, operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov", llm_session={"app": "test", "uuid": "release-lifecycle"},
            authorization_ref="authorization/release-manifest.md",
        )
        self.lifecycle = ReleaseManifestLifecycle(self.root, context)

    def _pending(self, event_id: str) -> tuple[dict, dict]:
        pending, event, _, _ = work_journal._read_pending_event(self.root, event_id)
        return pending, event

    def test_authorization_and_prepare_seal_pre_effect_exact_event(self) -> None:
        self.assertTrue(self.lifecycle.authorize_release_manifest_publication(self.plan, self.lifecycle.context))
        with patch("release_manifest_lifecycle.subprocess.run") as git:
            git.return_value.returncode, git.return_value.stdout = 0, "a" * 40 + "\n"
            event_id = self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        self.assertEqual(self.before, self.path.read_bytes())
        pending, event = self._pending(event_id)
        self.assertEqual(self.plan["manifest_ref"], event["result"]["path"])
        self.assertEqual(2, event["result"]["version"])
        self.assertEqual("release-manifest-publication:", pending["diagnostic"][:29])
        journal_root = self.root / ".caprmedio_caprmedio/_journal"
        records = [json.loads(line) for path in journal_root.glob("*.ndjson") for line in path.read_text().splitlines()]
        self.assertEqual(["recovered"], [record["event"] for record in records])

    def test_exact_candidate_finalizes_only_sealed_event(self) -> None:
        with patch("release_manifest_lifecycle.subprocess.run") as git:
            git.return_value.returncode, git.return_value.stdout = 0, "b" * 40 + "\n"
            event_id = self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        self.path.write_bytes(self.payload)
        receipt = self.lifecycle.record_release_manifest_publication({"mode": "execute", "published": True, **self.plan})
        self.assertEqual("journal:" + event_id, receipt["recording_ref"])
        with self.assertRaises(work_journal.WorkJournalError):
            work_journal._read_pending_event(self.root, event_id)
        journal_root = self.root / ".caprmedio_caprmedio/_journal"
        records = [json.loads(line) for path in journal_root.glob("*.ndjson") for line in path.read_text().splitlines()]
        self.assertEqual(["recovered", "completed"], [record["event"] for record in records])
        self.assertEqual(records[0]["event_id"], records[1]["previous_result_event"])
        self.assertEqual([1, 2], [record["result"]["version"] for record in records])

    def test_ambiguous_candidate_does_not_replay_or_finalize(self) -> None:
        with patch("release_manifest_lifecycle.subprocess.run") as git:
            git.return_value.returncode, git.return_value.stdout = 0, "c" * 40 + "\n"
            event_id = self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        # Valid JSON with a different byte representation is still ambiguous:
        # the sealed pending event binds the exact carrier bytes.
        self.path.write_bytes(self.payload + b"\n")
        before = self.path.read_bytes()
        with self.assertRaisesRegex(ReleaseManifestLifecycleError, "ambiguous"):
            self.lifecycle.recover_release_manifest_publication(event_id)
        self.assertEqual(before, self.path.read_bytes())
        self._pending(event_id)

    def test_ambiguous_bytes_are_classified_before_candidate_context_validation(self) -> None:
        with patch("release_manifest_lifecycle.subprocess.run") as git:
            git.return_value.returncode, git.return_value.stdout = 0, "e" * 40 + "\n"
            event_id = self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        self.path.write_bytes(self.payload + b"\n")
        with patch(
            "release_manifest_lifecycle.validate_publication_context",
            side_effect=AssertionError("candidate authorization must not preempt byte classification"),
        ):
            with self.assertRaisesRegex(ReleaseManifestLifecycleError, "ambiguous"):
                self.lifecycle.recover_release_manifest_publication(event_id)
        self._pending(event_id)

    def test_append_failure_retains_exact_pending_event_for_recovery(self) -> None:
        with patch("release_manifest_lifecycle.subprocess.run") as git:
            git.return_value.returncode, git.return_value.stdout = 0, "d" * 40 + "\n"
            event_id = self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        self.path.write_bytes(self.payload)
        with patch("release_manifest_lifecycle.work_journal.recover_pending_event", side_effect=work_journal.WorkJournalError("append-failed", "fixture")):
            with self.assertRaisesRegex(ReleaseManifestLifecycleError, "cannot finalize"):
                self.lifecycle.record_release_manifest_publication({"mode": "execute", "published": True, **self.plan})
        self._pending(event_id)
        recovered = self.lifecycle.recover_release_manifest_publication(event_id)
        self.assertEqual("recovered", recovered["disposition"])
        with self.assertRaises(work_journal.WorkJournalError):
            work_journal._read_pending_event(self.root, event_id)

    def test_non_context_authority_is_refused(self) -> None:
        self.assertFalse(self.lifecycle.authorize_release_manifest_publication(self.plan, True))
        self.assertFalse(self.lifecycle.authorize_release_manifest_publication({"bad": "plan"}, self.lifecycle.context))

    def test_lifecycle_owned_carrier_lock_skips_nested_prepare_lock(self) -> None:
        calls: list[str] = []

        @contextmanager
        def observed_lock(_root: Path, lock_id: str):
            calls.append(lock_id)
            yield

        with patch("release_manifest_lifecycle.subprocess.run") as git, patch(
            "release_manifest_lifecycle.work_journal._event_lock", side_effect=observed_lock,
        ):
            git.return_value.returncode, git.return_value.stdout = 0, "9" * 40 + "\n"
            with self.lifecycle.release_manifest_publication_lock(self.plan):
                self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        self.assertEqual(1, sum(lock.startswith("release-manifest-carrier:") for lock in calls))

    def test_prepare_exposes_no_lock_bypass_flag(self) -> None:
        with self.assertRaises(TypeError):
            self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload, publication_lock_held=True)

    def test_lifecycle_owned_carrier_lock_is_not_reentrant(self) -> None:
        with self.lifecycle.release_manifest_publication_lock(self.plan):
            with self.assertRaisesRegex(ReleaseManifestLifecycleError, "already held"):
                with self.lifecycle.release_manifest_publication_lock(self.plan):
                    pass

    def test_lifecycle_owned_carrier_lock_preserves_the_publisher_failure(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "publisher body failed"):
            with self.lifecycle.release_manifest_publication_lock(self.plan):
                raise RuntimeError("publisher body failed")

    def test_unrelated_legacy_journal_record_does_not_block_target_history(self) -> None:
        journal = self.root / ".caprmedio_caprmedio/_journal/unrelated-legacy.ndjson"
        journal.parent.mkdir(parents=True, exist_ok=True)
        journal.write_text(json.dumps({
            "schema_version": 1,
            "event_id": "legacy-unrelated",
            "event": "started",
            "kind": "projection_rebuild",
            "prior_state": None,
            "provenance": None,
        }) + "\n", encoding="utf-8")
        with patch("release_manifest_lifecycle.subprocess.run") as git:
            git.return_value.returncode, git.return_value.stdout = 0, "8" * 40 + "\n"
            event_id = self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        self._pending(event_id)

    def test_malformed_relevant_generic_carrier_history_remains_a_refusal(self) -> None:
        journal = self.root / ".caprmedio_caprmedio/_journal/relevant-malformed.ndjson"
        journal.parent.mkdir(parents=True, exist_ok=True)
        journal.write_text(json.dumps({
            "schema_version": 3,
            "kind": "governed_project_state",
            "result": {"path": self.plan["manifest_ref"]},
        }) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ReleaseManifestLifecycleError, "history is invalid"):
            self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)

    def test_unsupported_schema_claiming_target_history_is_refused(self) -> None:
        journal = self.root / ".caprmedio_caprmedio/_journal/target-unsupported-schema.ndjson"
        journal.parent.mkdir(parents=True, exist_ok=True)
        journal.write_text(json.dumps({
            "schema_version": 1,
            "kind": "governed_project_state",
            "result": {"path": self.plan["manifest_ref"]},
        }) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ReleaseManifestLifecycleError, "unsupported target carrier evidence"):
            self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)

    def test_unsupported_kind_claiming_target_history_is_refused(self) -> None:
        journal = self.root / ".caprmedio_caprmedio/_journal/target-unsupported-kind.ndjson"
        journal.parent.mkdir(parents=True, exist_ok=True)
        journal.write_text(json.dumps({
            "schema_version": 3,
            "kind": "workflow_execution",
            "result": {"path": self.plan["manifest_ref"]},
        }) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ReleaseManifestLifecycleError, "unsupported target carrier evidence"):
            self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)

    def test_repeated_prepare_reuses_the_same_closed_intent(self) -> None:
        first_time = dt.datetime(2026, 10, 5, 12, 0, tzinfo=dt.timezone.utc)
        second_time = dt.datetime(2026, 10, 5, 12, 1, tzinfo=dt.timezone.utc)
        with patch("release_manifest_lifecycle.subprocess.run") as git, patch(
            "release_manifest_lifecycle._now", side_effect=[first_time, second_time],
        ):
            git.side_effect = [
                subprocess.CompletedProcess([], 0, "f" * 40 + "\n", ""),
                subprocess.CompletedProcess([], 0, self.before, b""),
            ]
            first = self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        with patch("release_manifest_lifecycle._now", side_effect=AssertionError("retry must reuse immutable intent")):
            second = self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        self.assertEqual(first, second)
        pending, event = self._pending(first)
        self.assertEqual(second_time.isoformat(), event["occurred_at"])
        self.assertEqual(2, event["result"]["version"])
        self.assertTrue(pending["diagnostic"].startswith("release-manifest-publication:"))

    def test_recovered_prior_uses_working_tree_evidence_when_head_bytes_differ(self) -> None:
        with patch("release_manifest_lifecycle.subprocess.run") as git:
            git.side_effect = [
                subprocess.CompletedProcess([], 0, "1" * 40 + "\n", ""),
                subprocess.CompletedProcess([], 0, b"committed-but-not-observed", b""),
            ]
            self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        journal_root = self.root / ".caprmedio_caprmedio/_journal"
        recovered = [json.loads(line) for path in journal_root.glob("*.ndjson") for line in path.read_text().splitlines()][0]
        evidence = recovered["recovery_evidence"]
        self.assertNotIn("commit", evidence["git"])
        self.assertEqual("working_tree_only", evidence["git"]["provenance"])
        self.assertEqual(self.plan["manifest_ref"], evidence["git"]["path"])
        self.assertEqual(work_journal._sha256(self.before), evidence["git"]["sha256"])


if __name__ == "__main__":
    unittest.main()
