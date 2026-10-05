"""Read one selected Action Run without changing queue or Journal state."""
from __future__ import annotations

import json
import re
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any


_ACTION_ID = re.compile(
    r"^(?P<workflow>[A-Za-z0-9][A-Za-z0-9_-]{0,127}):step:(?P<step>[1-9][0-9]*)"
    r"(?::visit:(?P<visit>[2-9][0-9]*))?:action:(?P<action>[1-9][0-9]*)$"
)
_DIGEST = re.compile(r"^[0-9a-f]{64}$")
_RUNTIME = Path(".caprmedio_install/workflow_orchestrator/runs")
_MAX_JSON_BYTES = 512 * 1024
_MAX_JOURNAL_BYTES = 8 * 1024 * 1024
_MAX_JOURNAL_LINES = 100_000


class SelectedActionObservationError(ValueError):
    """A requested Action observation cannot be safely bound to saved evidence."""


def _safe_json(path: Path, *, limit: int = _MAX_JSON_BYTES) -> dict[str, Any] | None:
    """Read a bounded regular JSON carrier, never following a symlink."""
    try:
        if path.is_symlink() or not path.is_file() or path.stat().st_size > limit:
            return None
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def _safe_relative_path(root: Path, relative: str) -> Path | None:
    """Resolve one known repository-relative carrier without symlink escape."""
    candidate = Path(relative)
    if candidate.is_absolute() or not candidate.parts or ".." in candidate.parts:
        return None
    cursor = root
    for part in candidate.parts:
        cursor /= part
        if cursor.is_symlink():
            return None
    try:
        resolved = (root / candidate).resolve(strict=True)
        resolved.relative_to(root)
    except (OSError, ValueError):
        return None
    return resolved


def _support_definition(pin: Mapping[str, Any]) -> dict[str, Any] | None:
    if not isinstance(pin, Mapping) or set(pin) != {"atom_id", "version", "source_path", "digest"}:
        return None
    if (not isinstance(pin["atom_id"], str) or not pin["atom_id"]
            or type(pin["version"]) is not int or pin["version"] < 1
            or not isinstance(pin["source_path"], str) or not pin["source_path"]
            or not isinstance(pin["digest"], str) or not _DIGEST.fullmatch(pin["digest"])):
        return None
    return {"atom_id": pin["atom_id"], "version": pin["version"],
            "path": pin["source_path"], "digest": pin["digest"]}


def _graph_definition(definition: Mapping[str, Any], kind: str) -> dict[str, Any]:
    return {"atom_id": definition["atom_id"], "kind": kind, "version": definition["version"],
            "path": definition["path"], "sha256": definition["digest"]}


def _manifest_identity(manifest: Mapping[str, Any]) -> tuple[str, str, dict[str, Any], list[dict[str, Any]]]:
    reference = manifest.get("manifest_ref")
    digest = manifest.get("canonical_manifest_sha256")
    freshness = manifest.get("source_freshness")
    routes = manifest.get("routes")
    if (not isinstance(reference, str) or Path(reference).is_absolute() or ".." in Path(reference).parts
            or not isinstance(digest, str) or not _DIGEST.fullmatch(digest)
            or not isinstance(freshness, Mapping) or not isinstance(routes, list)):
        raise SelectedActionObservationError("current selected manifest is unavailable")
    normalized_routes = [dict(route) for route in routes if isinstance(route, Mapping)]
    if len(normalized_routes) != len(routes):
        raise SelectedActionObservationError("current selected manifest is invalid")
    return reference, digest, dict(freshness), normalized_routes


