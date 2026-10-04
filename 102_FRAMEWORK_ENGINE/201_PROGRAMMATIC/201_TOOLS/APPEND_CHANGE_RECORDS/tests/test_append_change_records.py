"""Deterministic acceptance tests for APPEND_CHANGE_RECORDS."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
from typing import Any


TOOLS = Path(__file__).resolve().parents[2]
APPENDER = TOOLS / "APPEND_CHANGE_RECORDS"
CONTEXT_TOOL = TOOLS / "COMMIT_CONTEXT"
for _parent in Path(__file__).resolve().parents:
    if _parent.name == ".caprmedio":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
for path in (str(APPENDER), str(TOOLS)):
    if path not in sys.path:
        sys.path.insert(0, path)

from append_change_records import (  # noqa: E402
    ToolError,
    _expected_context_id,
    _expected_event_id,
    release_verified_lease,
    run,
)
from work_journal import (  # noqa: E402
    WorkJournalError,
    append_sealed_events,
    canonical_json_bytes,
    canonical_json_digest,
    event_digest,
    validate_sealed_event,
    with_event_digest,
)
sys.path.insert(0, str(CONTEXT_TOOL))
from commit_context_logic import gather_context  # noqa: E402


def sha(value: bytes | str) -> str:
    raw = value.encode("utf-8") if isinstance(value, str) else value
    return hashlib.sha256(raw).hexdigest()


class AppendChangeRecordsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\n"
            'control_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        self.run_git("init", "-q")
        self.run_git("config", "user.name", "Test User")
        self.run_git("config", "user.email", "test@example.invalid")
        self.run_git("add", ".caprmedio_caprmedio/caprmedio_project_settings.toml")
        self.run_git("commit", "-qm", "initial")
        self.artifact = self.root / "artifact.md"
        self.artifact.write_text("# Artifact\n\nInitial governed content.\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_git(self, *arguments: str) -> str:
        completed = subprocess.run(
            ["git", "-C", str(self.root), *arguments],
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()

    def repository_identity(self) -> str:
        git_directory = Path(self.run_git("rev-parse", "--git-dir"))
        if not git_directory.is_absolute():
            git_directory = self.root / git_directory
        return canonical_json_digest(
            {"repository_root": self.root.resolve().as_posix(), "git_directory": git_directory.resolve().as_posix()}
        )

    def context(self, *, action: str = "ADD", local_date: str = "2026-08-20") -> dict[str, object]:
        git_base = {
            "commit": self.run_git("rev-parse", "HEAD"),
            "tree": self.run_git("rev-parse", "HEAD^{tree}"),
        }
        result = {
            "state": "present",
            "filename": self.artifact.name,
            "version": 1,
            "path": self.artifact.relative_to(self.root).as_posix(),
            "sha256": sha(self.artifact.read_bytes()),
        }
        source_frontier = {
            "identity": "CA-R-001",
            "kind": "file",
            "state": "present",
            "filename": result["filename"],
            "version": result["version"],
            "path": result["path"],
            "sha256": result["sha256"],
        }
        event = {
            "schema_version": 3,
            "action_id": "action-001",
            "event": "completed",
            "kind": "governed_project_change",
            "subject_kind": "file",
            "author": "test-user",
            "occurred_at": "2026-08-20T23:59:59+04:00",
            "llm_session": {"app": "codex", "uuid": "session-001"},
            "structural_scope": "CAPRMEDIO",
            "action_type": action,
            "sources": [],
            "result": result,
        }
        if action != "ADD":
            event["previous_result_event"] = "prior-event"
        event["event_id"] = _expected_event_id(event)
        event = with_event_digest(event)
        context: dict[str, object] = {
            "schema_version": 3,
            "action_id": "action-001",
            "trigger": {
                "repository": {"root": str(self.root), "identity": self.repository_identity()},
            },
            "subject": {"identity": "CA-R-001", "kind": "file", "selected_state": "working"},
            "structural_scope": "CAPRMEDIO",
            "action_type": action,
            "sources": [],
            "relations": [],
            "result": result,
            "llm_session": {"app": "codex", "uuid": "session-001"},
            "author": "test-user",
            "occurred_at": "2026-08-20T23:59:59+04:00",
            "timezone": "Asia/Tbilisi",
            "local_date": local_date,
            "git_base": git_base,
            "frontier": {
                "source_sha256": canonical_json_digest(source_frontier),
                "relations_sha256": canonical_json_digest([]),
            },
            "snapshots": {"working": result},
            "validation": {"valid": True, "diagnostics": []},
            "predictions": {
                "journal_records": [event],
                "journal_partitions": [
                    {
                        "author": "test-user",
                        "local_date": local_date,
                        "part": 1,
                        "path": f".caprmedio_caprmedio/_journal/test-user-{local_date}-part-1.ndjson",
                        "predicted_line": 1,
                    }
                ],
            },
        }
        context["context_id"] = _expected_context_id(context)
        return context

    def test_dry_run_is_mutation_free(self) -> None:
        result = run(self.root, {"context": self.context()}, apply=False, wait_seconds=0)
        self.assertTrue(result["ok"])
        self.assertEqual("dry-run", result["mode"])
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    def test_apply_is_idempotent_and_routes_by_sealed_date(self) -> None:
        payload = {"context": self.context()}
        first = run(self.root, payload, apply=True, wait_seconds=0)
        second = run(self.root, payload, apply=True, wait_seconds=0)
        path = self.root / ".caprmedio_caprmedio/_journal/test-user-2026-08-20-part-1.ndjson"
        self.assertTrue(path.is_file())
        self.assertEqual(1, len(path.read_text(encoding="utf-8").splitlines()))
        self.assertEqual(first["result"]["receipts"], second["result"]["receipts"])
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal/test-user-2026-08-21-part-1.ndjson").exists())
        correlations = self.root / ".caprmedio_runtime/state/commit_trigger/pipeline_correlations.ndjson"
        registered = [json.loads(line) for line in correlations.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(["registered"], [record["event"] for record in registered])
        self.assertEqual(first["result"]["receipts"][0]["appended_carrier_digest"], registered[0]["transition"]["appended_carrier_digest"])
        release_verified_lease(self.root, first["result"]["lease"])
        retired = [json.loads(line) for line in correlations.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(["registered", "retired"], [record["event"] for record in retired])

    def test_rejects_stale_context_before_append(self) -> None:
        context = self.context()
        context["git_base"] = {"commit": "0" * 40, "tree": "0" * 40}
        with self.assertRaisesRegex(ToolError, "context_id"):
            run(self.root, {"context": context}, apply=True, wait_seconds=0)
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/state/commit_change_set/lease.json").exists())

    def test_rejects_existing_staged_change_before_append(self) -> None:
        unrelated = self.root / "unrelated.txt"
        unrelated.write_text("unrelated\n", encoding="utf-8")
        self.run_git("add", "unrelated.txt")
        with self.assertRaisesRegex(ToolError, "index contains a change outside the resolved subject identity"):
            run(self.root, {"context": self.context()}, apply=True, wait_seconds=0)
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())

    def test_rejects_missing_result_before_append(self) -> None:
        context = self.context()
        context.pop("result")
        with self.assertRaisesRegex(ToolError, "result must be an object"):
            run(self.root, {"context": context}, apply=True, wait_seconds=0)
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())

    def test_rolls_to_second_part_after_one_hundred_records(self) -> None:
        event_template = self.context()["predictions"]["journal_records"][0]
        assert isinstance(event_template, dict)
        events: list[dict[str, object]] = []
        for number in range(101):
            event = copy.deepcopy(event_template)
            event["event_id"] = f"event-{number:03d}"
            event["action_id"] = "one-action"
            event = with_event_digest(event)
            events.append(event)
        receipts = append_sealed_events(
            self.root,
            events,
            author="test-user",
            local_date="2026-08-20",
            timezone="Asia/Tbilisi",
        )
        first = self.root / ".caprmedio_caprmedio/_journal/test-user-2026-08-20-part-1.ndjson"
        second = self.root / ".caprmedio_caprmedio/_journal/test-user-2026-08-20-part-2.ndjson"
        self.assertEqual(100, len(first.read_text(encoding="utf-8").splitlines()))
        self.assertEqual(1, len(second.read_text(encoding="utf-8").splitlines()))
        self.assertEqual(100, receipts[99]["line"])
        self.assertEqual(1, receipts[100]["line"])

    def test_appends_recovery_then_change_from_exact_sealed_evidence(self) -> None:
        context = self.context(action="UPDATE")
        result = copy.deepcopy(context["result"])
        assert isinstance(result, dict)
        evidence = {
            "git": {"base_commit": context["git_base"]["commit"], "path": result["path"], "sha256": result["sha256"]},
            "carrier": {"identity": "CA-R-001", "kind": "file", "filename": result["filename"], "version": result["version"], "sha256": result["sha256"]},
        }
        recovered = {
            "schema_version": 3,
            "action_id": "action-001",
            "event": "recovered",
            "kind": "governed_project_state",
            "subject_kind": "file",
            "author": "test-user",
            "occurred_at": "2026-08-20T23:59:59+04:00",
            "llm_session": {"app": "codex", "uuid": "session-001"},
            "structural_scope": "CAPRMEDIO",
            "result": result,
            "recovery_evidence": evidence,
        }
        recovered["event_id"] = _expected_event_id(recovered)
        recovered = with_event_digest(recovered)
        completed = context["predictions"]["journal_records"][0]
        assert isinstance(completed, dict)
        completed = copy.deepcopy(completed)
        completed["previous_result_event"] = recovered["event_id"]
        completed["event_id"] = _expected_event_id(completed)
        completed = with_event_digest(completed)
        context["previous_result_event"] = recovered["event_id"]
        context["recovery"] = {
            "event_id": recovered["event_id"],
            "result": result,
            "evidence": evidence,
            "evidence_digest": canonical_json_digest(evidence),
            "contradictions": [],
        }
        context["predictions"]["journal_records"] = [recovered, completed]
        context["context_id"] = _expected_context_id(context)
        output = run(self.root, {"context": context}, apply=True, wait_seconds=0)
        journal = self.root / ".caprmedio_caprmedio/_journal/test-user-2026-08-20-part-1.ndjson"
        records = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(["recovered", "completed"], [record["event"] for record in records])
        self.assertEqual(recovered["event_id"], records[-1]["previous_result_event"])
        release_verified_lease(self.root, output["result"]["lease"])

    def test_consumes_the_actual_commit_context_schema(self) -> None:
        parent = self.root / ".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--parent.md"
        parent.parent.mkdir(parents=True, exist_ok=True)
        parent.write_text("---\nversion: 1\nrelations: {}\n---\n# Parent\n\nBody\n", encoding="utf-8")
        subject = self.root / ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        subject.write_text(
            "---\nversion: 1\nrelations:\n  child_of:\n    - CA-R-001-REQUIREMENT--parent\n---\n# Subject\n\nBody\n",
            encoding="utf-8",
        )
        self.run_git("config", "github.username", "test-user")
        repository_id = self.repository_identity()
        adapter_id = "test"
        source_event_id = "source-event"
        trigger = {
            "schema_version": 1,
            "trigger_id": canonical_json_digest(
                {
                    "schema_version": 1,
                    "adapter_id": adapter_id,
                    "source_event_id": source_event_id,
                    "repository_id": repository_id,
                }
            ),
            "adapter": {"id": adapter_id},
            "source_event_id": source_event_id,
            "repository": {"root": str(self.root.resolve()), "identity": repository_id},
            "observed_at": "2026-08-20T23:59:59+04:00",
            "before_path": None,
            "after_path": subject.relative_to(self.root).as_posix(),
            "llm_session": {"app": "codex", "uuid": "019f591f-04f6-70f2-8de7-828b7cccc69d"},
        }
        context = gather_context(self.root, trigger)
        output = run(self.root, {"context": context}, apply=False, wait_seconds=0)
        self.assertTrue(output["ok"])
        self.assertEqual("dry-run", output["mode"])


class ReplacementPayloadTest(unittest.TestCase):
    """Exercise the sealed library boundary without a live Git or Atom frontier."""

    def event(self) -> dict[str, Any]:
        filename = "CA-M-224-CORE_META_MODEL-METHOD--compile-methodology@12.md"
        return with_event_digest({
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
                "filename": filename,
                "version": 12,
                "path": f".caprmedio_caprmedio/05_method/archive/{filename}",
                "sha256": sha("unchanged predecessor content"),
            },
        })

    def assert_invalid(self, event: dict[str, Any], message: str) -> None:
        with self.assertRaisesRegex(WorkJournalError, message) as raised:
            validate_sealed_event(with_event_digest(event))
        self.assertEqual("invalid-event", raised.exception.code)

    def set_filename(self, event: dict[str, Any], filename: str) -> None:
        event["result"]["filename"] = filename
        event["result"]["path"] = f".caprmedio_caprmedio/05_method/archive/{filename}"

    def recover(self, event: dict[str, Any]) -> None:
        event.update(event="recovered", kind="governed_project_state")
        for key in ("action_type", "sources", "previous_result_event"):
            event.pop(key)
        event["recovery_evidence"] = {
            "git": {"base_commit": "1" * 40},
            "carrier": {"filename": event["result"]["filename"]},
        }

    def test_accepts_explicit_replacement_and_preserves_successor_order(self) -> None:
        for successors in (["CA-O-101"], [f"CA-O-{number}" for number in range(108, 100, -1)]):
            with self.subTest(successors=successors):
                event = self.event()
                event["successor_atom_ids"] = successors
                sealed = with_event_digest(event)
                before = canonical_json_bytes(sealed)
                self.assertEqual(sealed, validate_sealed_event(sealed))
                self.assertEqual(before, canonical_json_bytes(sealed))

    def test_accepts_project_owned_ids_and_sequence_prefixed_filenames(self) -> None:
        for atom_id in ("CA-M-224", "TEST-I-001", "PROJ_2-P-17", "MY-PROJECT-R-7"):
            for sequence in ("", "03-"):
                with self.subTest(atom_id=atom_id, sequence=sequence):
                    event = self.event()
                    event["predecessor_atom_id"] = atom_id
                    event["successor_atom_ids"] = ["TEST-O-002"]
                    self.set_filename(event, f"{sequence}{atom_id}-SCOPE--summary@12.md")
                    sealed = with_event_digest(event)
                    self.assertEqual(sealed, validate_sealed_event(sealed))

    def test_requires_both_fields_and_rejects_null(self) -> None:
        for key in ("predecessor_atom_id", "successor_atom_ids"):
            with self.subTest(missing=key):
                event = self.event()
                event.pop(key)
                self.assert_invalid(event, "must appear together")
            with self.subTest(null=key):
                event = self.event()
                event[key] = None
                self.assert_invalid(event, key)

    def test_preserves_nonconforming_replacement_identities(self) -> None:
        invalid = (
            "", " ", " CA-M-224", "CA-M-224 ", "ca-M-224", "CA-X-224",
            "CA-M--224", "CA-M-", "CA-M-224@12", "CA-M-224.md",
            "CA-M-224-SCOPE--summary", "folder/CA-M-224", "CA-M-224\n",
            "CAPRMEDIO-META-METH-224", "-M-224", "CA--M-224", "CA---M-224",
            "CA_-M-224", "C--A-M-224",
        )
        for predecessor in invalid:
            with self.subTest(predecessor=predecessor):
                event = self.event()
                event["predecessor_atom_id"] = predecessor
                self.assertEqual(with_event_digest(event), validate_sealed_event(with_event_digest(event)))

    def test_preserves_nonconforming_successor_arrays_and_ids(self) -> None:
        invalid = (
            [], [""], [" "], ["CA-O-101 "], ["CA-O-101.md"], ["folder/CA-O-101"],
            ["CA-O-101@1"], ["CA-O-101-SCOPE--summary"], ["CA-X-101"],
            ["CAPRMEDIO-META-METH-101"], ["CA-O-101", "CA-O-101"], ["CA-M-224"],
            ["CA--O-101"], ["CA---O-101"], ["CA_-O-101"], ["C--A-O-101"],
        )
        for successors in invalid:
            with self.subTest(successors=successors):
                event = self.event()
                event["successor_atom_ids"] = successors
                self.assertEqual(with_event_digest(event), validate_sealed_event(with_event_digest(event)))

    def test_rejects_replacement_values_with_wrong_storage_types(self) -> None:
        for predecessor in (None, 224, True, [], {}):
            with self.subTest(predecessor=predecessor):
                event = self.event()
                event["predecessor_atom_id"] = predecessor
                self.assert_invalid(event, "predecessor_atom_id")
        for successors in (None, "CA-O-101", ("CA-O-101",), {}, [None], [False], [101], [[]], [{}]):
            with self.subTest(successors=successors):
                event = self.event()
                event["successor_atom_ids"] = successors
                self.assert_invalid(event, "successor_atom_ids")

    def test_rejects_schema_two_and_recovered_payloads(self) -> None:
        event = self.event()
        event.update(schema_version=2, kind="governed_file_change")
        event.pop("subject_kind")
        self.assert_invalid(event, "replacement.*schema-v3 completed file MOVE")
        event = self.event()
        self.recover(event)
        self.assert_invalid(event, "replacement.*schema-v3 completed file MOVE")
        event = self.event()
        event["schema_version"] = 3.0
        self.assert_invalid(event, "replacement.*schema-v3 completed file MOVE")

    def test_rejects_folder_replacement(self) -> None:
        event = self.event()
        event["subject_kind"] = "folder"
        result = event["result"]
        result["entries"] = [{"path": f"{result['path']}/entry.txt", "sha256": sha("entry")}]
        result["sha256"] = canonical_json_digest([{"path": "entry.txt", "sha256": sha("entry")}])
        self.assert_invalid(event, "replacement.*schema-v3 completed file MOVE")

    def test_accepts_replacement_move_with_lifecycle_metadata_update(self) -> None:
        event = self.event()
        event["action_type"] = "MOVE+UPDATE"
        event["result"]["sha256"] = sha("predecessor with Archived status and refreshed updated_at")
        sealed = with_event_digest(event)
        self.assertEqual(sealed, validate_sealed_event(sealed))
        self.assertEqual(12, sealed["result"]["version"])

    def test_replacement_move_update_preserves_nonconforming_placement(self) -> None:
        event = self.event()
        event["action_type"] = "MOVE+UPDATE"
        event["result"]["path"] = f"active/{event['result']['filename']}"
        sealed = with_event_digest(event)
        self.assertEqual(sealed, validate_sealed_event(sealed))

    def test_rejects_each_non_move_action(self) -> None:
        for action in ("ADD", "UPDATE", "REMOVE"):
            with self.subTest(action=action):
                event = self.event()
                event["action_type"] = action
                if action == "ADD":
                    event.pop("previous_result_event")
                self.assert_invalid(event, "replacement.*schema-v3 completed file MOVE")

    def test_preserves_nonconforming_result_state_and_placement(self) -> None:
        event = self.event()
        event["result"]["state"] = "removed"
        for key in ("path", "sha256"):
            event["result"].pop(key)
        sealed = with_event_digest(event)
        self.assertEqual(sealed, validate_sealed_event(sealed))
        for directory in ("active", "archived", "not-archive", "Archive"):
            with self.subTest(directory=directory):
                event = self.event()
                event["result"]["path"] = f"{directory}/{event['result']['filename']}"
                sealed = with_event_digest(event)
                self.assertEqual(sealed, validate_sealed_event(sealed))

    def test_preserves_filename_mismatched_replacement_identity(self) -> None:
        filenames = (
            "CA-M-225-SCOPE--summary@12.md", "CA-M-2240-SCOPE--summary@12.md",
            "NOT-CA-M-224-SCOPE--summary@12.md", "CA-M-224garbage@12.md",
            "CAPRMEDIO-META-METH-224--summary@12.md", "artifact@12.md",
        )
        for filename in filenames:
            with self.subTest(filename=filename):
                event = self.event()
                self.set_filename(event, filename)
                sealed = with_event_digest(event)
                self.assertEqual(sealed, validate_sealed_event(sealed))

    def test_preserves_nonconforming_archive_filename_suffix(self) -> None:
        filenames = (
            "CA-M-224-SCOPE--summary.md", "CA-M-224-SCOPE--summary@11.md",
            "CA-M-224-SCOPE--summary@012.md", "CA-M-224-SCOPE--summary@12.md.md",
            "CA-M-224-SCOPE--summary@12.MD", "CA-M-224-SCOPE--summary@1@12.md",
        )
        for filename in filenames:
            with self.subTest(filename=filename):
                event = self.event()
                self.set_filename(event, filename)
                sealed = with_event_digest(event)
                self.assertEqual(sealed, validate_sealed_event(sealed))

    def test_rejects_result_version_with_non_integer_or_nonpositive_storage_value(self) -> None:
        for version in (True, "12", None, 0, -1):
            with self.subTest(version=version):
                event = self.event()
                event["result"]["version"] = version
                self.assert_invalid(event, "result.version")

    def test_preserves_result_path_filename_mismatch(self) -> None:
        event = self.event()
        event["result"]["path"] = ".caprmedio_caprmedio/05_method/archive/other@12.md"
        sealed = with_event_digest(event)
        self.assertEqual(sealed, validate_sealed_event(sealed))

    def test_rejects_digest_tampering_after_successors_change(self) -> None:
        for successors in (["CA-O-103"], ["CA-O-102", "CA-O-101"]):
            with self.subTest(successors=successors):
                event = self.event()
                event["successor_atom_ids"] = successors
                self.assertNotEqual(event["event_digest"], event_digest(event))
                with self.assertRaises(WorkJournalError) as raised:
                    validate_sealed_event(event)
                self.assertEqual("event-digest-mismatch", raised.exception.code)
        event = self.event()
        event["predecessor_atom_id"] = "CA-M-225"
        self.assertNotEqual(event["event_digest"], event_digest(event))

    def test_ordinary_and_legacy_events_retain_exact_bytes_without_payload(self) -> None:
        for schema in (2, 3):
            for lifecycle in ("completed", "recovered"):
                for action in ("ADD", "MOVE", "UPDATE", "MOVE+UPDATE", "REMOVE"):
                    with self.subTest(schema=schema, lifecycle=lifecycle, action=action):
                        event = self.event()
                        event.pop("predecessor_atom_id")
                        event.pop("successor_atom_ids")
                        event["action_type"] = action
                        self.set_filename(event, "CAPRMEDIO-META-METH-224--legacy.md")
                        if action == "ADD":
                            event.pop("previous_result_event")
                        if lifecycle == "recovered":
                            # Recovery has no change fields, including an ADD predecessor.
                            event.setdefault("previous_result_event", "prior-event")
                            self.recover(event)
                        if schema == 2:
                            event["schema_version"] = 2
                            event["kind"] = "governed_file_change" if lifecycle == "completed" else "governed_file_state"
                            event.pop("subject_kind")
                        sealed = with_event_digest(event)
                        self.assertEqual(canonical_json_bytes(sealed), canonical_json_bytes(validate_sealed_event(sealed)))

    def test_repeated_replacement_append_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True) as directory:
            root = Path(directory)
            control = root / ".caprmedio_caprmedio"
            control.mkdir()
            (control / "caprmedio_project_settings.toml").write_text(
                '[paths]\ncontrol_root = ".caprmedio_caprmedio"\njournal_root = ".caprmedio_caprmedio/_journal"\n', encoding="utf-8"
            )
            event = self.event()
            partition = {"author": "test-user", "local_date": "2026-09-14", "timezone": "Asia/Tbilisi"}
            first = append_sealed_events(root, [event], **partition)
            second = append_sealed_events(root, [event], **partition)
            self.assertEqual(first, second)
            carrier = root / first[0]["carrier"]
            self.assertEqual(canonical_json_bytes(event) + b"\n", carrier.read_bytes())
            changed = copy.deepcopy(event)
            changed["successor_atom_ids"] = ["CA-O-103"]
            with self.assertRaises(WorkJournalError) as raised:
                append_sealed_events(root, [with_event_digest(changed)], **partition)
            self.assertEqual("identity-collision", raised.exception.code)
            self.assertEqual(canonical_json_bytes(event) + b"\n", carrier.read_bytes())


    def test_ordinary_folder_and_removed_results_remain_supported(self) -> None:
        event = self.event()
        event.pop("predecessor_atom_id")
        event.pop("successor_atom_ids")
        event["subject_kind"] = "folder"
        event["result"] = {
            "state": "present",
            "filename": "source",
            "version": 1,
            "path": "source",
            "entries": [{"path": "source/entry.txt", "sha256": sha("entry")}],
            "sha256": canonical_json_digest([{"path": "entry.txt", "sha256": sha("entry")}]),
        }
        sealed = with_event_digest(event)
        self.assertEqual(sealed, validate_sealed_event(sealed))
        for subject_kind in ("file", "folder"):
            with self.subTest(subject_kind=subject_kind):
                event["subject_kind"] = subject_kind
                event["action_type"] = "REMOVE"
                event["result"] = {"state": "removed", "filename": "source", "version": 1}
                sealed = with_event_digest(event)
                self.assertEqual(sealed, validate_sealed_event(sealed))


if __name__ == "__main__":
    unittest.main()
