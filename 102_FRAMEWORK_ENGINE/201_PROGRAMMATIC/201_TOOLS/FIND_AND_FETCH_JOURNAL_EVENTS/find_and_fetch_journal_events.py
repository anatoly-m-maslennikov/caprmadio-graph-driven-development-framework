"""Read-only queries over a sealed canonical Events Journal frontier.

This module deliberately has no RunJournal dependency: a future dispatch adapter
captures a snapshot *before* it records an actual invocation, then calls
``query(snapshot, request)``.  The public functions only read carrier bytes.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import secrets
import stat
import sys
import time
import tomllib
from pathlib import Path
from typing import Any, Mapping

try:
    from query_filter import (
        MISSING,
        QueryFilterError,
        collect_selectors,
        decode_json_pointer,
        evaluate_filter,
        parse_filter_with_stats,
        resolve_json_pointer,
    )
except ModuleNotFoundError:  # Package import from the repository root.
    _ARTIFACT_TOOL = Path(__file__).resolve().parents[1] / "FIND_AND_FETCH_ARTIFACTS"
    sys.path.insert(0, str(_ARTIFACT_TOOL))
    from query_filter import (  # type: ignore[no-redef]
        MISSING,
        QueryFilterError,
        collect_selectors,
        decode_json_pointer,
        evaluate_filter,
        parse_filter_with_stats,
        resolve_json_pointer,
    )


class JournalQueryError(ValueError):
    """A stable, non-secret diagnostic for an unavailable Journal frontier."""

    def __init__(self, code: str, message: str | None = None) -> None:
        self.code = code
        super().__init__(message or code)


_SETTINGS = Path("caprmedio_project_settings.toml")
_DEFAULT_SETTINGS = Path(
    "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/"
    "caprmedio_framework_default_settings.toml"
)
_INSTANCE_SETTINGS = Path(
    "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/"
    "caprmedio_framework_settings.toml"
)
_LIMIT_NAMES = (
    "max_request_bytes",
    "max_grammar_depth",
    "max_filter_tokens",
    "max_in_members",
    "max_selected_fields",
    "max_page_size",
    "max_snapshot_members",
    "max_file_bytes",
    "max_total_read_bytes",
    "timeout_seconds",
    "max_findings",
)
_REQUEST_FIELDS = frozenset({"filter", "mode", "select", "limit", "cursor", "limits"})
_SENSITIVE_NAMES = frozenset(
    {
        "api_key",
        "apikey",
        "authorization",
        "credential",
        "credentials",
        "password",
        "private_key",
        "secret",
        "secrets",
        "token",
    }
)
_RETAINED_SNAPSHOTS: dict[str, bytes] = {}
_PUBLIC_SNAPSHOT_KEYS = frozenset(
    {"snapshot_handle", "id", "source_root", "prefix_bytes", "prefix_digest", "event_ids"}
)


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _json_bytes(value: Any) -> bytes:
    try:
        return json.dumps(
            value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise JournalQueryError("invalid-request", "request must contain only RFC 8259 values") from error


def _safe_regular_file(path: Path, code: str) -> None:
    try:
        file_stat = path.lstat()
    except OSError as error:
        raise JournalQueryError(code) from error
    if path.is_symlink() or not path.is_file() or not stat.S_ISREG(file_stat.st_mode):
        raise JournalQueryError(code)


def _read_toml(path: Path, code: str) -> dict[str, Any]:
    _safe_regular_file(path, code)
    try:
        value = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise JournalQueryError(code) from error
    if not isinstance(value, dict):
        raise JournalQueryError(code)
    return value


def _control_and_settings(root: Path) -> tuple[Path, dict[str, Any], dict[str, Any]]:
    if root.is_symlink() or not root.is_dir():
        raise JournalQueryError("invalid-project-root")
    root = root.resolve()
    settings = _read_toml(root / ".caprmedio_caprmedio" / _SETTINGS, "project-settings-unavailable")
    paths = settings.get("paths")
    control_name = paths.get("control_root") if isinstance(paths, dict) else None
    if not isinstance(control_name, str) or not control_name:
        raise JournalQueryError("invalid-control-root")
    control_relative = Path(control_name)
    if control_relative.is_absolute() or ".." in control_relative.parts or control_relative == Path("."):
        raise JournalQueryError("invalid-control-root")
    control = root / control_relative
    if control.is_symlink() or not control.is_dir():
        raise JournalQueryError("invalid-control-root")
    defaults = _read_toml(control / _DEFAULT_SETTINGS, "default-settings-unavailable")
    instance_path = control / _INSTANCE_SETTINGS
    instance = _read_toml(instance_path, "instance-settings-unavailable") if instance_path.exists() else {}
    return control, defaults, instance


def _positive_int(value: Any, name: str) -> int:
    if type(value) is not int or value <= 0:
        raise JournalQueryError("invalid-limit", f"{name} must be a positive integer")
    return value


def _query_section(value: Mapping[str, Any] | None, code: str) -> Mapping[str, Any]:
    if value is None:
        return {}
    section = value.get("query")
    if section is None:
        return {}
    if not isinstance(section, Mapping):
        raise JournalQueryError(code)
    return section


def _resolve_limits(
    defaults: Mapping[str, Any], instance: Mapping[str, Any], override: Mapping[str, Any] | None
) -> tuple[dict[str, int], dict[str, str]]:
    default_query = _query_section(defaults, "invalid-default-query-settings")
    instance_query = _query_section(instance, "invalid-instance-query-settings")
    if override is not None and not isinstance(override, Mapping):
        raise JournalQueryError("invalid-limit-overrides")
    if override is not None and any(name not in _LIMIT_NAMES for name in override):
        raise JournalQueryError("invalid-limit-overrides")
    values: dict[str, int] = {}
    sources: dict[str, str] = {}
    for name in _LIMIT_NAMES:
        if override is not None and name in override:
            raw, source = override[name], "request"
        elif name in instance_query:
            raw, source = instance_query[name], "instance"
        elif name in default_query:
            raw, source = default_query[name], "default"
        else:
            raise JournalQueryError("unresolved-limit", name)
        values[name] = _positive_int(raw, name)
        sources[name] = source
    return values, sources


def _decode_event(raw: bytes) -> dict[str, Any]:
    def duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        output: dict[str, Any] = {}
        for key, value in pairs:
            if key in output:
                raise JournalQueryError("duplicate-json-key")
            output[key] = value
        return output

    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=duplicate_keys)
    except JournalQueryError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise JournalQueryError("malformed-event") from error
    if not isinstance(value, dict):
        raise JournalQueryError("malformed-event")
    event_id = value.get("event_id")
    if not isinstance(event_id, str) or not event_id:
        raise JournalQueryError("missing-event-id")
    return value


def _read_member(path: Path, *, max_file_bytes: int, total_read: int, max_total_read: int) -> tuple[bytes, int]:
    _safe_regular_file(path, "unreadable-member")
    try:
        size = path.stat().st_size
    except OSError as error:
        raise JournalQueryError("unreadable-member") from error
    if size > max_file_bytes:
        raise JournalQueryError("file-limit-exceeded")
    if total_read + size > max_total_read:
        raise JournalQueryError("total-read-limit-exceeded")
    try:
        content = path.read_bytes()
    except OSError as error:
        raise JournalQueryError("unreadable-member") from error
    if len(content) != size:
        raise JournalQueryError("incomplete-read")
    return content, total_read + size


def _member_events(relative: str, content: bytes) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    offset = 0
    for line_number, line in enumerate(content.splitlines(keepends=True), start=1):
        raw = line.rstrip(b"\r\n")
        if not raw:
            raise JournalQueryError("malformed-event")
        event = _decode_event(raw)
        entries.append(
            {
                "event_id": event["event_id"],
                "event": event,
                "member": relative,
                "line": line_number,
                "offset": offset,
                "raw_digest": _sha256(raw),
            }
        )
        offset += len(line)
    if content and not entries:
        raise JournalQueryError("malformed-event")
    return entries


def _snapshot_core(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "project_root": snapshot["project_root"],
        "source_root": snapshot["source_root"],
        "prefix_bytes": snapshot["prefix_bytes"],
        "prefix_digest": snapshot["prefix_digest"],
        "members": snapshot["members"],
        "records": snapshot["records"],
        "limits": snapshot["limits"],
        "limit_sources": snapshot["limit_sources"],
        "capture_read_bytes": snapshot["capture_read_bytes"],
    }


def _snapshot_public(snapshot: Mapping[str, Any], handle: str) -> dict[str, Any]:
    return {
        "snapshot_handle": handle,
        "id": snapshot["id"],
        "source_root": snapshot["source_root"],
        "prefix_bytes": snapshot["prefix_bytes"],
        "prefix_digest": snapshot["prefix_digest"],
        "event_ids": [record["event_id"] for record in snapshot["records"]],
    }


def _retain_snapshot(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    """Keep the authority-bearing snapshot server-side and return only a capability."""
    handle = secrets.token_urlsafe(32)
    _RETAINED_SNAPSHOTS[handle] = _json_bytes(snapshot)
    return _snapshot_public(snapshot, handle)


def _resolve_retained_snapshot(value: Any) -> tuple[dict[str, Any], dict[str, Any]]:
    """Reject unknown or altered public handles without accepting caller state."""
    if not isinstance(value, Mapping) or set(value) != _PUBLIC_SNAPSHOT_KEYS:
        raise JournalQueryError("invalid-snapshot")
    handle = value.get("snapshot_handle")
    if not isinstance(handle, str) or not handle:
        raise JournalQueryError("invalid-snapshot")
    payload = _RETAINED_SNAPSHOTS.get(handle)
    if payload is None:
        raise JournalQueryError("unknown-snapshot")
    try:
        snapshot = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:  # retained corruption is never caller input
        raise JournalQueryError("invalid-retained-snapshot") from error
    if not isinstance(snapshot, dict):
        raise JournalQueryError("invalid-retained-snapshot")
    expected = _snapshot_public(snapshot, handle)
    if dict(value) != expected:
        raise JournalQueryError("changed-snapshot")
    return snapshot, expected


def capture_snapshot(
    root: str | Path,
    *,
    instance_settings: Mapping[str, Any] | None = None,
    limits: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Seal canonical NDJSON members once, before any query execution evidence.

    ``root`` is the selected Project root.  The only Journal location is the
    configured control root plus ``_journal``; callers cannot supply a Journal
    path.  No write, Run, or directory re-enumeration is performed by ``query``.
    """
    project_root = Path(root)
    control, defaults, installed_instance = _control_and_settings(project_root)
    if instance_settings is not None:
        if not isinstance(instance_settings, Mapping):
            raise JournalQueryError("invalid-instance-query-settings")
        installed_instance = dict(installed_instance)
        installed_query = dict(_query_section(installed_instance, "invalid-instance-query-settings"))
        installed_query.update(_query_section(instance_settings, "invalid-instance-query-settings"))
        installed_instance["query"] = installed_query
    configured, sources = _resolve_limits(defaults, installed_instance, limits)
    journal = control / "_journal"
    if journal.is_symlink() or not journal.is_dir():
        raise JournalQueryError("journal-unavailable")
    deadline = time.monotonic() + configured["timeout_seconds"]
    total_read = 0
    members: list[dict[str, Any]] = []
    records: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    try:
        paths = sorted(journal.iterdir(), key=lambda path: path.name.encode("utf-8"))
    except OSError as error:
        raise JournalQueryError("journal-unavailable") from error
    carriers = [path for path in paths if path.name.endswith(".ndjson")]
    if len(carriers) > configured["max_snapshot_members"]:
        raise JournalQueryError("snapshot-member-limit-exceeded")
    for carrier in carriers:
        if time.monotonic() > deadline:
            raise JournalQueryError("timeout-exceeded")
        if carrier.is_symlink():
            raise JournalQueryError("symlink-member")
        relative = carrier.relative_to(project_root.resolve()).as_posix()
        content, total_read = _read_member(
            carrier,
            max_file_bytes=configured["max_file_bytes"],
            total_read=total_read,
            max_total_read=configured["max_total_read_bytes"],
        )
        if time.monotonic() > deadline:
            raise JournalQueryError("timeout-exceeded")
        member = {"ref": relative, "prefix_bytes": len(content), "prefix_digest": _sha256(content)}
        members.append(member)
        for record in _member_events(relative, content):
            event_id = record["event_id"]
            if event_id in seen_ids:
                raise JournalQueryError("duplicate-event-id")
            seen_ids.add(event_id)
            records.append(record)
    records.sort(key=lambda record: record["event_id"].encode("utf-8"))
    # The prefix was already bounded and read above.  For a single carrier its
    # digest is exactly the retained carrier-prefix digest; otherwise retain a
    # deterministic digest of the ordered carrier-prefix evidence.
    if len(members) == 1:
        prefix_digest = members[0]["prefix_digest"]
    else:
        prefix_digest = _sha256(
            _json_bytes([(member["ref"], member["prefix_bytes"], member["prefix_digest"]) for member in members])
        )
    snapshot: dict[str, Any] = {
        "project_root": str(project_root.resolve()),
        "source_root": str(journal.relative_to(project_root.resolve()).as_posix()),
        "prefix_bytes": sum(member["prefix_bytes"] for member in members),
        "prefix_digest": prefix_digest,
        "members": members,
        "records": records,
        "limits": configured,
        "limit_sources": sources,
        "capture_read_bytes": total_read,
    }
    snapshot["id"] = _sha256(_json_bytes(_snapshot_core(snapshot)))
    return _retain_snapshot(snapshot)


