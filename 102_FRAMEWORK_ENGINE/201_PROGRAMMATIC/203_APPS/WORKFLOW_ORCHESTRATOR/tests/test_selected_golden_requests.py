"""Strict fifteen-route request-carrier construction checks."""
from __future__ import annotations
import copy
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP"))
sys.path.insert(0, str(ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR"))
from selected_workflows_docker_fixture import FixtureLease, GoldenCase, GoldenProject, ROUTE_CASES, digest
from selected_routes import SelectedRouteAdapter
from selected_execution import SelectedExecution

class SelectedGoldenRequestsTest(unittest.TestCase):
    def fixture(self, case: str, route: str):
        parent = ROOT / ".caprmedio_tmp/tests/selected-golden-requests"; parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent)); project = GoldenProject(ROOT, root, GoldenCase(case, route)); project.prepare()
        return FixtureLease(root), project

    def test_all_fifteen_preview_and_execute_carriers_are_digest_bound(self):
        for case, route in ROUTE_CASES:
            with self.subTest(case=case):
                lease, project = self.fixture(case, route)
                try:
                    preview = project.request(request_id=f"preview-{case.lower()}")
                    self.assertEqual("preview", preview["mode"]); self.assertEqual(digest(preview["parameters"]), preview["parameters_digest"])
                    self.assertEqual(digest(preview["target_frontier"]), preview["target_frontier_digest"])
                    self.assertEqual(digest(preview["effects"]), preview["effects_digest"])
                    if case in {"W14", "W15"}: self.assertEqual([], preview["effects"])
                    execute = project.request(request_id=f"execute-{case.lower()}", mode="execute", receipt={"fixture": case}, receipt_digest=digest({"fixture": case}))
                    self.assertEqual(execute["request_id"], execute["requested_runs"][0]["requested_run_id"])
                    self.assertTrue(execute["operator_authorization"]["authorization_freshness"]["digest"])
                    self.assertEqual(execute["parameters_digest"], execute["operator_authorization"]["parameters_digest"])
                    if case == "W10":
                        self.assertEqual(preview["parameters"], execute["parameters"])
                    if case == "W13":
                        self.assertEqual("apply", preview["parameters"]["operation"])
                        self.assertEqual(preview["parameters"]["expected_source_frontier_digest"],
                                         execute["parameters"]["expected_source_frontier_digest"])
                finally: lease.cleanup()

    def test_query_inputs_are_closed_and_mutation_free(self):
        for case, route in (("W14", "find_and_fetch_artifacts"), ("W15", "find_and_fetch_journal_events")):
            lease, project = self.fixture(case, route)
            try:
                request = project.request(request_id=case.lower())
                self.assertEqual({"query_request"}, set(request["parameters"])); self.assertEqual([], request["effects"])
                if case == "W15":
                    relative = (".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
                                "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml")
                    self.assertEqual((ROOT / relative).read_bytes(), (project.root / relative).read_bytes())
                    self.assertIn(b"[query]", (project.root / relative).read_bytes())
                    journal = project.root / ".caprmedio_caprmedio/_journal"
                    self.assertTrue(journal.is_dir())
                    self.assertEqual([], list(journal.iterdir()))
            finally: lease.cleanup()

    def test_w10_structural_recovery_uses_current_pinned_approval_and_denies_tampering(self):
        lease, project = self.fixture("W10", "revert_changes")
        try:
            preview = project.request(request_id="preview-w10")
            execute = project.request(request_id="preview-w10", mode="execute", receipt={"fixture": "W10"},
                                      receipt_digest=digest({"fixture": "W10"}))
            frozen = SelectedExecution(project.root).freeze(
                {"operation": "enqueue_selected", "run_id": execute["request_id"], "execution": execute}
            )
            self.assertEqual("preview-w10", frozen["request"]["run_id"])
            parameters = project.native_revert_parameters()
            manifest = parameters["approved_reversal_manifest"]
            request = manifest["request"]
            revert_root = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/REVERT_CHANGES"
            if str(revert_root) not in sys.path:
                sys.path.insert(0, str(revert_root))
            from native_revert_provider import make_native_revert_service
            service = make_native_revert_service({"project_root": str(project.root), "approved_reversal_request": request})
            self.assertEqual("admitted", service.admit(request)["outcome"])
            tampered = copy.deepcopy(request)
            tampered["operator_decision"]["evidence_hash"] = "0" * 64
            denied = service.admit(tampered)
            self.assertEqual("blocked", denied["outcome"])
            self.assertTrue((project.root / ".caprmedio_caprmedio/_journal").is_dir())
        finally: lease.cleanup()

    def test_execution_project_root_changes_only_container_visible_w09_w13_paths(self):
        parent = ROOT / ".caprmedio_tmp/tests/selected-golden-requests"; parent.mkdir(parents=True, exist_ok=True)
        for case, route in (("W09", "run_implementation_workflow"), ("W13", "build_applicable_methodology")):
            root = Path(tempfile.mkdtemp(dir=parent))
            lease = FixtureLease(root)
            try:
                project = GoldenProject(ROOT, root, GoldenCase(case, route), execution_project_root="/project")
                project.prepare()
                parameters = project.request(request_id=f"container-{case.lower()}")["parameters"]
                if case == "W09":
                    packet = parameters["base_packet"]
                    self.assertEqual("/project/fixture/disposable-workspace", packet["workspace"])
                    self.assertEqual(packet["workspace"], packet["permissions"]["implementation_workspace"]["path"])
                else:
                    self.assertEqual("/project", parameters["project_root"])
            finally: lease.cleanup()

    def test_fourteen_non_revert_routes_reach_shared_preview_and_execute_admission(self):
        for case, route in ROUTE_CASES:
            if case == "W10":
                continue
            with self.subTest(case=case):
                lease, project = self.fixture(case, route)
                try:
                    adapter = SelectedRouteAdapter(project.root)
                    before = project.snapshot()
                    preview_request = project.request(request_id=f"preview-{case.lower()}")
                    preview = adapter.invoke(route, preview_request)
                    self.assertEqual("preview", preview.get("disposition"), preview)
                    self.assertEqual(before, project.snapshot())
                    execute = project.request(request_id=f"preview-{case.lower()}", mode="execute",
                                              receipt=preview["proposal_receipt"], receipt_digest=preview["proposal_receipt_digest"])
                    frozen = SelectedExecution(project.root).freeze({"operation": "enqueue_selected", "run_id": execute["request_id"], "execution": execute})
                    self.assertEqual(execute["request_id"], frozen["request"]["run_id"])
                    admitted = adapter.invoke(route, execute)
                    # The host lacks PyYAML required by the queue import; this
                    # is a truthful shared-admission environment blocker, not
                    # a route or effect pass.
                    self.assertEqual("blocked", admitted.get("disposition"), admitted)
                    self.assertTrue(any(marker in admitted["diagnostics"][0] for marker in (
                        "No module named 'yaml'", "initialize its DBOS database"
                    )))
                    malformed = dict(preview_request); malformed["parameters_digest"] = "0" * 64
                    self.assertEqual("rejected", adapter.invoke(route, malformed)["disposition"])
                    denied = dict(execute); denied["operator_authorization"] = dict(execute["operator_authorization"]); denied["operator_authorization"]["authorization_freshness"] = {"state": "stale", "digest": "0" * 64}
                    self.assertEqual("blocked", adapter.invoke(route, denied)["disposition"])
                finally: lease.cleanup()


if __name__ == "__main__": unittest.main()
