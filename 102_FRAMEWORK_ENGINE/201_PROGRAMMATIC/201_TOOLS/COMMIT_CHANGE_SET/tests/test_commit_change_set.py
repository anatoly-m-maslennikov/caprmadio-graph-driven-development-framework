"""Deterministic acceptance tests for COMMIT_CHANGE_SET Evaluations E179, E196-E204, and E211-E213."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


SCRIPT = Path(__file__).resolve().parents[1] / "commit_change_set.py"
SPEC = importlib.util.spec_from_file_location("commit_change_set", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
commit_change_set = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = commit_change_set
SPEC.loader.exec_module(commit_change_set)
UNSET = object()

class CommitChangeSetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".caprmedio").mkdir()
        (self.root / ".caprmedio_caprmedio").mkdir()
        (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            "[artifact_timestamps]\ntimezone = \"Asia/Tbilisi\"\n\n[paths]\njournal_root = \".caprmedio_caprmedio/work_journal\"\nruntime_root = \".caprmedio_runtime\"\n",
            encoding="utf-8",
        )
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "CAPRMEDIO Test")
        self.git("config", "github.username", "anatoly-m-maslennikov")
        self.write_atom(".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--parent.md", version=1, relations={})
        self.write_atom(
            ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md",
            version=1,
            relations={"child_of": ["CA-R-001-REQUIREMENT--parent"]},
            body="first",
        )
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        self.subject = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.write_atom(self.subject, version=2, relations={"child_of": ["CA-R-001-REQUIREMENT--parent"]}, body="second")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def git(self, *arguments: str) -> str:
        return subprocess.run(["git", "-C", str(self.root), *arguments], check=True, capture_output=True, text=True).stdout

    def write_atom(self, path: str, *, version: int, relations: dict[str, list[str]], body: str = "Body") -> None:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        relation_lines = "relations:\n" + "".join(
            f"  {kind}:\n" + "".join(f"    - {item}\n" for item in values) for kind, values in relations.items()
        )
        target.write_text(f"---\nversion: {version}\n{relation_lines}---\n# {target.stem}\n\n{body}\n", encoding="utf-8")

    def trigger(self, before_path: object = UNSET, after_path: object = UNSET, *, source_event_id: str = "source-event-1") -> dict[str, object]:
        git_directory = (self.root / self.git("rev-parse", "--git-dir").strip()).resolve()
        repository_identity = hashlib.sha256(
            json.dumps(
                {"repository_root": self.root.resolve().as_posix(), "git_directory": git_directory.as_posix()},
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        adapter_id = "codex-test"
        trigger_id = hashlib.sha256(
            json.dumps(
                {
                    "schema_version": 1,
                    "adapter_id": adapter_id,
                    "source_event_id": source_event_id,
                    "repository_id": repository_identity,
                },
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        return {
            "schema_version": 1,
            "trigger_id": trigger_id,
            "adapter": {"id": adapter_id},
            "source_event_id": source_event_id,
            "repository": {"root": str(self.root), "identity": repository_identity},
            "observed_at": "2026-08-20T20:21:22Z",
            "before_path": self.subject if before_path is UNSET else before_path,
            "after_path": self.subject if after_path is UNSET else after_path,
            "llm_session": {"app": "codex", "uuid": "019f591f-04f6-70f2-8de7-828b7cccc69d"},
        }

    def snapshot(self) -> dict[str, object]:
        def files(path: Path) -> dict[str, str]:
            if not path.exists():
                return {}
            return {
                item.relative_to(self.root).as_posix(): hashlib.sha256(item.read_bytes()).hexdigest()
                for item in sorted(path.rglob("*"))
                if item.is_file()
            }

        return {
            "status": self.git("status", "--porcelain=v1"),
            "index": (self.root / ".git/index").read_bytes(),
            "head": self.git("rev-parse", "HEAD").strip(),
            "runtime": files(self.root / ".caprmedio_runtime"),
            "journal": files(self.root / ".caprmedio_caprmedio/work_journal"),
        }

    def append_only(self) -> tuple[dict[str, object], dict[str, object]]:
        context = commit_change_set.gather_context(self.root, self.trigger())
        appender = commit_change_set._import_appender()
        envelope = appender.run(self.root, {"context": context}, apply=True, wait_seconds=0)
        self.assertTrue(envelope["ok"])
        return context, envelope["result"]

    def stage_appended(self) -> dict[str, object]:
        context, appended = self.append_only()
        events = context["predictions"]["journal_records"]
        commit_change_set._stage_subject(self.root, context)
        commit_change_set._stage_receipt_sidecars(self.root, events, appended["receipts"])
        return context

    def committed_without_release(self) -> tuple[dict[str, object], dict[str, object]]:
        """Model the historical crash after Git commit but before lease release."""
        self.git("checkout", "--", self.subject)
        added = "added.txt"
        (self.root / added).write_text("new governed file\n", encoding="utf-8")
        context = commit_change_set.gather_context(self.root, self.trigger(None, added, source_event_id="recovery-add"))
        appender = commit_change_set._import_appender()
        envelope = appender.run(self.root, {"context": context}, apply=True, wait_seconds=0)
        self.assertTrue(envelope["ok"])
        appended = envelope["result"]
        events = context["predictions"]["journal_records"]
        commit_change_set._stage_subject(self.root, context)
        commit_change_set._stage_receipt_sidecars(self.root, events, appended["receipts"])
        self.git("commit", "-qm", commit_change_set._render_message(context, events))
        return context, json.loads((self.root / ".caprmedio_runtime/state/commit_change_set/lease.json").read_text(encoding="utf-8"))

    def recovery_kwargs(self, context: dict[str, object], lease: dict[str, object], **overrides: object) -> dict[str, object]:
        kwargs: dict[str, object] = {
            "action_id": context["action_id"],
            "event_ids": [event["event_id"] for event in context["predictions"]["journal_records"]],
            "committed_revision": self.git("rev-parse", "HEAD").strip(),
            "operator_approval": "operator approved recovery test",
            "lease_token": lease["lease_token"],
            "context_id": lease["context_id"],
            "context_digest": lease["context_digest"],
        }
        kwargs.update(overrides)
        return kwargs

    def test_e179_dry_run_is_fully_mutation_free(self) -> None:
        before = self.snapshot()
        result = commit_change_set.run(self.root, {"trigger": self.trigger()}, apply=False, wait_seconds=0)
        self.assertEqual(before, self.snapshot())
        self.assertEqual("UPDATE", result["change_set"]["action_type"])
        self.assertTrue(result["journal_records"])
        self.assertTrue(result["git_message"])
        self.assertEqual("available", result["lease"]["status"])

    def test_e199_commits_subject_and_only_receipt_bound_sidecars(self) -> None:
        result = commit_change_set.run(self.root, {"trigger": self.trigger()}, apply=True, wait_seconds=0)
        changed = set(self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").splitlines())
        self.assertIn(self.subject, changed)
        self.assertEqual(2, len(changed), changed)
        journal = next(path for path in changed if path.endswith(".ndjson"))
        records = [json.loads(line) for line in (self.root / journal).read_text(encoding="utf-8").splitlines()]
        self.assertEqual([receipt["event_id"] for receipt in result["receipts"]], [record["event_id"] for record in records])
        self.assertEqual(len(result["receipts"]), len(result["pipeline_correlations"]))
        self.assertEqual("released", result["lease"]["status"])
        self.assertFalse((self.root / ".caprmedio_runtime/state/commit_change_set/lease.json").exists())

    def test_e236_commits_one_folder_action_with_all_entries_and_one_event(self) -> None:
        self.git("checkout", "--", self.subject)
        folder = self.root / "src"
        folder.mkdir()
        (folder / "a.py").write_text("a = 1\n", encoding="utf-8")
        (folder / "b.py").write_text("b = 1\n", encoding="utf-8")
        self.git("add", "src")
        self.git("commit", "-qm", "folder fixture")
        (folder / "a.py").write_text("a = 2\n", encoding="utf-8")
        (folder / "b.py").write_text("b = 2\n", encoding="utf-8")

        result = commit_change_set.run(
            self.root,
            {"trigger": self.trigger("src", "src", source_event_id="folder-event")},
            apply=True,
            wait_seconds=0,
        )

        changed = set(self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").splitlines())
        self.assertEqual({"src/a.py", "src/b.py"}, {path for path in changed if not path.endswith(".ndjson")})
        journal = next(path for path in changed if path.endswith(".ndjson"))
        records = [json.loads(line) for line in (self.root / journal).read_text(encoding="utf-8").splitlines()]
        completed = [record for record in records if record.get("event") == "completed"]
        self.assertEqual(1, len(completed))
        self.assertEqual("folder", completed[0]["subject_kind"])
        self.assertEqual("governed_project_change", completed[0]["kind"])
        self.assertEqual("released", result["lease"]["status"])

    def test_project_carrier_root_folder_commits_journal_only_as_receipt_bound_sidecar(self) -> None:
        result = commit_change_set.run(
            self.root,
            {
                "trigger": self.trigger(
                    ".caprmedio_caprmedio",
                    ".caprmedio_caprmedio",
                    source_event_id="migrated-project-root-folder",
                )
            },
            apply=True,
            wait_seconds=0,
        )

        context = result["context"]
        self.assertEqual("folder", context["subject"]["kind"])
        self.assertEqual(".caprmedio_caprmedio", context["result"]["path"])
        self.assertFalse(
            any(entry["path"].startswith(".caprmedio_caprmedio/work_journal/") for entry in context["result"]["entries"])
        )
        changed = set(self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").splitlines())
        journals = {path for path in changed if path.startswith(".caprmedio_caprmedio/work_journal/")}
        subjects = changed - journals
        self.assertEqual({self.subject}, subjects)
        self.assertEqual(1, len(journals))
        self.assertEqual(
            journals,
            {receipt["carrier"] for receipt in result["receipts"]},
        )

    def test_commits_one_ordinary_project_file_without_graph_metadata(self) -> None:
        self.git("checkout", "--", self.subject)
        path = "notes.txt"
        (self.root / path).write_text("first\n", encoding="utf-8")
        self.git("add", path)
        self.git("commit", "-qm", "ordinary fixture")
        (self.root / path).write_text("second\n", encoding="utf-8")

        result = commit_change_set.run(
            self.root,
            {"trigger": self.trigger(path, path, source_event_id="ordinary-file-event")},
            apply=True,
            wait_seconds=0,
        )

        changed = set(self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").splitlines())
        self.assertIn(path, changed)
        completed = result["context"]["predictions"]["journal_records"][-1]
        self.assertEqual("file", completed["subject_kind"])
        self.assertEqual([], completed["sources"])
        self.assertEqual(2, completed["result"]["version"])

    def test_folder_lifecycle_actions_each_remain_one_commit_and_event(self) -> None:
        self.git("checkout", "--", self.subject)
        folder = self.root / "src/pkg"
        folder.mkdir(parents=True)
        (folder / ".gitkeep").write_bytes(b"")
        (folder / "a.py").write_text("a = 1\n", encoding="utf-8")
        (folder / "b.py").write_text("b = 1\n", encoding="utf-8")
        cases = [
            (None, "src/pkg", "folder-add", "ADD", 1),
            ("src/pkg", "lib/pkg", "folder-move", "MOVE", 2),
            ("lib/pkg", "lib/pkg", "folder-update", "UPDATE", 3),
            ("lib/pkg", None, "folder-remove", "REMOVE", 3),
        ]
        for before, after, event_id, expected_action, expected_version in cases:
            if event_id == "folder-move":
                destination = self.root / "lib/pkg"
                destination.mkdir(parents=True)
                for carrier in sorted((self.root / "src/pkg").iterdir()):
                    carrier.replace(destination / carrier.name)
            elif event_id == "folder-update":
                (self.root / "lib/pkg/a.py").write_text("a = 2\n", encoding="utf-8")
                (self.root / "lib/pkg/b.py").write_text("b = 2\n", encoding="utf-8")
            elif event_id == "folder-remove":
                for carrier in sorted((self.root / "lib/pkg").iterdir()):
                    carrier.unlink()
            result = commit_change_set.run(
                self.root,
                {"trigger": self.trigger(before, after, source_event_id=event_id)},
                apply=True,
                wait_seconds=0,
            )
            context = result["context"]
            self.assertEqual(expected_action, context["action_type"])
            self.assertEqual(expected_version, context["result"]["version"])
            self.assertEqual("folder", context["subject"]["kind"])
            self.assertEqual(1, len([record for record in context["predictions"]["journal_records"] if record["event"] == "completed"]))

    def test_e196_rejects_missing_receipts_without_runtime_mutation(self) -> None:
        context = commit_change_set.gather_context(self.root, self.trigger())
        before = self.snapshot()
        with self.assertRaisesRegex(commit_change_set.ToolError, "receipt") as captured:
            commit_change_set.run(self.root, {"context": context, "receipts": [], "lease": {}}, apply=True, wait_seconds=0)
        self.assertEqual("receipt-set-incomplete", captured.exception.code)
        self.assertEqual(before, self.snapshot())

    def test_e203_preserves_unrelated_staged_change_after_append(self) -> None:
        context, appended = self.append_only()
        unrelated = self.root / "unrelated.txt"
        unrelated.write_text("unrelated\n", encoding="utf-8")
        self.git("add", "unrelated.txt")
        with self.assertRaisesRegex(commit_change_set.ToolError, "staged") as captured:
            commit_change_set.run(
                self.root,
                {"context": context, "receipts": appended["receipts"], "lease": appended["lease"]},
                apply=True,
                wait_seconds=0,
            )
        self.assertEqual("unrelated-staged-change", captured.exception.code)
        self.assertTrue((self.root / ".caprmedio_runtime/state/append_change_records/blocked" / f"{context['action_id']}.json").is_file())
        self.assertEqual("unrelated.txt\0", self.git("diff", "--cached", "--name-only", "-z"))

    def test_e202_preserves_blocked_action_when_git_base_becomes_stale_after_append(self) -> None:
        context, appended = self.append_only()
        (self.root / "other.txt").write_text("independent commit\n", encoding="utf-8")
        self.git("add", "other.txt")
        self.git("commit", "-qm", "independent")
        with self.assertRaisesRegex(commit_change_set.ToolError, "Git base") as captured:
            commit_change_set.run(
                self.root,
                {"context": context, "receipts": appended["receipts"], "lease": appended["lease"]},
                apply=True,
                wait_seconds=0,
            )
        self.assertEqual("stale-context", captured.exception.code)
        blocked = self.root / ".caprmedio_runtime/state/append_change_records/blocked" / f"{context['action_id']}.json"
        self.assertTrue(blocked.is_file())
        self.assertTrue((self.root / ".caprmedio_runtime/state/commit_change_set/lease.json").is_file())

    def test_e204_records_proven_corrupted_context_after_append(self) -> None:
        context, appended = self.append_only()
        corrupted = dict(context)
        corrupted.pop("result")
        with self.assertRaisesRegex(commit_change_set.ToolError, "result"):
            commit_change_set.run(
                self.root,
                {"context": corrupted, "receipts": appended["receipts"], "lease": appended["lease"]},
                apply=True,
                wait_seconds=0,
            )
        blocked = self.root / ".caprmedio_runtime/state/append_change_records/blocked" / f"{context['action_id']}.json"
        self.assertTrue(blocked.is_file())
        payload = json.loads(blocked.read_text(encoding="utf-8"))
        self.assertEqual("invalid-context", payload["reason"])
        self.assertEqual([receipt["event_id"] for receipt in appended["receipts"]], [row["event_id"] for row in payload["receipt_refs"]])

    def test_allows_exact_already_staged_subject(self) -> None:
        self.git("add", self.subject)
        context = commit_change_set.gather_context(self.root, self.trigger())
        appender = commit_change_set._import_appender()
        appended = appender.run(self.root, {"context": context}, apply=True, wait_seconds=0)["result"]
        result = commit_change_set.run(
            self.root,
            {"context": context, "receipts": appended["receipts"], "lease": appended["lease"]},
            apply=True,
            wait_seconds=0,
        )
        self.assertEqual("released", result["lease"]["status"])
        self.assertEqual([], self.git("diff", "--cached", "--name-only").splitlines())

    def test_recover_committed_dry_run_is_mutation_free_then_records_and_releases(self) -> None:
        context, lease = self.committed_without_release()
        kwargs = self.recovery_kwargs(context, lease)
        before = self.snapshot()
        dry_run = commit_change_set.recover_committed_action(self.root, apply=False, **kwargs)
        self.assertEqual(before, self.snapshot())
        self.assertEqual("predicted", dry_run["recovery_receipt"]["state"])

        applied = commit_change_set.recover_committed_action(self.root, apply=True, **kwargs)
        self.assertEqual("released", applied["lease"]["status"])
        self.assertFalse((self.root / ".caprmedio_runtime/state/commit_change_set/lease.json").exists())
        receipt = self.root / applied["recovery_receipt"]
        stored = json.loads(receipt.read_text(encoding="utf-8"))
        self.assertEqual(lease, stored["recovery"]["proof"]["lease"])
        replay = commit_change_set.recover_committed_action(self.root, apply=True, **kwargs)
        self.assertEqual("already-released", replay["lease"]["status"])

    def test_recover_committed_rejects_stale_result_without_runtime_mutation(self) -> None:
        context, lease = self.committed_without_release()
        (self.root / context["result"]["path"]).write_text("stale source\n", encoding="utf-8")
        before = self.snapshot()
        with self.assertRaises(commit_change_set.ToolError) as captured:
            commit_change_set.recover_committed_action(self.root, apply=True, **self.recovery_kwargs(context, lease))
        self.assertEqual("recovery-result-mismatch", captured.exception.code)
        self.assertEqual(before, self.snapshot())

    def test_recover_committed_rejects_stale_journal_without_runtime_mutation(self) -> None:
        context, lease = self.committed_without_release()
        journal = next((self.root / ".caprmedio_caprmedio/work_journal").glob("*.ndjson"))
        lines = journal.read_bytes().splitlines(keepends=True)
        lines[-1] = b" " + lines[-1]
        journal.write_bytes(b"".join(lines))
        before = self.snapshot()
        with self.assertRaises(commit_change_set.ToolError) as captured:
            commit_change_set.recover_committed_action(self.root, apply=True, **self.recovery_kwargs(context, lease))
        self.assertEqual("recovery-journal-mismatch", captured.exception.code)
        self.assertEqual(before, self.snapshot())

    def test_recover_committed_rejects_event_set_and_fingerprint_mismatch(self) -> None:
        context, lease = self.committed_without_release()
        wrong_event = "0" * 64
        before = self.snapshot()
        with self.assertRaisesRegex(commit_change_set.ToolError, "event ID set") as captured:
            commit_change_set.recover_committed_action(self.root, apply=True, **self.recovery_kwargs(context, lease, event_ids=[wrong_event]))
        self.assertEqual("lease-event-mismatch", captured.exception.code)
        self.assertEqual(before, self.snapshot())
        with self.assertRaisesRegex(commit_change_set.ToolError, "fingerprint") as captured:
            commit_change_set.recover_committed_action(self.root, apply=True, **self.recovery_kwargs(context, lease, lease_token="wrong-token"))
        self.assertEqual("lease-fingerprint-mismatch", captured.exception.code)
        self.assertEqual(before, self.snapshot())

    def test_recover_committed_rejects_nonancestor_or_missing_approval(self) -> None:
        context, lease = self.committed_without_release()
        orphan = self.git("commit-tree", "HEAD^{tree}", "-m", "orphan").strip()
        before = self.snapshot()
        with self.assertRaisesRegex(commit_change_set.ToolError, "not an ancestor") as captured:
            commit_change_set.recover_committed_action(self.root, apply=True, **self.recovery_kwargs(context, lease, committed_revision=orphan))
        self.assertEqual("recovery-commit-not-ancestor", captured.exception.code)
        self.assertEqual(before, self.snapshot())
        with self.assertRaisesRegex(commit_change_set.ToolError, "operator approval") as captured:
            commit_change_set.recover_committed_action(self.root, apply=True, **self.recovery_kwargs(context, lease, operator_approval=""))
        self.assertEqual("operator-approval-missing", captured.exception.code)
        self.assertEqual(before, self.snapshot())

    def test_recover_committed_rejects_tampered_receipt_and_preserves_lease_on_receipt_write_failure(self) -> None:
        context, lease = self.committed_without_release()
        kwargs = self.recovery_kwargs(context, lease)
        appender = commit_change_set._import_appender()
        with mock.patch.object(appender, "_atomic_json", side_effect=OSError("disk full")):
            with self.assertRaisesRegex(commit_change_set.ToolError, "disk full") as captured:
                commit_change_set.recover_committed_action(self.root, apply=True, **kwargs)
        self.assertEqual("recovery-release-failed", captured.exception.code)
        self.assertTrue((self.root / ".caprmedio_runtime/state/commit_change_set/lease.json").is_file())
        receipt_path = self.root / ".caprmedio_runtime/state/append_change_records/committed_recoveries" / f"{context['action_id']}.json"
        self.assertFalse(receipt_path.exists())

        applied = commit_change_set.recover_committed_action(self.root, apply=True, **kwargs)
        receipt_path.write_text("{}\n", encoding="utf-8")
        before = self.snapshot()
        with self.assertRaisesRegex(commit_change_set.ToolError, "receipt") as captured:
            commit_change_set.recover_committed_action(self.root, apply=True, **kwargs)
        self.assertEqual("invalid-runtime-state", captured.exception.code)
        self.assertEqual(before, self.snapshot())

    def test_e211_pre_commit_rejects_atom_without_journal(self) -> None:
        self.git("add", self.subject)
        before = self.snapshot()
        with self.assertRaisesRegex(commit_change_set.ToolError, "Journal") as captured:
            commit_change_set.evaluate_pre_commit(self.root)
        self.assertEqual("governed-journal-missing", captured.exception.code)
        self.assertEqual(before, self.snapshot())

    def test_e211_pre_commit_rejects_journal_without_atom(self) -> None:
        context, appended = self.append_only()
        commit_change_set._stage_receipt_sidecars(
            self.root,
            context["predictions"]["journal_records"],
            appended["receipts"],
        )
        before = self.snapshot()
        with self.assertRaisesRegex(commit_change_set.ToolError, "subject") as captured:
            commit_change_set.evaluate_pre_commit(self.root)
        self.assertEqual("governed-subject-missing", captured.exception.code)
        self.assertEqual(before, self.snapshot())

    def test_e211_pre_commit_rejects_second_governed_atom(self) -> None:
        self.stage_appended()
        parent = ".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--parent.md"
        self.write_atom(parent, version=2, relations={}, body="changed parent")
        self.git("add", parent)
        with self.assertRaisesRegex(commit_change_set.ToolError, "project paths") as captured:
            commit_change_set.evaluate_pre_commit(self.root)
        self.assertEqual("governed-subject-mismatch", captured.exception.code)

    def test_e211_pre_commit_rejects_git_whitespace_error(self) -> None:
        target = self.root / "ordinary.txt"
        target.write_text("trailing space \n", encoding="utf-8")
        self.git("add", target.name)
        with self.assertRaisesRegex(commit_change_set.ToolError, "whitespace") as captured:
            commit_change_set.evaluate_pre_commit(self.root)
        self.assertEqual("staged-content-invalid", captured.exception.code)

    def test_e216_pre_commit_rejects_runtime_and_temporary_state(self) -> None:
        for relative in (".caprmedio_runtime/state.toml", ".caprmedio_tmp/state.toml"):
            with self.subTest(relative=relative):
                carrier = self.root / relative
                carrier.parent.mkdir(parents=True, exist_ok=True)
                carrier.write_text("fixture = true\n", encoding="utf-8")
                self.git("add", "-f", relative)
                before = self.snapshot()
                with self.assertRaisesRegex(commit_change_set.ToolError, "cannot be part") as captured:
                    commit_change_set.evaluate_pre_commit(self.root)
                self.assertEqual("local-machine-path-staged", captured.exception.code)
                self.assertEqual(before, self.snapshot())
                self.git("reset", "-q", "HEAD", "--", relative)
                carrier.unlink()

    def test_e211_pre_commit_accepts_exact_subject_and_sidecars_read_only(self) -> None:
        self.stage_appended()
        before = self.snapshot()
        result = commit_change_set.evaluate_pre_commit(self.root)
        self.assertTrue(result["governed"])
        self.assertEqual([self.subject], result["subject_paths"])
        self.assertEqual(before, self.snapshot())

    def test_e212_commit_message_requires_exact_projection(self) -> None:
        context = self.stage_appended()
        message_path = self.root / ".git" / "COMMIT_EDITMSG"
        expected = context["predictions"]["git_message"]
        message_path.write_text(expected + "\n", encoding="utf-8")
        before = message_path.read_bytes()
        result = commit_change_set.evaluate_commit_message(self.root, message_path)
        self.assertTrue(result["message_valid"])
        self.assertEqual(before, message_path.read_bytes())

        message_path.write_text(expected + "\nextra body\n", encoding="utf-8")
        changed = message_path.read_bytes()
        with self.assertRaisesRegex(commit_change_set.ToolError, "message") as captured:
            commit_change_set.evaluate_commit_message(self.root, message_path)
        self.assertEqual("commit-message-mismatch", captured.exception.code)
        self.assertEqual(changed, message_path.read_bytes())

    def test_e213_post_commit_observes_once_without_governed_mutation(self) -> None:
        commit_change_set.run(self.root, {"trigger": self.trigger()}, apply=True, wait_seconds=0)
        head = self.git("rev-parse", "HEAD").strip()
        journal_before = {
            path.relative_to(self.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (self.root / ".caprmedio_caprmedio/work_journal").glob("*.ndjson")
        }

        first = commit_change_set.observe_post_commit(self.root)
        second = commit_change_set.observe_post_commit(self.root)

        self.assertTrue(first["valid"])
        self.assertTrue(first["governed"])
        self.assertTrue(first["observation_appended"])
        self.assertFalse(second["observation_appended"])
        log = self.root / first["observation"]
        self.assertEqual(1, len(log.read_text(encoding="utf-8").splitlines()))
        self.assertEqual(head, self.git("rev-parse", "HEAD").strip())
        self.assertEqual(
            journal_before,
            {
                path.relative_to(self.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in (self.root / ".caprmedio_caprmedio/work_journal").glob("*.ndjson")
            },
        )


if __name__ == "__main__":
    unittest.main()
