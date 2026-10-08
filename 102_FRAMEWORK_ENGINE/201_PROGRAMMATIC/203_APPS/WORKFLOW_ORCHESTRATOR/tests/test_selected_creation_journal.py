"""Focused canonical-Journal tests for observed W01 file creation."""

from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[2] / "201_TOOLS"
TEST_TEMP_ROOT = APP.parents[2] / ".caprmedio_tmp/tests/selected-creation-journal"
for location in (APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_creation_journal import (  # noqa: E402
    CreationJournalError,
    preflight_creation,
    record_selected_creation,
    seal_creation_append_context,
)
from work_journal import with_event_digest  # noqa: E402


class SelectedCreationJournalTest(unittest.TestCase):
    def setUp(self) -> None:
        TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(
            dir=TEST_TEMP_ROOT,
            ignore_cleanup_errors=True,
        )
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
        self.created = self.root / "atoms/CA-M-301.md"
        self.created.parent.mkdir()
        self.created.write_bytes(b"observed W01 carrier")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def event(self) -> dict[str, object]:
        return with_event_digest(
            {
                "schema_version": 3,
                "event_id": "creation-event",
                "action_id": "creation-action",
                "event": "completed",
                "kind": "governed_project_change",
                "subject_kind": "file",
                "author": "test-user",
                "occurred_at": "2026-10-08T00:00:00+04:00",
                "llm_session": {"app": "codex", "uuid": "creation-session"},
                "structural_scope": "CORE_META_MODEL",
                "action_type": "ADD",
                "sources": [],
                "result": {
                    "state": "present",
                    "filename": "CA-M-301.md",
                    "version": 1,
                    "path": "atoms/CA-M-301.md",
                    "sha256": hashlib.sha256(self.created.read_bytes()).hexdigest(),
                },
            }
        )

    def context(self, event: dict[str, object], *, author: str = "test-user") -> dict[str, object]:
        return seal_creation_append_context(
            self.root,
            event,
            author=author,
            local_date="2026-10-08",
            timezone="Asia/Tbilisi",
        )

    def test_real_canonical_add_append_returns_matching_receipt(self) -> None:
        event = self.event()

        recorded = record_selected_creation(
            self.root,
            canonical_event=event,
            append_context=self.context(event),
        )

        self.assertEqual("completed", recorded["state"])
        self.assertEqual(event["event_id"], recorded["receipt"]["event_id"])
        self.assertEqual(event["event_digest"], recorded["receipt"]["event_digest"])

    def test_append_failure_preserves_pending_actual_effect_reference(self) -> None:
        event = self.event()
        with patch("selected_creation_journal.append_sealed_events", side_effect=OSError("full")):
            recorded = record_selected_creation(
                self.root,
                canonical_event=event,
                append_context=self.context(event),
            )

        self.assertEqual("recording_pending", recorded["state"])
        self.assertEqual(event["event_digest"], recorded["pending"]["event_digest"])
        self.assertEqual(["atoms/CA-M-301.md"], recorded["pending"]["effect_refs"])

    def test_add_with_prior_history_is_refused(self) -> None:
        event = self.event()
        event["previous_result_event"] = "invented-history"

        with self.assertRaises(CreationJournalError):
            preflight_creation(event)

    def test_non_add_is_refused(self) -> None:
        event = self.event()
        event["action_type"] = "MOVE"

        with self.assertRaises(CreationJournalError):
            preflight_creation(event)

    def test_author_mismatch_is_refused_before_readback(self) -> None:
        event = self.event()

        with self.assertRaises(CreationJournalError):
            record_selected_creation(
                self.root,
                canonical_event=event,
                append_context=self.context(event, author="other-user"),
            )

    def test_readback_digest_drift_is_refused(self) -> None:
        event = self.event()
        self.created.write_bytes(b"drift")

        with self.assertRaises(CreationJournalError):
            record_selected_creation(
                self.root,
                canonical_event=event,
                append_context=self.context(event),
            )

    def test_unconfirmed_receipt_becomes_pending_evidence(self) -> None:
        event = self.event()
        with patch("selected_creation_journal.append_sealed_events", return_value=[]):
            recorded = record_selected_creation(
                self.root,
                canonical_event=event,
                append_context=self.context(event),
            )

        self.assertEqual("recording_pending", recorded["state"])
        self.assertEqual("unconfirmed-append", recorded["pending"]["diagnostic"])
