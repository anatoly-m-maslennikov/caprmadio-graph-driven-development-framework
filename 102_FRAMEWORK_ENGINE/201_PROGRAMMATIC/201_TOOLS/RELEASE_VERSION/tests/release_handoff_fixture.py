"""Disposable local evidence and independent D566 byte/checksum oracle.

The tiny declared Framework is a test fixture, never repository release,
compiler, installation, full-suite or candidate-image execution proof.
"""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
from pathlib import Path


DOCKERFILE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile"
CANONICAL_SOURCE = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"
MATERIALIZED = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/_release_materialized"
COMPILER = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py"


def digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")


def independent_checksum(manifest: dict) -> str:
    normalized = copy.deepcopy(manifest)
    normalized.pop("sha256", None)
    normalized["source_inventory_rows"].sort(
        key=lambda row: (row["destination_path"], row["source_path"], row["source_sha256"])
    )
    return digest(canonical_bytes(normalized))


def reseal(manifest: dict) -> dict:
    result = copy.deepcopy(manifest)
    result["sha256"] = independent_checksum(result)
    return result


def tree_records(root: Path) -> list[dict]:
    return [
        {
            "path": path.relative_to(root).as_posix(),
            "sha256": digest(path.read_bytes()),
            "mode": path.stat().st_mode & 0o777,
        }
        for path in sorted(root.rglob("*"))
        if path.is_file()
    ]


def independent_tree_digest(files: dict[str, bytes]) -> str:
    accumulator = hashlib.sha256()
    for relative, content in sorted(files.items()):
        name = relative.encode("utf-8")
        accumulator.update(len(name).to_bytes(8, "big"))
        accumulator.update(name)
        accumulator.update(len(content).to_bytes(8, "big"))
        accumulator.update(content)
    return accumulator.hexdigest()


def observed_tree_digest(root: Path) -> str:
    return independent_tree_digest({
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in root.rglob("*") if path.is_file()
    })


class ReleaseFixture:
    """Actual local source bytes, observed modes and prior selection fixtures."""

    def __init__(self, root: Path) -> None:
        root = root.resolve(strict=True)
        self.root = root
        inventory = (
            ("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", 0o755),
            ("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/worker.py", "FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/worker.py", 0o644),
            ("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py", "FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py", 0o644),
            ("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/run.md", "FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/run.md", 0o644),
            ("IMAGE_INPUT", DOCKERFILE, "IMAGE_INPUT/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile", 0o644),
            ("METHODOLOGY", f"{CANONICAL_SOURCE}/core-λ.md", "METHODOLOGY/sources/core-λ.md", 0o644),
            ("SKILL", "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md", "SKILLS/ca/SKILL.md", 0o644),
            ("SKILL", "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml", "SKILLS/ca/agents/openai.yaml", 0o644),
            ("SKILL", "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/references/usage.md", "SKILLS/ca/references/usage.md", 0o600),
        )
        self.rows = []
        for resource, source, destination, mode in inventory:
            path = self.write(source, f"fixture source: {source}\n".encode("utf-8"), mode)
            self.rows.append({
                "resource": resource,
                "source_path": source,
                "source_sha256": digest(path.read_bytes()),
                "source_mode": path.stat().st_mode & 0o777,
                "destination_path": destination,
            })
        self.structure = self.write(".caprmedio_caprmedio/project_structure.toml", b"[paths]\ncontrol_root = '.caprmedio_caprmedio'\n")
        settings_relative = f"{CANONICAL_SOURCE}/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml"
        self.settings = self.write(settings_relative, b"release_policy = 'sealed'\n")
        compiler = self.write(COMPILER, b"# declared compiler fixture, never invoked\n", 0o755)
        for resource, path, destination in (
            ("METHODOLOGY", self.settings, "METHODOLOGY/sources/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml"),
            ("FRAMEWORK_ENGINE", compiler, "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py"),
        ):
            self.rows.append({"resource": resource, "source_path": path.relative_to(root).as_posix(), "source_sha256": digest(path.read_bytes()), "source_mode": path.stat().st_mode & 0o777, "destination_path": destination})
        self.selection = self.write(".caprmedio_runtime/framework/current.toml", b"release = 'N'\n")
        self.write(".agents/skills/ca/SKILL.md", b"# prior N skill\n")
        self.write(".caprmedio_runtime/journal/evidence.jsonl", b'{"prior":"N"}\n')
        self.frontier = observed_tree_digest(root / CANONICAL_SOURCE)
        self.nested_digest = self.frontier
        self.source_digest = self.frontier
        self.compiled_payload = b"# source-bound compiled Methodology\n"
        self.manifest = reseal({
            "schema": "caprmedio.release_version.candidate.v2",
            "executing_release": "N",
            "candidate_release": "N+1",
            "canonical_source_snapshot_ref": CANONICAL_SOURCE,
            "canonical_source_snapshot_digest": self.source_digest,
            "project_structure_digest": digest(self.structure.read_bytes()),
            "framework_settings_digest": digest(self.settings.read_bytes()),
            "source_frontier_digest": self.frontier,
            "nested_source_recursive_sha256_before": self.nested_digest,
            "expected_derived_source_copy_sha256": self.source_digest,
            "expected_compiled_output_sha256": independent_tree_digest({"compiled.md": self.compiled_payload}),
            "full_suite_environment": {"runner": "declared-full-suite", "command": ["/opt/venv/bin/python", "-m", "unittest", "discover"], "working_directory": "."},
            "skill_target": ".agents/skills/ca",
            "candidate_image": {"dockerfile_path": DOCKERFILE, "dockerfile_sha256": digest((root / DOCKERFILE).read_bytes()), "candidate_image_reference": "candidate:N+1"},
            "source_inventory_rows": self.rows,
        })
        self.request = {
            "schema": "caprmedio.release_version.v1", "operation": "prepare", "project_root": ".",
            "candidateSnapshotManifest": self.manifest,
            "expected_executing_release": "N",
            "expected_project_structure_digest": self.manifest["project_structure_digest"],
            "expected_framework_settings_digest": self.manifest["framework_settings_digest"],
            "expected_source_frontier_digest": self.frontier,
            "run_receipt_refs": ["workflow-run:selected-release", "action-run:prepare"],
        }
        self.intent = {key: self.manifest[key] for key in (
            "candidate_release", "expected_derived_source_copy_sha256", "expected_compiled_output_sha256", "full_suite_environment",
        )}
        self.intent["candidate_image_reference"] = self.manifest["candidate_image"]["candidate_image_reference"]

    def write(self, relative: str, content: bytes, mode: int = 0o644) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        path.chmod(mode)
        return path

    def snapshot(self) -> dict[str, tuple[bytes, int]]:
        return {
            path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
            for path in self.root.rglob("*") if path.is_file()
        }

    def deliver_copy(self) -> Path:
        destination = self.root / "101_LAYER_1_FRAMEWORK_METHODOLOGY/sources"
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(self.root / CANONICAL_SOURCE, destination)
        return destination

    def materialize_bytes(self, candidate_sha256: str) -> Path:
        """Create only simulated output bytes, never compiler-success evidence."""
        relative = f"{MATERIALIZED}/{candidate_sha256}/compiled.md"
        return self.write(relative, self.compiled_payload).parent
