"""Disposable real-compiler fixture for Framework initialization tests.

The fixture writes a small, conflict-free Methodology source tree and derives
its compiled carriers through the compiler's read-only report and projection
renderer.  It never invokes the compiler Action or a runtime publisher.
"""

from __future__ import annotations

import os
import shutil
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
COMPILER_ROOT = RELEASE_ROOT.parent / "COMPILE_APPLICABLE_METHODOLOGY"
if str(COMPILER_ROOT) not in sys.path:
    sys.path.insert(0, str(COMPILER_ROOT))

import compile_applicable_methodology as compiler  # noqa: E402


def source_atom(atom_id: str, *, version: int = 1, summary: str | None = None) -> bytes:
    """Return the smallest active source Atom accepted by the real compiler."""

    claim = summary or f"{atom_id} is a current compiler fixture."
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "status: Active\n"
        f"version: {version}\n"
        "updated_at: 2026-10-06 00:00:00 +0000\n"
        "relations: {}\n"
        "---\n"
        "# Summary\n\n"
        f"{claim}\n"
    ).encode("utf-8")


@dataclass
class ConfiguredCompilerFixture:
    """A retained Project whose compiled tree is a real pure reconstruction."""

    root: Path
    source: Path
    output: Path

    @classmethod
    def create(cls, *, output_relative: Path | None = None) -> "ConfiguredCompilerFixture":
        """Materialize one fixture with an optionally configured output root."""

        base = Path.cwd() / ".caprmedio_tmp/framework-compiler-currentness"
        base.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(prefix="case-", dir=base)).resolve()
        source = root / compiler.SOURCE_RELATIVE
        configured_output = output_relative or compiler.OUTPUT_RELATIVE
        output = root / configured_output
        for _layer, directory, _order, _required in compiler.LAYERS:
            (source / directory).mkdir(parents=True)
        (source / "002_INSTALLED_EXTENSIONS/.gitkeep").write_text("", encoding="utf-8")
        for layer in ("001_CORE_META_MODEL", "003_PROJECT_CONFIGURATION"):
            for _role, role_directory in compiler.ROLES:
                (source / layer / role_directory).mkdir()
        structure = root / compiler.STRUCTURE_RELATIVE
        structure.parent.mkdir(parents=True, exist_ok=True)
        structure.write_text(
            "[[scope_units]]\n"
            'scope_unit_name = "METHODOLOGY_SOURCES"\n'
            f"authority_path = {compiler.SOURCE_RELATIVE.as_posix()!r}\n"
            f"delivery_path = {configured_output.as_posix()!r}\n",
            encoding="utf-8",
        )
        settings = root / compiler.SETTINGS_PATH
        settings.parent.mkdir(parents=True, exist_ok=True)
        settings.write_text('[paths]\ncontrol_root = ".caprmedio_caprmedio"\n', encoding="utf-8")
        compiler_entrypoint = root / (
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/"
            "COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py"
        )
        compiler_entrypoint.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(COMPILER_ROOT / "compile_applicable_methodology.py", compiler_entrypoint)
        # The package-plan regression cases exercise the read-only complete
        # inventory boundary.  These two regular, hook-free carriers are the
        # smallest valid project-local ca Skill payload; no image proof or
        # installation Action is involved.
        skill_root = root / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca"
        (skill_root / "agents").mkdir(parents=True, exist_ok=True)
        (skill_root / "SKILL.md").write_text("# ca\n", encoding="utf-8")
        (skill_root / "agents/openai.yaml").write_text("name: ca\n", encoding="utf-8")
        fixture = cls(root=root, source=source, output=output)
        fixture.write_source("001_CORE_META_MODEL", "04_requirement", "CA-R-001--foundation.md", source_atom("CA-R-001"))
        fixture.write_source("003_PROJECT_CONFIGURATION", "05_method", "CA-M-001--method.md", source_atom("CA-M-001"))
        fixture.materialize_current_projection()
        return fixture

    def write_source(self, layer: str, role_directory: str, name: str, payload: bytes) -> Path:
        target = self.source / layer / role_directory / name
        target.write_bytes(payload)
        return target

    def materialize_current_projection(self) -> dict[str, object]:
        """Render all selected candidates without calling compiler publication."""

        places = compiler.methodology_paths(self.root)
        report, candidates, _snapshot = compiler.compile_report(self.root, places)
        if not report["can_apply"]:
            raise AssertionError(f"fixture source must be conflict-free: {report}")
        for _role, role_directory in compiler.ROLES:
            (self.output / role_directory).mkdir(parents=True, exist_ok=True)
        for candidate in candidates:
            source = self.root / candidate.source_path
            destination_parent = self.output / candidate.role_directory
            source_relative = Path(os.path.relpath(source, start=destination_parent)).as_posix()
            (destination_parent / candidate.basename).write_bytes(
                compiler.projection_bytes(source.read_bytes(), source_relative, candidate)
            )
        return report

    def output_carrier(self, role_directory: str, name: str) -> Path:
        return self.output / role_directory / name
