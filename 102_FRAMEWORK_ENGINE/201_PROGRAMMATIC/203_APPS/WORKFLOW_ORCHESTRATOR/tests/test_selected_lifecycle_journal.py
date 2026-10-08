"""Focused lifecycle Journal producer tests using disposable canonical carriers."""

from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[2] / "201_TOOLS"
TEST_TEMP_ROOT = APP.parents[2] / ".caprmedio_tmp/tests/selected-lifecycle-journal"
for location in (APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_lifecycle_journal import (  # noqa: E402
    LifecycleJournalError,
    admit_lifecycle_prior,
    prepare_lifecycle_journal,
    record_lifecycle_change,
)
from work_journal import (  # noqa: E402
    WorkJournalError,
    append_sealed_events,
    canonical_json_digest,
    seal_append_context,
    validate_sealed_event,
    with_event_digest,
)


class SelectedLifecycleJournalTest(unittest.TestCase):
    def setUp(self) -> None:
        TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\n"
            'control_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        self.path = self.root / "atoms/draft.md"
        self.path.parent.mkdir()
        self.path.write_bytes(b"before")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def facts(self) -> dict[str, object]:
        return {
            "filename": "draft.md",
            "version": 1,
            "path": "atoms/draft.md",
            "sha256": hashlib.sha256(self.path.read_bytes()).hexdigest(),
        }

    def pin(self) -> dict[str, object]:
        return {
            "action_id": "draft-status-change",
            "structural_scope": "CORE_META_MODEL",
            "occurred_at": "2026-10-08T00:00:00+04:00",
            "llm_session": {"app": "codex", "uuid": "lifecycle-session"},
        }

    def context_for(self, event: dict[str, object]) -> dict[str, object]:
        return seal_append_context(
            self.root,
            event,
            author="test-user",
            local_date="2026-10-08",
            timezone="Asia/Tbilisi",
        )

    def prepared(self) -> tuple[dict[str, object], dict[str, object]]:
        provisional = with_event_digest(
            {
                "schema_version": 3,
                "event_id": "context-event",
                "action_id": "draft-status-change",
                "event": "recovered",
                "kind": "governed_project_state",
                "subject_kind": "file",
                "author": "test-user",
                "occurred_at": self.pin()["occurred_at"],
                "llm_session": self.pin()["llm_session"],
                "structural_scope": self.pin()["structural_scope"],
                "result": {"state": "present", **self.facts()},
                "recovery_evidence": {
                    "carrier": {
                        "path": self.facts()["path"],
                        "sha256": self.facts()["sha256"],
                        "observed_at": self.pin()["occurred_at"],
                        "observer_run_id": "context-run",
                    }
                },
            }
        )
        context = self.context_for(provisional)
        prepared = prepare_lifecycle_journal(
            self.root,
            self.facts(),
            self.path.read_bytes(),
            self.pin(),
            "run-before",
            context,
        )
        return dict(prepared), context

    def test_carrier_only_baseline_is_prepared_and_admitted_before_effects(self) -> None:
        prepared, context = self.prepared()

        admitted = admit_lifecycle_prior(self.root, prepared, context)

        self.assertEqual("prepared_observed_baseline", prepared["state"])
        self.assertEqual("admitted", admitted["state"])
        self.assertEqual("recovered", admitted["event"]["event"])
        self.assertEqual("atoms/draft.md", admitted["event"]["recovery_evidence"]["carrier"]["path"])

    def test_existing_legacy_add_without_git_is_exact_prior(self) -> None:
        event = with_event_digest(
            {
                "schema_version": 3,
                "event_id": "legacy-created",
                "action_id": "legacy-action",
                "event": "completed",
                "kind": "governed_project_change",
                "subject_kind": "file",
                "author": "test-user",
                "occurred_at": self.pin()["occurred_at"],
                "llm_session": self.pin()["llm_session"],
                "structural_scope": self.pin()["structural_scope"],
                "action_type": "ADD",
                "sources": [],
                "result": {"state": "present", **self.facts()},
            }
        )
        context = self.context_for(event)
        append_sealed_events(
            self.root,
            [event],
            author=context["author"],
            local_date=context["local_date"],
            timezone=context["timezone"],
            append_context=context,
        )

        prepared = prepare_lifecycle_journal(
            self.root, self.facts(), self.path.read_bytes(), self.pin(), "draft-run", context
        )

        self.assertEqual("exact_prior", prepared["state"])
        self.assertEqual("legacy-created", prepared["event"]["event_id"])

    def test_other_author_exact_prior_reuses_verified_receipt_without_reappend(self) -> None:
        event = with_event_digest(
            {
                "schema_version": 3,
                "event_id": "other-author-created",
                "action_id": "legacy-action",
                "event": "completed",
                "kind": "governed_project_change",
                "subject_kind": "file",
                "author": "other-user",
                "occurred_at": self.pin()["occurred_at"],
                "llm_session": self.pin()["llm_session"],
                "structural_scope": self.pin()["structural_scope"],
                "action_type": "ADD",
                "sources": [],
                "result": {"state": "present", **self.facts()},
            }
        )
        other_context = seal_append_context(
            self.root, event, author="other-user", local_date="2026-10-08", timezone="Asia/Tbilisi"
        )
        append_sealed_events(
            self.root, [event], author="other-user", local_date="2026-10-08",
            timezone="Asia/Tbilisi", append_context=other_context,
        )
        current_context = self.context_for(self.prepared()[0]["event"])
        prepared = prepare_lifecycle_journal(
            self.root, self.facts(), self.path.read_bytes(), self.pin(), "current-run", current_context
        )

        with patch("selected_lifecycle_journal.append_sealed_events") as append:
            admitted = admit_lifecycle_prior(self.root, prepared, current_context)

        self.assertEqual("admitted", admitted["state"])
        self.assertEqual("other-author-created", admitted["receipt"]["event_id"])
        append.assert_not_called()

    def test_schema2_prior_is_reused_by_v3_lifecycle_change(self) -> None:
        event = with_event_digest(
            {
                "schema_version": 2,
                "event_id": "schema2-created",
                "action_id": "schema2-action",
                "event": "completed",
                "kind": "governed_file_change",
                "author": "other-user",
                "occurred_at": self.pin()["occurred_at"],
                "llm_session": self.pin()["llm_session"],
                "structural_scope": self.pin()["structural_scope"],
                "action_type": "ADD",
                "sources": [],
                "result": {"state": "present", **self.facts()},
            }
        )
        other_context = seal_append_context(
            self.root, event, author="other-user", local_date="2026-10-08", timezone="Asia/Tbilisi"
        )
        append_sealed_events(
            self.root, [event], author="other-user", local_date="2026-10-08",
            timezone="Asia/Tbilisi", append_context=other_context,
        )
        current_context = self.context_for(self.prepared()[0]["event"])

        prepared = prepare_lifecycle_journal(
            self.root, self.facts(), self.path.read_bytes(), self.pin(), "v3-run", current_context
        )

        self.assertEqual("schema2-created", prepared["event"]["event_id"])
        self.assertEqual("admitted", admit_lifecycle_prior(self.root, prepared, current_context)["state"])

    def test_idless_draft_action_pin_is_supported(self) -> None:
        prepared, _context = self.prepared()

        self.assertEqual("draft-status-change", prepared["event"]["action_id"])

    def test_schema5_run_record_is_ignored_when_finding_file_prior(self) -> None:
        run = with_event_digest(
            {
                "schema_version": 5,
                "kind": "workflow_execution",
                "event_id": "unrelated-run",
                "action_id": "run-action",
                "event": "completed",
                "author": "test-user",
                "occurred_at": self.pin()["occurred_at"],
                "llm_session": self.pin()["llm_session"],
                "structural_scope": "TOOLS",
                "initiative": {
                    "initiative_id": "initiative-1",
                    "instruction_summary": "run unrelated work",
                    "initiative_ref": "plans/one.md",
                },
                "run": {
                    "run_id": "run-1",
                    "kind": "action",
                    "definition": {
                        "atom_id": "CA-O-1", "version": 1,
                        "path": "operations/one.md", "digest": "a" * 64,
                    },
                },
                "definition_bindings": [{
                    "kind": "action", "atom_id": "CA-O-1", "version": 1,
                    "path": "operations/one.md", "digest": "a" * 64,
                }],
                "input_ref": "inputs/one.json",
                "outcome": "completed",
                "result_ref": "results/one.json",
                "effect_refs": ["effects/one.md"],
                "report_ref": "reports/one.md",
                "redaction": {"redacted": False, "fields": []},
            }
        )
        context = self.context_for(run)
        append_sealed_events(
            self.root, [run], author=context["author"], local_date=context["local_date"],
            timezone=context["timezone"], append_context=context,
        )

        prepared = prepare_lifecycle_journal(
            self.root, self.facts(), self.path.read_bytes(), self.pin(), "baseline-run", context
        )

        self.assertEqual("prepared_observed_baseline", prepared["state"])

    def test_carrier_only_recovery_is_file_only_but_legacy_folder_evidence_still_reads(self) -> None:
        entries = [{"path": "archive/item.md", "sha256": "a" * 64}]
        result = {
            "state": "present", "filename": "archive", "version": 1, "path": "archive",
            "entries": entries,
            "sha256": canonical_json_digest([{"path": "item.md", "sha256": "a" * 64}]),
        }
        common = {
            "schema_version": 3,
            "event_id": "folder-recovery",
            "action_id": "folder-action",
            "event": "recovered",
            "kind": "governed_project_state",
            "subject_kind": "folder",
            "author": "test-user",
            "occurred_at": self.pin()["occurred_at"],
            "llm_session": self.pin()["llm_session"],
            "structural_scope": "CORE_META_MODEL",
            "result": result,
        }
        carrier_only = with_event_digest({
            **common,
            "recovery_evidence": {"carrier": {
                "path": "archive", "sha256": result["sha256"],
                "observed_at": self.pin()["occurred_at"], "observer_run_id": "folder-run",
            }},
        })
        legacy = with_event_digest({
            **common,
            "recovery_evidence": {"git": {"commit": "abc"}, "carrier": {"path": "archive"}},
        })

        with self.assertRaises(WorkJournalError):
            validate_sealed_event(carrier_only)
        self.assertEqual(legacy["event_id"], validate_sealed_event(legacy)["event_id"])

    def test_pending_prior_blocks_effect_admission(self) -> None:
        prepared, context = self.prepared()
        with patch("selected_lifecycle_journal.append_sealed_events", side_effect=OSError("full")):
            admitted = admit_lifecycle_prior(self.root, prepared, context)

        self.assertEqual("recording_pending", admitted["state"])

    def test_readback_drift_refuses_prior_admission(self) -> None:
        prepared, context = self.prepared()
        self.path.write_bytes(b"drift")

        with self.assertRaises(LifecycleJournalError):
            admit_lifecycle_prior(self.root, prepared, context)

    def test_noop_creates_no_change_event(self) -> None:
        prepared, context = self.prepared()
        admitted = admit_lifecycle_prior(self.root, prepared, context)

        result = record_lifecycle_change(
            self.root,
            prior=admitted["event"],
            after_facts=self.facts(),
            current_bytes=self.path.read_bytes(),
            action_pin=self.pin(),
            run_id="run-after",
            context=context,
            action_type="UPDATE",
            native_effects={"result": {"state": "present", **self.facts()}},
        )

        self.assertEqual({"state": "no_op"}, result)

    def test_pending_after_effect_retains_actual_effect_reference(self) -> None:
        prepared, context = self.prepared()
        prior = admit_lifecycle_prior(self.root, prepared, context)["event"]
        self.path.write_bytes(b"after")
        after = self.facts()
        with patch("selected_lifecycle_journal.append_sealed_events", side_effect=OSError("full")):
            recorded = record_lifecycle_change(
                self.root,
                prior=prior,
                after_facts=after,
                current_bytes=self.path.read_bytes(),
                action_pin=self.pin(),
                run_id="run-after",
                context=context,
                action_type="UPDATE",
                native_effects={"result": {"state": "present", **after}},
            )

        self.assertEqual("recording_pending", recorded["state"])
        self.assertEqual(["atoms/draft.md"], recorded["pending"]["effect_refs"])

    def test_unappended_or_pending_prior_cannot_record_orphan_change(self) -> None:
        prepared, context = self.prepared()
        baseline = prepared["event"]
        self.path.write_bytes(b"after")
        after = self.facts()

        with self.assertRaises(LifecycleJournalError):
            record_lifecycle_change(
                self.root,
                prior=baseline,
                after_facts=after,
                current_bytes=self.path.read_bytes(),
                action_pin=self.pin(),
                run_id="orphan-after",
                context=context,
                action_type="UPDATE",
                native_effects={"result": {"state": "present", **after}},
            )

    def test_corrupt_prior_carrier_is_not_treated_as_absent_baseline(self) -> None:
        _prepared, context = self.prepared()
        journal = self.root / ".caprmedio_caprmedio/_journal"
        journal.mkdir(parents=True)
        (journal / "test-user-2026-10-08-part-1.ndjson").write_text("{not-json}\n", encoding="utf-8")

        with self.assertRaises(LifecycleJournalError):
            prepare_lifecycle_journal(
                self.root, self.facts(), self.path.read_bytes(), self.pin(), "corrupt-run", context
            )

    def test_forged_exact_prior_with_cached_style_receipt_is_refused(self) -> None:
        prepared, context = self.prepared()
        event = prepared["event"]
        forged = {
            "state": "exact_prior",
            "event": event,
            "receipt": {"event_id": event["event_id"], "event_digest": event["event_digest"]},
        }

        with self.assertRaises(LifecycleJournalError):
            admit_lifecycle_prior(self.root, forged, context)

    def test_replaced_prior_between_prepare_and_admit_is_refused(self) -> None:
        prepared, context = self.prepared()
        admitted = admit_lifecycle_prior(self.root, prepared, context)
        exact = prepare_lifecycle_journal(
            self.root, self.facts(), self.path.read_bytes(), self.pin(), "later-run", context
        )
        carrier = self.root / admitted["receipt"]["carrier"]
        carrier.write_text("{}\n", encoding="utf-8")

        with self.assertRaises(LifecycleJournalError):
            admit_lifecycle_prior(self.root, exact, context)

    def test_replaced_prior_after_admission_cannot_anchor_change(self) -> None:
        prepared, context = self.prepared()
        admitted = admit_lifecycle_prior(self.root, prepared, context)
        (self.root / admitted["receipt"]["carrier"]).write_text("{}\n", encoding="utf-8")
        self.path.write_bytes(b"after")
        after = self.facts()

        with self.assertRaises(LifecycleJournalError):
            record_lifecycle_change(
                self.root,
                prior=admitted["event"],
                after_facts=after,
                current_bytes=self.path.read_bytes(),
                action_pin=self.pin(),
                run_id="after-removal",
                context=context,
                action_type="UPDATE",
                native_effects={"result": {"state": "present", **after}},
            )
