"""Schema-v5 Journal validation and date-rollover recovery tests."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import work_journal  # noqa: E402


class WorkJournalSchemaV5Test(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.root = Path(self.directory.name)
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
        self.event = self._event()

    def tearDown(self) -> None:
        self.directory.cleanup()

    def _event(self) -> dict[str, object]:
        event: dict[str, object] = {
            "schema_version": 5,
            "kind": "workflow_execution",
            "event_id": "event-1510",
            "action_id": "action-1510",
            "event": "completed",
            "author": "test-user",
            "occurred_at": "2026-10-04T19:15:00+04:00",
            "llm_session": {"app": "codex", "uuid": "session-1510"},
            "structural_scope": "TOOLS",
            "initiative": {
                "initiative_id": "initiative-1510",
                "instruction_summary": "record one selected run",
                "initiative_ref": "03_plan/CA-P-1510.md",
            },
            "run": {
                "run_id": "run-1510",
                "kind": "action",
                "definition": {
                    "atom_id": "CA-O-1510",
                    "version": 1,
                    "path": "operations/CA-O-1510.md",
                    "digest": "a" * 64,
                },
            },
            "definition_bindings": [
                {
                    "kind": "action",
                    "atom_id": "CA-O-1510",
                    "version": 1,
                    "path": "operations/CA-O-1510.md",
                    "digest": "a" * 64,
                }
            ],
            "input_ref": "inputs/CA-I-1510.json",
            "outcome": "completed",
            "result_ref": "results/CA-R-1510.json",
            "effect_refs": ["03_plan/result.md"],
            "report_ref": "reports/CA-R-1510.md",
            "redaction": {"redacted": False, "fields": []},
        }
        return work_journal.with_event_digest(event)

    def test_configured_root_defaults_to_exact_generic_control_journal(self) -> None:
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        settings.write_text(
            "[paths]\n"
            'control_root = ".caprmedio_example"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )

        self.assertEqual(
            Path(".caprmedio_example/_journal"),
            work_journal.configured_journal_root(self.root),
        )

        settings.write_text(
            "[paths]\n"
            'control_root = ".caprmedio_example"\n'
            'journal_root = ".caprmedio_example/work_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        with self.assertRaisesRegex(RuntimeError, "exactly"):
            work_journal.configured_journal_root(self.root)

    def test_recovery_maps_legacy_sealed_carrier_to_canonical_location(self) -> None:
        legacy_context = {
            "author": "test-user",
            "local_date": "2026-10-04",
            "timezone": "Asia/Tbilisi",
            "partition_ref": ".caprmedio_caprmedio/work_journal/test-user-2026-10-04-part-1.ndjson",
        }
        legacy_context["append_context_digest"] = work_journal.canonical_json_digest(legacy_context)
        pending = work_journal.store_pending_event(
            self.root,
            self.event,
            legacy_context,
            result_ref="results/CA-R-1510.json",
            effect_refs=["03_plan/result.md"],
            diagnostic="recover after the byte-preserving Journal rename",
        )
        self.assertEqual(
            work_journal.canonical_json_bytes(legacy_context).decode("utf-8"),
            pending["append_context_bytes"],
        )

        receipt = work_journal.recover_pending_event(self.root, "event-1510")

        self.assertEqual(
            ".caprmedio_caprmedio/_journal/test-user-2026-10-04-part-1.ndjson",
            receipt["carrier"],
        )
        journal = self.root / ".caprmedio_caprmedio/_journal/test-user-2026-10-04-part-1.ndjson"
        self.assertTrue(journal.is_file())
        self.assertEqual(1, len(journal.read_text(encoding="utf-8").splitlines()))
        self.assertFalse((self.root / ".caprmedio_caprmedio/work_journal").exists())

    def test_migration_pending_blocks_admission_without_new_journal_or_events(self) -> None:
        legacy = self.root / ".caprmedio_caprmedio/work_journal"
        legacy.mkdir()

        with self.assertRaisesRegex(RuntimeError, "migration-pending"):
            work_journal.append_sealed_events(
                self.root,
                [self.event],
                author="test-user",
                local_date="2026-10-04",
                timezone="Asia/Tbilisi",
            )

        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())
        self.assertEqual([], list(legacy.glob("*.ndjson")))

    def test_global_recovery_reuses_original_context_after_receipt_failure(self) -> None:
        original_atomic = work_journal._atomic_json
        with mock.patch.object(work_journal, "_atomic_json", side_effect=OSError("receipt write interrupted")):
            with self.assertRaises(OSError):
                work_journal.append_sealed_events(
                    self.root,
                    [self.event],
                    author="test-user",
                    local_date="2026-10-04",
                    timezone="Asia/Tbilisi",
                )
        context = work_journal.seal_append_context(
            self.root,
            self.event,
            author="test-user",
            local_date="2026-10-04",
            timezone="Asia/Tbilisi",
        )
        work_journal.store_pending_event(
            self.root,
            self.event,
            context,
            result_ref="results/CA-R-1510.json",
            effect_refs=["03_plan/result.md"],
            diagnostic="receipt write interrupted",
        )
        receipt = work_journal.recover_pending_event(self.root, "event-1510")
        self.assertEqual(".caprmedio_caprmedio/_journal/test-user-2026-10-04-part-1.ndjson", receipt["carrier"])
        journal = self.root / ".caprmedio_caprmedio/_journal/test-user-2026-10-04-part-1.ndjson"
        self.assertEqual(1, len(journal.read_text(encoding="utf-8").splitlines()))
        changed = dict(self.event)
        changed["event"] = "failed"
        changed["outcome"] = "failed"
        changed = work_journal.with_event_digest(changed)
        with self.assertRaises(work_journal.WorkJournalError) as error:
            work_journal.append_sealed_events(
                self.root,
                [changed],
                author="test-user",
                local_date="2026-10-05",
                timezone="UTC",
            )
        self.assertEqual("identity-collision", error.exception.code)
        self.assertEqual(1, len(journal.read_text(encoding="utf-8").splitlines()))
        self.assertIsNotNone(original_atomic)


if __name__ == "__main__":
    unittest.main()
