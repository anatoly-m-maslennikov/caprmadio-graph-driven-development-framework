"""Golden disposable-Project coverage for pending Draft-promotion recovery."""
from __future__ import annotations

import hashlib
import json
import multiprocessing
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import draft_promotion_pending as pending  # noqa: E402
import draft_history as history  # noqa: E402
from draft_history import (  # noqa: E402
    DraftHistoryError,
    append_draft_entry,
    reserve_history_entry,
    validate_current_draft_head,
)


def _concurrent_finalize(root: str, reservation: dict[str, object], results: object) -> None:
    try:
        outcome = finalize_pending_promotion(Path(root), reservation)
    except Exception as error:  # pragma: no cover - reported to the parent assertion
        results.put(("error", type(error).__name__, str(error)))  # type: ignore[union-attr]
    else:
        results.put(("result", outcome))  # type: ignore[union-attr]
from draft_promotion_pending import (  # noqa: E402
    PendingPromotionError,
    finalize_pending_promotion,
    lookup_pending_promotion,
    match_promotion_successor,
    pending_promotion_path,
    recover_pending_promotion,
    reserve_pending_promotion,
)


class PendingDraftPromotionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.control = self.root / ".caprmedio_caprmedio"
        self.control.mkdir()
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n', encoding="utf-8"
        )
        self.draft = self.control / "04_requirement" / "draft" / "draft--pending.md"
        self.draft.parent.mkdir(parents=True)
        self.head = reserve_history_entry(self.root)
        self._write_draft(self.head)
        append_draft_entry(self.root, self._relative(self.draft), reference=self.head, origin={"kind": "never_identified"})
        self.output = self.control / "04_requirement" / "active" / "CA-R-700--pending.md"
        self.output_bytes = self._output_bytes("CA-R-700")
        self.request = {"request_id": "promotion-700", "transition": "Draft->Active"}

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _relative(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def _write_draft(self, head: dict[str, str]) -> None:
        self.draft.write_text(
            "---\ncontent_role: Requirement\nstatus: Draft\nrevision_lineage: "
            + json.dumps({"history_entry_ref": head}, sort_keys=True)
            + "\n---\n# Summary\nPending meaning\n",
            encoding="utf-8",
        )

    def _output_bytes(self, atom_id: str) -> bytes:
        return (
            f"---\natom_id: {atom_id}\ncontent_role: Requirement\nstatus: Active\n---\n"
            "# Summary\nPending meaning\n"
        ).encode("utf-8")

    def _reserve(self, **changes: object) -> dict[str, object]:
        values: dict[str, object] = {
            "draft_path": self._relative(self.draft),
            "head": self.head,
            "request": self.request,
            "planned_atom_id": "CA-R-700",
            "output_path": self._relative(self.output),
            "output_digest": hashlib.sha256(self.output_bytes).hexdigest(),
        }
        values.update(changes)
        return reserve_pending_promotion(self.root, **values)  # type: ignore[arg-type]

    def _history(self) -> dict[str, bytes]:
        archive = self.control / "archive" / "_draft_history"
        return {path.name: path.read_bytes() for path in archive.glob("*.json")}

    def test_exact_reservation_is_idempotent_and_non_consuming(self) -> None:
        first = self._reserve()
        second = self._reserve()
        self.assertEqual("pending", first["disposition"])
        self.assertEqual(first, second)
        self.assertTrue(pending_promotion_path(self.root).is_file())
        self.assertEqual(1, len(self._history()))
        self.assertEqual("never_identified", validate_current_draft_head(self.root, self._relative(self.draft), self.head)["origin"]["kind"])

    def test_competing_identity_or_request_refuses_without_history_effect(self) -> None:
        self._reserve()
        before = self._history()
        with self.assertRaisesRegex(PendingPromotionError, "different Draft promotion"):
            self._reserve(planned_atom_id="CA-R-701")
        with self.assertRaisesRegex(PendingPromotionError, "different Draft promotion"):
            self._reserve(request={"request_id": "another"})
        self.assertEqual(before, self._history())
        self.assertFalse(self.output.exists())

    def test_missing_or_tampered_output_returns_pending_without_consuming_head(self) -> None:
        reservation = self._reserve()["reservation"]
        before = self._history()
        missing = finalize_pending_promotion(self.root, reservation)
        self.assertEqual(("pending", "output-missing"), (missing["disposition"], missing["repair_context"]["code"]))
        self.assertEqual(before, self._history())

        self.output.parent.mkdir(parents=True)
        self.output.write_bytes(self._output_bytes("CA-R-701"))
        tampered = finalize_pending_promotion(self.root, reservation)
        self.assertEqual(("pending", "output-digest-mismatch"), (tampered["disposition"], tampered["repair_context"]["code"]))
        self.assertEqual(before, self._history())
        validate_current_draft_head(self.root, self._relative(self.draft), self.head)

    def test_finalization_failure_is_pending_then_exact_recovery_appends_once(self) -> None:
        reservation = self._reserve()["reservation"]
        self.output.parent.mkdir(parents=True)
        self.output.write_bytes(self.output_bytes)
        before = self._history()
        with patch.object(pending, "append_promotion_successor", side_effect=DraftHistoryError("disk failed")):
            failed = finalize_pending_promotion(self.root, reservation)
        self.assertEqual(("pending", "finalization-failed"), (failed["disposition"], failed["repair_context"]["code"]))
        self.assertEqual(before, self._history())

        recovered = finalize_pending_promotion(self.root, reservation)
        self.assertEqual("finalized", recovered["disposition"])
        self.assertEqual(2, len(self._history()))
        replay = self._reserve()
        self.assertEqual("finalized", replay["disposition"])
        self.assertEqual(recovered["successor"], replay["successor"])
        self.assertEqual(recovered["successor"], finalize_pending_promotion(self.root, reservation)["successor"])
        self.draft.unlink()
        self.assertEqual("finalized", self._reserve()["disposition"])

    def test_terminal_receipt_write_failure_recovers_existing_successor_once(self) -> None:
        reservation = self._reserve()["reservation"]
        self.output.parent.mkdir(parents=True)
        self.output.write_bytes(self.output_bytes)
        with patch.object(pending, "_write_terminal", side_effect=PendingPromotionError("runtime-write-failed", "disk failed")):
            incomplete = finalize_pending_promotion(self.root, reservation)
        self.assertEqual(("pending", "runtime-write-failed"), (incomplete["disposition"], incomplete["repair_context"]["code"]))
        self.assertEqual(2, len(self._history()))
        self.draft.unlink()

        recovered = recover_pending_promotion(self.root, draft_path=self._relative(self.draft), head=self.head)
        self.assertEqual("finalized", recovered["disposition"])
        repaired = lookup_pending_promotion(self.root, draft_path=self._relative(self.draft), head=self.head)
        self.assertEqual("finalized", repaired["disposition"])
        self.assertEqual(2, len(self._history()))
        self.assertEqual(repaired["successor"], match_promotion_successor(
            self.root, head=self.head, output_path=self._relative(self.output),
            output_digest=hashlib.sha256(self.output_bytes).hexdigest(),
        ))

    def test_public_lookup_prevents_new_identity_before_preparing_output(self) -> None:
        reserved = self._reserve()
        found = lookup_pending_promotion(self.root, draft_path=self._relative(self.draft), head=self.head)
        self.assertEqual(reserved, found)
        self.assertEqual("CA-R-700", found["reservation"]["planned_atom_id"])
        with self.assertRaisesRegex(PendingPromotionError, "different Draft promotion"):
            lookup_pending_promotion(self.root, draft_path=".caprmedio_caprmedio/04_requirement/draft/draft--other.md", head=self.head)

    def test_concurrent_finalizers_share_one_consuming_successor(self) -> None:
        reservation = self._reserve()["reservation"]
        self.output.parent.mkdir(parents=True)
        self.output.write_bytes(self.output_bytes)
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
            first = context.Process(target=_concurrent_finalize, args=(str(self.root), reservation, results))
            first.start()
            self.assertTrue(entered.wait(timeout=5))
            second = context.Process(target=_concurrent_finalize, args=(str(self.root), reservation, results))
            second.start()
            release.set()
            first.join(timeout=5)
            second.join(timeout=5)

        self.assertEqual((0, 0), (first.exitcode, second.exitcode))
        outcomes = [results.get(timeout=2), results.get(timeout=2)]
        self.assertEqual(["result", "result"], sorted(item[0] for item in outcomes))
        finalized = [item[1] for item in outcomes]
        self.assertTrue(all(result["disposition"] == "finalized" for result in finalized))
        self.assertEqual(1, len({result["successor"]["history_revision"] for result in finalized}))
        self.assertEqual(2, len(self._history()))

    def test_tampered_reservation_and_retired_caller_evidence_fail_closed(self) -> None:
        self._reserve()
        state = pending_promotion_path(self.root)
        value = json.loads(state.read_text(encoding="utf-8"))
        value["reservation"]["planned_atom_id"] = "CA-R-701"
        state.write_text(json.dumps(value), encoding="utf-8")
        before = self._history()
        with self.assertRaisesRegex(PendingPromotionError, "seal does not match"):
            self._reserve()
        self.assertEqual(before, self._history())

        self.temp.cleanup()
        self.setUp()
        with self.assertRaisesRegex(PendingPromotionError, "identity evidence"):
            self._reserve(request={"draft_identity_evidence": {"head": self.head}})
        self.assertEqual(1, len(self._history()))


if __name__ == "__main__":
    unittest.main()