def _validate_snapshot(snapshot: Mapping[str, Any]) -> tuple[Path, Path]:
    required = {
        "id",
        "project_root",
        "source_root",
        "prefix_bytes",
        "prefix_digest",
        "members",
        "records",
        "limits",
        "limit_sources",
        "capture_read_bytes",
    }
    if not isinstance(snapshot, Mapping) or set(snapshot) != required:
        raise JournalQueryError("invalid-snapshot")
    if snapshot["id"] != _sha256(_json_bytes(_snapshot_core(snapshot))):
        raise JournalQueryError("invalid-snapshot")
    root = Path(snapshot["project_root"])
    source_relative = Path(snapshot["source_root"])
    if root.is_symlink() or not root.is_dir() or source_relative.is_absolute() or ".." in source_relative.parts:
        raise JournalQueryError("invalid-snapshot")
    source = root / source_relative
    if source.is_symlink() or not source.is_dir():
        raise JournalQueryError("changed-source")
    control, _, _ = _control_and_settings(root)
    canonical_source = control / "_journal"
    if canonical_source.is_symlink() or canonical_source != source:
        raise JournalQueryError("changed-source")
    return root, source


def _revalidate_members(
    snapshot: Mapping[str, Any], root: Path, source: Path, *, limits: Mapping[str, int], deadline: float
) -> int:
    total = 0
    derived_records: list[dict[str, Any]] = []
    members = snapshot["members"]
    if not isinstance(members, list):
        raise JournalQueryError("invalid-snapshot")
    for member in members:
        if time.monotonic() > deadline:
            raise JournalQueryError("timeout-exceeded")
        if not isinstance(member, Mapping):
            raise JournalQueryError("invalid-snapshot")
        reference = member.get("ref")
        size = member.get("prefix_bytes")
        digest = member.get("prefix_digest")
        if not isinstance(reference, str) or type(size) is not int or size < 0 or not isinstance(digest, str):
            raise JournalQueryError("invalid-snapshot")
        relative = Path(reference)
        if relative.is_absolute() or ".." in relative.parts:
            raise JournalQueryError("invalid-snapshot")
        path = root / relative
        try:
            path.relative_to(source)
        except ValueError as error:
            raise JournalQueryError("invalid-retained-provenance") from error
        _safe_regular_file(path, "deleted-member")
        try:
            current_size = path.stat().st_size
        except OSError as error:
            raise JournalQueryError("unreadable-member") from error
        if current_size < size:
            raise JournalQueryError("truncated-member")
        if size > limits["max_file_bytes"]:
            raise JournalQueryError("file-limit-exceeded")
        if total + size > limits["max_total_read_bytes"]:
            raise JournalQueryError("total-read-limit-exceeded")
        try:
            with path.open("rb") as handle:
                prefix = handle.read(size)
        except OSError as error:
            raise JournalQueryError("unreadable-member") from error
        total += len(prefix)
        if len(prefix) != size:
            raise JournalQueryError("incomplete-read")
        if _sha256(prefix) != digest:
            raise JournalQueryError("changed-member")
        derived_records.extend(_member_events(reference, prefix))
    if time.monotonic() > deadline:
        raise JournalQueryError("timeout-exceeded")
    expected_records = snapshot.get("records")
    if not isinstance(expected_records, list):
        raise JournalQueryError("invalid-retained-provenance")
    derived_records.sort(key=lambda record: record["event_id"].encode("utf-8"))
    if _json_bytes(derived_records) != _json_bytes(expected_records):
        raise JournalQueryError("invalid-retained-provenance")
    return total


