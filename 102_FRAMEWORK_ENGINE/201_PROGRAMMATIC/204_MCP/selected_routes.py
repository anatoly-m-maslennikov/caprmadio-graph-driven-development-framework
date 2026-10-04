"""Closed selected-Workflow MCP projection; execution remains in shared support."""
from __future__ import annotations

import hashlib
import importlib
import json
import re
import sys
import tomllib
from pathlib import Path
from typing import Any, Callable, Mapping


DEFAULT_CONTROL_ROOT = Path(".caprmedio_caprmedio")
MANIFEST_FILENAME = "selected_workflow_bindings.json"
PROJECT_SETTINGS_REF = DEFAULT_CONTROL_ROOT / "caprmedio_project_settings.toml"
SELECTED_ROUTE_NAMES = (
    "create_atom", "update_atom", "replace_atom", "change_atom_status",
    "create_scope_unit", "rename_scope_unit", "move_scope_unit", "remove_scope_unit",
    "run_implementation_workflow", "revert_changes", "build_entities_graph",
    "build_terms_graph", "build_applicable_methodology",
)
_DIGEST = re.compile(r"^[0-9a-f]{64}$")
_REQUEST_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
_FRESHNESS_FIELDS = {
    "selected_source_registry_ref", "selected_source_registry_version",
    "selected_source_registry_digest", "selected_binding_ref", "selected_binding_digest",
}


class SelectedRouteError(ValueError):
    """A rejected MCP projection request or stale source binding."""


def canonical_json(value: Any) -> str:
    """RFC 8785-compatible canonical JSON for the closed manifest schema."""
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":"))


