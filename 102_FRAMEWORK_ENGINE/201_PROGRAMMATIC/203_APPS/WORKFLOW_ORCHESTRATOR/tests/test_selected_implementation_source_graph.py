"""Source-grounded W09 graph interpretation checks without worker effects."""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_execution import SelectedExecution, SelectedExecutionError  # noqa: E402


_STEPS = (
    ("CA-O-091", "CA-O-017"), ("CA-O-092", "CA-O-018"),
    ("CA-O-093", "CA-O-019"), ("CA-O-094", "CA-O-020"),
    ("CA-O-095", "CA-O-089"), ("CA-O-096", "CA-O-024"),
    ("CA-O-099", "CA-O-021"),
)


class SelectedImplementationSourceGraphTests(unittest.TestCase):
    """W09 reads the pinned Workflow graph rather than stale manifest edges."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def _write(self, name: str, atom_id: str, *, body: str = "") -> dict[str, object]:
        path = self.root / "definitions" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"---\natom_id: {atom_id}\nversion: 1\nstatus: Active\n---\n{body}",
            encoding="utf-8",
        )
        return {
            "atom_id": atom_id,
            "version": 1,
            "source_path": path.relative_to(self.root).as_posix(),
            "digest": hashlib.sha256(path.read_bytes()).hexdigest(),
        }

    def _route(self, *, invalid_terminal: bool = False) -> dict[str, object]:
        terminal = "unknown_terminal" if invalid_terminal else "blocked"
        workflow = self._write(
            "workflow.md", "CA-O-016",
            body=(
                "# Current graph\n\n"
                "| From Step | Result condition | Next Step **or** terminal result |\n"
                "| --- | --- | --- |\n"
                "| CA-O-091 | evaluation_ready | CA-O-092 |\n"
                "| CA-O-091 | requirement_ready | CA-O-093 |\n"
                "| CA-O-091 | evaluation_runnable | CA-O-094 |\n"
                "| CA-O-091 | complete | completed |\n"
                f"| CA-O-091 | blocked | {terminal} |\n"
                "| CA-O-092 | prepared | CA-O-091 |\n"
                "| CA-O-092 | blocked | blocked |\n"
                "| CA-O-093 | implemented | CA-O-091 |\n"
                "| CA-O-093 | blocked | blocked |\n"
                "| CA-O-094 | passed | CA-O-091 |\n"
                "| CA-O-094 | failed | CA-O-095 |\n"
                "| CA-O-094 | blocked | blocked |\n"
                "| CA-O-095 | expected_initial_failure | CA-O-091 |\n"
                "| CA-O-095 | implementation_defect | CA-O-096 |\n"
                "| CA-O-095 | test_implementation_defect | CA-O-096 |\n"
                "| CA-O-095 | authority_change_required | blocked |\n"
                "| CA-O-095 | environment_blocker | blocked |\n"
                "| CA-O-095 | unresolved | blocked |\n"
                "| CA-O-096 | retry_permitted | CA-O-099 |\n"
                "| CA-O-096 | retry_blocked | blocked |\n"
                "| CA-O-099 | repaired | CA-O-091 |\n"
                "| CA-O-099 | authority_change_required | blocked |\n"
                "| CA-O-099 | blocked | blocked |\n"
            ),
        )
        ordered = []
        for index, (step_id, action_id) in enumerate(_STEPS, 1):
            ordered.append({
                "step": self._write(f"step-{index}.md", step_id),
                "action": self._write(f"action-{index}.md", action_id),
            })
        return {
            "workflow": workflow,
            "ordered_steps": ordered,
            "entry_step": "CA-O-091",
            # Deliberately stale legacy projection: W09 must never use these
            # labels or successor edges when the pinned Workflow has its table.
            "on_result": [
                {"from": "CA-O-091", "condition": "evaluation ready", "to": "CA-O-092"},
                {"from": "CA-O-092", "condition": "tests prepared", "to": "CA-O-093"},
                {"from": "CA-O-093", "condition": "implementation delivered", "to": "CA-O-094"},
                {"from": "CA-O-094", "condition": "checks pass", "to": "complete"},
            ],
        }

    def _reader(self) -> SelectedExecution:
        reader = SelectedExecution.__new__(SelectedExecution)
        reader.root = self.root.resolve()
        reader.implementation_agent = None
        return reader

    @staticmethod
    def _edges(steps: list[dict[str, object]]) -> list[tuple[str, str, str]]:
        rows = []
        for step in steps:
            for edge in step["on_result"]:
                target = edge["next"] if "next" in edge else f"terminal:{edge['terminal']}"
                rows.append((step["atom_id"], edge["result"], target))
        return rows

    def test_uses_exact_current_source_edges_not_stale_manifest_labels(self) -> None:
        steps, entry = self._reader()._d547_steps(self._route())

        self.assertEqual("CA-O-091", entry)
        self.assertEqual(
            [
                ("CA-O-091", "evaluation_ready", "CA-O-092"),
                ("CA-O-091", "requirement_ready", "CA-O-093"),
                ("CA-O-091", "evaluation_runnable", "CA-O-094"),
                ("CA-O-091", "complete", "terminal:completed"),
                ("CA-O-091", "blocked", "terminal:interrupted_pending"),
                ("CA-O-092", "prepared", "CA-O-091"),
                ("CA-O-092", "blocked", "terminal:interrupted_pending"),
                ("CA-O-093", "implemented", "CA-O-091"),
                ("CA-O-093", "blocked", "terminal:interrupted_pending"),
                ("CA-O-094", "passed", "CA-O-091"),
                ("CA-O-094", "failed", "CA-O-095"),
                ("CA-O-094", "blocked", "terminal:interrupted_pending"),
                ("CA-O-095", "expected_initial_failure", "CA-O-091"),
                ("CA-O-095", "implementation_defect", "CA-O-096"),
                ("CA-O-095", "test_implementation_defect", "CA-O-096"),
                ("CA-O-095", "authority_change_required", "terminal:interrupted_pending"),
                ("CA-O-095", "environment_blocker", "terminal:interrupted_pending"),
                ("CA-O-095", "unresolved", "terminal:interrupted_pending"),
                ("CA-O-096", "retry_permitted", "CA-O-099"),
                ("CA-O-096", "retry_blocked", "terminal:interrupted_pending"),
                ("CA-O-099", "repaired", "CA-O-091"),
                ("CA-O-099", "authority_change_required", "terminal:interrupted_pending"),
                ("CA-O-099", "blocked", "terminal:interrupted_pending"),
            ],
            self._edges(steps),
        )

    def test_refuses_source_graph_with_an_undeclared_terminal_status(self) -> None:
        with self.assertRaisesRegex(SelectedExecutionError, "terminal"):
            self._reader()._d547_steps(self._route(invalid_terminal=True))

    def test_native_implementation_label_remains_the_source_edge_label(self) -> None:
        adapter = types.ModuleType("implementation_actions")
        adapter.ACTION_HANDLERS = {"CA-O-017": lambda _parameters, **_kwargs: {"result": "evaluation_ready"}}

        with patch.dict(sys.modules, {"implementation_actions": adapter}):
            handler = self._reader()._native_handlers()["CA-O-017"]
            output = handler({"parameters": {}})

        self.assertEqual("evaluation_ready", output["result"])
        self.assertNotIn("terminal_outcome", output)

    def test_known_stale_publication_effect_is_partial_with_exact_plan_refs(self) -> None:
        output_path = ".caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY/04_requirement/CA-R-001.md"
        plan = [{
            "source_layer": "001_CORE_META_MODEL",
            "atom_id": "CA-R-001",
            "source_atom_id": "CA-R-001",
            "atom_revision": 1,
            "source_atom_revision": 1,
            "source_carrier_path": "source/CA-R-001.md",
            "source_carrier_sha256": "a" * 64,
            "original_relations_sha256": "b" * 64,
            "content_role": "requirement",
            "output_path": output_path,
        }]
        packet = {
            "outcome": "publication_recovery_required",
            "apply_status": "EFFECT_APPLIED_STALE",
            "output_plan": plan,
            "publication": {
                "effect_state": "output_replacement_completed",
                "output_plan": plan,
            },
        }
        adapter = types.ModuleType("compile_applicable_methodology")
        adapter.ACTION_ADAPTERS = {"CA-O-009": lambda _parameters: packet}
        reader = self._reader()
        context = {
            "workflow_definition_id": "CA-O-011",
            "step_definition_id": "CA-O-157",
            "action_definition_id": "CA-O-009",
            "project_root": reader.root,
            "parameters": {"project_root": reader.root.as_posix()},
        }

        with patch.dict(sys.modules, {"compile_applicable_methodology": adapter}):
            handler = reader._native_handlers()["CA-O-009"]
            output = handler(context)

        self.assertEqual("publication_recovery_required", output["result"])
        self.assertEqual("partial", output["terminal_outcome"])
        self.assertEqual([output_path], output["effect_refs"])
        self.assertIs(packet, output["native_result"])
        self.assertNotIn("compiler_publication_recording", output)

    def test_retry_consumption_tracks_completed_repair_rounds_without_double_counting(self) -> None:
        parameters = {
            "base_packet": {
                "retry": {"consumed": 0, "effective_limit": 1, "source": "CA-M-295"},
                "retained_state": {},
            },
            "step_packets": {
                "CA-O-096": {"context": "Integrated"},
                "CA-O-099": {"context": "Isolated"},
            },
        }
        permitted_only = [{
            "step_definition_id": "CA-O-096", "action_definition_id": "CA-O-024",
            "result": "retry_permitted", "outputs": {"consumed": 0},
        }]
        completed_round = [*permitted_only, {
            "step_definition_id": "CA-O-099", "action_definition_id": "CA-O-021",
            "result": "repaired", "outputs": {"changed_paths": ["fixture.py"]},
        }]

        before_repair = SelectedExecution._implementation_packet(parameters, "CA-O-096", permitted_only)
        round_start = SelectedExecution._implementation_packet(parameters, "CA-O-099", permitted_only)
        first_recheck = SelectedExecution._implementation_packet(parameters, "CA-O-096", completed_round)
        repeated_recheck = SelectedExecution._implementation_packet(parameters, "CA-O-096", completed_round)

        self.assertEqual(0, before_repair["retry"]["consumed"])
        self.assertEqual(1, round_start["retry"]["consumed"])
        self.assertEqual(1, first_recheck["retry"]["consumed"])
        self.assertEqual(1, repeated_recheck["retry"]["consumed"])
        self.assertEqual(0, parameters["base_packet"]["retry"]["consumed"])


if __name__ == "__main__":
    unittest.main()
