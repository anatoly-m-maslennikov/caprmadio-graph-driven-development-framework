"""Shared, non-executable Work Journal persistence library.

This module retains schema-v1 helpers for existing generators and adds the
sealed schema-v2 persistence API used by ``APPEND_CHANGE_RECORDS``.  Tool CLI
entry points deliberately live in their respective Tool units.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import tomllib
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator, Mapping, Sequence
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from project_runtime import atomic_tempfile


MODULE_PATH = Path(__file__).resolve()
for _parent in MODULE_PATH.parents:
    if _parent.name == ".caprmedio_runtime":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
    if _parent.name == ".caprmedio_install":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
    if _parent.name == ".caprmedio":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break


SETTINGS_PATH = Path(".caprmedio_caprmedio/caprmedio_project_settings.toml")
EVENTS = (
    "started",
    "progressed",
    "completed",
    "failed",
    "interrupted",
    "abandoned",
    "recovered",
)
SEALED_SCHEMA_VERSION = 3
MAX_EVENTS_PER_PART = 100
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
AUTHOR_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")
REPLACEMENT_FIELDS = frozenset({"predecessor_atom_id", "successor_atom_ids"})


def repository_root(path: Path) -> Path:
    for candidate in (path.resolve(), *path.resolve().parents):
        if (candidate / SETTINGS_PATH).is_file():
            return candidate
    raise RuntimeError(f"cannot locate {SETTINGS_PATH} from {path}")


def current_timestamp(root: Path) -> str:
    settings = tomllib.loads((root / SETTINGS_PATH).read_text(encoding="utf-8"))
    value = settings.get("artifact_timestamps", {}).get("timezone", "local")
    if value == "local":
        moment = dt.datetime.now().astimezone()
    elif value == "UTC":
        moment = dt.datetime.now(dt.UTC)
    else:
        try:
            moment = dt.datetime.now(ZoneInfo(value))
        except ZoneInfoNotFoundError as error:
            raise RuntimeError(f"unknown artifact timestamp timezone: {value}") from error
    return moment.strftime("%Y-%m-%d %H:%M:%S")


class WorkJournalError(RuntimeError):
    """Stable machine-readable Work Journal failure."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


def canonical_json_bytes(value: object) -> bytes:
    """The canonical encoding used for event and receipt digests."""
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def canonical_json_digest(value: object) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _safe_relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise WorkJournalError("unsafe-carrier", f"Journal carrier is outside repository: {path}") from error


def _write_all(descriptor: int, payload: bytes) -> None:
    offset = 0
    while offset < len(payload):
        written = os.write(descriptor, payload[offset:])
        if written <= 0:
            raise OSError("could not write Work Journal payload")
        offset += written


def _atomic_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(path, "work_journal")
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(canonical_json_bytes(value) + b"\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise


def configured_journal_root(root: Path) -> Path:
    settings = tomllib.loads((root / SETTINGS_PATH).read_text(encoding="utf-8"))
    paths = settings.get("paths", {})
    control_value = paths.get("control_root")
    if not isinstance(control_value, str) or not control_value:
        raise RuntimeError("Project Settings requires paths.control_root")
    control = Path(control_value)
    if control.is_absolute() or ".." in control.parts or not control.parts:
        raise RuntimeError("paths.control_root must be a safe repository-relative path")
    canonical = control / "_journal"
    value = paths.get("journal_root", canonical.as_posix())
    if not isinstance(value, str) or not value:
        raise RuntimeError("paths.journal_root must be a non-empty string when provided")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise RuntimeError("paths.journal_root must be a safe repository-relative path")
    if path != canonical:
        raise RuntimeError("paths.journal_root must be exactly paths.control_root/_journal")
    legacy = control / "work_journal"
    if (root / legacy).exists() and not (root / canonical).exists():
        raise RuntimeError(
            "migration-pending: move paths.control_root/work_journal to paths.control_root/_journal before Journal admission"
        )
    return canonical


def _legacy_journal_root(root: Path) -> Path:
    """Return the former Journal location accepted only for sealed recovery."""
    return configured_journal_root(root).parent / "work_journal"


def _physical_journal_path(root: Path, reference: str) -> Path:
    """Map an old sealed carrier reference to its renamed Journal location.

    The returned location is only for filesystem I/O.  Callers retain the
    original ``reference`` bytes in any sealed append context or receipt.
    """
    path = Path(reference)
    legacy = _legacy_journal_root(root)
    if path.parts[: len(legacy.parts)] == legacy.parts:
        remainder = path.parts[len(legacy.parts) :]
        return root / configured_journal_root(root) / Path(*remainder)
    return root / path


def configured_runtime_root(root: Path) -> Path:
    settings = tomllib.loads((root / SETTINGS_PATH).read_text(encoding="utf-8"))
    value = settings.get("paths", {}).get("runtime_root", ".caprmedio_runtime")
    if not isinstance(value, str) or not value:
        raise RuntimeError("Project Settings requires paths.runtime_root")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path.parts != (".caprmedio_runtime",):
        raise RuntimeError("paths.runtime_root must be .caprmedio_runtime")
    return path


# Schema-v1 compatibility ---------------------------------------------------

def segment_path(root: Path, occurred_at: str) -> Path:
    """Return the legacy v1 carrier path for existing callers only."""
    return root / configured_journal_root(root) / f"src-work-journal-{occurred_at[:10]}.ndjson"


def event_record(
    *,
    root: Path,
    event: str,
    action_id: str,
    kind: str,
    scope: str,
    operation: str,
    session_id: str,
    subjects: list[str],
    outputs: list[str],
    preceding_event: str | None,
    details: dict[str, str],
    occurred_at: str | None = None,
) -> dict[str, object]:
    """Create a legacy v1 record without changing historic record semantics."""
    record: dict[str, object] = {
        "schema_version": 1,
        "event_id": str(uuid.uuid4()),
        "action_id": action_id,
        "event": event,
        "kind": kind,
        "occurred_at": occurred_at or current_timestamp(root),
        "session_id": session_id,
        "structural_scope": scope,
        "operation": operation,
        "governed_subjects": subjects,
        "produced_outputs": outputs,
    }
    if preceding_event:
        record["preceding_event"] = preceding_event
    if details:
        record["details"] = details
    return record


def append_record(root: Path, record: dict[str, object]) -> Path:
    """Append a legacy v1 record for pre-existing library callers."""
    path = segment_path(root, str(record["occurred_at"]))
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o644)
    try:
        _write_all(descriptor, canonical_json_bytes(record) + b"\n")
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    return path


