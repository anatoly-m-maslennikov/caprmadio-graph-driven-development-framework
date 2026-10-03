from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


TOOL = Path(__file__).resolve().parents[1] / "compile_applicable_methodology.py"
SPEC = importlib.util.spec_from_file_location("compile_applicable_methodology", TOOL)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def carrier(atom_id: str, version: int = 1, extra: str = "", body: str = "claim", relations: str = "{}") -> bytes:
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: obligation\n"
        f"{extra}"
        f"version: {version}\n"
        "updated_at: 2026-08-27 00:00:00 +0400\n"
        f"relations: {relations}\n"
        "---\n"
        f"# {atom_id}\n\n{body}\n"
    ).encode()


def definition_carrier(atom_id: str, term: str, subject_path: str | None = None) -> bytes:
    governed = subject_path or term
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: definition\n"
        "subjects:\n"
        "  governs:\n"
        "    continuant:\n"
        f"      - {json.dumps(governed)}\n"
        "  depends_on:\n"
        "    continuant: []\n"
        "version: 1\n"
        "updated_at: 2026-08-29 00:00:00 +0400\n"
        "relations: {}\n"
        "---\n"
        f"# Define {term}\n\n"
        f"{term} definition.\n"
    ).encode()


class CompilerTest(unittest.TestCase):
    def test_definition_subject_accepts_scalar_governs_shorthand(self) -> None:
        frontmatter = (
            "atom_id: CA-R-001\n"
            "cce_form: definition\n"
            "subjects:\n"
            '  governs: "Evaluation For Relation"\n'
            "version: 1\n"
        )

        term, subject_path = module.definition_subject(frontmatter, "CA-R-001.md")

        self.assertEqual("Evaluation For Relation", term)
        self.assertEqual("Evaluation For Relation", subject_path)

    def test_identity_is_independent_of_mutable_filename_tokens(self) -> None:
        for name in (
            "CA-M-120-GOVERN-CORE-METHOD--old.md",
            "CA-M-120-CORE_META_MODEL-CORE-METHOD--new.md",
            "03-CA-M-120-CORE_META_MODEL-METHOD--new.md",
        ):
            self.assertEqual("CA-M-120", module.derive_atom_id(Path(name), "version: 1"))
        self.assertEqual(
            "CAPRMEDIO-E-169-EVAL_APPROACH",
            module.derive_atom_id(Path("CAPRMEDIO-E-169-CORE-EVAL_APPROACH--new.md"),
                                 'atom_id: "CAPRMEDIO-E-169-EVAL_APPROACH"'),
        )

    def setUp(self) -> None:
        temporary = Path.cwd() / ".caprmedio_tmp/compiler-tests"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temp = Path(tempfile.mkdtemp(prefix="case-", dir=temporary))
        self.source = self.temp / module.SOURCE_RELATIVE
        for _, directory, _, _ in module.LAYERS:
            (self.source / directory).mkdir(parents=True)
        (self.source / "002_INSTALLED_EXTENSIONS/.gitkeep").write_text("")
        for layer in ("001_CORE_META_MODEL", "003_PROJECT_CONFIGURATION"):
            for _, role in module.ROLES:
                (self.source / layer / role).mkdir()

    def tearDown(self) -> None:
        shutil.rmtree(self.temp, ignore_errors=True)

    def write(self, layer: str, role: str, name: str, data: bytes) -> Path:
        path = self.source / layer / role / name
        path.write_bytes(data)
        return path

    def invoke(self, *arguments: str) -> tuple[int, dict[str, object]]:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = module.run(["--root", str(self.temp), *arguments])
        return code, json.loads(stream.getvalue())

    def test_dry_run_apply_rerun_and_regeneration_are_deterministic(self) -> None:
        source = self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001-REQUIREMENT--one.md", carrier("CA-R-001"))
        local = self.write("003_PROJECT_CONFIGURATION", "05_method", "CA-M-001-METHOD--two.md", carrier("CA-M-001", body="two"))
        before = {source: source.read_bytes(), local: local.read_bytes()}

        first_code, first = self.invoke()
        second_code, second = self.invoke()
        self.assertEqual((first_code, first), (0, second))
        self.assertEqual(first["conflict_count"], 0)

        apply_code, applied = self.invoke("--apply")
        self.assertEqual(apply_code, 0)
        first_tree = applied["generated_tree_digest"]
        self.assertEqual(before, {source: source.read_bytes(), local: local.read_bytes()})
        projected = self.temp / module.OUTPUT_RELATIVE / "04_requirement" / source.name
        projected_text = projected.read_text()
        self.assertIn("projection:\n  source_carrier_path: ../000_APPLICABLE_MTHD_sources/", projected_text)
        self.assertIn("# CA-R-001\n\nclaim", projected_text)

        rerun_code, rerun = self.invoke("--apply")
        self.assertEqual(rerun_code, 0)
        self.assertEqual(first_tree, rerun["generated_tree_digest"])

        for _, role in module.ROLES:
            for path in (self.temp / module.OUTPUT_RELATIVE / role).glob("*"):
                path.unlink()
        regenerate_code, regenerated = self.invoke("--apply")
        self.assertEqual(regenerate_code, 0)
        self.assertEqual(first_tree, regenerated["generated_tree_digest"])
        self.assertEqual(before, {source: source.read_bytes(), local: local.read_bytes()})

    def test_source_unit_role_directories_do_not_count_as_source_layers(self) -> None:
        (self.source / "04_requirement").mkdir()
        (self.source / "04_requirement/CA-R-100--define-source-layer-goal.md").write_bytes(carrier("CA-R-100"))
        self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001--one.md", carrier("CA-R-001"))

        code, report = self.invoke()

        self.assertEqual(code, 0)
        self.assertTrue(report["can_apply"])
        self.assertEqual(report["selected_candidate_count"], 1)

    def test_duplicate_identity_blocks_apply_without_exact_approval(self) -> None:
        self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001-A--one.md", carrier("CA-R-001"))
        self.write("003_PROJECT_CONFIGURATION", "04_requirement", "CA-R-001-B--two.md", carrier("CA-R-001", version=2))
        code, report = self.invoke()
        self.assertEqual(code, 2)
        self.assertGreaterEqual(report["conflict_count"], 1)
        self.assertIn("duplicate_selected_atom_identity", {item["type"] for item in report["conflicts"]})
        apply_code, applied = self.invoke("--apply")
        self.assertEqual(apply_code, 2)
        self.assertEqual(applied["apply_status"], "BLOCKED")
        for _, role in module.ROLES:
            self.assertFalse((self.temp / module.OUTPUT_RELATIVE / role).exists())

    def test_duplicate_governed_term_definition_blocks_apply(self) -> None:
        self.write(
            "001_CORE_META_MODEL",
            "04_requirement",
            "CA-R-010--define-shared-term.md",
            definition_carrier("CA-R-010", "Shared Term"),
        )
        self.write(
            "003_PROJECT_CONFIGURATION",
            "04_requirement",
            "CA-R-011--redefine-shared-term.md",
            definition_carrier("CA-R-011", "Shared Term", "Artifact/Type: Shared Term"),
        )

        code, report = self.invoke()

        self.assertEqual(2, code)
        conflict = next(
            row for row in report["conflicts"] if row["type"] == "duplicate_governed_term_definition"
        )
        self.assertEqual("Shared Term", conflict["details"]["term"])
        apply_code, applied = self.invoke("--apply")
        self.assertEqual(2, apply_code)
        self.assertEqual("BLOCKED", applied["apply_status"])

    def test_exact_project_configuration_approval_resolves_one_conflict(self) -> None:
        first = self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001-A--one.md", carrier("CA-R-001"))
        second = self.write("003_PROJECT_CONFIGURATION", "04_requirement", "CA-R-001-B--two.md", carrier("CA-R-001", version=2))
        _, initial = self.invoke()
        conflict = next(item for item in initial["conflicts"] if item["type"] == "duplicate_selected_atom_identity")
        approval_path = self.temp / module.APPROVAL_RELATIVE
        approval = (
            'schema = "caprmedio.applicable_methodology_conflict_approvals.v1"\n\n'
            "[[approvals]]\n"
            f'conflict_id = "{conflict["conflict_id"]}"\n'
            f'source_frontier_digest = "{initial["source_frontier_digest"]}"\n'
            f'selected_source_carrier_path = "{second.relative_to(self.temp).as_posix()}"\n'
            'operator = "TEST_OPERATOR"\n'
        )
        approval_path.write_text(approval)

        code, report = self.invoke("--apply")
        self.assertEqual(code, 0)
        self.assertEqual(report["unresolved_conflict_count"], 0)
        output = self.temp / module.OUTPUT_RELATIVE / "04_requirement"
        self.assertFalse((output / first.name).exists())
        self.assertTrue((output / second.name).exists())

    def test_stale_approval_does_not_replace_output(self) -> None:
        self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001-A--one.md", carrier("CA-R-001"))
        selected = self.write("003_PROJECT_CONFIGURATION", "04_requirement", "CA-R-001-B--two.md", carrier("CA-R-001", version=2))
        _, initial = self.invoke()
        conflict = initial["conflicts"][0]
        approval = (
            'schema = "caprmedio.applicable_methodology_conflict_approvals.v1"\n\n'
            "[[approvals]]\n"
            f'conflict_id = "{conflict["conflict_id"]}"\n'
            'source_frontier_digest = "deadbeef"\n'
            f'selected_source_carrier_path = "{selected.relative_to(self.temp).as_posix()}"\n'
            'operator = "TEST_OPERATOR"\n'
        )
        (self.temp / module.APPROVAL_RELATIVE).write_text(approval)
        code, report = self.invoke("--apply")
        self.assertEqual(code, 2)
        self.assertEqual(report["apply_status"], "BLOCKED")

    def test_output_collision_is_reported(self) -> None:
        self.write("001_CORE_META_MODEL", "04_requirement", "SHARED--claim.md", carrier("CA-R-001"))
        self.write("003_PROJECT_CONFIGURATION", "04_requirement", "SHARED--claim.md", carrier("CA-R-002"))
        code, report = self.invoke()
        self.assertEqual(code, 2)
        self.assertIn("output_path_collision", {item["type"] for item in report["conflicts"]})

    def test_dry_run_reports_all_five_conflict_classes(self) -> None:
        self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001-A--one.md", carrier("CA-R-001"))
        self.write("003_PROJECT_CONFIGURATION", "04_requirement", "CA-R-001-B--two.md", carrier("CA-R-001", version=2))
        self.write(
            "001_CORE_META_MODEL",
            "04_requirement",
            "CA-R-002--replacer.md",
            carrier("CA-R-002", relations="\n  replacement_of:\n    - CA-R-003"),
        )
        self.write("003_PROJECT_CONFIGURATION", "04_requirement", "CA-R-003--replaced.md", carrier("CA-R-003"))
        self.write(
            "001_CORE_META_MODEL",
            "04_requirement",
            "CA-R-004--incompatible.md",
            carrier("CA-R-004", relations="\n  incompatible_with:\n    - CA-R-005"),
        )
        self.write("003_PROJECT_CONFIGURATION", "04_requirement", "CA-R-005--other.md", carrier("CA-R-005"))
        self.write(
            "001_CORE_META_MODEL",
            "05_method",
            "CA-M-001--priority-a.md",
            carrier("CA-M-001", extra="applicable_methodology_priority_group: group-one\npriority: 10\n"),
        )
        self.write(
            "003_PROJECT_CONFIGURATION",
            "05_method",
            "CA-M-002--priority-b.md",
            carrier("CA-M-002", extra="applicable_methodology_priority_group: group-one\npriority: 20\n"),
        )
        self.write("001_CORE_META_MODEL", "06_evaluation", "SHARED--collision.md", carrier("CA-E-001"))
        self.write("003_PROJECT_CONFIGURATION", "06_evaluation", "SHARED--collision.md", carrier("CA-E-002"))

        code, report = self.invoke()
        self.assertEqual(code, 2)
        self.assertEqual(
            {item["type"] for item in report["conflicts"]},
            {
                "duplicate_selected_atom_identity",
                "unresolved_replacement",
                "incompatible_retained_candidates",
                "unresolved_priority",
                "output_path_collision",
            },
        )

    def test_drafts_archives_cap_and_implementation_are_excluded(self) -> None:
        active = self.write(
            "001_CORE_META_MODEL",
            "09_operations",
            "CA-O-001-OPERATIONS--active.md",
            carrier("CA-O-001"),
        )
        drafts = self.source / "001_CORE_META_MODEL/04_requirement/drafts"
        archive = self.source / "001_CORE_META_MODEL/04_requirement/archive"
        drafts.mkdir()
        archive.mkdir()
        (drafts / "CA-R--draft.md").write_bytes(carrier("CA-R-DRAFT"))
        (archive / "CA-R-001--old@1.md").write_bytes(carrier("CA-R-OLD"))
        (self.source / "001_CORE_META_MODEL/01_concern").mkdir()
        (self.source / "001_CORE_META_MODEL/01_concern/CA-C-001.md").write_bytes(carrier("CA-C-001"))
        (self.source / "001_CORE_META_MODEL/08_implementation").mkdir()
        (self.source / "001_CORE_META_MODEL/08_implementation/CA-I-001.md").write_bytes(carrier("CA-I-001"))
        code, report = self.invoke()
        self.assertEqual(code, 0)
        self.assertEqual(report["eligible_candidate_count"], 1)
        self.assertEqual(report["output_plan"][0]["source_carrier_path"], active.relative_to(self.temp).as_posix())

    def test_failed_multi_directory_swap_rolls_back(self) -> None:
        self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001--one.md", carrier("CA-R-001"))
        self.write("001_CORE_META_MODEL", "05_method", "CA-M-001--two.md", carrier("CA-M-001"))
        code, _ = self.invoke("--apply")
        self.assertEqual(code, 0)
        output = self.temp / module.OUTPUT_RELATIVE
        before = {path.relative_to(output): path.read_bytes() for path in output.rglob("*.md")}
        _, selected, snapshot = module.compile_report(self.temp)
        staging = module.stage_outputs(self.temp, selected, snapshot)
        real_replace = module.os.replace
        calls = 0

        def fail_once(source: Path, target: Path) -> None:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("injected")
            real_replace(source, target)

        with mock.patch.object(module.os, "replace", side_effect=fail_once):
            with self.assertRaises(module.CompileError):
                module.replace_outputs_atomically(self.temp, staging)
        after = {path.relative_to(output): path.read_bytes() for path in output.rglob("*.md")}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
