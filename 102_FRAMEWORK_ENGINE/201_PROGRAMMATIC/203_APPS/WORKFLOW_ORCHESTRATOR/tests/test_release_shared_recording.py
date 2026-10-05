"""Pure Release shared-recording graph guards.

These tests retain all graph state in memory.  They do not create a fixture,
write a carrier, invoke Docker, or call the canonical Journal implementation.
"""
from __future__ import annotations

from pathlib import Path
import sys
import unittest
from typing import Any, Mapping


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

from selected_execution import SelectedExecution  # noqa: E402


ROOT = Path("/project")
RUN_ID = "release-run"


def _binding(atom_id: str, kind: str) -> dict[str, object]:
    return {
        "atom_id": atom_id,
        "kind": kind,
        "version": 1,
        "path": f"definitions/{atom_id}.md",
        "sha256": "a" * 64,
    }


def _step(atom_id: str, action_id: str, result: str, transition: dict[str, str]) -> dict[str, object]:
    return {
        **_binding(atom_id, "step"),
        "actions": [{**_binding(action_id, "action"), "result_map": {result: result}}],
        "on_result": [{"result": result, **transition}],
    }


def _frozen(steps: list[dict[str, object]]) -> dict[str, object]:
    return {
        "graph": {
            "route": "release_version",
            "workflow": _binding("CA-O-164", "workflow"),
            "entry_step": steps[0]["atom_id"],
            "steps": steps,
        },
        "request": {
            "run_id": RUN_ID,
            "execution": {"parameters": {}, "target_frontier": [], "effects": [], "initiative": {}},
        },
    }


class MemorySession:
    """Shared tracker double with controllable Action terminal receipts."""

    def __init__(self, action_receipt: Mapping[str, object]) -> None:
        self.action_receipt = dict(action_receipt)
        self.started: list[str] = []
        self.finished: list[dict[str, object]] = []
        self.action_run_ids: set[str] = set()

    def start_run(self, requested_run_id: str) -> dict[str, object]:
        self.started.append(requested_run_id)
        run_id = f"actual-{len(self.started)}"
        if ":action:" in requested_run_id:
            self.action_run_ids.add(run_id)
        return {"run_id": run_id}

    def finish_run(self, run_id: str, **result: object) -> dict[str, object]:
        saved = {"run_id": run_id, **result}
        self.finished.append(saved)
        if run_id in self.action_run_ids:
            return dict(self.action_receipt)
        return {"disposition": "terminal", "outcome": result.get("outcome"), **saved}


def _runner(handlers: Mapping[str, Any]) -> tuple[SelectedExecution, list[tuple[Path, object]]]:
    """Use the production interpreter with only carrier I/O replaced."""
    runner = SelectedExecution.__new__(SelectedExecution)
    runner.root = ROOT
    runner.handlers = dict(handlers)
    runner.implementation_agent = None
    writes: list[tuple[Path, object]] = []
    runner.run_directory = lambda _run_id: ROOT / ".caprmedio_install/runs" / _run_id
    runner._write = lambda path, value: writes.append((path, value))
    runner._prepare_journal_query_before_run = lambda _graph, _execution: None
    return runner, writes


def _release_handler(*, shared: bool = False) -> dict[str, object]:
    value: dict[str, object] = {"result": "completed", "effect_refs": []}
    if shared:
        value["shared_action_recording"] = {"on_recorded_result": "completed"}
    return value


class ReleaseSharedRecordingTests(unittest.TestCase):
    def test_final_completion_requires_the_exact_shared_action_terminal_receipt(self) -> None:
        final = _step("CA-O-179", "CA-O-169", "completed", {"terminal": "completed"})
        runner, writes = _runner({"CA-O-169": lambda _context: _release_handler(shared=True)})
        progress_ref = ".caprmedio_install/runs/release-run/release-run:step:1:action:1.json"
        session = MemorySession({
            "disposition": "terminal", "outcome": "completed", "run_id": "actual-3",
            "result_ref": progress_ref, "effect_refs": [],
        })

        result = runner._execute_graph(_frozen([final]), session)

        self.assertEqual("completed", result["outcome"])
        self.assertEqual([RUN_ID, f"{RUN_ID}:step:1", f"{RUN_ID}:step:1:action:1"], session.started)
        self.assertTrue(any(value.get("result") == "completed" for _path, value in writes
                            if isinstance(value, dict)))

    def test_final_pending_or_mismatched_receipt_cannot_complete(self) -> None:
        final = _step("CA-O-179", "CA-O-169", "completed", {"terminal": "completed"})
        progress_ref = ".caprmedio_install/runs/release-run/release-run:step:1:action:1.json"
        receipts = {
            "pending": {"disposition": "recording_pending", "outcome": "interrupted_pending"},
            "wrong-ref": {"disposition": "terminal", "outcome": "completed", "run_id": "actual-3",
                          "result_ref": "wrong.json", "effect_refs": []},
            "wrong-effects": {"disposition": "terminal", "outcome": "completed", "run_id": "actual-3",
                              "result_ref": progress_ref, "effect_refs": ["unexpected"]},
        }
        for label, receipt in receipts.items():
            with self.subTest(receipt=label):
                runner, _writes = _runner({"CA-O-169": lambda _context: _release_handler(shared=True)})
                session = MemorySession(receipt)

                result = runner._execute_graph(_frozen([final]), session)

                self.assertEqual("interrupted_pending", result["outcome"])
                self.assertEqual([RUN_ID, f"{RUN_ID}:step:1", f"{RUN_ID}:step:1:action:1"], session.started)

    def test_intermediate_pending_receipt_stops_before_the_next_release_phase(self) -> None:
        first = _step("CA-O-170", "CA-O-165", "frozen", {"next": "CA-O-179"})
        final = _step("CA-O-179", "CA-O-169", "completed", {"terminal": "completed"})
        calls: list[str] = []

        def first_handler(_context: dict[str, object]) -> dict[str, object]:
            calls.append("first")
            return {"result": "frozen", "effect_refs": []}

        def final_handler(_context: dict[str, object]) -> dict[str, object]:
            calls.append("final")
            return _release_handler(shared=True)

        runner, _writes = _runner({"CA-O-165": first_handler, "CA-O-169": final_handler})
        session = MemorySession({"disposition": "recording_pending", "outcome": "interrupted_pending"})

        result = runner._execute_graph(_frozen([first, final]), session)

        self.assertEqual("interrupted_pending", result["outcome"])
        self.assertEqual(["first"], calls)
        self.assertEqual([RUN_ID, f"{RUN_ID}:step:1", f"{RUN_ID}:step:1:action:1"], session.started)


if __name__ == "__main__":
    unittest.main()
