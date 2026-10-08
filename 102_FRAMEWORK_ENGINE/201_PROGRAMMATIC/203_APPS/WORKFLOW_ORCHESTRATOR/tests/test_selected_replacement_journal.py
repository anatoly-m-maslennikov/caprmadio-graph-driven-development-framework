"""Focused canonical-Journal tests for selected Atom replacement recording."""

from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[2] / "201_TOOLS"
TEST_TEMP_ROOT = APP.parents[2] / ".caprmedio_tmp/tests/selected-replacement-journal"
for location in (APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_replacement_journal import (  # noqa: E402
    ReplacementJournalError,
    preflight,
    record_selected_replacement,
)
from work_journal import seal_append_context, with_event_digest  # noqa: E402


class SelectedReplacementJournalTest(unittest.TestCase):
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
        self.result_path = self.root / "archive/replacement.md"
        self.result_path.parent.mkdir()
        self.result_path.write_bytes(b"replacement bytes")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def event(self, relative_path: str = "archive/replacement.md") -> dict[str, object]:
        result_path = self.root / relative_path
        return with_event_digest(
            {
                "schema_version": 3,
                "event_id": "replacement-event",
                "action_id": "replacement-action",
                "event": "completed",
                "kind": "governed_project_change",
                "subject_kind": "file",
                "author": "test-user",
                "occurred_at": "2026-09-14T00:00:00+04:00",
                "llm_session": {"app": "codex", "uuid": "replacement-session"},
                "structural_scope": "CORE_META_MODEL",
                "action_type": "MOVE",
                "sources": [],
                "previous_result_event": "predecessor-event",
                "predecessor_atom_id": "CA-M-224",
                "successor_atom_ids": ["CA-O-101", "CA-O-102"],
                "result": {
                    "state": "present",
                    "filename": "replacement.md",
                    "version": 12,
                    "path": relative_path,
                    "sha256": hashlib.sha256(result_path.read_bytes()).hexdigest(),
                },
            }
        )

    def context(self, event: dict[str, object], *, author: str = "test-user") -> dict[str, object]:
        return seal_append_context(
            self.root,
            event,
            author=author,
            local_date="2026-09-14",
            timezone="Asia/Tbilisi",
        )

    def test_real_canonical_append_returns_matching_receipt(self) -> None:
        event = self.event()

        recorded = record_selected_replacement(
            self.root,
            canonical_event=event,
            append_context=self.context(event),
        )

        self.assertEqual("completed", recorded["state"])
        self.assertEqual(event["event_id"], recorded["receipt"]["event_id"])
        self.assertEqual(event["event_digest"], recorded["receipt"]["event_digest"])

    def test_append_failure_preserves_pending_canonical_evidence(self) -> None:
        event = self.event()
        context = self.context(event)

        with patch("selected_replacement_journal.append_sealed_events", side_effect=OSError("full")):
            recorded = record_selected_replacement(self.root, canonical_event=event, append_context=context)

        self.assertEqual("recording_pending", recorded["state"])
        self.assertEqual(event["event_digest"], recorded["pending"]["event_digest"])
        self.assertEqual("archive/replacement.md", recorded["pending"]["effect_refs"][0])

    def test_invalid_append_context_is_refused_before_readback(self) -> None:
        with self.assertRaises(ReplacementJournalError):
            preflight(self.root, self.event(), {})

    def test_context_author_mismatch_is_refused_before_readback(self) -> None:
        event = self.event()
        context = self.context(event, author="other-user")

        with self.assertRaises(ReplacementJournalError):
            preflight(self.root, event, context)

    def test_noncanonical_event_is_refused(self) -> None:
        event = self.event()
        event["kind"] = "atom_replacement"

        with self.assertRaises(ReplacementJournalError):
            preflight(self.root, event, self.context(self.event()))

    def test_readback_digest_drift_is_refused(self) -> None:
        event = self.event()
        self.result_path.write_bytes(b"drift")

        with self.assertRaises(ReplacementJournalError):
            record_selected_replacement(self.root, canonical_event=event, append_context=self.context(event))

    def test_symlink_ancestor_is_refused(self) -> None:
        target = self.root / "outside"
        target.mkdir()
        (target / "replacement.md").write_bytes(b"replacement bytes")
        (self.root / "linked").symlink_to(target, target_is_directory=True)
        event = self.event("linked/replacement.md")

        with self.assertRaises(ReplacementJournalError):
            record_selected_replacement(self.root, canonical_event=event, append_context=self.context(event))

    def test_empty_append_receipts_become_pending_evidence(self) -> None:
        event = self.event()

        with patch("selected_replacement_journal.append_sealed_events", return_value=[]):
            recorded = record_selected_replacement(
                self.root,
                canonical_event=event,
                append_context=self.context(event),
            )

        self.assertEqual("recording_pending", recorded["state"])
        self.assertEqual("unconfirmed-append", recorded["pending"]["diagnostic"])

    def test_nonmatching_append_receipt_becomes_pending_evidence(self) -> None:
        event = self.event()

        with patch(
            "selected_replacement_journal.append_sealed_events",
            return_value=[{"event_id": "other", "event_digest": "other"}],
        ):
            recorded = record_selected_replacement(
                self.root,
                canonical_event=event,
                append_context=self.context(event),
            )

        self.assertEqual("recording_pending", recorded["state"])
        self.assertEqual("unconfirmed-append", recorded["pending"]["diagnostic"])
