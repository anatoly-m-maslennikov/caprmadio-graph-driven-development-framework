"""Public selected-Workflow status derives only from its canonical terminal."""
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest import mock


APP = Path(__file__).resolve().parents[1]
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(APP))

import backend  # noqa: E402


RUN_ID = "selected-status-run"


def _frozen() -> dict[str, object]:
    return {
        "request": {
            "run_id": RUN_ID,
            "execution": {
                "requested_runs": [
                    {"requested_run_id": RUN_ID, "kind": "workflow", "definition": {}},
                    {"requested_run_id": f"{RUN_ID}:step:1", "kind": "step", "definition": {}},
                    {"requested_run_id": f"{RUN_ID}:step:1:action:1", "kind": "action", "definition": {}},
                ],
            },
        },
        "graph": {"workflow": {"atom_id": "CA-O-127"}, "route": "create_atom"},
    }


def _terminal(run_id: str, outcome: str, **extra: object) -> dict[str, object]:
    return {"run_id": run_id, "disposition": "terminal", "outcome": outcome, **extra}


class SelectedPublicStatusTests(unittest.TestCase):
    def status(self, result: dict[str, object]) -> dict[str, object]:
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True) as directory:
            root = Path(directory)
            selected_directory = root / "selected"
            selected_directory.mkdir()
            (selected_directory / "selected_request.json").touch()
            (selected_directory / "accepted.json").touch()
            selected = mock.Mock()
            selected.run_directory.return_value = selected_directory
            selected._read.side_effect = [_frozen(), {"result": result}]
            scheduler = types.SimpleNamespace(status="SUCCESS")
            handle = mock.Mock()
            handle.get_status.return_value = scheduler
            transport = mock.Mock()
            transport.retrieve_workflow.return_value = handle
            with mock.patch.object(backend, "SelectedExecution", return_value=selected), \
                    mock.patch.object(backend, "client", return_value=transport):
                observed = backend.status(root, {"operation": "status", "run_id": RUN_ID})
        self.assertEqual("SUCCESS", observed["scheduler_status"])
        self.assertIs(observed["selected_result"], result)
        transport.destroy.assert_called_once()
        return observed

    def test_completed_workflow_terminal_wins_over_scheduler_and_action_outcome(self):
        result = {
            "disposition": "terminal",
            "terminal_runs": [
                _terminal(f"{RUN_ID}:step:1:action:1", "failed"),
                _terminal(RUN_ID, "completed"),
            ],
        }

        observed = self.status(result)

        self.assertEqual(("terminal", "completed"), (observed["disposition"], observed["outcome"]))

    def test_partial_and_failed_workflow_terminals_are_preserved(self):
        for outcome in ("partial", "failed"):
            with self.subTest(outcome=outcome):
                observed = self.status({
                    "disposition": "terminal",
                    "terminal_runs": [_terminal(RUN_ID, outcome)],
                })
                self.assertEqual(("terminal", outcome), (observed["disposition"], observed["outcome"]))

    def test_missing_ambiguous_and_mismatched_workflow_evidence_fails_closed(self):
        cases = {
            "missing": [_terminal(f"{RUN_ID}:step:1:action:1", "completed")],
            "ambiguous": [_terminal(RUN_ID, "completed"), _terminal(RUN_ID, "failed")],
            "mismatched-kind": [_terminal(RUN_ID, "completed", kind="action")],
        }
        for name, terminal_runs in cases.items():
            with self.subTest(name=name):
                observed = self.status({"disposition": "terminal", "terminal_runs": terminal_runs})
                self.assertEqual(("terminal", "failed"), (observed["disposition"], observed["outcome"]))
                self.assertIn("canonical Workflow terminal evidence", observed["reason"])

    def test_legacy_direct_outcome_and_recording_pending_envelopes_remain_unchanged(self):
        legacy = self.status({"disposition": "terminal", "outcome": "completed"})
        pending = self.status({
            "disposition": "recording_pending",
            "outcome": "interrupted_pending",
            "terminal_runs": [_terminal(RUN_ID, "completed")],
        })

        self.assertEqual(("terminal", "completed"), (legacy["disposition"], legacy["outcome"]))
        self.assertEqual(("recording_pending", "interrupted_pending"),
                         (pending["disposition"], pending["outcome"]))


if __name__ == "__main__":
    unittest.main()
