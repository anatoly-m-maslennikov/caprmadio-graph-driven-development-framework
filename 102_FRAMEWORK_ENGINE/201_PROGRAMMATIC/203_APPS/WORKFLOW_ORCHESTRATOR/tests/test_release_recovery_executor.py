"""Pure recovery tests for the private Release executor entry.

These tests keep Journal carriers, checkpoints, and Run output in dictionaries.
They exercise the real selected-Run reconstruction state machine but never make
directories, invoke Docker, or append a physical Journal event.
"""
from __future__ import annotations

from contextlib import nullcontext
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Mapping
from unittest import mock
import sys
import unittest


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
RELEASE_TOOLS = TOOLS / "RELEASE_VERSION"
for location in (APP, TOOLS, RELEASE_TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import release_checkpoint  # noqa: E402
import selected_run_recovery  # noqa: E402
import work_journal  # noqa: E402
from selected_execution import SelectedExecution, SelectedExecutionError  # noqa: E402
from release_actions import PHASES  # noqa: E402
from workflow_run_support import LazyRunTracker, RunExecutionSession  # noqa: E402


ROOT = Path("/project")
RUN_ID = "release-recovery-run"
REQUEST_ID = "release-recovery-request"
ACTION_ID = "release-recovery-action"


def _digest(value: object) -> str:
    return work_journal.canonical_json_digest(value)


def _definition(atom_id: str, kind: str) -> dict[str, object]:
    return {
        "atom_id": atom_id,
        "version": 1,
        "path": f"operations/{atom_id}.md",
        "digest": "a" * 64,
    }


def _execution() -> dict[str, object]:
    parameters: dict[str, object] = {"release": "candidate"}
    frontier = ["03_plan/CA-P-1624.md"]
    effects: list[object] = []
    workflow = _definition("CA-O-164", "workflow")
    step = _definition("CA-O-170", "step")
    action = _definition("CA-O-165", "action")
    return {
        "mode": "execute",
        "request_id": REQUEST_ID,
        "operation_route": "release_version",
        "parameters": parameters,
        "parameters_digest": _digest(parameters),
        "target_frontier": frontier,
        "target_frontier_digest": _digest(frontier),
        "effects": effects,
        "effects_digest": _digest(effects),
        "definition_manifest": {
            "manifest_ref": "_projection/selected_workflow_bindings.json",
            "manifest_digest": "b" * 64,
        },
        "source_freshness": {
            "selected_source_registry_ref": "_projection/selected_source_registry.json",
            "selected_source_registry_version": 1,
            "selected_source_registry_digest": "c" * 64,
            "selected_binding_ref": "_projection/release_version.json",
            "selected_binding_digest": "d" * 64,
        },
        "initiative": {
            "initiative_id": "CA-P-1624",
            "instruction_summary": "recover one selected Release Run",
            "initiative_ref": "03_plan/CA-P-1624.md",
        },
        "requested_runs": [
            {"requested_run_id": RUN_ID, "kind": "workflow", "definition": workflow},
            {
                "requested_run_id": f"{RUN_ID}:step:1",
                "kind": "step",
                "definition": step,
                "parent_requested_run_id": RUN_ID,
            },
            {
                "requested_run_id": f"{RUN_ID}:step:1:action:1",
                "kind": "action",
                "definition": action,
                "parent_requested_run_id": f"{RUN_ID}:step:1",
            },
        ],
        "proposal_receipt": {},
        "proposal_receipt_digest": "e" * 64,
        "assigned_action_id": ACTION_ID,
        "operator_authorization": {},
    }


def _binding(definition: Mapping[str, object], kind: str) -> dict[str, object]:
    return {"kind": kind, **definition}


def _event(
    execution: Mapping[str, object],
    *,
    event_id: str,
    event_name: str,
    run: Mapping[str, object],
    bindings: list[dict[str, object]],
    outcome: str | None = None,
    result_ref: str | None = None,
    effect_refs: list[str] | None = None,
) -> dict[str, object]:
    return work_journal.with_event_digest(
        {
            "schema_version": 5,
            "kind": "workflow_execution",
            "event_id": event_id,
            "action_id": execution["assigned_action_id"],
            "event": event_name,
            "author": "recovery-bot",
            "occurred_at": "2026-10-05T00:00:00+00:00",
            "llm_session": {"app": "run-support", "uuid": execution["request_id"]},
            "structural_scope": "TOOLS",
            "initiative": execution["initiative"],
            "run": dict(run),
            "definition_bindings": bindings,
            "input_ref": execution["initiative"]["initiative_ref"],
            "outcome": outcome,
            "result_ref": result_ref,
            "effect_refs": list(effect_refs or []),
            "report_ref": None,
            "redaction": {"redacted": False, "fields": []},
        }
    )


def _runs(execution: Mapping[str, object]) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    workflow_definition = execution["requested_runs"][0]["definition"]
    step_definition = execution["requested_runs"][1]["definition"]
    action_definition = execution["requested_runs"][2]["definition"]
    workflow = {"run_id": "actual-workflow", "kind": "workflow", "definition": workflow_definition}
    step = {
        "run_id": "actual-step",
        "kind": "step",
        "definition": step_definition,
        "parent_run_id": workflow["run_id"],
    }
    action = {
        "run_id": "actual-action",
        "kind": "action",
        "definition": action_definition,
        "parent_run_id": step["run_id"],
    }
    return workflow, step, action


def _start_events(execution: Mapping[str, object]) -> list[dict[str, object]]:
    workflow, step, action = _runs(execution)
    workflow_bindings = sorted(
        [
            _binding(execution["requested_runs"][0]["definition"], "workflow"),
            _binding(execution["requested_runs"][1]["definition"], "step"),
            _binding(execution["requested_runs"][2]["definition"], "action"),
        ],
        key=lambda item: (item["kind"], item["atom_id"], item["version"], item["path"]),
    )
    return [
        _event(execution, event_id="event-start-workflow", event_name="started", run=workflow, bindings=workflow_bindings),
        _event(execution, event_id="event-start-step", event_name="started", run=step,
               bindings=[_binding(execution["requested_runs"][1]["definition"], "step")]),
        _event(execution, event_id="event-start-action", event_name="started", run=action,
               bindings=[_binding(execution["requested_runs"][2]["definition"], "action")]),
    ]


def _evidence(events: list[dict[str, object]]) -> dict[str, object]:
    return {
        "dispatch": {"state": "accepted"},
        "events": [
            {
                "event": event,
                "receipt": {
                    "event_id": event["event_id"],
                    "action_id": event["action_id"],
                    "event_digest": event["event_digest"],
                    "carrier": f"memory/{index}.ndjson",
                    "line": 1,
                    "previous_carrier_digest": "0" * 64,
                    "appended_carrier_digest": "0" * 64,
                },
            }
            for index, event in enumerate(events, start=1)
        ],
    }


def _frozen(execution: Mapping[str, object]) -> dict[str, object]:
    action_definition = execution["requested_runs"][2]["definition"]
    step_definition = execution["requested_runs"][1]["definition"]
    workflow_definition = execution["requested_runs"][0]["definition"]
    return {
        "graph": {
            "route": "release_version",
            "manifest_ref": "_projection/selected_workflow_bindings.json",
            "manifest_digest": "b" * 64,
            "workflow": {"atom_id": "CA-O-164", "kind": "workflow", "version": 1,
                         "path": workflow_definition["path"], "sha256": "a" * 64},
            "entry_step": "CA-O-170",
            "steps": [
                {
                    "atom_id": "CA-O-170", "kind": "step", "version": 1,
                    "path": step_definition["path"], "sha256": "a" * 64,
                    "actions": [
                        {
                            "atom_id": "CA-O-165", "kind": "action", "version": 1,
                            "path": action_definition["path"], "sha256": "a" * 64,
                            "result_map": {"done": "done"},
                        }
                    ],
                    "on_result": [{"result": "done", "terminal": "completed"}],
                }
            ],
        },
        "request": {"run_id": RUN_ID, "execution": execution},
    }


def _full_release_execution() -> dict[str, object]:
    """One frozen request carrying every canonical Release phase."""
    execution = _execution()
    workflow = _definition("CA-O-164", "workflow")
    requested: list[dict[str, object]] = [
        {"requested_run_id": RUN_ID, "kind": "workflow", "definition": workflow},
    ]
    for index, (step_atom_id, action_atom_id, _phase) in enumerate(PHASES, start=1):
        requested_step = f"{RUN_ID}:step:{index}"
        requested.append({
            "requested_run_id": requested_step,
            "kind": "step",
            "definition": _definition(step_atom_id, "step"),
            "parent_requested_run_id": RUN_ID,
        })
        requested.append({
            "requested_run_id": f"{requested_step}:action:1",
            "kind": "action",
            "definition": _definition(action_atom_id, "action"),
            "parent_requested_run_id": requested_step,
        })
    execution["requested_runs"] = requested
    return execution


def _full_release_frozen(execution: Mapping[str, object]) -> dict[str, object]:
    requested = execution["requested_runs"]
    workflow_definition = requested[0]["definition"]
    steps: list[dict[str, object]] = []
    for index, (step_atom_id, action_atom_id, _phase) in enumerate(PHASES, start=1):
        step_definition = requested[(index - 1) * 2 + 1]["definition"]
        action_definition = requested[(index - 1) * 2 + 2]["definition"]
        steps.append({
            "atom_id": step_atom_id,
            "kind": "step",
            "version": 1,
            "path": step_definition["path"],
            "sha256": "a" * 64,
            "actions": [{
                "atom_id": action_atom_id,
                "kind": "action",
                "version": 1,
                "path": action_definition["path"],
                "sha256": "a" * 64,
                "result_map": {"done": "done"},
            }],
            "on_result": [{"result": "done", "terminal": "completed"}],
        })
    return {
        "graph": {
            "route": "release_version",
            "manifest_ref": "_projection/selected_workflow_bindings.json",
            "manifest_digest": "b" * 64,
            "workflow": {
                "atom_id": "CA-O-164", "kind": "workflow", "version": 1,
                "path": workflow_definition["path"], "sha256": "a" * 64,
            },
            "entry_step": PHASES[0][0],
            "steps": steps,
        },
        "request": {"run_id": RUN_ID, "execution": execution},
    }


def _full_release_evidence(
    execution: Mapping[str, object],
) -> tuple[list[dict[str, object]], dict[Path, object], SimpleNamespace]:
    """Build exact sealed proof for all ten Release Action occurrences."""
    requested = execution["requested_runs"]
    actual: dict[str, dict[str, object]] = {}
    workflow = {"run_id": "actual-workflow", "kind": "workflow", "definition": requested[0]["definition"]}
    actual[RUN_ID] = workflow
    for index in range(1, len(PHASES) + 1):
        requested_step = f"{RUN_ID}:step:{index}"
        requested_action = f"{requested_step}:action:1"
        step_definition = requested[(index - 1) * 2 + 1]["definition"]
        action_definition = requested[(index - 1) * 2 + 2]["definition"]
        step = {
            "run_id": f"actual-step-{index}", "kind": "step", "definition": step_definition,
            "parent_run_id": workflow["run_id"],
        }
        action = {
            "run_id": f"actual-action-{index}", "kind": "action", "definition": action_definition,
            "parent_run_id": step["run_id"],
        }
        actual[requested_step] = step
        actual[requested_action] = action

    all_bindings = RunExecutionSession.canonical_requested_definition_bindings(requested)
    events = [_event(
        execution, event_id="event-start-workflow", event_name="started", run=workflow,
        bindings=sorted(all_bindings, key=lambda item: (item["kind"], item["atom_id"], item["version"], item["path"])),
    )]
    for index in range(1, len(PHASES) + 1):
        requested_step = f"{RUN_ID}:step:{index}"
        requested_action = f"{requested_step}:action:1"
        for requested_id in (requested_step, requested_action):
            run = actual[requested_id]
            events.append(_event(
                execution, event_id=f"event-start-{requested_id}", event_name="started", run=run,
                bindings=[_binding(run["definition"], run["kind"])],
            ))

    folder = ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID
    storage: dict[Path, object] = {}
    contexts: dict[int, SimpleNamespace] = {}
    results: dict[int, SimpleNamespace] = {}
    step_results: list[dict[str, object]] = []
    for offset, (step_atom_id, action_atom_id, _phase) in enumerate(PHASES):
        index = offset + 1
        requested_step = f"{RUN_ID}:step:{index}"
        requested_action = f"{requested_step}:action:1"
        step = actual[requested_step]
        action = actual[requested_action]
        effect_refs = [f"evidence/phase-{index}.json"]
        action_path = folder / f"{requested_action}.json"
        storage[action_path] = {
            "result": "done", "action_run_id": action["run_id"], "effect_refs": effect_refs,
        }
        events.append(_event(
            execution, event_id=f"event-completed-action-{index}", event_name="completed", run=action,
            bindings=[_binding(action["definition"], "action")], outcome="completed",
            result_ref=action_path.relative_to(ROOT).as_posix(), effect_refs=effect_refs,
        ))
        events.append(_event(
            execution, event_id=f"event-completed-step-{index}", event_name="completed", run=step,
            bindings=[_binding(step["definition"], "step")], outcome="completed",
            result_ref=f".caprmedio_install/workflow_orchestrator/runs/{RUN_ID}/graph_result.json",
        ))
        contexts[offset] = SimpleNamespace(
            workflow_run_id=workflow["run_id"], step_run_id=step["run_id"], action_run_id=action["run_id"],
            step_atom_id=step_atom_id, action_atom_id=action_atom_id,
        )
        results[offset] = SimpleNamespace(
            outcome="completed", effect_outcome=None, shared_action_recording=None,
            effect_evidence_refs=tuple(effect_refs),
        )
        step_results.append({"effect_refs": effect_refs})
    graph_path = folder / "graph_result.json"
    storage[graph_path] = {
        "workflow_run_id": workflow["run_id"], "outcome": "completed", "step_results": step_results,
    }
    events.append(_event(
        execution, event_id="event-completed-workflow", event_name="completed", run=workflow,
        bindings=sorted(all_bindings, key=lambda item: (item["kind"], item["atom_id"], item["version"], item["path"])),
        outcome="completed", result_ref=graph_path.relative_to(ROOT).as_posix(),
        effect_refs=sorted({ref for row in step_results for ref in row["effect_refs"]}),
    ))
    private_run = SimpleNamespace(
        in_progress=None, stopped=False, next_phase=len(PHASES), contexts=contexts, results=results,
    )
    return events, storage, private_run


def _repeated_action_execution() -> dict[str, object]:
    """Two Action occurrences intentionally share one reusable definition."""
    execution = _execution()
    workflow = _definition("CA-O-164", "workflow")
    first_step = _definition("CA-O-170", "step")
    second_step = _definition("CA-O-171", "step")
    shared_action = _definition("CA-O-165", "action")
    execution["requested_runs"] = [
        {"requested_run_id": RUN_ID, "kind": "workflow", "definition": workflow},
        {
            "requested_run_id": f"{RUN_ID}:step:1", "kind": "step", "definition": first_step,
            "parent_requested_run_id": RUN_ID,
        },
        {
            "requested_run_id": f"{RUN_ID}:step:1:action:1", "kind": "action", "definition": shared_action,
            "parent_requested_run_id": f"{RUN_ID}:step:1",
        },
        {
            "requested_run_id": f"{RUN_ID}:step:2", "kind": "step", "definition": second_step,
            "parent_requested_run_id": RUN_ID,
        },
        {
            "requested_run_id": f"{RUN_ID}:step:2:action:1", "kind": "action", "definition": shared_action,
            "parent_requested_run_id": f"{RUN_ID}:step:2",
        },
    ]
    return execution


def _repeated_action_pending_case(
    execution: Mapping[str, object],
) -> tuple[list[dict[str, object]], dict[Path, object], SimpleNamespace, dict[str, object]]:
    """One already-canonical pending receipt for the second shared Action."""
    requested = execution["requested_runs"]
    workflow = {"run_id": "actual-workflow", "kind": "workflow", "definition": requested[0]["definition"]}
    first_step = {
        "run_id": "actual-step-1", "kind": "step", "definition": requested[1]["definition"],
        "parent_run_id": workflow["run_id"],
    }
    first_action = {
        "run_id": "actual-action-1", "kind": "action", "definition": requested[2]["definition"],
        "parent_run_id": first_step["run_id"],
    }
    second_step = {
        "run_id": "actual-step-2", "kind": "step", "definition": requested[3]["definition"],
        "parent_run_id": workflow["run_id"],
    }
    second_action = {
        "run_id": "actual-action-2", "kind": "action", "definition": requested[4]["definition"],
        "parent_run_id": second_step["run_id"],
    }
    all_bindings = RunExecutionSession.canonical_requested_definition_bindings(requested)
    workflow_bindings = sorted(
        all_bindings, key=lambda item: (item["kind"], item["atom_id"], item["version"], item["path"]),
    )
    events = [_event(
        execution, event_id="event-start-workflow", event_name="started", run=workflow,
        bindings=workflow_bindings,
    )]
    for ordinal, run in enumerate((first_step, first_action, second_step, second_action), start=1):
        events.append(_event(
            execution, event_id=f"event-start-{ordinal}", event_name="started", run=run,
            bindings=[_binding(run["definition"], run["kind"])],
        ))
    events.append(_event(
        execution, event_id="event-interrupted-workflow", event_name="interrupted", run=workflow,
        bindings=workflow_bindings, outcome="interrupted_pending",
    ))
    folder = ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID
    requested_action = f"{RUN_ID}:step:2:action:1"
    progress_path = folder / f"{requested_action}.json"
    completed = _event(
        execution, event_id="event-completed-second-action", event_name="completed", run=second_action,
        bindings=[_binding(second_action["definition"], "action")], outcome="completed",
        result_ref=progress_path.relative_to(ROOT).as_posix(), effect_refs=[],
    )
    events.append(completed)
    storage: dict[Path, object] = {
        folder / "release_action_run.json": {"checkpoint": "ignored"},
        progress_path: {"action_run_id": second_action["run_id"], "effect_refs": []},
    }
    private_run = SimpleNamespace(
        in_progress=None, stopped=False, next_phase=0, results={}, contexts={
            0: SimpleNamespace(
                workflow_run_id=workflow["run_id"], step_run_id=second_step["run_id"],
                action_run_id=second_action["run_id"], step_atom_id="CA-O-171", action_atom_id="CA-O-165",
            ),
        },
    )
    packet = {"event_id": completed["event_id"], "event_outcome": "completed"}
    return events, storage, private_run, packet


class _Tracker:
    def __init__(self, execution: Mapping[str, object], *, current: bool = True) -> None:
        self.execution = dict(execution)
        self.current = current
        self.appended: list[dict[str, object]] = []
        self.validated = 0

    def _observe(self, _execution: Mapping[str, object]) -> dict[str, object]:
        return {"selected": True, "current": self.current, "observed": {"current": self.current}}

    def _validate_execute(self, *_args: object) -> None:
        self.validated += 1

    def _session_result(self, request: Mapping[str, object], proposal: Mapping[str, object], session: Any) -> dict[str, object]:
        return LazyRunTracker._session_result(self, request, proposal, session)

    def _lazy_journal_event(
        self, request: Mapping[str, object], run: Mapping[str, object], event_name: str,
        outcome: str | None, result_ref: str | None, effect_refs: list[str], report_ref: str | None,
        bindings: list[dict[str, object]],
    ) -> dict[str, object]:
        return _event(
            request,
            event_id=f"event-new-{len(self.appended) + 1}",
            event_name=event_name,
            run=run,
            bindings=bindings,
            outcome=outcome,
            result_ref=result_ref,
            effect_refs=effect_refs,
        )

    def _append_one(
        self, event: Mapping[str, object], _result_ref: str | None, _effect_refs: list[str],
    ) -> dict[str, object]:
        saved = dict(event)
        self.appended.append(saved)
        return {
            "event_id": saved["event_id"],
            "action_id": saved["action_id"],
            "event_digest": saved["event_digest"],
            "carrier": f"memory/appended-{len(self.appended)}.ndjson",
            "line": 1,
            "previous_carrier_digest": "0" * 64,
            "appended_carrier_digest": "0" * 64,
        }


class ReleaseRecoveryExecutorTests(unittest.TestCase):
    def _runner(
        self, frozen: Mapping[str, object], tracker: _Tracker, storage: dict[Path, object],
    ) -> SelectedExecution:
        runner = SelectedExecution.__new__(SelectedExecution)
        runner.root = ROOT
        runner.handlers = {}
        runner.implementation_agent = None
        runner.run_directory = lambda _run_id: ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID
        runner._revalidate = lambda _frozen: frozen["graph"]
        runner._shared_tracker = lambda _frozen: tracker
        runner._read = lambda path: storage[Path(path)]
        runner._write = lambda path, value: storage.__setitem__(Path(path), value)
        return runner

    def test_recovery_reuses_started_ids_without_second_start(self) -> None:
        execution = _execution()
        frozen = _frozen(execution)
        starts = _start_events(execution)
        workflow, _step, action = _runs(execution)
        interrupted = _event(
            execution, event_id="event-interrupted-workflow", event_name="interrupted", run=workflow,
            bindings=starts[0]["definition_bindings"], outcome="interrupted_pending",
        )
        completed_action = _event(
            execution, event_id="event-completed-action", event_name="completed", run=action,
            bindings=starts[2]["definition_bindings"], outcome="completed",
            result_ref=(ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID
                        / f"{RUN_ID}:step:1:action:1.json").relative_to(ROOT).as_posix(),
        )
        evidence = _evidence([*starts, interrupted, completed_action])
        checkpoint_path = ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID / "release_action_run.json"
        progress_path = ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID / f"{RUN_ID}:step:1:action:1.json"
        storage: dict[Path, object] = {checkpoint_path: {"checkpoint": "ignored"}, progress_path: {
            "action_run_id": "actual-action", "effect_refs": [],
        }}
        tracker = _Tracker(execution)
        runner = self._runner(frozen, tracker, storage)
        runner._execute_graph = mock.Mock()
        recovered: list[str] = []
        with (
            mock.patch.object(selected_run_recovery, "read_selected_run_evidence", return_value=evidence),
            mock.patch.object(release_checkpoint, "load_release_checkpoint", return_value=(
                SimpleNamespace(in_progress=None, contexts={}, results={}, next_phase=0), {},
            )),
            mock.patch.object(release_checkpoint, "extract_pending_recordings", return_value={}),
            mock.patch.object(work_journal, "_event_lock", return_value=nullcontext()),
            mock.patch.object(work_journal, "recover_pending_event", side_effect=lambda _root, event_id: recovered.append(event_id)),
        ):
            result = runner.recover_release(frozen)

        self.assertEqual("started", result["disposition"])
        self.assertEqual([], recovered)
        self.assertNotIn("started", [event["event"] for event in tracker.appended])
        runner._execute_graph.assert_called_once()
        restored_session = runner._execute_graph.call_args.args[1]
        self.assertEqual("actual-action", restored_session.actual[f"{RUN_ID}:step:1:action:1"]["run_id"])
        self.assertEqual("completed", restored_session.terminal[f"{RUN_ID}:step:1:action:1"]["outcome"])

    def test_stale_source_blocks_before_canonical_read_or_recovery(self) -> None:
        execution = _execution()
        frozen = _frozen(execution)
        checkpoint_path = ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID / "release_action_run.json"
        reader = mock.Mock()
        tracker = _Tracker(execution, current=False)
        runner = self._runner(frozen, tracker, {checkpoint_path: {"checkpoint": "ignored"}})

        with mock.patch.object(selected_run_recovery, "read_selected_run_evidence", reader):
            with self.assertRaisesRegex(SelectedExecutionError, "source admission is not current"):
                runner.recover_release(frozen)

        reader.assert_not_called()
        self.assertEqual([], tracker.appended)

    def test_missing_canonical_workflow_start_blocks_before_any_native_resume(self) -> None:
        execution = _execution()
        frozen = _frozen(execution)
        checkpoint_path = ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID / "release_action_run.json"
        tracker = _Tracker(execution)
        runner = self._runner(frozen, tracker, {checkpoint_path: {"checkpoint": "ignored"}})
        native_calls: list[object] = []
        runner.handlers = {"CA-O-165": lambda context: native_calls.append(context) or {"result": "done", "effect_refs": []}}

        with (
            mock.patch.object(selected_run_recovery, "read_selected_run_evidence", return_value=_evidence([])),
            mock.patch.object(release_checkpoint, "load_release_checkpoint", return_value=(
                SimpleNamespace(in_progress=None, contexts={}, results={}, next_phase=0), {},
            )),
            mock.patch.object(release_checkpoint, "extract_pending_recordings", return_value={}),
            mock.patch.object(work_journal, "_event_lock", return_value=nullcontext()),
        ):
            with self.assertRaisesRegex(SelectedExecutionError, "no canonical Workflow start"):
                runner.recover_release(frozen)

        self.assertEqual([], native_calls)
        self.assertEqual([], tracker.appended)

    def test_pending_action_recording_recovers_the_original_event_before_resuming_without_effect(self) -> None:
        execution = _execution()
        frozen = _frozen(execution)
        starts = _start_events(execution)
        workflow, _step, action = _runs(execution)
        interrupted = _event(
            execution, event_id="event-interrupted-workflow", event_name="interrupted", run=workflow,
            bindings=starts[0]["definition_bindings"], outcome="interrupted_pending",
        )
        pending = _event(
            execution, event_id="event-pending-action", event_name="completed", run=action,
            bindings=starts[2]["definition_bindings"], outcome="completed",
            result_ref=(ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID
                        / f"{RUN_ID}:step:1:action:1.json").relative_to(ROOT).as_posix(),
        )
        before = _evidence([*starts, interrupted])
        after = _evidence([*starts, interrupted, pending])
        checkpoint_path = ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID / "release_action_run.json"
        progress_path = ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID / f"{RUN_ID}:step:1:action:1.json"
        storage: dict[Path, object] = {checkpoint_path: {"checkpoint": "ignored"}, progress_path: {
            "action_run_id": "actual-action", "effect_refs": [],
        }}
        tracker = _Tracker(execution)
        runner = self._runner(frozen, tracker, storage)
        runner._execute_graph = mock.Mock()
        recovered_ids: list[str] = []

        with (
            mock.patch.object(selected_run_recovery, "read_selected_run_evidence", side_effect=[before, after]),
            mock.patch.object(release_checkpoint, "load_release_checkpoint", return_value=(
                SimpleNamespace(
                    in_progress=None, next_phase=0, results={}, contexts={
                        0: SimpleNamespace(
                            workflow_run_id="actual-workflow", step_run_id="actual-step",
                            action_run_id="actual-action", step_atom_id="CA-O-170", action_atom_id="CA-O-165",
                        ),
                    },
                ), {},
            )),
            mock.patch.object(release_checkpoint, "extract_pending_recordings", return_value={
                0: {"event_id": "event-pending-action", "event_outcome": "completed"},
            }),
            mock.patch.object(work_journal, "_event_lock", return_value=nullcontext()),
            mock.patch.object(work_journal, "_read_pending_event", return_value=(
                {"result_ref": pending["result_ref"], "effect_refs": []}, pending, {}, ROOT / "pending.json",
            )),
            mock.patch.object(work_journal, "recover_pending_event", side_effect=lambda _root, event_id: recovered_ids.append(event_id)),
        ):
            result = runner.recover_release(frozen)

        self.assertEqual("started", result["disposition"])
        self.assertEqual(["event-pending-action"], recovered_ids)
        self.assertNotIn("started", [event["event"] for event in tracker.appended])
        runner._execute_graph.assert_called_once()

    def test_terminal_workflow_reuses_only_a_complete_ten_phase_proof(self) -> None:
        execution = _full_release_execution()
        frozen = _full_release_frozen(execution)
        events, storage, private_run = _full_release_evidence(execution)
        checkpoint_path = ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID / "release_action_run.json"
        storage[checkpoint_path] = {"checkpoint": "ignored"}
        tracker = _Tracker(execution)
        runner = self._runner(frozen, tracker, storage)
        runner._execute_graph = mock.Mock()

        with (
            mock.patch.object(selected_run_recovery, "read_selected_run_evidence", return_value=_evidence(events)),
            mock.patch.object(release_checkpoint, "load_release_checkpoint", return_value=(
                private_run, {},
            )),
            mock.patch.object(release_checkpoint, "extract_pending_recordings", return_value={}),
            mock.patch.object(release_checkpoint, "dump_release_checkpoint", return_value={"sealed": "checkpoint"}),
            mock.patch.object(work_journal, "_event_lock", return_value=nullcontext()),
        ):
            result = runner.recover_release(frozen)

        self.assertEqual("terminal", result["disposition"])
        runner._execute_graph.assert_not_called()
        self.assertEqual([], tracker.appended)

    def test_completed_workflow_with_incomplete_frontier_is_rejected(self) -> None:
        execution = _execution()
        frozen = _frozen(execution)
        starts = _start_events(execution)
        workflow, step, action = _runs(execution)
        action_result = (ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID
                         / f"{RUN_ID}:step:1:action:1.json").relative_to(ROOT).as_posix()
        graph_result = (ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID
                        / "graph_result.json").relative_to(ROOT).as_posix()
        events = [
            *starts,
            _event(execution, event_id="event-completed-action", event_name="completed", run=action,
                   bindings=starts[2]["definition_bindings"], outcome="completed", result_ref=action_result),
            _event(execution, event_id="event-completed-step", event_name="completed", run=step,
                   bindings=starts[1]["definition_bindings"], outcome="completed", result_ref=graph_result),
            _event(execution, event_id="event-completed-workflow", event_name="completed", run=workflow,
                   bindings=starts[0]["definition_bindings"], outcome="completed", result_ref=graph_result),
        ]
        checkpoint_path = ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID / "release_action_run.json"
        tracker = _Tracker(execution)
        runner = self._runner(frozen, tracker, {checkpoint_path: {"checkpoint": "ignored"}})
        runner._validate_release_saved_result = mock.Mock()
        runner._execute_graph = mock.Mock()

        with (
            mock.patch.object(selected_run_recovery, "read_selected_run_evidence", return_value=_evidence(events)),
            mock.patch.object(release_checkpoint, "load_release_checkpoint", return_value=(
                SimpleNamespace(in_progress=None, next_phase=0, contexts={}, results={}), {},
            )),
            mock.patch.object(release_checkpoint, "extract_pending_recordings", return_value={}),
            mock.patch.object(work_journal, "_event_lock", return_value=nullcontext()),
        ):
            with self.assertRaisesRegex(SelectedExecutionError, "complete ten-phase typed frontier"):
                runner.recover_release(frozen)

        runner._execute_graph.assert_not_called()

    def test_canonical_pending_uses_actual_occurrence_not_repeated_action_definition(self) -> None:
        execution = _repeated_action_execution()
        frozen = _frozen(execution)
        events, storage, private_run, packet = _repeated_action_pending_case(execution)
        tracker = _Tracker(execution)
        runner = self._runner(frozen, tracker, storage)
        runner._execute_graph = mock.Mock()
        recover = mock.Mock()

        with (
            mock.patch.object(selected_run_recovery, "read_selected_run_evidence", return_value=_evidence(events)),
            mock.patch.object(release_checkpoint, "load_release_checkpoint", return_value=(private_run, {})),
            mock.patch.object(release_checkpoint, "extract_pending_recordings", return_value={0: packet}),
            mock.patch.object(work_journal, "_event_lock", return_value=nullcontext()),
            mock.patch.object(work_journal, "_read_pending_event") as read_pending,
            mock.patch.object(work_journal, "recover_pending_event", recover),
        ):
            result = runner.recover_release(frozen)

        self.assertEqual("started", result["disposition"])
        read_pending.assert_not_called()
        recover.assert_not_called()
        runner._execute_graph.assert_called_once()

    def test_tampered_canonical_pending_is_rejected_before_resume(self) -> None:
        cases = (
            ("outcome", "pending checkpoint outcome differs", lambda _storage, _run, packet: packet.update(event_outcome="failed")),
            ("phase", "pending event differs", lambda _storage, run, _packet: setattr(run.contexts[0], "action_run_id", "other-action")),
            (
                "progress", "pending Release Action does not match",
                lambda storage, _run, _packet: storage.__setitem__(
                    ROOT / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID / f"{RUN_ID}:step:2:action:1.json",
                    {"action_run_id": "actual-action-2", "effect_refs": ["tampered"]},
                ),
            ),
        )
        for label, error, tamper in cases:
            with self.subTest(label=label):
                execution = _repeated_action_execution()
                frozen = _frozen(execution)
                events, storage, private_run, packet = _repeated_action_pending_case(execution)
                tamper(storage, private_run, packet)
                tracker = _Tracker(execution)
                runner = self._runner(frozen, tracker, storage)
                runner._execute_graph = mock.Mock()
                recover = mock.Mock()

                with (
                    mock.patch.object(selected_run_recovery, "read_selected_run_evidence", return_value=_evidence(events)),
                    mock.patch.object(release_checkpoint, "load_release_checkpoint", return_value=(private_run, {})),
                    mock.patch.object(release_checkpoint, "extract_pending_recordings", return_value={0: packet}),
                    mock.patch.object(work_journal, "_event_lock", return_value=nullcontext()),
                    mock.patch.object(work_journal, "recover_pending_event", recover),
                ):
                    with self.assertRaisesRegex(SelectedExecutionError, error):
                        runner.recover_release(frozen)

                recover.assert_not_called()
                runner._execute_graph.assert_not_called()


if __name__ == "__main__":
    unittest.main()
