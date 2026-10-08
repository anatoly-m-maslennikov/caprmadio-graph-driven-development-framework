"""Cold-process persistence coverage for the Release recovery boundary.

Acceptance criteria are CA-P-1713's restart boundaries and CA-P-1716's
explicit, already-frozen recovery boundary.  The sealed source revision is
the one admitted by the production checkpoint codec; this test never tries to
re-admit, redispatch, or alter it.

This is deliberately a synthetic fixture: it creates only typed checkpoint and
Journal evidence under ``.caprmedio_tmp`` and records a marker instead of
running any Release phase, Docker operation, or MCP route.  Each assertion
that follows setup is made by a new Python interpreter, so no in-memory
executor, tracker, or mock carries state across the simulated host restart.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[5]
TOOLS_ROOT = PROJECT_ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
RELEASE_ROOT = TOOLS_ROOT / "RELEASE_VERSION"
CHECKPOINT_TEST = RELEASE_ROOT / "tests/test_release_checkpoint.py"
RECOVERY_TEST = Path(__file__).with_name("test_release_recovery_executor.py")
SCRATCH_PARENT = PROJECT_ROOT / ".caprmedio_tmp/epic-resume-restart"


# This child intentionally imports the production codec and recorder.  The two
# existing pure-test modules only supply closed, synthetic typed evidence; no
# mocked object or module state crosses an invocation boundary.
CHILD = r'''
import json
import os
from dataclasses import replace
from pathlib import Path
import runpy
import sys

root = Path(sys.argv[1]).resolve()
mode = sys.argv[2]
checkpoint_test = Path(sys.argv[3])
recovery_test = Path(sys.argv[4])

for location in (Path(sys.argv[5]), Path(sys.argv[6])):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import work_journal
from release_checkpoint import dump_release_checkpoint, extract_pending_recordings, load_release_checkpoint


def emit(**value):
    value["pid"] = os.getpid()
    print(json.dumps(value, sort_keys=True))


def configure_root():
    (root / ".caprmedio_caprmedio").mkdir(parents=True, exist_ok=True)
    (root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
        "[paths]\ncontrol_root = '.caprmedio_caprmedio'\njournal_root = '.caprmedio_caprmedio/_journal'\nruntime_root = '.caprmedio_runtime'\n"
        "[artifact_timestamps]\ntimezone = 'UTC'\n",
        encoding="utf-8",
    )


def case_with_synthetic_typed_evidence():
    scope = runpy.run_path(str(checkpoint_test))
    # The existing fixture has no side effects; bind its sealed carrier to this
    # disposable root instead of the checkout it was written from.
    scope["PROJECT_ROOT"] = str(root)
    case = scope["ReleaseCheckpointTests"]("test_closed_canonical_round_trip_preserves_fresh_workflow_six")
    case.setUp()
    return scope, case


def write_checkpoint(payload):
    path = root / "state/release_action_run.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")), encoding="utf-8")


def load_checkpoint():
    return json.loads((root / "state/release_action_run.json").read_text(encoding="utf-8"))


def setup_pre_effect():
    configure_root()
    scope, case = case_with_synthetic_typed_evidence()
    context = replace(
        case.run.contexts[0], step_run_id="step-1", action_run_id="action-1",
        parent_step_run_id="step-1", step_atom_id=scope["PHASES"][1][0],
        action_atom_id=scope["PHASES"][1][1],
    )
    case.run.contexts[1] = context
    case.run.next_phase = 1
    case.run.in_progress = context
    write_checkpoint(dump_release_checkpoint(case.run))
    (root / "state/effect-marker.txt").write_text("no synthetic effect executed\n", encoding="utf-8")
    emit(state="pre-effect-checkpoint")


def setup_post_effect(event_outcome="completed"):
    configure_root()
    scope, case = case_with_synthetic_typed_evidence()
    recovery = runpy.run_path(str(recovery_test))
    execution = recovery["_execution"]()
    _workflow, _step, action = recovery["_runs"](execution)
    starts = recovery["_start_events"](execution)
    event = recovery["_event"](
        execution,
        event_id="synthetic-post-effect-event",
        event_name="completed" if event_outcome == "completed" else "interrupted",
        run=action,
        bindings=starts[2]["definition_bindings"],
        outcome=event_outcome,
        result_ref="state/synthetic-action.json",
        effect_refs=["state/synthetic-effect.json"],
    )
    (root / "state").mkdir(parents=True, exist_ok=True)
    (root / "state/synthetic-action.json").write_text('{"synthetic":"already-observed"}\n', encoding="utf-8")
    # The marker is the only synthetic effect probe. Recovery must never add a
    # second line; no actual release effect is emulated or dispatched.
    (root / "state/synthetic-effect.json").write_text("effect-observed-once\n", encoding="utf-8")
    context = work_journal.seal_append_context(
        root, event, author="recovery-bot", local_date="2026-10-06", timezone="UTC",
    )
    work_journal.store_pending_event(
        root, event, context, result_ref=event["result_ref"], effect_refs=event["effect_refs"],
        diagnostic="synthetic effect already observed; reconcile only the original sealed event",
    )
    write_checkpoint(dump_release_checkpoint(
        case.run,
        pending_recordings={0: {"event_id": event["event_id"], "event_outcome": event_outcome}},
    ))
    emit(state="post-effect-pending-recording", event_id=event["event_id"])


def setup_completed():
    configure_root()
    scope, case = case_with_synthetic_typed_evidence()
    # Reuse the repository's full typed fixture to get a fully advanced,
    # codec-valid Release frontier.  It is synthetic evidence, not a Release.
    case.test_round_trip_preserves_all_retained_preflight_and_evidence_types()
    case.run.full_gate = replace(case.run.full_gate, outcome="passed")
    case.run.results[9] = replace(case.run.results[9], output=case.run.full_gate)
    case.run.results[11] = replace(case.run.results[11], outcome="completed", reason="synthetic completed frontier")
    case.run.next_phase = len(scope["PHASES"])
    case.run.stopped = False
    write_checkpoint(dump_release_checkpoint(case.run))
    (root / "state/synthetic-effect.json").write_text("completed-before-restart\n", encoding="utf-8")
    emit(state="completed-frontier")


def setup_n5_shaped_recorded_failure():
    configure_root()
    scope, case = case_with_synthetic_typed_evidence()
    # Use real typed later-phase evidence, then retain only the N5-shaped
    # frontier: completed prefix, stopped pending unit gate, no pending event.
    case.test_round_trip_preserves_all_retained_preflight_and_evidence_types()
    case.run.full_gate = replace(case.run.full_gate, outcome="passed")
    case.run.results[9] = replace(case.run.results[9], output=case.run.full_gate)
    case.run.contexts = {index: case.run.contexts[index] for index in range(5)}
    case.run.results = {index: case.run.results[index] for index in range(5)}
    case.run.results[4] = replace(
        case.run.results[4], outcome="pending",
        reason="synthetic closed unit gate failed; preserved frozen protocol",
    )
    case.run.next_phase = 4
    case.run.stopped = True
    case.run.in_progress = None
    write_checkpoint(dump_release_checkpoint(case.run, pending_recordings={}))
    (root / "state/synthetic-effect.json").write_text("recorded-failure-before-restart\n", encoding="utf-8")
    emit(state="n5-shaped-already-recorded-unit-failure")


def cold_check(kind):
    payload = load_checkpoint()
    run, recordings = load_release_checkpoint(
        payload,
        expected_request=payload["request"],
        expected_workflow_run_id=payload["workflow_run_id"],
    )
    pending = {index: dict(packet) for index, packet in extract_pending_recordings(payload).items()}
    marker = root / "state/synthetic-effect.json"
    if kind == "pre":
        assert run.in_progress is not None
        assert not pending and not recordings
        assert (root / "state/effect-marker.txt").read_text(encoding="utf-8") == "no synthetic effect executed\n"
        emit(disposition="blocked-unresolved-in-progress", effect_calls=0, pending_ids=[])
        return
    if kind == "post":
        assert pending == {0: {"event_id": "synthetic-post-effect-event", "event_outcome": "completed"}}
        receipt = work_journal.recover_pending_event(root, "synthetic-post-effect-event")
        assert marker.read_text(encoding="utf-8") == "effect-observed-once\n"
        emit(disposition="recorded-original-event", effect_calls=0, receipt=receipt)
        return
    if kind == "post-repeat":
        assert pending
        try:
            work_journal.recover_pending_event(root, "synthetic-post-effect-event")
        except work_journal.WorkJournalError as error:
            assert error.code == "pending-not-found"
            assert marker.read_text(encoding="utf-8") == "effect-observed-once\n"
            emit(disposition="no-second-append", effect_calls=0, error=error.code)
            return
        raise AssertionError("recovery unexpectedly accepted an already-consumed pending carrier")
    if kind == "completed":
        assert run.next_phase == 12 and run.in_progress is None and not pending and not recordings
        assert marker.read_text(encoding="utf-8") == "completed-before-restart\n"
        emit(disposition="completed-no-new-facts", effect_calls=0, pending_ids=[])
        return
    if kind == "n5":
        assert run.next_phase == 4 and run.stopped and run.in_progress is None and not pending
        result = run.results[4]
        assert result.outcome == "pending"
        assert result.reason == "synthetic closed unit gate failed; preserved frozen protocol"
        assert marker.read_text(encoding="utf-8") == "recorded-failure-before-restart\n"
        emit(disposition="preserve-frozen-failure-no-replay", effect_calls=0, pending_ids=[], reason=result.reason)
        return
    raise AssertionError(kind)


if mode == "setup-pre":
    setup_pre_effect()
elif mode == "setup-post":
    setup_post_effect()
elif mode == "setup-completed":
    setup_completed()
elif mode == "setup-n5":
    setup_n5_shaped_recorded_failure()
elif mode == "cold-pre":
    cold_check("pre")
elif mode == "cold-post":
    cold_check("post")
elif mode == "cold-post-repeat":
    cold_check("post-repeat")
elif mode == "cold-completed":
    cold_check("completed")
elif mode == "cold-n5":
    cold_check("n5")
else:
    raise SystemExit(f"unknown mode: {mode}")
'''


class ReleaseRecoveryHostRestartE2ETests(unittest.TestCase):
    """Persistence-only restart proof; no production Release/Docker assertion."""

    @classmethod
    def setUpClass(cls) -> None:
        SCRATCH_PARENT.mkdir(parents=True, exist_ok=True)

    def setUp(self) -> None:
        self._temporary = tempfile.TemporaryDirectory(prefix="recovery-", dir=SCRATCH_PARENT)
        self.root = Path(self._temporary.name)

    def tearDown(self) -> None:
        self._temporary.cleanup()

    def child(self, mode: str) -> dict[str, object]:
        environment = os.environ.copy()
        environment["PYTHONPATH"] = os.pathsep.join((str(TOOLS_ROOT), str(RELEASE_ROOT)))
        result = subprocess.run(
            [
                sys.executable, "-c", CHILD, str(self.root), mode, str(CHECKPOINT_TEST),
                str(RECOVERY_TEST), str(TOOLS_ROOT), str(RELEASE_ROOT),
            ],
            cwd=self.root,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=f"child {mode} failed:\n{result.stderr}\n{result.stdout}")
        return json.loads(result.stdout)

    def test_pre_effect_checkpoint_blocks_cold_replay(self) -> None:
        setup = self.child("setup-pre")
        cold = self.child("cold-pre")

        self.assertNotEqual(setup["pid"], cold["pid"])
        self.assertEqual(cold["disposition"], "blocked-unresolved-in-progress")
        self.assertEqual(cold["effect_calls"], 0)

    def test_post_effect_pending_event_appends_original_bytes_once_after_restart(self) -> None:
        self.child("setup-post")
        recovered = self.child("cold-post")
        repeated = self.child("cold-post-repeat")

        self.assertEqual(recovered["disposition"], "recorded-original-event")
        self.assertEqual(recovered["effect_calls"], 0)
        self.assertEqual(repeated["disposition"], "no-second-append")
        carrier = self.root / str(recovered["receipt"]["carrier"])
        self.assertEqual(len(carrier.read_text(encoding="utf-8").splitlines()), 1)
        self.assertFalse((self.root / ".caprmedio_runtime/state/work_journal/pending/synthetic-post-effect-event.json").exists())

    def test_completed_frontier_creates_no_new_facts_after_restart(self) -> None:
        self.child("setup-completed")
        cold = self.child("cold-completed")

        self.assertEqual(cold["disposition"], "completed-no-new-facts")
        self.assertEqual(cold["effect_calls"], 0)

    def test_n5_shaped_recorded_unit_failure_preserves_frozen_protocol(self) -> None:
        self.child("setup-n5")
        cold = self.child("cold-n5")

        self.assertEqual(cold["disposition"], "preserve-frozen-failure-no-replay")
        self.assertEqual(cold["effect_calls"], 0)
        self.assertIn("preserved frozen protocol", str(cold["reason"]))


if __name__ == "__main__":
    unittest.main()
