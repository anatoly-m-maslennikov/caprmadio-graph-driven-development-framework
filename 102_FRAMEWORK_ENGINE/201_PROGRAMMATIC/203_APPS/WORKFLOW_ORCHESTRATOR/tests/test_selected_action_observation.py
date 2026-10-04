"""Focused read-only evidence contracts for selected Action observations."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
MCP = APP.parents[1] / "204_MCP"
sys.path.insert(0, str(APP))
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(MCP))

import work_journal  # noqa: E402
from selected_routes import _QueueBackedSelectedSupport  # noqa: E402
from selected_action_observation import observe_selected_action  # noqa: E402


class SelectedActionObservationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n', encoding="utf-8",
        )
        self.manifest = {
            "manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
            "canonical_manifest_sha256": "a" * 64,
            "source_freshness": {
                "selected_source_registry_ref": "analysis/registry.md",
                "selected_source_registry_version": 2,
                "selected_source_registry_digest": "b" * 64,
                "selected_binding_ref": "projection/bindings.json",
                "selected_binding_digest": "c" * 64,
            },
            "routes": [{
                "route": "find_and_fetch_artifacts",
                "workflow": self._pin("CA-O-158", "workflow.md"),
                "ordered_steps": [{
                    "step": self._pin("CA-O-160", "step.md"),
                    "action": self._pin("CA-O-159", "action.md"),
                }],
            }],
        }

    @staticmethod
    def _pin(atom_id: str, name: str) -> dict[str, object]:
        return {"atom_id": atom_id, "version": 2, "source_path": f"definitions/{name}",
                "digest": hashlib.sha256(name.encode("utf-8")).hexdigest()}

    @staticmethod
    def _definition(pin: dict[str, object]) -> dict[str, object]:
        return {"atom_id": pin["atom_id"], "version": pin["version"],
                "path": pin["source_path"], "digest": pin["digest"]}

    def _run(self, name: str) -> tuple[str, Path, dict[str, object]]:
        action_id = f"{name}:step:1:action:1"
        step_id = f"{name}:step:1"
        route = self.manifest["routes"][0]
        action = self._definition(route["ordered_steps"][0]["action"])
        workflow = self._definition(route["workflow"])
        step = self._definition(route["ordered_steps"][0]["step"])
        execution = {
            "request_id": f"request-{name}", "assigned_action_id": f"operator-{name}",
            "operation_route": "find_and_fetch_artifacts",
            "definition_manifest": {"manifest_ref": self.manifest["manifest_ref"],
                                    "manifest_digest": self.manifest["canonical_manifest_sha256"]},
            "source_freshness": self.manifest["source_freshness"],
            "requested_runs": [
                {"requested_run_id": name, "kind": "workflow", "definition": workflow},
                {"requested_run_id": step_id, "kind": "step", "definition": step,
                 "parent_requested_run_id": name},
                {"requested_run_id": action_id, "kind": "action", "definition": action,
                 "parent_requested_run_id": step_id},
            ],
        }
        graph = {
            "route": "find_and_fetch_artifacts", "manifest_ref": self.manifest["manifest_ref"],
            "manifest_digest": self.manifest["canonical_manifest_sha256"],
            "workflow": {"atom_id": workflow["atom_id"], "kind": "workflow",
                         "version": workflow["version"], "path": workflow["path"], "sha256": workflow["digest"]},
            "steps": [{
                "atom_id": step["atom_id"], "kind": "step", "version": step["version"],
                "path": step["path"], "sha256": step["digest"],
                "actions": [{"atom_id": action["atom_id"], "kind": "action", "version": action["version"],
                             "path": action["path"], "sha256": action["digest"]}],
            }],
        }
        folder = self.root / ".caprmedio_install/workflow_orchestrator/runs" / name
        folder.mkdir(parents=True)
        (folder / "selected_request.json").write_text(json.dumps({"request": {
            "operation": "enqueue_selected", "run_id": name, "execution": execution,
        }, "graph": graph}), encoding="utf-8")
        return action_id, folder, execution

    def _progress(self, action_id: str, folder: Path) -> str:
        result_ref = (folder.relative_to(self.root) / f"{action_id}.json").as_posix()
        (folder / f"{action_id}.json").write_text(json.dumps({
            "result": "completed", "action_run_id": action_id,
            "native_result": {"token": "must-not-be-disclosed", "payload": "unbound-output"},
        }), encoding="utf-8")
        return result_ref

    def _record_terminal(
        self, action_id: str, result_ref: str, execution: dict[str, object], *, event_name: str, outcome: str,
    ) -> dict[str, object]:
        step_id = f"{execution['request_id'][8:]}:step:1"
        action = self._definition(self.manifest["routes"][0]["ordered_steps"][0]["action"])
        event = work_journal.with_event_digest({
            "schema_version": 5, "kind": "workflow_execution", "event_id": f"event-{outcome}-{action_id}",
            "action_id": execution["assigned_action_id"], "event": event_name, "author": "run-support",
            "occurred_at": "2026-10-05T12:00:00+00:00",
            "llm_session": {"app": "run-support", "uuid": execution["request_id"]},
            "structural_scope": "TOOLS",
            "initiative": {"initiative_id": "fixture", "instruction_summary": "fixture"},
            "run": {"run_id": action_id, "kind": "action", "definition": action,
                    "parent_run_id": step_id},
            "definition_bindings": [{"kind": "action", **action}],
            "input_ref": "fixture/input", "outcome": outcome, "result_ref": result_ref,
            "effect_refs": [], "report_ref": None, "redaction": {"redacted": False, "fields": []},
        })
        receipt = work_journal.append_sealed_events(
            self.root, [event], author="run-support", local_date="2026-10-05", timezone="UTC",
        )[0]
        return dict(receipt)

    def _accepted(self, folder: Path, receipt: dict[str, object]) -> None:
        (folder / "accepted.json").write_text(json.dumps({"result": {
            "event_receipts": [receipt], "disposition": "terminal",
        }}), encoding="utf-8")

    def test_completed_observation_requires_a_matching_sealed_journal_fact(self) -> None:
        action_id, folder, execution = self._run("completed")
        result_ref = self._progress(action_id, folder)
        self._accepted(folder, self._record_terminal(action_id, result_ref, execution,
                                                      event_name="completed", outcome="completed"))
        before = {path.relative_to(self.root).as_posix(): path.read_bytes()
                  for path in self.root.rglob("*") if path.is_file()}

        result = observe_selected_action(self.root, action_id, self.manifest)

        after = {path.relative_to(self.root).as_posix(): path.read_bytes()
                 for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(before, after)
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual("completed", result["outcome"])
        self.assertEqual("completed:step:1", result["step_run_id"])
        self.assertEqual(result_ref, result["result_ref"])
        self.assertEqual("completed", result["journal_confirmation"]["event"])
        self.assertNotIn("must-not-be-disclosed", json.dumps(result))
        self.assertNotIn("unbound-output", json.dumps(result))

    def test_failed_and_pending_observations_remain_truthful(self) -> None:
        failed_id, failed_folder, failed_execution = self._run("failed")
        failed_ref = self._progress(failed_id, failed_folder)
        self._accepted(failed_folder, self._record_terminal(
            failed_id, failed_ref, failed_execution, event_name="failed", outcome="failed",
        ))
        pending_id, pending_folder, _ = self._run("pending")
        self._progress(pending_id, pending_folder)

        failed = observe_selected_action(self.root, failed_id, self.manifest)
        pending = observe_selected_action(self.root, pending_id, self.manifest)

        self.assertEqual(("terminal", "failed"), (failed["disposition"], failed["outcome"]))
        self.assertEqual(("recording_pending", "pending"), (pending["disposition"], pending["outcome"]))
        self.assertEqual(
            (pending_folder.relative_to(self.root) / f"{pending_id}.json").as_posix(),
            pending["progress_ref"],
        )
        self.assertNotIn("native_result", pending)

    def test_queue_backed_mcp_helper_observes_without_dispatch(self) -> None:
        action_id, folder, execution = self._run("adapter")
        result_ref = self._progress(action_id, folder)
        self._accepted(folder, self._record_terminal(action_id, result_ref, execution,
                                                      event_name="completed", outcome="completed"))
        support = _QueueBackedSelectedSupport(self.root, object())

        with patch("selected_routes.load_selected_manifest", return_value=self.manifest):
            result = support.get_selected_action_run({"action_run_id": action_id})

        self.assertEqual(("terminal", "completed"), (result["disposition"], result["outcome"]))

    def test_unknown_and_unsafe_identities_are_not_resolved(self) -> None:
        unknown = observe_selected_action(self.root, "unknown:step:1:action:1", self.manifest)
        unsafe = observe_selected_action(self.root, "../selected_request.json", self.manifest)

        self.assertEqual(("unknown", "unknown"), (unknown["disposition"], unknown["outcome"]))
        self.assertEqual(("rejected", "rejected"), (unsafe["disposition"], unsafe["outcome"]))

    def test_stale_manifest_never_relabels_saved_action_progress(self) -> None:
        action_id, folder, _ = self._run("stale")
        self._progress(action_id, folder)
        stale = {**self.manifest, "canonical_manifest_sha256": "d" * 64}

        result = observe_selected_action(self.root, action_id, stale)

        self.assertEqual(("blocked", "blocked"), (result["disposition"], result["outcome"]))
        self.assertIn("current canonical manifest", result["diagnostics"][0])
