"""Regression proof for Git-backed Release binding state reconciliation."""
from __future__ import annotations

from contextlib import contextmanager
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import types
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
TOOLS = MCP.parent / "201_TOOLS"
APP_TESTS = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
for location in (MCP, MCP / "tests", TOOLS, APP_TESTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import release_source_admission as admission_module  # noqa: E402
import release_manifest_reconciliation as reconciliation_module  # noqa: E402
import test_release_source_admission as source_goldens  # noqa: E402
import work_journal  # noqa: E402
from release_manifest_authorization import (  # noqa: E402
    authorize_operator_publication,
)
from release_manifest_publisher import (  # noqa: E402
    plan_release_manifest_publish,
    plan_release_manifest_refresh,
    publish_release_manifest,
    refresh_release_manifest,
)
from release_manifest_reconciliation import (  # noqa: E402
    authorize_operator_reconciliation,
    authorize_operator_reconciliation_recovery,
    plan_release_manifest_reconciliation,
    reconcile_release_manifest_history,
    recover_release_manifest_reconciliation,
)
from release_source_admission import derive_release_graph_admission  # noqa: E402
from selected_routes import canonical_digest, selected_manifest_ref  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402


class ReleaseManifestReconciliationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        source_goldens.ReleaseSourceAdmissionTest.setUpClass()

    def setUp(self) -> None:
        self.fixture = source_goldens.ReleaseSourceAdmissionTest()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        GoldenProject(REPOSITORY, self.root, GoldenCase("W04", "change_atom_status"))._copy_reviewed_manifest()
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
            self.root, initial_plan, operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "reconciliation-initial"},
            authorization_ref="authorization/reconciliation-initial.md",
        )
        with patch(
            "release_manifest_lifecycle.subprocess.run",
            return_value=types.SimpleNamespace(returncode=0, stdout="0" * 40 + "\n"),
        ):
            result = publish_release_manifest(self.root, execute=True, authorization=initial_context)
        self.assertEqual("published", result["disposition"])
        self.initial_context = initial_context
        self.initial_bytes = self.path.read_bytes()
        self.initial_records = self.records()
        self.assertEqual(["recovered", "completed"], [record["event"] for record in self.initial_records])
        self.assertEqual(2, self.initial_records[-1]["result"]["version"])

    def records(self) -> list[dict]:
        journal = self.root / ".caprmedio_caprmedio/_journal"
        return [
            json.loads(line)
            for path in sorted(journal.glob("*.ndjson"))
            for line in path.read_text(encoding="utf-8").splitlines()
        ]

    def _resign(self, manifest: dict) -> bytes:
        manifest["source_freshness"]["selected_binding_digest"] = canonical_digest(manifest["routes"])
        unsigned = {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
        manifest["canonical_manifest_sha256"] = canonical_digest(unsigned)
        return json.dumps(manifest, separators=(",", ":")).encode("utf-8")

    def _git(self, *arguments: str) -> str:
        completed = subprocess.run(
            ["git", "-C", str(self.root), *arguments], check=True, capture_output=True, text=True,
        )
        return completed.stdout.strip()

    def _commit_manifest(self, payload: bytes) -> None:
        self.path.write_bytes(payload)
        self._git("init", "-q")
        self._git("config", "user.name", "Reconciliation Test")
        self._git("config", "user.email", "reconciliation@example.invalid")
        self._git("add", self.path.relative_to(self.root).as_posix())
        self._git("commit", "--allow-empty", "-qm", "reconcile exact selected manifest state")

    @contextmanager
    def stale_git_backed_gap(self):
        """Advance accepted source pins, then commit a distinct stale sixteen-route state."""
        initial_admission = json.loads(self.initial_bytes)["release_source_admissions"][0]
        private_paths = {row["source_path"] for row in self.fixture.private_carriers}
        pin = next(pin for pin in initial_admission["rmed_frontier"] if pin["source_path"] not in private_paths)
        source = self.root / pin["source_path"]
        authority = self.root / source_goldens.AUTHORITY_REF
        source_before, authority_before = source.read_bytes(), authority.read_bytes()
        changed_source = re.sub(
            rf"(?m)^version:\s*{pin['version']}\s*$", f"version: {pin['version'] + 1}",
            source_before.decode("utf-8"), count=1,
        ).encode("utf-8")
        changed_digest = hashlib.sha256(changed_source).hexdigest()
        old_row = f"| {pin['atom_id']} | {pin['version']} | `{pin['source_path']}` | `{pin['digest']}` |"
        new_row = f"| {pin['atom_id']} | {pin['version'] + 1} | `{pin['source_path']}` | `{changed_digest}` |"
        changed_authority = authority_before.decode("utf-8").replace(old_row, new_row, 1).encode("utf-8")
        self.assertNotEqual(authority_before, changed_authority)
        source.write_bytes(changed_source)
        authority.write_bytes(changed_authority)
        trusted_authority = {
            **admission_module.AUTHORITY_PIN,
            "digest": hashlib.sha256(changed_authority).hexdigest(),
        }
        try:
            with patch.object(admission_module, "AUTHORITY_PIN", trusted_authority):
                _, current_admission = derive_release_graph_admission(self.root)
                stale = json.loads(self.initial_bytes)
                stale_pin = next(
                    row for row in stale["release_source_admissions"][0]["rmed_frontier"]
                    if row["atom_id"] == pin["atom_id"] and row["source_path"] == pin["source_path"]
                )
                stale_pin["version"] = current_admission["rmed_frontier"][
                    next(index for index, row in enumerate(current_admission["rmed_frontier"])
                         if row["atom_id"] == pin["atom_id"] and row["source_path"] == pin["source_path"])
                ]["version"] - 1
                stale_pin["digest"] = "f" * 64
                gap_bytes = self._resign(stale)
                self.assertNotEqual(self.initial_bytes, gap_bytes)
                self._commit_manifest(gap_bytes)
                yield gap_bytes
        finally:
            source.write_bytes(source_before)
            authority.write_bytes(authority_before)

    def _authorize(self, plan: dict) -> object:
        return authorize_operator_reconciliation(
            self.root, plan, operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "reconciliation-observation"},
            authorization_ref="authorization/reconciliation-observation.md",
        )

    def _pending_ids(self) -> list[str]:
        pending = self.root / ".caprmedio_runtime/state/work_journal/pending"
        return sorted(path.stem for path in pending.glob("release-manifest-reconciliation:*.json")) if pending.exists() else []

    def _append_context(self, event: dict) -> dict:
        occurred = dt.datetime.fromisoformat(event["occurred_at"])
        return work_journal.seal_append_context(
            self.root, event, author=event["author"],
            local_date=occurred.date().isoformat(),
            timezone=occurred.tzname() or occurred.strftime("%z"),
        )

    def _append_valid_event(self, event: dict) -> dict:
        sealed = work_journal.with_event_digest(event)
        context = self._append_context(sealed)
        work_journal.append_sealed_events(
            self.root, [sealed], author=context["author"],
            local_date=context["local_date"], timezone=context["timezone"],
            append_context=context,
        )
        return sealed

    def _unrelated_event(self) -> dict:
        event = json.loads(json.dumps(self.initial_records[0]))
        event["event_id"] = "reconciliation-unrelated-state"
        event["result"] = {
            **event["result"], "filename": "unrelated-state.json",
            "path": "state/unrelated-state.json",
        }
        return event

    def test_plan_and_execute_observe_exact_git_backed_gap_without_rewrite(self) -> None:
        with self.stale_git_backed_gap() as gap_bytes:
            history_before = self.records()
            plan = plan_release_manifest_reconciliation(self.root)
            self.assertEqual("plan", plan["mode"])
            self.assertEqual(gap_bytes, self.path.read_bytes())
            self.assertEqual(history_before, self.records())
            self.assertEqual([], self._pending_ids())

            authorization = self._authorize(plan)
            result = reconcile_release_manifest_history(
                self.root, execute=True, authorization=authorization,
            )
            self.assertEqual("observed", result["disposition"])
            self.assertEqual("execute", result["mode"])
            self.assertEqual(gap_bytes, self.path.read_bytes())
            records = self.records()
            self.assertEqual(history_before, records[:-1])
            observed = records[-1]
            self.assertEqual("recovered", observed["event"])
            self.assertEqual("governed_project_state", observed["kind"])
            self.assertEqual(3, observed["result"]["version"])
            self.assertEqual(hashlib.sha256(gap_bytes).hexdigest(), observed["result"]["sha256"])
            self.assertNotIn("previous_result_event", observed)
            self.assertNotIn("action_type", observed)
            self.assertNotIn("sources", observed)
            evidence = observed["recovery_evidence"]
            self.assertEqual({"git", "carrier"}, set(evidence))
            self.assertEqual(
                {"identity", "kind", "filename", "version", "sha256", "predecessor_event_id", "predecessor_version", "predecessor_sha256"},
                set(evidence["carrier"]),
            )
            self.assertEqual(history_before[-1]["event_id"], evidence["carrier"]["predecessor_event_id"])
            self.assertEqual(2, evidence["carrier"]["predecessor_version"])
            self.assertEqual(history_before[-1]["result"]["sha256"], evidence["carrier"]["predecessor_sha256"])
            self.assertEqual([], self._pending_ids())

            journal_after_first = self.records()
            original = journal_after_first[-1]
            repeated = reconcile_release_manifest_history(
                self.root, execute=True, authorization=authorization,
            )
            self.assertEqual("already_recorded", repeated["disposition"])
            self.assertEqual("execute", repeated["mode"])
            self.assertEqual(journal_after_first, self.records())
            self.assertEqual(original["event_id"], repeated["event_id"])
            self.assertEqual(original["occurred_at"], self.records()[-1]["occurred_at"])

    def test_unrelated_valid_journal_event_does_not_block_observation(self) -> None:
        with self.stale_git_backed_gap() as gap_bytes:
            unrelated = self._append_valid_event(self._unrelated_event())
            plan = plan_release_manifest_reconciliation(self.root)
            result = reconcile_release_manifest_history(
                self.root, execute=True, authorization=self._authorize(plan),
            )
            self.assertEqual("observed", result["disposition"])
            self.assertEqual("execute", result["mode"])
            self.assertEqual(gap_bytes, self.path.read_bytes())
            self.assertIn(unrelated["event_id"], [event["event_id"] for event in self.records()])
            self.assertEqual(3, self.records()[-1]["result"]["version"])

    def test_competing_target_pending_refuses_without_observation(self) -> None:
        with self.stale_git_backed_gap() as gap_bytes:
            plan = plan_release_manifest_reconciliation(self.root)
            authorization = self._authorize(plan)
            event = self.initial_records[-1]
            work_journal.store_pending_event(
                self.root, event, self._append_context(event), result_ref=plan["manifest_ref"],
                effect_refs=[], diagnostic="competing selected Manifest publication",
            )
            before = self.records()
            result = reconcile_release_manifest_history(
                self.root, execute=True, authorization=authorization,
            )
            self.assertEqual("blocked", result["disposition"])
            self.assertEqual("execute", result["mode"])
            self.assertEqual(gap_bytes, self.path.read_bytes())
            self.assertEqual(before, self.records())

    def test_locked_recheck_refuses_git_bytes_source_and_history_drift(self) -> None:
        def source_drift() -> None:
            pin = next(
                pin for pin in json.loads(self.initial_bytes)["release_source_admissions"][0]["rmed_frontier"]
                if pin["source_path"] not in {row["source_path"] for row in self.fixture.private_carriers}
            )
            source = self.root / pin["source_path"]
            source_text = source.read_text(encoding="utf-8")
            version = int(re.search(r"(?m)^version:\s*(\d+)\s*$", source_text).group(1))
            changed_source = re.sub(
                rf"(?m)^version:\s*{version}\s*$", f"version: {version + 1}", source_text, count=1,
            ).encode("utf-8")
            changed_digest = hashlib.sha256(changed_source).hexdigest()
            authority = self.root / source_goldens.AUTHORITY_REF
            authority_text = authority.read_text(encoding="utf-8")
            authority_pattern = (
                rf"(?m)^\| {re.escape(pin['atom_id'])} \| \d+ \| "
                rf"`{re.escape(pin['source_path'])}` \| `[0-9a-f]{{64}}` \|$"
            )
            matched = re.search(authority_pattern, authority_text)
            self.assertIsNotNone(matched)
            authority.write_text(
                authority_text[:matched.start()] +
                f"| {pin['atom_id']} | {version + 1} | `{pin['source_path']}` | `{changed_digest}` |" +
                authority_text[matched.end():], encoding="utf-8",
            )
            source.write_bytes(changed_source)
            admission_module.AUTHORITY_PIN = {
                **admission_module.AUTHORITY_PIN,
                "digest": hashlib.sha256(authority.read_bytes()).hexdigest(),
            }

        def history_drift(gap_bytes: bytes) -> None:
            event = json.loads(json.dumps(self.initial_records[-1]))
            event["event_id"] = "reconciliation-target-history-drift"
            event["result"] = {
                **event["result"], "version": 3,
                "sha256": hashlib.sha256(gap_bytes).hexdigest(),
            }
            event["previous_result_event"] = self.initial_records[-1]["event_id"]
            self._append_valid_event(event)

        variants = {
            "git": lambda _gap: self._git("commit", "--allow-empty", "-qm", "advance fixture Git HEAD"),
            "bytes": lambda gap: self.path.write_bytes(gap + b"\nlocked-drift\n"),
            "source": lambda _gap: source_drift(),
            "history": history_drift,
        }
        for label, mutate in variants.items():
            with self.subTest(drift=label), self.stale_git_backed_gap() as gap_bytes:
                plan = plan_release_manifest_reconciliation(self.root)
                authorization = self._authorize(plan)
                before = self.records()
                original_lock = reconciliation_module._carrier_lock

                @contextmanager
                def mutate_after_lock(root: Path, manifest_ref: str):
                    with original_lock(root, manifest_ref):
                        mutate(gap_bytes)
                        yield

                with patch("release_manifest_reconciliation._carrier_lock", mutate_after_lock):
                    result = reconcile_release_manifest_history(
                        self.root, execute=True, authorization=authorization,
                    )
                self.assertEqual("blocked", result["disposition"])
                self.assertEqual("execute", result["mode"])
                if label != "history":
                    self.assertEqual(before, self.records())

    def test_completed_current_git_state_without_gap_is_refused(self) -> None:
        self._commit_manifest(self.initial_bytes)
        with self.assertRaises(ValueError):
            plan_release_manifest_reconciliation(self.root)
        self.assertEqual(self.initial_bytes, self.path.read_bytes())
        self.assertEqual(self.initial_records, self.records())
        self.assertEqual([], self._pending_ids())

    def test_cross_operation_dirty_bytes_and_changed_history_refuse_before_observation(self) -> None:
        with self.stale_git_backed_gap() as gap_bytes:
            plan = plan_release_manifest_reconciliation(self.root)
            with self.assertRaises(ValueError):
                reconcile_release_manifest_history(self.root, execute=True, authorization=self.initial_context)
            self.assertEqual(gap_bytes, self.path.read_bytes())
            self.assertEqual(self.initial_records, self.records())
            self.path.write_bytes(gap_bytes + b"\ndirty\n")
            with self.assertRaises(ValueError):
                reconcile_release_manifest_history(self.root, execute=True, authorization=self._authorize(plan))
            self.assertEqual([], self._pending_ids())
            self.path.write_bytes(gap_bytes)
            journal = self.root / ".caprmedio_caprmedio/_journal/conflicting.ndjson"
            journal.write_text(json.dumps({"schema_version": 3, "event": "recovered", "kind": "governed_project_state", "subject_kind": "file", "result": {"path": plan["manifest_ref"], "version": 2, "sha256": "f" * 64}}) + "\n")
            with self.assertRaises(ValueError):
                plan_release_manifest_reconciliation(self.root)
            self.assertEqual(gap_bytes, self.path.read_bytes())

    def test_append_failure_retries_original_observation_once_then_refresh_links_it(self) -> None:
        with self.stale_git_backed_gap() as gap_bytes:
            plan = plan_release_manifest_reconciliation(self.root)
            original_append = work_journal.append_sealed_events
            with patch(
                "release_manifest_reconciliation.work_journal.append_sealed_events",
                side_effect=work_journal.WorkJournalError("injected", "append failure"),
            ):
                failed = reconcile_release_manifest_history(
                    self.root, execute=True, authorization=self._authorize(plan),
            )
            self.assertEqual("recording_required", failed["disposition"])
            self.assertEqual("execute", failed["mode"])
            pending = self._pending_ids()
            self.assertEqual(1, len(pending))
            self.assertEqual(gap_bytes, self.path.read_bytes())
            with self.assertRaises(ValueError):
                self._authorize(plan)
            recovery_context = authorize_operator_reconciliation_recovery(
                self.root, pending[0], operator_name="Anatoly Maslennikov",
                journal_author="anatoly-m-maslennikov",
                llm_session={"app": "test", "uuid": "reconciliation-recovery"},
                authorization_ref="authorization/reconciliation-recovery.md",
            )
            with patch(
                "release_manifest_reconciliation.work_journal.append_sealed_events", original_append,
            ):
                retried = recover_release_manifest_reconciliation(
                    self.root, pending[0], recovery_context,
            )
            self.assertEqual("recovered", retried["disposition"])
            self.assertEqual("recover", retried["mode"])
            observed = self.records()[-1]
            self.assertEqual(3, observed["result"]["version"])
            self.assertEqual([], self._pending_ids())

            refresh_plan = plan_release_manifest_refresh(self.root)
            from release_manifest_authorization import authorize_operator_refresh
            refresh_context = authorize_operator_refresh(
                self.root, refresh_plan, operator_name="Anatoly Maslennikov",
                journal_author="anatoly-m-maslennikov",
                llm_session={"app": "test", "uuid": "reconciliation-refresh"},
                authorization_ref="authorization/reconciliation-refresh.md",
            )
            refreshed = refresh_release_manifest(self.root, execute=True, authorization=refresh_context)
            self.assertEqual("published", refreshed["disposition"])
            completed = self.records()[-1]
            self.assertEqual("completed", completed["event"])
            self.assertEqual(4, completed["result"]["version"])
            self.assertEqual(observed["event_id"], completed["previous_result_event"])


if __name__ == "__main__":
    unittest.main()
