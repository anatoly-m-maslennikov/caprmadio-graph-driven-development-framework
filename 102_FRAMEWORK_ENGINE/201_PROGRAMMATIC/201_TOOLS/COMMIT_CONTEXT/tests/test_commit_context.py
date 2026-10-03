from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
for _parent in Path(__file__).resolve().parents:
    if _parent.name == ".caprmedio":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
sys.path.insert(0, str(TOOL_DIRECTORY))

from commit_context_logic import ContextError, derive_identity, digest, gather_context, repository_identity, validate_context  # noqa: E402

class IdentityTests(unittest.TestCase):
    def test_task_sequence_and_scope_are_not_identity(self) -> None:
        self.assertEqual("CA-P-095", derive_identity("03-CA-P-095-TASK--old.md", ""))
        self.assertEqual("CA-P-095", derive_identity("08-CA-P-095-TOOLS-TASK--new.md", ""))
        self.assertEqual("LEGACY-ID", derive_identity("CA-P-095-TASK--new.md", "atom_id: LEGACY-ID"))


class CommitContextTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".caprmedio").mkdir()
        (self.root / ".caprmedio_caprmedio").mkdir()
        (self.root / ".caprmedio_runtime").mkdir()
        (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            "[artifact_timestamps]\ntimezone = \"Asia/Tbilisi\"\n\n[paths]\njournal_root = \".caprmedio_caprmedio/work_journal\"\nruntime_root = \".caprmedio_runtime\"\n",
            encoding="utf-8",
        )
        self.git("init")
        self.git("config", "user.email", "test@example.com")
        self.git("config", "user.name", "Test Operator")
        self.git("config", "github.username", "anatoly-m-maslennikov")
        self.write_atom(".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--parent.md", version=1, relations={})
        self.git("add", ".")
        self.git("commit", "-m", "initial")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def git(self, *arguments: str) -> None:
        subprocess.run(["git", "-C", str(self.root), *arguments], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def write_atom(self, path: str, *, version: int, relations: dict[str, list[str]], body: str = "Body") -> None:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        relation_lines = "relations:\n" + "".join(f"  {kind}:\n" + "".join(f"    - {item}\n" for item in items) for kind, items in relations.items())
        target.write_text(f"---\nversion: {version}\n{relation_lines}---\n# {target.stem}\n\n{body}\n", encoding="utf-8")

    def trigger(self, before: str | None, after: str | None, *, observed_at: str = "2026-08-20T00:30:00+04:00") -> dict[str, object]:
        repository_id = repository_identity(self.root)
        adapter_id = "codex-test"
        source_event_id = "source-event-1"
        return {
            "schema_version": 1,
            "trigger_id": digest(
                {
                    "schema_version": 1,
                    "adapter_id": adapter_id,
                    "source_event_id": source_event_id,
                    "repository_id": repository_id,
                }
            ),
            "adapter": {"id": adapter_id},
            "source_event_id": source_event_id,
            "repository": {"root": str(self.root), "identity": repository_id},
            "observed_at": observed_at,
            "before_path": before,
            "after_path": after,
            "llm_session": {"app": "codex", "uuid": "019f591f-04f6-70f2-8de7-828b7cccc69d"},
        }

    def commit_subject(self, path: str, *, version: int = 1, relations: dict[str, list[str]] | None = None, body: str = "Body") -> None:
        self.write_atom(path, version=version, relations=relations or {"child_of": ["CA-R-001-REQUIREMENT--parent"]}, body=body)
        self.git("add", path)
        self.git("commit", "-m", "subject")

    def test_add_is_read_only_and_resolves_relations(self) -> None:
        path = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--child.md"
        self.write_atom(path, version=1, relations={"child_of": ["CA-R-001-REQUIREMENT--parent"]})
        before = subprocess.run(["git", "-C", str(self.root), "status", "--porcelain=v1"], check=True, stdout=subprocess.PIPE).stdout
        context = gather_context(self.root, self.trigger(None, path))
        after = subprocess.run(["git", "-C", str(self.root), "status", "--porcelain=v1"], check=True, stdout=subprocess.PIPE).stdout
        self.assertEqual(before, after)
        self.assertEqual("ADD", context["action_type"])
        self.assertEqual([{"relation_type": "child_of", "filename": "CA-R-001-REQUIREMENT--parent.md", "version": 1}], context["sources"])
        event = context["predictions"]["journal_records"][-1]
        self.assertNotIn("before_path", event)
        self.assertNotIn("action_message", event)
        self.assertEqual("2026-08-20", context["local_date"])
        self.assertEqual("anatoly-m-maslennikov", context["author"])
        self.assertEqual(
            ".caprmedio_caprmedio/work_journal/anatoly-m-maslennikov-2026-08-20-part-1.ndjson",
            context["predictions"]["journal_partitions"][0]["path"],
        )
        self.assertNotIn("previous_result_event", event)

    def test_graph_excludes_non_atom_markdown_lookalikes(self) -> None:
        narrative = self.root / ".caprmedio_caprmedio/README--CA-R-999.md"
        narrative.write_text("# Narrative document\n", encoding="utf-8")
        legacy = self.root / ".caprmedio_caprmedio/04_requirement/CA-R-999-REQUIREMENT--legacy-packet.md"
        legacy.parent.mkdir(parents=True, exist_ok=True)
        legacy.write_text("+++\nversion = 1\n+++\n\n# Legacy packet\n", encoding="utf-8")
        malformed = self.root / ".caprmedio_caprmedio/04_requirement/CA-R-998-REQUIREMENT--malformed-lookalike.md"
        malformed.write_text("---\nversion: 1\nrelations: invalid\n---\n# Malformed lookalike\n", encoding="utf-8")
        path = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--child.md"
        self.write_atom(path, version=1, relations={"child_of": ["CA-R-001-REQUIREMENT--parent"]})

        context = gather_context(self.root, self.trigger(None, path))

        self.assertEqual("ADD", context["action_type"])
        self.assertEqual("CA-R-002-REQUIREMENT--child.md", context["result"]["filename"])

    def test_unrelated_duplicate_identity_does_not_block_logging(self) -> None:
        self.write_atom(
            ".caprmedio_caprmedio/04_requirement/CA-R-999-REQUIREMENT--first.md",
            version=1,
            relations={},
        )
        self.write_atom(
            ".caprmedio_caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-103_BSEED_LAYER_3_GOVERNANCE/04_requirement/CA-R-999-REQUIREMENT-BSEED_GOVERNANCE--second.md",
            version=1,
            relations={},
        )
        path = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--child.md"
        self.write_atom(path, version=1, relations={"child_of": ["CA-R-001-REQUIREMENT--parent"]})

        context = gather_context(self.root, self.trigger(None, path))

        self.assertEqual("ADD", context["action_type"])
        self.assertEqual(
            [{"relation_type": "child_of", "filename": "CA-R-001-REQUIREMENT--parent.md", "version": 1}],
            context["sources"],
        )

    def test_ordinary_project_file_uses_logger_revision_without_graph_requirements(self) -> None:
        path = "README.txt"
        (self.root / path).write_text("first\n", encoding="utf-8")
        added = gather_context(self.root, self.trigger(None, path))
        self.assertEqual("file", added["subject"]["kind"])
        self.assertEqual(1, added["result"]["version"])
        self.assertEqual([], added["sources"])

        self.git("add", path)
        self.git("commit", "-m", "ordinary fixture")
        (self.root / path).write_text("second\n", encoding="utf-8")
        updated = gather_context(self.root, self.trigger(path, path))
        self.assertEqual("UPDATE", updated["action_type"])
        self.assertEqual(2, updated["result"]["version"])

    def test_folder_context_seals_one_ordered_entry_set(self) -> None:
        folder = self.root / "src"
        folder.mkdir()
        (folder / "a.py").write_text("a = 1\n", encoding="utf-8")
        (folder / "b.py").write_text("b = 1\n", encoding="utf-8")
        self.git("add", "src")
        self.git("commit", "-m", "folder fixture")
        (folder / "a.py").write_text("a = 2\n", encoding="utf-8")
        (folder / "b.py").write_text("b = 2\n", encoding="utf-8")

        context = gather_context(self.root, self.trigger("src", "src"))

        self.assertEqual("folder", context["subject"]["kind"])
        self.assertEqual("UPDATE", context["action_type"])
        self.assertEqual(["src/a.py", "src/b.py"], [entry["path"] for entry in context["result"]["entries"]])
        self.assertEqual(2, context["result"]["version"])
        self.assertEqual([], context["sources"])

    def test_project_carrier_root_folder_excludes_configured_journal_subtree(self) -> None:
        subject = ".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--parent.md"
        self.write_atom(subject, version=2, relations={}, body="updated")
        journal = self.root / ".caprmedio_caprmedio/work_journal/fixture.ndjson"
        journal.parent.mkdir(parents=True)
        journal.write_text("", encoding="utf-8")

        context = gather_context(
            self.root,
            self.trigger(".caprmedio_caprmedio", ".caprmedio_caprmedio", observed_at="2026-08-20T00:31:00+04:00"),
        )

        self.assertEqual("folder", context["subject"]["kind"])
        self.assertEqual(".caprmedio_caprmedio", context["result"]["path"])
        self.assertTrue(context["result"]["entries"])
        self.assertFalse(
            any(entry["path"].startswith(".caprmedio_caprmedio/work_journal/") for entry in context["result"]["entries"])
        )

    def test_project_carrier_root_add_ignores_committed_journal_only_tree(self) -> None:
        self.git("rm", "--cached", ".caprmedio_caprmedio/caprmedio_project_settings.toml")
        self.git("rm", ".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--parent.md")
        journal = self.root / ".caprmedio_caprmedio/work_journal/fixture.ndjson"
        journal.parent.mkdir(parents=True)
        journal.write_text("{}\n", encoding="utf-8")
        self.git("add", ".caprmedio_caprmedio/work_journal/fixture.ndjson")
        self.git("commit", "-m", "journal-only project carrier root")
        subject = self.root / ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        subject.parent.mkdir(parents=True, exist_ok=True)
        subject.write_text("new governed content\n", encoding="utf-8")

        context = gather_context(self.root, self.trigger(None, ".caprmedio_caprmedio"))

        self.assertEqual("ADD", context["action_type"])
        self.assertEqual("folder", context["subject"]["kind"])
        result_paths = [entry["path"] for entry in context["result"]["entries"]]
        self.assertIn(subject.relative_to(self.root).as_posix(), result_paths)
        self.assertIn(".caprmedio_caprmedio/caprmedio_project_settings.toml", result_paths)
        self.assertFalse(any(path.startswith(".caprmedio_caprmedio/work_journal/") for path in result_paths))

    def test_legacy_migration_root_remains_an_admitted_subject(self) -> None:
        path = ".caprmedio/retained-history.md"
        target = self.root / path
        target.write_text("retained migration history\n", encoding="utf-8")

        context = gather_context(self.root, self.trigger(None, path))

        self.assertEqual("ADD", context["action_type"])
        self.assertEqual(path, context["result"]["path"])
        self.assertEqual("file", context["subject"]["kind"])

    def test_repeated_context_is_byte_identical_and_keeps_session_provenance_structured(self) -> None:
        path = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.write_atom(path, version=1, relations={})
        trigger = self.trigger(None, path)
        first = gather_context(self.root, trigger)
        second = gather_context(self.root, trigger)
        self.assertEqual(
            json.dumps(first, sort_keys=True, separators=(",", ":")),
            json.dumps(second, sort_keys=True, separators=(",", ":")),
        )
        event = first["predictions"]["journal_records"][-1]
        self.assertEqual({"app": "codex", "uuid": "019f591f-04f6-70f2-8de7-828b7cccc69d"}, event["llm_session"])
        self.assertNotIn("session_id", event)
        self.assertNotIn("action_message", event)

    def test_subject_frontier_binds_selected_result_carrier_state(self) -> None:
        path = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.commit_subject(path, version=1, relations={})
        self.write_atom(path, version=2, relations={}, body="first update")
        first = gather_context(self.root, self.trigger(path, path))
        self.write_atom(path, version=3, relations={}, body="second update")
        second = gather_context(self.root, self.trigger(path, path))
        self.assertNotEqual(first["frontier"]["source_sha256"], second["frontier"]["source_sha256"])
        self.assertNotEqual(first["context_id"], second["context_id"])
        self.assertEqual(first["frontier"]["relations_sha256"], second["frontier"]["relations_sha256"])

    def test_relation_frontier_binds_target_content_version_and_path(self) -> None:
        path = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.write_atom(path, version=1, relations={"child_of": ["CA-R-001-REQUIREMENT--parent"]})
        first = gather_context(self.root, self.trigger(None, path))

        parent = ".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--parent.md"
        self.write_atom(parent, version=2, relations={}, body="revised parent")
        second = gather_context(self.root, self.trigger(None, path))
        self.assertEqual(first["frontier"]["source_sha256"], second["frontier"]["source_sha256"])
        self.assertNotEqual(first["frontier"]["relations_sha256"], second["frontier"]["relations_sha256"])

        moved_parent = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CA-R-001-REQUIREMENT--parent.md"
        (self.root / moved_parent).parent.mkdir(parents=True, exist_ok=True)
        os.replace(self.root / parent, self.root / moved_parent)
        third = gather_context(self.root, self.trigger(None, path))
        self.assertNotEqual(second["frontier"]["relations_sha256"], third["frontier"]["relations_sha256"])
        self.assertNotEqual(second["context_id"], third["context_id"])

    def test_action_classification_matrix(self) -> None:
        original = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.commit_subject(original, body="v1")

        self.write_atom(original, version=2, relations={"child_of": ["CA-R-001-REQUIREMENT--parent"]}, body="v2")
        self.assertEqual("UPDATE", gather_context(self.root, self.trigger(original, original))["action_type"])
        self.git("checkout", "--", original)

        renamed = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--renamed.md"
        (self.root / renamed).parent.mkdir(parents=True, exist_ok=True)
        os.replace(self.root / original, self.root / renamed)
        self.assertEqual("UPDATE", gather_context(self.root, self.trigger(original, renamed))["action_type"])
        self.git("checkout", "--", original)
        (self.root / renamed).unlink(missing_ok=True)

        moved = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        (self.root / moved).parent.mkdir(parents=True, exist_ok=True)
        os.replace(self.root / original, self.root / moved)
        self.assertEqual("MOVE", gather_context(self.root, self.trigger(original, moved))["action_type"])
        self.git("checkout", "--", original)
        shutil.rmtree((self.root / moved).parent.parent, ignore_errors=True)

        moved_updated = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CA-R-002-REQUIREMENT--changed.md"
        self.write_atom(moved_updated, version=2, relations={"child_of": ["CA-R-001-REQUIREMENT--parent"]}, body="v2")
        (self.root / original).unlink(missing_ok=True)
        self.assertEqual("MOVE+UPDATE", gather_context(self.root, self.trigger(original, moved_updated))["action_type"])

    def test_remove_creates_tombstone_and_recovery_baseline(self) -> None:
        path = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.commit_subject(path, version=3)
        (self.root / path).unlink()
        context = gather_context(self.root, self.trigger(path, None))
        self.assertEqual("REMOVE", context["action_type"])
        self.assertEqual({"state": "removed", "filename": "CA-R-002-REQUIREMENT--subject.md", "version": 3}, context["result"])
        self.assertIn("recovery", context)
        self.assertEqual([], context["recovery"]["contradictions"])
        self.assertEqual("recovered", context["predictions"]["journal_records"][0]["event"])

    def test_no_change_fails_closed(self) -> None:
        path = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.commit_subject(path)
        with self.assertRaisesRegex(ContextError, "no lifecycle") as captured:
            gather_context(self.root, self.trigger(path, path))
        self.assertEqual("no_governed_file_change", captured.exception.code)

    def test_non_current_upstream_version_is_logged_as_a_diagnostic(self) -> None:
        path = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.write_atom(path, version=1, relations={"child_of": ["CA-R-001-REQUIREMENT--parent@2"]})

        context = gather_context(self.root, self.trigger(None, path))

        self.assertEqual("ADD", context["action_type"])
        self.assertEqual(1, context["sources"][0]["version"])
        self.assertIn(
            "relation_target_version_differs",
            [diagnostic["code"] for diagnostic in context["validation"]["diagnostics"]],
        )

    def test_trigger_and_repository_identities_are_verified(self) -> None:
        path = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.write_atom(path, version=1, relations={})
        invalid_repository = self.trigger(None, path)
        invalid_repository["repository"] = {"root": str(self.root), "identity": "0" * 64}
        with self.assertRaises(ContextError) as captured:
            gather_context(self.root, invalid_repository)
        self.assertEqual("trigger_repository_identity_mismatch", captured.exception.code)

        invalid_trigger = self.trigger(None, path)
        invalid_trigger["trigger_id"] = "0" * 64
        with self.assertRaises(ContextError) as captured:
            gather_context(self.root, invalid_trigger)
        self.assertEqual("trigger_id_mismatch", captured.exception.code)

    def test_validate_context_rejects_changed_sealed_fields(self) -> None:
        path = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.write_atom(path, version=1, relations={})
        context = gather_context(self.root, self.trigger(None, path))
        validate_context(context)
        corrupted = dict(context)
        corrupted["author"] = "different-operator"
        with self.assertRaises(ContextError) as captured:
            validate_context(corrupted)
        self.assertEqual("context_identity_mismatch", captured.exception.code)

    def test_cli_machine_envelopes(self) -> None:
        path = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.write_atom(path, version=1, relations={})
        script = TOOL_DIRECTORY / "commit_context.py"
        trigger_file = self.root / "trigger.json"
        trigger_file.write_text(json.dumps(self.trigger(None, path)), encoding="utf-8")
        valid = subprocess.run(
            [sys.executable, str(script), "--repository", str(self.root), "run", "--input", str(trigger_file)],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        envelope = json.loads(valid.stdout)
        self.assertEqual(0, valid.returncode, valid.stderr)
        self.assertTrue(envelope["ok"])
        self.assertEqual("finder", envelope["tool"]["kind"])
        invalid = subprocess.run(
            [sys.executable, str(script), "--repository", str(self.root), "run", "--input", str(self.root / "missing.json")],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.assertEqual(2, invalid.returncode)
        self.assertFalse(json.loads(invalid.stdout)["ok"])


if __name__ == "__main__":
    unittest.main()
