"""Native read-only query Action adapters for the selected Workflow interpreter.

The adapters deliberately delegate filtering, retained snapshots, and every
source diagnostic to the two native Tools.  They only bind an already-admitted
selected Action to its closed ``parameters.query_request`` shape.
"""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Any


_TOOLS = Path(__file__).resolve().parents[2] / "201_TOOLS"
_ARTIFACT_ROUTE = ("find_and_fetch_artifacts", "CA-O-158", "CA-O-160", "CA-O-159")
_JOURNAL_ROUTE = ("find_and_fetch_journal_events", "CA-O-161", "CA-O-163", "CA-O-162")
_ARTIFACT_COMPLETED_RESULT = "one complete, valid snapshot query result"
_JOURNAL_COMPLETED_RESULT = "valid query completed with truthful coverage"
_ARTIFACT_REQUEST_FIELDS = frozenset({"filter", "select", "limit", "cursor", "snapshot", "settings"})
_JOURNAL_REQUEST_FIELDS = frozenset({"filter", "mode", "select", "limit", "cursor", "limits", "snapshot"})


class QueryActionError(ValueError):
    """The selected query Action cannot consume the exact admitted input."""


@dataclass(frozen=True)
class JournalPreparation:
    """In-process pre-Run Journal source binding; never a persisted request field."""

    snapshot: Mapping[str, Any] | None = None
    diagnostic: str | None = None


def _tool_modules() -> tuple[Any, Any, type[Exception], type[Exception]]:
    """Load the native Tools through their package exports, without a duplicate API."""
    location = str(_TOOLS)
    if location not in sys.path:
        sys.path.insert(0, location)
    from FIND_AND_FETCH_ARTIFACTS import ArtifactQueryError, query_artifacts
    from FIND_AND_FETCH_JOURNAL_EVENTS import JournalQueryError, capture_snapshot, query

    return (query_artifacts, (capture_snapshot, query), ArtifactQueryError, JournalQueryError)


def _request(context: Mapping[str, Any], allowed: frozenset[str]) -> dict[str, Any]:
    parameters = context.get("parameters")
    if not isinstance(parameters, Mapping) or set(parameters) != {"query_request"}:
        raise QueryActionError("query Action requires exactly parameters.query_request")
    request = parameters.get("query_request")
    if not isinstance(request, Mapping) or any(key not in allowed for key in request):
        raise QueryActionError("query_request has an unsupported field")
    return dict(request)


def _assert_route(context: Mapping[str, Any], expected: tuple[str, str, str, str]) -> None:
    route, workflow, step, action = expected
    if (
        context.get("route"),
        context.get("workflow_definition_id"),
        context.get("step_definition_id"),
        context.get("action_definition_id"),
    ) != (route, workflow, step, action):
        raise QueryActionError("query Action is not bound to its admitted source Workflow, Step, and Action")


def _diagnostic(code: str, *, blocked: bool = False) -> dict[str, Any]:
    return {
        "result": "diagnostic",
        "terminal_outcome": "interrupted_pending" if blocked else "failed",
        "effect_refs": [],
        "native_result": {
            "status": "blocked" if blocked else "invalid",
            "results": [],
            "findings": [{"code": code}],
        },
    }


def validate_query_parameters(context: Mapping[str, Any]) -> dict[str, Any]:
    """Reject a non-Tool query shape before shared execution can create a Run."""
    action = context.get("action_definition_id")
    if action == "CA-O-159":
        _assert_route(context, _ARTIFACT_ROUTE)
        return _request(context, _ARTIFACT_REQUEST_FIELDS)
    if action == "CA-O-162":
        _assert_route(context, _JOURNAL_ROUTE)
        request = _request(context, _JOURNAL_REQUEST_FIELDS)
        if ("snapshot" in request) != ("cursor" in request):
            raise QueryActionError("Journal continuation requires its exact snapshot and cursor together")
        return request
    raise QueryActionError("query route does not bind a native query Action")


