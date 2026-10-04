"""Registered startup proofs using disposable Projects and an executable mock CLI."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import textwrap
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
REPOSITORY = APP.parents[3]
TOOLS = APP.parents[1] / "201_TOOLS"
REVERT = TOOLS / "WORKFLOW_OPERATIONS/REVERT_CHANGES"
PROMPTS = REPOSITORY / "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW"
for path in (APP, APP / "tests", TOOLS, REVERT, REVERT / "tests", PROMPTS):
    sys.path.insert(0, str(path))

import backend
import lifecycle_intents
import test_native_revert_provider as revert_fixture
from implementation_agent import ImplementationAgent
from native_revert_provider import NativeRevertProvider, make_native_revert_service
from selected_execution import SelectedExecution, build_requested_runs
from selected_native_providers import SelectedNativeProviders
from selected_workflows_docker_fixture import GoldenCase, GoldenProject


class RegisteredDBOS:
    def __init__(self):
        self.steps = {}
        self.workflows = {}

    def step(self, *, name):
        def register(function):
            self.steps[name] = function
            return function
        return register

    def workflow(self, *, name):
        def register(function):
            self.workflows[name] = function
            return function
        return register


class Session:
    """One lazy selected lineage; repeated bridge access reuses the Action."""
    def __init__(self):
        self.started = {}
        self.finished = []

    def start_run(self, requested):
        return self.started.setdefault(requested, {"run_id": f"actual-{len(self.started) + 1}"})

    def finish_run(self, run_id, **result):
        row = {"run_id": run_id, "disposition": "terminal", **result}
        self.finished.append(row)
        return row


class SelectedNativeProvidersTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.project = GoldenProject(REPOSITORY, self.root, GoldenCase("W10", "revert_changes"))
        self.manifest = self.project.prepare()

    def freeze(self, route, parameters, run_id="native-selected"):
        execution = {"mode": "execute", "operation_route": route, "workflow_run_id": run_id,
                     "parameters": parameters, "source_freshness": self.manifest["source_freshness"],
                     "definition_manifest": {"manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
                                             "manifest_digest": self.manifest["canonical_manifest_sha256"]}}
        selected = SelectedExecution(self.root)
        graph = selected._validate_graph(execution)
        execution["requested_runs"] = build_requested_runs(graph, run_id)
        return selected.freeze({"operation": "enqueue_selected", "run_id": run_id, "execution": execution})

    def registered_dispatch(self, frozen, *, agent=None):
        providers = SelectedNativeProviders(self.root, implementation_agent=agent)
        dbos = RegisteredDBOS()
        engine = type("Engine", (), {"root": self.root})()
        backend.register_execution(dbos, engine, selected_providers=providers)
        session = Session()
        with patch.object(SelectedExecution, "_shared_dispatch", lambda selected, saved: selected._execute_graph(saved, session)):
            result = dbos.workflows[backend.SELECTED_WORKFLOW](frozen["request"]["run_id"])
        return result, session

    def structural_request(self):
        path = self.root / ".caprmedio_caprmedio/project_structure.toml"
        before = path.read_text(encoding="utf-8")
        after = before + "\n# admitted partial cutover\n"
        path.write_text(after, encoding="utf-8")
        boundary = {"authorized_boundary": "disposable-cutover", "references": [], "toml": {
            "path": path.relative_to(self.root).as_posix(), "before_text": before,
            "before_sha256": hashlib.sha256(before.encode()).hexdigest(),
            "after_sha256": hashlib.sha256(after.encode()).hexdigest()}}
        target = {"recovery_boundary": boundary}
        effect = {"effect_id": "structure", "target_id": "structure:disposable", "expected_before": "partial cutover",
                  "expected_after": "approved prior state", "expected_current_hash": "", "expected_result_hash": "",
                  "before_evidence": "before:structure", "after_evidence": "after:structure",
                  "capability_binding": revert_fixture.NativeRevertProviderTests._binding(
                      "structure.rollback_scope_unit_change", {"recovery_boundary": boundary}, target,
                      before="before:structure", after="after:structure")}
        provider = NativeRevertProvider({"project_root": str(self.root), "approved_reversal_request":
                                        revert_fixture.NativeRevertProviderTests._request(effect, "placeholder")})
        effect["expected_current_hash"] = provider.observe(effect["target_id"])
        effect["expected_result_hash"] = revert_fixture.canonical_digest({"members": [{
            "path": path.relative_to(self.root).as_posix(), "sha256": hashlib.sha256(before.encode()).hexdigest()}]})
        return revert_fixture.NativeRevertProviderTests._request(effect, effect["expected_current_hash"]), path, before

    def admit(self, request):
        service = make_native_revert_service({"project_root": str(self.root), "approved_reversal_request": request})
        admitted = service.admit(request)
        self.assertEqual("admitted", admitted["outcome"])
        return admitted["approved_reversal_manifest"]

    def test_registered_structural_revert_performs_exact_effect_and_one_action_terminal(self):
        request, path, before = self.structural_request()
        frozen = self.freeze("revert_changes", {"approved_reversal_manifest": self.admit(request)})
        result, session = self.registered_dispatch(frozen)
        self.assertEqual("completed", result["outcome"])
        self.assertEqual(before, path.read_text(encoding="utf-8"))
        self.assertEqual(3, len(session.started))
        self.assertEqual(3, len(session.finished))
        self.assertEqual("reverted", result["step_results"][0]["result"])

    def test_registered_lifecycle_revert_preserves_revision_and_summary(self):
        helper = revert_fixture.NativeRevertProviderTests()
        target_path = self.project._authority_dir / "CA-R-100--target.md"
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as forecast_raw:
            forecast = Path(forecast_raw)
            (forecast / ".git").mkdir()
            control = forecast / ".caprmedio_caprmedio"
            control.mkdir()
            (control / "caprmedio_project_settings.toml").write_text(
                (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").read_text(), encoding="utf-8")
            forecast_path = forecast / target_path.relative_to(self.root)
            forecast_path.parent.mkdir(parents=True, exist_ok=True)
            forecast_path.write_bytes(target_path.read_bytes())
            with patch.object(lifecycle_intents, "datetime", revert_fixture.FrozenDatetime):
                forecast_result = lifecycle_intents.update_atom_action(forecast, {
                    "target": lifecycle_intents.carrier_descriptor(forecast, "CA-R-100"),
                    "proposed": helper._proposal(forecast_path), "change_class": "semantic_revision"}, execute=True, authorized=True)
                target = lifecycle_intents.carrier_descriptor(self.root, "CA-R-100")
                effect = {"effect_id": "lifecycle", "target_id": "atom:CA-R-100", "expected_before": "version 1",
                          "expected_after": "version 2", "expected_current_hash": revert_fixture.canonical_digest(target),
                          "expected_result_hash": revert_fixture.canonical_digest(forecast_result["observed"]),
                          "before_evidence": "before:lifecycle", "after_evidence": "after:lifecycle",
                          "capability_binding": helper._binding("lifecycle.update_atom", {
                              "target": target, "proposed": helper._proposal(target_path), "change_class": "semantic_revision"},
                              target, before="before:lifecycle", after="after:lifecycle")}
                request = helper._request(effect, effect["expected_current_hash"])
                frozen = self.freeze("revert_changes", {"approved_reversal_manifest": self.admit(request)})
                result, session = self.registered_dispatch(frozen)
        self.assertEqual("completed", result["outcome"])
        self.assertIn("Semantic reversal detail.", target_path.read_text())
        self.assertIn("Stable summary", target_path.read_text())
        self.assertTrue(list(target_path.parent.rglob("CA-R-100--target@1.md")))
        self.assertEqual(3, len(session.finished))

    def test_unsupported_and_denied_revert_are_truthful_without_effects(self):
        for capability, granted in (("file.write", True), ("structure.rollback_scope_unit_change", False)):
            with self.subTest(capability=capability, granted=granted):
                request, path, before = self.structural_request()
                binding = request["ordered_effects"][0]["capability_binding"]
                binding["capability_id"] = capability
                binding["permission_evidence"].update(capability_id=capability, granted=granted)
                frozen = self.freeze("revert_changes", {"approved_reversal_manifest": {"request": request}}, run_id=f"denied-{granted}")
                prior = path.read_bytes()
                result, _ = self.registered_dispatch(frozen)
                self.assertEqual("interrupted_pending", result["outcome"])
                self.assertEqual(prior, path.read_bytes())
                self.assertEqual("blocked", result["step_results"][0]["result"])

    def test_registered_implementation_agent_executes_disposable_code_and_assertion(self):
        import implementation_actions
        workspace = self.root / "disposable-workspace"
        workspace.mkdir()
        script = self.root / "mock_cli.py"
        script.write_text(textwrap.dedent('''
            import json, subprocess, sys
            from pathlib import Path
            args = sys.argv[1:]
            output = Path(args[args.index('--output-last-message') + 1])
            workspace = Path(args[args.index('--cd') + 1])
            packet = json.loads(sys.stdin.read().split('Input packet:\\n', 1)[1])
            step = packet['step_marker']
            assert args[args.index('--sandbox') + 1] == 'workspace-write'
            outputs = {}
            if step == 'CA-O-092':
                outputs = {'golden_e2e': True, 'commands': ['assertion.py'], 'expected_outcomes': ['pass']}
            elif step == 'CA-O-093':
                (workspace / 'implementation.py').write_text('def ready():\\n    return True\\n')
                (workspace / 'assertion.py').write_text('from implementation import ready\\nassert ready()\\n')
                outputs = {'candidate': 'actual-code', 'changed_paths': ['implementation.py', 'assertion.py']}
            elif step == 'CA-O-094':
                check = subprocess.run([sys.executable, '-B', 'assertion.py'], cwd=workspace)
                assert check.returncode == 0
                outputs = {'commands': ['assertion.py'], 'checks': [{'returncode': check.returncode}]}
            result = {'CA-O-091': 'evaluation_ready', 'CA-O-092': 'prepared', 'CA-O-093': 'implemented', 'CA-O-094': 'passed'}[step]
            output.write_text(json.dumps({'result': result, 'outputs': outputs, 'evidence': [{'step': step}], 'blockers': []}))
        '''), encoding="utf-8")
        bindings = implementation_actions.current_source_bindings()
        projection = implementation_actions.prepare_method_projection([row["path"] for row in bindings if row["atom_id"].startswith("CA-M-")])
        base = {"workspace": str(workspace), "source_bindings": bindings, "permissions": {"allowed": True,
                "implementation_workspace": {"kind": "disposable_workspace", "path": str(workspace), "allow_write": True}},
                "method_projection": projection, "requirements_delivery": ["R/D"], "evaluations": ["E"],
                "plan_item": {"estimated_minutes": 1}, "handoff_complete": True, "golden_e2e": True,
                "baseline_command": "assertion.py", "agent_timeout_seconds": 5}
        parameters = {"base_packet": base, "step_packets": {step: {"context": context, "step_marker": step}
                      for step, (_action, context) in implementation_actions.ACTION_BY_STEP.items()}}
        frozen = self.freeze("run_implementation_workflow", parameters)
        result, session = self.registered_dispatch(frozen, agent=ImplementationAgent([sys.executable, str(script)]))
        self.assertEqual("completed", result["outcome"])
        self.assertTrue((workspace / "implementation.py").is_file())
        self.assertEqual(["evaluation ready", "tests prepared", "implementation delivered", "checks pass"],
                         [row["result"] for row in result["step_results"]])
        self.assertEqual(9, len(session.started))

    def test_startup_is_lazy_and_default_agent_is_distinct(self):
        with patch("implementation_agent._run", side_effect=AssertionError("startup must not launch Agent")):
            providers = SelectedNativeProviders(self.root)
            self.assertIsInstance(providers.implementation_agent, ImplementationAgent)
            dbos = RegisteredDBOS()
            engine = type("Engine", (), {"root": self.root, "agent": object()})()
            backend.register_execution(dbos, engine, selected_providers=providers)
            self.assertIsNot(engine.agent, providers.implementation_agent)
            self.assertIn(backend.WORKFLOW, dbos.workflows)
            self.assertIn("base-revise-fix", dbos.steps)

    def test_denied_implementation_packet_never_launches_callback(self):
        import implementation_actions
        parameters = {"base_packet": {"source_bindings": implementation_actions.current_source_bindings(),
                                      "permissions": {"allowed": False}},
                      "step_packets": {step: {"context": context}
                                       for step, (_action, context) in implementation_actions.ACTION_BY_STEP.items()}}
        frozen = self.freeze("run_implementation_workflow", parameters)

        def forbidden_agent(_prompt, _packet):
            self.fail("denied Implementation packet launched Agent")

        result, session = self.registered_dispatch(frozen, agent=forbidden_agent)
        self.assertEqual("interrupted_pending", result["outcome"])
        self.assertEqual("blocked", result["step_results"][0]["result"])
        self.assertEqual(3, len(session.started))


if __name__ == "__main__":
    unittest.main()
