"""Disposable, source-pinned corpus for selected Workflow Docker evidence.

The corpus is deliberately only a harness input.  It copies the reviewed
manifest and its exact source pins into a throw-away Git Project; it never
points a Docker worker at this repository's authority or an existing Run.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import shutil
from typing import Any, Iterable, Mapping


MANIFEST_REF = ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json"
BASE_REVISE_BINDINGS_REF = (
    "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/"
    "RMED_ATOM_REVIEW/source_bindings.json"
)
ROUTE_CASES = (
    ("W01", "create_atom"),
    ("W02", "update_atom"),
    ("W03", "replace_atom"),
    ("W04", "change_atom_status"),
    ("W05", "create_scope_unit"),
    ("W06", "rename_scope_unit"),
    ("W07", "move_scope_unit"),
    ("W08", "remove_scope_unit"),
    ("W09", "run_implementation_workflow"),
    ("W10", "revert_changes"),
    ("W11", "build_entities_graph"),
    ("W12", "build_terms_graph"),
    ("W13", "build_applicable_methodology"),
)
JOURNAL_CASES = tuple(f"J{number:02d}" for number in range(1, 9))


class GoldenCorpusError(RuntimeError):
    """The selected-route delivery has not supplied a runnable frozen corpus."""


def canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value: object) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def file_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _safe_relative(value: object, *, name: str) -> Path:
    if not isinstance(value, str) or not value:
        raise GoldenCorpusError(f"{name} must be a non-empty repository-relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise GoldenCorpusError(f"{name} escapes the disposable fixture")
    return path


def _pin_paths(route: Mapping[str, Any]) -> Iterable[Mapping[str, Any]]:
    yield route["workflow"]
    for item in route["ordered_steps"]:
        yield item["step"]
        yield item["action"]
    yield from route["ordered_actions"]
    yield from route["native_action_calls"]


@dataclass(frozen=True)
class GoldenCase:
    case_id: str
    route: str

    @property
    def authority_path(self) -> str:
        return f"fixture/authority/{self.case_id}.json"

    @property
    def expected_effect_path(self) -> str:
        return f"fixture/effects/{self.case_id}.json"


@dataclass(frozen=True)
class FixtureLease:
    """A scoped fixture path, with an explicit evidence-retention escape hatch."""

    root: Path

    def cleanup(self) -> None:
        # macOS managed workspaces can deny deletion of a just-unmounted bind
        # directory.  Retaining the scoped path is preferable to reporting a
        # slow/failed deletion as route evidence; operators may set this only
        # while diagnosing Docker failures.
        if os.environ.get("CAPRMEDIO_KEEP_DOCKER_FIXTURES") == "1":
            return
        shutil.rmtree(self.root, ignore_errors=True)


class GoldenProject:
    """One fresh, source-pinned Project per Docker/MCP case."""

    def __init__(self, source_root: Path, root: Path, case: GoldenCase) -> None:
        self.source_root = Path(source_root).resolve(strict=True)
        self.root = Path(root).resolve(strict=True)
        self.case = case
        self.manifest: dict[str, Any] | None = None

    @property
    def manifest_path(self) -> Path:
        return self.root / MANIFEST_REF

    def prepare(self) -> dict[str, Any]:
        """Create the only Project a harness may mutate, then freeze its pins."""
        (self.root / ".caprmedio_caprmedio").mkdir(parents=True, exist_ok=True)
        (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            "[paths]\n"
            'control_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        (self.root / ".caprmedio_caprmedio/operators_registry.toml").write_text(
            '[[operators]]\nname = "golden-operator"\nrole = "project owner"\n',
            encoding="utf-8",
        )
        (self.root / "fixture/authority").mkdir(parents=True, exist_ok=True)
        (self.root / self.case.authority_path).write_text(
            json.dumps({"case": self.case.case_id, "route": self.case.route, "state": "before"}),
            encoding="utf-8",
        )
        # Runtime admission intentionally requires the Project Git authority
        # mount to be a real directory.  A bare fixture marker is enough for
        # these mock-only evidence cases and avoids a host Git repository that
        # Docker can make non-removable on macOS file-sharing backends.
        (self.root / ".git").mkdir()
        self._copy_runtime_readiness_definition()
        manifest = self._copy_reviewed_manifest()
        self.manifest = manifest
        return manifest

    def _copy_runtime_readiness_definition(self) -> None:
        """Keep the existing worker's unrelated readiness fingerprint satisfiable.

        The selected suite does not exercise Base Revise, but the already
        deployed Docker worker fingerprints CA-O-104 before it advertises
        readiness.  Copying its one pinned definition permits a disposable
        selected-route runtime without borrowing any real Project authority.
        """
        bindings = self.source_root / BASE_REVISE_BINDINGS_REF
        try:
            value = json.loads(bindings.read_text(encoding="utf-8"))
            definition = next(
                row for row in value["sources"] if row.get("atom_id") == "CA-O-104"
            )
        except (OSError, ValueError, KeyError, StopIteration, TypeError) as error:
            raise GoldenCorpusError("existing Docker worker has no readable CA-O-104 readiness binding") from error
        self._copy_pinned(
            _safe_relative(definition.get("path"), name="Base Revise readiness source"),
            definition.get("sha256"),
        )

    def _copy_reviewed_manifest(self) -> dict[str, Any]:
        source_manifest = self.source_root / MANIFEST_REF
        if not source_manifest.is_file():
            raise GoldenCorpusError(
                "missing selected_workflow_bindings.json; no selected Docker route may claim a pass"
            )
        try:
            manifest = json.loads(source_manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise GoldenCorpusError("selected workflow manifest is not JSON") from error
        if not isinstance(manifest, dict) or not isinstance(manifest.get("routes"), list):
            raise GoldenCorpusError("selected workflow manifest does not contain a route list")
        actual_routes = tuple(item.get("route") for item in manifest["routes"] if isinstance(item, dict))
        expected_routes = tuple(route for _, route in ROUTE_CASES)
        if actual_routes != expected_routes:
            raise GoldenCorpusError("selected workflow manifest is not the exact W01--W13 route portfolio")
        freshness = manifest.get("source_freshness")
        if not isinstance(freshness, dict):
            raise GoldenCorpusError("selected workflow manifest omits source freshness")
        registry = _safe_relative(freshness.get("selected_source_registry_ref"), name="source registry")
        self._copy_pinned(registry, freshness.get("selected_source_registry_digest"))
        copied: set[Path] = {registry}
        for route in manifest["routes"]:
            if not isinstance(route, Mapping):
                raise GoldenCorpusError("selected workflow route is malformed")
            for pin in _pin_paths(route):
                if not isinstance(pin, Mapping):
                    raise GoldenCorpusError("selected workflow source pin is malformed")
                relative = _safe_relative(pin.get("source_path"), name="source pin")
                if relative not in copied:
                    self._copy_pinned(relative, pin.get("digest"))
                    copied.add(relative)
        self.manifest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_manifest, self.manifest_path)
        if file_digest(self.manifest_path) != file_digest(source_manifest):
            raise GoldenCorpusError("manifest copy did not preserve canonical bytes")
        return manifest

    def _copy_pinned(self, relative: Path, expected_digest: object) -> None:
        if not isinstance(expected_digest, str) or len(expected_digest) != 64:
            raise GoldenCorpusError(f"{relative.as_posix()} has no SHA-256 pin")
        source = self.source_root / relative
        if not source.is_file() or file_digest(source) != expected_digest:
            raise GoldenCorpusError(f"source pin is unavailable or stale: {relative.as_posix()}")
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        if file_digest(target) != expected_digest:
            raise GoldenCorpusError(f"fixture copy changed source pin: {relative.as_posix()}")

    def snapshot(self) -> dict[str, str]:
        """Hash only admitted mutable fixture files; mounts/code are not evidence."""
        files = list((self.root / ".caprmedio_caprmedio").rglob("*")) + list((self.root / "fixture").rglob("*"))
        return {
            path.relative_to(self.root).as_posix(): file_digest(path)
            for path in files
            if path.is_file() and not {"_journal", "_projection"}.intersection(path.relative_to(self.root).parts)
        }

    def request(self, *, request_id: str, mode: str = "preview", receipt: object | None = None,
                receipt_digest: object | None = None) -> dict[str, Any]:
        if self.manifest is None:
            raise GoldenCorpusError("prepare the golden Project before creating a request")
        route = self.case.route
        parameters = {
            "fixture_schema": "selected-workflows-docker-golden/v1",
            "case_id": self.case.case_id,
            "route": route,
            "authority_path": self.case.authority_path,
            "expected_effect_path": self.case.expected_effect_path,
        }
        refs = [self.case.authority_path]
        effects = [{"type": route, "target": self.case.expected_effect_path}]
        request: dict[str, Any] = {
            "operation_route": route,
            "mode": mode,
            "request_id": request_id,
            "parameters": parameters,
            "parameters_digest": digest(parameters),
            "target_frontier": {"refs": refs, "target_frontier_digest": digest(refs)},
            "effects": {"descriptors": effects, "effects_digest": digest(effects)},
            "definition_manifest": {
                "manifest_ref": MANIFEST_REF,
                "manifest_digest": self.manifest["canonical_manifest_sha256"],
            },
            "source_freshness": dict(self.manifest["source_freshness"]),
            "initiative": {
                "initiative_id": f"golden-{self.case.case_id}",
                "instruction_summary": f"Disposable golden {self.case.case_id}",
                "reference": "fixture/initiative.json",
                "sealed": True,
            },
        }
        if mode == "execute":
            request.update(
                proposal_receipt=receipt,
                proposal_receipt_digest=receipt_digest,
                assigned_action_id=f"golden-{self.case.case_id}-action",
                requested_run_ids={
                    "workflow_run_id": request_id,
                    "action_run_ids": [f"{request_id}:action"],
                },
            )
            request["operator_authorization"] = {
                "reference": "fixture/operator-authorization.json",
                "sealed": True,
                "request_id": request_id,
                "operation_route": route,
                "proposal_receipt_digest": receipt_digest,
                "parameters_digest": request["parameters_digest"],
                "target_frontier_digest": request["target_frontier"]["target_frontier_digest"],
                "effects_digest": request["effects"]["effects_digest"],
                "definition_manifest": request["definition_manifest"],
                "source_freshness": request["source_freshness"],
            }
        return request

    def corrupt_one_bound_source(self) -> Path:
        """Create a deliberate currentness conflict after all clean hashes are saved."""
        if self.manifest is None:
            raise GoldenCorpusError("prepare the golden Project before corrupting a source")
        route = next(item for item in self.manifest["routes"] if item["route"] == self.case.route)
        source = self.root / _safe_relative(route["workflow"]["source_path"], name="workflow source pin")
        source.write_text(source.read_text(encoding="utf-8") + "\n<!-- stale-fixture -->\n", encoding="utf-8")
        return source
