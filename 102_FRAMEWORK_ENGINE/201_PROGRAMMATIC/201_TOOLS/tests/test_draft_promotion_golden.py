"""Focused D570 native Draft-promotion evidence and zero-effect coverage."""
from __future__ import annotations

from pathlib import Path
import copy
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / "tests")]

from atom_operations import atom_digest, atom_from_path, draft_revision_lineage, replace_draft_revision_lineage, scan_atoms  # noqa: E402
from lifecycle_intents import LifecycleError, carrier_descriptor, update_atom_action  # noqa: E402
from draft_history import append_draft_entry, reserve_history_entry  # noqa: E402
from draft_promotion_pending import lookup_pending_promotion  # noqa: E402
import test_model_driven_status_lifecycle as fixture_module  # noqa: E402


class DraftPromotionGoldenTest(unittest.TestCase):
    def setUp(self) -> None:
        fixture_module.ModelDrivenStatusLifecycleTest.setUpClass()
        self.fixture = fixture_module.ModelDrivenStatusLifecycleTest("run")
        self.fixture.setUp()

    def tearDown(self) -> None:
        self.fixture.tearDown()

    def _demoted(self, number: int = 8000):
        path = self.fixture.atom("Requirement", "Active", number=number)
        demoted = self.fixture.execute(self.fixture.request(path, "Draft"))
        return self.fixture.root / demoted["observed"]["path"], demoted

    def _fresh_draft(self, *, container: str | None = None):
        settings = self.fixture.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        settings_text = settings.read_text(encoding="utf-8")
        if "[artifacts.identity]" not in settings_text:
            settings.write_text(settings_text + "\n[artifacts.identity]\nproject_prefix = \"CA\"\n", encoding="utf-8")
        draft = self.fixture.atom("Requirement", "Draft", draft=True, container=container)
        text = draft.read_text(encoding="utf-8")
        front, content = text[4:].split("\n---\n", 1)
        head = reserve_history_entry(self.fixture.root)
        draft.write_text(
            "---\n" + replace_draft_revision_lineage(front, {"history_entry_ref": head}) + "\n---\n" + content,
            encoding="utf-8",
        )
        append_draft_entry(self.fixture.root, str(draft.relative_to(self.fixture.root)), reference=head, origin={"kind": "never_identified"})
        return draft, head

    def _history_count(self) -> int:
        return len(list((self.fixture.root / ".caprmedio_caprmedio/archive/_draft_history").glob("*.json")))

    def _draft_update(self, draft: Path, *, suffix: str) -> dict[str, object]:
        atom = atom_from_path(self.fixture.root, draft)
        return {
            "target": carrier_descriptor(self.fixture.root, atom),
            "proposed": {"frontmatter": atom.frontmatter, "content": atom.content + suffix},
            "change_class": "carrier_only",
        }

    def test_demote_restore_and_optional_history_evidence(self) -> None:
        draft, _ = self._demoted()
        request = self.fixture.request(draft, "Active")
        restored = self.fixture.execute(request)
        self.assertEqual("CA-R-8000", restored["observed"]["atom_id"])

    def test_retired_or_stale_evidence_and_live_identity_collision_are_zero_effect(self) -> None:
        draft, _ = self._demoted()
        request = self.fixture.request(draft, "Active")
        request["draft_identity_evidence"] = {"kind": "prior_identified_revision"}
        before = self.fixture.snapshot()
        with self.assertRaises(LifecycleError):
            self.fixture.execute(request)
        self.assertEqual(before, self.fixture.snapshot())

        request.pop("draft_identity_evidence")
        self.fixture.atom("Requirement", "Active", number=8000)
        collided = self.fixture.snapshot()
        with self.assertRaises(LifecycleError):
            self.fixture.execute(request)
        self.assertEqual(collided, self.fixture.snapshot())

    def test_non_direct_history_locator_and_unknown_marker_are_zero_effect(self) -> None:
        draft, _ = self._demoted()
        original = draft.read_text(encoding="utf-8")
        draft.write_text(original.replace('"history_entry_ref": {', '"history_entry_ref": {"extra": true, '), encoding="utf-8")
        before = self.fixture.snapshot()
        with self.assertRaises(LifecycleError):
            self.fixture.execute(self.fixture.request(draft, "Active"))
        self.assertEqual(before, self.fixture.snapshot())
        draft.write_text(original.replace('"history_revision"', '"retired_revision"'), encoding="utf-8")
        before = self.fixture.snapshot()
        with self.assertRaises(LifecycleError):
            self.fixture.execute(self.fixture.request(draft, "Active"))
        self.assertEqual(before, self.fixture.snapshot())

    def test_missing_forged_stale_and_summary_mismatch_are_zero_effect(self) -> None:
        for number, mutate in enumerate(("missing", "forged", "stale", "summary", "role", "extra"), start=8000):
            with self.subTest(mutate=mutate):
                if number != 8000:
                    self.fixture.tearDown()
                    self.fixture = fixture_module.ModelDrivenStatusLifecycleTest("run")
                    self.fixture.setUp()
                draft, _ = self._demoted(number)
                if mutate == "missing":
                    text = draft.read_text(encoding="utf-8").replace("revision_lineage:", "retired_lineage:")
                    draft.write_text(text, encoding="utf-8")
                elif mutate == "forged":
                    text = draft.read_text(encoding="utf-8").replace('"history_revision": "', '"history_revision": "f')
                    draft.write_text(text, encoding="utf-8")
                elif mutate == "stale":
                    text = draft.read_text(encoding="utf-8").replace('"path": "', '"path": "04_requirement/archive/')
                    draft.write_text(text, encoding="utf-8")
                elif mutate == "role":
                    text = draft.read_text(encoding="utf-8").replace("content_role: Requirement", "content_role: Plan")
                    draft.write_text(text, encoding="utf-8")
                elif mutate == "extra":
                    text = draft.read_text(encoding="utf-8").replace('"history_entry_ref": {', '"history_entry_ref": {"extra": true, ')
                    draft.write_text(text, encoding="utf-8")
                else:
                    text = draft.read_text(encoding="utf-8").replace("Golden immutable meaning", "Changed meaning")
                    draft.write_text(text, encoding="utf-8")
                before = self.fixture.snapshot()
                with self.assertRaises(LifecycleError):
                    self.fixture.execute(self.fixture.request(draft, "Active"))
                self.assertEqual(before, self.fixture.snapshot())

    def test_fresh_lineage_allocates_next_unused_and_collision_refuses(self) -> None:
        draft, _ = self._fresh_draft()
        promoted = self.fixture.execute(self.fixture.request(draft, "Active"))
        self.assertRegex(promoted["observed"]["atom_id"], r"^CA-R-[1-9][0-9]*$")

    def test_actual_finalization_failure_retries_reserved_output_without_second_identity(self) -> None:
        draft, head = self._fresh_draft()
        request = self.fixture.request(draft, "Active")
        lock_directory = self.fixture.root / ".caprmedio_caprmedio/.draft_promotion_locks"
        lock_directory.symlink_to(self.fixture.root, target_is_directory=True)
        first = self.fixture.execute(copy.deepcopy(request))
        self.assertEqual("pending", first["outcome"])
        self.assertEqual("finalization-failed", first["pending_promotion"]["repair_context"]["code"])
        sealed = lookup_pending_promotion(self.fixture.root, draft_path=request["target"]["path"], head=head)
        self.assertIsNotNone(sealed)
        planned_id = sealed["reservation"]["planned_atom_id"]
        self.assertEqual(planned_id, first["observed"]["atom_id"])
        self.assertEqual(1, self._history_count())

        lock_directory.unlink()
        retried = self.fixture.execute(copy.deepcopy(request))
        self.assertEqual("applied", retried["outcome"])
        self.assertEqual(planned_id, retried["observed"]["atom_id"])
        self.assertFalse(draft.exists())
        self.assertEqual(2, self._history_count())
        self.assertEqual(1, sum(atom.atom_id == planned_id for atom in scan_atoms(self.fixture.root)))

    def test_terminal_retry_after_old_draft_removal_is_idempotent(self) -> None:
        draft, _ = self._fresh_draft()
        request = self.fixture.request(draft, "Active")
        first = self.fixture.execute(copy.deepcopy(request))
        self.assertFalse(draft.exists())
        before = self.fixture.snapshot()
        retried = self.fixture.execute(copy.deepcopy(request))
        self.assertEqual(first["observed"], retried["observed"])
        self.assertEqual("terminal-promotion-retry", retried["effects"][0]["reason"])
        self.assertEqual(before, self.fixture.snapshot())

    def test_changed_request_origin_substitution_and_replay_refuse_without_effects(self) -> None:
        draft, head = self._fresh_draft()
        request = self.fixture.request(draft, "Active")
        lock_directory = self.fixture.root / ".caprmedio_caprmedio/.draft_promotion_locks"
        lock_directory.symlink_to(self.fixture.root, target_is_directory=True)
        self.fixture.execute(copy.deepcopy(request))
        lock_directory.unlink()

        changed = copy.deepcopy(request)
        changed["status"] = "Archived"
        before = self.fixture.snapshot()
        with self.assertRaisesRegex(LifecycleError, "different sealed request"):
            self.fixture.execute(changed)
        self.assertEqual(before, self.fixture.snapshot())

        other, other_head = self._fresh_draft(container="substituted-origin")
        original = draft.read_text(encoding="utf-8")
        substituted = replace_draft_revision_lineage(original[4:].split("\n---\n", 1)[0], {"history_entry_ref": other_head})
        draft.write_text("---\n" + substituted + "\n---\n" + original.split("\n---\n", 1)[1], encoding="utf-8")
        before = self.fixture.snapshot()
        with self.assertRaises(LifecycleError):
            self.fixture.execute(self.fixture.request(draft, "Active"))
        self.assertEqual(before, self.fixture.snapshot())

        # Restore the exact first head, complete it, then replay those old bytes.
        restored = replace_draft_revision_lineage(substituted, {"history_entry_ref": head})
        draft.write_text("---\n" + restored + "\n---\n" + original.split("\n---\n", 1)[1], encoding="utf-8")
        replay_request = self.fixture.request(draft, "Active")
        saved_bytes = draft.read_bytes()
        self.fixture.execute(copy.deepcopy(replay_request))
        self.assertFalse(draft.exists())
        draft.write_bytes(saved_bytes)
        before = self.fixture.snapshot()
        with self.assertRaises(LifecycleError):
            self.fixture.execute(copy.deepcopy(replay_request))
        self.assertEqual(before, self.fixture.snapshot())

    def test_draft_update_rejects_unrelated_and_replayed_current_heads_before_writing(self) -> None:
        draft_a, _ = self._fresh_draft(container="update-a")
        _, head_b = self._fresh_draft(container="update-b")
        original = draft_a.read_text(encoding="utf-8")
        front, content = original[4:].split("\n---\n", 1)
        draft_a.write_text(
            "---\n" + replace_draft_revision_lineage(front, {"history_entry_ref": head_b}) + "\n---\n" + content,
            encoding="utf-8",
        )
        before = self.fixture.snapshot()
        with self.assertRaisesRegex(LifecycleError, "own current retained-history head"):
            update_atom_action(self.fixture.root, self._draft_update(draft_a, suffix="\nUnrelated head update.\n"), execute=True, authorized=True)
        self.assertEqual(before, self.fixture.snapshot())

        replayed, first_head = self._fresh_draft(container="update-replayed")
        update_atom_action(self.fixture.root, self._draft_update(replayed, suffix="\nFirst update.\n"), execute=True, authorized=True)
        current = replayed.read_text(encoding="utf-8")
        front, content = current[4:].split("\n---\n", 1)
        replayed.write_text(
            "---\n" + replace_draft_revision_lineage(front, {"history_entry_ref": first_head}) + "\n---\n" + content,
            encoding="utf-8",
        )
        before = self.fixture.snapshot()
        with self.assertRaisesRegex(LifecycleError, "own current retained-history head"):
            update_atom_action(self.fixture.root, self._draft_update(replayed, suffix="\nReplayed head update.\n"), execute=True, authorized=True)
        self.assertEqual(before, self.fixture.snapshot())


if __name__ == "__main__":
    unittest.main()