def _event_pointer(selector: str, *, mode: str) -> str:
    if not isinstance(selector, str) or not selector.startswith("event:/"):
        raise JournalQueryError("invalid-event-selector")
    pointer = "" if selector == "event:/" else selector[len("event:") :]
    if selector == "event:/" and mode != "full_events":
        raise JournalQueryError("invalid-event-selector")
    try:
        resolve_json_pointer({}, pointer)
    except QueryFilterError as error:
        raise JournalQueryError("invalid-event-selector") from error
    return pointer


def _sensitive_name(name: str) -> bool:
    normal = name.lower().replace("-", "_")
    return normal in _SENSITIVE_NAMES or any(token in normal for token in ("secret", "password", "credential"))


def _contains_sensitive(value: Any) -> bool:
    pending = [value]
    while pending:
        item = pending.pop()
        if isinstance(item, dict):
            for key, nested in item.items():
                if _sensitive_name(str(key)):
                    return True
                pending.append(nested)
        elif isinstance(item, list):
            pending.extend(item)
    return False


def _admit_selector(selector: str, *, mode: str, records: list[Mapping[str, Any]]) -> str:
    pointer = _event_pointer(selector, mode=mode)
    try:
        decoded = decode_json_pointer(pointer)
    except QueryFilterError as error:  # pragma: no cover - validation precedes this
        raise JournalQueryError("invalid-event-selector") from error
    if any("." in token or _sensitive_name(token) for token in decoded):
        raise JournalQueryError("protected-selector")
    for record in records:
        value = resolve_json_pointer(record["event"], pointer)
        if value is not MISSING and _contains_sensitive(value):
            raise JournalQueryError("protected-selector")
    return pointer


