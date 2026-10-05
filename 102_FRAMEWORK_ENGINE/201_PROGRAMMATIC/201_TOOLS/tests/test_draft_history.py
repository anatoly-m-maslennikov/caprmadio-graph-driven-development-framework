"""Focused retained Draft-history primitive tests."""
from __future__ import annotations

import json
import multiprocessing
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import draft_history as history  # noqa: E402
from draft_history import (  # noqa: E402
    DraftHistoryError,
    append_draft_entry,
    append_promotion_successor,
    reserve_history_entry,
    validate_current_draft_head,
)


def _concurrent_promotion_append(root: str, head: dict[str, str], output_path: str, results: object) -> None:
    """Fork-safe worker used to prove the per-head promotion lock."""

    try:
        reference = append_promotion_successor(Path(root), head, output_path)
    except DraftHistoryError as error:
        results.put(("refused", str(error)))  # type: ignore[union-attr]
    else:
        results.put(("appended", reference))  # type: ignore[union-attr]


class DraftHistoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n', encoding="utf-8"
        )
        self.draft = control / "04_requirement" / "draft" / "draft--history.md"
        self.draft.parent.mkdir(parents=True)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _write_draft(self, ref: dict[str, str], body: str = "Meaning") -> None:
        self.draft.write_text(
            "---\ncontent_role: Requirement\nstatus: Draft\nrevision_lineage: "
            + json.dumps({"history_entry_ref": ref}, sort_keys=True)
            + f"\n---\n# Summary\n{body}\n",
            encoding="utf-8",
        )

    def test_reserved_reference_binds_exact_current_carrier_and_unique_head(self) -> None:
        ref = reserve_history_entry(self.root)
        self._write_draft(ref)
        self.assertEqual(
            ref,
            append_draft_entry(self.root, str(self.draft.relative_to(self.root)), reference=ref, origin={"kind": "never_identified"}),
        )
        self.assertEqual("never_identified", validate_current_draft_head(self.root, str(self.draft.relative_to(self.root)), ref)["origin"]["kind"])

        self._write_draft(ref, "Changed")
        with self.assertRaises(DraftHistoryError):
            validate_current_draft_head(self.root, str(self.draft.relative_to(self.root)), ref)

    def test_update_requires_exact_parent_and_inherited_basis(self) -> None:
        first = reserve_history_entry(self.root)
        self._write_draft(first)
        append_draft_entry(self.root, str(self.draft.relative_to(self.root)), reference=first, origin={"kind": "never_identified"})
        second = reserve_history_entry(self.root)
        self._write_draft(second, "Edited")
        with self.assertRaises(DraftHistoryError):
            append_draft_entry(
                self.root, str(self.draft.relative_to(self.root)), reference=second,
                origin={"kind": "draft_update"}, parent_history_entry_ref=first,
                direct_predecessor={"atom_id": "CA-R-1"},
            )

        # A never-identified chain has no identified predecessor and therefore cannot forge an update basis.
        self.assertFalse((self.root / second["path"]).exists())
        append_draft_entry(
            self.root, str(self.draft.relative_to(self.root)), reference=second,
            origin={"kind": "draft_update"}, parent_history_entry_ref=first,
        )
        self.assertEqual("draft_update", validate_current_draft_head(self.root, str(self.draft.relative_to(self.root)), second)["origin"]["kind"])

    def test_malformed_carrier_reference_and_untrusted_locator_fail_closed(self) -> None:
        ref = reserve_history_entry(self.root)
        self._write_draft({"history_revision": ref["history_revision"], "path": "archive/elsewhere.json"})
        with self.assertRaises(DraftHistoryError):
            append_draft_entry(self.root, str(self.draft.relative_to(self.root)), reference=ref, origin={"kind": "never_identified"})
        self.assertFalse((self.root / ref["path"]).exists())

    def test_demoted_basis_requires_actual_archived_predecessor(self) -> None:
        archived = self.root / ".caprmedio_caprmedio" / "04_requirement" / "archive" / "CA-R-1--history@2.md"
        archived.parent.mkdir(parents=True)
        archived.write_text("---\natom_id: CA-R-1\nversion: 2\n---\n# Summary\nHistory\n", encoding="utf-8")
        predecessor = {
            "atom_id": "CA-R-1", "version": 2, "content_role": "Requirement", "summary": "History",
            "digest": __import__("hashlib").sha256(archived.read_bytes()).hexdigest(),
            "immutable_locator": {"history_revision": 2, "path": str(archived.relative_to(self.root))},
        }
        ref = reserve_history_entry(self.root)
        self._write_draft(ref)
        append_draft_entry(
            self.root, str(self.draft.relative_to(self.root)), reference=ref,
            origin={"kind": "demoted_identified"}, direct_predecessor=predecessor,
        )
        self.assertEqual("demoted_identified", validate_current_draft_head(self.root, str(self.draft.relative_to(self.root)), ref)["origin"]["kind"])
        predecessor["immutable_locator"]["path"] = "04_requirement/active/CA-R-1--history.md"
        next_ref = reserve_history_entry(self.root)
        self._write_draft(next_ref, "next")
        with self.assertRaises(DraftHistoryError):
            append_draft_entry(
                self.root, str(self.draft.relative_to(self.root)), reference=next_ref,
                origin={"kind": "demoted_identified"}, direct_predecessor=predecessor,
            )

    def test_demoted_update_chain_repeats_observed_basis(self) -> None:
        archived = self.root / ".caprmedio_caprmedio" / "04_requirement" / "archive" / "CA-R-1--history@2.md"
        archived.parent.mkdir(parents=True)
        archived.write_text("---\natom_id: CA-R-1\nversion: 2\n---\n# Summary\nHistory\n", encoding="utf-8")
        predecessor = {"atom_id": "CA-R-1", "version": 2, "content_role": "Requirement", "summary": "History",
                       "digest": __import__("hashlib").sha256(archived.read_bytes()).hexdigest(),
                       "immutable_locator": {"history_revision": 2, "path": str(archived.relative_to(self.root))}}
        first = reserve_history_entry(self.root); self._write_draft(first)
        append_draft_entry(self.root, str(self.draft.relative_to(self.root)), reference=first,
                           origin={"kind": "demoted_identified"}, direct_predecessor=predecessor)
        second = reserve_history_entry(self.root); self._write_draft(second, "Updated")
        append_draft_entry(self.root, str(self.draft.relative_to(self.root)), reference=second,
                           origin={"kind": "draft_update"}, parent_history_entry_ref=first,
                           direct_predecessor=predecessor)
        self.assertEqual("draft_update", validate_current_draft_head(self.root, str(self.draft.relative_to(self.root)), second)["origin"]["kind"])

    def test_observed_promotion_successor_consumes_head(self) -> None:
        ref = reserve_history_entry(self.root)
        self._write_draft(ref)
        append_draft_entry(self.root, str(self.draft.relative_to(self.root)), reference=ref, origin={"kind": "never_identified"})
        output = self.root / ".caprmedio_caprmedio" / "04_requirement" / "active" / "CA-R-1--history.md"
        output.parent.mkdir(parents=True)
        output.write_text("---\natom_id: CA-R-1\n---\n# Summary\nMeaning\n", encoding="utf-8")
        successor = append_promotion_successor(self.root, ref, str(output.relative_to(self.root)))
        self.assertTrue((self.root / successor["path"]).is_file())
        with self.assertRaises(DraftHistoryError):
            validate_current_draft_head(self.root, str(self.draft.relative_to(self.root)), ref)

    def test_concurrent_finalizers_append_one_child_for_one_head(self) -> None:
        """Force a second process to arrive while the first owns the head lock."""

        ref = reserve_history_entry(self.root)
        self._write_draft(ref)
        append_draft_entry(self.root, str(self.draft.relative_to(self.root)), reference=ref, origin={"kind": "never_identified"})
        output = self.root / ".caprmedio_caprmedio" / "04_requirement" / "active" / "CA-R-1--history.md"
        output.parent.mkdir(parents=True)
        output.write_text("---\natom_id: CA-R-1\n---\n# Summary\nMeaning\n", encoding="utf-8")

        context = multiprocessing.get_context("fork")
        entered = context.Event()
        release = context.Event()
        results = context.Queue()
        original = history._append_history_entry

        def hold_first_append(*args: object, **kwargs: object) -> None:
            entered.set()
            if not release.wait(timeout=5):
                raise RuntimeError("test did not release first finalizer")
            original(*args, **kwargs)

        with patch.object(history, "_append_history_entry", side_effect=hold_first_append):
            first = context.Process(target=_concurrent_promotion_append, args=(str(self.root), ref, str(output.relative_to(self.root)), results))
            first.start()
            self.assertTrue(entered.wait(timeout=5))
            second = context.Process(target=_concurrent_promotion_append, args=(str(self.root), ref, str(output.relative_to(self.root)), results))
            second.start()
            release.set()
            first.join(timeout=5)
            second.join(timeout=5)

        self.assertEqual((0, 0), (first.exitcode, second.exitcode))
        outcomes = [results.get(timeout=2), results.get(timeout=2)]
        self.assertEqual(["appended", "appended"], sorted(kind for kind, _ in outcomes))
        self.assertEqual(1, len({value["history_revision"] for _, value in outcomes}))
        archive = self.root / ".caprmedio_caprmedio" / "archive" / "_draft_history"
        entries = list(archive.glob("*.json"))
        self.assertEqual(2, len(entries))
        children = [json.loads(path.read_text(encoding="utf-8")) for path in entries]
        self.assertEqual(1, sum(entry.get("parent_history_entry_ref") == ref for entry in children))

    def test_symlinked_archive_is_refused_before_reservation_writes(self) -> None:
        outside = self.root / "outside"
        outside.mkdir()
        archive = self.root / ".caprmedio_caprmedio" / "archive"
        os.symlink(outside, archive)
        with self.assertRaises(DraftHistoryError):
            reserve_history_entry(self.root)
        self.assertFalse((outside / "_draft_history").exists())


if __name__ == "__main__":
    unittest.main()
