"""CA-E-555 through CA-E-558 functional tests for selected graph builds."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
SCRIPT = Path(__file__).resolve().parents[1] / "generate_entity_graph.py"
SPEC = importlib.util.spec_from_file_location("selected_graphs_generator", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
graph = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = graph
SPEC.loader.exec_module(graph)


def atom(
    atom_id: str,
    *,
    cce_form: str,
    governs: str,
    depends_on: tuple[str, ...] = (),
    claim: str = "claim.",
) -> str:
    dependencies = "".join(f"      - {json.dumps(value)}\n" for value in depends_on)
    if not dependencies:
        dependencies = "    continuant: []\n"
    else:
        dependencies = f"    continuant:\n{dependencies}"
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        f"cce_form: {cce_form}\n"
        "subjects:\n"
        "  governs:\n"
        "    continuant:\n"
        f"      - {json.dumps(governs)}\n"
        f"  depends_on:\n{dependencies}"
        "version: 1\n"
        "updated_at: 2026-10-04 00:00:00 +0000\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\n{claim}\n"
    )


def current_atom(
    atom_id: str,
    *,
    governs: str | tuple[str, ...],
    depends_on: tuple[str, ...] = (),
    atom_type: str = "Definition",
    status: str = "Active",
    claim: str = "claim.",
) -> str:
    """A current source carrier: scalar/list Subjects and no retired CCE fields."""

    dependencies = ", ".join(json.dumps(value) for value in depends_on)
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "content_role: Requirement\n"
        f"type: {atom_type}\n"
        "current_scope_unit: TOOLS\n"
        "claim_target_scope_unit: TOOLS\n"
        f"status: {status}\n"
        "author: Test Author\n"
        "version: 1\n"
        "updated_at: \"2026-10-04 00:00:00 +0000\"\n"
        "subjects:\n"
        f"  governs: {json.dumps(governs)}\n"
        f"  depends_on: [{dependencies}]\n"
        "relations:\n"
        "  relates_to: []\n"
        "---\n"
        f"# {atom_id}\n\n{claim}\n"
    )


class SelectedGraphTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name) / "repository"
        self.control_root = ".caprmedio_selected_graphs"
        self.projection_root = f"{self.control_root}/_projection"
        self.selected = self.root / "selected"
        self.selected.mkdir(parents=True)
        settings = self.root / self.control_root / "caprmedio_project_settings.toml"
        settings.parent.mkdir(parents=True)
        settings.write_text(
            "[paths]\n"
            f'control_root = "{self.control_root}"\n'
            f'projection_root = "{self.projection_root}"\n',
            encoding="utf-8",
            newline="\n",
        )
        self.write(
            "CA-R-001.md",
            atom("CA-R-001", cce_form="definition", governs="Entity"),
        )
        self.write(
            "CA-R-002.md",
            atom("CA-R-002", cce_form="definition", governs="Property"),
        )
        self.write(
            "CA-R-003.md",
            atom(
                "CA-R-003",
                cce_form="classification",
                governs="Property",
                depends_on=("Entity",),
                claim="Property SUBKIND_OF Entity.",
            ),
        )
        self.write(
            "CA-R-004.md",
            atom("CA-R-004", cce_form="definition", governs="Entity/Property: Label"),
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.selected / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        return path

    def request(self, graph_kind: str, **overrides: object) -> dict[str, object]:
        start_receipt = {
            "event_id": "test-action-start",
            "action_id": "test-action",
            "event_digest": "0" * 64,
            "carrier": ".caprmedio_selected_graphs/_journal/events.ndjson",
            "line": 1,
            "previous_carrier_digest": "0" * 64,
            "appended_carrier_digest": "1" * 64,
        }
        request: dict[str, object] = {
            "graph_kind": graph_kind,
            "source_frontier": graph.source_frontier_for(self.root, self.selected),
            "selection": {"atom_ids": ["CA-R-001", "CA-R-002", "CA-R-003", "CA-R-004"]},
            "representation_configuration": {"format": "canonical-json"},
            "capability_permission_evidence": {"authorized": True},
            "run_recording_context": graph.actual_run_recording_context(
                "test-workflow-run", "test-step-run", "test-action-run", start_receipt,
            ),
        }
        request.update(overrides)
        return request

    def test_caller_supplied_recording_claim_cannot_publish(self) -> None:
        result = graph.build_graph(
            self.root,
            self.request(
                "entities",
                run_recording_context={"state": "confirmed", "receipt_refs": ["forged-receipt"]},
            ),
        )

        self.assertEqual("failed", result["outcome"])
        self.assertEqual("recording-context-untrusted", result["diagnostics"][0]["code"])
        self.assertEqual([], result["output_effects"]["paths"])
        self.assertFalse((self.root / self.projection_root / "entities_graph.json").exists())

    def test_secret_shaped_property_is_rejected_without_value_disclosure(self) -> None:
        secret = "do-not-disclose-graph-secret"
        self.write(
            "CA-R-005.md",
            current_atom("CA-R-005", governs="Protected Entity").replace(
                "version: 1\n", f"api_key: {secret}\nversion: 1\n",
            ),
        )
        result = graph.build_graph(
            self.root,
            self.request(
                "entities",
                selection={"atom_ids": ["CA-R-001", "CA-R-002", "CA-R-003", "CA-R-004", "CA-R-005"]},
            ),
        )

        serialized = json.dumps(result, sort_keys=True)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("secret-shaped-property", result["diagnostics"][0]["code"])
        self.assertNotIn(secret, serialized)
        self.assertFalse((self.root / self.projection_root / "entities_graph.json").exists())

    def test_complete_entities_and_terms_graphs_are_separate_and_traceable(self) -> None:
        entities = graph.build_graph(self.root, self.request("entities"))
        terms = graph.build_graph(self.root, self.request("terms"))

        self.assertEqual("built", entities["outcome"])
        self.assertEqual("built", terms["outcome"])
        self.assertIn("entities_graph", entities)
        self.assertNotIn("terms_graph", entities)
        self.assertIn("terms_graph", terms)
        self.assertNotIn("entities_graph", terms)
        self.assertTrue(entities["non_authoritative"])
        self.assertTrue(terms["non_authoritative"])

        entity_nodes = entities["entities_graph"]["entities"]
        self.assertEqual(["Entity", "Entity/Property: Label", "Property"], [row["identity"] for row in entity_nodes])
        source_atoms = entities["entities_graph"]["source_atoms"]
        self.assertEqual(["CA-R-001", "CA-R-002", "CA-R-003", "CA-R-004"], [row["atom_id"] for row in source_atoms])
        self.assertEqual(1, source_atoms[0]["properties"]["atom_revision"])
        self.assertEqual("selected/CA-R-001.md", source_atoms[0]["source"]["carrier_path"])
        self.assertIn("carrier_sha256", source_atoms[0]["source"])
        self.assertEqual(
            {"GOVERNS", "DEPENDS_ON"},
            {row["relation"] for row in entities["entities_graph"]["relations"]},
        )
        self.assertEqual(
            {"IS_ALLOWED_VALUE_OF", "IS_BORNE_BY"},
            {row["relation"] for row in entities["entities_graph"]["structural_relations"]},
        )

        terms_graph = terms["terms_graph"]
        self.assertEqual(["Entity", "Label", "Property"], [row["identity"] for row in terms_graph["terms"]])
        self.assertEqual(["Entity"], terms_graph["parents_by_term"]["Property"])
        self.assertEqual(["Entity"], terms_graph["ancestors_by_term"]["Property"])
        self.assertEqual(["Entity"], terms_graph["dependencies_by_term"]["Property"])
        self.assertEqual(
            {"DEPENDS_ON", "SUBKIND_OF"},
            {row["relation"] for row in terms_graph["relations"]},
        )
        self.assertEqual([], terms_graph["unresolved_terms"])
        self.assertEqual([], terms_graph["cycles"])

        self.assertEqual(
            entities["source_frontier_evidence"]["source_frontier_sha256"],
            terms["source_frontier_evidence"]["source_frontier_sha256"],
        )
        self.assertEqual("pass", entities["quality_dispositions"]["currentness"])
        self.assertEqual("pass", terms["quality_dispositions"]["validity"])

    def test_current_scalar_and_list_subject_schema_builds_expanded_entities_and_terms(self) -> None:
        self.write(
            "CA-R-101.md",
            current_atom("CA-R-101", governs="Entity", depends_on=("Property",)),
        )
        self.write(
            "CA-R-102.md",
            current_atom("CA-R-102", governs=("Property",)),
        )
        self.write(
            "CA-R-103.md",
            current_atom("CA-R-103", governs="Entity/Property: Label", depends_on=("Property",)),
        )
        selection = {"atom_ids": ["CA-R-101", "CA-R-102", "CA-R-103"]}
        entities = graph.build_graph(self.root, self.request("entities", selection=selection))
        terms = graph.build_graph(self.root, self.request("terms", selection=selection))

        self.assertEqual("built", entities["outcome"])
        self.assertEqual("built", terms["outcome"])
        self.assertEqual(
            ["Entity", "Entity/Property: Label", "Property"],
            [row["identity"] for row in entities["entities_graph"]["entities"]],
        )
        self.assertEqual(
            ["CA-R-101", "CA-R-102", "CA-R-103"],
            [row["atom_id"] for row in entities["entities_graph"]["source_atoms"]],
        )
        self.assertIn(
            "status",
            {row["name"] for row in entities["entities_graph"]["properties"]},
        )
        self.assertEqual(
            {"GOVERNS", "DEPENDS_ON"},
            {row["relation"] for row in entities["entities_graph"]["relations"]},
        )
        self.assertEqual(["Entity", "Label", "Property"], [row["identity"] for row in terms["terms_graph"]["terms"]])
        self.assertEqual(["Property"], terms["terms_graph"]["dependencies_by_term"]["Entity"])

    def test_current_status_excludes_non_active_carriers_without_dropping_active_frontier(self) -> None:
        self.write("CA-R-110.md", current_atom("CA-R-110", governs="Active Entity"))
        self.write(
            "CA-R-111.md",
            current_atom("CA-R-111", governs="Retired Entity", status="Done"),
        )
        frontier = graph.source_frontier_for(self.root, self.selected)
        frontier_ids = [row["atom_id"] for row in frontier["carriers"]]
        self.assertIn("CA-R-110", frontier_ids)
        self.assertNotIn("CA-R-111", frontier_ids)
        self.assertEqual(
            "inactive-status-skipped",
            graph.discover_atoms(self.root, self.selected)[1][-1]["code"],
        )

    def test_whole_control_root_excludes_persisted_projection_and_journal_copies(self) -> None:
        live = self.root / self.control_root / "000_framework" / "CA-R-201.md"
        live.parent.mkdir(parents=True)
        live.write_text(
            current_atom("CA-R-201", governs="Projection/Journal: Ledger"),
            encoding="utf-8",
            newline="\n",
        )
        copied_projection = self.root / self.projection_root / "snapshot" / "CA-R-201.md"
        copied_projection.parent.mkdir(parents=True)
        copied_projection.write_bytes(live.read_bytes())
        journal_copy = self.root / self.control_root / "_journal" / "CA-R-202.md"
        journal_copy.parent.mkdir(parents=True)
        journal_copy.write_text(
            current_atom("CA-R-202", governs="Journal Copy"),
            encoding="utf-8",
            newline="\n",
        )

        control = self.root / self.control_root
        carriers, _ = graph.discover_atoms(self.root, control)
        frontier = graph.source_frontier_for(self.root, control)

        self.assertEqual(["CA-R-201"], [carrier.atom_id for carrier in carriers])
        self.assertEqual([f"{self.control_root}/000_framework/CA-R-201.md"], [carrier.carrier_path for carrier in carriers])
        self.assertEqual(["CA-R-201"], [row["atom_id"] for row in frontier["carriers"]])

    def test_queue_handlers_consume_frozen_parameters_without_owning_transitions(self) -> None:
        handlers = graph.queue_action_handlers(self.root)
        output = handlers["CA-O-134"]({"parameters": self.request("entities")})

        self.assertEqual("built", output["result"])
        self.assertEqual([f"{self.projection_root}/entities_graph.json"], output["effect_refs"])
        self.assertEqual("built", output["graph_result"]["outcome"])
        self.assertIn("entities_graph", output["graph_result"])

    def test_quality_failures_never_return_built_or_no_op(self) -> None:
        self.write(
            "CA-R-005.md",
            atom("CA-R-005", cce_form="definition", governs="Cycle", depends_on=("Cycle",)),
        )
        frontier = graph.source_frontier_for(self.root, self.selected)
        result = graph.build_graph(
            self.root,
            self.request(
                "terms",
                source_frontier=frontier,
                selection={"atom_ids": ["CA-R-005"]},
            ),
        )
        self.assertIn(result["outcome"], {"incomplete", "conflicting", "stale", "blocked", "failed"})
        self.assertNotIn(result["outcome"], {"built", "no_op"})
        self.assertIn("self-reference", {row["code"] for row in result["diagnostics"]})
        self.assertEqual("fail", result["quality_dispositions"]["validity"])

    def test_selected_project_structure_is_traced_from_the_authoritative_toml(self) -> None:
        structure = self.root / self.control_root / "project_structure.toml"
        structure.parent.mkdir(parents=True, exist_ok=True)
        structure.write_text(
            "schema_version = 1\n\n"
            "[[scope_units]]\n"
            'scope_unit_name = "TOOLS"\n'
            'parent = "PROGRAMMATIC"\n'
            'scope_unit_type = "Unordered"\n'
            'scope_unit_label = "FEATURE"\n'
            "structural_level = 3\n"
            "navigational_order_number = 1\n"
            'authority_path = ".caprmedio_caprmedio/tools"\n'
            'delivery_path = "tools"\n'
            'authority_mode = "strict"\n',
            encoding="utf-8",
            newline="\n",
        )
        result = graph.build_graph(
            self.root,
            self.request("entities", selection={"atom_ids": ["CA-R-001"], "scope_unit_names": ["TOOLS"]}),
        )
        self.assertEqual("built", result["outcome"])
        row = result["entities_graph"]["project_structure"][0]
        self.assertEqual("TOOLS", row["scope_unit_name"])
        self.assertEqual("PROGRAMMATIC", row["parent"])
        self.assertEqual(f"{self.control_root}/project_structure.toml", row["source"]["carrier_path"])
        self.assertIn("carrier_sha256", row["source"])

    def test_canonical_atomic_publication_no_op_and_stale_frontier_are_truthful(self) -> None:
        destination = f"{self.projection_root}/terms-checkpoint.json"
        first = graph.build_graph(self.root, self.request("terms", output_destination=destination))
        output = self.root / destination
        first_bytes = output.read_bytes()
        second = graph.build_graph(
            self.root,
            self.request(
                "terms",
                output_destination=destination,
                existing_projection_evidence={"sha256": hashlib.sha256(first_bytes).hexdigest()},
            ),
        )
        self.assertEqual("built", first["outcome"])
        self.assertEqual("no_op", second["outcome"])
        self.assertEqual(first_bytes, output.read_bytes())
        stale_frontier = self.request("entities")["source_frontier"]
        self.write("CA-R-001.md", atom("CA-R-001", cce_form="definition", governs="Entity", claim="changed."))
        stale = graph.build_graph(self.root, self.request("entities", source_frontier=stale_frontier))
        self.assertEqual("stale", stale["outcome"])
        self.assertEqual([], stale["output_effects"]["paths"])

    def test_default_publication_uses_the_configured_project_projection_root(self) -> None:
        entities = graph.build_graph(self.root, self.request("entities"))
        terms = graph.build_graph(self.root, self.request("terms"))

        entity_destination = f"{self.projection_root}/entities_graph.json"
        term_destination = f"{self.projection_root}/terms_graph.json"
        self.assertEqual("built", entities["outcome"])
        self.assertEqual({"state": "created", "paths": [entity_destination]}, entities["output_effects"])
        self.assertEqual("built", terms["outcome"])
        self.assertEqual({"state": "created", "paths": [term_destination]}, terms["output_effects"])
        self.assertTrue((self.root / entity_destination).is_file())
        self.assertTrue((self.root / term_destination).is_file())
        self.assertFalse((self.root / ".caprmedio_runtime" / "graph_projections").exists())

        rejected = graph.build_graph(
            self.root,
            self.request("entities", output_destination=".caprmedio_runtime/graph_projections/entities.json"),
        )
        self.assertEqual("failed", rejected["outcome"])
        self.assertEqual("output-destination-unauthorized", rejected["diagnostics"][0]["code"])


if __name__ == "__main__":
    unittest.main()
