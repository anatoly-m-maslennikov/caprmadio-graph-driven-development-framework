#!/usr/bin/env python3
"""Append sealed file-change Journal records through the common Tool CLI.

Usage:
    append_change_records.py describe
    append_change_records.py run --input CONTEXT.json [--apply]

``run`` is mutation-free unless ``--apply`` is present.  Its input is the
schema-v2 ``COMMIT_CONTEXT`` envelope.  In particular,
``predictions.journal_records`` is already sealed by COMMIT_CONTEXT and is
never regenerated, re-timestamped, or assigned another LLM session here.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import time
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping


SCRIPT_PATH = Path(__file__).resolve()
TOOLS_ROOT = SCRIPT_PATH.parents[1]
CONTEXT_ROOT = TOOLS_ROOT / "COMMIT_CONTEXT"
for _parent in SCRIPT_PATH.parents:
    if _parent.name == ".caprmedio_runtime":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
    if _parent.name == ".caprmedio_install":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
    if _parent.name == ".caprmedio":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
for _path in (TOOLS_ROOT, CONTEXT_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from commit_context_logic import project_paths_eligible, repository_root  # noqa: E402
from project_runtime import atomic_tempfile  # noqa: E402
from work_journal import (  # noqa: E402
    WorkJournalError,
    canonical_json_bytes,
    canonical_json_digest,
    configured_runtime_root,
    predict_sealed_event_receipts,
    validate_partition,
    validate_sealed_event,
    append_sealed_events,
)


TOOL_ID = "APPEND_CHANGE_RECORDS"
TOOL_KIND = "doer"
TOOL_SCHEMA_VERSION = 1
ACTIONS = {"ADD", "MOVE", "UPDATE", "MOVE+UPDATE", "REMOVE"}
HEX40_RE = __import__("re").compile(r"^[0-9a-f]{40}$")
HEX64_RE = __import__("re").compile(r"^[0-9a-f]{64}$")
SAFE_ID_RE = __import__("re").compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")


class ToolError(RuntimeError):
    """Stable diagnostic emitted by this Tool."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


def _json_result(*, ok: bool, mode: str, **values: Any) -> dict[str, Any]:
    return {
        "schema_version": TOOL_SCHEMA_VERSION,
        "tool": {"capability_id": TOOL_ID, "kind": TOOL_KIND},
        "ok": ok,
        "mode": mode,
        **values,
    }


def _emit(payload: Mapping[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))


def _require_mapping(value: object, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ToolError("invalid-context", f"{field} must be an object")
    return dict(value)


def _require_string(value: Mapping[str, Any], field: str) -> str:
    item = value.get(field)
    if not isinstance(item, str) or not item:
        raise ToolError("invalid-context", f"{field} must be a non-empty string")
    return item


def _require_sha256(value: object, field: str) -> str:
    if not isinstance(value, str) or not HEX64_RE.fullmatch(value):
        raise ToolError("invalid-context", f"{field} must be a lowercase SHA-256 digest")
    return value


def _safe_action_id(value: str, field: str) -> str:
    if not SAFE_ID_RE.fullmatch(value):
        raise ToolError("invalid-context", f"{field} contains unsupported characters")
    return value


def _load_json(source: str) -> dict[str, Any]:
    try:
        text = sys.stdin.read() if source == "-" else Path(source).read_text(encoding="utf-8")
    except OSError as error:
        raise ToolError("input-unreadable", f"cannot read input: {source}") from error
    try:
        value = json.loads(text)
    except json.JSONDecodeError as error:
        raise ToolError("invalid-json", "input must be one JSON object") from error
    return _require_mapping(value, "input")


def _parse_datetime(value: str) -> None:
    try:
        parsed = dt.datetime.fromisoformat(value)
    except ValueError as error:
        raise ToolError("invalid-context", "occurred_at must be ISO-8601") from error
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ToolError("invalid-context", "occurred_at must be timezone-qualified")


def _canonical_source_projection(sources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "relation_type": source["relation_type"],
            "filename": source["filename"],
            "version": source["version"],
        }
        for source in sources
    ]


def _frontier_source_projection(context: Mapping[str, Any]) -> dict[str, Any]:
    """Return the sealed selected-carrier frontier without reading new state."""
    subject = _require_mapping(context["subject"], "subject")
    result = _require_mapping(context["result"], "result")
    projection: dict[str, Any] = {
        "identity": subject["identity"],
        "kind": subject["kind"],
        "state": "removed" if result["state"] == "removed" else "present",
        "filename": result["filename"],
        "version": result["version"],
    }
    if result["state"] == "present":
        projection["path"] = result["path"]
        projection["sha256"] = result["sha256"]
        return projection
    committed = _require_mapping(_require_mapping(context["snapshots"], "snapshots").get("committed"), "snapshots.committed")
    projection["path"] = committed.get("path")
    projection["sha256"] = committed.get("sha256")
    _relative_path(root=Path("."), raw=projection["path"], field="snapshots.committed.path")
    _require_sha256(projection["sha256"], "snapshots.committed.sha256")
    return projection


