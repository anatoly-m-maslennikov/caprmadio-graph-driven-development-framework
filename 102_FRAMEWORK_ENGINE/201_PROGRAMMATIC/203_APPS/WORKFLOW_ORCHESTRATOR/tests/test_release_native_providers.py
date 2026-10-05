"""Focused private provider contracts, with explicit admission/phase doubles.

RunExecutionSession and SelectedExecution are real. The test tracker and phase
effects are doubles: this is not canonical Journal, image, MCP or restart proof.
"""
from __future__ import annotations

import copy
from dataclasses import dataclass
from pathlib import Path
import re
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
MCP = APP.parents[1] / "204_MCP"
RELEASE = TOOLS / "RELEASE_VERSION"
for location in (APP, TOOLS, MCP, RELEASE):
    sys.path.insert(0, str(location))

import release_actions
import selected_routes
from release_image import DockerSubprocessExecutor
from selected_execution import SelectedExecution, SelectedExecutionError, build_requested_runs
from selected_native_providers import SelectedNativeProviders
from workflow_run_support import RunExecutionSession


CURRENT_RELEASE_PHASES = (
    ("CA-O-170", "CA-O-165", "freeze"),
    ("CA-O-171", "CA-O-165", "validate"),
    ("CA-O-172", "CA-O-166", "deliver_sources"),
    ("CA-O-173", "CA-O-166", "compile"),
    ("CA-O-185", "CA-O-168", "closed_unit_gate"),
    ("CA-O-175", "CA-O-167", "stage_candidate"),
    ("CA-O-176", "CA-O-168", "candidate_image_build"),
    ("CA-O-186", "CA-O-168", "candidate_image_canary"),
    ("CA-O-182", "CA-O-181", "host_candidate_e2e"),
    ("CA-O-184", "CA-O-183", "aggregate_full_gate"),
    ("CA-O-178", "CA-O-169", "promote"),
    ("CA-O-179", "CA-O-169", "retire"),
)


@dataclass(frozen=True)
class PhaseResult:
    outcome: str = "completed"
    effect_evidence_refs: tuple[str, ...] = ()
    reason: str = "explicit test double"


class TrackerDouble:
    def __init__(self):
        self.events = []
        self.pending = False

    def _lazy_journal_event(self, request, record, event, outcome, result, effects, report, bindings):
        return {"event_id": str(len(self.events)), "run": record, "event": event,
                "outcome": outcome, "result_ref": result, "effect_refs": effects}

    def _append_one(self, event, result, effects):
        if self.pending:
            raise OSError("explicit recording failure double")
        self.events.append(event)
        return {"event_id": event["event_id"]}


class ReleaseSourceBindingTests(unittest.TestCase):
    """Source-only guard: this does not allocate a fixture directory."""

    def test_private_provider_fixture_uses_the_current_release_workflow_revision(self):
        source = APP.parents[3] / (
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/"
            "CA-O-164-PROJECT_CONFIGURATION-WORKFLOW--release-a-selected-framework-version.md"
        )
        text = source.read_text(encoding="utf-8")
        self.assertIn("atom_id: CA-O-164", text)
        self.assertIn("version: 5", text)
        source_pairs = tuple(re.findall(
            r"^\| (CA-O-\d+) \| (CA-O-\d+) \| ([a-z0-9_]+) \|$", text, flags=re.MULTILINE,
        ))
        self.assertEqual(CURRENT_RELEASE_PHASES, source_pairs)

    def test_private_provider_phase_contract_matches_current_o164_graph(self):
        self.assertEqual(CURRENT_RELEASE_PHASES, release_actions.PHASES)


class ReleaseNativeProvidersTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.parameters = {"project_root": str(self.root), "operation": "apply", "fixture": True}
        self.graph = {"route": "release_version", "workflow": self.binding("CA-O-164", "workflow", 5),
                      "entry_step": "CA-O-170", "steps": []}
        for index, (step, action, _phase) in enumerate(release_actions.PHASES):
            edge = {"result": f"phase_{index}"}
            edge.update({"next": release_actions.PHASES[index + 1][0]}
                        if index < len(release_actions.PHASES) - 1 else {"terminal": "completed"})
            self.graph["steps"].append({**self.binding(step, "step"),
                                        "actions": [self.binding(action, "action")], "on_result": [edge]})
        self.admitted = {"release_source_admissions": [{"fixture": True}], "manifest_ref": "manifest.json",
                         "canonical_manifest_sha256": "1" * 64}
        execution = {"mode": "execute", "request_id": "fixture-request", "operation_route": "release_version",
                     "workflow_run_id": "fixture-workflow", "parameters": self.parameters,
                     "requested_runs": build_requested_runs(self.graph, "fixture-workflow"),
                     "definition_manifest": {"manifest_ref": "manifest.json", "manifest_digest": "1" * 64}}
        self.frozen = {"request": {"operation": "enqueue_selected", "run_id": "fixture-workflow",
                                    "execution": execution}, "graph": self.graph}
        self.tracker = TrackerDouble()
        self.session = RunExecutionSession(self.tracker, execution)
        self.private_runs = []
        self.direct_checkpoints = []

        def begin_private_run(*_args, checkpoint_callback=None, **_kwargs):
            self.assertTrue(callable(checkpoint_callback))
            run = SimpleNamespace(
                frozen_parameters_sha256="2" * 64,
                checkpoint_callback=checkpoint_callback,
                contexts={},
                results={},
            )
            self.private_runs.append(run)
            return run

        self.begin = self.enterContext(patch.object(release_actions, "begin_release_action_run",
             side_effect=begin_private_run))
        self.execute = self.enterContext(patch.object(release_actions, "execute_release_action", return_value=PhaseResult()))
        self.dump_checkpoint = self.enterContext(patch(
            "release_checkpoint.dump_release_checkpoint",
            side_effect=lambda run, *, shared_recordings, pending_recordings: {
                "schema": "fixture-release-checkpoint",
                "phase_count": len(run.contexts),
                "shared_recording_count": len(shared_recordings),
                "pending_recording_count": len(pending_recordings),
            },
        ))
        self.enterContext(patch.object(selected_routes, "load_selected_manifest", return_value=self.admitted))
        self.enterContext(patch.object(SelectedExecution, "_revalidate", return_value=self.graph))

    @staticmethod
    def binding(atom, kind, version=1):
        return {"atom_id": atom, "kind": kind, "version": version, "path": f"definitions/{atom}.md", "sha256": "0" * 64}

    def providers(self):
        return SelectedNativeProviders(self.root, implementation_agent=lambda *args: {}).execution(self.frozen)

    def context(self, index=0, *, session=None):
        session = session or self.session
        workflow = session.start_run("fixture-workflow")
        step_id = SelectedExecution._requested_step_id("fixture-workflow", index + 1, 1)
        step = session.start_run(step_id)
        action_id = f"{step_id}:action:1"
        action = session.start_run(action_id)
        definition = self.graph["steps"][index]

        def checkpoint_writer(payload):
            self.direct_checkpoints.append(payload)

        def checkpoint_reader():
            return None

        def progress_reader(requested_action_id):
            actual = session.actual.get(requested_action_id)
            if actual is None:
                raise SelectedExecutionError("fixture progress has no requested Action")
            terminal = session.terminal.get(requested_action_id, {})
            return {
                "action_run_id": actual["run_id"],
                "result": terminal.get("result", "fixture"),
                "effect_refs": terminal.get("effect_refs", []),
            }

        return {"session": session, "sealed_outer_admission": True, "project_root": self.root,
                "route": "release_version", "parameters": self.parameters,
                "workflow_definition": self.graph["workflow"], "workflow_run_id": workflow["run_id"],
                "step_run_id": step["run_id"], "action_run_id": action["run_id"],
                "requested_action_run_id": action_id, "step_definition_id": definition["atom_id"],
                "action_definition_id": definition["actions"][0]["atom_id"],
                "action_definition": definition["actions"][0],
                "step_definition": {key: value for key, value in definition.items() if key not in {"actions", "on_result"}},
                "checkpoint_writer": checkpoint_writer,
                "checkpoint_reader": checkpoint_reader,
                "checkpoint_progress_reader": progress_reader,
                "restored_action": False}

    def test_construction_starts_no_run_phase_or_image_call(self):
        executor = SimpleNamespace(run=lambda *args: self.fail("construction invoked image"))
        SelectedNativeProviders(self.root, release_image_executor=executor)
        self.providers()
        self.begin.assert_not_called()
        self.execute.assert_not_called()
        self.assertEqual(self.session.actual, {})

    def test_default_image_binding_is_program_owned_docker_executor(self):
        selected = self.providers()
        selected.handlers["CA-O-165"](self.context())
        admission = self.begin.call_args.kwargs["image_executor"]
        self.assertIsInstance(admission, release_actions.AdmittedImageExecutor)
        self.assertIsInstance(admission.executor, DockerSubprocessExecutor)

    def test_complete_current_phase_graph_uses_one_private_run_and_shared_session(self):
        selected = self.providers()
        result = selected._execute_graph(self.frozen, self.session)
        self.assertEqual(result["outcome"], "completed")
        self.assertEqual(self.begin.call_count, 1)
        self.assertEqual(self.execute.call_count, len(release_actions.PHASES))
        self.assertEqual(len(self.session.actual), 1 + 2 * len(release_actions.PHASES))
        self.assertEqual(len(self.session.terminal), 1 + 2 * len(release_actions.PHASES))
        self.assertEqual(len(self.tracker.events), 2 * (1 + 2 * len(release_actions.PHASES)))
        self.assertEqual(len(self.private_runs), 1)
        self.assertTrue(callable(self.private_runs[0].checkpoint_callback))
        self.assertEqual(self.dump_checkpoint.call_count, len(release_actions.PHASES))
        typed = [call.kwargs["context"] for call in self.execute.call_args_list]
        self.assertEqual([(item.step_atom_id, item.action_atom_id) for item in typed],
                         [phase[:2] for phase in release_actions.PHASES])
        self.assertEqual({item.workflow_run_id for item in typed}, {"fixture-workflow"})

    def test_missing_source_admission_refuses_before_phase(self):
        self.admitted["release_source_admissions"] = []
        with self.assertRaises(SelectedExecutionError):
            self.providers()
        self.begin.assert_not_called()

    def test_wrong_manifest_digest_refuses_before_phase(self):
        self.frozen["request"]["execution"]["definition_manifest"]["manifest_digest"] = "3" * 64
        with self.assertRaises(SelectedExecutionError):
            self.providers()
        self.begin.assert_not_called()

    def test_wrong_workflow_revision_and_pairs_refuse(self):
        for mutation in (lambda graph: graph["workflow"].update(version=1),
                         lambda graph: graph["steps"][1].update(atom_id="CA-O-999")):
            graph = copy.deepcopy(self.graph)
            mutation(graph)
            with patch.object(SelectedExecution, "_revalidate", return_value=graph):
                frozen = {**self.frozen, "graph": graph}
                with self.assertRaises(SelectedExecutionError):
                    SelectedNativeProviders(self.root).execution(frozen)
        self.begin.assert_not_called()

    def test_context_root_request_definition_and_parent_mismatches_refuse(self):
        handler = self.providers().handlers["CA-O-165"]
        context = self.context()
        for key, value in (("sealed_outer_admission", False), ("project_root", self.root / "wrong"),
                           ("parameters", {}), ("workflow_run_id", "other"),
                           ("action_run_id", "other"), ("requested_action_run_id", "other"),
                           ("action_definition", {}), ("step_definition_id", "CA-O-999")):
            with self.subTest(key=key), self.assertRaises(SelectedExecutionError):
                handler({**context, key: value})
        self.begin.assert_not_called()

    def test_missing_actual_identities_refuse_cleanly(self):
        handler = self.providers().handlers["CA-O-165"]
        context = self.context()
        self.session.actual.clear()
        with self.assertRaises(SelectedExecutionError):
            handler(context)
        self.begin.assert_not_called()

    def test_unrecorded_previous_action_blocks_and_does_not_advance(self):
        handler = self.providers().handlers["CA-O-165"]
        handler(self.context())
        result = handler(self.context(1))
        self.assertEqual(result["terminal_outcome"], "interrupted_pending")
        self.assertEqual(self.execute.call_count, 1)

    def test_pending_previous_recording_blocks_and_does_not_replay(self):
        handler = self.providers().handlers["CA-O-165"]
        first = self.context()
        handler(first)
        self.tracker.pending = True
        recorded = self.session.finish_run(first["action_run_id"], outcome="completed", result_ref="fixture.json", effect_refs=[])
        self.assertEqual(recorded["disposition"], "recording_pending")
        self.tracker.pending = False
        self.assertEqual(handler(self.context(1))["result"], "blocked")
        self.assertEqual(self.execute.call_count, 1)

    def test_phase_pending_stops_graph_before_next_phase(self):
        self.execute.return_value = PhaseResult(outcome="pending")
        result = self.providers()._execute_graph(self.frozen, self.session)
        self.assertEqual(result["outcome"], "interrupted_pending")
        self.assertEqual(self.execute.call_count, 1)
        self.assertEqual(len(self.session.actual), 3)

    def test_unsafe_or_absent_effect_references_refuse(self):
        handler = self.providers().handlers["CA-O-165"]
        context = self.context()
        for reference in ("../outside", "/absolute", "missing", "#sha256=fixture"):
            with self.subTest(reference=reference):
                self.execute.return_value = PhaseResult(effect_evidence_refs=(reference,))
                with self.assertRaises(SelectedExecutionError):
                    handler(context)

    def test_effect_reference_symlink_escape_refuses(self):
        handler = self.providers().handlers["CA-O-165"]
        (self.root / "escape").symlink_to("/tmp", target_is_directory=True)
        self.execute.return_value = PhaseResult(effect_evidence_refs=("escape",))
        with self.assertRaises(SelectedExecutionError):
            handler(self.context())

    def test_non_release_execution_keeps_native_handlers_without_release_installation(self):
        self.frozen["request"]["execution"]["operation_route"] = "create_atom"
        selected = self.providers()
        self.assertIn("CA-O-131", selected.handlers)
        self.assertNotIn("CA-O-165", selected.handlers)
        self.begin.assert_not_called()


class ReleaseResultSerializationTests(unittest.TestCase):
    """Pure result-boundary checks need no disposable filesystem effects."""
    def test_phase_result_conversion_preserves_typed_data(self):
        self.assertEqual(SelectedNativeProviders._json_value(PhaseResult()),
                         {"outcome": "completed", "effect_evidence_refs": [], "reason": "explicit test double"})

    def test_result_conversion_refuses_untyped_private_objects(self):
        with self.assertRaises(SelectedExecutionError):
            SelectedNativeProviders._json_value(object())

    def test_result_conversion_handles_nested_relative_paths(self):
        self.assertEqual(SelectedNativeProviders._json_value({"refs": (Path("evidence/receipt.json"),)}),
                         {"refs": ["evidence/receipt.json"]})


if __name__ == "__main__":
    unittest.main()