# Schema-v2 sealed events ---------------------------------------------------

def event_digest(event: Mapping[str, Any]) -> str:
    unsigned = dict(event)
    unsigned.pop("event_digest", None)
    return canonical_json_digest(unsigned)


def with_event_digest(event: Mapping[str, Any]) -> dict[str, Any]:
    sealed = dict(event)
    sealed["event_digest"] = event_digest(sealed)
    return sealed


def _require_string(value: Mapping[str, Any], key: str) -> str:
    item = value.get(key)
    if not isinstance(item, str) or not item:
        raise WorkJournalError("invalid-event", f"{key} must be a non-empty string")
    return item


def _require_sha256(value: object, key: str) -> None:
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise WorkJournalError("invalid-event", f"{key} must be a lowercase SHA-256 digest")


def _validate_occurred_at(value: str) -> None:
    try:
        parsed = dt.datetime.fromisoformat(value)
    except ValueError as error:
        raise WorkJournalError("invalid-event", "occurred_at must be ISO-8601") from error
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise WorkJournalError("invalid-event", "occurred_at must be timezone-qualified")


def _validate_sources(value: object) -> None:
    if not isinstance(value, list):
        raise WorkJournalError("invalid-event", "sources must be an ordered array")
    prior: tuple[str, str, int] | None = None
    seen: set[tuple[str, str, int]] = set()
    for source in value:
        if not isinstance(source, dict):
            raise WorkJournalError("invalid-event", "each source must be an object")
        required = {"relation_type", "filename", "version"}
        if not required <= set(source):
            raise WorkJournalError("invalid-event", "source must contain relation_type, filename, and version")
        relation_type = source["relation_type"]
        filename = source["filename"]
        version = source["version"]
        if not isinstance(relation_type, str) or not relation_type:
            raise WorkJournalError("invalid-event", "source.relation_type must be a non-empty string")
        if not isinstance(filename, str) or not filename.endswith(".md"):
            raise WorkJournalError("invalid-event", "source.filename must be a Markdown filename")
        if not isinstance(version, int) or version < 1:
            raise WorkJournalError("invalid-event", "source.version must be a positive integer")
        key = (relation_type, filename, version)
        if key in seen:
            raise WorkJournalError("invalid-event", "sources must not contain duplicates")
        if prior is not None and key < prior:
            raise WorkJournalError("invalid-event", "sources must be in canonical order")
        seen.add(key)
        prior = key


def _validate_result(value: object, *, schema_version: int, subject_kind: str) -> None:
    if not isinstance(value, dict):
        raise WorkJournalError("invalid-event", "result must be an object")
    state = value.get("state")
    filename = value.get("filename")
    version = value.get("version")
    if state not in {"present", "removed"}:
        raise WorkJournalError("invalid-event", "result.state must be present or removed")
    if not isinstance(filename, str) or not filename or Path(filename).name != filename:
        raise WorkJournalError("invalid-event", "result.filename must be one path-segment name")
    if schema_version == 2 and not filename.endswith(".md"):
        raise WorkJournalError("invalid-event", "schema-v2 result.filename must be a Markdown filename")
    if type(version) is not int or version < 1:
        raise WorkJournalError("invalid-event", "result.version must be a positive integer")
    if {"before_path", "before_sha256", "action_message", "previous_result"} & set(value):
        raise WorkJournalError("invalid-event", "result contains forbidden duplicated prior state")
    if state == "present":
        expected = {"state", "filename", "version", "path", "sha256"}
        if schema_version == 3 and subject_kind == "folder":
            expected.add("entries")
        if set(value) != expected:
            raise WorkJournalError("invalid-event", "present result has invalid fields")
        path = value.get("path")
        if not isinstance(path, str) or not path or Path(path).is_absolute() or ".." in Path(path).parts:
            raise WorkJournalError("invalid-event", "result.path must be a safe repository-relative path")
        _require_sha256(value.get("sha256"), "result.sha256")
        if subject_kind == "folder":
            entries = value.get("entries")
            if not isinstance(entries, list) or not entries:
                raise WorkJournalError("invalid-event", "present folder result requires a non-empty ordered entry set")
            prior: str | None = None
            prefix = path.rstrip("/") + "/"
            for entry in entries:
                if not isinstance(entry, dict) or set(entry) != {"path", "sha256"}:
                    raise WorkJournalError("invalid-event", "folder entry must contain only path and sha256")
                entry_path = entry.get("path")
                if not isinstance(entry_path, str) or not entry_path.startswith(prefix) or Path(entry_path).is_absolute() or ".." in Path(entry_path).parts:
                    raise WorkJournalError("invalid-event", "folder entry path must be below result.path")
                if prior is not None and entry_path <= prior:
                    raise WorkJournalError("invalid-event", "folder entries must be uniquely ordered by path")
                _require_sha256(entry.get("sha256"), "result.entries.sha256")
                prior = entry_path
            relative_entries = [
                {"path": Path(entry["path"]).relative_to(path).as_posix(), "sha256": entry["sha256"]}
                for entry in entries
            ]
            if canonical_json_digest(relative_entries) != value.get("sha256"):
                raise WorkJournalError("invalid-event", "folder result digest must bind the canonical entry set")
    elif set(value) != {"state", "filename", "version"}:
        raise WorkJournalError("invalid-event", "removed result has invalid fields")


