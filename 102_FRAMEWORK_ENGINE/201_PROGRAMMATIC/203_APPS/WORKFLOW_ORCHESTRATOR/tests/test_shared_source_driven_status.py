"""Current-source selected status proof; development-only, not live MCP/image proof.

The canonical first-fifteen-route portfolio is copied unchanged. A stale
production pin is a real failing gate, never replaced by a fixture-only rehash
or a skipped positive case. Release is intentionally outside this historical
fixture baseline and has separate proof.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import re
import sys
import unittest


APP = Path(__file__).resolve().parents[1]
REPOSITORY = APP.parents[3]
TOOLS = APP.parents[1] / "201_TOOLS"
MCP = APP.parents[1] / "204_MCP"
for location in (TOOLS / "tests", TOOLS, MCP, APP, Path(__file__).resolve().parent):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

# Explicit reuse of the real eight-role source-copy fixture, not its TestCase
# inheritance (which would silently rediscover the separate native suite).
import test_model_driven_status_lifecycle as native_goldens  # noqa: E402
from selected_execution import SelectedExecution, SelectedExecutionError  # noqa: E402
from selected_routes import SelectedRouteAdapter, SelectedRouteError  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject, digest  # noqa: E402


ROUTE = "change_atom_status"


class _StatusProject(GoldenProject):
    """Replace only fixture input construction, never source admission/handlers."""

    selected_parameters: dict[str, object]

    def native_parameters(self) -> dict[str, object]:
        return copy.deepcopy(self.selected_parameters)


class SharedSourceDrivenStatusTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        native_goldens.ModelDrivenStatusLifecycleTest.setUpClass()

    def setUp(self) -> None:
        self.fixture = native_goldens.ModelDrivenStatusLifecycleTest()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.journal = self.root / native_goldens.CONTROL / "_journal"
        self.journal.mkdir()
        # The Journal stages atomic appends here, then removes their files.
        # Materialize only its known empty staging directories before snapshots;
        # any leftover staging file is still an unexpected authority mutation.
        (self.root / ".caprmedio_tmp/work_journal/atomic").mkdir(parents=True)
        self.admitted_run_roots: set[Path] = set()
        self.project = _StatusProject(REPOSITORY, self.root, GoldenCase("W04", ROUTE))

    def prepare_route(self) -> None:
        # This strict existing helper copies the actual canonical portfolio and
        # every declared source pin. It intentionally fails on pending rebinds.
        self.project.manifest = self.project._copy_reviewed_manifest()

    def authority_snapshot(self) -> dict[str, str | None]:
        allowed_evidence = {self.journal.relative_to(self.root),
                            Path(".caprmedio_runtime/state/work_journal"),
                            *self.admitted_run_roots}
        snapshot = {}
        for relative, value in self.fixture.snapshot().items():
            path = Path(relative)
            if any(path == evidence or evidence in path.parents for evidence in allowed_evidence):
                continue
            if value is None and any(path in evidence.parents for evidence in allowed_evidence):
                continue  # Only directory ancestors of actual Run/Journal evidence.
            snapshot[relative] = value
        return snapshot

    def events(self, request_id: str | None = None) -> list[dict[str, object]]:
        records = [json.loads(line) for path in sorted(self.journal.glob("*.ndjson"))
                   for line in path.read_text(encoding="utf-8").splitlines() if line]
        return [record for record in records if request_id is None
                or record.get("llm_session", {}).get("uuid") == request_id]

    def request(self, path: Path, status: str, request_id: str, *, mode: str = "preview",
                preview: dict[str, object] | None = None) -> dict[str, object]:
        self.project.selected_parameters = self.fixture.request(path, status)
        self.assertEqual({"target", "status"}, set(self.project.selected_parameters))
        return self.project.request(request_id=request_id, mode=mode,
                                    receipt=preview["proposal_receipt"] if preview else None,
                                    receipt_digest=preview["proposal_receipt_digest"] if preview else None)

    def preview(self, path: Path, status: str, request_id: str) -> dict[str, object]:
        before = self.fixture.snapshot()
        result = SelectedRouteAdapter(self.root).invoke(ROUTE, self.request(path, status, request_id))
        self.assertEqual("preview", result.get("disposition"), result)
        self.assertEqual(before, self.fixture.snapshot(), "preview mutated the disposable Project")
        self.assertEqual([], self.events(request_id), "preview invented Run Journal facts")
        admission = result["proposal_receipt"]["source_freshness"]["observed"]["lifecycle_admission"]
        model = native_goldens.resolve_status_model(self.root, native_goldens.atom_from_path(self.root, path), status)
        self.assertEqual(model, admission["status_model"], "preview did not seal actual model source/revision pins")
        return result

    def freeze(self, path: Path, status: str, request_id: str,
               preview: dict[str, object]) -> tuple[SelectedExecution, dict[str, object]]:
        runner = SelectedExecution(self.root)
        execution = self.request(path, status, request_id, mode="execute", preview=preview)
        frozen = runner.freeze({"operation": "enqueue_selected", "run_id": request_id,
                                "execution": execution})
        self.assertEqual(preview["proposal_receipt"]["source_freshness"]["observed"]["lifecycle_admission"],
                         frozen["lifecycle_admission"])
        self.admitted_run_roots.add(runner.run_directory(request_id).relative_to(self.root))
        return runner, frozen

    def complete(self, path: Path, status: str, request_id: str) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
        preview = self.preview(path, status, request_id)
        runner, frozen = self.freeze(path, status, request_id, preview)
        result = runner.dispatch(frozen)
        self.assertEqual("terminal", result.get("disposition"), result)
        graph_path = runner.run_directory(request_id) / "graph_result.json"
        self.assertTrue(graph_path.is_file(), result)
        graph = json.loads(graph_path.read_text(encoding="utf-8"))
        self.assertEqual(1, len(graph["step_results"]), graph)
        action_row = graph["step_results"][0]
        progress = json.loads((runner.run_directory(request_id) / f"{action_row['action_run_id']}.json").read_text())
        self.assert_shared_lineage(request_id, result, graph)
        return result, graph, progress

    def assert_shared_lineage(self, request_id: str, result: dict[str, object], graph: dict[str, object]) -> None:
        route = next(row for row in self.project.manifest["routes"] if row["route"] == ROUTE)
        action = graph["step_results"][0]
        binding = next(row for row in route["ordered_steps"]
                       if row["step"]["atom_id"] == action["step_definition_id"])
        self.assertEqual(binding["action"]["atom_id"], action["action_definition_id"])
        expected = {request_id: (route["workflow"], None),
                    action["step_run_id"]: (binding["step"], request_id),
                    action["action_run_id"]: (binding["action"], action["step_run_id"])}
        self.assertEqual(3, len(expected), "one Workflow/Step/Action lineage is required")
        self.assertEqual(set(expected), set(result["run_ids"]), result)
        terminals = {row["run_id"]: row for row in result["terminal_runs"]}
        self.assertEqual(set(expected), set(terminals), result)
        facts = self.events(request_id)
        self.assertEqual(6, len(facts), facts)
        self.assertEqual(6, len({row["event_id"] for row in facts}), facts)
        self.assertEqual(set(expected), {row["run"]["run_id"] for row in facts}, facts)
        for run_id, (pin, parent) in expected.items():
            expected_definition = {"atom_id": pin["atom_id"], "version": pin["version"],
                                   "path": pin["source_path"], "digest": pin["digest"]}
            terminal = terminals[run_id]
            self.assertEqual("terminal", terminal["disposition"], terminal)
            self.assertTrue((self.root / terminal["result_ref"]).is_file(), terminal)
            rows = [row for row in facts if row["run"]["run_id"] == run_id]
            self.assertEqual(["started", "completed"], [row["event"] for row in rows], rows)
            self.assertEqual(terminal["outcome"], rows[-1]["outcome"], rows)
            self.assertEqual(terminal["effect_refs"], rows[-1]["effect_refs"], rows)
            for row in rows:
                self.assertEqual(expected_definition, row["run"]["definition"], row)
                if parent is None:
                    self.assertNotIn("parent_run_id", row["run"], row)
                else:
                    self.assertEqual(parent, row["run"].get("parent_run_id"), row)

    def assert_refusal(self, invoke: object, diagnostic: str) -> None:
        try:
            result = invoke()
        except (SelectedExecutionError, SelectedRouteError) as error:
            if getattr(error, "code", None) is not None:
                self.assertEqual(diagnostic, error.code, error)
            else:
                self.assertIn(diagnostic, str(error), error)
        else:
            self.assertIsInstance(result, dict, "expected a typed refusal, not accepted/frozen execution")
            self.assertIn(result.get("disposition"), {"blocked", "declined", "rejected"}, result)
            self.assertIn(diagnostic, json.dumps(result), result)
            self.assertEqual([], result.get("effect_refs", []), result)

    def test_canonical_current_manifest_is_an_unsubstituted_source_gate(self) -> None:
        self.prepare_route()
        SelectedRouteAdapter(self.root)
        current = json.loads((REPOSITORY / self.project.manifest_path.relative_to(self.root)).read_text())
        fixture = json.loads(self.project.manifest_path.read_text())
        current_routes = current["routes"]
        self.assertEqual(
            ["create_atom", "update_atom", "replace_atom", "change_atom_status", "create_scope_unit",
             "rename_scope_unit", "move_scope_unit", "remove_scope_unit", "run_implementation_workflow",
             "revert_changes", "build_entities_graph", "build_terms_graph", "build_applicable_methodology",
             "find_and_fetch_artifacts", "find_and_fetch_journal_events", "release_version"],
            [row["route"] for row in current_routes],
        )
        self.assertEqual(current_routes[:15], fixture["routes"])
        self.assertEqual(current["query_source_admissions"], fixture["query_source_admissions"])
        self.assertNotIn("release_source_admissions", fixture)
        self.assertNotIn("release_version", [row["route"] for row in fixture["routes"]])
        self.assertEqual(
            {key: value for key, value in current["source_freshness"].items()
             if key != "selected_binding_digest"},
            {key: value for key, value in fixture["source_freshness"].items()
             if key != "selected_binding_digest"},
        )
        self.assertEqual(digest(fixture["routes"]), fixture["source_freshness"]["selected_binding_digest"])
        self.assertEqual(
            digest({key: value for key, value in fixture.items() if key != "canonical_manifest_sha256"}),
            fixture["canonical_manifest_sha256"],
        )
        self.assertEqual([], self.events())

    def test_actual_selected_definition_change_refuses_without_preview_or_run(self) -> None:
        self.prepare_route()
        route = next(row for row in self.project.manifest["routes"] if row["route"] == ROUTE)
        source = self.root / route["workflow"]["source_path"]
        source.write_bytes(source.read_bytes() + b"\nDeliberately stale selected definition.\n")
        before = self.fixture.snapshot()
        with self.assertRaisesRegex(SelectedRouteError, "source pin is stale"):
            SelectedRouteAdapter(self.root)
        self.assertEqual(before, self.fixture.snapshot())
        self.assertEqual([], self.events())

    def test_all_eight_real_role_noops_have_empty_changed_refs_and_single_lineage(self) -> None:
        self.prepare_route()
        for role, _, _, source_id, _ in native_goldens.DOMAINS:
            with self.subTest(role=role):
                status = "active" if role == "Concern" else "Done" if role in {"Plan", "Analysis"} else "Active"
                path = self.fixture.atom(role, status)
                before = self.authority_snapshot()
                result, graph, progress = self.complete(path, status, f"shared-status-noop-{role.lower()}")
                self.assertEqual("no-op", progress["result"], progress)
                native = progress["native_result"]
                self.assertEqual("no-op", native["outcome"], native)
                self.assertEqual(source_id, native["status_model"]["model_sources"][0]["atom_id"])
                self.assertEqual(hashlib.sha256(self.fixture.sources[source_id].read_bytes()).hexdigest(),
                                 native["status_model"]["model_sources"][0]["sha256"])
                self.assertEqual(before, self.authority_snapshot(), "no-op changed authority/history/Projection")
                self.assertEqual([], graph["step_results"][0]["effect_refs"])
                for terminal in result["terminal_runs"]:
                    self.assertEqual([], terminal["effect_refs"], terminal)
                action_id = graph["step_results"][0]["action_run_id"]
                self.assertEqual("no_op", next(row["outcome"] for row in result["terminal_runs"] if row["run_id"] == action_id))

    def test_identified_to_draft_removes_assignment_and_retains_actual_history_lineage(self) -> None:
        self.prepare_route()
        path = self.fixture.atom("Requirement", "Active")
        before = native_goldens.atom_from_path(self.root, path)
        before_raw = path.read_bytes()
        legacy = path.parent / "archive" / f"{path.stem}@2.md"
        legacy.parent.mkdir()
        legacy.write_bytes(b"immutable old identified revision")
        legacy_raw = legacy.read_bytes()
        result, graph, progress = self.complete(path, "Draft", "shared-status-demote-draft")
        native = progress["native_result"]
        self.assertEqual("applied", native["outcome"], native)
        destination = self.root / native["observed"]["path"]
        self.assertFalse(path.exists())
        self.assertEqual("CA-R--golden.md", destination.name)
        self.assertIsNone(native["observed"]["atom_id"])
        after = native_goldens.atom_from_path(self.root, destination)
        self.assertEqual(before.content, after.content)
        self.assertIsNone(native_goldens.frontmatter_scalar(after.frontmatter, "atom_id"))
        self.assertEqual(3, native["observed"]["version"])
        history = native["history"]["prior_revision"]
        self.assertEqual("CA-R-8000", history["atom_id"])
        self.assertEqual(before_raw, (self.root / history["path"]).read_bytes())
        self.assertEqual(legacy_raw, legacy.read_bytes())
        effects = set(graph["step_results"][0]["effect_refs"])
        self.assertTrue({native["observed"]["path"], history["path"]} <= effects,
                        "shared changed-effect evidence omitted a newly preserved history Carrier")
        self.assertTrue(all(row["outcome"] == "completed" for row in result["terminal_runs"]))

    def test_precise_case_and_unavailable_model_preview_refusals_create_no_runs(self) -> None:
        self.prepare_route()
        path = self.fixture.atom("Requirement", "Active")
        for status in ("Reviewed", "active"):
            before = self.fixture.snapshot()
            request = self.request(path, status, f"shared-status-denied-{status.lower()}")
            self.assert_refusal(lambda: SelectedRouteAdapter(self.root).invoke(ROUTE, request), "status-unadmitted")
            self.assertEqual(before, self.fixture.snapshot())
            self.assertEqual([], self.events())
        self.fixture.sources["CA-R-1309"].unlink()
        before = self.fixture.snapshot()
        request = self.request(path, "Archived", "shared-status-missing-model")
        self.assert_refusal(lambda: SelectedRouteAdapter(self.root).invoke(ROUTE, request), "model-missing")
        self.assertEqual(before, self.fixture.snapshot())
        self.assertEqual([], self.events())

    def test_model_source_changed_after_preview_is_rejected_before_freeze_write(self) -> None:
        self.prepare_route()
        path = self.fixture.atom("Requirement", "Active")
        request_id = "shared-status-stale-preview"
        preview = self.preview(path, "Archived", request_id)
        source = self.fixture.sources["CA-R-1309"]
        source.write_bytes(source.read_bytes() + b"\nChanged after preview.\n")
        before = self.fixture.snapshot()
        self.assert_refusal(lambda: self.freeze(path, "Archived", request_id, preview), "status-model-stale")
        self.assertEqual(before, self.fixture.snapshot(), "refused freeze wrote admission/effect evidence")
        self.assertEqual([], self.events())

    def test_ambiguous_and_invalid_actual_model_sources_refuse_before_preview_or_run(self) -> None:
        self.prepare_route()
        path = self.fixture.atom("Requirement", "Active")
        source = self.fixture.sources["CA-R-1309"]
        original = source.read_text(encoding="utf-8")
        duplicate = source.with_name("CA-R-1309--deliberately-ambiguous-fixture.md")
        duplicate.write_text(original, encoding="utf-8")
        before = self.fixture.snapshot()
        request = self.request(path, "Archived", "shared-status-ambiguous-model")
        self.assert_refusal(lambda: SelectedRouteAdapter(self.root).invoke(ROUTE, request), "model-ambiguous")
        self.assertEqual(before, self.fixture.snapshot())
        self.assertEqual([], self.events())
        duplicate.unlink()
        source.write_text(re.sub(r"(?m)^version:.*$", "version: invalid", original, count=1), encoding="utf-8")
        before = self.fixture.snapshot()
        request = self.request(path, "Archived", "shared-status-invalid-model")
        self.assert_refusal(lambda: SelectedRouteAdapter(self.root).invoke(ROUTE, request), "source-invalid")
        self.assertEqual(before, self.fixture.snapshot())
        self.assertEqual([], self.events())

    def test_model_source_changed_after_freeze_is_rejected_before_run_start_or_effect(self) -> None:
        self.prepare_route()
        path = self.fixture.atom("Requirement", "Active")
        request_id = "shared-status-stale-admission"
        preview = self.preview(path, "Archived", request_id)
        runner, frozen = self.freeze(path, "Archived", request_id, preview)
        source = self.fixture.sources["CA-R-1309"]
        source.write_bytes(source.read_bytes() + b"\nChanged after admission.\n")
        before = self.authority_snapshot()
        self.assert_refusal(lambda: runner.dispatch(frozen), "status-model-stale")
        self.assertEqual(before, self.authority_snapshot())
        self.assertEqual([], self.events(), "invalidated admission started a Run")


if __name__ == "__main__":
    unittest.main()
