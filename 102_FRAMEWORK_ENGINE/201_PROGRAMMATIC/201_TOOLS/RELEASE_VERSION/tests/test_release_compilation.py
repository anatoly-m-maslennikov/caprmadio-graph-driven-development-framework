"""Golden child-only Release compiler tests using disposable local projects."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_compilation import (  # noqa: E402
    CHILD_MANIFEST_NAME,
    EXECUTING_COMPILER_PATH,
    build_preflight_validated_candidate,
    preflight_release_compilation,
    render_release_candidate,
)
from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE, MATERIALIZED_RELATIVE, tree_sha256  # noqa: E402


def carrier(atom_id: str, *, version: int = 1) -> bytes:
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: obligation\n"
        "status: Active\n"
        f"version: {version}\n"
        "updated_at: 2026-10-05 00:00:00 +0000\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\nclaim\n"
    ).encode()


class ReleaseCompilationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve(strict=True)
        self.control = self.root / ".caprmedio_caprmedio"
        self.source = self.root / CANONICAL_SOURCE_RELATIVE
        for layer in ("001_CORE_META_MODEL", "003_PROJECT_CONFIGURATION"):
            for role in ("04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations"):
                (self.source / layer / role).mkdir(parents=True, exist_ok=True)
        (self.source / "002_INSTALLED_EXTENSIONS").mkdir(parents=True)
        self.write(".caprmedio_caprmedio/project_structure.toml", (
            "[[scope_units]]\n"
            'scope_unit_name = "METHODOLOGY_SOURCES"\n'
            f'authority_path = "{CANONICAL_SOURCE_RELATIVE}"\n'
        ).encode())
        self.write(".caprmedio_caprmedio/caprmedio_project_settings.toml", b'[paths]\ncontrol_root = ".caprmedio_caprmedio"\n')
        self.write(f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml", b"")
        self.write(f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml", b"")
        self.write(".caprmedio_runtime/framework/current.toml", b'release = "N"\n')
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool\n", 0o755)
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py", b"app\n")
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py", b"mcp\n")
        self.write("102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md", b"prompt\n")
        self.write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md", b"# ca\n")
        self.write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml", b"name: ca\n")
        self.write("pyproject.toml", b"[project]\nname = 'fixture'\n")
        self.write("uv.lock", b"version = 1\n")
        self.write(
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile",
            b"FROM scratch\nCOPY pyproject.toml uv.lock ./\n",
        )
        self.compiler = self.write(
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py",
            EXECUTING_COMPILER_PATH.read_bytes(),
            0o755,
        )
        self.core = self.write(f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))

    def write(self, relative: str, data: bytes, mode: int = 0o644) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        path.chmod(mode)
        return path

    def copy_source(self) -> Path:
        target = self.root / "101_LAYER_1_FRAMEWORK_METHODOLOGY/sources"
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(self.source, target)
        return target

    def snapshot(self) -> dict[str, bytes]:
        return {path.relative_to(self.root).as_posix(): path.read_bytes() for path in self.root.rglob("*") if path.is_file()}

    def build(self):
        return build_preflight_validated_candidate(
            self.root,
            candidate_release="N+1",
            full_suite_environment={"runner": "fixture", "command": ["python", "-m", "unittest"], "working_directory": "."},
            candidate_image_reference="fixture:N+1",
        )

    def test_actual_child_renderer_matches_preflight_and_preserves_canonical_carriers(self) -> None:
        before = self.snapshot()
        preflight, candidate = self.build()
        self.assertEqual(preflight.expected_derived_source_copy_sha256, tree_sha256(self.root, self.source))
        self.assertEqual(candidate.manifest.source_frontier_digest, preflight.compiler_frontier_digest)
        self.assertNotEqual(candidate.manifest.source_frontier_digest, candidate.manifest.canonical_source_snapshot_digest)
        self.copy_source()
        handoff = render_release_candidate(candidate, preflight)
        child = self.root / MATERIALIZED_RELATIVE / candidate.manifest.sha256
        self.assertEqual(handoff.actual_compiled_output_sha256, preflight.expected_compiled_output_sha256)
        self.assertEqual(handoff.compiler_frontier_digest, preflight.compiler_frontier_digest)
        self.assertTrue((child / CHILD_MANIFEST_NAME).is_file())
        self.assertNotIn(candidate.manifest.sha256.encode(), (child / CHILD_MANIFEST_NAME).read_bytes())
        self.assertFalse((self.control / "_projection/APPLICABLE_METHODOLOGY").exists())
        for relative, data in before.items():
            if relative.startswith("101_LAYER_1_FRAMEWORK_METHODOLOGY/"):
                continue
            self.assertEqual((self.root / relative).read_bytes(), data)

    def test_preflight_is_deterministic_and_placeholder_component_does_not_change_bytes(self) -> None:
        first = preflight_release_compilation(self.root, candidate_release="N+1")
        second = preflight_release_compilation(self.root, candidate_release="N+1")
        self.assertEqual(first, second)
        self.assertTrue(first.expected_compiled_output_sha256)

    def test_stale_source_and_compilation_conflict_refuse_without_canonical_projection_write(self) -> None:
        preflight, candidate = self.build()
        self.copy_source()
        original = self.core.read_bytes()
        self.core.write_bytes(original + b"changed\n")
        with self.assertRaises(ReleaseContractError) as stale:
            render_release_candidate(candidate, preflight)
        self.assertEqual(stale.exception.code, "release-currentness-stale")
        self.core.write_bytes(original)
        duplicate = self.write(f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/04_requirement/CA-R-001--duplicate.md", carrier("CA-R-001"))
        with self.assertRaises(ReleaseContractError) as conflict:
            preflight_release_compilation(self.root, candidate_release="N+1")
        self.assertEqual(conflict.exception.code, "release-compiler-blocked")
        duplicate.unlink()
        self.assertFalse((self.control / "_projection/APPLICABLE_METHODOLOGY").exists())

    def test_declared_stub_compiler_and_symlinked_materialization_parent_refuse_before_write(self) -> None:
        self.compiler.write_bytes(b"# different compiler bytes\n")
        with self.assertRaises(ReleaseContractError) as identity:
            self.build()
        self.assertEqual(identity.exception.code, "release-compiler-identity-mismatch")
        self.compiler.write_bytes(EXECUTING_COMPILER_PATH.read_bytes())
        preflight, candidate = self.build()
        self.copy_source()
        escaped = self.root / "escape"
        escaped.mkdir()
        materialized = self.root / MATERIALIZED_RELATIVE
        materialized.symlink_to(escaped, target_is_directory=True)
        with self.assertRaises(ReleaseContractError) as unsafe:
            render_release_candidate(candidate, preflight)
        self.assertEqual(unsafe.exception.code, "release-materialization-path-unsafe")
        self.assertEqual(list(escaped.iterdir()), [])

    def test_forged_compiler_frontier_refuses_before_child_render(self) -> None:
        preflight, candidate = self.build()
        self.copy_source()
        forged = replace(
            candidate,
            authority=candidate.authority.model_copy(update={"source_frontier_digest": "0" * 64}),
        )
        with self.assertRaises(ReleaseContractError) as rejected:
            render_release_candidate(forged, preflight)
        self.assertEqual(rejected.exception.code, "release-currentness-stale")
        child = self.root / MATERIALIZED_RELATIVE / candidate.manifest.sha256
        self.assertFalse(child.exists())


if __name__ == "__main__":
    unittest.main()