def _normalise_context(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Accept the common envelope but keep exactly its sealed context object."""
    if "context" in payload:
        context = _require_mapping(payload["context"], "context")
    elif isinstance(payload.get("result"), dict) and "context" in payload["result"]:
        context = _require_mapping(payload["result"]["context"], "result.context")
    else:
        context = dict(payload)
    if context.get("schema_version") != 3:
        raise ToolError("invalid-context", "context.schema_version must be 3")
    return context


def _detailed_relation_projection(relations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "relation_type": relation["relation_type"],
            "filename": relation["filename"],
            "version": relation["version"],
            "path": relation["path"],
            "sha256": relation["sha256"],
            "registry": relation["registry"],
        }
        for relation in relations
    ]


def _validate_prediction_partitions(context: Mapping[str, Any], author: str, local_date: str) -> None:
    predictions = _require_mapping(context.get("predictions"), "predictions")
    partitions = predictions.get("journal_partitions")
    if not isinstance(partitions, list) or not partitions:
        raise ToolError("invalid-context", "predictions.journal_partitions must be a non-empty array")
    expected_prefix = f"{author}-{local_date}-part-"
    matched = False
    for partition in partitions:
        if isinstance(partition, str):
            matched = matched or Path(partition).name.startswith(expected_prefix)
            continue
        if isinstance(partition, dict):
            name = partition.get("carrier") or partition.get("path")
            if isinstance(name, str) and Path(name).name.startswith(expected_prefix):
                matched = True
                continue
            if partition.get("author") == author and partition.get("local_date") == local_date:
                matched = True
                continue
        raise ToolError("invalid-context", "journal partition prediction has an unsupported shape")
    if not matched:
        raise ToolError("invalid-context", "journal partition prediction does not match sealed author and local_date")


def _validate_recovery(context: Mapping[str, Any], events: list[dict[str, Any]]) -> None:
    recovered = [event for event in events if event.get("event") == "recovered"]
    recovery = context.get("recovery")
    if not recovered and recovery is None:
        return
    if len(recovered) != 1 or not isinstance(recovery, dict):
        raise ToolError("invalid-recovery", "a recovered event requires one sealed recovery object")
    required = {"event_id", "result", "evidence", "evidence_digest", "contradictions"}
    if set(recovery) != required:
        raise ToolError("invalid-recovery", "recovery must contain exactly event_id, result, evidence, evidence_digest, contradictions")
    if recovery["event_id"] != recovered[0].get("event_id"):
        raise ToolError("invalid-recovery", "recovery.event_id must identify the recovered Journal event")
    if recovery["result"] != recovered[0].get("result"):
        raise ToolError("invalid-recovery", "recovery.result must equal the recovered Journal result")
    evidence = recovery["evidence"]
    if not isinstance(evidence, dict) or set(evidence) != {"git", "carrier"}:
        raise ToolError("invalid-recovery", "recovery.evidence must contain git and carrier evidence")
    if not isinstance(evidence["git"], dict) or not evidence["git"]:
        raise ToolError("invalid-recovery", "recovery.evidence.git must be a non-empty object")
    if not isinstance(evidence["carrier"], dict) or not evidence["carrier"]:
        raise ToolError("invalid-recovery", "recovery.evidence.carrier must be a non-empty object")
    _require_sha256(recovery["evidence_digest"], "recovery.evidence_digest")
    if recovery["evidence_digest"] != canonical_json_digest(evidence):
        raise ToolError("recovery-evidence-mismatch", "recovery evidence digest does not match sealed evidence")
    if not isinstance(recovery["contradictions"], list) or recovery["contradictions"]:
        raise ToolError("unsupported-recovery", "recovery must have an empty contradictions list")


def _expected_context_id(context: Mapping[str, Any]) -> str:
    fields = (
        "schema_version",
        "action_id",
        "trigger",
        "subject",
        "structural_scope",
        "action_type",
        "sources",
        "result",
        "llm_session",
        "author",
        "occurred_at",
        "timezone",
        "local_date",
        "git_base",
        "frontier",
    )
    core = {field: context[field] for field in fields}
    if "previous_result_event" in context:
        core["previous_result_event"] = context["previous_result_event"]
    return canonical_json_digest(core)


def _expected_event_id(event: Mapping[str, Any]) -> str:
    if event["event"] == "recovered":
        evidence = _require_mapping(event.get("recovery_evidence"), "recovery_evidence")
        return canonical_json_digest(
            {
                "schema_version": event["schema_version"],
                "action_id": event["action_id"],
                "event": "recovered",
                "kind": event["kind"],
                "subject_kind": event["subject_kind"],
                "result": event["result"],
                "evidence_digest": canonical_json_digest(evidence),
            }
        )
    fields = (
        "schema_version",
        "action_id",
        "event",
        "kind",
        "subject_kind",
        "author",
        "occurred_at",
        "llm_session",
        "structural_scope",
        "action_type",
        "sources",
        "result",
    )
    core = {field: event[field] for field in fields}
    if "previous_result_event" in event:
        core["previous_result_event"] = event["previous_result_event"]
    return canonical_json_digest(core)


def validate_context(context: Mapping[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Validate the sealed COMMIT_CONTEXT without discovering replacement data."""
    value = dict(context)
    context_id = _safe_action_id(_require_string(value, "context_id"), "context_id")
    action_id = _safe_action_id(_require_string(value, "action_id"), "action_id")
    trigger = _require_mapping(value.get("trigger"), "trigger")
    repository = _require_mapping(trigger.get("repository"), "trigger.repository")
    _require_string(repository, "identity")
    _require_string(repository, "root")
    subject = _require_mapping(value.get("subject"), "subject")
    _require_string(subject, "identity")
    _require_string(subject, "selected_state")
    if subject.get("kind") not in {"file", "folder"}:
        raise ToolError("invalid-context", "subject.kind must be file or folder")
    action_type = value.get("action_type")
    if action_type not in ACTIONS:
        raise ToolError("invalid-context", "action_type is invalid")
    author = _require_string(value, "author")
    occurred_at = _require_string(value, "occurred_at")
    _parse_datetime(occurred_at)
    local_date = _require_string(value, "local_date")
    timezone = _require_string(value, "timezone")
    validate_partition(author, local_date, timezone)
    session = _require_mapping(value.get("llm_session"), "llm_session")
    if set(session) != {"app", "uuid"}:
        raise ToolError("invalid-context", "llm_session must contain only app and uuid")
    _require_string(session, "app")
    _require_string(session, "uuid")
    _require_string(value, "structural_scope")
    sources_value = value.get("sources")
    if not isinstance(sources_value, list):
        raise ToolError("invalid-context", "sources must be an array")
    sources = [_require_mapping(source, "sources item") for source in sources_value]
    for source in sources:
        relation_type = source.get("relation_type")
        filename = source.get("filename")
        version = source.get("version")
        if not isinstance(relation_type, str) or not relation_type:
            raise ToolError("invalid-context", "sources.relation_type must be a non-empty string")
        if not isinstance(filename, str) or not filename.endswith(".md"):
            raise ToolError("invalid-context", "sources.filename must be a Markdown filename")
        if not isinstance(version, int) or version < 1:
            raise ToolError("invalid-context", "sources.version must be a positive integer")
    relations_value = value.get("relations")
    if not isinstance(relations_value, list):
        raise ToolError("invalid-context", "relations must be an ordered array")
    relations = [_require_mapping(relation, "relations item") for relation in relations_value]
    prior_relation: tuple[str, str, int] | None = None
    for relation in relations:
        relation_type = relation.get("relation_type")
        filename = relation.get("filename")
        version = relation.get("version")
        if not isinstance(relation_type, str) or not relation_type:
            raise ToolError("invalid-context", "relations.relation_type must be a non-empty string")
        if not isinstance(filename, str) or not filename.endswith(".md"):
            raise ToolError("invalid-context", "relations.filename must be a Markdown filename")
        if not isinstance(version, int) or version < 1:
            raise ToolError("invalid-context", "relations.version must be a positive integer")
        _relative_path(root=Path("."), raw=relation.get("path"), field="relations.path")
        _require_sha256(relation.get("sha256"), "relations.sha256")
        relation_key = (relation_type, filename, version)
        if prior_relation is not None and relation_key <= prior_relation:
            raise ToolError("invalid-context", "relations must be uniquely sorted in canonical order")
        prior_relation = relation_key
    if _canonical_source_projection(relations) != sources:
        raise ToolError("invalid-context", "sources must be the compact projection of detailed relations")
    result = _require_mapping(value.get("result"), "result")
    git_base = _require_mapping(value.get("git_base"), "git_base")
    commit = _require_string(git_base, "commit")
    tree = _require_string(git_base, "tree")
    if not HEX40_RE.fullmatch(commit) or not HEX40_RE.fullmatch(tree):
        raise ToolError("invalid-context", "git_base.commit and git_base.tree must be Git object ids")
    frontier = _require_mapping(value.get("frontier"), "frontier")
    _require_sha256(frontier.get("source_sha256"), "frontier.source_sha256")
    _require_sha256(frontier.get("relations_sha256"), "frontier.relations_sha256")
    snapshots = _require_mapping(value.get("snapshots"), "snapshots")
    validation = _require_mapping(value.get("validation"), "validation")
    if not validation:
        raise ToolError("invalid-context", "validation must not be empty")
    if not snapshots:
        raise ToolError("invalid-context", "snapshots must not be empty")
    expected_source_digest = canonical_json_digest(_frontier_source_projection(value))
    expected_relations_digest = canonical_json_digest(_detailed_relation_projection(relations))
    if frontier["source_sha256"] != expected_source_digest or frontier["relations_sha256"] != expected_relations_digest:
        raise ToolError("stale-context", "sealed frontier digest does not match its sealed source frontier")
    predictions = _require_mapping(value.get("predictions"), "predictions")
    event_values = predictions.get("journal_records")
    if not isinstance(event_values, list) or not event_values:
        raise ToolError("invalid-context", "predictions.journal_records must be a non-empty array")
    events = [validate_sealed_event(_require_mapping(event, "journal record")) for event in event_values]
    if any(event["action_id"] != action_id for event in events):
        raise ToolError("invalid-context", "every Journal event must use context.action_id")
    if any(event["author"] != author for event in events):
        raise ToolError("invalid-context", "every Journal event must use context.author")
    if any(event["occurred_at"] != occurred_at for event in events):
        raise ToolError("invalid-context", "every Journal event must use sealed occurred_at")
    if any(event["llm_session"] != session for event in events):
        raise ToolError("invalid-context", "every Journal event must use sealed llm_session")
    completed = [event for event in events if event["event"] == "completed"]
    if len(completed) != 1:
        raise ToolError("invalid-context", "event set must contain exactly one completed governed_project_change")
    change = completed[0]
    if change.get("subject_kind") != subject["kind"] or change["action_type"] != action_type or change["sources"] != _canonical_source_projection(sources) or change["result"] != result:
        raise ToolError("invalid-context", "completed Journal event must be the exact context projection")
    if value.get("previous_result_event") != change.get("previous_result_event"):
        raise ToolError("invalid-context", "previous_result_event differs between context and Journal event")
    _validate_recovery(value, events)
    _validate_prediction_partitions(value, author, local_date)
    if context_id != _expected_context_id(value):
        raise ToolError("context-identity-mismatch", "context_id does not match the exact sealed context core")
    for event in events:
        if event["event_id"] != _expected_event_id(event):
            raise ToolError("event-identity-mismatch", "event_id does not match the exact sealed event core")
        if event["structural_scope"] != value["structural_scope"]:
            raise ToolError("invalid-context", "every Journal event must use context.structural_scope")
    # Retain named values to prevent callers from treating a partial mapping as validated.
    if not context_id or not action_id:
        raise AssertionError("unreachable")
    return value, events


def _git(root: Path, *arguments: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(root), *arguments],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip() or "Git command failed"
        raise ToolError("git-preflight-failed", detail)
    return completed.stdout


def _git_bytes(root: Path, *arguments: str, allow_failure: bool = False) -> bytes | None:
    completed = subprocess.run(
        ["git", "-C", str(root), *arguments],
        check=False,
        capture_output=True,
    )
    if completed.returncode == 0:
        return completed.stdout
    if allow_failure:
        return None
    detail = completed.stderr.decode("utf-8", errors="replace").strip() or "Git command failed"
    raise ToolError("git-preflight-failed", detail)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _working_bytes(path: Path) -> bytes:
    if path.is_symlink():
        return os.readlink(path).encode("utf-8")
    return path.read_bytes()


def _folder_entries(root: Path, folder: str) -> list[dict[str, str]]:
    paths = [
        value
        for value in _git(root, "ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", folder).split("\0")
        if value
    ]
    prefix = folder.rstrip("/") + "/"
    eligible = project_paths_eligible(root, [relative for relative in paths if relative.startswith(prefix)])
    entries: list[dict[str, str]] = []
    for relative in sorted(paths):
        if relative not in eligible:
            continue
        path = root / relative
        if path.is_file() or path.is_symlink():
            entries.append({"path": relative, "sha256": hashlib.sha256(_working_bytes(path)).hexdigest()})
    return entries


def _folder_digest(folder: str, entries: list[dict[str, str]]) -> str:
    return canonical_json_digest(
        [
            {"path": Path(entry["path"]).relative_to(folder).as_posix(), "sha256": entry["sha256"]}
            for entry in entries
        ]
    )


def _atomic_json(path: Path, value: Mapping[str, Any]) -> None:
    """Persist non-authoritative runtime state durably and replace atomically."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(path, "append_change_records")
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


def _append_ndjson(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = canonical_json_bytes(value) + b"\n"
    descriptor = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o600)
    try:
        offset = 0
        while offset < len(payload):
            written = os.write(descriptor, payload[offset:])
            if written <= 0:
                raise OSError("could not append pipeline correlation")
            offset += written
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _relative_path(root: Path, raw: object, field: str) -> Path:
    if not isinstance(raw, str) or not raw:
        raise ToolError("invalid-context", f"{field} must be a non-empty repository-relative path")
    value = Path(raw)
    if value.is_absolute() or ".." in value.parts:
        raise ToolError("invalid-context", f"{field} must be a safe repository-relative path")
    return root / value


def validate_live_preflight(root: Path, context: Mapping[str, Any]) -> None:
    """Repeat deterministic mutable-boundary checks without refreshing context."""
    trigger = _require_mapping(context["trigger"], "trigger")
    repository = _require_mapping(trigger.get("repository"), "trigger.repository")
    reported_root = _require_string(repository, "root")
    if Path(reported_root).expanduser().resolve() != root.resolve():
        raise ToolError("repository-mismatch", "trigger repository.root does not match selected repository")
    git_directory = Path(_git(root, "rev-parse", "--git-dir").strip())
    if not git_directory.is_absolute():
        git_directory = root / git_directory
    expected_identity = canonical_json_digest(
        {"repository_root": root.resolve().as_posix(), "git_directory": git_directory.resolve().as_posix()}
    )
    if repository.get("identity") != expected_identity:
        raise ToolError("repository-identity-mismatch", "trigger repository.identity does not match selected repository")
    git_base = _require_mapping(context["git_base"], "git_base")
    if _git(root, "rev-parse", "HEAD").strip() != git_base["commit"]:
        raise ToolError("stale-context", "Git base commit no longer matches sealed context")
    if _git(root, "rev-parse", "HEAD^{tree}").strip() != git_base["tree"]:
        raise ToolError("stale-context", "Git base tree no longer matches sealed context")
    result = _require_mapping(context["result"], "result")
    subject = _require_mapping(context["subject"], "subject")
    committed_snapshot = _require_mapping(context["snapshots"], "snapshots").get("committed")
    if subject.get("kind") == "folder":
        current_entries = result.get("entries") if result.get("state") == "present" else []
        previous_entries = committed_snapshot.get("entries", []) if isinstance(committed_snapshot, Mapping) else []
        subject_paths = {
            entry["path"]
            for entry in [*previous_entries, *current_entries]
            if isinstance(entry, Mapping) and isinstance(entry.get("path"), str)
        }
    else:
        subject_paths = {
            value
            for value in (trigger.get("before_path"), trigger.get("after_path"), result.get("path"))
            if isinstance(value, str) and value
        }
    staged = [item for item in _git(root, "diff", "--cached", "--name-only", "--no-renames", "-z").split("\0") if item]
    if any(path not in subject_paths for path in staged):
        raise ToolError("unrelated-staged-change", "repository index contains a change outside the resolved subject identity")
    if result["state"] == "present" and subject.get("kind") == "folder":
        folder = str(result.get("path"))
        current_entries = _folder_entries(root, folder)
        if current_entries != result.get("entries") or _folder_digest(folder, current_entries) != result.get("sha256"):
            raise ToolError("stale-context", "folder entry frontier no longer matches sealed result")
        if Path(folder).name != result.get("filename"):
            raise ToolError("stale-context", "folder result name and path disagree")
    elif result["state"] == "present":
        result_path = _relative_path(root, result["path"], "result.path")
        if (not result_path.is_file() and not result_path.is_symlink()) or hashlib.sha256(_working_bytes(result_path)).hexdigest() != result["sha256"]:
            raise ToolError("stale-context", "result carrier no longer matches sealed digest")
        if result_path.name != result["filename"]:
            raise ToolError("stale-context", "result carrier name no longer matches sealed filename")
        if result["path"] in staged:
            staged_bytes = _git_bytes(root, "show", f":{result['path']}")
            if staged_bytes is None or hashlib.sha256(staged_bytes).hexdigest() != result["sha256"]:
                raise ToolError("stale-context", "staged subject carrier no longer matches sealed digest")
    elif result["state"] == "removed":
        committed = _require_mapping(committed_snapshot, "snapshots.committed")
        if subject.get("kind") == "folder":
            entries = committed.get("entries")
            if not isinstance(entries, list) or _folder_digest(str(committed.get("path")), entries) != committed.get("sha256"):
                raise ToolError("stale-context", "removed folder predecessor digest is invalid")
            for entry in entries:
                if _git_bytes(root, "show", f"HEAD:{entry['path']}", allow_failure=True) is None:
                    raise ToolError("stale-context", "removed folder predecessor entry is unavailable")
                candidate = root / str(entry["path"])
                if candidate.exists() or candidate.is_symlink():
                    raise ToolError("stale-context", "removed folder entry has reappeared")
            return
        committed_path = _relative_path(root, committed.get("path"), "snapshots.committed.path")
        committed_digest = _require_sha256(committed.get("sha256"), "snapshots.committed.sha256")
        payload = _git_bytes(root, "show", f"HEAD:{committed_path.relative_to(root).as_posix()}")
        assert payload is not None
        if hashlib.sha256(payload).hexdigest() != committed_digest:
            raise ToolError("stale-context", "removed predecessor no longer matches sealed digest")
        if committed_path.relative_to(root).as_posix() in staged and _git_bytes(root, "show", f":{committed_path.relative_to(root).as_posix()}", allow_failure=True) is not None:
            raise ToolError("stale-context", "removed subject remains present in the staged index")
    else:
        raise ToolError("invalid-context", "result.state is invalid")
    for source in context["relations"]:
        source_path = _relative_path(root, source.get("path"), "relations.path")
        source_digest = _require_sha256(source.get("sha256"), "relations.sha256")
        if not source_path.is_file() or _sha256_file(source_path) != source_digest:
            raise ToolError("stale-context", "relation frontier no longer matches sealed digest")


def _runtime_dir(root: Path) -> Path:
    return root / configured_runtime_root(root) / "state" / "append_change_records"


def _correlation_path(root: Path) -> Path:
    return root / configured_runtime_root(root) / "state" / "commit_trigger" / "pipeline_correlations.ndjson"


def _correlation_id(action_id: str, receipt: Mapping[str, Any]) -> str:
    transition = {
        key: receipt[key]
        for key in (
            "event_id",
            "event_digest",
            "carrier",
            "line",
            "previous_carrier_digest",
            "appended_carrier_digest",
        )
    }
    return canonical_json_digest({"action_id": action_id, "transition": transition})


def _correlation_states(root: Path) -> dict[str, str]:
    path = _correlation_path(root)
    if not path.exists():
        return {}
    states: dict[str, str] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line:
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ToolError("invalid-runtime-state", f"pipeline correlation JSON is invalid at line {line_number}") from error
        if not isinstance(value, dict) or not isinstance(value.get("correlation_id"), str):
            raise ToolError("invalid-runtime-state", f"pipeline correlation is invalid at line {line_number}")
        event = value.get("event")
        if event == "registered":
            states[value["correlation_id"]] = "active"
        elif event == "retired":
            states[value["correlation_id"]] = "retired"
        else:
            raise ToolError("invalid-runtime-state", f"pipeline correlation event is invalid at line {line_number}")
    return states


def register_pipeline_correlations(root: Path, action_id: str, receipts: list[Mapping[str, Any]]) -> list[str]:
    """Register exact pipeline-owned Journal transitions before appending them."""
    correlation_ids: list[str] = []
    with _lease_guard(root, create=True):
        states = _correlation_states(root)
        for receipt in receipts:
            if receipt.get("disposition") == "reused":
                continue
            correlation_id = _correlation_id(action_id, receipt)
            correlation_ids.append(correlation_id)
            if states.get(correlation_id) == "active":
                continue
            transition = {
                key: receipt[key]
                for key in (
                    "event_id",
                    "event_digest",
                    "carrier",
                    "line",
                    "previous_carrier_digest",
                    "appended_carrier_digest",
                )
            }
            _append_ndjson(
                _correlation_path(root),
                {
                    "schema_version": 1,
                    "event": "registered",
                    "correlation_id": correlation_id,
                    "action_id": action_id,
                    "transition": transition,
                },
            )
    return correlation_ids


def retire_pipeline_correlations(root: Path, action_id: str) -> list[str]:
    """Retire this action's active correlations after commit verification."""
    retired: list[str] = []
    path = _correlation_path(root)
    with _lease_guard(root, create=True):
        if not path.exists():
            return retired
        states = _correlation_states(root)
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line:
                continue
            value = json.loads(line)
            if value.get("event") != "registered" or value.get("action_id") != action_id:
                continue
            correlation_id = value["correlation_id"]
            if states.get(correlation_id) != "active" or correlation_id in retired:
                continue
            _append_ndjson(
                path,
                {
                    "schema_version": 1,
                    "event": "retired",
                    "correlation_id": correlation_id,
                    "action_id": action_id,
                },
            )
            retired.append(correlation_id)
    return retired


def _lease_path(root: Path) -> Path:
    """The end-to-end flow owns one shared repository apply lease carrier."""
    return root / configured_runtime_root(root) / "state" / "commit_change_set" / "lease.json"


@contextmanager
def _lease_guard(root: Path, *, create: bool) -> Iterator[None]:
    runtime = _runtime_dir(root)
    guard = runtime / "lease.lock"
    if create:
        runtime.mkdir(parents=True, exist_ok=True)
    if not guard.exists() and not create:
        yield
        return
    token = str(uuid.uuid4())
    descriptor: int | None = None
    deadline = time.monotonic() + 30.0
    while descriptor is None:
        try:
            descriptor = os.open(guard, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise ToolError("lease-guard-unavailable", "repository lease guard remains held")
            time.sleep(0.05)
    try:
        try:
            os.write(descriptor, canonical_json_bytes({"token": token, "pid": os.getpid()}) + b"\n")
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    except BaseException:
        guard.unlink(missing_ok=True)
        raise
    try:
        yield
    finally:
        try:
            active = json.loads(guard.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            active = {}
        if active.get("token") == token:
            guard.unlink(missing_ok=True)


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ToolError("invalid-runtime-state", f"cannot read runtime state: {path}") from error
    return _require_mapping(value, "runtime state")


def _lease_observation(root: Path) -> dict[str, Any]:
    path = _lease_path(root)
    if not path.exists():
        return {"status": "available"}
    lease = _read_json(path)
    return {
        "status": lease.get("status", "active"),
        "action_id": lease.get("action_id"),
        "lease_token": lease.get("lease_token"),
    }


def acquire_lease(root: Path, context: Mapping[str, Any], *, wait_seconds: float) -> tuple[dict[str, Any], bool]:
    """Acquire/reuse the repository lease without persisting provenance copies."""
    action_id = str(context["action_id"])
    context_id = str(context["context_id"])
    event_ids = [str(event["event_id"]) for event in context["predictions"]["journal_records"]]
    context_digest = canonical_json_digest(context)
    deadline = time.monotonic() + wait_seconds
    while True:
        with _lease_guard(root, create=True):
            path = _lease_path(root)
            if not path.exists():
                lease = {
                    "schema_version": 1,
                    "status": "active",
                    "action_id": action_id,
                    "context_id": context_id,
                    "context_digest": context_digest,
                    "event_ids": event_ids,
                    "lease_token": str(uuid.uuid4()),
                }
                _atomic_json(path, lease)
                return lease, True
            lease = _read_json(path)
            if lease.get("action_id") == action_id:
                if lease.get("context_digest") != context_digest:
                    raise ToolError("action-context-collision", "action_id is already leased for different sealed context")
                return lease, False
        if time.monotonic() >= deadline:
            raise ToolError("lease-unavailable", "another action retains the repository lease")
        time.sleep(min(0.1, max(0.0, deadline - time.monotonic())))


def release_unconsumed_lease(root: Path, lease: Mapping[str, Any], *, acquired: bool) -> None:
    if not acquired:
        return
    with _lease_guard(root, create=True):
        path = _lease_path(root)
        if path.exists() and _read_json(path).get("lease_token") == lease.get("lease_token"):
            path.unlink()


def release_verified_lease(
    root: Path,
    lease: Mapping[str, Any],
    *,
    expected_live_lease: Mapping[str, Any] | None = None,
    verify_recovery: Callable[[], None] | None = None,
) -> None:
    """Release the shared lease only after COMMIT_CHANGE_SET has verified it.

    This intentionally compares the active carrier's status, action, and token
    inside the Appender's serialization guard, so a stale receipt can never
    release another action's lease.
    """
    expected_action = lease.get("action_id")
    expected_token = lease.get("lease_token")
    if not isinstance(expected_action, str) or not isinstance(expected_token, str):
        raise ToolError("invalid-lease", "lease must contain action_id and lease_token")
    expected_fingerprint = dict(expected_live_lease) if expected_live_lease is not None else None
    with _lease_guard(root, create=True):
        path = _lease_path(root)
        if not path.exists():
            raise ToolError("lease-not-live", "repository lease is no longer present")
        active = _read_json(path)
        if (
            active.get("status") != "active"
            or active.get("action_id") != expected_action
            or active.get("lease_token") != expected_token
        ):
            raise ToolError("lease-not-live", "repository lease does not match verified action and token")
        if expected_fingerprint is not None and active != expected_fingerprint:
            raise ToolError("lease-not-live", "repository lease differs from the verified recovery fingerprint")
        if verify_recovery is not None:
            verify_recovery()
    # The caller reaches this function only after complete commit verification.
    # Retire before freeing the action slot so a restarted Trigger never treats a
    # later operator Journal write as part of the completed pipeline transition.
    retire_pipeline_correlations(root, expected_action)
    with _lease_guard(root, create=True):
        path = _lease_path(root)
        if not path.exists():
            raise ToolError("lease-not-live", "repository lease is no longer present")
        active = _read_json(path)
        if (
            active.get("status") != "active"
            or active.get("action_id") != expected_action
            or active.get("lease_token") != expected_token
        ):
            raise ToolError("lease-not-live", "repository lease changed before verified release")
        if expected_fingerprint is not None and active != expected_fingerprint:
            raise ToolError("lease-not-live", "repository lease changed before verified recovery release")
        if verify_recovery is not None:
            verify_recovery()
        path.unlink()


def _committed_recovery_path(root: Path, action_id: str) -> Path:
    _require_sha256(action_id, "recovery.action_id")
    return _runtime_dir(root) / "committed_recoveries" / f"{action_id}.json"


def _validated_committed_recovery(raw: object) -> dict[str, Any]:
    recovery = _require_mapping(raw, "committed recovery")
    if set(recovery) != {"schema_version", "recovery_id", "proof"}:
        raise ToolError("invalid-recovery", "committed recovery must contain exactly schema_version, recovery_id, and proof")
    if recovery["schema_version"] != 1:
        raise ToolError("invalid-recovery", "committed recovery schema_version must be 1")
    _require_sha256(recovery["recovery_id"], "recovery.recovery_id")
    proof = _require_mapping(recovery["proof"], "recovery.proof")
    required = {
        "schema_version",
        "kind",
        "action_id",
        "operator_approval",
        "committed_revision",
        "lease",
        "event_ids",
        "events",
    }
    if set(proof) != required:
        raise ToolError("invalid-recovery", "committed recovery proof has an unexpected schema")
    if proof["schema_version"] != 1 or proof["kind"] != "committed-lease-recovery":
        raise ToolError("invalid-recovery", "committed recovery proof kind is invalid")
    action_id = _require_sha256(proof["action_id"], "recovery.proof.action_id")
    approval = proof["operator_approval"]
    if not isinstance(approval, str) or not approval.strip():
        raise ToolError("operator-approval-missing", "committed recovery requires explicit operator approval")
    revision = proof["committed_revision"]
    if not isinstance(revision, str) or not __import__("re").fullmatch(r"[0-9a-f]{40}", revision):
        raise ToolError("invalid-recovery", "committed recovery revision must be a full Git SHA")
    lease = _require_mapping(proof["lease"], "recovery.proof.lease")
    required_lease = {"schema_version", "status", "action_id", "lease_token", "context_id", "context_digest", "event_ids"}
    if not required_lease.issubset(lease) or lease.get("schema_version") != 1 or lease.get("status") != "active":
        raise ToolError("invalid-recovery", "committed recovery lease fingerprint is invalid")
    if lease.get("action_id") != action_id or not isinstance(lease.get("lease_token"), str) or not lease["lease_token"]:
        raise ToolError("invalid-recovery", "committed recovery lease identity is invalid")
    _require_sha256(lease.get("context_id"), "recovery.proof.lease.context_id")
    _require_sha256(lease.get("context_digest"), "recovery.proof.lease.context_digest")
    event_ids = proof["event_ids"]
    if not isinstance(event_ids, list) or not event_ids or any(not isinstance(value, str) for value in event_ids):
        raise ToolError("invalid-recovery", "committed recovery event_ids must be a non-empty list")
    if len(set(event_ids)) != len(event_ids):
        raise ToolError("invalid-recovery", "committed recovery event_ids must be unique")
    for event_id in event_ids:
        _require_sha256(event_id, "recovery.proof.event_ids")
    if lease.get("event_ids") != event_ids:
        raise ToolError("invalid-recovery", "committed recovery event_ids must equal the lease fingerprint")
    events = proof["events"]
    if not isinstance(events, list) or [item.get("event_id") if isinstance(item, Mapping) else None for item in events] != event_ids:
        raise ToolError("invalid-recovery", "committed recovery event evidence must exactly match event_ids")
    if canonical_json_digest(proof) != recovery["recovery_id"]:
        raise ToolError("recovery-proof-mismatch", "committed recovery proof digest does not match its contents")
    return {"schema_version": 1, "recovery_id": recovery["recovery_id"], "proof": proof}


def read_committed_recovery(root: Path, action_id: str) -> dict[str, Any] | None:
    """Return one durable recovery proof, never synthesizing a missing one."""
    root = repository_root(root)
    path = _committed_recovery_path(root, action_id)
    if not path.exists():
        return None
    if path.is_symlink() or not path.is_file():
        raise ToolError("invalid-runtime-state", "committed recovery receipt is not a regular file")
    record = _read_json(path)
    if set(record) != {"schema_version", "kind", "recovery", "recorded_at"}:
        raise ToolError("invalid-runtime-state", "committed recovery receipt has an unexpected schema")
    if record.get("schema_version") != 1 or record.get("kind") != "committed-lease-recovery" or not isinstance(record.get("recorded_at"), str):
        raise ToolError("invalid-runtime-state", "committed recovery receipt is invalid")
    return _validated_committed_recovery(record["recovery"])


def release_verified_committed_recovery(
    root: Path,
    recovery: Mapping[str, Any],
    *,
    verify_recovery: Callable[[], Mapping[str, Any]],
) -> dict[str, Any]:
    """Durably record one verified committed recovery before releasing its exact lease.

    COMMIT_CHANGE_SET supplies the already-verified historical proof.  This
    function owns the serialized runtime transition, so it cannot be used as
    an unrecorded lease-unlink shortcut.
    """
    root = repository_root(root)
    verified = _validated_committed_recovery(recovery)
    proof = verified["proof"]
    action_id = proof["action_id"]
    expected_lease = _require_mapping(proof["lease"], "recovery.proof.lease")
    path = _committed_recovery_path(root, action_id)
    existing = read_committed_recovery(root, action_id)
    if existing is not None and existing != verified:
        raise ToolError("recovery-conflict", "existing committed recovery receipt differs from the verified proof")
    with _lease_guard(root, create=True):
        live_path = _lease_path(root)
        if not live_path.exists():
            if existing is not None:
                return {"status": "already-released", "recovery_receipt": path.relative_to(root).as_posix()}
            raise ToolError("lease-not-live", "repository lease is absent before committed recovery")
        live = _read_json(live_path)
        if live != expected_lease:
            raise ToolError("lease-not-live", "repository lease differs from the verified recovery fingerprint")
        if _validated_committed_recovery(verify_recovery()) != verified:
            raise ToolError("recovery-proof-mismatch", "live committed recovery evidence changed before receipt persistence")
        if existing is None:
            _atomic_json(
                path,
                {
                    "schema_version": 1,
                    "kind": "committed-lease-recovery",
                    "recovery": verified,
                    "recorded_at": dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
                },
            )
    # The ordinary release path rechecks the complete fingerprint inside its
    # own guards and retires any associated pipeline correlations first.
    release_verified_lease(
        root,
        {"status": "active", "action_id": action_id, "lease_token": expected_lease["lease_token"]},
        expected_live_lease=expected_lease,
        verify_recovery=lambda: _verified_recovery_matches(verified, verify_recovery),
    )
    return {"status": "released", "recovery_receipt": path.relative_to(root).as_posix()}


def _verified_recovery_matches(expected: Mapping[str, Any], reverify: Callable[[], Mapping[str, Any]]) -> None:
    if _validated_committed_recovery(reverify()) != expected:
        raise ToolError("recovery-proof-mismatch", "live committed recovery evidence changed before lease release")


def _blocked_path(root: Path, action_id: str) -> Path:
    return _runtime_dir(root) / "blocked" / f"{action_id}.json"


def record_blocked_state(
    root: Path,
    *,
    lease: Mapping[str, Any],
    action_id: str,
    event_ids: list[str],
    receipts: list[Mapping[str, Any]],
    reason: str,
) -> None:
    payload = {
        "schema_version": 1,
        "status": "blocked",
        "action_id": action_id,
        "event_ids": event_ids,
        "receipt_refs": [
            {
                "event_id": receipt["event_id"],
                "event_digest": receipt["event_digest"],
                "carrier": receipt["carrier"],
                "line": receipt["line"],
            }
            for receipt in receipts
        ],
        "lease_token": lease["lease_token"],
        "reason": reason,
    }
    _atomic_json(_blocked_path(root, action_id), payload)


def _blocked_receipts(root: Path, blocked: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Validate the Journal evidence retained for one blocked action."""
    action_id = str(blocked["action_id"])
    event_ids = blocked.get("event_ids")
    references = blocked.get("receipt_refs")
    if not isinstance(event_ids, list) or not isinstance(references, list) or len(event_ids) != len(references):
        raise ToolError("blocked-state-invalid", "blocked action receipt references are incomplete")
    receipts: list[dict[str, Any]] = []
    for event_id, raw in zip(event_ids, references, strict=True):
        reference = _require_mapping(raw, "blocked receipt reference")
        carrier = _relative_path(root, reference.get("carrier"), "receipt.carrier")
        line = reference.get("line")
        if not isinstance(line, int) or line < 1 or not carrier.is_file():
            raise ToolError("blocked-state-invalid", "blocked action Journal carrier is unavailable")
        lines = carrier.read_bytes().splitlines()
        if line > len(lines):
            raise ToolError("blocked-state-invalid", "blocked action Journal line is unavailable")
        record = _require_mapping(json.loads(lines[line - 1]), "blocked Journal record")
        if record.get("action_id") != action_id or record.get("event_id") != event_id:
            raise ToolError("blocked-state-invalid", "blocked action Journal identity does not match")
        if record.get("event_digest") != reference.get("event_digest"):
            raise ToolError("blocked-state-invalid", "blocked action Journal digest does not match")
        receipts.append(reference)
    return receipts


def resolve_blocked_action(
    root: Path,
    action_id: str,
    reason: str,
    *,
    apply: bool,
) -> dict[str, Any]:
    """Explicitly resolve one proven blocked action without deleting its Journal."""
    root = repository_root(root)
    _require_sha256(action_id, "action_id")
    if not reason.strip():
        raise ToolError("resolution-reason-missing", "operator resolution requires a reason")
    blocked_path = _blocked_path(root, action_id)
    blocked = _read_json(blocked_path)
    if blocked.get("status") != "blocked" or blocked.get("action_id") != action_id:
        raise ToolError("blocked-state-invalid", "selected blocked action is not active")
    receipts = _blocked_receipts(root, blocked)
    lease = _read_json(_lease_path(root))
    token = blocked.get("lease_token")
    if lease.get("status") != "active" or lease.get("action_id") != action_id or lease.get("lease_token") != token:
        raise ToolError("lease-not-live", "blocked action does not own the live repository lease")
    result = {
        "action_id": action_id,
        "reason": reason.strip(),
        "receipt_count": len(receipts),
        "journal_preserved": True,
        "apply": apply,
    }
    if not apply:
        return result
    retire_pipeline_correlations(root, action_id)
    with _lease_guard(root, create=True):
        current = _read_json(_lease_path(root))
        if current.get("action_id") != action_id or current.get("lease_token") != token:
            raise ToolError("lease-not-live", "blocked action lease changed before resolution")
        resolved = {
            **blocked,
            "status": "resolved",
            "resolution_reason": reason.strip(),
            "resolved_at": dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        }
        _atomic_json(blocked_path, resolved)
        _lease_path(root).unlink()
    return {**result, "status": "resolved"}


def _predicted_effects(root: Path, context: Mapping[str, Any], events: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    receipts = predict_sealed_event_receipts(
        root,
        events,
        author=context["author"],
        local_date=context["local_date"],
        timezone=context["timezone"],
    )
    return receipts, _lease_observation(root)


def describe() -> dict[str, Any]:
    return _json_result(
        ok=True,
        mode="read-only",
        result={
            "capability": {
                "capability_id": TOOL_ID,
                "kind": TOOL_KIND,
                "summary": "Append sealed schema-v2 Work Journal records with durable receipts.",
            },
            "input_schema": {
                "command": "--repository REPOSITORY run --input CONTEXT.json [--apply]",
                "required_context": [
                    "schema_version",
                    "context_id",
                    "action_id",
                    "trigger",
                    "subject",
                    "action_type",
                    "sources",
                    "result",
                    "llm_session",
                    "author",
                    "occurred_at",
                    "timezone",
                    "local_date",
                    "git_base",
                    "frontier",
                    "snapshots",
                    "validation",
                    "predictions.journal_records",
                    "predictions.journal_partitions",
                ],
            },
            "result_schema": {"resolved_targets": "object", "planned_effects": "object", "validation_results": "array", "receipts": "array", "lease": "object", "pipeline_correlations": "array"},
        },
        diagnostics=[],
    )


def run(root: Path, payload: Mapping[str, Any], *, apply: bool, wait_seconds: float) -> dict[str, Any]:
    context, events = validate_context(_normalise_context(payload))
    validation_results: list[dict[str, Any]] = [
        {"name": "sealed-context", "ok": True},
        {"name": "sealed-events", "ok": True},
    ]
    validate_live_preflight(root, context)
    validation_results.append({"name": "live-preflight", "ok": True})
    predicted_receipts, observed_lease = _predicted_effects(root, context, events)
    result_payload = {
        "resolved_targets": {"repository": str(root), "action_id": context["action_id"], "event_ids": [event["event_id"] for event in events]},
        "planned_effects": {"journal_records": events, "receipts": predicted_receipts},
        "validation_results": validation_results,
    }
    if not apply:
        return _json_result(ok=True, mode="dry-run", result={**result_payload, "receipts": predicted_receipts, "lease": observed_lease}, diagnostics=[])
    lease, acquired = acquire_lease(root, context, wait_seconds=wait_seconds)
    correlations: list[str] = []
    try:
        # Recheck every mutable boundary after the repository-scoped lease is acquired.
        validate_live_preflight(root, context)
        validation_results.append({"name": "leased-live-preflight", "ok": True})
        leased_predictions, _ = _predicted_effects(root, context, events)
        correlations = register_pipeline_correlations(root, context["action_id"], leased_predictions)
        receipts = append_sealed_events(
            root,
            events,
            author=context["author"],
            local_date=context["local_date"],
            timezone=context["timezone"],
        )
    except (ToolError, WorkJournalError) as error:
        # No append has occurred if every event prediction remains predicted.  A
        # partial append is retained as a recoverable blocked action and keeps
        # its lease for COMMIT_CHANGE_SET retry or explicit operator resolution.
        observed, _ = _predicted_effects(root, context, events)
        existing = [receipt for receipt in observed if receipt.get("disposition") == "reused"]
        if existing:
            record_blocked_state(
                root,
                lease=lease,
                action_id=context["action_id"],
                event_ids=[event["event_id"] for event in events],
                receipts=existing,
                reason=error.code,
            )
        else:
            retire_pipeline_correlations(root, context["action_id"])
            release_unconsumed_lease(root, lease, acquired=acquired)
        raise
    return _json_result(
        ok=True,
        mode="apply",
        result={
            **result_payload,
            "receipts": receipts,
            "lease": {"status": "active", "lease_token": lease["lease_token"], "action_id": lease["action_id"]},
            "pipeline_correlations": correlations,
        },
        diagnostics=[],
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=Path("."), help="CAPRMEDIO repository root")
    parser.add_argument("--root", dest="repository", type=Path, help=argparse.SUPPRESS)
    subcommands = parser.add_subparsers(dest="command", required=True)
    subcommands.add_parser("describe", help="emit Tool contract as JSON")
    run_parser = subcommands.add_parser("run", help="validate or append a sealed context")
    run_parser.add_argument("--input", required=True, help="JSON input path or - for stdin")
    run_parser.add_argument("--apply", action="store_true", help="append records; omission is dry-run")
    run_parser.add_argument("--wait-seconds", type=float, default=30.0, help="maximum repository-lease wait")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "describe":
            _emit(describe())
            return 0
        if args.wait_seconds < 0:
            raise ToolError("invalid-input", "wait_seconds must be non-negative")
        root = repository_root(args.repository)
        result = run(root, _load_json(args.input), apply=args.apply, wait_seconds=args.wait_seconds)
        _emit(result)
        return 0
    except (ToolError, WorkJournalError) as error:
        _emit(
            _json_result(
                ok=False,
                mode="apply" if getattr(args, "apply", False) else "dry-run",
                result={
                    "resolved_targets": {},
                    "planned_effects": {},
                    "validation_results": [],
                    "receipts": [],
                    "lease": {},
                },
                diagnostics=[{"code": error.code, "message": str(error)}],
            )
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
