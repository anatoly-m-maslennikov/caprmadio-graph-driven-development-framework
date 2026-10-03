"""Deterministic acceptance tests for GENERATE_ENTITY_GRAPH."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


SCRIPT = Path(__file__).resolve().parents[1] / "generate_entity_graph.py"
SPEC = importlib.util.spec_from_file_location("generate_entity_graph", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
generate_entity_graph = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = generate_entity_graph
SPEC.loader.exec_module(generate_entity_graph)


def atom(
    atom_id: str,
    *,
    cce_form: str,
    governs: tuple[str, ...] = (),
    depends_on: tuple[str, ...] = (),
    legacy: bool = False,
    claim: str = "claim.",
) -> str:
    governs_key = "declared" if legacy else "governs"
    depends_on_key = "prerequisite" if legacy else "depends_on"

    def block(key: str, values: tuple[str, ...]) -> str:
        if not values:
            return f"  {key}:\n    continuant: []\n"
        items = "".join(f"      - {json.dumps(value)}\n" for value in values)
        return f"  {key}:\n    continuant:\n{items}"

    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        f"cce_form: {cce_form}\n"
        "subjects:\n"
        f"{block(governs_key, governs)}"
        f"{block(depends_on_key, depends_on)}"
        "version: 1\n"
        "updated_at: 2026-08-29 00:00:00 +0400\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\n"
        f"{claim}\n"
    )


class GenerateEntityGraphTests(unittest.TestCase):
    def test_filename_migration_preserves_unstated_canonical_identity(self) -> None:
        first = self.write("CA-R-123-MMODEL-CORE-REQUIREMENT--old.md",
                           atom("CA-R-123", cce_form="definition", governs=("Atom",)).replace("atom_id: CA-R-123\n", ""))
        before, _ = generate_entity_graph.discover_atoms(self.root, self.selected)
        first.rename(first.with_name("CA-R-123-CORE_META_MODEL-CORE-REQUIREMENT--new.md"))
        after, _ = generate_entity_graph.discover_atoms(self.root, self.selected)
        self.assertEqual(["CA-R-123"], [item.atom_id for item in before])
        self.assertEqual([item.atom_id for item in before], [item.atom_id for item in after])

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name) / "repository"
        self.selected = self.root / "selected"
        self.selected.mkdir(parents=True)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.selected / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        return path

    def test_builds_the_three_sets_and_keeps_terms_distinct_from_other_subjects(self) -> None:
        self.write(
            "definitions/CA-R-001.md",
            atom(
                "CA-R-001",
                cce_form="definition",
                governs=("Atom/Content Role: Plan/Type: Task",),
                depends_on=("Atom/Claim", "Work"),
            ),
        )
        self.write(
            "definitions/CA-R-002.md",
            atom(
                "CA-R-002",
                cce_form="definition",
                governs=("Atom/Claim",),
                depends_on=("Expression",),
            ),
        )
        self.write(
            "rules/CA-R-003.md",
            atom(
                "CA-R-003",
                cce_form="obligation",
                governs=("Work",),
                depends_on=("Runtime Observation",),
            ),
        )

        projection = generate_entity_graph.generate_projection(self.root, self.selected)

        self.assertEqual(
            ["Claim", "Task"],
            projection["declared_terms"],
        )
        self.assertEqual(
            ["Atom/Claim", "Atom/Content Role: Plan/Type: Task", "Work"],
            projection["governed_subjects"],
        )
        self.assertEqual(
            ["Atom/Claim", "Expression", "Runtime Observation", "Work"],
            projection["sets"]["depends_on_subjects"],
        )
        self.assertEqual(["Claim"], projection["terms_in_depends_on"])
        self.assertEqual(
            ["Expression", "Runtime Observation"],
            projection["depends_on_without_governs"],
        )
        task_tree = next(
            tree
            for tree in projection["sets"]["dependency_trees_by_declared_term"]
            if tree["subject"] == "Task"
        )
        parent_by_subject = {parent["subject"]: parent for parent in task_tree["parents"]}
        self.assertTrue(parent_by_subject["Claim"]["is_declared_term"])
        self.assertFalse(parent_by_subject["Work"]["is_declared_term"])
        self.assertEqual("Expression", parent_by_subject["Claim"]["parents"][0]["subject"])

        definitions = {row["term"]: row for row in projection["term_definitions"]}
        self.assertEqual(
            "Atom/Content Role: Plan/Type: Task",
            definitions["Task"]["definitions"][0]["subject_path"],
        )
        self.assertEqual("Atom/Claim", definitions["Claim"]["definitions"][0]["subject_path"])

        declared_tree = projection["sets"]["declared_term_tree"]
        atom_root = next(node for node in declared_tree if node["segment"] == "Atom")
        content_role = next(node for node in atom_root["children"] if node["segment"] == "Content Role")
        self.assertEqual("IS_BORNE_BY", content_role["relation_from_parent"])
        plan = next(node for node in content_role["children"] if node["segment"] == "Plan")
        self.assertEqual("IS_ALLOWED_VALUE_OF", plan["relation_from_parent"])

    def test_dependency_trees_expose_recursive_term_definitions(self) -> None:
        self.write(
            "CA-R-010.md",
            atom("CA-R-010", cce_form="definition", governs=("Alpha",), depends_on=("Beta",)),
        )
        self.write(
            "CA-R-011.md",
            atom("CA-R-011", cce_form="definition", governs=("Beta",), depends_on=("Gamma",)),
        )
        self.write(
            "CA-R-012.md",
            atom("CA-R-012", cce_form="definition", governs=("Gamma",), depends_on=("Alpha",)),
        )

        projection = generate_entity_graph.generate_projection(self.root, self.selected)

        self.assertEqual([["Alpha", "Beta", "Gamma"]], projection["dependency_cycles"])
        alpha = next(
            tree for tree in projection["sets"]["dependency_trees_by_declared_term"] if tree["subject"] == "Alpha"
        )
        cycle_leaf = alpha["parents"][0]["parents"][0]["parents"][0]
        self.assertTrue(cycle_leaf["cycle"])
        self.assertEqual(["Alpha", "Beta", "Gamma", "Alpha"], cycle_leaf["cycle_path"])

    def test_every_atom_must_govern_exactly_one_entity(self) -> None:
        self.write(
            "CA-R-013.md",
            atom(
                "CA-R-013",
                cce_form="definition",
                governs=("First Term", "Second Term"),
                depends_on=("Parent Subject",),
            ),
        )

        with self.assertRaisesRegex(
            generate_entity_graph.EntityGraphError,
            "exactly one governed Entity",
        ):
            generate_entity_graph.generate_projection(self.root, self.selected)

    def test_maps_legacy_subject_roles_and_excludes_nested_inactive_folders(self) -> None:
        self.write(
            "CA-R-020.md",
            atom(
                "CA-R-020",
                cce_form="definition",
                governs=("Current Term",),
                depends_on=("Parent Subject",),
                legacy=True,
            ),
        )
        self.write(
            "archive/CA-R-020@1.md",
            atom(
                "CA-R-020",
                cce_form="definition",
                governs=("Archived Term",),
                depends_on=("Archived Parent",),
            ),
        )

        projection = generate_entity_graph.generate_projection(self.root, self.selected)

        self.assertEqual(["Current Term"], projection["declared_terms"])
        self.assertEqual(["Parent Subject"], projection["depends_on_subjects"])
        self.assertEqual(1, projection["counts"]["legacy_schema_atoms"])
        relation = projection["claim_subject_relations"][0]
        self.assertIn(relation["source_schema_key"], {"declared", "prerequisite"})

    def test_reports_two_definition_atoms_for_the_same_terminal_term(self) -> None:
        self.write(
            "CA-R-021.md",
            atom("CA-R-021", cce_form="definition", governs=("Atom/Status",)),
        )
        self.write(
            "CA-R-022.md",
            atom("CA-R-022", cce_form="definition", governs=("Artifact/Status",)),
        )

        projection = generate_entity_graph.generate_projection(self.root, self.selected)

        self.assertEqual(1, projection["counts"]["definition_conflicts"])
        self.assertEqual("Status", projection["definition_conflicts"][0]["term"])
        self.assertEqual(2, len(projection["definition_conflicts"][0]["definitions"]))
        self.assertIn(
            "governed-term-definition-conflict",
            {row["code"] for row in projection["diagnostics"]},
        )

    def test_derives_the_three_typed_term_system_relations(self) -> None:
        self.write(
            "CA-R-023.md",
            atom(
                "CA-R-023",
                cce_form="definition",
                governs=("Type",),
                depends_on=("Property",),
            ),
        )
        self.write(
            "CA-R-024.md",
            atom(
                "CA-R-024",
                cce_form="classification",
                governs=("Type",),
                depends_on=("Property",),
                claim="Type SUBKIND_OF Property.",
            ),
        )
        self.write(
            "CA-R-025.md",
            atom(
                "CA-R-025",
                cce_form="definition",
                governs=("Atom/Content Role: Requirement/Type: Demand",),
                depends_on=("Type",),
            ),
        )

        projection = generate_entity_graph.generate_projection(self.root, self.selected)
        edge_keys = {
            (edge["relation"], edge["source_subject"], edge["target_subject"])
            for edge in projection["term_system"]["edges"]
        }
        self.assertIn(("SUBKIND_OF", "Type", "Property"), edge_keys)
        self.assertIn(
            ("IS_BORNE_BY", "Atom/Content Role: Requirement/Type", "Atom/Content Role: Requirement"),
            edge_keys,
        )
        self.assertIn(
            (
                "IS_ALLOWED_VALUE_OF",
                "Atom/Content Role: Requirement/Type: Demand",
                "Atom/Content Role: Requirement/Type",
            ),
            edge_keys,
        )
        self.assertEqual(
            ["Atom/Content Role: Requirement/Type"],
            projection["term_system"]["direct_parents"]["Demand"]["IS_ALLOWED_VALUE_OF"],
        )

    def test_derives_subkind_edge_from_modal_cce_claim(self) -> None:
        self.write(
            "CA-R-026.md",
            atom(
                "CA-R-026",
                cce_form="classification",
                governs=("Structural Entity",),
                depends_on=("Relational Artifact",),
                claim="the Term Structural Entity **must** be a SUBKIND_OF Relational Artifact.",
            ),
        )

        projection = generate_entity_graph.generate_projection(self.root, self.selected)
        edge_keys = {
            (edge["relation"], edge["source_subject"], edge["target_subject"])
            for edge in projection["term_system"]["edges"]
        }
        self.assertIn(
            ("SUBKIND_OF", "Structural Entity", "Relational Artifact"),
            edge_keys,
        )

    def test_reports_typed_parent_cardinality_and_subkind_cycles(self) -> None:
        self.write(
            "CA-R-026.md",
            atom("CA-R-026", cce_form="definition", governs=("Value",)),
        )
        self.write(
            "CA-R-027.md",
            atom("CA-R-027", cce_form="obligation", governs=("First/Type: Value",)),
        )
        self.write(
            "CA-R-028.md",
            atom("CA-R-028", cce_form="obligation", governs=("Second/Type: Value",)),
        )
        self.write(
            "CA-R-029.md",
            atom(
                "CA-R-029",
                cce_form="classification",
                governs=("Alpha",),
                depends_on=("Beta",),
                claim="Alpha SUBKIND_OF Beta.",
            ),
        )
        self.write(
            "CA-R-030.md",
            atom(
                "CA-R-030",
                cce_form="classification",
                governs=("Beta",),
                depends_on=("Alpha",),
                claim="Beta SUBKIND_OF Alpha.",
            ),
        )
        codes = {
            row["code"]
            for row in generate_entity_graph.generate_projection(self.root, self.selected)["term_system"][
                "violations"
            ]
        }
        self.assertIn("term-allowed-value-parent-cardinality", codes)
        self.assertIn("term-subkind-cycle", codes)

    def test_allows_multiple_direct_subkind_parents(self) -> None:
        self.write(
            "CA-R-039.md",
            atom("CA-R-039", cce_form="definition", governs=("Hybrid",)),
        )
        self.write(
            "CA-R-040.md",
            atom(
                "CA-R-040",
                cce_form="classification",
                governs=("Hybrid",),
                depends_on=("Alpha",),
                claim="Hybrid SUBKIND_OF Alpha.",
            ),
        )
        self.write(
            "CA-R-041.md",
            atom(
                "CA-R-041",
                cce_form="classification",
                governs=("Hybrid",),
                depends_on=("Beta",),
                claim="Hybrid SUBKIND_OF Beta.",
            ),
        )

        term_system = generate_entity_graph.generate_projection(self.root, self.selected)["term_system"]

        self.assertEqual(
            ["Alpha", "Beta"],
            term_system["direct_parents"]["Hybrid"]["SUBKIND_OF"],
        )
        self.assertNotIn(
            "term-subkind-parent-cardinality",
            {row["code"] for row in term_system["violations"]},
        )

    def test_reuses_type_across_bearer_occurrences_and_rejects_role_specific_type_terms(self) -> None:
        self.write(
            "CA-R-031.md",
            atom("CA-R-031", cce_form="definition", governs=("Type",), depends_on=("Property",)),
        )
        self.write(
            "CA-R-032.md",
            atom("CA-R-032", cce_form="obligation", governs=("Atom/Type",)),
        )
        self.write(
            "CA-R-034.md",
            atom("CA-R-034", cce_form="obligation", governs=("Artifact/Type",)),
        )
        self.write(
            "CA-R-033.md",
            atom("CA-R-033", cce_form="definition", governs=("Requirement Type",)),
        )

        projection = generate_entity_graph.generate_projection(self.root, self.selected)
        self.assertEqual(
            ["Requirement Type"],
            projection["term_system"]["prohibited_role_specific_type_terms"],
        )
        bearer_parents = projection["term_system"]["bearer_parents_by_subject_occurrence"]
        self.assertEqual(["Atom"], bearer_parents["Atom/Type"])
        self.assertEqual(["Artifact"], bearer_parents["Artifact/Type"])
        self.assertNotIn(
            "dependent-subject-bearer-cardinality",
            {row["code"] for row in projection["term_system"]["violations"]},
        )

    def test_cli_accepts_any_folder_and_is_read_only_by_default(self) -> None:
        self.write(
            "CA-R-030.md",
            atom("CA-R-030", cce_form="definition", governs=("Author",), depends_on=("Actor",)),
        )
        completed = subprocess.run(
            [
                sys.executable,
                "-B",
                str(SCRIPT),
                str(self.selected),
                "--repository",
                str(self.root),
                "--compact",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        document = json.loads(completed.stdout)
        self.assertTrue(document["ok"])
        self.assertEqual("selected", document["result"]["projection"]["source"]["selected_folder"])
        self.assertFalse((self.root / "ENTITY_GRAPH.projection.md").exists())

        output = self.root / "tmp/ENTITY_GRAPH.projection.md"
        subprocess.run(
            [
                sys.executable,
                "-B",
                str(SCRIPT),
                str(self.selected),
                "--repository",
                str(self.root),
                "--format",
                "markdown",
                "--output",
                str(output),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        rendered = output.read_text(encoding="utf-8")
        self.assertIn("Set 1 — Declared Term Tree", rendered)
        self.assertIn("Gaps — DEPENDS_ON without GOVERNS", rendered)


if __name__ == "__main__":
    unittest.main()
