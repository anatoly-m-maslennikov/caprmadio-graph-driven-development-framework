"""Pure provider guards for private Release checkpoint reuse.

No test creates a Project, carrier, Journal, temporary directory, or Docker
process.  The small doubles model only the Session evidence a provider must
observe before it can trust a decoded checkpoint result.
"""
from __future__ import annotations

from pathlib import Path
import sys
from types import SimpleNamespace
import unittest


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

from selected_execution import SelectedExecutionError  # noqa: E402
from selected_native_providers import SelectedNativeProviders  # noqa: E402


REQUESTED_ACTION = "release:step:1:action:1"
ACTUAL_ACTION = "actual-action"


def _run(*, outcome: str = "completed") -> SimpleNamespace:
    return SimpleNamespace(
        contexts={0: SimpleNamespace(action_run_id=ACTUAL_ACTION)},
        results={0: SimpleNamespace(outcome=outcome, effect_evidence_refs=("evidence/receipt.json",)),},
    )


def _session(*, terminal: dict[str, object] | None = None, receipts: list[dict[str, object]] | None = None) -> SimpleNamespace:
    return SimpleNamespace(
        terminal={REQUESTED_ACTION: terminal or {
            "disposition": "terminal", "outcome": "completed", "run_id": ACTUAL_ACTION,
            "result_ref": "_journal/release.json", "effect_refs": ["evidence/receipt.json"],
            "event_receipt": {"event_id": "completion-event"},
        }},
        receipts=receipts or [{"event_id": "start-event"}, {"event_id": "completion-event"}],
    )


def _progress(*, result: str = "phase-completed", effects: list[str] | None = None) -> dict[str, object]:
    return {
        "action_run_id": ACTUAL_ACTION,
        "result": result,
        "effect_refs": ["evidence/receipt.json"] if effects is None else effects,
    }