def _record_filter_statistics(
    evidence: dict[str, dict[str, Any]], statistics: Mapping[str, Any] | None
) -> None:
    """Record counters from the shared parser, never inferred AST/text guesses."""
    if not isinstance(statistics, Mapping):
        raise JournalQueryError("invalid-filter-statistics")
    bindings = {
        "max_grammar_depth": "grammar_depth",
        "max_filter_tokens": "tokens",
        "max_in_members": "in_members",
    }
    for limit_name, counter_name in bindings.items():
        consumed = statistics.get(counter_name)
        if type(consumed) is not int or consumed < 0:
            raise JournalQueryError("invalid-filter-statistics")
        evidence[limit_name]["consumed"] = consumed


def _limit_evidence(limits: Mapping[str, int], sources: Mapping[str, str]) -> dict[str, dict[str, Any]]:
    return {
        name: {"configured": value, "source": sources.get(name, "snapshot"), "consumed": 0, "exhausted": False}
        for name, value in limits.items()
    }


def _diagnostic_result(
    snapshot: Mapping[str, Any] | None,
    limits: Mapping[str, int],
    sources: Mapping[str, str],
    evidence: dict[str, dict[str, Any]],
    error: JournalQueryError,
) -> dict[str, Any]:
    exhausted = error.code.endswith("limit-exceeded") or error.code == "timeout-exceeded"
    if error.code in {"page-limit-exceeded", "selected-fields-limit-exceeded", "request-limit-exceeded"}:
        status = "invalid"
    elif error.code in {"changed-member", "deleted-member", "truncated-member", "unreadable-member", "changed-source", "incomplete-read"}:
        status = "blocked"
    elif exhausted:
        status = "incomplete"
    else:
        status = "invalid"
    exhausted_limits = {
        "request-limit-exceeded": "max_request_bytes",
        "grammar-depth-limit-exceeded": "max_grammar_depth",
        "filter-token-limit-exceeded": "max_filter_tokens",
        "in-members-limit-exceeded": "max_in_members",
        "selected-fields-limit-exceeded": "max_selected_fields",
        "page-limit-exceeded": "max_page_size",
        "snapshot-member-limit-exceeded": "max_snapshot_members",
        "file-limit-exceeded": "max_file_bytes",
        "total-read-limit-exceeded": "max_total_read_bytes",
        "timeout-exceeded": "timeout_seconds",
    }
    if limit_name := exhausted_limits.get(error.code):
        evidence[limit_name]["exhausted"] = True
    evidence["max_findings"]["consumed"] = 1
    return {
        "status": status,
        "snapshot": dict(snapshot) if snapshot is not None else None,
        "results": [],
        "next_cursor": None,
        "coverage": {"scanned": 0, "matched": 0, "returned": 0, "complete": False},
        "limits": evidence,
        "findings": [{"code": error.code}],
    }