def _validate_replacement_payload(value: Mapping[str, Any]) -> None:
    present = REPLACEMENT_FIELDS & value.keys()
    if not present:
        return
    if present != REPLACEMENT_FIELDS:
        raise WorkJournalError("invalid-event", "predecessor_atom_id and successor_atom_ids must appear together")
    if (
        type(value["schema_version"]) is not int
        or value["schema_version"] != 3
        or value["event"] != "completed"
        or value.get("subject_kind") != "file"
        or value.get("action_type") not in {"MOVE", "MOVE+UPDATE"}
    ):
        raise WorkJournalError("invalid-event", "replacement payload requires a schema-v3 completed file MOVE or MOVE+UPDATE event")
    # CA-D-435 records the observed identity strings and their order exactly.
    # Atom-ID grammar, successor semantics, and archive placement belong to
    # CA-E-462, not Journal storage admission (CA-R-1491).
    if not isinstance(value["predecessor_atom_id"], str):
        raise WorkJournalError("invalid-event", "predecessor_atom_id must be a string")
    successors = value["successor_atom_ids"]
    if not isinstance(successors, list) or any(not isinstance(item, str) for item in successors):
        raise WorkJournalError("invalid-event", "successor_atom_ids must be an array of strings")


def _validate_workflow_event(value: dict[str, Any]) -> dict[str, Any]:
    """Admit execution evidence to the same Journal, not a file-change fiction."""
    expected = {'schema_version', 'kind', 'event_id', 'action_id', 'event', 'author',
                'occurred_at', 'llm_session', 'structural_scope', 'workflow_run_id',
                'workflow_name', 'step', 'outcome', 'report_path', 'details', 'event_digest'}
    if set(value) != expected or value.get('schema_version') != 4:
        raise WorkJournalError('invalid-event', 'workflow execution requires schema-v4 fields')
    if value.get('kind') != 'workflow_execution' or value.get('event') not in EVENTS:
        raise WorkJournalError('invalid-event', 'invalid workflow execution kind or event')
    for field in ('event_id', 'action_id', 'author', 'occurred_at', 'structural_scope',
                  'workflow_run_id', 'workflow_name', 'step', 'outcome', 'report_path'):
        _require_string(value, field)
    if not AUTHOR_RE.fullmatch(value['author']):
        raise WorkJournalError('invalid-event', 'author must be a full GitHub username')
    _validate_occurred_at(value['occurred_at'])
    session = value['llm_session']
    if not isinstance(session, dict) or set(session) != {'app', 'uuid'}:
        raise WorkJournalError('invalid-event', 'llm_session must contain only app and uuid')
    for field in ('app', 'uuid'):
        _require_string(session, field)
    path = Path(value['report_path'])
    if path.is_absolute() or '..' in path.parts or not path.parts:
        raise WorkJournalError('invalid-event', 'report_path must be repository-relative')
    if not isinstance(value['details'], dict):
        raise WorkJournalError('invalid-event', 'details must be an object')
    if value['event_digest'] != event_digest(value):
        raise WorkJournalError('invalid-event', 'event_digest does not match event')
    return value


def _validate_safe_ref(value: object, label: str, *, allow_none: bool = False) -> str | None:
    if value is None and allow_none:
        return None
    if not isinstance(value, str) or not value:
        raise WorkJournalError("invalid-event", f"{label} must be a non-empty safe repository-relative reference")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise WorkJournalError("invalid-event", f"{label} must be repository-relative")
    return value