class ReleaseProviderCheckpointTests(unittest.TestCase):
    def test_cached_completed_result_requires_current_session_terminal_and_receipts(self) -> None:
        proven = SelectedNativeProviders._restored_completed_result_is_proven(
            _session(), index=0, run=_run(), requested_action=REQUESTED_ACTION,
            action_run_id=ACTUAL_ACTION, expected_result="phase-completed",
            progress_reader=lambda requested_action: _progress() if requested_action == REQUESTED_ACTION else {},
            shared_recordings={0: {"terminal_outcome": "completed", "receipt_refs": ("completion-event",)}},
        )
        self.assertTrue(proven)

    def test_forged_checkpoint_recording_is_not_canonical_session_proof(self) -> None:
        for recording, session in (
            (
                {"terminal_outcome": "completed", "receipt_refs": ("forged-event",)},
                _session(),
            ),
            (
                {"terminal_outcome": "completed", "receipt_refs": ("completion-event",)},
                _session(terminal={
                    "disposition": "terminal", "outcome": "completed", "run_id": ACTUAL_ACTION,
                    "result_ref": "_journal/release.json", "effect_refs": ["different-effect"],
                    "event_receipt": {"event_id": "completion-event"},
                }),
            ),
        ):
            with self.subTest(recording=recording, terminal=session.terminal[REQUESTED_ACTION]):
                self.assertFalse(SelectedNativeProviders._restored_completed_result_is_proven(
                    session, index=0, run=_run(), requested_action=REQUESTED_ACTION,
                    action_run_id=ACTUAL_ACTION, expected_result="phase-completed",
                    progress_reader=lambda _requested_action: _progress(),
                    shared_recordings={0: recording},
                ))

    def test_mismatched_progress_cannot_reuse_a_checkpointed_effect(self) -> None:
        recordings = {0: {"terminal_outcome": "completed", "receipt_refs": ("completion-event",)}}
        for progress in (
            _progress(result="different-result"),
            _progress(effects=["different-effect"]),
            {"action_run_id": "different-action", "result": "phase-completed", "effect_refs": ["evidence/receipt.json"]},
            {},
        ):
            with self.subTest(progress=progress):
                self.assertFalse(SelectedNativeProviders._restored_completed_result_is_proven(
                    _session(), index=0, run=_run(), requested_action=REQUESTED_ACTION,
                    action_run_id=ACTUAL_ACTION, expected_result="phase-completed",
                    progress_reader=lambda _requested_action, value=progress: value,
                    shared_recordings=recordings,
                ))

    def test_reader_failure_is_not_checkpoint_proof(self) -> None:
        def unreadable(_requested_action: str) -> dict[str, object]:
            raise OSError("reader failed")

        self.assertFalse(SelectedNativeProviders._restored_completed_result_is_proven(
            _session(), index=0, run=_run(), requested_action=REQUESTED_ACTION,
            action_run_id=ACTUAL_ACTION, expected_result="release retired", progress_reader=unreadable,
            shared_recordings={0: {"terminal_outcome": "completed", "receipt_refs": ("completion-event",)}},
        ))

    def test_pending_recording_clears_only_after_exact_canonical_reconciliation(self) -> None:
        pending = {"event_id": "completion-event", "event_outcome": "completed"}
        self.assertTrue(SelectedNativeProviders._pending_recording_is_reconciled(
            _session(), result=_run().results[0], pending_recording=pending,
            requested_action=REQUESTED_ACTION, action_run_id=ACTUAL_ACTION,
            expected_result="phase-completed", progress_reader=lambda _requested_action: _progress(),
            allowed_private_outcomes=frozenset({"completed"}),
        ))
        for rejected in (
            {"event_id": "other-event", "event_outcome": "completed"},
            {"event_id": "completion-event", "event_outcome": "failed"},
            {"event_id": "completion-event", "event_outcome": "completed", "extra": "field"},
        ):
            with self.subTest(rejected=rejected):
                self.assertFalse(SelectedNativeProviders._pending_recording_is_reconciled(
                    _session(), result=_run().results[0], pending_recording=rejected,
                    requested_action=REQUESTED_ACTION, action_run_id=ACTUAL_ACTION,
                    expected_result="phase-completed", progress_reader=lambda _requested_action: _progress(),
                    allowed_private_outcomes=frozenset({"completed"}),
                ))

    def test_resumed_retirement_uses_the_proven_completion_edge_without_replaying(self) -> None:
        self.assertTrue(SelectedNativeProviders._restored_completed_result_is_proven(
            _session(), index=0, run=_run(outcome="pending"), requested_action=REQUESTED_ACTION,
            action_run_id=ACTUAL_ACTION, expected_result="release retired",
            progress_reader=lambda _requested_action: _progress(result="release retired"),
            allowed_private_outcomes=frozenset({"pending"}),
            shared_recordings={0: {"terminal_outcome": "completed", "receipt_refs": ("completion-event",)}},
        ))

    def test_restored_started_action_without_a_typed_result_is_blocked_before_replay(self) -> None:
        self.assertTrue(SelectedNativeProviders._restored_action_without_typed_result_is_blocked(
            {"restored_action": True}, cached_result=False,
        ))
        self.assertFalse(SelectedNativeProviders._restored_action_without_typed_result_is_blocked(
            {"restored_action": True}, cached_result=True,
        ))
        self.assertFalse(SelectedNativeProviders._restored_action_without_typed_result_is_blocked(
            {}, cached_result=False,
        ))

    def test_checkpoint_uses_the_exact_terminal_receipt_not_all_session_receipts(self) -> None:
        self.assertEqual(
            "completion-event",
            SelectedNativeProviders._canonical_terminal_receipt_ref(_session().terminal[REQUESTED_ACTION]),
        )
        for receipt in ({}, {"event_receipt": {}}, {"event_receipt": {"event_id": " "}}):
            with self.subTest(receipt=receipt):
                with self.assertRaises(SelectedExecutionError):
                    SelectedNativeProviders._canonical_terminal_receipt_ref(receipt)


if __name__ == "__main__":
    unittest.main()
