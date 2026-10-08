"""Focused W03 execution evidence for O128's nested O051 invocation."""
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
    """A narrow shared-session stand-in which asserts parent Run lineage."""

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
                raise AssertionError("terminal record lost observed replacement effects")
        receipt = {"run_id": run_id, "disposition": "terminal", **result}
        self.terminal[requested] = receipt
        return dict(receipt)


class SelectedReplacementExecutionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.fixture = GoldenProject(REPOSITORY, self.root, GoldenCase("W03", "replace_atom"))
        self.manifest = self.fixture.prepare()
        self.selected = SelectedExecution(self.root)

    def _graph(self) -> dict[str, object]:
        return self.selected._validate_graph({
            "mode": "execute",
            "operation_route": "replace_atom",
            "source_freshness": self.manifest["source_freshness"],
            "definition_manifest": {
                "manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
                "manifest_digest": self.manifest["canonical_manifest_sha256"],
            },
        })

    def _frozen(self, parameters: dict[str, object], run_id: str = "w03-nested") -> tuple[dict[str, object], _Session]:
        graph = self._graph()
        requested = build_requested_runs(graph, run_id)
        execution = {"request_id": f"{run_id}-request", "parameters": parameters,
                     "requested_runs": requested}
        return {"graph": graph, "request": {"run_id": run_id, "execution": execution}}, _Session(requested)

    @staticmethod
    def _events(root: Path) -> list[dict[str, object]]:
        events: list[dict[str, object]] = []
        for path in sorted((root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")):
            events.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line)
        return events

    def test_predeclares_source_pinned_o051_child_and_records_its_parent_lineage(self) -> None:
        parameters = self.fixture.native_parameters()
        frozen, session = self._frozen(parameters)
        requested = frozen["request"]["execution"]["requested_runs"]
        parent_id = "w03-nested:step:1:action:1"
        child_id = f"{parent_id}:nested:CA-O-051"
        child = next(row for row in requested if row["requested_run_id"] == child_id)

        self.assertEqual(parent_id, child["parent_requested_run_id"])
        self.assertEqual("CA-O-051", child["definition"]["atom_id"])
        native_binding = next(item for item in frozen["graph"]["native_action_calls"] if item["atom_id"] == "CA-O-051")
        self.assertEqual(native_binding["sha256"], child["definition"]["digest"])

        result = self.selected._execute_graph(frozen, session)

        self.assertEqual("completed", result["outcome"])
        self.assertEqual(parent_id, session.actual[child_id]["parent_run_id"])
        self.assertEqual("completed", session.terminal[child_id]["outcome"])
        child_result = self.root / ".caprmedio_install/workflow_orchestrator/runs/w03-nested" / f"{child_id}.json"
        self.assertTrue(child_result.is_file())
        replacement = next(event for event in self._events(self.root) if event.get("event_id") == f"selected-replacement:{child_id}")
        self.assertEqual("golden-w03-predecessor", replacement["previous_result_event"])
        self.assertEqual("CA-R-100", replacement["predecessor_atom_id"])
        self.assertEqual(["CA-R-103"], replacement["successor_atom_ids"])

    def test_missing_prior_journal_state_blocks_before_native_replacement_effect(self) -> None:
        for path in (self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"):
            path.unlink()
        parameters = self.fixture.native_parameters()
        predecessor = self.root / parameters["predecessor"]["path"]
        before = predecessor.read_bytes()
        frozen, session = self._frozen(parameters, "w03-missing-prior")

        result = self.selected._execute_graph(frozen, session)

        self.assertEqual("interrupted_pending", result["outcome"])
        self.assertEqual(before, predecessor.read_bytes())
        self.assertFalse((self.root / parameters["successors"][0]["path"]).exists())
        self.assertNotIn("w03-missing-prior:step:1:action:1:nested:CA-O-051", session.actual)

    def test_preserves_all_successor_ids_in_native_order(self) -> None:
        parameters = self.fixture.native_parameters()
        parameters["successors"].append(self.fixture._carrier("CA-R-104", "replacement-two", "Second successor"))
        frozen, session = self._frozen(parameters, "w03-multiple-successors")

        result = self.selected._execute_graph(frozen, session)

        self.assertEqual("completed", result["outcome"])
        child_id = "w03-multiple-successors:step:1:action:1:nested:CA-O-051"
        replacement = next(event for event in self._events(self.root) if event.get("event_id") == f"selected-replacement:{child_id}")
        self.assertEqual(["CA-R-103", "CA-R-104"], replacement["successor_atom_ids"])

    def test_canonical_append_pending_keeps_observed_child_effects_without_success(self) -> None:
        parameters = self.fixture.native_parameters()
        frozen, session = self._frozen(parameters, "w03-append-pending")

        with patch("selected_replacement_journal.append_sealed_events", side_effect=OSError("full")):
            result = self.selected._execute_graph(frozen, session)

        child_id = "w03-append-pending:step:1:action:1:nested:CA-O-051"
        self.assertEqual("partial", result["outcome"])
        self.assertEqual("partial", session.terminal[child_id]["outcome"])
        self.assertTrue(session.observed[child_id]["effect_refs"])
        self.assertFalse(any(event.get("event_id") == f"selected-replacement:{child_id}" for event in self._events(self.root)))
        pending = list((self.root / ".caprmedio_runtime/state/work_journal/pending").glob("*.json"))
        self.assertTrue(pending, "exact canonical replacement event must remain recoverable")


if __name__ == "__main__":
    unittest.main()