def _validate_definition_binding(value: object, *, label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != {"kind", "atom_id", "version", "path", "digest"}:
        raise WorkJournalError("invalid-event", f"{label} must contain kind, atom_id, version, path, and digest")
    if value["kind"] not in {"workflow", "step", "action"}:
        raise WorkJournalError("invalid-event", f"{label}.kind is invalid")
    _require_string(value, "atom_id")
    if type(value["version"]) is not int or value["version"] < 1:
        raise WorkJournalError("invalid-event", f"{label}.version must be a positive integer")
    _validate_safe_ref(value["path"], f"{label}.path")
    _require_sha256(value["digest"], f"{label}.digest")
    return value


def _validate_workflow_event_v5(value: dict[str, Any]) -> dict[str, Any]:
    """Validate selected-run evidence without changing schema-v4 readers."""
    expected = {
        "schema_version", "kind", "event_id", "action_id", "event", "author", "occurred_at", "llm_session",
        "structural_scope", "initiative", "run", "definition_bindings", "input_ref", "outcome", "result_ref",
        "effect_refs", "report_ref", "redaction", "event_digest",
    }
    if set(value) != expected or value.get("schema_version") != 5:
        raise WorkJournalError("invalid-event", "workflow execution requires schema-v5 fields")
    if value.get("kind") != "workflow_execution" or value.get("event") not in EVENTS:
        raise WorkJournalError("invalid-event", "invalid workflow execution kind or event")
    for field in ("event_id", "action_id", "author", "occurred_at", "structural_scope"):
        _require_string(value, field)
    if not AUTHOR_RE.fullmatch(value["author"]):
        raise WorkJournalError("invalid-event", "author must be a full GitHub username")
    _validate_occurred_at(value["occurred_at"])
    session = value["llm_session"]
    if not isinstance(session, dict) or set(session) != {"app", "uuid"}:
        raise WorkJournalError("invalid-event", "llm_session must contain only app and uuid")
    _require_string(session, "app")
    _require_string(session, "uuid")
    initiative = value["initiative"]
    if not isinstance(initiative, dict) or set(initiative) - {"initiative_id", "instruction_summary", "initiative_ref"}:
        raise WorkJournalError("invalid-event", "initiative has unsupported fields")
    _require_string(initiative, "initiative_id")
    _require_string(initiative, "instruction_summary")
    if "initiative_ref" in initiative:
        _validate_safe_ref(initiative["initiative_ref"], "initiative.initiative_ref")
    run = value["run"]
    if not isinstance(run, dict) or set(run) - {"run_id", "kind", "definition", "parent_run_id", "predecessor_run_id", "successor_run_ids"}:
        raise WorkJournalError("invalid-event", "run has unsupported fields")
    _require_string(run, "run_id")
    if run.get("kind") not in {"workflow", "step", "action"}:
        raise WorkJournalError("invalid-event", "run.kind is invalid")
    definition = run.get("definition")
    if not isinstance(definition, dict):
        raise WorkJournalError("invalid-event", "run.definition must be an object")
    _validate_definition_binding({"kind": run["kind"], **definition}, label="run.definition")
    for relation in ("parent_run_id", "predecessor_run_id"):
        if relation in run:
            _require_string(run, relation)
            if run[relation] == run["run_id"]:
                raise WorkJournalError("invalid-event", f"run.{relation} cannot self-reference")
    if "successor_run_ids" in run:
        successors = run["successor_run_ids"]
        if not isinstance(successors, list) or not successors or len(set(successors)) != len(successors):
            raise WorkJournalError("invalid-event", "run.successor_run_ids must be a distinct non-empty list")
        for successor in successors:
            if not isinstance(successor, str) or not successor or successor == run["run_id"]:
                raise WorkJournalError("invalid-event", "run.successor_run_ids contains an invalid identity")
    bindings = value["definition_bindings"]
    if not isinstance(bindings, list) or not bindings:
        raise WorkJournalError("invalid-event", "definition_bindings must be a non-empty ordered list")
    prior: tuple[str, str, int, str] | None = None
    seen: set[tuple[str, str, int, str]] = set()
    for binding in bindings:
        _validate_definition_binding(binding, label="definition binding")
        key = (binding["kind"], binding["atom_id"], binding["version"], binding["path"])
        if key in seen or (prior is not None and key <= prior):
            raise WorkJournalError("invalid-event", "definition_bindings must be uniquely canonical")
        seen.add(key)
        prior = key
    run_key = (run["kind"], definition["atom_id"], definition["version"], definition["path"])
    if run_key not in seen:
        raise WorkJournalError("invalid-event", "definition_bindings must retain the Run definition")
    _validate_safe_ref(value["input_ref"], "input_ref")
    outcome = value["outcome"]
    if outcome is not None and outcome not in {"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"}:
        raise WorkJournalError("invalid-event", "outcome is invalid")
    event = value["event"]
    allowed_outcomes = {
        "started": {None}, "progressed": {None}, "completed": {"completed", "no_op"},
        "failed": {"failed", "partial"}, "abandoned": {"cancelled", "partial"},
        "interrupted": {"interrupted_pending"}, "recovered": {"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"},
    }
    if outcome not in allowed_outcomes[event]:
        raise WorkJournalError("invalid-event", "event and outcome do not have an admitted truthful mapping")
    result_ref = _validate_safe_ref(value["result_ref"], "result_ref", allow_none=True)
    report_ref = _validate_safe_ref(value["report_ref"], "report_ref", allow_none=True)
    if event in {"completed", "failed", "abandoned"} and result_ref is None:
        raise WorkJournalError("invalid-event", "terminal selected Run evidence requires result_ref")
    effect_refs = value["effect_refs"]
    if not isinstance(effect_refs, list) or len(set(effect_refs)) != len(effect_refs):
        raise WorkJournalError("invalid-event", "effect_refs must be a duplicate-free ordered list")
    for effect_ref in effect_refs:
        _validate_safe_ref(effect_ref, "effect_ref")
    if outcome == "no_op" and effect_refs:
        raise WorkJournalError("invalid-event", "no_op cannot carry a fictitious effect reference")
    redaction = value["redaction"]
    if not isinstance(redaction, dict) or set(redaction) != {"redacted", "fields"} or type(redaction["redacted"]) is not bool or not isinstance(redaction["fields"], list):
        raise WorkJournalError("invalid-event", "redaction must contain redacted and fields")
    if any(not isinstance(field, str) or not field for field in redaction["fields"]):
        raise WorkJournalError("invalid-event", "redaction.fields must contain non-empty field labels")
    if bool(redaction["fields"]) != redaction["redacted"]:
        raise WorkJournalError("invalid-event", "redaction flag must match listed redacted fields")
    _require_sha256(value.get("event_digest"), "event_digest")
    if value["event_digest"] != event_digest(value):
        raise WorkJournalError("event-digest-mismatch", f"sealed event {value['event_id']} has mismatched canonical bytes")
    return value


def validate_sealed_event(event: Mapping[str, Any]) -> dict[str, Any]:
    """Validate an event already sealed by COMMIT_CONTEXT without re-resolution."""
    value = dict(event)
    if value.get("schema_version") == 5:
        return _validate_workflow_event_v5(value)
    if value.get('schema_version') == 4 or value.get('kind') == 'workflow_execution':
        return _validate_workflow_event(value)
    if {"action_message", "before_path", "before_sha256", "session_id", "session"} & set(value):
        raise WorkJournalError("invalid-event", "event contains forbidden duplicated provenance or prior state")
    schema_version = value.get("schema_version")
    if schema_version not in {2, SEALED_SCHEMA_VERSION}:
        raise WorkJournalError("invalid-event", "schema_version must be 2 or 3")
    _require_string(value, "event_id")
    _require_string(value, "action_id")
    lifecycle = value.get("event")
    kind = value.get("kind")
    expected_change_kind = "governed_file_change" if schema_version == 2 else "governed_project_change"
    expected_state_kind = "governed_file_state" if schema_version == 2 else "governed_project_state"
    if lifecycle == "completed" and kind != expected_change_kind:
        raise WorkJournalError("invalid-event", f"completed event must be {expected_change_kind}")
    if lifecycle == "recovered" and kind != expected_state_kind:
        raise WorkJournalError("invalid-event", f"recovered event must be {expected_state_kind}")
    if lifecycle not in {"completed", "recovered"}:
        raise WorkJournalError("invalid-event", "event must be completed or recovered")
    author = _require_string(value, "author")
    if not AUTHOR_RE.fullmatch(author):
        raise WorkJournalError("invalid-event", "author must be a full GitHub username")
    occurred_at = _require_string(value, "occurred_at")
    _validate_occurred_at(occurred_at)
    session = value.get("llm_session")
    if not isinstance(session, dict) or set(session) != {"app", "uuid"}:
        raise WorkJournalError("invalid-event", "llm_session must contain only app and uuid")
    _require_string(session, "app")
    _require_string(session, "uuid")
    _require_string(value, "structural_scope")
    subject_kind = "file" if schema_version == 2 else value.get("subject_kind")
    if subject_kind not in {"file", "folder"}:
        raise WorkJournalError("invalid-event", "subject_kind must be file or folder")
    _validate_result(value.get("result"), schema_version=schema_version, subject_kind=subject_kind)
    _validate_replacement_payload(value)
    if kind == expected_change_kind:
        allowed = {
            "schema_version",
            "event_id",
            "action_id",
            "event",
            "kind",
            "author",
            "occurred_at",
            "llm_session",
            "structural_scope",
            "action_type",
            "sources",
            "result",
            "event_digest",
            "previous_result_event",
        }
        if schema_version == 3:
            allowed.add("subject_kind")
            allowed.update(REPLACEMENT_FIELDS)
        if not set(value) <= allowed:
            raise WorkJournalError("invalid-event", "governed_file_change contains unsupported fields")
        _validate_sources(value.get("sources"))
        action_type = value.get("action_type")
        if action_type not in {"ADD", "MOVE", "UPDATE", "MOVE+UPDATE", "REMOVE"}:
            raise WorkJournalError("invalid-event", "governed_file_change action_type is invalid")
        previous = value.get("previous_result_event")
        if action_type == "ADD" and previous is not None:
            raise WorkJournalError("invalid-event", "ADD must not name previous_result_event")
        if action_type != "ADD" and (not isinstance(previous, str) or not previous):
            raise WorkJournalError("invalid-event", "non-ADD must name previous_result_event")
    else:
        allowed = {
            "schema_version",
            "event_id",
            "action_id",
            "event",
            "kind",
            "author",
            "occurred_at",
            "llm_session",
            "structural_scope",
            "result",
            "recovery_evidence",
            "event_digest",
        }
        if schema_version == 3:
            allowed.add("subject_kind")
        if set(value) != allowed:
            raise WorkJournalError("invalid-event", "governed_file_state has invalid fields")
        if "action_type" in value or "previous_result_event" in value or "sources" in value:
            raise WorkJournalError("invalid-event", "governed_file_state must not carry change fields")
        evidence = value.get("recovery_evidence")
        if not isinstance(evidence, dict) or set(evidence) != {"git", "carrier"}:
            raise WorkJournalError("invalid-event", "recovered state requires git and carrier evidence")
        if not isinstance(evidence["git"], dict) or not evidence["git"]:
            raise WorkJournalError("invalid-event", "recovery git evidence must be non-empty")
        if not isinstance(evidence["carrier"], dict) or not evidence["carrier"]:
            raise WorkJournalError("invalid-event", "recovery carrier evidence must be non-empty")
    actual_digest = value.get("event_digest")
    _require_sha256(actual_digest, "event_digest")
    if actual_digest != event_digest(value):
        raise WorkJournalError("event-digest-mismatch", f"sealed event {value['event_id']} has mismatched canonical bytes")
    return value


def validate_partition(author: object, local_date: object, timezone: object) -> tuple[str, str, str]:
    if not isinstance(author, str) or not AUTHOR_RE.fullmatch(author):
        raise WorkJournalError("invalid-context", "author must be a full GitHub username")
    if not isinstance(local_date, str) or not DATE_RE.fullmatch(local_date):
        raise WorkJournalError("invalid-context", "local_date must be YYYY-MM-DD")
    if not isinstance(timezone, str) or not timezone:
        raise WorkJournalError("invalid-context", "timezone must be a non-empty sealed value")
    return author, local_date, timezone


def _part_path(root: Path, author: str, local_date: str, part: int) -> Path:
    return root / configured_journal_root(root) / f"{author}-{local_date}-part-{part}.ndjson"


def _part_paths(root: Path, author: str, local_date: str) -> list[tuple[int, Path]]:
    directory = root / configured_journal_root(root)
    if not directory.exists():
        return []
    pattern = re.compile(rf"^{re.escape(author)}-{re.escape(local_date)}-part-([1-9][0-9]*)\.ndjson$")
    paths: list[tuple[int, Path]] = []
    for path in directory.iterdir():
        if path.is_file() and (match := pattern.fullmatch(path.name)):
            paths.append((int(match.group(1)), path))
    paths.sort()
    for expected, (part, _) in enumerate(paths, start=1):
        if part != expected:
            raise WorkJournalError("journal-part-gap", f"Journal parts for {author} {local_date} are not contiguous")
    return paths


def _carrier_records(path: Path) -> tuple[bytes, list[dict[str, Any]]]:
    data = path.read_bytes() if path.exists() else b""
    if data and not data.endswith(b"\n"):
        raise WorkJournalError("invalid-carrier", f"Journal carrier lacks terminal newline: {path}")
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(data.splitlines(), start=1):
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            raise WorkJournalError("invalid-carrier", f"Journal JSON invalid at {path}:{line_number}") from error
        if not isinstance(record, dict):
            raise WorkJournalError("invalid-carrier", f"Journal record is not an object at {path}:{line_number}")
        records.append(record)
    return data, records


def _receipt(root: Path, path: Path, data: bytes, line: int, event: Mapping[str, Any]) -> dict[str, Any]:
    lines = data.splitlines(keepends=True)
    previous = b"".join(lines[: line - 1])
    appended = b"".join(lines[:line])
    return {
        "event_id": event["event_id"],
        "action_id": event["action_id"],
        "event_digest": event["event_digest"],
        "carrier": _safe_relative(path, root),
        "line": line,
        "previous_carrier_digest": _sha256(previous),
        "appended_carrier_digest": _sha256(appended),
    }


def _receipt_path(root: Path, event_id: str) -> Path:
    return root / configured_runtime_root(root) / "state" / "work_journal" / "receipts" / f"{event_id}.json"


def _all_journal_parts(root: Path) -> list[Path]:
    directory = root / configured_journal_root(root)
    if not directory.exists():
        return []
    return sorted(path for path in directory.glob("*.ndjson") if path.is_file())


def _existing_receipt(root: Path, event: Mapping[str, Any]) -> dict[str, Any] | None:
    """Find an Event identity globally, before any date-partition choice."""
    event_id = str(event["event_id"])
    digest = str(event["event_digest"])
    for path in _all_journal_parts(root):
        data, records = _carrier_records(path)
        for line, record in enumerate(records, start=1):
            if record.get("event_id") != event_id:
                continue
            if record.get("event_digest") != digest:
                raise WorkJournalError("identity-collision", f"event_id {event_id} already has different canonical bytes")
            return _receipt(root, path, data, line, event)
    receipt_path = _receipt_path(root, event_id)
    if receipt_path.is_file():
        try:
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise WorkJournalError("invalid-receipt", f"cannot read receipt for event_id {event_id}") from error
        if not isinstance(receipt, dict) or receipt.get("event_id") != event_id:
            raise WorkJournalError("invalid-receipt", f"receipt for event_id {event_id} is malformed")
        if receipt.get("event_digest") != digest:
            raise WorkJournalError("identity-collision", f"event_id {event_id} already has different canonical bytes")
        return receipt
    return None


@contextmanager
def _partition_lock(root: Path, author: str, local_date: str) -> Iterator[None]:
    locks = root / configured_runtime_root(root) / "state" / "work_journal" / "locks"
    locks.mkdir(parents=True, exist_ok=True)
    path = locks / f"{author}-{local_date}.lock"
    token = str(uuid.uuid4())
    deadline = time.monotonic() + 30.0
    descriptor: int | None = None
    while descriptor is None:
        try:
            descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise WorkJournalError("journal-lock-unavailable", f"Journal partition lock remains held: {path}")
            time.sleep(0.05)
    try:
        try:
            _write_all(descriptor, canonical_json_bytes({"token": token, "pid": os.getpid()}) + b"\n")
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    except BaseException:
        path.unlink(missing_ok=True)
        raise
    try:
        yield
    finally:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            value = {}
        if value.get("token") == token:
            path.unlink(missing_ok=True)


@contextmanager
def _event_lock(root: Path, event_id: str) -> Iterator[None]:
    """Serialize an Event identity across every author/date partition."""
    locks = root / configured_runtime_root(root) / "state" / "work_journal" / "locks" / "events"
    locks.mkdir(parents=True, exist_ok=True)
    path = locks / f"{_sha256(event_id.encode('utf-8'))}.lock"
    token = str(uuid.uuid4())
    deadline = time.monotonic() + 30.0
    descriptor: int | None = None
    while descriptor is None:
        try:
            descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise WorkJournalError("journal-lock-unavailable", f"Journal event lock remains held: {event_id}")
            time.sleep(0.05)
    try:
        try:
            _write_all(descriptor, canonical_json_bytes({"token": token, "pid": os.getpid()}) + b"\n")
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        yield
    finally:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            value = {}
        if value.get("token") == token:
            path.unlink(missing_ok=True)


def _open_part(root: Path, author: str, local_date: str) -> tuple[Path, bytes, list[dict[str, Any]]]:
    paths = _part_paths(root, author, local_date)
    if not paths:
        return _part_path(root, author, local_date, 1), b"", []
    part, path = paths[-1]
    data, records = _carrier_records(path)
    if len(records) < MAX_EVENTS_PER_PART:
        return path, data, records
    return _part_path(root, author, local_date, part + 1), b"", []


def _append_locked(root: Path, event: Mapping[str, Any], author: str, local_date: str, *, partition_ref: str | None = None) -> dict[str, Any]:
    existing = _existing_receipt(root, event)
    if existing is not None:
        return existing
    if partition_ref is None:
        path, before, records = _open_part(root, author, local_date)
    else:
        path = _physical_journal_path(root, partition_ref)
        before, records = _carrier_records(path)
    if len(records) >= MAX_EVENTS_PER_PART:
        raise WorkJournalError("journal-part-full", "sealed original Journal partition is full")
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = canonical_json_bytes(event) + b"\n"
    descriptor = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o644)
    try:
        _write_all(descriptor, payload)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    receipt = {
        "event_id": event["event_id"],
        "action_id": event["action_id"],
        "event_digest": event["event_digest"],
        "carrier": _safe_relative(path, root),
        "line": len(records) + 1,
        "previous_carrier_digest": _sha256(before),
        "appended_carrier_digest": _sha256(before + payload),
    }
    receipt_path = _receipt_path(root, str(event["event_id"]))
    _atomic_json(receipt_path, receipt)
    return receipt