def _bound_request(
    saved: Mapping[str, Any], action_run_id: str, manifest: Mapping[str, Any],
) -> dict[str, Any]:
    """Bind exactly one requested Action to its saved parent and current manifest."""
    manifest_ref, manifest_digest, freshness, routes = _manifest_identity(manifest)
    request = saved.get("request")
    graph = saved.get("graph")
    if (set(saved) != {"request", "graph"} or not isinstance(request, Mapping)
            or set(request) != {"operation", "run_id", "execution"} or not isinstance(graph, Mapping)):
        raise SelectedActionObservationError("saved selected request has an invalid outer shape")
    execution = request.get("execution")
    if request.get("operation") != "enqueue_selected" or not isinstance(execution, Mapping):
        raise SelectedActionObservationError("saved selected request is not an admitted enqueue")
    match = _ACTION_ID.fullmatch(action_run_id)
    assert match is not None
    workflow_run_id = match.group("workflow")
    if request.get("run_id") != workflow_run_id:
        raise SelectedActionObservationError("Action identity is not bound to its saved Workflow Run")
    definition_manifest = execution.get("definition_manifest")
    if definition_manifest != {"manifest_ref": manifest_ref, "manifest_digest": manifest_digest}:
        raise SelectedActionObservationError("saved Action request is not bound to the current canonical manifest")
    if execution.get("source_freshness") != freshness:
        raise SelectedActionObservationError("saved Action request has stale source freshness")
    route_name = execution.get("operation_route")
    route_rows = [route for route in routes if route.get("route") == route_name]
    if not isinstance(route_name, str) or len(route_rows) != 1:
        raise SelectedActionObservationError("saved Action request has no current selected route")
    route = route_rows[0]
    if (graph.get("route") != route_name or graph.get("manifest_ref") != manifest_ref
            or graph.get("manifest_digest") != manifest_digest):
        raise SelectedActionObservationError("saved selected graph is not bound to the current canonical manifest")
    workflow_definition = _support_definition(route.get("workflow", {}))
    steps = route.get("ordered_steps")
    if workflow_definition is None or not isinstance(steps, list):
        raise SelectedActionObservationError("current selected route has no bound Run graph")

    requested = execution.get("requested_runs")
    if not isinstance(requested, list):
        raise SelectedActionObservationError("saved Action request has no requested Runs")
    action_rows = [dict(row) for row in requested if isinstance(row, Mapping)
                   and row.get("kind") == "action" and row.get("requested_run_id") == action_run_id]
    if len(action_rows) != 1:
        raise SelectedActionObservationError("Action identity is unknown or ambiguous in the saved request")
    action_row = action_rows[0]
    step_run_id = action_row.get("parent_requested_run_id")
    action_definition = action_row.get("definition")
    if not isinstance(step_run_id, str) or not isinstance(action_definition, Mapping):
        raise SelectedActionObservationError("saved Action request has no source-bound parent Step")
    step_rows = [dict(row) for row in requested if isinstance(row, Mapping)
                 and row.get("kind") == "step" and row.get("requested_run_id") == step_run_id]
    workflow_rows = [dict(row) for row in requested if isinstance(row, Mapping)
                     and row.get("kind") == "workflow" and row.get("requested_run_id") == workflow_run_id]
    if len(step_rows) != 1 or len(workflow_rows) != 1 or workflow_rows[0].get("definition") != workflow_definition:
        raise SelectedActionObservationError("saved Action parent lineage is incomplete or ambiguous")
    step_definition = step_rows[0].get("definition")
    if step_rows[0].get("parent_requested_run_id") != workflow_run_id or not isinstance(step_definition, Mapping):
        raise SelectedActionObservationError("saved Action parent lineage is not source-bound")

    admitted = False
    for item in steps:
        if not isinstance(item, Mapping):
            continue
        source_step = _support_definition(item.get("step", {}))
        source_action = _support_definition(item.get("action", {}))
        if source_step == step_definition and source_action == action_definition:
            admitted = True
            break
    if not admitted:
        raise SelectedActionObservationError("saved Action definition is not admitted by the current route")
    graph_steps = graph.get("steps")
    graph_workflow = graph.get("workflow")
    if not isinstance(graph_steps, list) or not isinstance(graph_workflow, Mapping):
        raise SelectedActionObservationError("saved selected graph has no source-bound Action")
    expected_graph_workflow = _graph_definition(workflow_definition, "workflow")
    graph_action_matches = False
    for item in graph_steps:
        if not isinstance(item, Mapping) or not isinstance(item.get("actions"), list):
            continue
        graph_step = {key: item.get(key) for key in ("atom_id", "kind", "version", "path", "sha256")}
        if graph_step != _graph_definition(step_definition, "step"):
            continue
        for action in item["actions"]:
            if isinstance(action, Mapping) and {
                key: action.get(key) for key in ("atom_id", "kind", "version", "path", "sha256")
            } == _graph_definition(action_definition, "action"):
                graph_action_matches = True
    if graph_workflow != expected_graph_workflow or not graph_action_matches:
        raise SelectedActionObservationError("saved selected graph does not retain the requested Action binding")
    return {
        "action_run_id": action_run_id,
        "workflow_run_id": workflow_run_id,
        "step_run_id": step_run_id,
        "operation_route": route_name,
        "action_definition": dict(action_definition),
        "definition_manifest": {"manifest_ref": manifest_ref, "manifest_digest": manifest_digest},
        "source_freshness": freshness,
    }


