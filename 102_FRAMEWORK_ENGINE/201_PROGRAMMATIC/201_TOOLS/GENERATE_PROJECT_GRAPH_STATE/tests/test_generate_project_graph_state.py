"""Focused acceptance tests for typed Project Scope Unit graph discovery."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
import tomllib


SCRIPT = Path(__file__).resolve().parents[1] / "generate_project_graph_state.py"
SPEC = importlib.util.spec_from_file_location("generate_project_graph_state", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
generate_project_graph_state = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = generate_project_graph_state
SPEC.loader.exec_module(generate_project_graph_state)


class GenerateProjectGraphStateTests(unittest.TestCase):
    def test_quoted_source_timestamps_use_the_existing_supported_formats(self) -> None:
        for value in ('"2026-09-06 12:00:00 +0400"', "'2026-09-06 12:00:00'", "2026-09-06 12:00:00 +0400"):
            self.assertEqual("2026-09-06 12:00:00", generate_project_graph_state.normalise_timestamp(value))
        self.assertEqual("", generate_project_graph_state.normalise_timestamp('"invalid"'))

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name) / "repository"
        self.control = self.root / ".caprmedio_caprmedio"
        self.control.mkdir(parents=True)
        self.modes = {"default": "casual"}
        self.project_settings = self.root / generate_project_graph_state.SETTINGS_PATH
        self.project_settings.write_text(
            "[project]\nkey = 'fixture_project'\nname = 'fixture_project'\nrepository_slug = 'test'\n"
            "[artifacts.identity]\nproject_prefix = 'TEST'\n", encoding="utf-8",
        )
        self.framework_settings = self.root / "framework_settings.toml"
        self.framework_settings.write_text(
            "[authority_modes]\ndefault = 'casual'\ngovernance = 'strict'\n"
            "metamodel = 'strict'\nproject = 'strict'\nsemantics = 'strict'\n", encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def mkdir(self, relative: str) -> Path:
        path = self.control / relative
        path.mkdir(parents=True)
        return path

    def test_live_topology_has_exactly_the_current_typed_scope_units(self) -> None:
        rows = generate_project_graph_state.scope_units(
            generate_project_graph_state.CONTROL,
            generate_project_graph_state.ROOT,
            generate_project_graph_state.configuration()["authority_modes"],
        )
        parent_by_node = {row["node_id"]: row["structural_parent"] for row in rows}
        levels_by_node = {row["node_id"]: row["structural_level"] for row in rows}
        navigational_orders_by_node = {
            row["node_id"]: row["navigational_order_number"] for row in rows
        }
        self.assertEqual(
            [
                "101_LAYER_1_FRAMEWORK_METHODOLOGY",
                "102_LAYER_2_FRAMEWORK_ENGINE",
                "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC",
                "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS",
                "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS",
                "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP",
                "102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC",
                "102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS",
                "103_LAYER_3_OPERATOR_DOCUMENTATION",
                "104_LAYER_4_CORE_EXTENSIONS",
                "105_LAYER_5_RELEASES",
                "110_FEATURE_COMMUNITY_EXTENSIONS",
                "110_FEATURE_FIELD",
            ],
            [row["node_id"] for row in rows],
        )
        self.assertEqual("caprmedio", parent_by_node["102_LAYER_2_FRAMEWORK_ENGINE"])
        self.assertEqual(
            "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC",
            parent_by_node["102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS"],
        )
        self.assertEqual(
            "102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC",
            parent_by_node["102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS"],
        )
        self.assertEqual(1, levels_by_node["101_LAYER_1_FRAMEWORK_METHODOLOGY"])
        self.assertEqual(2, levels_by_node["102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC"])
        self.assertEqual(
            3,
            levels_by_node[
                "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS"
            ],
        )
        self.assertEqual(10, navigational_orders_by_node["110_FEATURE_COMMUNITY_EXTENSIONS"])
        self.assertEqual(
            1,
            navigational_orders_by_node[
                "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS"
            ],
        )
        self.assertNotIn("CA-Epic", "\n".join(row["node_id"] for row in rows))
        required_fields = {
            "scope_unit_name",
            "project_boundary_position",
            "scope_unit_type",
            "scope_unit_label",
            "child_composition",
            "structural_level",
            "local_order",
            "navigational_order_number",
            "parent",
            "authority_path",
        }
        self.assertTrue(all(required_fields <= set(row) for row in rows))
        self.assertTrue(all(row["project_boundary_position"] == "PROJECT" for row in rows))
        self.assertEqual("Ordered", rows[0]["scope_unit_type"])
        self.assertEqual("LAYER", rows[0]["scope_unit_label"])
        self.assertEqual("UNORDERED", rows[1]["child_composition"])
        self.assertEqual("NONE", rows[0]["child_composition"])

    def test_nearest_typed_scope_unit_is_parent_even_across_an_epic_directory(self) -> None:
        self.mkdir("101_LAYER_1_ROOT")
        self.mkdir(
            "101_LAYER_1_ROOT/03_plan/02-CA-Epic-004-ROOT-separate-epic-carrier/201_FEATURE_CHILD"
        )
        self.mkdir("101_LAYER_1_ROOT/archive/301_FEATURE_RETIRED")
        self.mkdir("jobs_archive/CA-J-100")

        rows = generate_project_graph_state.scope_units(self.control, self.root, self.modes)
        parent_by_node = {row["node_id"]: row["structural_parent"] for row in rows}

        self.assertEqual(
            [
                "101_LAYER_1_ROOT",
                "101_LAYER_1_ROOT/03_plan/02-CA-Epic-004-ROOT-separate-epic-carrier/201_FEATURE_CHILD",
            ],
            [row["node_id"] for row in rows],
        )
        self.assertEqual(
            "101_LAYER_1_ROOT",
            parent_by_node[
                "101_LAYER_1_ROOT/03_plan/02-CA-Epic-004-ROOT-separate-epic-carrier/201_FEATURE_CHILD"
            ],
        )
        self.assertTrue(
            generate_project_graph_state.EPIC_DIRECTORY.fullmatch(
                "02-CA-Epic-004-ROOT-separate-epic-carrier"
            )
        )

    def test_directory_grammar_requires_layer_order_and_forbids_feature_order(self) -> None:
        layer = generate_project_graph_state.parse_scope_unit_name("101_LAYER_3_FRAMEWORK")
        feature = generate_project_graph_state.parse_scope_unit_name("201_FEATURE_PROGRAMMATIC")
        self.assertEqual("101", layer["numeric_prefix"])
        self.assertEqual(3, layer["local_order"])
        self.assertEqual("Ordered", layer["scope_unit_type"])
        self.assertEqual("LAYER", layer["scope_unit_label"])
        self.assertIsNone(feature["local_order"])
        self.assertEqual("Unordered", feature["scope_unit_type"])
        self.assertEqual("FEATURE", feature["scope_unit_label"])
        with self.assertRaisesRegex(SystemExit, "Local Order"):
            generate_project_graph_state.parse_scope_unit_name("201_FEATURE_1_PROGRAMMATIC")
        with self.assertRaisesRegex(SystemExit, "Local Order"):
            generate_project_graph_state.parse_scope_unit_name("101_LAYER_FRAMEWORK")

    def test_dynamic_prefix_width_validates_ancestry_and_emits_navigational_order(self) -> None:
        self.assertEqual(
            7,
            generate_project_graph_state.navigational_order_number(
                "12007", structural_level=12, structural_level_width=2
            ),
        )
        with self.assertRaisesRegex(SystemExit, "Structural Level"):
            generate_project_graph_state.navigational_order_number(
                "110", structural_level=2, structural_level_width=1
            )
        with self.assertRaisesRegex(SystemExit, "Navigational Order Number"):
            generate_project_graph_state.navigational_order_number(
                "100", structural_level=1, structural_level_width=1
            )

    def test_current_configuration_binding_and_projection_keep_project_identity_lowercase(self) -> None:
        config = generate_project_graph_state.configuration()
        bindings = generate_project_graph_state.settings_bindings()
        modes = config["authority_modes"]
        assert isinstance(modes, dict)
        rows = generate_project_graph_state.bind_scope_unit_structure(
            generate_project_graph_state.scope_units(
                generate_project_graph_state.CONTROL,
                generate_project_graph_state.ROOT,
                modes,
            )
        )
        source_atoms = generate_project_graph_state.active_source_atoms()
        payload = generate_project_graph_state.project_scope_unit_graph(
            generate_project_graph_state.source_updated_at(bindings, source_atoms), config, bindings, rows, source_atoms
        )

        self.assertEqual(
            ".caprmedio_caprmedio/caprmedio_project_settings.toml",
            bindings["project_settings"]["carrier"],
        )
        self.assertEqual("CA", config["artifacts"]["identity"]["project_prefix"])
        self.assertEqual("caprmedio", config["project"]["key"])
        self.assertIn('key = "caprmedio"', payload)
        self.assertIn('name = "caprmedio"', payload)
        self.assertIn(
            'carrier = ".caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml"',
            payload,
        )
        self.assertNotIn("002_FRAMEWORK_ENGINE", payload)


    def test_identity_and_structural_project_parent_come_only_from_project_settings(self) -> None:
        self.mkdir("101_LAYER_1_ROOT")
        with mock.patch.object(generate_project_graph_state, "ROOT", self.root), mock.patch.object(
            generate_project_graph_state, "CONFIG", self.framework_settings
        ):
            config = generate_project_graph_state.configuration()
            rows = generate_project_graph_state.scope_units(self.control, self.root, config["authority_modes"])
        self.assertEqual("fixture_project", config["project"]["name"])
        self.assertEqual("TEST", config["artifacts"]["identity"]["project_prefix"])
        self.assertEqual("fixture_project", rows[0]["parent"])
        self.assertEqual("fixture_project", rows[0]["structural_parent"])

    def test_missing_or_invalid_project_settings_never_falls_back_to_framework_settings(self) -> None:
        self.framework_settings.write_text(
            self.framework_settings.read_text() + "\n[project]\nkey='caprmedio'\nname='caprmedio'\nrepository_slug='test'\n"
            "[artifacts.identity]\nproject_prefix='CA'\n", encoding="utf-8",
        )
        self.project_settings.unlink()
        with mock.patch.object(generate_project_graph_state, "ROOT", self.root), mock.patch.object(
            generate_project_graph_state, "CONFIG", self.framework_settings
        ):
            with self.assertRaisesRegex(SystemExit, "Project Settings"):
                generate_project_graph_state.configuration()
            for payload in ("not valid TOML", "project='bad'", "[project]\nname='caprmedio'\n"):
                with self.subTest(payload=payload):
                    self.project_settings.write_text(payload)
                    with self.assertRaisesRegex(SystemExit, "Project Settings"):
                        generate_project_graph_state.configuration()

    def test_duplicate_project_identity_in_framework_settings_is_rejected(self) -> None:
        original = self.framework_settings.read_text()
        with mock.patch.object(generate_project_graph_state, "ROOT", self.root), mock.patch.object(
            generate_project_graph_state, "CONFIG", self.framework_settings
        ):
            for addition in ("\n[project]\nname='other'\n", "\n[artifacts.identity]\nproject_prefix='OTHER'\n"):
                with self.subTest(addition=addition):
                    self.framework_settings.write_text(original + addition)
                    with self.assertRaisesRegex(SystemExit, "belongs only in Project Settings"):
                        generate_project_graph_state.configuration()

    def test_receipts_bind_both_settings_separately_and_detect_drift_or_ambiguity(self) -> None:
        journal = self.control / "work_journal"
        journal.mkdir()
        records = [
            {
                "kind": "governed_project_change", "event": "completed", "subject_kind": "file",
                "occurred_at": "2026-09-11 00:00:00 +0400", "event_id": path.stem,
                "result": {"path": path.relative_to(self.root).as_posix(),
                           "sha256": generate_project_graph_state.sha(path), "version": 1},
            }
            for path in (self.project_settings, self.framework_settings)
        ]
        receipt = journal / "settings.ndjson"
        receipt.write_text("\n".join(json.dumps(record) for record in records) + "\n")
        with mock.patch.object(generate_project_graph_state, "ROOT", self.root), mock.patch.object(
            generate_project_graph_state, "CONFIG", self.framework_settings
        ), mock.patch.object(generate_project_graph_state, "JOURNAL", journal):
            bindings = generate_project_graph_state.settings_bindings()
            self.assertTrue(all(item["status"] == "resolved" for item in bindings.values()))
            self.assertNotEqual(bindings["project_settings"]["carrier"], bindings["framework_settings"]["carrier"])
            self.assertTrue(all("atom_id" not in item for item in bindings.values()))
            original = self.project_settings.read_text()
            self.project_settings.write_text(original + "\n# drift\n")
            bindings = generate_project_graph_state.settings_bindings()
            self.assertEqual("unresolved", bindings["project_settings"]["status"])
            self.assertEqual("resolved", bindings["framework_settings"]["status"])
            self.project_settings.write_text(original)
            receipt.write_text(receipt.read_text() + json.dumps(records[0]) + "\n")
            self.assertEqual("ambiguous", generate_project_graph_state.settings_bindings()["project_settings"]["status"])

    def test_active_methodology_source_frontier_covers_every_emitted_scope_unit_field(self) -> None:
        config = generate_project_graph_state.configuration()
        bindings = generate_project_graph_state.settings_bindings()
        modes = config["authority_modes"]
        assert isinstance(modes, dict)
        rows = generate_project_graph_state.bind_scope_unit_structure(
            generate_project_graph_state.scope_units(
                generate_project_graph_state.CONTROL,
                generate_project_graph_state.ROOT,
                modes,
            )
        )
        source_atoms = generate_project_graph_state.active_source_atoms()
        payload = generate_project_graph_state.project_scope_unit_graph_sources(
            generate_project_graph_state.source_updated_at(bindings, source_atoms),
            bindings,
            rows,
            source_atoms,
        )
        document = tomllib.loads(payload)
        bindings = document["bindings"]
        projection = document["projection"]
        by_field = {item["output_path"]: item for item in bindings}
        for field in ("project.key", "project.name", "project.repository_slug", "project.obsolete_names", "artifacts.identity.project_prefix"):
            self.assertEqual("project_settings", by_field[field]["source_kind"])
            self.assertEqual(generate_project_graph_state.SETTINGS_PATH.as_posix(), by_field[field]["source_carrier"])
        self.assertEqual("framework_settings", by_field["authority_modes"]["source_kind"])

        self.assertEqual(
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py",
            projection["canonical_generator"],
        )
        self.assertEqual(
            generate_project_graph_state.sha(generate_project_graph_state.CANONICAL_GENERATOR),
            projection["canonical_generator_sha256"],
        )
        self.assertTrue(projection["executed_generator"])
        self.assertTrue(projection["executed_generator_sha256"])
        self.assertEqual(13, len(rows))
        self.assertGreater(len(source_atoms), 0)
        self.assertEqual(
            {atom["atom_id"] for atom in source_atoms},
            {
                binding["output_path"].removeprefix("methodology_source_atoms.")
                for binding in bindings
                if binding["source_kind"] == "methodology_source_atom"
            },
        )
        for row in rows:
            prefix = "scope_units." + str(row["node_id"]) + "."
            output_paths = {item["output_path"] for item in bindings if item["output_path"].startswith(prefix)}
            for field in (
                "scope_unit_name",
                "project_boundary_position",
                "scope_unit_type",
                "scope_unit_label",
                "child_composition",
                "structural_level",
                "navigational_order_number",
                "parent",
                "authority_path",
                "delivery_path",
            ):
                self.assertIn(prefix + field, output_paths)
            self.assertIn(prefix + "delivery_path", output_paths)
            structure_bindings = [
                item
                for item in bindings
                if item["output_path"] == prefix + "delivery_path"
            ]
            self.assertEqual(1, len(structure_bindings))
            self.assertEqual("scope_unit_directory_structure", structure_bindings[0]["source_kind"])
            self.assertEqual(row["structure_sha256"], structure_bindings[0]["source_sha256"])

    def test_canonical_projection_bytes_do_not_depend_on_executed_generator_carrier(self) -> None:
        config = generate_project_graph_state.configuration()
        bindings = generate_project_graph_state.settings_bindings()
        modes = config["authority_modes"]
        assert isinstance(modes, dict)
        rows = generate_project_graph_state.bind_scope_unit_structure(
            generate_project_graph_state.scope_units(
                generate_project_graph_state.CONTROL,
                generate_project_graph_state.ROOT,
                modes,
            )
        )
        source_atoms = generate_project_graph_state.active_source_atoms()
        installation = generate_project_graph_state.installation_status(
            generate_project_graph_state.ROOT
        )
        installed = (
            generate_project_graph_state.ROOT
            / str(installation["package_root"])
            / "GENERATE_PROJECT_GRAPH_STATE"
            / "generate_project_graph_state.py"
        )
        self.assertTrue(installed.is_file())
        source_payload = generate_project_graph_state.project_scope_unit_graph(
            generate_project_graph_state.source_updated_at(bindings, source_atoms),
            config,
            bindings,
            rows,
            source_atoms,
            generate_project_graph_state.CANONICAL_GENERATOR,
        )
        installed_payload = generate_project_graph_state.project_scope_unit_graph(
            generate_project_graph_state.source_updated_at(bindings, source_atoms),
            config,
            bindings,
            rows,
            source_atoms,
            installed,
        )
        self.assertEqual(
            generate_project_graph_state.canonical_projection_bytes(source_payload),
            generate_project_graph_state.canonical_projection_bytes(installed_payload),
        )
        self.assertIn(
            'canonical_generator = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py"',
            installed_payload,
        )
        self.assertIn('executed_generator = ".caprmedio_runtime/tools/releases/', installed_payload)

    def test_identical_scope_frontier_serializes_identically(self) -> None:
        self.mkdir("101_LAYER_1_ROOT")
        self.mkdir("101_LAYER_1_ROOT/201_FEATURE_CHILD")

        first = generate_project_graph_state.scope_units(self.control, self.root, self.modes)
        second = generate_project_graph_state.scope_units(self.control, self.root, self.modes)

        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
