"""Golden domain tests for authoritative Project Structure mutations."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest


MODULE = Path(__file__).resolve().parents[1] / "project_structure.py"
TOOLS = Path(__file__).resolve().parents[3]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
SPEC = importlib.util.spec_from_file_location("project_structure", MODULE)
assert SPEC and SPEC.loader
project_structure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = project_structure
SPEC.loader.exec_module(project_structure)
from work_journal import canonical_json_digest  # noqa: E402
from workflow_run_support import RunTracker  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def declaration(
    name: str,
    *,
    parent: str = "PROJECT",
    unit_type: str = "Unordered",
    label: str = "FEATURE",
    level: int = 1,
    navigation: int = 0,
    local_order: int | None = None,
    authority_mode: str | None = None,
) -> dict[str, object]:
    result: dict[str, object] = {
        "scope_unit_name": name,
        "parent": parent,
        "scope_unit_type": unit_type,
        "scope_unit_label": label,
        "structural_level": level,
        "navigational_order_number": navigation,
        "authority_path": f".caprmedio_caprmedio/{name}",
        "delivery_path": f"delivery/{name}",
    }
    if local_order is not None:
        result["local_order"] = local_order
    if authority_mode is not None:
        result["authority_mode"] = authority_mode
    return result


class ProjectStructureActions(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[authority_modes]\ndefault = 'casual'\n", encoding="utf-8"
        )
        self.toml = control / "project_structure.toml"
        self.write_structure([declaration("PARENT", unit_type="Ordered", label="LAYER", local_order=1)])
        self.reference = self.root / "references.md"
        self.reference.write_text("PARENT\n", encoding="utf-8")
        self.carrier = self.root / "observed-carrier.txt"
        self.carrier.write_text("do not delete", encoding="utf-8")

    def write_structure(self, rows: list[dict[str, object]]) -> None:
        self.toml.write_text(project_structure.serialize_project_structure(rows), encoding="utf-8")

    def parameters(self, operation: str, **values: object) -> dict[str, object]:
        result: dict[str, object] = {
            "operation": operation,
            "expected_toml_revision": digest(self.toml),
            "reference_frontier": [],
            "goal_coverage_disposition": {"state": "present", "parent": "PARENT"},
            "preservation_disposition": {"preserved": ["observed-carrier.txt"]},
            "recovery_disposition": {"authorized": True, "boundary": "toml-and-listed-references"},
        }
        result.update(values)
        return result

    def completed_o143_handoff(
        self, context: dict[str, object], applied: dict[str, object], *, result_ref: str = "results/o143.json",
    ) -> dict[str, object]:
        """Model the executor's retained O140--O143 Action records."""
        workflow_run_id = str(context["workflow_run_id"])
        native = applied["native_result"]
        effects = applied["effect_refs"]
        retained: list[dict[str, object]] = []
        for step_id, action_id, result in (
            ("CA-O-140", "CA-O-012", "proposal ready"),
            ("CA-O-141", "CA-O-005", "checks complete"),
            ("CA-O-142", "CA-O-013", "authorization valid"),
            ("CA-O-143", "CA-O-014", "cutover completed"),
        ):
            action_run_id = str(context["action_run_id"]) if step_id == "CA-O-143" else f"{workflow_run_id}:{step_id}"
            path = result_ref if step_id == "CA-O-143" else f"results/{step_id}.json"
            result_path = self.root / path
            result_path.parent.mkdir(parents=True, exist_ok=True)
            result_path.write_text(json.dumps({
                "result": result, "action_run_id": action_run_id,
                "native_result": native if step_id == "CA-O-143" else {"operation": "Rename"},
            }, sort_keys=True), encoding="utf-8")
            retained.append({
                "workflow_run_id": workflow_run_id, "workflow_definition_id": "CA-O-015",
                "step_definition_id": step_id, "action_definition_id": action_id,
                "action_run_id": action_run_id, "result": result, "result_ref": path,
                "completed_receipt": {
                    "run_id": action_run_id, "disposition": "terminal", "outcome": "completed",
                    "result_ref": path, "effect_refs": effects if step_id == "CA-O-143" else [],
                },
                "native_result": native if step_id == "CA-O-143" else {"operation": "Rename"},
            })
        return {"structural_prior_results": retained}

    def test_create_reports_inherited_mode_and_missing_goal_gap_without_inventing_goal(self) -> None:
        result = project_structure.create_scope_unit(
            self.root,
            self.parameters(
                "Create",
                declaration=declaration("CHILD", parent="PARENT", unit_type="Ordered", level=2, local_order=1),
                goal_coverage_disposition={
                    "state": "missing",
                    "parent": "PARENT",
                    "gap_ref": "GOAL-GAP-1",
                    "authorized_disposition": "report-only",
                },
            ),
        )
        self.assertEqual("completed", result["state"])
        self.assertEqual("casual", result["resulting_scope_unit"]["effective_authority_mode"])
        self.assertEqual("missing", result["goal_coverage_disposition"]["state"])
        self.assertFalse((self.root / "delivery" / "CHILD").exists())
        self.assertIn("CHILD", self.toml.read_text(encoding="utf-8"))

    def test_rename_move_repair_only_exact_listed_references(self) -> None:
        self.assertEqual(
            "completed",
            project_structure.create_scope_unit(
                self.root,
                self.parameters("Create", declaration=declaration("CHILD", parent="PARENT", level=2)),
            )["state"],
        )
        self.reference.write_text("CHILD\n", encoding="utf-8")
        renamed = project_structure.rename_scope_unit(
            self.root,
            self.parameters(
                "Rename",
                target_name="CHILD",
                declaration=declaration("RENAMED", parent="PARENT", level=2),
                reference_frontier=[{
                    "path": "references.md", "expected_sha256": digest(self.reference),
                    "replacements": [{"old": "CHILD", "new": "RENAMED"}],
                }],
            ),
        )
        self.assertEqual("completed", renamed["state"])
        moved = project_structure.move_scope_unit(
            self.root,
            self.parameters(
                "Move",
                target_name="RENAMED",
                declaration=declaration("RENAMED", parent="PROJECT", level=1),
                goal_coverage_disposition={"state": "present", "parent": "PROJECT"},
                reference_frontier=[{
                    "path": "references.md", "expected_sha256": digest(self.reference),
                    "replacements": [{"old": "RENAMED", "new": "ROOT"}],
                }],
            ),
        )
        self.assertEqual("completed", moved["state"])
        self.assertEqual("ROOT\n", self.reference.read_text(encoding="utf-8"))
        self.assertEqual("PROJECT", moved["resulting_scope_unit"]["parent"])

    def test_rejects_invalid_tree_and_stale_without_mutation(self) -> None:
        before = self.toml.read_bytes()
        conflict = project_structure.create_scope_unit(
            self.root,
            self.parameters("Create", declaration=declaration("BAD", parent="PARENT", level=9)),
        )
        self.assertEqual("conflict", conflict["state"])
        self.assertEqual(before, self.toml.read_bytes())
        stale = project_structure.create_scope_unit(
            self.root,
            self.parameters("Create", expected_toml_revision="0" * 64, declaration=declaration("STALE")),
        )
        self.assertEqual("stale", stale["state"])
        self.assertEqual(before, self.toml.read_bytes())

    def test_remove_preserves_observed_carrier_and_no_op_is_truthful(self) -> None:
        result = project_structure.remove_scope_unit(
            self.root,
            self.parameters("Remove", target_name="PARENT", reference_frontier=[]),
        )
        self.assertEqual("completed", result["state"])
        self.assertTrue(self.carrier.is_file())
        repeat = project_structure.remove_scope_unit(
            self.root,
            self.parameters("Remove", target_name="PARENT", reference_frontier=[]),
        )
        self.assertEqual("no_op", repeat["state"])
        self.assertEqual([], repeat["actual_effects"])

    def test_partial_cutover_returns_exact_rollback_boundary(self) -> None:
        parameters = self.parameters("Create", declaration=declaration("CHILD", parent="PARENT", level=2))

        def fail_after_declaration() -> None:
            raise OSError("injected reference write failure")

        partial = project_structure.apply_scope_unit_action(
            self.root, parameters, after_declaration=fail_after_declaration
        )
        self.assertEqual("partial", partial["state"])
        self.assertIn("toml", partial["recovery_boundary"])
        rolled_back = project_structure.rollback_scope_unit_change(self.root, partial["recovery_boundary"])
        self.assertEqual("rolled_back", rolled_back["state"])
        self.assertNotIn("CHILD", self.toml.read_text(encoding="utf-8"))

    def test_unordered_order_and_unsafe_reference_path_are_rejected(self) -> None:
        before = self.toml.read_bytes()
        bad_order = project_structure.create_scope_unit(
            self.root,
            self.parameters("Create", declaration=declaration("BAD", local_order=1)),
        )
        self.assertEqual("conflict", bad_order["state"])
        unsafe_ref = project_structure.create_scope_unit(
            self.root,
            self.parameters(
                "Create", declaration=declaration("SAFE"),
                reference_frontier=[{"path": "../escape", "expected_sha256": "0" * 64, "replacements": []}],
            ),
        )
        self.assertEqual("conflict", unsafe_ref["state"])
        self.assertEqual(before, self.toml.read_bytes())

    def test_create_no_op_requires_the_authorized_declaration_already_match(self) -> None:
        different = declaration("PARENT", unit_type="Ordered", label="FEATURE", local_order=1)
        result = project_structure.create_scope_unit(
            self.root, self.parameters("Create", declaration=different)
        )
        self.assertEqual("conflict", result["state"])
        self.assertIn("different declaration", result["validation_errors"][0])

    def test_queue_handlers_are_o015_scoped_and_apply_only_after_shared_admission(self) -> None:
        handlers = project_structure.queue_action_handlers(self.root)
        parameters = self.parameters(
            "Create", declaration=declaration("CHILD", parent="PARENT", level=2)
        )
        compiler_context = {
            "workflow_definition_id": "CA-O-011",
            "route": "create_scope_unit",
            "parameters": parameters,
        }
        self.assertEqual("blocked", handlers["CA-O-004"](compiler_context)["result"])
        context = {**compiler_context, "workflow_definition_id": "CA-O-015"}
        self.assertEqual("selected", handlers["CA-O-004"](context)["result"])
        self.assertEqual("prepared", handlers["CA-O-012"](context)["result"])
        self.assertEqual("accepted", handlers["CA-O-005"](context)["result"])
        self.assertEqual("blocked", handlers["CA-O-014"](context)["result"])
        self.assertNotIn("CHILD", self.toml.read_text(encoding="utf-8"))
        applied = handlers["CA-O-014"]({**context, "sealed_outer_admission": True})
        self.assertEqual("completed", applied["result"])
        self.assertIn("CHILD", self.toml.read_text(encoding="utf-8"))

    def test_queue_reassesses_only_the_exact_post_cutover_structure_result(self) -> None:
        """O144 accepts its own observed structural effect, never an arbitrary drift."""
        handlers = project_structure.queue_action_handlers(self.root)

        def apply_and_assess(route: str, parameters: dict[str, object]) -> dict[str, object]:
            context: dict[str, object] = {
                "workflow_definition_id": "CA-O-015", "route": route,
                "parameters": parameters, "sealed_outer_admission": True,
                "workflow_run_id": "structural-queue-test", "action_run_id": f"{route}:o143",
            }
            self.assertEqual("accepted", handlers["CA-O-005"](context)["result"])
            applied = handlers["CA-O-014"](context)
            self.assertEqual("completed", applied["result"])
            return handlers["CA-O-005"]({
                **context, **self.completed_o143_handoff(context, applied),
                "step_definition_id": "CA-O-144", "action_run_id": f"{route}:o144",
            })

        created = apply_and_assess(
            "create_scope_unit",
            self.parameters("Create", declaration=declaration("CHILD", parent="PARENT", level=2)),
        )
        self.assertEqual("accepted", created["result"])
        moved = apply_and_assess(
            "move_scope_unit",
            self.parameters(
                "Move", target_name="CHILD", declaration=declaration("CHILD", parent="PROJECT", level=1),
                goal_coverage_disposition={"state": "present", "parent": "PROJECT"},
            ),
        )
        self.assertEqual("accepted", moved["result"])
        removed = apply_and_assess("remove_scope_unit", self.parameters("Remove", target_name="CHILD"))
        self.assertEqual("accepted", removed["result"])

    def test_rename_frontier_stays_literal_and_binds_completed_post_image(self) -> None:
        """O144 accepts only the exact retained O143 result, never a claimed post-image."""
        handlers = project_structure.queue_action_handlers(self.root)
        self.assertEqual(
            "completed",
            project_structure.create_scope_unit(
                self.root, self.parameters("Create", declaration=declaration("CHILD", parent="PARENT", level=2)),
            )["state"],
        )
        self.reference.write_text("CHILD\n", encoding="utf-8")
        parameters = self.parameters(
            "Rename", target_name="CHILD", declaration=declaration("RENAMED", parent="PARENT", level=2),
            reference_frontier=[{
                "path": "references.md", "expected_sha256": digest(self.reference),
                "replacements": [{"old": "CHILD", "new": "RENAMED"}],
            }],
        )
        original = copy.deepcopy(parameters)
        context: dict[str, object] = {
            "workflow_definition_id": "CA-O-015", "route": "rename_scope_unit",
            "parameters": parameters, "sealed_outer_admission": True,
            "workflow_run_id": "rename-queue-test", "action_run_id": "rename:o143",
        }
        self.assertEqual("selected", handlers["CA-O-004"](context)["result"])
        self.assertEqual(original, parameters)
        applied = handlers["CA-O-014"](context)
        self.assertEqual("completed", applied["result"])
        self.assertEqual([".caprmedio_caprmedio/project_structure.toml", "references.md"], applied["effect_refs"])
        self.assertEqual("RENAMED\n", self.reference.read_text(encoding="utf-8"))
        self.assertEqual(original, parameters)
        final_context = {**context, "step_definition_id": "CA-O-144", "action_run_id": "rename:o144"}
        missing = handlers["CA-O-005"](final_context)
        self.assertEqual("blocked", missing["result"])
        handoff = self.completed_o143_handoff(context, applied)
        unsafe = copy.deepcopy(handoff)
        unsafe["structural_prior_results"][-1]["result_ref"] = "../unsafe-result.json"
        unsafe["structural_prior_results"][-1]["completed_receipt"]["result_ref"] = "../unsafe-result.json"
        self.assertEqual("blocked", handlers["CA-O-005"]({**final_context, **unsafe})["result"])
        final = handlers["CA-O-005"]({**final_context, **handoff})
        self.assertEqual("accepted", final["result"])
        self.reference.write_text("tampered\n", encoding="utf-8")
        mismatch = handlers["CA-O-005"]({**final_context, **handoff})
        self.assertEqual("blocked", mismatch["result"])


