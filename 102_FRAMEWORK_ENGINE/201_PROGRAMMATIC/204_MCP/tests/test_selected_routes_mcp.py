"""Golden contracts for the selected, source-bound MCP route adapter."""
from __future__ import annotations

import copy
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
ROOT = MCP.parents[2]
ORCHESTRATOR = MCP.parent / "203_APPS" / "WORKFLOW_ORCHESTRATOR"
TEST_TEMP_ROOT = ROOT / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(MCP))

from selected_routes import (  # noqa: E402
    ORIGINAL_SELECTED_ROUTE_NAMES,
    QUERY_ROUTE_NAMES,
    SELECTED_ROUTE_NAMES,
    SelectedRouteError,
    SelectedRouteAdapter,
    canonical_digest,
    load_selected_manifest,
    selected_manifest_contract,
    selected_manifest_ref,
)


class FakeRunSupport:
    """Records adapter calls without executing a Workflow, Action, or effect."""

    def __init__(self) -> None:
        self.calls: list[dict] = []
        self.recovery_calls: list[dict] = []

    def run_selected_operation(self, request: dict) -> dict:
        self.calls.append(copy.deepcopy(request))
        if request["mode"] == "preview":
            receipt = {"request_id": request["request_id"], "definition_manifest": request["definition_manifest"]}
            return {
                "request_id": request["request_id"],
                "disposition": "preview",
                "outcome": "prepared",
                "proposal_receipt": receipt,
                "proposal_receipt_digest": canonical_digest(receipt),
                "source_freshness": copy.deepcopy(request["source_freshness"]),
            }
        return {
            "request_id": request["request_id"],
            "disposition": "started",
            "outcome": "started",
            "workflow_run_id": "run:fixture",
            "action_run_ids": ["action:fixture"],
            "event_refs": ["event:fixture"],
            "report_ref": "report:fixture",
            "source_freshness": copy.deepcopy(request["source_freshness"]),
        }

    def get_selected_workflow_run(self, request: dict) -> dict:
        return {"run_id": request["run_id"], "status": "recording_pending", "event_refs": ["event:pending"]}

    def get_selected_action_run(self, request: dict) -> dict:
        return {"action_run_id": request["action_run_id"], "status": "completed", "lineage": {"workflow_run_id": "run:fixture"}}

    def recover_selected_run_recording(self, request: dict) -> dict:
        self.recovery_calls.append(copy.deepcopy(request))
        return {"event_ref": request["pending_event_ref"], "receipt_ref": "receipt:fixture"}


class SelectedManifestRefResolverTest(unittest.TestCase):
    def test_manifest_ref_uses_the_configured_control_root_projection(self) -> None:
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True) as temporary:
            project = Path(temporary)
            self.assertEqual(
                ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
                selected_manifest_ref(project),
            )

            settings = project / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
            settings.parent.mkdir()
            settings.write_text(
                '[paths]\ncontrol_root = ".caprmedio_fixture"\njournal_root = ".caprmedio_fixture/_journal"\n',
                encoding="utf-8",
            )
            self.assertEqual(
                ".caprmedio_fixture/_projection/selected_workflow_bindings.json",
                selected_manifest_ref(project),
            )


class SelectedRoutesMCPTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # One real load proves the live source pins.  The route-contract tests
        # below deliberately exercise the same immutable snapshot instead of
        # re-reading every source graph once per route.
        cls._verified_manifest = load_selected_manifest(ROOT)

    def setUp(self) -> None:
        self.manifest = copy.deepcopy(self._verified_manifest)
        self.support = FakeRunSupport()
        self.loader = patch("selected_routes.load_selected_manifest", return_value=self.manifest)
        self.loader.start()
        self.addCleanup(self.loader.stop)
        self.adapter = SelectedRouteAdapter(ROOT, service=self.support)

    def request(self, route: str, *, mode: str = "preview") -> dict:
        parameters = {"route_input": route}
        refs = ["target:fixture"]
        effects = []
        request = {
            "operation_route": route,
            "mode": mode,
            "request_id": f"request-{route}",
            "parameters": parameters,
            "parameters_digest": canonical_digest(parameters),
            "target_frontier": refs,
            "target_frontier_digest": canonical_digest(refs),
            "effects": effects,
            "effects_digest": canonical_digest(effects),
            "definition_manifest": {
                "manifest_ref": self.manifest["manifest_ref"],
                "manifest_digest": self.manifest["canonical_manifest_sha256"],
            },
            "source_freshness": copy.deepcopy(self.manifest["source_freshness"]),
            "initiative": {"initiative_id": "initiative:fixture", "instruction_summary": "fixture",
                           "initiative_ref": "initiative:fixture"},
        }
        if mode == "execute":
            receipt = {"request_id": request["request_id"], "definition_manifest": request["definition_manifest"]}
            receipt_digest = canonical_digest(receipt)
            request.update({
                "proposal_receipt": receipt,
                "proposal_receipt_digest": receipt_digest,
                "assigned_action_id": "operator:fixture",
                "requested_runs": [{"requested_run_id": "requested:workflow", "kind": "workflow",
                                    "definition": self._definition(route, "workflow")},
                                   {"requested_run_id": "requested:action", "kind": "action",
                                    "definition": self._definition(route, "action"),
                                    "parent_requested_run_id": "requested:workflow"}],
                "operator_authorization": {"authorization_ref": "authorization:fixture",
                    "authorization_freshness": {"state": "current", "digest": "b" * 64},
                    "request_id": request["request_id"], "operation_route": route,
                    "proposal_receipt_digest": receipt_digest,
                    "parameters_digest": request["parameters_digest"],
                    "target_frontier_digest": request["target_frontier_digest"],
                    "effects_digest": request["effects_digest"],
                    "definition_manifest": copy.deepcopy(request["definition_manifest"]),
                    "source_freshness": copy.deepcopy(request["source_freshness"])},
            })
        return request

    def _definition(self, route: str, kind: str) -> dict:
        entry = next(item for item in self.manifest["routes"] if item["route"] == route)
        pin = entry["workflow"] if kind == "workflow" else entry["ordered_actions"][0]
        return {"atom_id": pin["atom_id"], "version": pin["version"],
                "path": pin["source_path"], "digest": pin["digest"]}

    @staticmethod
    def _queue_requested_runs(graph: dict, run_id: str) -> list[dict]:
        def definition(pin: dict) -> dict:
            return {"atom_id": pin["atom_id"], "version": pin["version"],
                    "path": pin["path"], "digest": pin["sha256"]}

        requested = [{"requested_run_id": run_id, "kind": "workflow",
                      "definition": definition(graph["workflow"])}]
        for ordinal, step in enumerate(graph["steps"], start=1):
            step_run_id = f"{run_id}:step:{ordinal}"
            requested.append({"requested_run_id": step_run_id, "kind": "step",
                              "definition": definition(step), "parent_requested_run_id": run_id})
            for action_ordinal, action in enumerate(step["actions"], start=1):
                requested.append({"requested_run_id": f"{step_run_id}:action:{action_ordinal}",
                                  "kind": "action", "definition": definition(action),
                                  "parent_requested_run_id": step_run_id})
        return requested

    def test_current_physical_manifest_freezes_the_original_thirteen_routes_through_queue_consumer(self) -> None:
        """The MCP source fixture must be sufficient for the independent queue.

        This copies only the immutable manifest and its pinned sources into a
        disposable Project, then uses the queue consumer's real ``freeze``
        boundary. No Action handler or DBOS worker is invoked.
        """
        sys.path.insert(0, str(ORCHESTRATOR))
        from selected_execution import SelectedExecution  # noqa: PLC0415

        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True) as temporary:
            project = Path(temporary)
            (project / ".git").mkdir()
            control = project / ".caprmedio_caprmedio"
            control.mkdir()
            (control / "caprmedio_project_settings.toml").write_text(
                '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
                'journal_root = ".caprmedio_caprmedio/_journal"\n',
                encoding="utf-8",
            )
            pins = {self.manifest["manifest_ref"], self.manifest["source_freshness"]["selected_source_registry_ref"]}
            for route in self.manifest["routes"]:
                pins.add(route["workflow"]["source_path"])
                pins.update(item["step"]["source_path"] for item in route["ordered_steps"])
                pins.update(item["action"]["source_path"] for item in route["ordered_steps"])
                pins.update(item["source_path"] for item in route["native_action_calls"])
            for relative in pins:
                source = ROOT / relative
                destination = project / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, destination)

            queue = SelectedExecution(project, handlers={})
            original_routes = [route for route in self.manifest["routes"]
                               if route["route"] in ORIGINAL_SELECTED_ROUTE_NAMES]
            self.assertEqual(13, len(original_routes))
            for ordinal, route in enumerate(original_routes, start=1):
                run_id = f"freeze{ordinal:02d}"
                execution = {
                    "mode": "execute", "request_id": f"request-{run_id}",
                    "operation_route": route["route"], "parameters": {},
                    "target_frontier": ["fixture/input"], "effects": [],
                    "definition_manifest": {"manifest_ref": self.manifest["manifest_ref"],
                                            "manifest_digest": self.manifest["canonical_manifest_sha256"]},
                    "source_freshness": copy.deepcopy(self.manifest["source_freshness"]),
                    "initiative": {"initiative_id": "fixture", "instruction_summary": "freeze"},
                }
                graph = queue._validate_graph(execution)
                execution["requested_runs"] = self._queue_requested_runs(graph, run_id)
                frozen = queue.freeze({"operation": "enqueue_selected", "run_id": run_id,
                                       "execution": execution})
                self.assertEqual(route["route"], frozen["graph"]["route"])
                self.assertEqual(graph["entry_step"], frozen["graph"]["entry_step"])

    def test_manifest_is_full_closed_fifteen_route_projection_with_fresh_pins(self) -> None:
        contract = selected_manifest_contract(ROOT)
        self.assertEqual(self.manifest["manifest_ref"], contract["manifest_ref"])
        self.assertEqual(list(SELECTED_ROUTE_NAMES), contract["route_names"])
        self.assertTrue(contract["canonical_digest"]["self_field_omitted_from_digest"])
        self.assertEqual(["route", "acceptance_frontier", "workflow", "ordered_steps", "ordered_actions"],
                         contract["query_source_admission_fields"])
        self.assertEqual(["from", "condition", "to"], contract["on_result_fields"])
        self.assertEqual("complete", contract["on_result_terminal_target"])
        self.assertEqual(list(SELECTED_ROUTE_NAMES), [entry["route"] for entry in self.manifest["routes"]])
        self.assertEqual(15, len(self.manifest["routes"]))
        self.assertEqual(self.manifest["canonical_manifest_sha256"], canonical_digest(
            {key: value for key, value in self.manifest.items()
             if key not in {"canonical_manifest_sha256", "manifest_ref"}}))
        for entry in self.manifest["routes"]:
            self.assertTrue(entry["entry_step"])
            self.assertTrue(entry["ordered_steps"])
            self.assertEqual([item["action"]["atom_id"] for item in entry["ordered_steps"]],
                             [item["atom_id"] for item in entry["ordered_actions"]])
            steps = {item["step"]["atom_id"] for item in entry["ordered_steps"]}
            self.assertIn(entry["entry_step"], steps)
            for edge in entry["on_result"]:
                self.assertIn(edge["from"], steps)
                self.assertTrue(edge["to"] == "complete" or edge["to"] in steps)
            for pin in [entry["workflow"], *[item["step"] for item in entry["ordered_steps"]],
                        *entry["ordered_actions"], *entry["native_action_calls"]]:
                self.assertEqual(64, len(pin["digest"]))
                self.assertTrue((ROOT / pin["source_path"]).is_file())

        routes = {entry["route"]: entry for entry in self.manifest["routes"]}
        admissions = self.manifest["query_source_admissions"]
        self.assertEqual(list(QUERY_ROUTE_NAMES), [entry["route"] for entry in admissions])
        self.assertEqual(["CA-P-1532", "CA-P-1535"], [entry["acceptance_frontier"]["atom_id"] for entry in admissions])
        self.assertNotIn("CA-P-1543", {pin["atom_id"] for entry in admissions
                                        for pin in [entry["acceptance_frontier"], entry["workflow"],
                                                    *[item["step"] for item in entry["ordered_steps"]],
                                                    *[item["action"] for item in entry["ordered_steps"]]]})
        for admission in admissions:
            route = routes[admission["route"]]
            self.assertFalse(route["mutation_capable"])
            for field in ("workflow", "ordered_steps", "ordered_actions"):
                self.assertEqual(admission[field], route[field])
        for route in ("create_atom", "replace_atom", "change_atom_status"):
            self.assertEqual([], routes[route]["on_result"])
        self.assertEqual(
            [
                ("CA-O-152", "complete exact selection", "CA-O-153"),
                ("CA-O-153", "required checks complete, no unresolved conflict, required approvals valid", "CA-O-157"),
                ("CA-O-153", "unresolved conflict with an authorized correction-proposal route", "CA-O-154"),
                ("CA-O-154", "exact supported proposal ready", "CA-O-155"),
                ("CA-O-155", "valid exact approval and upstream corrections required", "CA-O-156"),
                ("CA-O-155", "valid exact resolution decision without a needed source correction", "CA-O-152"),
                ("CA-O-155", "requested revision and applicable authority permits another bounded proposal attempt", "CA-O-154"),
                ("CA-O-156", "authorized correction completed", "CA-O-152"),
                ("CA-O-157", "completed publication from the still-valid final frontier", "complete"),
                ("CA-O-157", "changed frontier", "CA-O-152"),
            ],
            [(edge["from"], edge["condition"], edge["to"])
             for edge in routes["build_applicable_methodology"]["on_result"]],
        )

    def test_manifest_rejects_missing_or_third_query_source_admission(self) -> None:
        """The two accepted frontier records are closed manifest evidence."""
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True) as temporary:
            project = Path(temporary)
            (project / ".git").mkdir()
            control = project / ".caprmedio_caprmedio"
            control.mkdir()
            (control / "caprmedio_project_settings.toml").write_text(
                '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
                'journal_root = ".caprmedio_caprmedio/_journal"\n', encoding="utf-8",
            )
            pins = {self.manifest["manifest_ref"], self.manifest["source_freshness"]["selected_source_registry_ref"]}
            for route in self.manifest["routes"]:
                pins.add(route["workflow"]["source_path"])
                pins.update(item["step"]["source_path"] for item in route["ordered_steps"])
                pins.update(item["action"]["source_path"] for item in route["ordered_steps"])
                pins.update(item["source_path"] for item in route["native_action_calls"])
            for admission in self.manifest["query_source_admissions"]:
                pins.add(admission["acceptance_frontier"]["source_path"])
            for relative in pins:
                source = ROOT / relative
                destination = project / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, destination)

            for mutation in ("missing", "third"):
                with self.subTest(mutation=mutation):
                    candidate = {key: copy.deepcopy(value) for key, value in self.manifest.items()
                                 if key not in {"manifest_ref", "canonical_manifest_sha256"}}
                    if mutation == "missing":
                        candidate["query_source_admissions"] = candidate["query_source_admissions"][:1]
                    else:
                        candidate["query_source_admissions"].append(
                            copy.deepcopy(candidate["query_source_admissions"][0])
                        )
                    candidate["canonical_manifest_sha256"] = canonical_digest(candidate)
                    (project / self.manifest["manifest_ref"]).write_text(
                        __import__("json").dumps(candidate), encoding="utf-8",
                    )
                    with self.assertRaises(SelectedRouteError):
                        load_selected_manifest(project)

    def test_every_selected_route_forwards_one_mutation_free_preview(self) -> None:
        for route in SELECTED_ROUTE_NAMES:
            result = self.adapter.invoke(route, self.request(route))
            self.assertEqual("prepared", result["outcome"])
            self.assertEqual(route, self.support.calls[-1]["operation_route"])
            self.assertEqual("preview", self.support.calls[-1]["mode"])
        self.assertEqual(15, len(self.support.calls))

    def test_default_adapter_uses_shared_preview_support_without_an_executor(self) -> None:
        result = SelectedRouteAdapter(ROOT).invoke("create_atom", self.request("create_atom"))
        self.assertEqual("preview", result["disposition"])
        self.assertIn("proposal_receipt", result)
        self.assertNotIn("run_ids", result)

    def test_execute_forwards_exact_request_once_and_observations_do_not_dispatch(self) -> None:
        route = "create_atom"
        request = self.request(route, mode="execute")
        result = self.adapter.invoke(route, request)
        self.assertEqual("started", result["outcome"])
        self.assertEqual(request, self.support.calls[-1])
        before = len(self.support.calls)
        self.assertEqual("recording_pending", self.adapter.get_workflow_run({"run_id": "run:fixture"})["status"])
        self.assertEqual("completed", self.adapter.get_action_run({"action_run_id": "action:fixture"})["status"])
        self.assertEqual(before, len(self.support.calls))

    def test_execute_accepts_manifest_in_the_shared_supports_real_preview_receipt(self) -> None:
        route = "create_atom"
        preview = SelectedRouteAdapter(ROOT).invoke(route, self.request(route))
        self.assertEqual("preview", preview["disposition"])
        request = self.request(route, mode="execute")
        request["proposal_receipt"] = preview["proposal_receipt"]
        request["proposal_receipt_digest"] = preview["proposal_receipt_digest"]
        request["operator_authorization"]["proposal_receipt_digest"] = preview["proposal_receipt_digest"]

        result = self.adapter.invoke(route, request)

        self.assertEqual("started", result["outcome"], result)
        self.assertEqual([request], self.support.calls)

    def test_receipt_exception_does_not_allow_nested_shadow_manifest_wrappers(self) -> None:
        cases = []
        for wrapper in ("proposal_receipt", "operator_authorization"):
            request = self.request("create_atom", mode="execute")
            request["parameters"] = {wrapper: {"definition_manifest": request["definition_manifest"]}}
            request["parameters_digest"] = canonical_digest(request["parameters"])
            request["operator_authorization"]["parameters_digest"] = request["parameters_digest"]
            cases.append(request)
        request = self.request("create_atom", mode="execute")
        request["proposal_receipt"] = {"unexpected": {"definition_manifest": request["definition_manifest"]}}
        cases.append(request)

        for request in cases:
            with self.subTest(request=request):
                self.assertEqual("rejected", self.adapter.invoke("create_atom", request)["disposition"])
        self.assertEqual([], self.support.calls)

    def test_execute_rejects_non_object_empty_or_digest_mismatched_receipts(self) -> None:
        for receipt in ("proposal:fixture", {}, {"request_id": "changed"}):
            with self.subTest(receipt=receipt):
                request = self.request("create_atom", mode="execute")
                request["proposal_receipt"] = receipt
                result = self.adapter.invoke("create_atom", request)
                self.assertEqual("blocked", result["disposition"])
        self.assertEqual([], self.support.calls)

    def test_stale_manifest_and_matching_or_different_shadow_manifest_fields_reject_before_support(self) -> None:
        cases = []
        altered = self.request("create_atom")
        altered["definition_manifest"]["manifest_digest"] = "b" * 64
        cases.append(altered)
        stale_ref = self.request("create_atom")
        stale_ref["definition_manifest"]["manifest_ref"] = (
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_workflow_bindings.json"
        )
        cases.append(stale_ref)
        for value in (self.manifest["canonical_manifest_sha256"], "c" * 64):
            shadow = self.request("create_atom")
            shadow["source_freshness"]["definition_manifest_digest"] = value
            cases.append(shadow)
        stale = self.request("create_atom")
        stale["source_freshness"]["selected_binding_digest"] = "d" * 64
        cases.append(stale)
        for request in cases:
            result = self.adapter.invoke("create_atom", request)
            self.assertEqual("rejected", result["disposition"])
        self.assertEqual([], self.support.calls)

    def test_apply_unknown_route_bad_lineage_and_recording_recovery_are_strict(self) -> None:
        apply = self.request("create_atom", mode="apply")
        self.assertEqual("rejected", self.adapter.invoke("create_atom", apply)["disposition"])
        malformed = self.request("create_atom")
        malformed["lineage"] = {"parent_workflow_run_id": "not-a-real-lineage", "unexpected": True}
        self.assertEqual("rejected", self.adapter.invoke("create_atom", malformed)["disposition"])
        recovered = self.adapter.recover_recording({"pending_event_ref": "event:pending", "request_id": "recovery-1"})
        self.assertEqual("receipt:fixture", recovered["receipt_ref"])
        self.assertEqual([{"pending_event_ref": "event:pending", "request_id": "recovery-1"}], self.support.recovery_calls)
        self.assertEqual("rejected", self.adapter.recover_recording({"pending_event_ref": "event:pending", "payload": {}})["disposition"])

if __name__ == "__main__":
    unittest.main()
