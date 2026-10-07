"""Terminalize the one C517-authorized N15 effect whose outcome is unknown.

This is intentionally not a recovery executor.  It authenticates retained
historical carriers, validates current resolver authority, records only the
existing ``interrupted`` facts, and stores a companion record.  It never opens
Docker, a Unit runner, a selected dispatcher, or DBOS history storage.

The private ``_load_admitted_state`` and ``_current_resolver_authority`` read
boundaries are intentionally narrow test seams.  They are not public APIs and
the public operation accepts exactly ``(root, request)``.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


_APP_ROOT = Path(__file__).resolve().parent
_TOOLS_ROOT = _APP_ROOT.parents[1] / "201_TOOLS"
_RELEASE_TOOLS = _TOOLS_ROOT / "RELEASE_VERSION"
_MCP_ROOT = _APP_ROOT.parents[1] / "204_MCP"
for _location in (_TOOLS_ROOT, _RELEASE_TOOLS, _MCP_ROOT):
    if str(_location) not in sys.path:
        sys.path.insert(0, str(_location))

import work_journal  # noqa: E402
from release_checkpoint import derive_unknown_effect_terminal_checkpoint, load_release_checkpoint  # noqa: E402
from selected_execution import SelectedExecution, SelectedExecutionError, canonical_json  # noqa: E402
import selected_run_recovery as _selected_run_recovery  # noqa: E402
from workflow_run_support import LazyRunTracker, RunExecutionSession, _canonical_digest, _validate_common  # noqa: E402


_OPERATION = "resolve_release_unknown_effect"
_RUN_ID = "release-epic-resume-20261006-N15"
_REQUEST_IDENTITY = "5228bc2214ef3868794ae48f12c435c266587fd856fcefdd4598612b3ba80ec4"
_SNAPSHOT_SHA256 = "3bfdd04e1b9901c97a6af49c59e01731c456ea5313816db657457e94bd35a9f7"
_AUTHORIZATION_REF = ".caprmedio_caprmedio/01_concern/CA-C-517-QUESTION--resolve-the-unknown-n15-unit-outcome.md"
_AUTHORIZATION_SHA256 = "1d3d7c3c1d10827362952d684193fe844e634d18dfa5098a32f54af4863974d4"
_CHECKPOINT_SHA256 = "71d93f97c0f07b84e94d49d5bd18a4ab83d86e3e52d00e39368ce881153a4344"
_RESOLUTION_FILENAME = "release_unknown_effect_resolution.json"
_TERMINAL_CHECKPOINT_FILENAME = "release_unknown_effect_terminal_checkpoint.json"
_UNKNOWN_REASON = "unknown_effect"
_PIN_IDS = ("CA-R-1895", "CA-M-351", "CA-E-594", "CA-D-589")
_PIN_FIELDS = frozenset({"atom_id", "version", "source_path", "digest"})
_REQUEST_FIELDS = frozenset({
    "operation", "run_id", "request_identity", "authorization_ref", "authorization_sha256",
    "expected_checkpoint_sha256",
})
_RESOLUTION_FIELDS = frozenset({
    "schema", "resolution_kind", "run_id", "workflow_run_id", "step_run_id", "action_run_id",
    "old_checkpoint_sha256", "authorization_ref", "authorization_sha256", "approved_authority_pins",
    "event_refs", "unknown_reason",
})
_DIGEST = re.compile(r"^[0-9a-f]{64}$")


class _Blocked(ValueError):
    """One closed pre-write refusal for this exceptional resolution."""


@dataclass(frozen=True)
class _ResolutionState:
    root: Path
    folder: Path
    execution: dict[str, Any]
    session: RunExecutionSession
    terminal_checkpoint: dict[str, Any]
    terminal_checkpoint_ref: str
    resolution_ref: str


@dataclass(frozen=True)
class _ResolutionPreflight:
    """Opaque proof that lets the adapter avoid a cancellation on bad input.

    The helper does not consume this object as an authority token: it repeats
    every check under its lock immediately before its private cancellation
    seam.  The adapter uses the object only to distinguish an admitted
    no-write preflight from the closed response mapping.
    """

    root: Path
    request: dict[str, str]


def _blocked(request: Mapping[str, Any] | object, reason: str) -> dict[str, str]:
    run_id = request.get("run_id") if isinstance(request, Mapping) else None
    return {
        "operation": _OPERATION,
        "run_id": run_id if isinstance(run_id, str) else "",
        "disposition": "blocked",
        "blocked_reason": reason,
    }


def _request(value: Mapping[str, Any]) -> dict[str, str]:
    if not isinstance(value, Mapping) or set(value) != _REQUEST_FIELDS:
        raise _Blocked("request must contain exactly the six unknown-effect resolution fields")
    result: dict[str, str] = {}
    for key in _REQUEST_FIELDS:
        item = value.get(key)
        if not isinstance(item, str) or not item:
            raise _Blocked(f"{key} must be a non-empty string")
        result[key] = item
    expected = {
        "operation": _OPERATION,
        "run_id": _RUN_ID,
        "request_identity": _REQUEST_IDENTITY,
        "authorization_ref": _AUTHORIZATION_REF,
        "authorization_sha256": _AUTHORIZATION_SHA256,
        "expected_checkpoint_sha256": _CHECKPOINT_SHA256,
    }
    if result != expected:
        raise _Blocked("request does not bind the one admitted N15 unknown-effect resolution")
    return result


def _root(value: Path | str) -> Path:
    try:
        root = Path(value).resolve(strict=True)
    except OSError as error:
        raise _Blocked("project root is unavailable") from error
    if root.is_symlink() or not root.is_dir():
        raise _Blocked("project root must be one regular directory")
    return root


def _regular_file(root: Path, relative: str, *, label: str) -> tuple[Path, bytes]:
    candidate = Path(relative)
    if not relative or candidate.is_absolute() or ".." in candidate.parts:
        raise _Blocked(f"{label} must be repository-relative")
    path = root
    try:
        for part in candidate.parts:
            path = path / part
            if path.is_symlink():
                raise _Blocked(f"{label} has a symlinked ancestor")
        if not path.is_file():
            raise _Blocked(f"{label} is unavailable")
        return path, path.read_bytes()
    except _Blocked:
        raise
    except OSError as error:
        raise _Blocked(f"{label} is unreadable") from error


def _read_json(root: Path, relative: str, *, label: str) -> tuple[Path, dict[str, Any], bytes]:
    path, raw = _regular_file(root, relative, label=label)
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise _Blocked(f"{label} is not one JSON object") from error
    if not isinstance(value, dict):
        raise _Blocked(f"{label} is not one JSON object")
    return path, value, raw


def _pin_shape(value: Any) -> dict[str, Any]:
    if not isinstance(value, Mapping) or set(value) != _PIN_FIELDS:
        raise _Blocked("resolver authority pin has an invalid shape")
    atom_id, version, source_path, digest = (
        value.get("atom_id"), value.get("version"), value.get("source_path"), value.get("digest"),
    )
    if (not isinstance(atom_id, str) or type(version) is not int or version < 1
            or not isinstance(source_path, str) or not isinstance(digest, str)
            or _DIGEST.fullmatch(digest) is None):
        raise _Blocked("resolver authority pin has an invalid identity")
    return {"atom_id": atom_id, "version": version, "source_path": source_path, "digest": digest}


def _pin(root: Path, value: Any) -> dict[str, Any]:
    pin = _pin_shape(value)
    source_path, digest = pin["source_path"], pin["digest"]
    _path, contents = _regular_file(root, source_path, label="resolver authority source")
    if hashlib.sha256(contents).hexdigest() != digest:
        raise _Blocked("resolver authority source is stale")
    try:
        text = contents.decode("utf-8")
    except UnicodeDecodeError as error:
        raise _Blocked("resolver authority source is not UTF-8") from error
    atom_match = re.search(r"(?m)^atom_id:\s*[\"']?([^\n\"']+)", text)
    version_match = re.search(r"(?m)^version:\s*[\"']?([^\n\"']+)", text)
    if (atom_match is None or version_match is None
            or atom_match.group(1).strip() != pin["atom_id"]
            or version_match.group(1).strip() != str(pin["version"])):
        raise _Blocked("resolver authority source metadata differs from its pin")
    return pin


def _current_resolver_authority(root: Path) -> list[dict[str, Any]]:
    """Read only the separate current D572 recovery-control selection.

    This does not re-admit the historical Unit Action's source.  Its old pin is
    evidence for an already-started occurrence, while these four sources are
    current authority for this separate terminalization decision.
    """
    try:
        from release_source_admission import derive_unknown_effect_resolver_authority
        selected = derive_unknown_effect_resolver_authority(root)
    except Exception as error:
        raise _Blocked("D572 unknown-effect resolver authority is unavailable") from error
    if not isinstance(selected, list) or len(selected) != len(_PIN_IDS):
        raise _Blocked("D572 unknown-effect resolver authority has an invalid shape")
    pins = [_pin(root, item) for item in selected]
    if [pin["atom_id"] for pin in pins] != list(_PIN_IDS):
        raise _Blocked("D572 unknown-effect resolver authority pins are missing, repeated, or out of order")
    return pins


def _authorization(root: Path) -> None:
    _path, contents = _regular_file(root, _AUTHORIZATION_REF, label="C517 authorization carrier")
    if hashlib.sha256(contents).hexdigest() != _AUTHORIZATION_SHA256:
        raise _Blocked("C517 authorization carrier is stale")


def _cancel_scheduler(root: Path, request: Mapping[str, str]) -> None:
    """Use the backend's DBOS client boundary; never open scheduler storage here.

    ``backend.cancel_release_unknown_effect_scheduler`` is intentionally the
    only scheduler capability accepted by this native guard.  It must cancel
    the old, exact workflow identity and return its confirmed ``CANCELLED``
    observation.  Tests replace this one private seam; production never
    reads or writes DBOS SQLite directly.
    """

    try:
        from backend import cancel_release_unknown_effect_scheduler
        observed = cancel_release_unknown_effect_scheduler(root, dict(request))
    except Exception as error:
        raise _Blocked(f"old N15 scheduler workflow was not cancelled: {error}") from error
    if (
        not isinstance(observed, Mapping)
        or set(observed) != {"workflow_run_id", "scheduler_status"}
        or observed.get("workflow_run_id") != _RUN_ID
        or observed.get("scheduler_status") != "CANCELLED"
    ):
        raise _Blocked("old N15 scheduler workflow lacks confirmed cancellation")


def _pending_original_event(root: Path, execution: Mapping[str, Any]) -> bool:
    """Reject any sealed pending event that belongs to the frozen N15 request."""
    try:
        runtime = work_journal.configured_runtime_root(root)
    except (OSError, RuntimeError) as error:
        raise _Blocked("configured runtime root is unavailable") from error
    pending = root / runtime / "state" / "work_journal" / "pending"
    if not pending.exists():
        return False
    if pending.is_symlink() or not pending.is_dir():
        raise _Blocked("pending Journal carrier is unsafe")
    request_id, action_id = execution.get("request_id"), execution.get("assigned_action_id")
    for carrier in pending.iterdir():
        if carrier.is_symlink() or not carrier.is_file() or carrier.suffix != ".json":
            raise _Blocked("pending Journal carrier is unsafe")
        try:
            payload = json.loads(carrier.read_text(encoding="utf-8"))
            event = json.loads(payload["event_bytes"])
        except (OSError, TypeError, KeyError, json.JSONDecodeError) as error:
            raise _Blocked("pending Journal carrier is invalid") from error
        session = event.get("llm_session") if isinstance(event, Mapping) else None
        if (isinstance(session, Mapping) and session.get("uuid") == request_id) or event.get("action_id") == action_id:
            return True
    return False


def _historical_tracker(root: Path) -> LazyRunTracker:
    """Provide the existing Journal writer without re-admitting an old effect."""
    return LazyRunTracker(
        root,
        source_observer=lambda _request: {"selected": True, "current": True, "observed": {}},
        executor=lambda _request, _session: {},
    )


def _read_exact_n15_evidence(root: Path, execution: Mapping[str, Any]) -> dict[str, Any]:
    """Read only N15's exact UUID-and-action Journal intersection.

    Normal selected-Run recovery deliberately treats a match on either field
    as a collision, because most selected Action identities are unique.  The
    frozen Release history instead reuses CA-O-165 across different Release
    runs.  This narrow reader leaves that generic guard untouched: it ignores
    another Run's action-only events, but fails closed if the frozen N15 UUID
    appears with any other Action identity.  All accepted events still pass
    the existing dispatch, bounded-carrier, sealed-event, receipt, and later
    ``RunExecutionSession.restore`` validation.
    """

    parsed = _validate_common(execution)
    dispatch = _selected_run_recovery.inspect_selected_run_dispatch(root, parsed)
    try:
        journal_root = root / work_journal.configured_journal_root(root)
        parts = _selected_run_recovery._journal_parts(root, journal_root)
    except (OSError, RuntimeError) as error:
        raise _Blocked("configured N15 Journal root is unavailable") from error
    records_seen = 0
    bytes_read = 0
    evidence: list[dict[str, Any]] = []
    for path in parts:
        try:
            raw = path.read_bytes()
        except OSError as error:
            raise _Blocked(f"canonical N15 Journal carrier is unreadable: {path.name}") from error
        if len(raw) > _selected_run_recovery.MAX_JOURNAL_CARRIER_BYTES:
            raise _Blocked("canonical N15 Journal carrier exceeds the read limit")
        bytes_read += len(raw)
        if bytes_read > _selected_run_recovery.MAX_JOURNAL_BYTES:
            raise _Blocked("N15 Journal scan exceeds the total byte read limit")
        if raw and not raw.endswith(b"\n"):
            raise _Blocked(f"canonical N15 Journal carrier lacks terminal newline: {path.name}")
        lines = raw.splitlines(keepends=True)
        for line_number, line in enumerate(lines, start=1):
            if records_seen >= _selected_run_recovery.MAX_JOURNAL_EVENTS:
                raise _Blocked("N15 Journal event scan exceeds the configured limit")
            try:
                event = json.loads(line)
            except json.JSONDecodeError as error:
                raise _Blocked(f"invalid JSON in canonical N15 Journal carrier {path.name}:{line_number}") from error
            if not isinstance(event, dict):
                raise _Blocked(f"non-object N15 Journal event in {path.name}:{line_number}")
            records_seen += 1
            session = event.get("llm_session")
            request_matches = isinstance(session, Mapping) and session.get("uuid") == parsed["request_id"]
            action_matches = event.get("action_id") == parsed["assigned_action_id"]
            if request_matches and not action_matches:
                raise _Blocked("N15 Journal evidence has a UUID-only identity match")
            if not request_matches:
                # CA-O-165 is intentionally shared among historical Release
                # runs.  An action-only match cannot identify N15.
                continue
            if event.get("schema_version") != 5 or event.get("kind") != "workflow_execution":
                raise _Blocked("N15 identity occurs in non-canonical workflow evidence")
            try:
                sealed = work_journal.validate_sealed_event(event)
            except work_journal.WorkJournalError as error:
                raise _Blocked("N15 Journal event is not canonically sealed") from error
            previous = b"".join(lines[: line_number - 1])
            appended = b"".join(lines[:line_number])
            evidence.append({
                "event": sealed,
                "receipt": {
                    "event_id": sealed["event_id"],
                    "action_id": sealed["action_id"],
                    "event_digest": sealed["event_digest"],
                    "carrier": path.relative_to(root).as_posix(),
                    "line": line_number,
                    "previous_carrier_digest": hashlib.sha256(previous).hexdigest(),
                    "appended_carrier_digest": hashlib.sha256(appended).hexdigest(),
                },
            })
    return {"dispatch": dispatch, "events": evidence}


def _interruption_prefix(session: RunExecutionSession, *, terminal_checkpoint_ref: str, resolution_ref: str) -> list[str]:
    """Return the only resumable prefix of the three N15 interruption facts."""

    prefix: list[str] = []
    missing = False
    for run_id in (f"{_RUN_ID}:step:5:action:1", f"{_RUN_ID}:step:5", _RUN_ID):
        if run_id in session.terminal:
            raise _Blocked("N15 Unit occurrence already has competing terminal evidence")
        interruption = session.interrupted.get(run_id)
        if interruption is None:
            missing = True
            continue
        if missing:
            raise _Blocked("N15 interruption facts are not one canonical Action-Step-Workflow prefix")
        if (
            interruption.get("outcome") != "interrupted_pending"
            or interruption.get("result_ref") != terminal_checkpoint_ref
            or interruption.get("report_ref") != resolution_ref
            or not isinstance(interruption.get("event_id"), str)
            or not interruption["event_id"]
        ):
            raise _Blocked("N15 interruption facts differ from the admitted unknown-effect resolution")
        prefix.append(interruption["event_id"])
    return prefix


def _require_historical_frontier(
    execution: Mapping[str, Any], private_run: Any, session: RunExecutionSession, *,
    terminal_checkpoint_ref: str, resolution_ref: str,
) -> list[str]:
    if (
        private_run.workflow_run_id != _RUN_ID
        or private_run.next_phase != 4
        or private_run.stopped is not False
        or private_run.in_progress is None
        or set(private_run.results) != {0, 1, 2, 3}
        or any(private_run.results[index].outcome != "completed" for index in range(4))
    ):
        raise _Blocked("Release checkpoint does not retain the admitted N15 unknown-effect frontier")
    context = private_run.in_progress
    if (
        context.step_run_id != f"{_RUN_ID}:step:5"
        or context.action_run_id != f"{_RUN_ID}:step:5:action:1"
        or context.step_atom_id != "CA-O-185"
        or context.action_atom_id != "CA-O-168"
    ):
        raise _Blocked("Release checkpoint in-progress occurrence differs from N15 Unit Action")
    for index in range(1, 5):
        for requested_id in (f"{_RUN_ID}:step:{index}", f"{_RUN_ID}:step:{index}:action:1"):
            terminal = session.terminal.get(requested_id)
            if not isinstance(terminal, Mapping) or terminal.get("outcome") != "completed":
                raise _Blocked("N15 completed predecessor Run evidence is incomplete")
    action = f"{_RUN_ID}:step:5:action:1"
    step = f"{_RUN_ID}:step:5"
    if (
        session.actual.get(_RUN_ID, {}).get("run_id") != _RUN_ID
        or session.actual.get(step, {}).get("run_id") != context.step_run_id
        or session.actual.get(action, {}).get("run_id") != context.action_run_id
    ):
        raise _Blocked("N15 Unit occurrence start evidence differs from the frozen occurrence")
    return _interruption_prefix(
        session, terminal_checkpoint_ref=terminal_checkpoint_ref, resolution_ref=resolution_ref,
    )


def _load_admitted_state(root: Path, request: Mapping[str, str]) -> _ResolutionState:
    """Read all historical evidence before the resolver opens a Journal lock."""
    selected = SelectedExecution(root)
    try:
        frozen = selected.load(_RUN_ID)
    except (OSError, SelectedExecutionError) as error:
        raise _Blocked("frozen N15 Release request is unavailable") from error
    saved = frozen.get("request") if isinstance(frozen, Mapping) else None
    execution_raw = saved.get("execution") if isinstance(saved, Mapping) else None
    if not isinstance(saved, Mapping) or saved.get("run_id") != _RUN_ID or not isinstance(execution_raw, Mapping):
        raise _Blocked("frozen N15 Release request has an invalid shape")
    try:
        execution = _validate_common(execution_raw)
    except Exception as error:
        raise _Blocked("frozen N15 Release request is invalid") from error
    snapshot = execution.get("parameters", {}).get("candidateSnapshotManifest") if isinstance(execution.get("parameters"), Mapping) else None
    if (
        execution.get("mode") != "execute"
        or execution.get("operation_route") != "release_version"
        or execution.get("request_id") != _RUN_ID
        or not isinstance(snapshot, Mapping)
        or snapshot.get("sha256") != _SNAPSHOT_SHA256
        or _canonical_digest(execution) != request["request_identity"]
    ):
        raise _Blocked("frozen N15 request does not bind its exact historical identity")
    folder = selected.run_directory(_RUN_ID)
    checkpoint_ref = (folder / "release_action_run.json").relative_to(root).as_posix()
    _checkpoint_path, checkpoint, raw_checkpoint = _read_json(
        root, checkpoint_ref, label="historical N15 checkpoint",
    )
    if hashlib.sha256(raw_checkpoint).hexdigest() != request["expected_checkpoint_sha256"]:
        raise _Blocked("historical N15 checkpoint bytes differ from the approved digest")
    try:
        private_run, recordings = load_release_checkpoint(
            checkpoint,
            expected_request=execution["parameters"],
            expected_workflow_run_id=_RUN_ID,
        )
        terminal_checkpoint = derive_unknown_effect_terminal_checkpoint(checkpoint)
        evidence = _read_exact_n15_evidence(root, execution)
        session = RunExecutionSession.restore(_historical_tracker(root), execution, evidence["events"])
    except Exception as error:
        raise _Blocked("historical N15 checkpoint or Journal evidence is not admitted") from error
    if set(recordings) != {0, 1, 2, 3} or _pending_original_event(root, execution):
        raise _Blocked("N15 retains a pending or non-canonical original event carrier")
    terminal_checkpoint_ref = (folder / _TERMINAL_CHECKPOINT_FILENAME).relative_to(root).as_posix()
    resolution_ref = (folder / _RESOLUTION_FILENAME).relative_to(root).as_posix()
    _require_historical_frontier(
        execution, private_run, session,
        terminal_checkpoint_ref=terminal_checkpoint_ref, resolution_ref=resolution_ref,
    )
    return _ResolutionState(
        root=root,
        folder=folder,
        execution=execution,
        session=session,
        terminal_checkpoint=terminal_checkpoint,
        terminal_checkpoint_ref=terminal_checkpoint_ref,
        resolution_ref=resolution_ref,
    )


def _record_value(*, authority: list[dict[str, Any]], event_refs: list[str]) -> dict[str, Any]:
    return {
        "schema": "release_unknown_effect_resolution_v1",
        "resolution_kind": _UNKNOWN_REASON,
        "run_id": _RUN_ID,
        "workflow_run_id": _RUN_ID,
        "step_run_id": f"{_RUN_ID}:step:5",
        "action_run_id": f"{_RUN_ID}:step:5:action:1",
        "old_checkpoint_sha256": _CHECKPOINT_SHA256,
        "authorization_ref": _AUTHORIZATION_REF,
        "authorization_sha256": _AUTHORIZATION_SHA256,
        "approved_authority_pins": authority,
        "event_refs": event_refs,
        "unknown_reason": _UNKNOWN_REASON,
    }


def _stored_authority(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list) or len(value) != len(_PIN_IDS):
        raise _Blocked("unknown-effect resolution companion has invalid approved authority pins")
    pins = [_pin_shape(item) for item in value]
    if [pin["atom_id"] for pin in pins] != list(_PIN_IDS):
        raise _Blocked("unknown-effect resolution companion has invalid approved authority pins")
    return pins


def _require_terminal_checkpoint(state: _ResolutionState) -> None:
    """Read and prove the companion without creating or replacing anything."""

    path = state.root / state.terminal_checkpoint_ref
    expected = canonical_json(state.terminal_checkpoint)
    if not path.exists() or path.is_symlink():
        raise _Blocked("unknown-effect resolution companion lacks its terminal checkpoint companion")
    _path, _payload, raw = _read_json(
        state.root, state.terminal_checkpoint_ref, label="unknown-effect terminal checkpoint companion",
    )
    if raw != expected:
        raise _Blocked("unknown-effect terminal checkpoint companion differs from the admitted stop frontier")


def _ensure_terminal_checkpoint(state: _ResolutionState) -> None:
    """Create the effect-free companion once, or prove its exact old bytes."""

    path = state.root / state.terminal_checkpoint_ref
    if path.exists() or path.is_symlink():
        _require_terminal_checkpoint(state)
        return
    # The existing selected-run writer uses a temp file, fsync, replacement,
    # and directory fsync.  The per-Run Journal lock makes this one creation
    # serial; we never replace an existing companion above.
    SelectedExecution._write(path, state.terminal_checkpoint)
    _require_terminal_checkpoint(state)


def _read_existing_resolution(root: Path, *, state: _ResolutionState) -> dict[str, Any] | None:
    relative = (Path(".caprmedio_install") / "workflow_orchestrator" / "runs" / _RUN_ID / _RESOLUTION_FILENAME).as_posix()
    path = root / relative
    if not path.exists():
        return None
    _path, record, _raw = _read_json(root, relative, label="unknown-effect resolution companion")
    if set(record) != _RESOLUTION_FIELDS:
        raise _Blocked("unknown-effect resolution companion has an invalid shape")
    authority = _stored_authority(record.get("approved_authority_pins"))
    expected = _record_value(authority=authority, event_refs=record.get("event_refs"))
    for key, value in expected.items():
        if key == "event_refs":
            continue
        if record.get(key) != value:
            raise _Blocked("unknown-effect resolution companion differs from the admitted N15 resolution")
    refs = record.get("event_refs")
    if (not isinstance(refs, list) or len(refs) != 3 or len(set(refs)) != 3
            or any(not isinstance(item, str) or not item for item in refs)):
        raise _Blocked("unknown-effect resolution companion has invalid canonical event references")
    _require_terminal_checkpoint(state)
    prefix = _interruption_prefix(
        state.session,
        terminal_checkpoint_ref=state.terminal_checkpoint_ref,
        resolution_ref=state.resolution_ref,
    )
    if prefix != refs:
        raise _Blocked("unknown-effect resolution companion does not bind the canonical Journal facts")
    return record


def _already_resolved(record: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "operation": _OPERATION,
        "run_id": _RUN_ID,
        "disposition": "already_resolved",
        "resolution_ref": (Path(".caprmedio_install") / "workflow_orchestrator" / "runs" / _RUN_ID / _RESOLUTION_FILENAME).as_posix(),
        "event_refs": list(record["event_refs"]),
        "unknown_reason": _UNKNOWN_REASON,
    }


def preflight(root: Path, request: Mapping[str, Any]) -> _ResolutionPreflight | dict[str, str]:
    """Verify a proposed resolution without cancellation or a write.

    A settled companion is returned before C517/D572 validation so a later
    legitimate source update cannot erase its historical observation.  An
    unrecorded decision requires the current guards, but cancellation remains
    exclusively in ``resolve_release_unknown_effect``.
    """

    try:
        sealed = _request(request)
        project_root = _root(root)
        with work_journal._event_lock(project_root, f"selected-release-recovery:{_RUN_ID}"):
            state = _load_admitted_state(project_root, sealed)
            existing = _read_existing_resolution(project_root, state=state)
            if existing is not None:
                return _already_resolved(existing)
            _authorization(project_root)
            _current_resolver_authority(project_root)
            return _ResolutionPreflight(root=project_root, request=sealed)
    except _Blocked as error:
        return _blocked(request, str(error))
    except Exception as error:
        return _blocked(request, f"resolution admission failed: {error}")


def resolve_release_unknown_effect(root: Path, request: Mapping[str, Any]) -> dict[str, Any]:
    """Resolve only the guarded N15 unknown effect, once.

    Under its per-Run lock it verifies retained history, invokes the one
    backend-owned scheduler cancellation seam, reopens history, writes the
    effect-free checkpoint companion, then records only missing members of
    the canonical Action, Step, Workflow interruption prefix.
    """
    try:
        sealed = _request(request)
        project_root = _root(root)
        with work_journal._event_lock(project_root, f"selected-release-recovery:{_RUN_ID}"):
            state = _load_admitted_state(project_root, sealed)
            existing = _read_existing_resolution(project_root, state=state)
            if existing is not None:
                return _already_resolved(existing)

            # A new carrier is a new authorization decision, so it must see
            # the current authorization source and exact current resolver
            # frontier before it asks the backend to stop the old scheduler
            # Run.  That request is the only DBOS interaction in this module.
            _authorization(project_root)
            authority = _current_resolver_authority(project_root)
            _cancel_scheduler(project_root, sealed)
            # The scheduler could have been running until cancellation.  Read
            # history again before writing: an observed concurrent terminal
            # fact turns this into a refusal, never a replacement history.
            state = _load_admitted_state(project_root, sealed)
            existing = _read_existing_resolution(project_root, state=state)
            if existing is not None:
                return _already_resolved(existing)
            _authorization(project_root)
            authority = _current_resolver_authority(project_root)
            _ensure_terminal_checkpoint(state)
            event_refs = _interruption_prefix(
                state.session,
                terminal_checkpoint_ref=state.terminal_checkpoint_ref,
                resolution_ref=state.resolution_ref,
            )
            ordered_runs = (
                f"{_RUN_ID}:step:5:action:1", f"{_RUN_ID}:step:5", _RUN_ID,
            )
            for actual_run_id in ordered_runs[len(event_refs):]:
                receipt = state.session.finish_run(
                    actual_run_id,
                    outcome="interrupted_pending",
                    result_ref=state.terminal_checkpoint_ref,
                    effect_refs=[],
                    report_ref=state.resolution_ref,
                )
                if receipt.get("disposition") != "interrupted" or not isinstance(receipt.get("event_id"), str):
                    raise _Blocked("canonical Journal could not record the unknown-effect interruption")
                event_refs.append(receipt["event_id"])
            if len(event_refs) != 3:
                raise _Blocked("canonical Journal did not retain all N15 interruption facts")
            record = _record_value(authority=authority, event_refs=event_refs)
            # The resolution record is last.  If a process stops between its
            # canonical facts, the next guarded invocation resumes only their
            # missing suffix; it cannot replay the Unit effect.
            SelectedExecution._write(state.root / state.resolution_ref, record)
            return {
                "operation": _OPERATION,
                "run_id": _RUN_ID,
                "disposition": "resolved",
                "resolution_ref": state.resolution_ref,
                "event_refs": event_refs,
                "unknown_reason": _UNKNOWN_REASON,
            }
    except _Blocked as error:
        return _blocked(request, str(error))
    except Exception as error:
        return _blocked(request, f"resolution admission failed: {error}")


# The adapter reaches this on the already-imported native callable.  It is a
# read-only hook only; no caller can pass the opaque result back to bypass the
# full locked admission in ``resolve_release_unknown_effect``.
resolve_release_unknown_effect.preflight = preflight  # type: ignore[attr-defined]


__all__ = ["resolve_release_unknown_effect"]