def canonical_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _configured_control_root(root: Path) -> Path:
    """Read the Project-local control root, retaining caprmedio as the default."""
    settings_path = root / PROJECT_SETTINGS_REF
    if settings_path.is_symlink():
        raise SelectedRouteError("project settings carrier is unavailable")
    if not settings_path.exists():
        return DEFAULT_CONTROL_ROOT
    if not settings_path.is_file():
        raise SelectedRouteError("project settings carrier is unavailable")
    try:
        settings = tomllib.loads(settings_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise SelectedRouteError("project settings carrier is invalid") from error
    paths = settings.get("paths")
    value = paths.get("control_root") if isinstance(paths, Mapping) else None
    if value is None:
        return DEFAULT_CONTROL_ROOT
    if not isinstance(value, str) or not value:
        raise SelectedRouteError("paths.control_root must be a safe repository-relative path")
    candidate = Path(value)
    if candidate.is_absolute() or candidate == Path(".") or ".." in candidate.parts:
        raise SelectedRouteError("paths.control_root must be a safe repository-relative path")
    resolved = (root / candidate).resolve()
    if root != resolved and root not in resolved.parents:
        raise SelectedRouteError("paths.control_root escapes project root")
    return candidate


def selected_manifest_ref(root: str | Path | None = None) -> str:
    """Return the one derived binding projection for this Project authority root."""
    if root is None:
        control_root = DEFAULT_CONTROL_ROOT
    else:
        project_root = Path(root).resolve(strict=True)
        control_root = _configured_control_root(project_root)
    return (control_root / "_projection" / MANIFEST_FILENAME).as_posix()


def selected_manifest_contract(root: str | Path | None = None) -> dict[str, Any]:
    """Publish the immutable manifest boundary consumed by queue and Docker callers.

    ``load_selected_manifest`` is the only loader: it validates this schema,
    the manifest self-digest, and every live source pin before returning data.
    The returned contract contains no mutable project state.
    """
    return {
        "manifest_ref": selected_manifest_ref(root),
        "schema_version": 1,
        "canonical_digest": {
            "algorithm": "sha256",
            "serialization": "RFC8785",
            "self_field": "canonical_manifest_sha256",
            "self_field_omitted_from_digest": True,
        },
        "outer_fields": ["schema_version", "source_freshness", "routes", "canonical_manifest_sha256"],
        "source_freshness_fields": sorted(_FRESHNESS_FIELDS),
        "route_fields": [
            "route", "workflow", "ordered_steps", "ordered_actions", "native_action_calls",
            "entry_step", "on_result", "mutation_capable",
        ],
        "definition_pin_fields": ["atom_id", "version", "source_path", "digest"],
        "on_result_fields": ["from", "condition", "to"],
        "on_result_terminal_target": "complete",
        "route_names": list(SELECTED_ROUTE_NAMES),
    }


def _safe_path(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or relative.startswith("/") or "\\" in relative:
        raise SelectedRouteError("source_path must be a safe repository-relative path")
    path = (root / relative).resolve()
    if root != path and root not in path.parents:
        raise SelectedRouteError("source_path escapes project root")
    return path


def _frontmatter_value(contents: str, field: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(field)}:\s*[\"']?([^\n\"']+)", contents)
    return match.group(1).strip() if match else None


def _validate_pin(root: Path, pin: Any) -> dict[str, Any]:
    if not isinstance(pin, Mapping) or set(pin) != {"atom_id", "version", "source_path", "digest"}:
        raise SelectedRouteError("definition pin must contain atom_id, version, source_path, and digest")
    atom_id, version, source_path, digest = (pin["atom_id"], pin["version"], pin["source_path"], pin["digest"])
    if not isinstance(atom_id, str) or not atom_id or not isinstance(version, int) or version < 1:
        raise SelectedRouteError("definition pin has invalid identity or version")
    if not isinstance(digest, str) or not _DIGEST.fullmatch(digest):
        raise SelectedRouteError("definition pin has invalid digest")
    path = _safe_path(root, source_path)
    if not path.is_file():
        raise SelectedRouteError(f"source pin is unavailable: {source_path}")
    contents = path.read_bytes()
    if hashlib.sha256(contents).hexdigest() != digest:
        raise SelectedRouteError(f"source pin is stale: {source_path}")
    try:
        text = contents.decode("utf-8")
    except UnicodeDecodeError as error:
        raise SelectedRouteError(f"source pin is not UTF-8: {source_path}") from error
    if _frontmatter_value(text, "atom_id") != atom_id or _frontmatter_value(text, "version") != str(version):
        raise SelectedRouteError(f"source pin metadata differs: {source_path}")
    return dict(pin)


def _manifest_path(root: Path) -> Path:
    return _safe_path(root, selected_manifest_ref(root))


def _definition_sequence(route: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [route["workflow"], *[item["step"] for item in route["ordered_steps"]], *route["ordered_actions"]]


def _validate_route(root: Path, entry: Any) -> dict[str, Any]:
    required = {"route", "workflow", "ordered_steps", "ordered_actions", "native_action_calls",
                "entry_step", "on_result", "mutation_capable"}
    if not isinstance(entry, Mapping) or set(entry) != required:
        raise SelectedRouteError("route binding has an incomplete or unknown schema")
    if entry["route"] not in SELECTED_ROUTE_NAMES or not isinstance(entry["entry_step"], str):
        raise SelectedRouteError("route binding has an unsupported route or entry step")
    if not isinstance(entry["mutation_capable"], bool) or not isinstance(entry["ordered_steps"], list) or not entry["ordered_steps"]:
        raise SelectedRouteError("route binding has no ordered step graph")
    if not isinstance(entry["ordered_actions"], list) or not isinstance(entry["native_action_calls"], list):
        raise SelectedRouteError("route binding has an invalid ordered Action list")
    result = dict(entry)
    result["workflow"] = _validate_pin(root, entry["workflow"])
    steps: list[dict[str, Any]] = []
    for item in entry["ordered_steps"]:
        if not isinstance(item, Mapping) or set(item) != {"step", "action"}:
            raise SelectedRouteError("ordered step binding must have one Step and one Action")
        steps.append({"step": _validate_pin(root, item["step"]), "action": _validate_pin(root, item["action"])})
    step_ids = {item["step"]["atom_id"] for item in steps}
    if entry["entry_step"] not in step_ids:
        raise SelectedRouteError("route entry step is not in its ordered Step list")
    actions = [_validate_pin(root, item) for item in entry["ordered_actions"]]
    if [item["action"]["atom_id"] for item in steps] != [item["atom_id"] for item in actions]:
        raise SelectedRouteError("ordered Action list differs from Step Action bindings")
    if not isinstance(entry["on_result"], list):
        raise SelectedRouteError("route on_result must be an ordered list")
    for edge in entry["on_result"]:
        if not isinstance(edge, Mapping) or set(edge) != {"from", "condition", "to"} or not all(
                isinstance(edge[key], str) and edge[key] for key in ("from", "condition", "to")):
            raise SelectedRouteError("route on_result edge is malformed")
        if edge["from"] not in step_ids:
            raise SelectedRouteError("route on_result source is not in its ordered Step list")
        if edge["to"] != "complete" and edge["to"] not in step_ids:
            raise SelectedRouteError("route on_result target is not in its ordered Step list or complete")
    result.update(ordered_steps=steps, ordered_actions=actions,
                  native_action_calls=[_validate_pin(root, item) for item in entry["native_action_calls"]])
    return result


def load_selected_manifest(root: str | Path) -> dict[str, Any]:
    """Load the immutable projection and verify its self digest and live source pins."""
    project_root = Path(root).resolve(strict=True)
    manifest_ref = selected_manifest_ref(project_root)
    try:
        manifest = json.loads(_manifest_path(project_root).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SelectedRouteError("selected workflow binding manifest is unreadable") from error
    required = {"schema_version", "source_freshness", "routes", "canonical_manifest_sha256"}
    if not isinstance(manifest, Mapping) or set(manifest) != required or manifest["schema_version"] != 1:
        raise SelectedRouteError("selected workflow binding manifest schema is invalid")
    if not isinstance(manifest["canonical_manifest_sha256"], str) or not _DIGEST.fullmatch(manifest["canonical_manifest_sha256"]):
        raise SelectedRouteError("selected workflow binding manifest digest is invalid")
    without_self = {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
    if canonical_digest(without_self) != manifest["canonical_manifest_sha256"]:
        raise SelectedRouteError("selected workflow binding manifest canonical digest differs")
    freshness = manifest["source_freshness"]
    if not isinstance(freshness, Mapping) or set(freshness) != _FRESHNESS_FIELDS:
        raise SelectedRouteError("selected workflow binding manifest source freshness is invalid")
    if not all(isinstance(freshness[key], str) and freshness[key] for key in _FRESHNESS_FIELDS - {"selected_source_registry_version"}) or type(freshness["selected_source_registry_version"]) is not int or freshness["selected_source_registry_version"] < 1:
        raise SelectedRouteError("selected workflow binding manifest source freshness is incomplete")
    if not _DIGEST.fullmatch(freshness["selected_source_registry_digest"]) or not _DIGEST.fullmatch(freshness["selected_binding_digest"]):
        raise SelectedRouteError("selected workflow binding manifest freshness digest is invalid")
    registry = _safe_path(project_root, freshness["selected_source_registry_ref"])
    if not registry.is_file() or hashlib.sha256(registry.read_bytes()).hexdigest() != freshness["selected_source_registry_digest"]:
        raise SelectedRouteError("selected source registry pin is stale")
    routes = manifest["routes"]
    if not isinstance(routes, list) or len(routes) != len(SELECTED_ROUTE_NAMES):
        raise SelectedRouteError("selected workflow binding manifest does not contain thirteen routes")
    validated = [_validate_route(project_root, entry) for entry in routes]
    if tuple(entry["route"] for entry in validated) != SELECTED_ROUTE_NAMES or len({entry["route"] for entry in validated}) != 13:
        raise SelectedRouteError("selected workflow route registry is incomplete or duplicate")
    if canonical_digest(validated) != freshness["selected_binding_digest"]:
        raise SelectedRouteError("selected workflow route binding digest differs")
    return {"manifest_ref": manifest_ref, "schema_version": 1, "source_freshness": dict(freshness), "routes": validated,
            "canonical_manifest_sha256": manifest["canonical_manifest_sha256"]}


def _find_shadow_manifest_fields(value: Any, *, allowed_definition_manifest: bool = False) -> bool:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if key in {"definition_manifest_ref", "definition_manifest_digest"}:
                return True
            if key == "definition_manifest" and not allowed_definition_manifest:
                return True
            if _find_shadow_manifest_fields(child, allowed_definition_manifest=key == "operator_authorization"):
                return True
    elif isinstance(value, list):
        return any(_find_shadow_manifest_fields(item, allowed_definition_manifest=allowed_definition_manifest) for item in value)
    return False


def _require_digest(value: Any, message: str) -> str:
    if not isinstance(value, str) or not _DIGEST.fullmatch(value):
        raise SelectedRouteError(message)
    return value


class _SelectedRouteAdapterBase:
    """Validates the closed projection then calls the shared selected-run service once."""

    def __init__(self, root: str | Path, service: Any | None = None, *, strict_manifest: bool = True) -> None:
        self.root = Path(root).resolve(strict=True)
        self.manifest: dict[str, Any] | None = None
        self.routes: dict[str, dict[str, Any]] = {}
        if strict_manifest:
            self.manifest = load_selected_manifest(self.root)
            self.routes = {entry["route"]: entry for entry in self.manifest["routes"]}
        self.service = service

    def _result(self, request: Any, disposition: str, outcome: str, diagnostic: str) -> dict[str, Any]:
        value = {"disposition": disposition, "outcome": outcome, "diagnostics": [diagnostic]}
        if isinstance(request, Mapping) and isinstance(request.get("request_id"), str):
            value["request_id"] = request["request_id"]
        return value

    def _support(self) -> Any | None:
        if self.service is not None:
            return self.service
        return _QueueBackedSelectedSupport(self.root, self)


class _QueueBackedSelectedSupport:
    """Thin MCP composition of shared preview support and the existing queue APP.

    It deliberately does not execute Actions.  Preview uses the shared
    ``RunTracker`` admission implementation; execute only forwards the exact
    request to the already-owned ``enqueue_selected`` APP variant.
    """

    def __init__(self, root: Path, adapter: "SelectedRouteAdapter") -> None:
        self.root, self.adapter = root, adapter

    def _tracker(self) -> Any:
        # Code is loaded from the immutable MCP image; ``root`` is only the
        # caller's Project authority/data root and need not contain code.
        tools = Path(__file__).resolve().parents[1] / "201_TOOLS"
        if str(tools) not in sys.path:
            sys.path.insert(0, str(tools))
        module = importlib.import_module("workflow_run_support")

        def observe(request: dict[str, Any]) -> dict[str, Any]:
            try:
                manifest = load_selected_manifest(self.root)
                selected = request.get("operation_route") in {entry["route"] for entry in manifest["routes"]}
                current = dict(request.get("definition_manifest", {})) == {
                    "manifest_ref": manifest["manifest_ref"], "manifest_digest": manifest["canonical_manifest_sha256"]
                } and dict(request.get("source_freshness", {})) == manifest["source_freshness"]
            except (SelectedRouteError, TypeError, ValueError):
                selected, current = False, False
            return {"selected": selected, "current": current, "observed": {
                "manifest_ref": request.get("definition_manifest", {}).get("manifest_ref") if isinstance(request.get("definition_manifest"), Mapping) else None,
                "manifest_digest": request.get("definition_manifest", {}).get("manifest_digest") if isinstance(request.get("definition_manifest"), Mapping) else None,
            }}

        def never_execute(_request: dict[str, Any], _session: Any) -> Mapping[str, Any]:
            raise RuntimeError("MCP delegates selected execution to enqueue_selected")

        return module.RunTracker(self.root, source_observer=observe, executor=never_execute)

    @staticmethod
    def _workflow_run_id(request: Mapping[str, Any]) -> str:
        rows = request.get("requested_runs")
        if not isinstance(rows, list):
            raise SelectedRouteError("execute has no requested Workflow Run identity")
        workflow = [row for row in rows if isinstance(row, Mapping) and row.get("kind") == "workflow"]
        if len(workflow) != 1 or not isinstance(workflow[0].get("requested_run_id"), str):
            raise SelectedRouteError("execute must carry one requested Workflow Run identity")
        return str(workflow[0]["requested_run_id"])

    def run_selected_operation(self, request: dict[str, Any]) -> dict[str, Any]:
        if request["mode"] == "preview":
            return self._tracker().run_selected_operation(request)
        preview = {key: value for key, value in request.items() if key not in {
            "proposal_receipt", "proposal_receipt_digest", "assigned_action_id", "operator_authorization", "requested_runs"
        }}
        preview["mode"] = "preview"
        prepared = self._tracker().run_selected_operation(preview)
        if prepared.get("disposition") != "preview" or request.get("proposal_receipt") != prepared.get("proposal_receipt") or request.get("proposal_receipt_digest") != prepared.get("proposal_receipt_digest"):
            return {"request_id": request["request_id"], "disposition": "blocked", "outcome": "blocked",
                    "source_freshness": prepared.get("source_freshness"), "diagnostics": ["exact current preview receipt is required before enqueue"]}
        try:
            app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
            if str(app) not in sys.path:
                sys.path.insert(0, str(app))
            orchestrator = importlib.import_module("orchestrator")
            return orchestrator.run(self.root, {"operation": "enqueue_selected", "run_id": self._workflow_run_id(request), "execution": request})
        except (ImportError, SelectedRouteError, ValueError, RuntimeError, OSError) as error:
            return {"request_id": request["request_id"], "disposition": "blocked", "outcome": "blocked",
                    "source_freshness": prepared.get("source_freshness"),
                    "diagnostics": [f"enqueue_selected did not admit the exact request: {error}"]}

    def get_selected_workflow_run(self, request: dict[str, Any]) -> dict[str, Any]:
        try:
            app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
            if str(app) not in sys.path:
                sys.path.insert(0, str(app))
            return importlib.import_module("orchestrator").run(self.root, {"operation": "status", "run_id": request["run_id"]})
        except (ImportError, ValueError, RuntimeError, OSError) as error:
            return {"disposition": "blocked", "outcome": "blocked", "diagnostics": [f"selected Run observation unavailable: {error}"]}

    def get_selected_action_run(self, request: dict[str, Any]) -> dict[str, Any]:
        return {"action_run_id": request["action_run_id"], "disposition": "blocked", "outcome": "implementation_gap",
                "diagnostics": ["shared action-Run observation is not yet published by the queue service"]}

    def recover_selected_run_recording(self, request: dict[str, Any]) -> dict[str, Any]:
        try:
            return self._tracker().recover_recording(request["pending_event_ref"])
        except (ImportError, ValueError, RuntimeError, OSError) as error:
            return {"disposition": "blocked", "outcome": "blocked", "diagnostics": [f"shared recording recovery failed: {error}"]}


class SelectedRouteAdapter(_SelectedRouteAdapterBase):

    def _validate_request(self, route: str, request: Any) -> dict[str, Any]:
        if not isinstance(request, Mapping):
            raise SelectedRouteError("request must be an object")
        allowed = {"operation_route", "mode", "request_id", "parameters", "parameters_digest", "target_frontier",
                   "target_frontier_digest", "effects", "effects_digest", "definition_manifest", "source_freshness",
                   "expected_definition_revisions", "initiative", "lineage", "proposal_receipt",
                   "proposal_receipt_digest", "assigned_action_id", "requested_runs", "operator_authorization"}
        unknown = set(request) - allowed
        if unknown or _find_shadow_manifest_fields(request, allowed_definition_manifest=True):
            raise SelectedRouteError("request contains unknown or shadow manifest fields")
        normalized = dict(request)
        normalized.setdefault("mode", "preview")
        if normalized.get("operation_route") != route or route not in self.routes:
            raise SelectedRouteError("request route is not the selected MCP route")
        if normalized["mode"] not in {"preview", "execute"}:
            raise SelectedRouteError("mode must be preview or execute")
        if not isinstance(normalized.get("request_id"), str) or not _REQUEST_ID.fullmatch(normalized["request_id"]):
            raise SelectedRouteError("request_id must be a stable safe identity")
        if not isinstance(normalized.get("parameters"), Mapping) or canonical_digest(normalized["parameters"]) != _require_digest(normalized.get("parameters_digest"), "parameters_digest differs"):
            raise SelectedRouteError("parameters or parameters_digest differs")
        frontier = normalized.get("target_frontier")
        if not isinstance(frontier, list) or not frontier or not all(isinstance(ref, str) and ref and not ref.startswith("/") and ".." not in Path(ref).parts for ref in frontier):
            raise SelectedRouteError("target_frontier is invalid")
        if len(set(frontier)) != len(frontier) or canonical_digest(frontier) != _require_digest(normalized.get("target_frontier_digest"), "target_frontier_digest differs"):
            raise SelectedRouteError("target_frontier_digest differs")
        effects = normalized.get("effects")
        if not isinstance(effects, list) or any(not isinstance(effect, Mapping) or not isinstance(effect.get("type"), str) or not effect["type"] for effect in effects):
            raise SelectedRouteError("effects are invalid")
        if canonical_digest(effects) != _require_digest(normalized.get("effects_digest"), "effects_digest differs"):
            raise SelectedRouteError("effects_digest differs")
        manifest = normalized.get("definition_manifest")
        if not isinstance(manifest, Mapping) or set(manifest) != {"manifest_ref", "manifest_digest"}:
            raise SelectedRouteError("definition_manifest is invalid")
        if manifest != {"manifest_ref": self.manifest["manifest_ref"], "manifest_digest": self.manifest["canonical_manifest_sha256"]}:
            raise SelectedRouteError("definition_manifest is stale or does not identify the canonical binding")
        freshness = normalized.get("source_freshness")
        if not isinstance(freshness, Mapping) or dict(freshness) != self.manifest["source_freshness"]:
            raise SelectedRouteError("source_freshness is stale or incomplete")
        initiative = normalized.get("initiative")
        if not isinstance(initiative, Mapping) or not set(initiative) <= {"initiative_id", "instruction_summary", "initiative_ref"} or not all(isinstance(initiative.get(key), str) and initiative[key] for key in ("initiative_id", "instruction_summary")) or ("initiative_ref" in initiative and (not isinstance(initiative["initiative_ref"], str) or not initiative["initiative_ref"] or initiative["initiative_ref"].startswith("/") or ".." in Path(initiative["initiative_ref"]).parts)):
            raise SelectedRouteError("initiative must be an explicit sealed authorization boundary")
        if "lineage" in normalized:
            lineage = normalized["lineage"]
            if not isinstance(lineage, list) or any(not isinstance(value, str) or not value for value in lineage):
                raise SelectedRouteError("lineage must contain only actual parent Run references")
        if "expected_definition_revisions" in normalized:
            expected = normalized["expected_definition_revisions"]
            source = self._expected_revisions(route)
            if not isinstance(expected, list) or expected != source:
                raise SelectedRouteError("expected definition revisions differ from the selected route binding")
        return normalized

    def _expected_revisions(self, route: str) -> list[dict[str, Any]]:
        entry = self.routes[route]
        rows: list[dict[str, Any]] = []
        for kind, pin in [("workflow", entry["workflow"]), *[("step", item["step"]) for item in entry["ordered_steps"]], *[("action", item) for item in entry["ordered_actions"]]]:
            row = {"kind": kind, "atom_id": pin["atom_id"], "version": pin["version"], "path": pin["source_path"], "digest": pin["digest"]}
            if row not in rows:
                rows.append(row)
        return sorted(rows, key=lambda item: (item["kind"], item["atom_id"], item["version"], item["path"]))

    def _validate_execute(self, request: Mapping[str, Any]) -> str | None:
        required = {"proposal_receipt", "proposal_receipt_digest", "assigned_action_id", "requested_runs", "operator_authorization"}
        missing = [name for name in sorted(required) if name not in request]
        if missing:
            return "execute requires exact preview receipt and Operator authorization"
        if not isinstance(request["proposal_receipt"], str) or not request["proposal_receipt"] or not _DIGEST.fullmatch(str(request["proposal_receipt_digest"])):
            return "execute proposal receipt is invalid"
        if not isinstance(request["assigned_action_id"], str) or not request["assigned_action_id"]:
            return "execute assigned_action_id is invalid"
        requested = request["requested_runs"]
        if not isinstance(requested, list) or not requested:
            return "execute requested Run identities are invalid"
        authorization = request["operator_authorization"]
        if not isinstance(authorization, Mapping) or not isinstance(authorization.get("authorization_ref"), str) or not authorization["authorization_ref"]:
            return "execute lacks explicit sealed Operator authorization"
        required_bindings = {
            "request_id": request["request_id"], "operation_route": request["operation_route"],
            "proposal_receipt_digest": request["proposal_receipt_digest"], "parameters_digest": request["parameters_digest"],
            "target_frontier_digest": request["target_frontier_digest"],
            "effects_digest": request["effects_digest"], "definition_manifest": request["definition_manifest"],
            "source_freshness": request["source_freshness"],
        }
        if any(authorization.get(key) != value for key, value in required_bindings.items()):
            return "Operator authorization is not bound to the exact preview and current source frontier"
        freshness = authorization.get("authorization_freshness")
        if not isinstance(freshness, Mapping) or set(freshness) != {"state", "digest"} or freshness.get("state") != "current" or not isinstance(freshness.get("digest"), str) or not _DIGEST.fullmatch(freshness["digest"]):
            return "Operator authorization freshness is invalid"
        if set(authorization) != {"authorization_ref", "authorization_freshness", *required_bindings}:
            return "Operator authorization contains unknown or incomplete bindings"
        return None

    def invoke(self, route: str, request: Any) -> dict[str, Any]:
        try:
            self.manifest = load_selected_manifest(self.root)
            self.routes = {entry["route"]: entry for entry in self.manifest["routes"]}
            normalized = self._validate_request(route, request)
        except SelectedRouteError as error:
            return self._result(request, "rejected", "rejected", str(error))
        if normalized["mode"] == "execute":
            blocked = self._validate_execute(normalized)
            if blocked:
                return self._result(normalized, "blocked", "blocked", blocked)
        support = self._support()
        if support is None:
            return {"request_id": normalized["request_id"], "disposition": "blocked", "outcome": "implementation_gap",
                    "source_freshness": normalized["source_freshness"], "diagnostics": ["shared implement_run_support is unavailable"]}
        try:
            handler: Callable[[dict[str, Any]], dict[str, Any]] = getattr(support, "run_selected_operation")
            return handler(normalized)
        except (AttributeError, TypeError, ValueError, RuntimeError) as error:
            return self._result(normalized, "blocked", "blocked", f"shared support rejected request: {error}")

    def _observe(self, method: str, request: Any, required_key: str) -> dict[str, Any]:
        if not isinstance(request, Mapping) or set(request) != {required_key} or not isinstance(request[required_key], str) or not request[required_key]:
            return self._result(request, "rejected", "rejected", f"{method} requires one exact {required_key}")
        support = self._support()
        if support is None or not hasattr(support, method):
            return self._result(request, "blocked", "implementation_gap", "shared implement_run_support observation is unavailable")
        try:
            return getattr(support, method)(dict(request))
        except (TypeError, ValueError, RuntimeError) as error:
            return self._result(request, "blocked", "blocked", f"shared support rejected observation: {error}")

    def get_workflow_run(self, request: Any) -> dict[str, Any]:
        return self._observe("get_selected_workflow_run", request, "run_id")

    def get_action_run(self, request: Any) -> dict[str, Any]:
        return self._observe("get_selected_action_run", request, "action_run_id")

    def recover_recording(self, request: Any) -> dict[str, Any]:
        if not isinstance(request, Mapping) or not set(request) <= {"pending_event_ref", "request_id"} or "pending_event_ref" not in request or not isinstance(request["pending_event_ref"], str) or not request["pending_event_ref"] or ("request_id" in request and (not isinstance(request["request_id"], str) or not _REQUEST_ID.fullmatch(request["request_id"]))):
            return self._result(request, "rejected", "rejected", "recovery requires one exact pending event reference and optional request_id")
        support = self._support()
        if support is None or not hasattr(support, "recover_selected_run_recording"):
            return self._result(request, "blocked", "implementation_gap", "shared implement_run_support recording recovery is unavailable")
        try:
            return support.recover_selected_run_recording(dict(request))
        except (TypeError, ValueError, RuntimeError) as error:
            return self._result(request, "blocked", "blocked", f"shared support rejected recording recovery: {error}")


def register_selected_routes(server: Any, root: str | Path) -> SelectedRouteAdapter:
    """Additive registration retaining the stable server, helpers, and reload gateway."""
    from mcp.types import ToolAnnotations

    adapter = SelectedRouteAdapter(root, strict_manifest=False)
    selected_annotations = ToolAnnotations(read_only_hint=False, destructive_hint=False, idempotent_hint=True, open_world_hint=False)
    observation_annotations = ToolAnnotations(read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False)

    for route_name in SELECTED_ROUTE_NAMES:
        def add_route(route: str) -> None:
            @server.tool(name=route, structured_output=True, annotations=selected_annotations)
            def selected_route(request: dict[str, Any]) -> dict[str, Any]:
                """Preview by default; execute requires exact sealed Operator authorization and never starts a worker."""
                return adapter.invoke(route, request)
        add_route(route_name)

    @server.tool(name="get_selected_workflow_run", structured_output=True, annotations=observation_annotations)
    def get_selected_workflow_run(request: dict[str, Any]) -> dict[str, Any]:
        """Read one saved selected Workflow Run without dispatch."""
        return adapter.get_workflow_run(request)

    @server.tool(name="get_selected_action_run", structured_output=True, annotations=observation_annotations)
    def get_selected_action_run(request: dict[str, Any]) -> dict[str, Any]:
        """Read one saved selected Action Run without dispatch."""
        return adapter.get_action_run(request)

    @server.tool(name="recover_selected_run_recording", structured_output=True, annotations=selected_annotations)
    def recover_selected_run_recording(request: dict[str, Any]) -> dict[str, Any]:
        """Retry one pending shared event append; never replay an Action or Workflow."""
        return adapter.recover_recording(request)

    return adapter