def _encode_cursor(value: Mapping[str, Any]) -> str:
    return base64.urlsafe_b64encode(_json_bytes(value)).decode("ascii").rstrip("=")


def _decode_cursor(value: Any) -> Mapping[str, Any]:
    if not isinstance(value, str) or not value:
        raise JournalQueryError("invalid-cursor")
    try:
        raw = base64.urlsafe_b64decode(value + "=" * (-len(value) % 4))
        parsed = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError, json.JSONDecodeError) as error:
        raise JournalQueryError("invalid-cursor") from error
    if not isinstance(parsed, dict) or set(parsed) != {"snapshot_id", "context", "offset"}:
        raise JournalQueryError("invalid-cursor")
    if not isinstance(parsed["snapshot_id"], str) or not isinstance(parsed["context"], str) or type(parsed["offset"]) is not int:
        raise JournalQueryError("invalid-cursor")
    return parsed


def query(snapshot: Mapping[str, Any], request: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Query a pre-sealed frontier; never enumerate or write the Journal again."""
    request = {} if request is None else request
    fallback_limits: dict[str, int] = {}
    fallback_sources: dict[str, str] = {}
    evidence: dict[str, dict[str, Any]] | None = None
    public_snapshot: dict[str, Any] | None = None
    try:
        snapshot, public_snapshot = _resolve_retained_snapshot(snapshot)
        base_limits = snapshot.get("limits")
        base_sources = snapshot.get("limit_sources")
        if not isinstance(base_limits, Mapping) or not isinstance(base_sources, Mapping):
            raise JournalQueryError("invalid-snapshot")
        fallback_limits = {name: _positive_int(base_limits.get(name), name) for name in _LIMIT_NAMES}
        fallback_sources = {name: str(base_sources.get(name, "snapshot")) for name in _LIMIT_NAMES}
        if not isinstance(request, Mapping):
            raise JournalQueryError("invalid-request")
        if any(name not in _REQUEST_FIELDS for name in request):
            raise JournalQueryError("forbidden-request-field")
        query_overrides = request.get("limits")
        limits, _ = _resolve_limits({"query": fallback_limits}, {}, query_overrides)
        # Keep the Default/Instance provenance sealed at capture, while making
        # only this request's explicit overrides report as request-sourced.
        sources = dict(fallback_sources)
        if query_overrides is not None:
            sources.update({name: "request" for name in query_overrides})
        fallback_limits, fallback_sources = dict(limits), dict(sources)
        evidence = _limit_evidence(limits, sources)
        request_bytes = len(_json_bytes(request))
        evidence["max_request_bytes"]["consumed"] = request_bytes
        if request_bytes > limits["max_request_bytes"]:
            raise JournalQueryError("request-limit-exceeded")
        root, source = _validate_snapshot(snapshot)
        deadline = time.monotonic() + limits["timeout_seconds"]
        validated_bytes = _revalidate_members(snapshot, root, source, limits=limits, deadline=deadline)
        evidence["max_total_read_bytes"]["consumed"] = validated_bytes
        evidence["max_snapshot_members"]["consumed"] = len(snapshot["members"])
        if len(snapshot["members"]) > limits["max_snapshot_members"]:
            raise JournalQueryError("snapshot-member-limit-exceeded")
        evidence["max_file_bytes"]["consumed"] = max((item["prefix_bytes"] for item in snapshot["members"]), default=0)
        records = snapshot["records"]
        if not isinstance(records, list) or any(not isinstance(record, Mapping) for record in records):
            raise JournalQueryError("invalid-snapshot")
        mode = request.get("mode", "ids")
        if mode not in {"ids", "fields", "full_events"}:
            raise JournalQueryError("invalid-mode")
        select = request.get("select", [])
        if mode == "fields":
            if not isinstance(select, list) or not all(isinstance(value, str) for value in select):
                raise JournalQueryError("invalid-selection")
            evidence["max_selected_fields"]["consumed"] = len(select)
            if len(select) > limits["max_selected_fields"]:
                raise JournalQueryError("selected-fields-limit-exceeded")
            selected = [_admit_selector(value, mode=mode, records=records) for value in select]
        elif select not in ([], None) and "select" in request:
            raise JournalQueryError("invalid-selection")
        else:
            selected = []
        evidence["max_selected_fields"]["consumed"] = len(selected)
        if mode == "full_events" and any(_contains_sensitive(record["event"]) for record in records):
            raise JournalQueryError("protected-full-event")
        expression = request.get("filter")
        tree = None
        filter_selectors: dict[str, str] = {}
        if expression is not None:
            if not isinstance(expression, str):
                raise JournalQueryError("invalid-filter")
            filter_statistics: Mapping[str, Any] | None = None
            try:
                tree, filter_statistics = parse_filter_with_stats(
                    expression,
                    max_depth=limits["max_grammar_depth"],
                    max_tokens=limits["max_filter_tokens"],
                    max_in_members=limits["max_in_members"],
                )
                # Selector admission is local policy after a successful shared
                # parse.  Preserve that parser's actual consumption if this
                # tool subsequently rejects the selector.
                _record_filter_statistics(evidence, filter_statistics)
                filter_selectors = {
                    selector: _admit_selector(selector, mode=mode, records=records)
                    for selector in collect_selectors(tree)
                }
            except QueryFilterError as error:
                _record_filter_statistics(
                    evidence,
                    error.statistics if error.statistics is not None else filter_statistics,
                )
                message = str(error)
                if "grammar depth" in message or "literal depth" in message:
                    code = "grammar-depth-limit-exceeded"
                elif "token budget" in message:
                    code = "filter-token-limit-exceeded"
                elif "IN member budget" in message:
                    code = "in-members-limit-exceeded"
                else:
                    code = "invalid-filter"
                raise JournalQueryError(code) from error
        limit = request.get("limit", limits["max_page_size"])
        if type(limit) is not int or limit <= 0:
            raise JournalQueryError("invalid-page-limit")
        evidence["max_page_size"]["consumed"] = limit
        if limit > limits["max_page_size"]:
            raise JournalQueryError("page-limit-exceeded")
        context = _sha256(
            _json_bytes(
                {
                    "snapshot_id": snapshot["id"],
                    "filter": expression,
                    "mode": mode,
                    "select": request.get("select", []),
                    "limit": limit,
                    "limits": limits,
                }
            )
        )
        cursor = request.get("cursor")
        if cursor is None:
            offset = 0
        else:
            cursor_value = _decode_cursor(cursor)
            if cursor_value["snapshot_id"] != snapshot["id"] or cursor_value["context"] != context or cursor_value["offset"] < 0:
                raise JournalQueryError("cursor-context-mismatch")
            offset = cursor_value["offset"]
        matches: list[Mapping[str, Any]] = []
        for record in records:
            if time.monotonic() > deadline:
                raise JournalQueryError("timeout-exceeded")
            if tree is None or evaluate_filter(tree, lambda selector, event=record["event"]: resolve_json_pointer(event, filter_selectors[selector])):
                matches.append(record)
        if offset > len(matches):
            raise JournalQueryError("invalid-cursor")
        page = matches[offset : offset + limit]
        if mode == "ids":
            results: list[Any] = [record["event_id"] for record in page]
        elif mode == "fields":
            results = []
            for record in page:
                result: dict[str, Any] = {"event_id": record["event_id"]}
                for selector, pointer in zip(request["select"], selected):
                    value = resolve_json_pointer(record["event"], pointer)
                    result[selector] = {"state": "missing"} if value is MISSING else value
                results.append(result)
        else:
            results = [{"event_id": record["event_id"], "event": record["event"]} for record in page]
        next_offset = offset + len(page)
        has_more = next_offset < len(matches)
        next_cursor = _encode_cursor({"snapshot_id": snapshot["id"], "context": context, "offset": next_offset}) if has_more else None
        return {
            "status": "incomplete" if has_more else "complete",
            "snapshot": public_snapshot,
            "results": results,
            "next_cursor": next_cursor,
            "coverage": {"scanned": len(records), "matched": len(matches), "returned": len(results), "complete": not has_more},
            "limits": evidence,
            "findings": [],
        }
    except JournalQueryError as error:
        limits = fallback_limits or {name: 0 for name in _LIMIT_NAMES}
        sources = fallback_sources or {name: "unavailable" for name in _LIMIT_NAMES}
        result_evidence = evidence or _limit_evidence(limits, sources)
        return _diagnostic_result(public_snapshot, limits, sources, result_evidence, error)


__all__ = ["JournalQueryError", "capture_snapshot", "query"]
