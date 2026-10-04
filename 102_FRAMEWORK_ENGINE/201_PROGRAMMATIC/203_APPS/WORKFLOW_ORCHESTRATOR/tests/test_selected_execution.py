"""Golden contracts for source-bound selected Workflow queue execution."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
REPOSITORY = APP.parents[3]
sys.path.insert(0, str(APP))

from selected_execution import (  # noqa: E402
    SelectedExecution,
    SelectedExecutionError,
    canonical_json,
    manifest_relative_path,
    make_revert_action_handler,
)


def digest(value: object) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


class SelectedExecutionTests(unittest.TestCase):
    """The queue interprets frozen source graphs; it does not author policies."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (self.root / ".git").mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\njournal_root = ".caprmedio_caprmedio/_journal"\n', encoding="utf-8"
        )
        self.manifest_path = control / "_projection/selected_workflow_bindings.json"
        self._write_definitions()
        self._write_manifest()

    def _write_definitions(self) -> None:
        for name, atom_id in (("workflow.md", "CA-O-127"), ("step-one.md", "CA-O-129"),
                              ("step-two.md", "CA-O-130"), ("action-one.md", "CA-O-128"),
                              ("action-two.md", "CA-O-131")):
            path = self.root / "definitions" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                f"---\natom_id: {atom_id}\nversion: 1\nstatus: Active\n---\n# Summary\nFixture\n",
                encoding="utf-8",
            )

    def _binding(self, name: str, atom_id: str, kind: str) -> dict[str, object]:
        path = self.root / "definitions" / name
        return {
            "atom_id": atom_id,
            "kind": kind,
            "version": 1,
            "path": path.relative_to(self.root).as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }

    def _write_manifest(self) -> None:
        first = self._binding("action-one.md", "CA-O-128", "action")
        second = self._binding("action-two.md", "CA-O-131", "action")
        value = {
            "routes": [
                {
                    "route": "create_atom",
                    "workflow": self._binding("workflow.md", "CA-O-127", "workflow"),
                    "steps": [
                        {
                            **self._binding("step-one.md", "CA-O-129", "step"),
                            "actions": [first],
                            "on_result": [{"result": "prepared", "next": "CA-O-130"}],
                        },
                        {
                            **self._binding("step-two.md", "CA-O-130", "step"),
                            "actions": [second],
                            "on_result": [{"result": "completed", "terminal": "completed"}],
                        },
                    ],
                }
            ]
        }
        value["canonical_manifest_sha256"] = digest(value)
        self.manifest_path.parent.mkdir(parents=True, exist_ok=True)
        self.manifest_path.write_text(json.dumps(value), encoding="utf-8")

    def request(self, run_id: str = "selected-run") -> dict[str, object]:
        manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        manifest_ref = self.manifest_path.relative_to(self.root).as_posix()
        definition_manifest = {
            "manifest_ref": manifest_ref,
            "manifest_digest": manifest["canonical_manifest_sha256"],
        }
        source_freshness = {
            "selected_source_registry_ref": "selected/registry.json",
            "selected_source_registry_version": 1,
            "selected_source_registry_digest": "a" * 64,
            "selected_binding_ref": "selected/create-atom.json",
            "selected_binding_digest": "b" * 64,
        }
        requested_runs = [
            {
                "requested_run_id": run_id,
                "kind": "workflow",
                "definition": {**{key: manifest["routes"][0]["workflow"][key] for key in ("atom_id", "version", "path")},
                               "digest": manifest["routes"][0]["workflow"]["sha256"]},
            }
        ]
        for ordinal, step in enumerate(manifest["routes"][0]["steps"], start=1):
            step_run_id = f"{run_id}:step:{ordinal}"
            requested_runs.append({
                "requested_run_id": step_run_id,
                "kind": "step",
                "definition": {**{key: step[key] for key in ("atom_id", "version", "path")}, "digest": step["sha256"]},
                "parent_requested_run_id": run_id,
            })
            for action_ordinal, action in enumerate(step["actions"], start=1):
                requested_runs.append({
                    "requested_run_id": f"{step_run_id}:action:{action_ordinal}",
                    "kind": "action",
                    "definition": {**{key: action[key] for key in ("atom_id", "version", "path")}, "digest": action["sha256"]},
                    "parent_requested_run_id": step_run_id,
                })
        parameters = {"fixture": True}
        target_frontier = ["definitions/workflow.md"]
        effects = [{"type": "create", "target": "results/fixture.md"}]
        execution = {
            "mode": "execute",
            "request_id": "request-1",
            "operation_route": "create_atom",
            "parameters": parameters,
            "parameters_digest": digest(parameters),
            "target_frontier": target_frontier,
            "target_frontier_digest": digest(target_frontier),
            "effects": effects,
            "effects_digest": digest(effects),
            "definition_manifest": definition_manifest,
            "source_freshness": source_freshness,
            "initiative": {"initiative_id": "initiative-1", "instruction_summary": "fixture",
                           "initiative_ref": "definitions/workflow.md"},
            "requested_runs": requested_runs,
        }
        observed = {"definition_manifest": definition_manifest, "manifest_ref": manifest_ref,
                    "manifest_digest": manifest["canonical_manifest_sha256"]}
        proposal = {
            "request_id": execution["request_id"],
            "operation_route": execution["operation_route"],
            "initiative_ref": execution["initiative"]["initiative_ref"],
            "source_freshness": {"declared": source_freshness, "observed": observed,
                                  "selected": True, "current": True},
            "parameters_digest": execution["parameters_digest"],
            "target_frontier_digest": execution["target_frontier_digest"],
            "effects_digest": execution["effects_digest"],
            "definition_manifest": definition_manifest,
        }
        proposal_digest = digest(proposal)
        execution.update({
            "proposal_receipt": proposal,
            "proposal_receipt_digest": proposal_digest,
            "assigned_action_id": "fixture-assignment",
            "operator_authorization": {
                "authorization_ref": "authorizations/fixture.json",
                "authorization_freshness": {"state": "current", "digest": "d" * 64},
                "request_id": execution["request_id"],
                "operation_route": execution["operation_route"],
                "proposal_receipt_digest": proposal_digest,
                "parameters_digest": execution["parameters_digest"],
                "target_frontier_digest": execution["target_frontier_digest"],
                "effects_digest": execution["effects_digest"],
                "definition_manifest": definition_manifest,
                "source_freshness": source_freshness,
            },
        })
        return {
            "operation": "enqueue_selected",
            "run_id": run_id,
            "execution": execution,
        }

    def executor(self, handlers: dict[str, object]) -> SelectedExecution:
        return SelectedExecution(self.root, handlers=handlers)

    @staticmethod
    def current_manifest_request(route_name: str, run_id: str) -> tuple[SelectedExecution, dict[str, object]]:
        """Build a frozen mock request from the physical D547 binding carrier."""
        manifest_path = REPOSITORY / ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        execution: dict[str, object] = {
            "mode": "execute", "operation_route": route_name, "workflow_run_id": run_id,
            "source_freshness": manifest["source_freshness"],
            "definition_manifest": {
                "manifest_ref": manifest_path.relative_to(REPOSITORY).as_posix(),
                "manifest_digest": manifest["canonical_manifest_sha256"],
            },
        }
        selected = SelectedExecution(REPOSITORY)
        graph = selected._validate_graph(execution)
        requested_runs = [{
            "requested_run_id": run_id, "kind": "workflow",
            "definition": selected._support_definition(graph["workflow"]),
        }]
        for ordinal, step in enumerate(graph["steps"], start=1):
            step_run_id = f"{run_id}:step:{ordinal}"
            requested_runs.append({
                "requested_run_id": step_run_id, "kind": "step",
                "definition": selected._support_definition(step), "parent_requested_run_id": run_id,
            })
            for action_ordinal, action in enumerate(step["actions"], start=1):
                requested_runs.append({
                    "requested_run_id": f"{step_run_id}:action:{action_ordinal}", "kind": "action",
                    "definition": selected._support_definition(action),
                    "parent_requested_run_id": step_run_id,
                })
        execution["requested_runs"] = requested_runs
        return selected, {"operation": "enqueue_selected", "run_id": run_id, "execution": execution}

    @staticmethod
    def session(frozen: dict[str, object]) -> object:
        """A lazy tracker mock: graph nodes create actual Run IDs only on entry."""
        requested = {row["requested_run_id"]: row for row in frozen["request"]["execution"]["requested_runs"]}

        class Session:
            def __init__(self) -> None:
                self.actual: dict[str, dict[str, object]] = {}
                self.finished: list[dict[str, object]] = []

            def start_run(self, requested_run_id: str) -> dict[str, object]:
                if requested_run_id not in self.actual:
                    row = requested[requested_run_id]
                    self.actual[requested_run_id] = {
                        "run_id": f"actual-{len(self.actual) + 1}", "kind": row["kind"],
                        "definition": row["definition"],
                    }
                return dict(self.actual[requested_run_id])

            def finish_run(self, run_id: str, **result: object) -> dict[str, object]:
                value = {"run_id": run_id, **result}
                self.finished.append(value)
                return value

        return Session()

    def test_freeze_rejects_a_stale_manifest_before_any_dispatch(self) -> None:
        request = self.request()
        request["execution"]["definition_manifest"]["manifest_digest"] = "0" * 64

        with self.assertRaisesRegex(SelectedExecutionError, "manifest"):
            self.executor({}).freeze(request)
        self.assertFalse((self.root / ".caprmedio_install/workflow_orchestrator/runs/selected-run").exists())

    def test_manifest_path_resolves_configured_control_root(self) -> None:
        configured = self.root / ".caprmedio_selected"
        configured.mkdir()
        (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_selected"\n', encoding="utf-8"
        )

        self.assertEqual(
            ".caprmedio_selected/_projection/selected_workflow_bindings.json",
            manifest_relative_path(self.root),
        )

    def test_interprets_source_graph_with_distinct_workflow_step_and_action_runs(self) -> None:
        calls: list[dict[str, object]] = []

        def first(context: dict[str, object]) -> dict[str, object]:
            calls.append(context)
            return {"result": "prepared", "effects": []}

        def second(context: dict[str, object]) -> dict[str, object]:
            calls.append(context)
            return {"result": "completed", "effects": []}

        execution = self.executor({"CA-O-128": first, "CA-O-131": second})
        frozen = execution.freeze(self.request())
        result = execution.dispatch(
            frozen, run_support=lambda _root, _request, graph: graph(self.session(frozen))
        )

        self.assertEqual(result["outcome"], "completed")
        self.assertEqual([row["action_definition_id"] for row in calls], ["CA-O-128", "CA-O-131"])
        for row in calls:
            self.assertNotEqual(row["workflow_run_id"], row["step_run_id"])
            self.assertNotEqual(row["step_run_id"], row["action_run_id"])
        saved = json.loads((execution.run_directory("selected-run") / "accepted.json").read_text())
        self.assertEqual(saved["result"]["workflow_run_id"], "actual-1")

    def test_shared_run_support_records_actual_workflow_step_and_action_runs(self) -> None:
        execution = self.executor({
            "CA-O-128": lambda _context: {"result": "prepared", "effect_refs": []},
            "CA-O-131": lambda _context: {"result": "completed", "effect_refs": []},
        })
        frozen = execution.freeze(self.request())
        result = execution.dispatch(frozen)

        self.assertEqual(result["disposition"], "terminal")
        self.assertEqual({row["outcome"] for row in result["terminal_runs"]}, {"completed"})
        self.assertEqual(len(result["run_ids"]), 5)
        self.assertEqual(len(set(result["run_ids"])), 5)
        journal = next((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))
        events = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(events), 10)
        self.assertEqual({event["run"]["kind"] for event in events}, {"workflow", "step", "action"})

    def test_dispatch_rechecks_definition_bindings_after_queue_admission(self) -> None:
        execution = self.executor({"CA-O-128": lambda _context: {"result": "prepared"}})
        frozen = execution.freeze(self.request())
        (self.root / "definitions/action-one.md").write_text("changed", encoding="utf-8")

        with self.assertRaisesRegex(SelectedExecutionError, "definition"):
            execution.dispatch(frozen, run_support=lambda _root, _request, graph: graph(self.session(frozen)))
        self.assertFalse((execution.run_directory("selected-run") / "dispatch-intent.json").exists())

    def test_uncertain_dispatch_intent_never_replays_an_action(self) -> None:
        calls: list[dict[str, object]] = []
        execution = self.executor({"CA-O-128": lambda context: calls.append(context) or {"result": "prepared"}})
        frozen = execution.freeze(self.request())
        intent = execution.run_directory("selected-run") / "dispatch-intent.json"
        intent.write_text(json.dumps({"state": "started"}), encoding="utf-8")

        result = execution.dispatch(
            frozen, run_support=lambda _root, _request, graph: graph(self.session(frozen))
        )
        self.assertEqual(result["disposition"], "recording_pending")
        self.assertEqual(result["outcome"], "interrupted_pending")
        self.assertEqual(calls, [])

    def test_undeclared_action_never_becomes_a_transition(self) -> None:
        execution = self.executor({"CA-O-128": lambda _context: {"result": "invented"}})
        frozen = execution.freeze(self.request())

        result = execution.dispatch(
            frozen, run_support=lambda _root, _request, graph: graph(self.session(frozen))
        )
        self.assertEqual(result["disposition"], "recording_pending")
        self.assertEqual(result["outcome"], "interrupted_pending")

    def test_current_d547_manifest_verifies_all_thirteen_routes(self) -> None:
        """Exercise the physical producer schema, not the legacy mock shape."""
        manifest_path = REPOSITORY / ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        executor = SelectedExecution(REPOSITORY)
        accepted: set[str] = set()
        for route in manifest["routes"]:
            execution = {
                "mode": "execute", "operation_route": route["route"],
                "source_freshness": manifest["source_freshness"],
                "definition_manifest": {
                    "manifest_ref": manifest_path.relative_to(REPOSITORY).as_posix(),
                    "manifest_digest": manifest["canonical_manifest_sha256"],
                },
            }
            try:
                graph = executor._validate_graph(execution)
            except SelectedExecutionError as error:
                self.fail(f"{route['route']} D547 binding was refused: {error}")
            else:
                accepted.add(graph["route"])
        self.assertEqual(len(accepted), 13)
        self.assertEqual(accepted, {route["route"] for route in manifest["routes"]})
        self.assertIn("run_implementation_workflow", accepted)
        self.assertIn("build_applicable_methodology", accepted)

    def test_current_d547_all_thirteen_routes_pass_prequeue_freeze_validation(self) -> None:
        manifest_path = REPOSITORY / ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        frozen_routes: set[str] = set()
        for ordinal, route in enumerate(manifest["routes"], start=1):
            selected, request = self.current_manifest_request(route["route"], f"current-freeze-{ordinal}")
            frozen = selected._validated_freeze(request)
            frozen_routes.add(frozen["graph"]["route"])
        self.assertEqual(frozen_routes, {route["route"] for route in manifest["routes"]})

    def test_current_d547_actions_have_builtin_context_scoped_handlers(self) -> None:
        manifest_path = REPOSITORY / ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        bound_actions = {
            entry["action"]["atom_id"]
            for route in manifest["routes"]
            for entry in route["ordered_steps"]
        }
        builtin = SelectedExecution(REPOSITORY).handlers
        self.assertFalse(bound_actions - set(builtin))
        self.assertIn("CA-O-131", builtin)

    def test_current_d547_update_graph_uses_only_actual_bound_nodes(self) -> None:
        selected, request = self.current_manifest_request("update_atom", "current-update")
        calls: list[str] = []
        runner = self.executor({
            "CA-O-067": lambda context: calls.append(context["action_definition_id"]) or {
                "result": "identity-preserving", "effect_refs": [],
            },
            "CA-O-128": lambda context: calls.append(context["action_definition_id"]) or {
                "result": "applied", "terminal_outcome": "completed", "effect_refs": [],
            },
        })
        frozen = {"request": request, "graph": selected._validate_graph(request["execution"])}
        result = runner._execute_graph(frozen, self.session(frozen))

        self.assertEqual(calls, ["CA-O-067", "CA-O-128"])
        self.assertEqual(result["outcome"], "completed")
        self.assertEqual(len(result["step_results"]), 2)

    def test_revert_adapter_uses_the_existing_lazy_action_run(self) -> None:
        frozen = self.executor({}).freeze(self.request())
        session = self.session(frozen)

        class RevertService:
            def execute_with_session(self, manifest: dict[str, object], supplied_session: object,
                                     requested_action_run_id: str, _cancel: object) -> dict[str, object]:
                self.assertEqual(manifest, {"manifest_id": "reversal-1"})
                actual = supplied_session.start_run(requested_action_run_id)
                supplied_session.finish_run(actual["run_id"], outcome="completed",
                                            result_ref="results/revert.json", effect_refs=[])
                return {
                    "outcome": "reverted", "manifest_id": "reversal-1",
                    "effect_account": {"effects": [], "applied_effect_count": 0},
                    "run_receipt_refs": [{"run_id": actual["run_id"]}],
                }

            def assertEqual(self, left: object, right: object) -> None:
                if left != right:
                    raise AssertionError((left, right))

        output = make_revert_action_handler(RevertService())({
            "parameters": {"approved_reversal_manifest": {"manifest_id": "reversal-1"}},
            "session": session, "requested_action_run_id": "selected-run:step:2:action:1",
        })

        self.assertTrue(output["action_terminal_recorded"])
        self.assertEqual(output["terminal_outcome"], "completed")
        self.assertEqual(len(session.finished), 1)


if __name__ == "__main__":
    unittest.main()