def _journal_module() -> Any:
    tools_root = Path(__file__).resolve().parents[2] / "201_TOOLS"
    if str(tools_root) not in sys.path:
        sys.path.insert(0, str(tools_root))
    import work_journal
    return work_journal


def _read_receipt_event(root: Path, receipt: Any, journal_root: Path, journal: Any) -> dict[str, Any] | None:
    """Validate one receipt-addressed Journal line without scanning any carrier."""
    if not isinstance(receipt, Mapping):
        return None
    carrier, line, event_id, digest = (receipt.get("carrier"), receipt.get("line"),
                                       receipt.get("event_id"), receipt.get("event_digest"))
    if (not isinstance(carrier, str) or not isinstance(line, int) or isinstance(line, bool)
            or line < 1 or line > _MAX_JOURNAL_LINES or not isinstance(event_id, str)
            or not event_id or not isinstance(digest, str) or not _DIGEST.fullmatch(digest)):
        return None
    carrier_path = _safe_relative_path(root, carrier)
    if carrier_path is None or not carrier_path.is_file() or carrier_path.stat().st_size > _MAX_JOURNAL_BYTES:
        return None
    try:
        carrier_path.relative_to(journal_root)
    except ValueError:
        return None
    try:
        with carrier_path.open("r", encoding="utf-8") as handle:
            for ordinal, raw in enumerate(handle, start=1):
                if ordinal == line:
                    event = json.loads(raw)
                    break
            else:
                return None
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None
    if not isinstance(event, Mapping):
        return None
    try:
        sealed = journal.validate_sealed_event(event)
    except (ValueError, RuntimeError):
        return None
    if sealed.get("event_id") != event_id or sealed.get("event_digest") != digest:
        return None
    return {**sealed, "_observation_receipt": {"carrier": carrier, "line": line}}


def _matches_action_event(event: Mapping[str, Any], bound: Mapping[str, Any], request_id: str, assigned_action_id: str) -> bool:
    run = event.get("run")
    session = event.get("llm_session")
    return (
        event.get("schema_version") == 5
        and event.get("kind") == "workflow_execution"
        and event.get("action_id") == assigned_action_id
        and isinstance(session, Mapping) and session.get("uuid") == request_id
        and isinstance(run, Mapping)
        and run.get("run_id") == bound["action_run_id"]
        and run.get("kind") == "action"
        and run.get("parent_run_id") == bound["step_run_id"]
        and run.get("definition") == bound["action_definition"]
    )


def _accepted_events(root: Path, run_directory: Path, bound: Mapping[str, Any]) -> list[dict[str, Any]]:
    accepted = _safe_json(run_directory / "accepted.json")
    if accepted is None or not isinstance(accepted.get("result"), Mapping):
        return []
    saved_request = _safe_json(run_directory / "selected_request.json")
    if saved_request is None:
        return []
    execution = saved_request.get("request", {}).get("execution") if isinstance(saved_request.get("request"), Mapping) else None
    if not isinstance(execution, Mapping):
        return []
    request_id, assigned_action_id = execution.get("request_id"), execution.get("assigned_action_id")
    receipts = accepted["result"].get("event_receipts")
    if not isinstance(request_id, str) or not isinstance(assigned_action_id, str) or not isinstance(receipts, list):
        return []
    try:
        journal = _journal_module()
        journal_relative = journal.configured_journal_root(root)
        journal_root = _safe_relative_path(root, journal_relative.as_posix())
    except (ImportError, OSError, RuntimeError, ValueError):
        return []
    if journal_root is None or not journal_root.is_dir():
        return []
    events: list[dict[str, Any]] = []
    for receipt in receipts:
        event = _read_receipt_event(root, receipt, journal_root, journal)
        if event is not None and _matches_action_event(event, bound, request_id, assigned_action_id):
            events.append(event)
    return events