class ProjectStructureSharedServiceIntegration(unittest.TestCase):
    """CA-D-527 integration: the service admits, this route performs effects."""

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[authority_modes]\ndefault = 'casual'\n\n"
            "[paths]\ncontrol_root = '.caprmedio_caprmedio'\njournal_root = '.caprmedio_caprmedio/_journal'\n"
            "runtime_root = '.caprmedio_runtime'\n",
            encoding="utf-8",
        )
        self.toml = control / "project_structure.toml"
        self.toml.write_text(
            project_structure.serialize_project_structure([
                declaration("PARENT", unit_type="Ordered", label="LAYER", local_order=1)
            ]),
            encoding="utf-8",
        )
        (self.root / "observed-carrier.md").write_text("retain", encoding="utf-8")
        self.executions: list[dict[str, object]] = []
        self.tracker = RunTracker(
            self.root,
            source_observer=self._observe,
            executor=self._execute,
            journal_context={"author": "project-structure-test", "timezone": "UTC"},
        )

    def _parameters(self, operation: str, **overrides: object) -> dict[str, object]:
        values: dict[str, object] = {
            "operation": operation,
            "expected_toml_revision": digest(self.toml),
            "reference_frontier": [],
            "goal_coverage_disposition": {"state": "present", "parent": "PARENT"},
            "preservation_disposition": {"preserved": ["observed-carrier.md"]},
            "recovery_disposition": {"authorized": True, "boundary": "toml-and-listed-references"},
        }
        values.update(overrides)
        return values

    @staticmethod
    def _digest(value: object) -> str:
        return canonical_json_digest(value)

    def _request(self, request_id: str, route: str, parameters: dict[str, object]) -> dict[str, object]:
        frontier = [".caprmedio_caprmedio/project_structure.toml", "observed-carrier.md"]
        effects = [{"type": "project_structure", "target": ".caprmedio_caprmedio/project_structure.toml"}]
        manifest = {"manifest_ref": "selected/project_structure.manifest.json", "manifest_digest": "a" * 64}
        return {
            "request_id": request_id,
            "operation_route": route,
            "parameters": parameters,
            "parameters_digest": self._digest(parameters),
            "target_frontier": frontier,
            "target_frontier_digest": self._digest(frontier),
            "effects": effects,
            "effects_digest": self._digest(effects),
            "definition_manifest": manifest,
            "source_freshness": {
                "selected_source_registry_ref": "selected/registry.json",
                "selected_source_registry_version": 1,
                "selected_source_registry_digest": "b" * 64,
                "selected_binding_ref": "selected/project_structure.json",
                "selected_binding_digest": "c" * 64,
            },
            "initiative": {
                "initiative_id": f"initiative-{request_id}",
                "instruction_summary": "one authorized structural change",
                "initiative_ref": "03_plan/CA-P-1512.md",
            },
            "requested_runs": [{
                "requested_run_id": "project-structure-apply",
                "kind": "action",
                "definition": {
                    "atom_id": "CA-O-014",
                    "version": 5,
                    "path": "operations/CA-O-014.md",
                    "digest": "d" * 64,
                },
            }],
        }

    def _observe(self, request: dict[str, object]) -> dict[str, object]:
        parameters = request["parameters"]
        return {
            "selected": request["operation_route"] in {
                "create_scope_unit", "rename_scope_unit", "move_scope_unit", "remove_scope_unit"
            },
            "current": isinstance(parameters, dict)
            and parameters.get("expected_toml_revision") == digest(self.toml),
            "observed": {
                "toml_revision": digest(self.toml),
                "definition_manifest": request["definition_manifest"],
            },
        }

    def _execute(self, request: dict[str, object], session: object) -> None:
        actual = session.start_run("project-structure-apply", run_id=f"actual-{request['request_id']}")
        adapters = {
            "create_scope_unit": project_structure.create_scope_unit,
            "rename_scope_unit": project_structure.rename_scope_unit,
            "move_scope_unit": project_structure.move_scope_unit,
            "remove_scope_unit": project_structure.remove_scope_unit,
        }
        structural = adapters[request["operation_route"]](self.root, request["parameters"])
        self.executions.append(structural)
        result_path = self.root / "results" / f"{request['request_id']}.json"
        result_path.parent.mkdir(parents=True, exist_ok=True)
        result_path.write_text(json.dumps(structural, sort_keys=True), encoding="utf-8")
        effects = [effect["path"] for effect in structural["actual_effects"]]
        outcome = "completed" if structural["state"] == "completed" else (
            "no_op" if structural["state"] == "no_op" else "failed"
        )
        session.finish_run(
            actual["run_id"],
            outcome=outcome,
            result_ref=result_path.relative_to(self.root).as_posix(),
            effect_refs=effects,
        )

    def _authorization(self, request: dict[str, object], preview: dict[str, object]) -> dict[str, object]:
        return {
            "authorization_ref": "authorizations/project-structure.json",
            "authorization_freshness": {"state": "current", "digest": "e" * 64},
            "request_id": request["request_id"],
            "operation_route": request["operation_route"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "parameters_digest": request["parameters_digest"],
            "target_frontier_digest": request["target_frontier_digest"],
            "effects_digest": request["effects_digest"],
            "definition_manifest": request["definition_manifest"],
            "source_freshness": request["source_freshness"],
        }

    def _execute_request(self, request: dict[str, object]) -> tuple[dict[str, object], dict[str, object]]:
        preview = self.tracker.run_selected_operation(request)
        self.assertEqual("preview", preview["disposition"])
        executed = self.tracker.run_selected_operation({
            **request,
            "mode": "execute",
            "proposal_receipt": preview["proposal_receipt"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "assigned_action_id": "CA-O-014",
            "operator_authorization": self._authorization(request, preview),
        })
        return preview, executed

    def test_preview_execute_mutates_after_admission_and_records_canonical_journal(self) -> None:
        request = self._request(
            "structure-create-gap",
            "create_scope_unit",
            self._parameters(
                "Create",
                declaration=declaration("CHILD", parent="PARENT", level=2),
                goal_coverage_disposition={
                    "state": "missing", "parent": "PARENT", "gap_ref": "GOAL-GAP-1",
                    "authorized_disposition": "report-only",
                },
            ),
        )
        preview = self.tracker.run_selected_operation(request)
        self.assertEqual("preview", preview["disposition"])
        self.assertNotIn("CHILD", self.toml.read_text(encoding="utf-8"))
        self.assertFalse((self.root / ".caprmedio_caprmedio" / "_journal").exists())

        result = self.tracker.run_selected_operation({
            **request,
            "mode": "execute",
            "proposal_receipt": preview["proposal_receipt"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "assigned_action_id": "CA-O-014",
            "operator_authorization": self._authorization(request, preview),
        })
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual("completed", result["terminal_runs"][0]["outcome"])
        self.assertEqual("actual-structure-create-gap", result["run_ids"][0])
        self.assertEqual("completed", self.executions[-1]["state"])
        self.assertEqual("missing", self.executions[-1]["goal_coverage_disposition"]["state"])
        self.assertIn("CHILD", self.toml.read_text(encoding="utf-8"))
        self.assertFalse((self.root / "delivery" / "CHILD").exists())
        journal = next((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))
        events = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(["started", "completed"], [event["event"] for event in events])
        self.assertTrue(all(event["schema_version"] == 5 for event in events))
        self.assertTrue(all(event["run"]["run_id"] == "actual-structure-create-gap" for event in events))

    def test_shared_no_op_and_declared_remove_refusal_are_truthful(self) -> None:
        create = self._request(
            "structure-create-child", "create_scope_unit",
            self._parameters("Create", declaration=declaration("CHILD", parent="PARENT", level=2)),
        )
        self._execute_request(create)
        no_op = self._request(
            "structure-create-no-op", "create_scope_unit",
            self._parameters("Create", declaration=declaration("CHILD", parent="PARENT", level=2)),
        )
        _, no_op_result = self._execute_request(no_op)
        self.assertEqual("terminal", no_op_result["disposition"])
        self.assertEqual("no_op", no_op_result["terminal_runs"][0]["outcome"])
        self.assertEqual([], self.executions[-1]["actual_effects"])

        remove = self._request(
            "structure-remove-parent", "remove_scope_unit",
            self._parameters("Remove", target_name="PARENT"),
        )
        _, refusal = self._execute_request(remove)
        self.assertEqual("terminal", refusal["disposition"])
        self.assertEqual("failed", refusal["terminal_runs"][0]["outcome"])
        self.assertEqual("conflict", self.executions[-1]["state"])
        self.assertIn("PARENT", self.toml.read_text(encoding="utf-8"))
        self.assertIn("CHILD", self.toml.read_text(encoding="utf-8"))
        self.assertEqual("retain", (self.root / "observed-carrier.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
