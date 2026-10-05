"""Retained Journal-only tests for the explicit first-install Action recorder.

No test calls Docker or the framework installer.  Fixture roots are retained:
managed macOS can deny directory cleanup, and no test should hide that fact by
turning cleanup failures into success.
"""

from __future__ import annotations

import datetime as dt
import shutil
import sys
import tempfile
import unittest
from contextlib import AbstractContextManager
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = RELEASE_ROOT.parent
for path in (RELEASE_ROOT, TOOLS_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import work_journal  # noqa: E402
from direct_action_session import (  # noqa: E402
    ACTION_ATOM_RELATIVE,
    DirectActionJournalError,
    DirectActionSession,
    INITIALIZATION_ACTION_ID,
)


def _repository_root() -> Path:
    for candidate in RELEASE_ROOT.parents:
        if (candidate / ".caprmedio_caprmedio/caprmedio_project_settings.toml").is_file():
            return candidate
    raise RuntimeError("repository root is unavailable")


REPOSITORY_ROOT = _repository_root()
AUTHORIZATION = {"operator": "Anatoly Maslennikov", "authorization_ref": "tmp/operator-authorizations/bootstrap.md"}
INTENT = {
    "action_id": INITIALIZATION_ACTION_ID,
    "kind": "first_framework_runtime_installation",
    "manifest_sha256": "a" * 64,
    "source_context_sha256": "b" * 64,
    "image_digest": "sha256:" + "c" * 64,
}


class _ExclusiveFixtureLock(AbstractContextManager[None]):
    """In-memory lock used only to prove no second session may start a Run."""

    def __init__(self, held: set[str], key: str) -> None:
        self.held = held
        self.key = key

    def __enter__(self) -> None:
        if self.key in self.held:
            raise work_journal.WorkJournalError("journal-lock-unavailable", "fixture lock is held")
        self.held.add(self.key)

    def __exit__(self, exc_type, exc, traceback) -> None:
        del exc_type, exc, traceback
        self.held.remove(self.key)


class DirectActionSessionTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = REPOSITORY_ROOT / ".caprmedio_tmp/direct-action-session-tests"
        parent.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="direct-action-", dir=parent))
        self._write(
            ".caprmedio_caprmedio/caprmedio_project_settings.toml",
            b"[paths]\ncontrol_root = '.caprmedio_caprmedio'\njournal_root = '.caprmedio_caprmedio/_journal'\nruntime_root = '.caprmedio_runtime'\n",
        )
        source = REPOSITORY_ROOT / ACTION_ATOM_RELATIVE
        target = self.root / ACTION_ATOM_RELATIVE
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        shutil.copyfile(
            REPOSITORY_ROOT / ".caprmedio_caprmedio/operators_registry.toml",
            self.root / ".caprmedio_caprmedio/operators_registry.toml",
        )
        self.session = DirectActionSession(
            self.root,
            author="anatoly-m",
            operator_authorization=AUTHORIZATION,
            now=lambda: dt.datetime(2026, 10, 5, 18, 0, tzinfo=dt.UTC),
        )

    def _write(self, relative: str, payload: bytes) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        return path

    def _events(self) -> list[dict]:
        journal = self.root / ".caprmedio_caprmedio/_journal"
        events: list[dict] = []
        for path in sorted(journal.glob("*.ndjson")):
            events.extend(__import__("json").loads(line) for line in path.read_text(encoding="utf-8").splitlines())
        return events

    def test_starts_one_deterministic_direct_action_and_reopens_before_effects(self) -> None:
        started = self.session.begin_action(
            action_id=INITIALIZATION_ACTION_ID,
            requested_run_id="bootstrap-001",
            intent=INTENT,
        )

        self.assertEqual(started["disposition"], "started")
        self.assertIn(started["run_id"], self.session.actual)
        self.assertEqual(self.session.terminal, {})
        events = self._events()
        self.assertEqual(len(events), 1)
        event = events[0]
        self.assertEqual(event["event"], "started")
        self.assertEqual(event["action_id"], INITIALIZATION_ACTION_ID)
        self.assertEqual(event["run"]["definition"]["atom_id"], "CA-O-180")
        self.assertEqual(event["initiative"]["initiative_ref"], AUTHORIZATION["authorization_ref"])
        self.assertEqual(event["event_id"], started["event_id"])

        # Repeating inside the same process is blocked.  It cannot be treated
        # as a successful fresh start and therefore cannot replay effects.
        with self.assertRaises(DirectActionJournalError) as repeated:
            self.session.begin_action(
                action_id=INITIALIZATION_ACTION_ID,
                requested_run_id="bootstrap-001",
                intent=INTENT,
            )
        self.assertEqual(repeated.exception.code, "direct-action-invocation-active")
        self.assertEqual(len(self._events()), 1)

    def test_finishes_only_after_observed_effects_with_one_terminal_receipt(self) -> None:
        started = self.session.begin_action(
            action_id=INITIALIZATION_ACTION_ID,
            requested_run_id="bootstrap-002",
            intent=INTENT,
        )
        effects = [
            ".caprmedio_runtime/framework/releases/" + "a" * 64,
            ".agents/skills/ca",
            ".caprmedio_runtime/framework/current.toml",
            ".caprmedio_runtime/framework_initialization/" + "a" * 64 + "/result.json",
        ]
        self.session.record_effects(started["run_id"], result_ref=effects[-1], effect_refs=effects)
        terminal = self.session.finish_action(
            started["run_id"],
            outcome="completed",
            result_ref=effects[-1],
            effect_refs=effects,
        )

        self.assertEqual(terminal["disposition"], "terminal")
        self.assertEqual(terminal["outcome"], "completed")
        self.assertEqual([event["event"] for event in self._events()], ["started", "completed"])
        self.assertIn(started["run_id"], self.session.terminal)

    def test_refuses_terminal_evidence_before_effect_observation(self) -> None:
        started = self.session.begin_action(
            action_id=INITIALIZATION_ACTION_ID,
            requested_run_id="bootstrap-003",
            intent=INTENT,
        )
        with self.assertRaises(DirectActionJournalError) as raised:
            self.session.finish_action(
                started["run_id"],
                outcome="failed",
                result_ref="tmp/bootstrap/result.json",
                effect_refs=[],
            )
        self.assertEqual(raised.exception.code, "direct-action-effects-unobserved")
        self.assertEqual([event["event"] for event in self._events()], ["started"])

    def test_restart_with_started_intent_requires_recovery_and_never_replays(self) -> None:
        self.session.begin_action(
            action_id=INITIALIZATION_ACTION_ID,
            requested_run_id="bootstrap-004",
            intent=INTENT,
        )
        self.session.close()
        resumed = DirectActionSession(
            self.root,
            author="anatoly-m",
            operator_authorization=AUTHORIZATION,
            now=lambda: dt.datetime(2026, 10, 5, 18, 1, tzinfo=dt.UTC),
        )
        with self.assertRaises(DirectActionJournalError) as raised:
            resumed.begin_action(
                action_id=INITIALIZATION_ACTION_ID,
                requested_run_id="bootstrap-004",
                intent=INTENT,
            )
        self.assertEqual(raised.exception.code, "direct-action-recovery-required")
        self.assertEqual([event["event"] for event in self._events()], ["started"])

    def test_recovers_only_the_original_pending_started_event(self) -> None:
        with patch.object(work_journal, "append_sealed_events", side_effect=OSError("fixture append denied")):
            with self.assertRaises(DirectActionJournalError) as raised:
                self.session.begin_action(
                    action_id=INITIALIZATION_ACTION_ID,
                    requested_run_id="bootstrap-005",
                    intent=INTENT,
                )
        self.assertEqual(raised.exception.code, "direct-action-recording-pending")
        event_id = next(iter(self.session.pending))
        self.assertEqual(self._events(), [])

        recovered = self.session.recover_pending(event_id)
        self.assertEqual(recovered["disposition"], "recovered")
        self.assertEqual([event["event_id"] for event in self._events()], [event_id])
        with self.assertRaises(DirectActionJournalError):
            self.session.recover_pending("event-not-a-direct-action")

    def test_recovers_sealed_pending_completion_after_o180_source_changes(self) -> None:
        started = self.session.begin_action(
            action_id=INITIALIZATION_ACTION_ID,
            requested_run_id="bootstrap-005-terminal",
            intent=INTENT,
        )
        result_ref = "tmp/bootstrap/result.json"
        effects = [".caprmedio_runtime/framework/current.toml"]
        self.session.record_effects(started["run_id"], result_ref=result_ref, effect_refs=effects)
        with patch.object(work_journal, "append_sealed_events", side_effect=OSError("fixture append denied")):
            with self.assertRaises(DirectActionJournalError) as raised:
                self.session.finish_action(
                    started["run_id"], outcome="completed", result_ref=result_ref, effect_refs=effects
                )
        self.assertEqual(raised.exception.code, "direct-action-recording-pending")
        self.assertEqual(self.session._observed[started["run_id"]], {"result_ref": result_ref, "effect_refs": effects})
        pending_id = next(iter(self.session.pending))
        # A later call cannot append a new terminal event.  The immutable
        # pending one is the sole permitted recovery path.
        with self.assertRaises(DirectActionJournalError) as repeat:
            self.session.finish_action(
                started["run_id"], outcome="completed", result_ref=result_ref, effect_refs=effects
            )
        self.assertEqual(repeat.exception.code, "direct-action-invocation-closed")
        # The original event is already sealed into pending evidence.  A later
        # O-180 edit cannot authorize a new Action, but it must not prevent
        # appending this exact completed Journal fact.
        (self.root / ACTION_ATOM_RELATIVE).write_text("O-180 changed after the pending completion", encoding="utf-8")
        inspector = DirectActionSession(
            self.root,
            author="anatoly-m",
            operator_authorization=AUTHORIZATION,
            now=lambda: dt.datetime(2026, 10, 5, 18, 1, tzinfo=dt.UTC),
        )
        with self.assertRaises(DirectActionJournalError) as new_execution:
            inspector.begin_action(
                action_id=INITIALIZATION_ACTION_ID,
                requested_run_id="bootstrap-005-terminal-new",
                intent=INTENT,
            )
        self.assertEqual(new_execution.exception.code, "direct-action-source-stale")
        self.session.recover_pending(pending_id)
        self.assertEqual([event["event"] for event in self._events()], ["started", "completed"])

    def test_exact_source_pin_and_explicit_operator_authorization_are_required(self) -> None:
        source = self.root / ACTION_ATOM_RELATIVE
        source.write_text("changed", encoding="utf-8")
        with self.assertRaises(DirectActionJournalError) as raised:
            self.session.begin_action(
                action_id=INITIALIZATION_ACTION_ID,
                requested_run_id="bootstrap-006",
                intent=INTENT,
            )
        self.assertEqual(raised.exception.code, "direct-action-source-stale")
        with self.assertRaises(DirectActionJournalError) as authorization:
            DirectActionSession(self.root, author="anatoly-m", operator_authorization={})
        self.assertEqual(authorization.exception.code, "direct-action-authorization-required")

    def test_refuses_a_symlinked_pinned_action_source(self) -> None:
        source = self.root / ACTION_ATOM_RELATIVE
        redirected = self.root / "tmp/pinned-action-source"
        redirected.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, redirected / source.name)
        source.unlink()
        source.symlink_to(redirected / source.name)

        with self.assertRaises(DirectActionJournalError) as raised:
            self.session.begin_action(
                action_id=INITIALIZATION_ACTION_ID,
                requested_run_id="bootstrap-006-symlink",
                intent=INTENT,
            )
        self.assertEqual(raised.exception.code, "direct-action-source-stale")

    def test_reused_requested_id_with_changed_intent_is_a_conflict_not_a_second_start(self) -> None:
        self.session.begin_action(
            action_id=INITIALIZATION_ACTION_ID,
            requested_run_id="bootstrap-007",
            intent=INTENT,
        )
        self.session.close()
        changed = dict(INTENT, image_digest="sha256:" + "d" * 64)
        resumed = DirectActionSession(
            self.root,
            author="anatoly-m",
            operator_authorization=AUTHORIZATION,
            now=lambda: dt.datetime(2026, 10, 5, 18, 1, tzinfo=dt.UTC),
        )
        with self.assertRaises(DirectActionJournalError) as raised:
            resumed.begin_action(
                action_id=INITIALIZATION_ACTION_ID,
                requested_run_id="bootstrap-007",
                intent=changed,
            )
        self.assertEqual(raised.exception.code, "direct-action-intent-conflict")
        self.assertEqual([event["event"] for event in self._events()], ["started"])

    def test_another_session_cannot_start_same_or_distinct_run_while_first_install_is_owned(self) -> None:
        held: set[str] = set()

        def fixture_lock(root: Path, key: str) -> _ExclusiveFixtureLock:
            del root
            return _ExclusiveFixtureLock(held, key)

        with patch.object(work_journal, "_event_lock", side_effect=fixture_lock):
            self.session.begin_action(
                action_id=INITIALIZATION_ACTION_ID,
                requested_run_id="bootstrap-008",
                intent=INTENT,
            )
            for requested_run_id in ("bootstrap-008", "bootstrap-009"):
                competing = DirectActionSession(
                    self.root,
                    author="anatoly-m",
                    operator_authorization=AUTHORIZATION,
                    now=lambda: dt.datetime(2026, 10, 5, 18, 1, tzinfo=dt.UTC),
                )
                with self.assertRaises(DirectActionJournalError) as raised:
                    competing.begin_action(
                        action_id=INITIALIZATION_ACTION_ID,
                        requested_run_id=requested_run_id,
                        intent=INTENT,
                    )
                self.assertEqual(raised.exception.code, "direct-action-lock-unavailable")
            self.assertEqual([event["event"] for event in self._events()], ["started"])
            self.session.close()
            self.assertEqual(held, set())


if __name__ == "__main__":
    unittest.main()