def _base(bound: Mapping[str, Any], disposition: str, outcome: str, diagnostic: str | None = None) -> dict[str, Any]:
    value = {**bound, "disposition": disposition, "outcome": outcome}
    if diagnostic is not None:
        value["diagnostics"] = [diagnostic]
    return value


def observe_selected_action(root: str | Path, action_run_id: object, manifest: Mapping[str, Any]) -> dict[str, Any]:
    """Return one bounded, Journal-confirmed selected Action observation.

    This deliberately consults only the Action's deterministic run directory,
    frozen request, optional progress carrier, accepted receipt list, and the
    exact receipt-addressed Journal lines.  It never queues, replays, or
    writes anything.
    """
    if not isinstance(action_run_id, str) or not _ACTION_ID.fullmatch(action_run_id):
        return {"disposition": "rejected", "outcome": "rejected",
                "diagnostics": ["action Run identity is invalid"]}
    try:
        project_root = Path(root).resolve(strict=True)
    except (OSError, ValueError):
        return {"action_run_id": action_run_id, "disposition": "blocked", "outcome": "blocked",
                "diagnostics": ["Project root is unavailable"]}
    workflow_run_id = _ACTION_ID.fullmatch(action_run_id).group("workflow")  # type: ignore[union-attr]
    run_directory = _safe_relative_path(project_root, (_RUNTIME / workflow_run_id).as_posix())
    if run_directory is None or not run_directory.is_dir():
        return {"action_run_id": action_run_id, "workflow_run_id": workflow_run_id,
                "disposition": "unknown", "outcome": "unknown",
                "diagnostics": ["no selected Workflow Run carrier exists for this Action"]}
    saved = _safe_json(run_directory / "selected_request.json")
    if saved is None:
        return {"action_run_id": action_run_id, "workflow_run_id": workflow_run_id,
                "disposition": "unknown", "outcome": "unknown",
                "diagnostics": ["selected Workflow Run has no readable frozen request"]}
    try:
        bound = _bound_request(saved, action_run_id, manifest)
    except SelectedActionObservationError as error:
        return {"action_run_id": action_run_id, "workflow_run_id": workflow_run_id,
                "disposition": "blocked", "outcome": "blocked", "diagnostics": [str(error)]}

    progress_relative = (_RUNTIME / workflow_run_id / f"{action_run_id}.json").as_posix()
    progress = _safe_json(run_directory / f"{action_run_id}.json")
    progress_is_bound = bool(progress and progress.get("action_run_id") == action_run_id
                             and isinstance(progress.get("result"), str))
    events = _accepted_events(project_root, run_directory, bound)
    terminal = [event for event in events if event.get("event") in {
        "completed", "failed", "abandoned", "interrupted", "recovered"
    } and isinstance(event.get("outcome"), str)]
    if terminal:
        event = terminal[-1]
        outcome = str(event["outcome"])
        if outcome == "interrupted_pending":
            result = _base(bound, "recording_pending", outcome,
                           "sealed Action interruption has no completed result")
            if progress_is_bound:
                result["progress_ref"] = progress_relative
            return result
        if event.get("result_ref") != progress_relative or not progress_is_bound:
            return _base(bound, "recording_pending", outcome,
                         "sealed Action result reference is not durably available")
        result = _base(bound, "terminal", outcome)
        result.update({"result_ref": progress_relative, "effect_refs": list(event.get("effect_refs", [])),
                       "report_ref": event.get("report_ref"),
                       "journal_confirmation": {
                           "event_id": event["event_id"], "event": event["event"],
                           "event_digest": event["event_digest"],
                           "carrier": event["_observation_receipt"]["carrier"],
                           "line": event["_observation_receipt"]["line"],
                       }})
        return result
    if progress is not None:
        result = _base(bound, "recording_pending", "pending",
                       "Action progress is present without sealed terminal Journal confirmation")
        if progress_is_bound:
            result["progress_ref"] = progress_relative
        return result
    if any(event.get("event") == "started" for event in events):
        return _base(bound, "started", "started", "sealed Action start has no terminal confirmation")
    return _base(bound, "unstarted", "unstarted", "no Action progress or sealed Journal fact is recorded")
