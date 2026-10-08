"""Focused non-Docker guards for W04 terminal-outcome assertions."""
from __future__ import annotations

import asyncio
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest


TESTS = Path(__file__).resolve().parent
if str(TESTS) not in sys.path:
    sys.path.insert(0, str(TESTS))

from test_selected_workflows_docker_e2e import SelectedWorkflowsDockerEndToEnd


class _StatusFixture:
    case = SimpleNamespace(route="change_atom_status")

    @staticmethod
    def request_for_status(*_args: object, **_kwargs: object) -> dict[str, object]:
        return {"request": "status"}


class SelectedW04TerminalOutcomeAssertions(unittest.TestCase):
    def test_noop_probe_rejects_completed_terminal(self) -> None:
        harness = SelectedWorkflowsDockerEndToEnd(methodName="runTest")
        calls = iter((
            {"disposition": "preview", "proposal_receipt": "receipt", "proposal_receipt_digest": "digest"},
            {"outcome": "queued"},
        ))

        async def call(*_args: object, **_kwargs: object) -> dict[str, object]:
            return next(calls)

        async def terminal(*_args: object, **_kwargs: object) -> dict[str, object]:
            return {"disposition": "terminal", "outcome": "completed"}

        harness._call = call  # type: ignore[method-assign]
        harness._terminal_status = terminal  # type: ignore[method-assign]
        with self.assertRaises(AssertionError):
            asyncio.run(
                harness._execute_status_case(
                    None, Path.cwd(), _StatusFixture(), Path("carrier.md"), "Archived", "w04-noop",
                    expected_outcome="no_op",
                )
            )


if __name__ == "__main__":
    unittest.main()