def _validate_event_set(events: Sequence[Mapping[str, Any]], author: str) -> list[dict[str, Any]]:
    if not events:
        raise WorkJournalError("invalid-event-set", "at least one sealed event is required")
    sealed = [validate_sealed_event(event) for event in events]
    action_ids = {str(event["action_id"]) for event in sealed}
    if len(action_ids) != 1:
        raise WorkJournalError("invalid-event-set", "related events must share one action_id")
    if any(event["author"] != author for event in sealed):
        raise WorkJournalError("invalid-event-set", "related events must use the context author")
    event_ids = [str(event["event_id"]) for event in sealed]
    if len(set(event_ids)) != len(event_ids):
        raise WorkJournalError("invalid-event-set", "event set contains duplicate event_id values")
    return sealed


def append_sealed_events(
    root: Path,
    events: Sequence[Mapping[str, Any]],
    *,
    author: object,
    local_date: object,
    timezone: object,
    append_context: Mapping[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Append an ordered v2 event set with fsync and idempotent receipts.

    ``author``, ``local_date``, and ``timezone`` are sealed COMMIT_CONTEXT
    values.  They are validated and used as supplied; this library does not
    resolve a clock, user, or timezone.
    """
    sealed_author, sealed_date, sealed_timezone = validate_partition(author, local_date, timezone)
    sealed = _validate_event_set(events, sealed_author)
    configured_journal_root(root)
    partition_ref: str | None = None
    if append_context is not None:
        if len(sealed) != 1:
            raise WorkJournalError("invalid-context", "sealed append context supports exactly one event")
        context = validate_append_context(root, append_context)
        if (context["author"], context["local_date"], context["timezone"]) != (sealed_author, sealed_date, sealed_timezone):
            raise WorkJournalError("invalid-context", "append context must match supplied partition context")
        partition_ref = context["partition_ref"]
    receipts: list[dict[str, Any]] = []
    for event in sealed:
        with _event_lock(root, str(event["event_id"])):
            with _partition_lock(root, sealed_author, sealed_date):
                receipts.append(_append_locked(root, event, sealed_author, sealed_date, partition_ref=partition_ref))
    return receipts


def seal_append_context(
    root: Path,
    event: Mapping[str, Any],
    *,
    author: object,
    local_date: object,
    timezone: object,
) -> dict[str, Any]:
    """Seal the original append partition before a selected-run append attempt."""
    sealed_author, sealed_date, sealed_timezone = validate_partition(author, local_date, timezone)
    validate_sealed_event(event)
    path, _, _ = _open_part(root, sealed_author, sealed_date)
    context: dict[str, Any] = {
        "author": sealed_author,
        "local_date": sealed_date,
        "timezone": sealed_timezone,
        "partition_ref": _safe_relative(path, root),
    }
    context["append_context_digest"] = canonical_json_digest(context)
    return context


def validate_append_context(root: Path, context: Mapping[str, Any]) -> dict[str, Any]:
    """Verify an immutable append context without consulting the current clock."""
    value = dict(context)
    expected = {"author", "local_date", "timezone", "partition_ref", "append_context_digest"}
    if set(value) != expected:
        raise WorkJournalError("invalid-context", "append context has missing or unsupported fields")
    author, local_date, timezone = validate_partition(value["author"], value["local_date"], value["timezone"])
    partition_ref = _validate_safe_ref(value["partition_ref"], "partition_ref")
    expected_paths = (
        _safe_relative(_part_path(root, author, local_date, 1), root),
        _safe_relative(
            root / _legacy_journal_root(root) / f"{author}-{local_date}-part-1.ndjson",
            root,
        ),
    )
    patterns = tuple(
        re.compile(rf"^{re.escape(expected_path[:-len('1.ndjson')])}[1-9][0-9]*\.ndjson$")
        for expected_path in expected_paths
    )
    if not any(pattern.fullmatch(str(partition_ref)) for pattern in patterns):
        raise WorkJournalError("invalid-context", "partition_ref is not the original author/date Journal partition")
    actual = value.pop("append_context_digest")
    _require_sha256(actual, "append_context_digest")
    if actual != canonical_json_digest(value):
        raise WorkJournalError("invalid-context", "append context digest does not match canonical bytes")
    return {**value, "append_context_digest": actual}


def _pending_path(root: Path, event_id: str) -> Path:
    return root / configured_runtime_root(root) / "state" / "work_journal" / "pending" / f"{event_id}.json"


def store_pending_event(
    root: Path,
    event: Mapping[str, Any],
    append_context: Mapping[str, Any],
    *,
    result_ref: str | None,
    effect_refs: Sequence[str],
    diagnostic: str,
    retry_linkage: str | None = None,
) -> dict[str, Any]:
    """Persist retry-only evidence without issuing an effect or a new Run."""
    sealed = validate_sealed_event(event)
    context = validate_append_context(root, append_context)
    event_bytes = canonical_json_bytes(sealed)
    context_bytes = canonical_json_bytes(context)
    if result_ref is not None:
        _validate_safe_ref(result_ref, "result_ref")
    if any(_validate_safe_ref(effect_ref, "effect_ref") != effect_ref for effect_ref in effect_refs):
        raise WorkJournalError("invalid-pending", "effect_refs must be safe repository-relative references")
    if not isinstance(diagnostic, str) or not diagnostic:
        raise WorkJournalError("invalid-pending", "diagnostic must be non-empty")
    if retry_linkage is not None and (not isinstance(retry_linkage, str) or not retry_linkage):
        raise WorkJournalError("invalid-pending", "retry_linkage must be a non-empty string when supplied")
    pending: dict[str, Any] = {
        "event_id": sealed["event_id"],
        "event_digest": sealed["event_digest"],
        "event_bytes": event_bytes.decode("utf-8"),
        "event_bytes_digest": _sha256(event_bytes),
        "append_context_bytes": context_bytes.decode("utf-8"),
        "append_context_bytes_digest": _sha256(context_bytes),
        "result_ref": result_ref,
        "effect_refs": list(effect_refs),
        "diagnostic": diagnostic,
        "retry_linkage": retry_linkage,
    }
    path = _pending_path(root, str(sealed["event_id"]))
    if path.exists():
        try:
            prior = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise WorkJournalError("invalid-pending", f"cannot read pending evidence for {sealed['event_id']}") from error
        if not isinstance(prior, dict) or prior.get("event_bytes") != pending["event_bytes"] or prior.get("append_context_bytes") != pending["append_context_bytes"]:
            raise WorkJournalError("identity-collision", f"pending event_id {sealed['event_id']} has different immutable bytes")
        return prior
    _atomic_json(path, pending)
    return pending


def _read_pending_event(root: Path, event_id: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], Path]:
    if not isinstance(event_id, str) or not event_id:
        raise WorkJournalError("invalid-pending", "event_id must be a non-empty string")
    path = _pending_path(root, event_id)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise WorkJournalError("pending-not-found", f"no pending evidence for event_id {event_id}") from error
    except (OSError, json.JSONDecodeError) as error:
        raise WorkJournalError("invalid-pending", f"cannot read pending evidence for {event_id}") from error
    required = {"event_id", "event_digest", "event_bytes", "event_bytes_digest", "append_context_bytes", "append_context_bytes_digest", "result_ref", "effect_refs", "diagnostic", "retry_linkage"}
    if not isinstance(value, dict) or set(value) != required or value.get("event_id") != event_id:
        raise WorkJournalError("invalid-pending", f"pending evidence for {event_id} has invalid fields")
    event_bytes = value["event_bytes"]
    context_bytes = value["append_context_bytes"]
    if not isinstance(event_bytes, str) or not isinstance(context_bytes, str):
        raise WorkJournalError("invalid-pending", "pending evidence must retain immutable byte strings")
    encoded_event = event_bytes.encode("utf-8")
    encoded_context = context_bytes.encode("utf-8")
    if value["event_bytes_digest"] != _sha256(encoded_event) or value["append_context_bytes_digest"] != _sha256(encoded_context):
        raise WorkJournalError("invalid-pending", "pending evidence byte digest mismatch")
    try:
        event = json.loads(event_bytes)
        context = json.loads(context_bytes)
    except json.JSONDecodeError as error:
        raise WorkJournalError("invalid-pending", "pending evidence bytes are not JSON") from error
    if not isinstance(event, dict) or not isinstance(context, dict) or canonical_json_bytes(event) != encoded_event or canonical_json_bytes(context) != encoded_context:
        raise WorkJournalError("invalid-pending", "pending evidence is not canonical immutable JSON")
    sealed = validate_sealed_event(event)
    if sealed["event_id"] != event_id or sealed["event_digest"] != value["event_digest"]:
        raise WorkJournalError("invalid-pending", "pending event identity does not match immutable payload")
    return value, sealed, validate_append_context(root, context), path


def recover_pending_event(root: Path, event_id: str) -> dict[str, Any]:
    """Append exactly the pending original bytes in their sealed original partition."""
    _, event, context, path = _read_pending_event(root, event_id)
    receipt = append_sealed_events(
        root,
        [event],
        author=context["author"],
        local_date=context["local_date"],
        timezone=context["timezone"],
        append_context=context,
    )[0]
    path.unlink(missing_ok=True)
    return receipt


def register_selected_run_dispatch(
    root: Path,
    *,
    request_id: str,
    canonical_request_bytes: bytes,
) -> tuple[dict[str, Any], bool]:
    """Persist one accepted selected-run dispatch before any route effect.

    The carrier is runtime recovery evidence, not a second historical Journal.
    A process restart can therefore refuse to dispatch the same request again
    until it inspects or recovers the original evidence.
    """
    if not isinstance(request_id, str) or not request_id:
        raise WorkJournalError("invalid-dispatch", "request_id must be a non-empty string")
    if not isinstance(canonical_request_bytes, bytes) or not canonical_request_bytes:
        raise WorkJournalError("invalid-dispatch", "canonical_request_bytes must be non-empty bytes")
    try:
        parsed = json.loads(canonical_request_bytes)
    except json.JSONDecodeError as error:
        raise WorkJournalError("invalid-dispatch", "canonical request bytes must be JSON") from error
    if canonical_json_bytes(parsed) != canonical_request_bytes:
        raise WorkJournalError("invalid-dispatch", "request dispatch bytes must be canonical JSON")
    configured_journal_root(root)
    digest = _sha256(canonical_request_bytes)
    path = (
        root
        / configured_runtime_root(root)
        / "state"
        / "work_journal"
        / "selected_runs"
        / "requests"
        / f"{_sha256(request_id.encode('utf-8'))}.json"
    )
    value = {
        "schema_version": 1,
        "request_id": request_id,
        "canonical_request_bytes": canonical_request_bytes.decode("utf-8"),
        "canonical_request_bytes_digest": digest,
        "state": "accepted",
    }
    with _event_lock(root, f"selected-run-request:{request_id}"):
        if path.exists():
            try:
                prior = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as error:
                raise WorkJournalError("invalid-dispatch", f"cannot read selected-run dispatch for {request_id}") from error
            expected = {"schema_version", "request_id", "canonical_request_bytes", "canonical_request_bytes_digest", "state"}
            if not isinstance(prior, dict) or set(prior) != expected or prior.get("schema_version") != 1 or prior.get("request_id") != request_id:
                raise WorkJournalError("invalid-dispatch", f"selected-run dispatch for {request_id} has invalid fields")
            if prior.get("canonical_request_bytes") != canonical_request_bytes.decode("utf-8") or prior.get("canonical_request_bytes_digest") != digest:
                raise WorkJournalError("request-id-conflict", f"request_id {request_id} already has different accepted dispatch bytes")
            if prior.get("state") != "accepted":
                raise WorkJournalError("invalid-dispatch", f"selected-run dispatch for {request_id} has invalid state")
            return prior, False
        _atomic_json(path, value)
        return value, True


def predict_sealed_event_receipts(
    root: Path,
    events: Sequence[Mapping[str, Any]],
    *,
    author: object,
    local_date: object,
    timezone: object,
) -> list[dict[str, Any]]:
    """Return complete side-effect-free carrier and receipt predictions."""
    sealed_author, sealed_date, _ = validate_partition(author, local_date, timezone)
    sealed = _validate_event_set(events, sealed_author)
    parts = _part_paths(root, sealed_author, sealed_date)
    simulated: dict[Path, tuple[bytes, list[dict[str, Any]]]] = {
        path: _carrier_records(path) for _, path in parts
    }
    output: list[dict[str, Any]] = []
    for event in sealed:
        existing = _existing_receipt(root, event)
        if existing is not None:
            output.append({**existing, "disposition": "reused"})
            continue
        if not parts:
            part, path = 1, _part_path(root, sealed_author, sealed_date, 1)
            parts.append((part, path))
        else:
            part, path = parts[-1]
        before, records = simulated.get(path, (b"", []))
        if len(records) >= MAX_EVENTS_PER_PART:
            part += 1
            path = _part_path(root, sealed_author, sealed_date, part)
            parts.append((part, path))
            before, records = simulated.get(path, (b"", []))
        payload = canonical_json_bytes(event) + b"\n"
        simulated[path] = (before + payload, [*records, dict(event)])
        output.append(
            {
                "event_id": event["event_id"],
                "action_id": event["action_id"],
                "event_digest": event["event_digest"],
                "carrier": _safe_relative(path, root),
                "line": len(records) + 1,
                "previous_carrier_digest": _sha256(before),
                "appended_carrier_digest": _sha256(before + payload),
                "disposition": "predicted",
            }
        )
    return output
