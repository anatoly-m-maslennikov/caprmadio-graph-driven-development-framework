"""Focused W01 canonical-add evidence and W01-to-W03 composition tests."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
REPOSITORY = APP.parents[3]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, APP / "tests", TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_execution import SelectedExecution, build_requested_runs  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402


class _Tracker:
    journal_context = {"author": "golden-operator", "timezone": "UTC"}


class _Session:
    """Narrow shared-session stand-in retaining the actual effect observation."""

    def __init__(self, requested_runs: list[dict[str, object]]) -> None:
        self.requested = {row["requested_run_id"]: row for row in requested_runs}
        self.actual: dict[str, dict[str, object]] = {}
        self.terminal: dict[str, dict[str, object]] = {}
        self.interrupted: dict[str, dict[str, object]] = {}
        self.observed: dict[str, dict[str, object]] = {}
        self.pending: list[str] = []
        self.receipts: list[dict[str, object]] = []
        self.tracker = _Tracker()

    def start_run(self, requested_run_id: str) -> dict[str, object]:
        existing = self.actual.get(requested_run_id)
        if existing is not None:
            return dict(existing)
        row = self.requested[requested_run_id]
        record: dict[str, object] = {
            "run_id": requested_run_id,
            "kind": row["kind"],
            "definition": row["definition"],
        }
        parent = row.get("parent_requested_run_id")
        if parent is not None:
            if parent not in self.actual:
                raise AssertionError(f"child {requested_run_id} started before parent {parent}")
            record["parent_run_id"] = self.actual[parent]["run_id"]
        self.actual[requested_run_id] = record
        return dict(record)

    def note_effects(self, run_id: str, *, result_ref: str, effect_refs: list[str]) -> None:
        requested = next(key for key, value in self.actual.items() if value["run_id"] == run_id)
        self.observed[requested] = {"result_ref": result_ref, "effect_refs": list(effect_refs)}

    def finish_run(self, run_id: str, **result: object) -> dict[str, object]:
        requested = next(key for key, value in self.actual.items() if value["run_id"] == run_id)
        observed = self.observed.get(requested)
        if observed is not None:
            if observed["result_ref"] != result.get("result_ref") or observed["effect_refs"] != result.get("effect_refs"):
                raise AssertionError("terminal record lost observed creation effects")
        receipt = {"run_id": run_id, "disposition": "terminal", **result}
        self.terminal[requested] = receipt
        return dict(receipt)


class _PendingChildSession(_Session):
    """Model a child terminal writer that retained, but did not seal, its fact."""

    def __init__(self, requested_runs: list[dict[str, object]], pending_child: str) -> None:
        super().__init__(requested_runs)
        self.pending_child = pending_child

    def finish_run(self, run_id: str, **result: object) -> dict[str, object]:
        requested = next(key for key, value in self.actual.items() if value["run_id"] == run_id)
        if requested != self.pending_child:
            return super().finish_run(run_id, **result)
        observed = self.observed.get(requested)
        if observed is None or observed["result_ref"] != result.get("result_ref") or observed["effect_refs"] != result.get("effect_refs"):
            raise AssertionError("pending child lost observed creation effects")
        receipt = {"run_id": run_id, "disposition": "recording_pending", **result}
        self.interrupted[requested] = receipt
        return dict(receipt)


class SelectedCreationExecutionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.w01 = GoldenProject(REPOSITORY, self.root, GoldenCase("W01", "create_atom"))
        self.manifest = self.w01.prepare()
        self.selected = SelectedExecution(self.root)

    def _graph(self, route: str) -> dict[str, object]:
        return self.selected._validate_graph({
            "mode": "execute",
            "operation_route": route,
            "source_freshness": self.manifest["source_freshness"],
            "definition_manifest": {
                "manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
                "manifest_digest": self.manifest["canonical_manifest_sha256"],
            },
        })

    def _frozen(
        self, route: str, parameters: dict[str, object], run_id: str,
    ) -> tuple[dict[str, object], _Session]:
        graph = self._graph(route)
        requested = build_requested_runs(graph, run_id)
        execution = {
            "request_id": f"{run_id}-request",
            "parameters": parameters,
            "requested_runs": requested,
        }
        return {"graph": graph, "request": {"run_id": run_id, "execution": execution}}, _Session(requested)

    @staticmethod
    def _events(root: Path) -> list[dict[str, object]]:
        events: list[dict[str, object]] = []
        for path in sorted((root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")):
            events.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line)
        return events

    def test_real_create_records_canonical_add_that_unblocks_real_replace(self) -> None:
        create_parameters = self.w01.native_parameters()
        create_frozen, create_session = self._frozen("create_atom", create_parameters, "w01-create")
        requested = create_frozen["request"]["execution"]["requested_runs"]
        actions = [row for row in requested if row["kind"] == "action"]
        self.assertEqual(["CA-O-128", "CA-O-032"], [row["definition"]["atom_id"] for row in actions])
        parent_id = "w01-create:step:1:action:1"
        creation_child_id = f"{parent_id}:nested:CA-O-032"
        child = next(row for row in actions if row["requested_run_id"] == creation_child_id)
        self.assertEqual(parent_id, child["parent_requested_run_id"])
        self.assertFalse(any("CA-O-051" in row["requested_run_id"] for row in requested))

        create_result = self.selected._execute_graph(create_frozen, create_session)

        self.assertEqual("completed", create_result["outcome"])
        create_action_id = creation_child_id
        creation = next(event for event in self._events(self.root)
                        if event.get("event_id") == f"selected-creation:{create_action_id}")
        child_result = self.root / ".caprmedio_install/workflow_orchestrator/runs/w01-create" / f"{create_action_id}.json"
        created = json.loads(child_result.read_text(encoding="utf-8"))["native_result"]["observed"]
        self.assertEqual("CA-O-032", creation["action_id"])
        self.assertEqual("ADD", creation["action_type"])
        self.assertEqual(create_parameters["carrier"]["path"], creation["result"]["path"])
        self.assertEqual(created["path"], creation["result"]["path"])
        self.assertEqual(created["digest"], creation["result"]["sha256"])

        w03 = GoldenProject(REPOSITORY, self.root, GoldenCase("W03", "replace_atom"))
        w03.manifest = self.manifest
        replace_parameters = w03.native_parameters()
        replace_parameters["predecessor"] = dict(created)
        replace_frozen, replace_session = self._frozen("replace_atom", replace_parameters, "w03-after-create")

        replace_result = self.selected._execute_graph(replace_frozen, replace_session)

        self.assertEqual("completed", replace_result["outcome"])
        replacement = next(event for event in self._events(self.root)
                           if event.get("event_id") == "selected-replacement:w03-after-create:step:1:action:1:nested:CA-O-051")
        self.assertEqual(creation["event_id"], replacement["previous_result_event"])
        self.assertEqual(created["atom_id"], replacement["predecessor_atom_id"])

    def test_create_append_pending_is_partial_and_retains_effect_without_replay(self) -> None:
        parameters = self.w01.native_parameters()
        frozen, session = self._frozen("create_atom", parameters, "w01-append-pending")
        parent_id = "w01-append-pending:step:1:action:1"
        action_id = f"{parent_id}:nested:CA-O-032"

        with patch("selected_creation_journal.append_sealed_events", side_effect=OSError("full")):
            result = self.selected._execute_graph(frozen, session)

        self.assertEqual("partial", result["outcome"])
        self.assertEqual("recording-pending", result["step_results"][0]["result"])
        self.assertEqual("partial", session.terminal[parent_id]["outcome"])
        self.assertEqual("partial", session.terminal[action_id]["outcome"])
        self.assertTrue(session.observed[action_id]["effect_refs"])
        self.assertTrue((self.root / parameters["carrier"]["path"]).is_file())
        self.assertFalse(any(event.get("event_id") == f"selected-creation:{action_id}"
                             for event in self._events(self.root)))
        pending = list((self.root / ".caprmedio_runtime/state/work_journal/pending").glob("*.json"))
        self.assertTrue(pending, "exact canonical Create event must remain recoverable")

    def test_child_terminal_recording_pending_never_exposes_applied_completion(self) -> None:
        parameters = self.w01.native_parameters()
        frozen, _ = self._frozen("create_atom", parameters, "w01-child-pending")
        parent_id = "w01-child-pending:step:1:action:1"
        action_id = f"{parent_id}:nested:CA-O-032"
        requested = frozen["request"]["execution"]["requested_runs"]
        session = _PendingChildSession(requested, action_id)

        result = self.selected._execute_graph(frozen, session)

        self.assertEqual("partial", result["outcome"])
        self.assertEqual("recording-pending", result["step_results"][0]["result"])
        self.assertEqual("recording_pending", session.interrupted[action_id]["disposition"])
        self.assertTrue(session.observed[action_id]["effect_refs"])
        self.assertTrue(any(event.get("event_id") == f"selected-creation:{action_id}"
                            for event in self._events(self.root)))


if __name__ == "__main__":
    unittest.main()
