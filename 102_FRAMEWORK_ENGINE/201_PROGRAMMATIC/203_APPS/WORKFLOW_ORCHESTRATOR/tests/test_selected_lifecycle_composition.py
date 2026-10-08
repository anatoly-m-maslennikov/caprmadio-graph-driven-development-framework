"""Focused W02/W04 current-state composition through selected execution."""
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
TEST_TEMP_ROOT = REPOSITORY / ".caprmedio_tmp" / "test_selected_lifecycle_composition"
for location in (APP, APP / "tests", TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from authoritative_status_models import resolve_status_model  # noqa: E402
from lifecycle_intents import carrier_descriptor  # noqa: E402
from selected_execution import SelectedExecution, build_requested_runs  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402
from test_selected_creation_execution import _Session  # noqa: E402


class _ActualRunSession(_Session):
    """Make the observed Run identity distinct from its requested identity."""

    def start_run(self, requested_run_id: str) -> dict[str, object]:
        existing = self.actual.get(requested_run_id)
        if existing is not None:
            return dict(existing)
        row = self.requested[requested_run_id]
        record: dict[str, object] = {
            "run_id": f"actual::{requested_run_id}",
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


class SelectedLifecycleCompositionTests(unittest.TestCase):
    def setUp(self) -> None:
        TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()

    def _prepare(self, case_id: str, route: str) -> tuple[GoldenProject, dict[str, object], SelectedExecution]:
        fixture = GoldenProject(REPOSITORY, self.root, GoldenCase(case_id, route))
        manifest = fixture.prepare()
        return fixture, manifest, SelectedExecution(self.root)

    @staticmethod
    def _events(root: Path) -> list[dict[str, object]]:
        events: list[dict[str, object]] = []
        for path in sorted((root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")):
            events.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line)
        return events

    @staticmethod
    def _child_result(root: Path, run_id: str, requested_child_id: str) -> dict[str, object]:
        path = root / ".caprmedio_install/workflow_orchestrator/runs" / run_id / f"{requested_child_id}.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def _frozen(
        self,
        selected: SelectedExecution,
        manifest: dict[str, object],
        route: str,
        parameters: dict[str, object],
        run_id: str,
    ) -> tuple[dict[str, object], list[dict[str, object]]]:
        graph = selected._validate_graph({
            "mode": "execute",
            "operation_route": route,
            "source_freshness": manifest["source_freshness"],
            "definition_manifest": {
                "manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
                "manifest_digest": manifest["canonical_manifest_sha256"],
            },
        })
        requested = build_requested_runs(graph, run_id)
        return {
            "graph": graph,
            "request": {
                "run_id": run_id,
                "execution": {
                    "request_id": f"{run_id}-request",
                    "parameters": parameters,
                    "requested_runs": requested,
                },
            },
        }, requested

    def _execute(
        self,
        selected: SelectedExecution,
        manifest: dict[str, object],
        route: str,
        parameters: dict[str, object],
        run_id: str,
        *,
        session_type: type[_Session] = _Session,
    ) -> tuple[dict[str, object], _Session, list[dict[str, object]], dict[str, object]]:
        frozen, requested = self._frozen(selected, manifest, route, parameters, run_id)
        session = session_type(requested)
        return selected._execute_graph(frozen, session), session, requested, frozen

    @staticmethod
    def _requested_action(requested: list[dict[str, object]], action_id: str) -> str:
        return next(
            str(row["requested_run_id"])
            for row in requested
            if row["kind"] == "action" and row["definition"]["atom_id"] == action_id
        )

    def test_create_update_replace_uses_the_actual_current_state_chain(self) -> None:
        fixture, manifest, selected = self._prepare("W01", "create_atom")
        create, _session, requested, _frozen = self._execute(
            selected, manifest, "create_atom", fixture.native_parameters(), "lifecycle-create",
        )
        self.assertEqual("completed", create["outcome"])
        create_child = self._requested_action(requested, "CA-O-032")
        created = self._child_result(self.root, "lifecycle-create", create_child)["native_result"]["observed"]

        update_fixture = GoldenProject(REPOSITORY, self.root, GoldenCase("W02", "update_atom"))
        current = self.root / created["path"]
        frontmatter, content = current.read_text(encoding="utf-8")[4:].split("\n---\n", 1)
        proposed = {"frontmatter": frontmatter, "content": content + "\nClarified composition detail.\n"}
        update_parameters = {
            "target": created,
            "proposed": proposed,
            "change_class": "semantic_revision",
            "semantic_assessment_report": update_fixture._semantic_assessment_report(created, proposed),
        }
        update, update_session, requested, _frozen = self._execute(
            selected, manifest, "update_atom", update_parameters, "lifecycle-update",
        )
        self.assertEqual("completed", update["outcome"])
        update_child = self._requested_action(requested, "CA-O-030")
        update_packet = self._child_result(self.root, "lifecycle-update", update_child)["native_result"]
        updated = update_packet["observed"]
        prior_revision_path = update_packet["history"]["prior_revision"]["path"]
        self.assertIn(prior_revision_path, update_session.terminal[update_child]["effect_refs"])
        self.assertIn(prior_revision_path, update["effect_refs"])

        replacement_parameters = {
            "predecessor": updated,
            "successors": [fixture._carrier("CA-R-103", "replacement", "Replacement summary")],
            "status_model": resolve_status_model(self.root, updated, "Archived"),
        }
        replace, _session, _requested, _frozen = self._execute(
            selected, manifest, "replace_atom", replacement_parameters, "lifecycle-replace",
        )
        self.assertEqual("completed", replace["outcome"])

        events = self._events(self.root)
        creation = next(event for event in events if event["action_id"] == "CA-O-032")
        update_event = next(event for event in events if event["action_id"] == "CA-O-030")
        replacement = next(event for event in events if event["action_id"] == "CA-O-051")
        self.assertEqual(creation["event_id"], update_event["previous_result_event"])
        self.assertEqual(update_event["event_id"], replacement["previous_result_event"])

    def test_plan_backlog_to_active_then_replace_has_move_update_current_state(self) -> None:
        fixture, manifest, selected = self._prepare("W04", "change_atom_status")
        plan = fixture.status_atom("Plan", "Backlog", number=8011)
        status_parameters = {
            "target": fixture._descriptor(plan.relative_to(self.root).as_posix()),
            "status": "Active",
        }
        status, _session, requested, _frozen = self._execute(
            selected, manifest, "change_atom_status", status_parameters, "plan-active",
        )
        self.assertEqual("completed", status["outcome"])
        action = self._requested_action(requested, "CA-O-128")
        active = self._child_result(self.root, "plan-active", action)["native_result"]["observed"]
        active_path = self.root / active["path"]
        frontmatter, content = active_path.read_text(encoding="utf-8")[4:].split("\n---\n", 1)
        successor = {
            "path": ".caprmedio_caprmedio/PARENT/03_plan/CA-P-8012--replacement.md",
            "frontmatter": frontmatter.replace("CA-P-8011", "CA-P-8012"),
            "content": content.replace("Docker status proof carrier", "Replacement plan summary"),
        }
        replacement_parameters = {
            "predecessor": active,
            "successors": [successor],
            "status_model": resolve_status_model(self.root, active, "Archived"),
        }
        replacement, _session, _requested, _frozen = self._execute(
            selected, manifest, "replace_atom", replacement_parameters, "plan-replace",
        )
        self.assertEqual("completed", replacement["outcome"])

        events = self._events(self.root)
        status_event = next(
            event for event in events
            if event["action_id"] == "CA-O-128" and event["event"] == "completed"
        )
        replacement_event = next(event for event in events if event["action_id"] == "CA-O-051")
        self.assertEqual("MOVE+UPDATE", status_event["action_type"])
        self.assertEqual(status_event["event_id"], replacement_event["previous_result_event"])

    def test_unrecorded_existing_carrier_gets_baseline_from_outer_actual_run(self) -> None:
        fixture, manifest, selected = self._prepare("W02", "update_atom")
        result, session, requested, _frozen = self._execute(
            selected, manifest, "update_atom", fixture.native_parameters(), "legacy-current", session_type=_ActualRunSession,
        )
        self.assertEqual("completed", result["outcome"])
        nested = self._requested_action(requested, "CA-O-030")
        parent = nested.rsplit(":nested:", 1)[0]
        events = self._events(self.root)
        baseline = next(event for event in events if event["event"] == "recovered")
        change = next(event for event in events if event["action_id"] == "CA-O-030")
        self.assertEqual("CA-O-128", baseline["action_id"])
        self.assertEqual(session.actual[parent]["run_id"], baseline["recovery_evidence"]["carrier"]["observer_run_id"])
        self.assertEqual(baseline["event_id"], change["previous_result_event"])

    def test_idless_draft_history_and_noop_retains_only_verified_effects(self) -> None:
        fixture, manifest, selected = self._prepare("W04", "change_atom_status")
        active = fixture.status_atom("Requirement", "Active", number=8015)
        result, session, requested, _frozen = self._execute(
            selected,
            manifest,
            "change_atom_status",
            {"target": fixture._descriptor(active.relative_to(self.root).as_posix()), "status": "Draft"},
            "idless-draft-history",
        )
        self.assertEqual("completed", result["outcome"])
        action = self._requested_action(requested, "CA-O-128")
        packet = self._child_result(self.root, "idless-draft-history", action)["native_result"]
        history_path = packet["history"]["prior_revision"]["path"]
        self.assertIn(history_path, session.terminal[action]["effect_refs"])
        self.assertIn(history_path, result["effect_refs"])
        before_noop = self._events(self.root)
        no_op, _session, no_op_requested, _frozen = self._execute(
            selected,
            manifest,
            "change_atom_status",
            {"target": packet["observed"], "status": "Draft"},
            "idless-draft-noop",
        )
        self.assertEqual("no_op", no_op["outcome"])
        self.assertEqual(before_noop, self._events(self.root))
        self.assertFalse(any(":nested:" in str(row["requested_run_id"]) for row in no_op_requested))

    def test_pending_change_retains_observed_effect_and_refuses_native_replay(self) -> None:
        fixture, manifest, selected = self._prepare("W04", "change_atom_status")
        plan = fixture.status_atom("Plan", "Backlog", number=8013)
        parameters = {"target": fixture._descriptor(plan.relative_to(self.root).as_posix()), "status": "Active"}
        frozen, requested = self._frozen(selected, manifest, "change_atom_status", parameters, "pending-status")
        session = _Session(requested)
        child = self._requested_action(requested, "CA-O-128")

        import lifecycle_intents
        import selected_lifecycle_journal

        native = lifecycle_intents.change_status_atom_action
        append = selected_lifecycle_journal.append_sealed_events
        execute_calls: list[bool] = []
        append_calls = 0

        def track_native(*args: object, **kwargs: object) -> dict[str, object]:
            execute_calls.append(bool(kwargs.get("execute")))
            return native(*args, **kwargs)

        def pending_change(*args: object, **kwargs: object) -> object:
            nonlocal append_calls
            append_calls += 1
            if append_calls == 2:
                raise OSError("recording unavailable")
            return append(*args, **kwargs)

        # Recreate handlers inside the patches so the native closure observes
        # the tracked adapter while the first append admits the baseline and
        # only the observed post-effect change becomes pending.
        with patch("lifecycle_intents.change_status_atom_action", side_effect=track_native), patch(
            "selected_lifecycle_journal.append_sealed_events", side_effect=pending_change,
        ):
            selected = SelectedExecution(self.root)
            result = selected._execute_graph(frozen, session)

        self.assertEqual("partial", result["outcome"])
        self.assertEqual([False, True], execute_calls)
        self.assertEqual("partial", session.terminal[child]["outcome"])
        self.assertTrue(session.terminal[child]["effect_refs"])
        self.assertEqual(["recovered"], [event["event"] for event in self._events(self.root)])
        saved = self._child_result(self.root, "pending-status", child)
        self.assertEqual("recording_pending", saved["lifecycle_recording"]["state"])

        recovery = selected.handlers["CA-O-128"]({
            "route": "change_atom_status",
            "session": session,
            "lifecycle_current_state": True,
            "restored_action": True,
        })
        self.assertEqual("lifecycle-recovery-required", recovery["result"])
        self.assertEqual([False, True], execute_calls)

    def test_pending_prior_blocks_status_effect_before_the_outer_action_can_mutate(self) -> None:
        fixture, manifest, selected = self._prepare("W04", "change_atom_status")
        plan = fixture.status_atom("Plan", "Backlog", number=8014)
        parameters = {"target": fixture._descriptor(plan.relative_to(self.root).as_posix()), "status": "Active"}
        frozen, requested = self._frozen(selected, manifest, "change_atom_status", parameters, "pending-prior")
        session = _Session(requested)

        import lifecycle_intents

        native = lifecycle_intents.change_status_atom_action
        execute_calls: list[bool] = []

        def track_native(*args: object, **kwargs: object) -> dict[str, object]:
            execute_calls.append(bool(kwargs.get("execute")))
            return native(*args, **kwargs)

        with patch("lifecycle_intents.change_status_atom_action", side_effect=track_native), patch(
            "selected_lifecycle_journal.append_sealed_events", side_effect=OSError("recording unavailable"),
        ):
            selected = SelectedExecution(self.root)
            result = selected._execute_graph(frozen, session)

        outer = self._requested_action(requested, "CA-O-128")
        self.assertEqual("interrupted_pending", result["outcome"])
        self.assertEqual([False], execute_calls)
        self.assertEqual("interrupted_pending", session.terminal[outer]["outcome"])
        self.assertEqual("Backlog", carrier_descriptor(self.root, plan.relative_to(self.root).as_posix())["status"])
        self.assertEqual([], self._events(self.root))


if __name__ == "__main__":
    unittest.main()
