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
            'runtime_root = ".caprmedio_runtime"\n\n'
            "[authority_modes]\n"
            'default = "casual"\n',
            encoding="utf-8",
        )
        (self.root / ".caprmedio_caprmedio/operators_registry.toml").write_text(
            '[[operators]]\nname = "golden-operator"\nrole = "project owner"\n',
            encoding="utf-8",
        )
        self._write_native_authority()
        self._write_graph_authority()
        self._write_compiler_authority()
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

    @property
    def _authority_dir(self) -> Path:
        # Atom discovery uses the registered content-role directory convention.
        return self.root / ".caprmedio_caprmedio/04_requirement"

    @staticmethod
    def _status_model() -> dict[str, Any]:
        """The registered Requirement status model carried by W03/W04."""
        return {
            "model_ref": "fixture://requirement-statuses",
            "model_revision": "1",
            "content_role": "Requirement",
            "statuses": ["Active", "Reviewed", "Archived"],
            "transitions": {"Active": ["Reviewed", "Archived"],
                            "Reviewed": ["Active", "Archived"]},
            "archive_status": "Archived",
        }

    def _write_atom(self, atom_id: str, slug: str, summary: str) -> Path:
        path = self._authority_dir / f"{atom_id}--{slug}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "---\n"
            f"atom_id: {atom_id}\ncontent_role: Requirement\nstatus: Active\nversion: 1\n"
            "updated_at: 2026-10-05 00:00:00 +0000\nrelations: {}\n---\n"
            f"# Summary\n\n{summary}\n\n## Scope\n\nFixture scope.\n\n## Claim\n\nFixture claim.\n",
            encoding="utf-8",
        )
        return path

    def _write_native_authority(self) -> None:
        """Create real disposable carriers and structure authority for W01--W08.

        These are deliberately ordinary Project files, rather than a test-only
        request schema: the native Action adapters validate them directly.
        """
        self._write_atom("CA-R-100", "target", "Stable summary")
        self._write_atom("CA-R-101", "related", "Related summary")
        control = self.root / ".caprmedio_caprmedio"
        # Canonical serializer output is not required by the adapter; this is
        # the minimal valid Project Structure source it parses and rewrites.
        (control / "project_structure.toml").write_text(
            "[[scope_units]]\n"
            'scope_unit_name = "PARENT"\nparent = "PROJECT"\nscope_unit_type = "Ordered"\n'
            'scope_unit_label = "LAYER"\nstructural_level = 1\nlocal_order = 1\n'
            'navigational_order_number = 0\nauthority_path = ".caprmedio_caprmedio/PARENT"\n'
            'delivery_path = "delivery/PARENT"\n\n'
            "[[scope_units]]\n"
            'scope_unit_name = "CHILD"\nparent = "PARENT"\nscope_unit_type = "Unordered"\n'
            'scope_unit_label = "FEATURE"\nstructural_level = 2\n'
            'navigational_order_number = 0\nauthority_path = ".caprmedio_caprmedio/CHILD"\n'
            'delivery_path = "delivery/CHILD"\n\n'
            "[[scope_units]]\n"
            'scope_unit_name = "DEST"\nparent = "PROJECT"\nscope_unit_type = "Unordered"\n'
            'scope_unit_label = "LAYER"\nstructural_level = 1\n'
            'navigational_order_number = 1\nauthority_path = ".caprmedio_caprmedio/DEST"\n'
            'delivery_path = "delivery/DEST"\n',
            encoding="utf-8",
        )
        (self.root / "fixture/reference.txt").parent.mkdir(parents=True, exist_ok=True)
        (self.root / "fixture/reference.txt").write_text("CHILD\n", encoding="utf-8")

    @property
    def graph_source_dir(self) -> Path:
        """The explicit selected source folder for the two graph Actions."""
        return self.root / ".caprmedio_caprmedio/graph_sources"

    def _write_graph_authority(self) -> None:
        """Declare a minimal current Entity/Term frontier, never a graph fake."""
        self.graph_source_dir.mkdir(parents=True, exist_ok=True)
        def atom(atom_id: str, governs: str, depends_on: tuple[str, ...] = ()) -> str:
            dependencies = ", ".join(json.dumps(value) for value in depends_on)
            return (
                "---\n"
                f"atom_id: {atom_id}\ncontent_role: Requirement\ntype: Definition\n"
                "current_scope_unit: PARENT\nclaim_target_scope_unit: PARENT\nstatus: Active\n"
                "author: Golden Fixture\nversion: 1\nupdated_at: 2026-10-05 00:00:00 +0000\n"
                "subjects:\n"
                f"  governs: {json.dumps(governs)}\n  depends_on: [{dependencies}]\n"
                "relations: {}\n---\n"
                f"# {atom_id}\n\nDeclared fixture source.\n"
            )
        (self.graph_source_dir / "CA-R-201.md").write_text(atom("CA-R-201", "Entity"), encoding="utf-8")
        (self.graph_source_dir / "CA-R-202.md").write_text(atom("CA-R-202", "Property", ("Entity",)), encoding="utf-8")
        (self.graph_source_dir / "CA-R-203.md").write_text(
            atom("CA-R-203", "Entity/Property: Label", ("Property",)), encoding="utf-8"
        )

    def native_graph_parameters(self, graph_kind: str) -> dict[str, Any]:
        """Return the actual CA-O-134/O-137 request, with pinned source bytes."""
        if graph_kind not in {"entities", "terms"}:
            raise GoldenCorpusError("graph kind must be entities or terms")
        import sys
        graph_root = Path(__file__).resolve().parents[3] / "201_TOOLS" / "GENERATE_ENTITY_GRAPH"
        if str(graph_root) not in sys.path:
            sys.path.insert(0, str(graph_root))
        import generate_entity_graph
        return {
            "graph_kind": graph_kind,
            "source_frontier": generate_entity_graph.source_frontier_for(self.root, self.graph_source_dir),
            "selection": {"atom_ids": ["CA-R-201", "CA-R-202", "CA-R-203"], "scope_unit_names": ["PARENT"]},
            "representation_configuration": {"format": "canonical-json"},
            "capability_permission_evidence": {"authorized": True},
            "run_recording_context": {"state": "confirmed", "receipt_refs": [f"golden-{self.case.case_id}"]},
        }

    @property
    def compiler_source_dir(self) -> Path:
        return self.root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"

    def _write_compiler_authority(self) -> None:
        """Declare Core, selected Extension, and Project Configuration sources."""
        source = self.compiler_source_dir
        for layer in ("001_CORE_META_MODEL", "003_PROJECT_CONFIGURATION"):
            for role in ("04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations"):
                (source / layer / role).mkdir(parents=True, exist_ok=True)
        def carrier(atom_id: str) -> str:
            return (
                "---\n" + f"atom_id: {atom_id}\ncce_version: cce_1\ncce_form: obligation\n"
                "status: Active\nversion: 1\nupdated_at: 2026-10-05 00:00:00 +0000\nrelations: {}\n---\n"
                f"# {atom_id}\n\nDeclared compiler fixture source.\n"
            )
        (source / "001_CORE_META_MODEL/04_requirement/CA-R-301--core.md").write_text(carrier("CA-R-301"), encoding="utf-8")
        extension = source / "002_INSTALLED_EXTENSIONS/example/v2/05_method"
        extension.mkdir(parents=True, exist_ok=True)
        (extension / "CA-M-302--extension.md").write_text(carrier("CA-M-302"), encoding="utf-8")
        (source / "003_PROJECT_CONFIGURATION/07_delivery/CA-D-303--project.md").write_text(carrier("CA-D-303"), encoding="utf-8")
        (source / "001_CORE_META_MODEL/caprmedio_framework_default_settings.toml").write_text("", encoding="utf-8")
        (source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml").write_text(
            '[extensions.example]\nenabled = true\nrevision = "v2"\n', encoding="utf-8"
        )
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        with structure.open("a", encoding="utf-8") as handle:
            handle.write(
                "\n[[scope_units]]\n"
                'scope_unit_name = "METHODOLOGY_SOURCES"\nparent = "PROJECT"\n'
                'scope_unit_type = "Unordered"\nscope_unit_label = "FEATURE"\nstructural_level = 1\n'
                'navigational_order_number = 2\n'
                'authority_path = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"\n'
                'delivery_path = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"\n'
            )

    def native_compiler_parameters(self, operation: str = "dry_run", *, expected_source_frontier_digest: str | None = None) -> dict[str, Any]:
        """Actual CA-O-011 request; it deliberately has no fabricated receipt."""
        import sys
        compiler_root = Path(__file__).resolve().parents[3] / "201_TOOLS" / "COMPILE_APPLICABLE_METHODOLOGY"
        if str(compiler_root) not in sys.path:
            sys.path.insert(0, str(compiler_root))
        import compile_applicable_methodology
        request: dict[str, Any] = {
            "operation": operation, "project_root": self.root.as_posix(),
            "governed_bindings": compile_applicable_methodology.governed_bindings(
                self.root, compile_applicable_methodology.methodology_paths(self.root)
            ),
        }
        if operation == "apply":
            if not expected_source_frontier_digest:
                raise GoldenCorpusError("compiler apply needs the just-assessed source frontier digest")
            request["expected_source_frontier_digest"] = expected_source_frontier_digest
        return request

    def native_implementation_parameters(self) -> dict[str, Any]:
        """Source-full CA-O-016 packets; mock transport is supplied separately."""
        import sys
        implementation_root = Path(__file__).resolve().parents[4] / "202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW"
        if str(implementation_root) not in sys.path:
            sys.path.insert(0, str(implementation_root))
        import implementation_actions
        bindings = implementation_actions.current_source_bindings()
        methods = [row["path"] for row in bindings if str(row["atom_id"]).startswith("CA-M-")]
        base = {
            "source_bindings": bindings, "permissions": {"allowed": True},
            "method_projection": implementation_actions.prepare_method_projection(methods),
            "requirements_delivery": ["CA-R-1843", "CA-D-544"], "evaluations": ["CA-E-563"],
            "plan_item": {"estimated_minutes": 1}, "handoff_complete": True,
            "golden_e2e": ["disposable executable assertion"], "baseline_command": "python fixture_assertion.py",
            "retry": {"consumed": 0, "limit": 1}, "retained_state": {"transport": "mock-not-live-llm"},
        }
        return {"base_packet": base, "run_visit_limits": {"CA-O-094": 2}, "step_packets": {
            step: {"context": context, "step_marker": step}
            for step, (_action, context) in implementation_actions.ACTION_BY_STEP.items()
        }}

    def _carrier(self, atom_id: str, slug: str, summary: str) -> dict[str, str]:
        return {
            "path": f".caprmedio_caprmedio/04_requirement/{atom_id}--{slug}.md",
            "frontmatter": f"atom_id: {atom_id}\ncontent_role: Requirement\nstatus: Active",
            "content": f"# Summary\n\n{summary}\n\n## Scope\n\nFixture scope.\n",
        }

    def _descriptor(self, atom_id: str) -> dict[str, Any]:
        # Imported lazily so this corpus module remains usable by Docker's
        # harness bootstrap without host implementation imports.
        import sys
        tools_root = Path(__file__).resolve().parents[3] / "201_TOOLS"
        if str(tools_root) not in sys.path:
            sys.path.insert(0, str(tools_root))
        from lifecycle_intents import carrier_descriptor
        return carrier_descriptor(self.root, atom_id)

    def native_parameters(self) -> dict[str, Any]:
        """Return one source-valid native Action payload for W01--W08 only."""
        route = self.case.route
        if route == "run_implementation_workflow":
            return self.native_implementation_parameters()
        if route == "build_applicable_methodology":
            return self.native_compiler_parameters()
        if route == "build_entities_graph":
            return self.native_graph_parameters("entities")
        if route == "build_terms_graph":
            return self.native_graph_parameters("terms")
        target = self._descriptor("CA-R-100")
        if route == "create_atom":
            return {"carrier": self._carrier("CA-R-102", "created", "Created summary")}
        if route == "update_atom":
            path = self.root / target["path"]
            frontmatter, content = path.read_text(encoding="utf-8")[4:].split("\n---\n", 1)
            return {"target": target, "proposed": {"frontmatter": frontmatter,
                    "content": content + "\nCarrier-only fixture detail.\n"}, "change_class": "carrier_only"}
        if route == "replace_atom":
            return {"predecessor": target, "successors": [self._carrier("CA-R-103", "replacement", "Replacement summary")],
                    "status_model": self._status_model()}
        if route == "change_atom_status":
            return {"target": target, "status": "Reviewed", "status_model": self._status_model()}
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        base: dict[str, Any] = {
            "expected_toml_revision": file_digest(structure), "reference_frontier": [],
            "goal_coverage_disposition": {"state": "present", "parent": "PARENT"},
            "preservation_disposition": {"preserved": ["fixture/reference.txt"]},
            "recovery_disposition": {"authorized": True, "boundary": "toml-and-listed-references"},
        }
        def declaration(name: str, parent: str, level: int) -> dict[str, Any]:
            return {"scope_unit_name": name, "parent": parent, "scope_unit_type": "Unordered",
                    "scope_unit_label": "FEATURE", "structural_level": level,
                    "navigational_order_number": 0, "authority_path": f".caprmedio_caprmedio/{name}",
                    "delivery_path": f"delivery/{name}"}
        if route == "create_scope_unit":
            return {**base, "operation": "Create", "declaration": declaration("NEW_CHILD", "PARENT", 2)}
        if route == "rename_scope_unit":
            reference = self.root / "fixture/reference.txt"
            return {**base, "operation": "Rename", "target_name": "CHILD",
                    "declaration": declaration("RENAMED", "PARENT", 2),
                    "reference_frontier": [{"path": "fixture/reference.txt", "expected_sha256": file_digest(reference),
                                            "replacements": [{"old": "CHILD", "new": "RENAMED"}]}]}
        if route == "move_scope_unit":
            return {**base, "operation": "Move", "target_name": "CHILD", "declaration": declaration("CHILD", "DEST", 2),
                    "goal_coverage_disposition": {"state": "present", "parent": "DEST"}}
        if route == "remove_scope_unit":
            return {**base, "operation": "Remove", "target_name": "CHILD"}
        raise GoldenCorpusError(f"native golden parameters are not separately bound for {route}")

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
        # W09--W13 remain the reviewed legacy corpus until their own packets.
        # W01--W08 use precisely the native Action payloads above.
        parameters = self.native_parameters() if self.case.case_id in {
            "W01", "W02", "W03", "W04", "W05", "W06", "W07", "W08", "W09", "W11", "W12", "W13"
        } else {
            "fixture_schema": "selected-workflows-docker-golden/v1", "case_id": self.case.case_id,
            "route": route, "authority_path": self.case.authority_path,
            "expected_effect_path": self.case.expected_effect_path,
        }
        refs = ([".caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY"] if self.case.case_id == "W13"
                else [f".caprmedio_caprmedio/_projection/{'entities_graph.json' if route == 'build_entities_graph' else 'terms_graph.json'}"]
                if self.case.case_id in {"W11", "W12"}
                else [".caprmedio_caprmedio/project_structure.toml"] if self.case.case_id in {"W05", "W06", "W07", "W08"}
                else [str(parameters.get("target", parameters.get("predecessor", parameters.get("carrier", {}))).get("path", self.case.authority_path))])
        effects = [{"type": route, "target": refs[0]}]
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
