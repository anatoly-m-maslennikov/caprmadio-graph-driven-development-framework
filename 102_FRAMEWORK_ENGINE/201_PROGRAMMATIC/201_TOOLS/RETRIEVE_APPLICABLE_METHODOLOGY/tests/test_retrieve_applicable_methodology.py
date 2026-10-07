from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


TOOL = Path(__file__).resolve().parents[1] / "retrieve_applicable_methodology.py"
SPEC = importlib.util.spec_from_file_location("retrieve_applicable_methodology", TOOL)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def source_carrier(atom_id: str, governs: tuple[str, str], depends_on: tuple[str, str] | None = None) -> bytes:
    dependency = ""
    if depends_on:
        dependency = f"  depends_on:\n    {depends_on[0]}:\n      - {depends_on[1]}\n"
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: obligation\n"
        "subjects:\n"
        "  governs:\n"
        f"    {governs[0]}:\n"
        f"      - {governs[1]}\n"
        f"{dependency}"
        "version: 1\n"
        "updated_at: 2026-08-27 00:00:00 +0400\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\nclaim\n"
    ).encode()


def projected(source: bytes, relative_source: str) -> bytes:
    boundary = source.find(b"\n---\n", 4)
    addition = f"\nprojection:\n  source_carrier_path: {relative_source}".encode()
    return source[:boundary] + addition + source[boundary:]


class RetrieverTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = Path.cwd() / ".caprmedio_tmp/retriever-tests"
        temporary.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="case-", dir=temporary))
        self.applicable = self.root / module.APPLICABLE_RELATIVE
        self.source_root = self.root / module.SOURCES_RELATIVE / "001_CORE_META_MODEL"
        for role in module.ROLES:
            (self.applicable / role).mkdir(parents=True)
            (self.source_root / role).mkdir(parents=True)
        self.add_project_settings()

    def tearDown(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def add(self, role: str, name: str, data: bytes) -> None:
        source = self.source_root / role / name
        source.write_bytes(data)
        target = self.applicable / role / name
        relative = Path(os.path.relpath(source, start=target.parent))
        target.write_bytes(projected(data, relative.as_posix()))

    def add_project_settings(self, project_name: str = "caprmedio", control_root: str = ".caprmedio_caprmedio") -> None:
        graph = self.root / module.SETTINGS_PATH
        graph.parent.mkdir(parents=True, exist_ok=True)
        graph.write_text(
            f"[project]\nkey = {project_name!r}\nname = {project_name!r}\nrepository_slug = 'test'\n"
            f"[artifacts.identity]\nproject_prefix = 'TEST'\n[paths]\ncontrol_root = {control_root!r}\n",
            encoding="utf-8",
        )

    def invoke(self, *arguments: str) -> tuple[int, dict[str, object]]:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = module.run(["--root", str(self.root), *arguments])
        return code, json.loads(output.getvalue())

    def test_subject_seed_closes_prerequisites_and_preserves_compilation_order(self) -> None:
        self.add("04_requirement", "CA-R-001--base.md", source_carrier("CA-R-001", ("continuant", "Base")))
        self.add(
            "05_method",
            "CA-M-001--consumer.md",
            source_carrier("CA-M-001", ("continuant", "Consumer"), ("continuant", "Base")),
        )
        code, report = self.invoke("--subject", "Consumer")
        self.assertEqual(code, 0)
        self.assertTrue(report["complete"])
        self.assertEqual([item["atom_id"] for item in report["selected_atoms"]], ["CA-R-001", "CA-M-001"])
        self.assertEqual(report["selected_atom_count"], 2)
        self.assertFalse(report["persistent_subject_index_created"])

    def test_process_query_matches_only_occurrent_governors(self) -> None:
        self.add("04_requirement", "CA-R-001--continuant.md", source_carrier("CA-R-001", ("continuant", "Build")))
        self.add("05_method", "CA-M-001--occurrent.md", source_carrier("CA-M-001", ("occurrent", "Build")))
        code, report = self.invoke("--process", "Build")
        self.assertEqual(code, 0)
        self.assertEqual([item["atom_id"] for item in report["selected_atoms"]], ["CA-M-001"])

    def test_unknown_uppercase_subject_fails_closed(self) -> None:
        self.add("04_requirement", "CA-R-001--base.md", source_carrier("CA-R-001", ("continuant", "Base")))
        code, report = self.invoke("--subject", "Missing")
        self.assertEqual(code, 2)
        self.assertEqual(report["selected_atom_count"], 0)
        self.assertFalse(report["complete"])
        self.assertEqual(report["diagnostics"][0]["subject_path"], "Missing")

    def test_scope_unit_query_returns_structural_frontier_without_atom_selection(self) -> None:
        code, report = self.invoke("--subject", "CORE_META_MODEL")
        self.assertEqual(code, 0)
        self.assertTrue(report["complete"])
        self.assertEqual(report["selected_atom_count"], 0)
        outcomes = report["resolution_outcomes"]
        self.assertTrue(all(item["category"] == "scope_unit" for item in outcomes))
        self.assertTrue(all(item["scope_unit"] == "CORE_META_MODEL" for item in outcomes))
        self.assertTrue(all(item["current_scope"] == "METHODOLOGY_SOURCES" for item in outcomes))

    def test_project_scope_unit_query_uses_project_settings(self) -> None:
        self.add_project_settings()
        code, report = self.invoke("--subject", "Project")
        self.assertEqual(code, 0)
        self.assertTrue(report["complete"])
        outcomes = report["resolution_outcomes"]
        self.assertTrue(all(item["category"] == "scope_unit" for item in outcomes))
        self.assertTrue(all(item["scope_unit"] == "caprmedio" for item in outcomes))
        self.assertTrue(all(item["source"] == "project_settings" for item in outcomes))


    def test_stale_graph_cannot_override_settings_identity(self) -> None:
        self.add_project_settings("different_project")
        graph = self.root / ".caprmedio_caprmedio/project_scope_unit_graph.projection.toml"
        graph.write_text("[project]\nname = 'CAPRMEDIO'\n", encoding="utf-8")
        code, report = self.invoke("--subject", "Project")
        self.assertEqual(0, code)
        self.assertTrue(all(item["scope_unit"] == "different_project" for item in report["resolution_outcomes"]))
        self.assertTrue(all(item["project_settings_carrier"] == module.SETTINGS_PATH.as_posix() for item in report["resolution_outcomes"]))

    def test_project_query_fails_closed_without_valid_settings(self) -> None:
        path = self.root / module.SETTINGS_PATH
        graph = path.parent / "project_scope_unit_graph.projection.toml"
        graph.write_text("[project]\nname = 'caprmedio'\n", encoding="utf-8")
        for payload in (None, "[project", "project = 'bad'", "[project]\nname = 'caprmedio'\n"):
            with self.subTest(payload=payload):
                if payload is None:
                    path.unlink(missing_ok=True)
                else:
                    path.write_text(payload, encoding="utf-8")
                code, report = self.invoke("--subject", "Project")
                self.assertEqual(2, code)
                self.assertEqual("project-settings-invalid", report["diagnostics"][0]["code"])

    def test_project_settings_rejects_nonlowercase_name_and_symlink(self) -> None:
        self.add_project_settings("CAPRMEDIO")
        code, _ = self.invoke("--subject", "Project")
        self.assertEqual(2, code)
        path = self.root / module.SETTINGS_PATH
        original = path.with_suffix(".original")
        path.rename(original)
        path.symlink_to(original)
        code, _ = self.invoke("--subject", "Project")
        self.assertEqual(2, code)

    def test_lowercase_general_subject_is_successful_terminal(self) -> None:
        code, report = self.invoke("--subject", "methodology")
        self.assertEqual(code, 0)
        self.assertTrue(report["complete"])
        self.assertEqual(report["selected_atom_count"], 0)
        outcomes = report["resolution_outcomes"]
        self.assertTrue(all(item["category"] == "general_subject" for item in outcomes))
        self.assertTrue(all(item["terminal"] == "true" for item in outcomes))

    def test_unresolved_prerequisite_is_explicit_and_fails_closed(self) -> None:
        self.add(
            "05_method",
            "CA-M-001--consumer.md",
            source_carrier("CA-M-001", ("continuant", "Consumer"), ("continuant", "Missing")),
        )
        code, report = self.invoke("--subject", "Consumer")
        self.assertEqual(code, 2)
        self.assertFalse(report["complete"])
        self.assertEqual(report["diagnostics"][0]["subject_path"], "Missing")

    def test_source_drift_fails_before_retrieval(self) -> None:
        self.add("04_requirement", "CA-R-001--base.md", source_carrier("CA-R-001", ("continuant", "Base")))
        source = self.source_root / "04_requirement/CA-R-001--base.md"
        source.write_bytes(source.read_bytes() + b"drift")
        code, report = self.invoke("--subject", "Base")
        self.assertEqual(code, 2)
        self.assertEqual(report["diagnostics"][0]["code"], "projection-source-mismatch")

    def test_role_root_ds_store_is_ignored_without_changing_retrieval_or_bytes(self) -> None:
        self.add("04_requirement", "CA-R-001--base.md", source_carrier("CA-R-001", ("continuant", "Base")))
        expected_code, expected_report = self.invoke("--subject", "Base")
        metadata = self.applicable / "04_requirement/.DS_Store"
        payload = b"Finder metadata must remain untouched"
        metadata.write_bytes(payload)

        code, report = self.invoke("--subject", "Base")

        self.assertEqual(expected_code, code)
        self.assertEqual(expected_report, report)
        self.assertEqual(payload, metadata.read_bytes())

    def test_role_root_ds_store_directory_or_symlink_still_fails_closed(self) -> None:
        role_root = self.applicable / "04_requirement"
        metadata = role_root / ".DS_Store"
        real_iterdir = Path.iterdir
        real_is_file = Path.is_file
        real_is_symlink = Path.is_symlink
        for kind in ("directory", "symlink"):
            with self.subTest(kind=kind):
                # macOS may deny removal of a directory literally named
                # .DS_Store. Simulate only the role-root entry type while
                # retaining real Path values for diagnostic rendering.
                def iterdir(path: Path):
                    entries = list(real_iterdir(path))
                    return iter(entries + [metadata] if path == role_root else entries)

                def is_file(path: Path) -> bool:
                    return kind == "symlink" if path == metadata else real_is_file(path)

                def is_symlink(path: Path) -> bool:
                    return kind == "symlink" if path == metadata else real_is_symlink(path)

                with mock.patch.object(Path, "iterdir", iterdir), \
                        mock.patch.object(Path, "is_file", is_file), \
                        mock.patch.object(Path, "is_symlink", is_symlink):
                    code, report = self.invoke("--subject", "Base")

                self.assertEqual(2, code)
                self.assertEqual("role-root-non-carrier", report["diagnostics"][0]["code"])

    def test_role_root_non_carrier_entry_still_fails_closed(self) -> None:
        invalid = self.applicable / "04_requirement/unexpected.txt"
        invalid.write_text("not a projected carrier", encoding="utf-8")

        code, report = self.invoke("--subject", "Base")

        self.assertEqual(2, code)
        self.assertEqual("role-root-non-carrier", report["diagnostics"][0]["code"])
        self.assertIn("unexpected.txt", report["diagnostics"][0]["details"]["paths"][0])

    def test_compiler_projection_metadata_does_not_change_source_payload(self) -> None:
        data = source_carrier("CA-R-001", ("continuant", "Base"))
        source = self.source_root / "04_requirement/CA-R-001--base.md"
        source.write_bytes(data)
        target = self.applicable / "04_requirement/CA-R-001--base.md"
        relative = Path(os.path.relpath(source, start=target.parent)).as_posix()
        rendered = projected(data, relative).replace(
            f"  source_carrier_path: {relative}\n---\n".encode(),
            (
                f"  source_carrier_path: {relative}\n"
                "  source_atom_id: CA-R-001\n"
                "  source_atom_revision: 1\n"
                "  source_sha256: fixture\n"
                "  original_relations_sha256: fixture\n---\n"
            ).encode(),
        )
        target.write_bytes(rendered)

        code, report = self.invoke("--subject", "Base")

        self.assertEqual(0, code)
        self.assertTrue(report["complete"])

    def test_same_frontier_produces_same_selection_digest(self) -> None:
        self.add("04_requirement", "CA-R-001--base.md", source_carrier("CA-R-001", ("continuant", "Base")))
        first_code, first = self.invoke("--subject", "Base")
        second_code, second = self.invoke("--subject", "Base")
        self.assertEqual((first_code, second_code), (0, 0))
        self.assertEqual(first["selected_frontier_digest"], second["selected_frontier_digest"])

    def test_published_output_uses_configured_control_root_while_sources_remain_framework(self) -> None:
        control = ".caprmedio_fixture"
        self.add_project_settings(control_root=control)
        published = self.root / control / "_projection/APPLICABLE_METHODOLOGY"
        for role in module.ROLES:
            (published / role).mkdir(parents=True, exist_ok=True)
        self.applicable = published
        self.add("04_requirement", "CA-R-001--base.md", source_carrier("CA-R-001", ("continuant", "Base")))

        code, report = self.invoke("--subject", "Base")

        self.assertEqual(0, code)
        self.assertTrue(report["complete"])


if __name__ == "__main__":
    unittest.main()