def prepare_journal_query(root: str | Path, context: Mapping[str, Any]) -> JournalPreparation:
    """Seal a new Journal frontier before any selected Run start is recorded.

    A continuation carries only the native Tool's opaque public snapshot.  It
    is never captured again here and is validated by ``query`` in the same
    process; an unknown post-restart handle therefore remains a truthful Tool
    diagnostic instead of a widened or caller-supplied source frontier.
    """
    _assert_route(context, _JOURNAL_ROUTE)
    request = validate_query_parameters(context)
    has_snapshot = "snapshot" in request
    has_cursor = "cursor" in request
    if has_snapshot:
        if not has_cursor:
            return JournalPreparation(diagnostic="continuation-requires-cursor")
        return JournalPreparation()
    if has_cursor:
        return JournalPreparation(diagnostic="continuation-requires-snapshot")
    _, tools, _, journal_error = _tool_modules()
    capture_snapshot, _ = tools
    try:
        return JournalPreparation(snapshot=capture_snapshot(root))
    except journal_error as error:
        # Capture was attempted before any Run evidence.  Retain only the
        # stable Tool code, never an exception payload or raw source record.
        return JournalPreparation(diagnostic=getattr(error, "code", "journal-unavailable"))


def artifact_query_action(context: dict[str, Any]) -> dict[str, Any]:
    """Invoke CA-O-159 once against its native retained Artifact snapshot."""
    artifact_error: type[Exception] | None = None
    try:
        _assert_route(context, _ARTIFACT_ROUTE)
        request = _request(context, _ARTIFACT_REQUEST_FIELDS)
        query_artifacts, _, artifact_error, _ = _tool_modules()
        result = query_artifacts(context["project_root"], request)
    except (KeyError, QueryActionError) as error:
        return _diagnostic(str(error))
    except Exception as error:
        if artifact_error is not None and isinstance(error, artifact_error):
            return _diagnostic(str(error))
        raise
    return {
        "result": _ARTIFACT_COMPLETED_RESULT,
        "effect_refs": [],
        "native_result": result,
    }


def journal_query_action(context: dict[str, Any]) -> dict[str, Any]:
    """Invoke CA-O-162 against its exact pre-Run or retained opaque frontier."""
    journal_error: type[Exception] | None = None
    try:
        _assert_route(context, _JOURNAL_ROUTE)
        request = _request(context, _JOURNAL_REQUEST_FIELDS)
        prepared = context.get("journal_preparation")
        if not isinstance(prepared, JournalPreparation):
            return _diagnostic("journal-snapshot-preparation-unavailable", blocked=True)
        if prepared.diagnostic is not None:
            return _diagnostic(prepared.diagnostic, blocked=prepared.diagnostic in {"changed-source", "journal-unavailable"})
        supplied_snapshot = request.pop("snapshot", None)
        if prepared.snapshot is not None:
            if supplied_snapshot is not None:
                return _diagnostic("unexpected-client-snapshot")
            snapshot = prepared.snapshot
        else:
            snapshot = supplied_snapshot
            if snapshot is None:
                return _diagnostic("journal-snapshot-unavailable", blocked=True)
        _, tools, _, journal_error = _tool_modules()
        _, query = tools
        result = query(snapshot, request)
    except (KeyError, QueryActionError) as error:
        return _diagnostic(str(error))
    except Exception as error:
        if journal_error is not None and isinstance(error, journal_error):
            return _diagnostic(getattr(error, "code", "journal-query-rejected"))
        raise
    status = result.get("status")
    if status in {"complete", "incomplete"}:
        return {
            "result": _JOURNAL_COMPLETED_RESULT,
            "effect_refs": [],
            "native_result": result,
        }
    if status == "blocked":
        return {
            "result": "diagnostic", "terminal_outcome": "interrupted_pending",
            "effect_refs": [], "native_result": result,
        }
    return {"result": "diagnostic", "terminal_outcome": "failed", "effect_refs": [], "native_result": result}


ACTION_HANDLERS = {
    "CA-O-159": artifact_query_action,
    "CA-O-162": journal_query_action,
}


__all__ = [
    "ACTION_HANDLERS",
    "JournalPreparation",
    "QueryActionError",
    "prepare_journal_query",
    "validate_query_parameters",
]
