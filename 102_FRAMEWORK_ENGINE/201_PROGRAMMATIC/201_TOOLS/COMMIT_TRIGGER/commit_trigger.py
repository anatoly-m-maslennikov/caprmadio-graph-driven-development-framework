#!/usr/bin/env python3
"""Emit minimal, mutation-free triggers for one governed repository file change.

COMMIT_TRIGGER is a Hook Tool.  It receives host-adapter observations as JSON,
coalesces repeated observations of one adapter source event, and emits the
canonical trigger envelope that COMMIT_CHANGE_SET accepts.  It never classifies
the change, reads the Atom graph, modifies the Git index, writes a Journal, or
invokes the downstream Tool itself.

The ``adapter`` lifecycle commands write only reconstructible registration
state below ``.caprmedio_runtime/state/commit_trigger``.  The generic user-level
Codex dispatcher delegates only for a repository carrying the installer-set
local Git activation marker.  Observation is always read-only, including when
it suppresses a correlated pipeline Journal or runtime-state event.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
import threading
import time
import tomllib
import uuid
from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve()
PACKAGE_ROOT = SCRIPT_PATH.parents[1]
CONTEXT_ROOT = PACKAGE_ROOT / "COMMIT_CONTEXT"


def _installed_project_root(path: Path) -> Path | None:
    for parent in path.parents:
        if parent.name == ".caprmedio_runtime":
            return parent.parent
        if parent.name == ".caprmedio_install":
            return parent.parent
        if parent.name == ".caprmedio":
            return parent.parent
    return None


if (project_root := _installed_project_root(SCRIPT_PATH)) is not None:
    sys.pycache_prefix = str(project_root / ".caprmedio_tmp" / "cache" / "python")

for _path in (PACKAGE_ROOT, CONTEXT_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from framework_installation import InstallationError, installation_status  # noqa: E402
from project_runtime import atomic_tempfile  # noqa: E402
from commit_context_logic import (  # noqa: E402
    configured_repository_paths,
    is_forbidden_commit_path,
    is_journal_path,
    project_path_eligible,
    repository_root,
)

TOOL_SCHEMA_VERSION = 1
TRIGGER_SCHEMA_VERSION = 1
CAPABILITY_ID = "COMMIT_TRIGGER"
TOOL_KIND = "hook"
RUNTIME_DIRECTORY = Path(".caprmedio_runtime/state/commit_trigger")
REGISTRY_NAME = "adapter_registry.toml"
PIPELINE_CORRELATIONS_NAME = "pipeline_correlations.ndjson"
HOOK_CONTROL_NAME = "hook_control.json"
CODEX_HOOK_MATCHER = ".*"
CODEX_HOOK_TIMEOUT_SECONDS = 5
CODEX_HOOK_BUDGET_SECONDS = 4.0
CODEX_ACTIVATION_KEY = "caprmedio.codex-hooks"
CODEX_ACTIVATION_VALUE = "v1"
MANAGED_GIT_HOOKS_PATH = ".caprmedio_runtime/tools/hooks/git"
STABLE_TRIGGER_LAUNCHER = ".caprmedio_runtime/tools/bin/commit-trigger"
GIT_HOOK_NAMES = ("pre-commit", "commit-msg", "post-commit")
GIT_HOOK_MARKER = "# CAPRMEDIO managed Git Hook v1"
IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9._-]{0,127}\Z")
UUID_TEXT = re.compile(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\Z",
    re.IGNORECASE,
)


class ToolError(RuntimeError):
    """A deterministic, machine-readable Tool failure."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


@dataclass(frozen=True)
class AdapterSpec:
    """One explicit host-adapter registration."""

    adapter_id: str
    application: str
    host_session_env: str
    fallback_session_env: str | None
    enabled: bool = True

    def __post_init__(self) -> None:
        _require_identifier(self.adapter_id, "adapter_id")
        _require_identifier(self.application, "application")
        _require_environment_name(self.host_session_env, "host_session_env")
        if self.fallback_session_env is not None:
            _require_environment_name(self.fallback_session_env, "fallback_session_env")


@dataclass(frozen=True)
class FileState:
    """A content-addressed eligible-file observation for the polling adapter."""

    path: str
    sha256: str
    identity: str
    line_count: int


@dataclass(frozen=True)
class PipelineCorrelation:
    """One exact downstream Journal transition that must not re-trigger."""

    correlation_id: str
    action_id: str
    event_id: str
    event_digest: str
    carrier: str
    line: int
    previous_carrier_digest: str
    appended_carrier_digest: str

    def __post_init__(self) -> None:
        if not re.fullmatch(r"[0-9a-f]{64}", self.correlation_id):
            raise ToolError("invalid-pipeline-correlation", "correlation_id must be a SHA-256 digest")
        _require_string(self.action_id, "action_id")
        _require_string(self.event_id, "event_id")
        if not re.fullmatch(r"[0-9a-f]{64}", self.event_digest):
            raise ToolError("invalid-pipeline-correlation", "event_digest must be a SHA-256 digest")
        _canonical_path(self.carrier, "carrier")
        if self.line < 1:
            raise ToolError("invalid-pipeline-correlation", "line must be a positive integer")
        for field, value in (
            ("previous_carrier_digest", self.previous_carrier_digest),
            ("appended_carrier_digest", self.appended_carrier_digest),
        ):
            if not re.fullmatch(r"[0-9a-f]{64}", value):
                raise ToolError("invalid-pipeline-correlation", f"{field} must be a SHA-256 digest")


def _require_identifier(value: object, field: str) -> str:
    if not isinstance(value, str) or not IDENTIFIER.fullmatch(value):
        raise ToolError("invalid-identifier", f"{field} must be an ASCII identifier")
    return value


def _require_environment_name(value: object, field: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[A-Z_][A-Z0-9_]*", value):
        raise ToolError("invalid-environment-name", f"{field} must be an uppercase environment name")
    return value


def _require_mapping(value: object, field: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ToolError("invalid-observation", f"{field} must be an object")
    return value


def _require_string(value: object, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ToolError("invalid-observation", f"{field} must be a non-empty string")
    return value


def _canonical_timestamp(value: object) -> str:
    source = _require_string(value, "observed_at")
    normalized = source[:-1] + "+00:00" if source.endswith("Z") else source
    try:
        moment = dt.datetime.fromisoformat(normalized)
    except ValueError as error:
        raise ToolError("invalid-observation-time", "observed_at must be RFC 3339") from error
    if moment.tzinfo is None:
        raise ToolError("invalid-observation-time", "observed_at must include a timezone")
    return moment.astimezone(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_path(value: object, field: str) -> str | None:
    if value is None:
        return None
    raw = _require_string(value, field)
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts or raw.startswith("./"):
        raise ToolError("invalid-observed-path", f"{field} must be a normalized repository-relative path")
    rendered = path.as_posix()
    if rendered in {".", ""}:
        raise ToolError("invalid-observed-path", f"{field} must name a file")
    return rendered


def _canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256(value: object) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def resolve_repository(path: Path) -> Path:
    """Resolve the repository top level without writing or initializing Git."""

    candidate = path.expanduser().resolve()
    completed = subprocess.run(
        ["git", "-C", str(candidate), "rev-parse", "--show-toplevel"],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise ToolError("repository-not-found", f"cannot resolve Git repository from {candidate}")
    return Path(completed.stdout.strip()).resolve()


def _repository_identity(repository: Path) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repository), "rev-parse", "--git-dir"],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise ToolError("repository-not-found", f"cannot resolve Git metadata for {repository}")
    git_directory = (repository / completed.stdout.strip()).resolve()
    return _sha256({"repository_root": repository.as_posix(), "git_directory": git_directory.as_posix()})


def _validate_uuid(value: object, field: str) -> str:
    raw = _require_string(value, field)
    if not UUID_TEXT.fullmatch(raw):
        raise ToolError("invalid-llm-session", f"{field} must be a UUID")
    return str(uuid.UUID(raw))


def resolve_codex_session(
    explicit_uuid: str | None = None,
    environment: Mapping[str, str] | None = None,
) -> dict[str, str]:
    """Resolve Codex provenance using explicit input, then native host variables."""

    if explicit_uuid is not None:
        return {"app": "codex", "uuid": _validate_uuid(explicit_uuid, "llm_session.uuid")}
    values = os.environ if environment is None else environment
    primary = values.get("CODEX_THREAD_ID")
    fallback = values.get("CODEX_SESSION_ID")
    if primary:
        return {"app": "codex", "uuid": _validate_uuid(primary, "CODEX_THREAD_ID")}
    if fallback:
        return {"app": "codex", "uuid": _validate_uuid(fallback, "CODEX_SESSION_ID")}
    raise ToolError("missing-llm-session", "Codex requires CODEX_THREAD_ID or CODEX_SESSION_ID")


def _resolve_session(
    observation: Mapping[str, Any],
    adapter: AdapterSpec,
    environment: Mapping[str, str],
) -> dict[str, str]:
    candidate = observation.get("llm_session")
    if candidate is not None:
        session = _require_mapping(candidate, "llm_session")
        app = _require_identifier(session.get("app"), "llm_session.app")
        if app != adapter.application:
            raise ToolError("llm-application-mismatch", "llm_session.app does not match the registered adapter")
        return {"app": app, "uuid": _validate_uuid(session.get("uuid"), "llm_session.uuid")}
    primary = environment.get(adapter.host_session_env)
    fallback = environment.get(adapter.fallback_session_env) if adapter.fallback_session_env else None
    if primary:
        return {"app": adapter.application, "uuid": _validate_uuid(primary, adapter.host_session_env)}
    if fallback:
        return {"app": adapter.application, "uuid": _validate_uuid(fallback, adapter.fallback_session_env or "session")}
    raise ToolError(
        "missing-llm-session",
        f"adapter {adapter.adapter_id} requires {adapter.host_session_env}"
        + (f" or {adapter.fallback_session_env}" if adapter.fallback_session_env else ""),
    )


def _is_pipeline_owned(observation: Mapping[str, Any]) -> bool:
    pipeline = observation.get("pipeline")
    if pipeline is None:
        return False
    details = _require_mapping(pipeline, "pipeline")
    if details.get("owned") is not True:
        return False
    action_id = details.get("action_id")
    if not isinstance(action_id, str) or not action_id:
        raise ToolError("invalid-pipeline-correlation", "pipeline-owned observation requires pipeline.action_id")
    kind = details.get("kind")
    if kind not in {"journal", "runtime-state"}:
        raise ToolError("invalid-pipeline-correlation", "pipeline.kind must be journal or runtime-state")
    return True


def _trigger_from_observation(
    observation: Mapping[str, Any],
    adapter: AdapterSpec,
    repository: Path,
    environment: Mapping[str, str],
) -> dict[str, object] | None:
    """Convert one host event to an immutable canonical trigger or suppress it."""

    adapter_id = _require_identifier(observation.get("adapter_id"), "adapter_id")
    if adapter_id != adapter.adapter_id:
        raise ToolError("unregistered-adapter", f"adapter {adapter_id} is not selected")
    if _is_pipeline_owned(observation):
        return None
    source_event_id = _require_string(observation.get("source_event_id"), "source_event_id")
    before_path = _canonical_path(observation.get("before_path"), "before_path")
    after_path = _canonical_path(observation.get("after_path"), "after_path")
    if before_path is None and after_path is None:
        raise ToolError("no-file-change", "observation must include before_path or after_path")
    observed_at = _canonical_timestamp(observation.get("observed_at"))
    llm_session = _resolve_session(observation, adapter, environment)
    repository_identity = _repository_identity(repository)
    identity_source = {
        "schema_version": TRIGGER_SCHEMA_VERSION,
        "adapter_id": adapter_id,
        "source_event_id": source_event_id,
        "repository_id": repository_identity,
    }
    return {
        "schema_version": TRIGGER_SCHEMA_VERSION,
        "trigger_id": _sha256(identity_source),
        "adapter": {"id": adapter_id},
        "source_event_id": source_event_id,
        "repository": {"root": repository.as_posix(), "identity": repository_identity},
        "observed_at": observed_at,
        "before_path": before_path,
        "after_path": after_path,
        "llm_session": llm_session,
    }


def emit_triggers(
    observations: Iterable[Mapping[str, Any]],
    *,
    adapter: AdapterSpec,
    repository: Path | str,
    environment: Mapping[str, str] | None = None,
) -> list[dict[str, object]]:
    """Coalesce accepted host observations without mutating any project state.

    Observations with equal adapter/source-event/repository identities must agree
    on the boundary and session provenance.  Their earliest observation time is
    retained so the result is independent of the host's noisy delivery order.
    """

    if not adapter.enabled:
        return []
    resolved_repository = resolve_repository(Path(repository))
    values = dict(os.environ if environment is None else environment)
    by_identity: dict[str, list[dict[str, object]]] = defaultdict(list)
    for raw in observations:
        trigger = _trigger_from_observation(_require_mapping(raw, "observation"), adapter, resolved_repository, values)
        if trigger is not None:
            by_identity[str(trigger["trigger_id"])].append(trigger)

    triggers: list[dict[str, object]] = []
    for trigger_id in sorted(by_identity):
        candidates = by_identity[trigger_id]
        baseline = candidates[0]
        comparable = ("adapter", "source_event_id", "repository", "before_path", "after_path", "llm_session")
        for candidate in candidates[1:]:
            if any(candidate[field] != baseline[field] for field in comparable):
                raise ToolError(
                    "ambiguous-source-event",
                    f"adapter source event cannot establish one boundary: {baseline['source_event_id']}",
                )
        selected = min(candidates, key=lambda candidate: str(candidate["observed_at"]))
        triggers.append(selected)
    return triggers


def _carrier_identity(relative: str, data: bytes) -> str:
    """Return a stable adapter-level carrier identity without graph traversal.

    The polling adapter needs only enough identity to pair the two path
    candidates of a move.  It does not inspect relations or classify the
    resulting action.  Invalid or non-Markdown carriers fall back to their
    address and are never guessed into a move.
    """

    path = Path(relative)
    if path.suffix != ".md":
        return f"path:{relative}"
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return f"path:{relative}"
    if text.startswith("---\n") and (boundary := text.find("\n---\n", 4)) >= 0:
        frontmatter = text[4:boundary]
        matches = re.findall(r"(?m)^atom_id:\s*['\"]?([^'\"\s]+)['\"]?\s*$", frontmatter)
        if len(matches) == 1:
            return f"atom:{matches[0]}"
    match = re.match(r"(CA-[RMCAPIDEO]-[0-9]+)(?:-|$)", path.name)
    if match:
        return f"atom:{match.group(1)}"
    if "--" in path.name:
        return f"carrier:{path.name.split('--', 1)[0]}"
    return f"path:{relative}"


def _is_work_journal_path(repository: Path, relative: str) -> bool:
    return is_journal_path(repository, relative, require_carrier=True)


def _path_candidate_admitted(repository: Path, relative: str, *, journal_for_correlation: bool = False) -> bool:
    path = Path(relative)
    if path.is_absolute() or not path.parts or ".." in path.parts or is_forbidden_commit_path(repository, relative):
        return False
    if _is_work_journal_path(repository, relative):
        return journal_for_correlation
    if path.parts[0].startswith(".") and len(path.parts) > 1:
        configured = configured_repository_paths(repository)
        admitted = (*configured.governed_roots, *configured.legacy_migration_roots)
        return any(path == root or path.parts[: len(root.parts)] == root.parts for root in admitted)
    return True


def _git_ignores(repository: Path, relative: str) -> bool:
    completed = subprocess.run(
        ["git", "-C", str(repository), "check-ignore", "--no-index", "-q", "--", relative],
        check=False,
        capture_output=True,
    )
    if completed.returncode in {0, 1}:
        return completed.returncode == 0
    raise ToolError(
        "git-ignore-check-failed",
        completed.stderr.decode("utf-8", "replace").strip() or f"cannot evaluate Git ignore rules for {relative}",
    )


def _git_ignored_paths(repository: Path, relatives: Sequence[str], *, timeout: float | None = None) -> set[str]:
    """Resolve Git ignore rules for one frontier with one bounded subprocess."""

    if not relatives:
        return set()
    try:
        completed = subprocess.run(
            ["git", "-C", str(repository), "check-ignore", "--no-index", "--stdin", "-z"],
            input=b"\0".join(relative.encode("utf-8") for relative in relatives) + b"\0",
            check=False,
            capture_output=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as error:
        raise ToolError("hook-budget-exceeded", "Git ignore evaluation exceeded the Hook time budget") from error
    if completed.returncode not in {0, 1}:
        raise ToolError(
            "git-ignore-check-failed",
            completed.stderr.decode("utf-8", "replace").strip() or "cannot evaluate Git ignore rules",
        )
    return {value.decode("utf-8") for value in completed.stdout.split(b"\0") if value}


def _project_path_eligible(repository: Path, relative: str, *, journal_for_correlation: bool = False) -> bool:
    if not _path_candidate_admitted(repository, relative, journal_for_correlation=journal_for_correlation):
        return False
    if _is_work_journal_path(repository, relative):
        return not _git_ignores(repository, relative)
    return project_path_eligible(repository, relative)


def _working_bytes(path: Path) -> bytes:
    if path.is_symlink():
        return os.readlink(path).encode("utf-8")
    return path.read_bytes()


def _remaining_hook_time(deadline: float | None) -> float | None:
    if deadline is None:
        return None
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise ToolError("hook-budget-exceeded", "CAPRMEDIO Hook exceeded its time budget")
    return remaining


def scan_governed_files(
    repository: Path | str,
    *,
    deadline: float | None = None,
    control_generation: int | None = None,
) -> dict[str, FileState]:
    """Read every Git-admitted project file plus Journal correlation carriers."""

    resolved_repository = repository_root(resolve_repository(Path(repository)))
    try:
        completed = subprocess.run(
            ["git", "-C", str(resolved_repository), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            check=False,
            capture_output=True,
            timeout=_remaining_hook_time(deadline),
        )
    except subprocess.TimeoutExpired as error:
        raise ToolError("hook-budget-exceeded", "Git frontier enumeration exceeded the Hook time budget") from error
    if completed.returncode != 0:
        raise ToolError(
            "git-project-frontier-failed",
            completed.stderr.decode("utf-8", "replace").strip() or "cannot enumerate the Git-admitted project frontier",
        )
    candidates = sorted(value.decode("utf-8") for value in completed.stdout.split(b"\0") if value)
    eligible_candidates = [
        relative
        for relative in candidates
        if _path_candidate_admitted(resolved_repository, relative, journal_for_correlation=True)
    ]
    ignored = _git_ignored_paths(
        resolved_repository,
        eligible_candidates,
        timeout=_remaining_hook_time(deadline),
    )
    result: dict[str, FileState] = {}
    for relative in eligible_candidates:
        _remaining_hook_time(deadline)
        if control_generation is not None:
            control = _read_hook_control(resolved_repository)
            if control["mode"] != "running" or control["generation"] != control_generation:
                raise ToolError("hook-control-changed", "CAPRMEDIO Hook control changed during execution")
        if relative in ignored:
            continue
        path = resolved_repository / relative
        if not path.is_file() and not path.is_symlink():
            continue
        data = _working_bytes(path)
        result[relative] = FileState(
            path=relative,
            sha256=hashlib.sha256(data).hexdigest(),
            identity=_carrier_identity(relative, data),
            line_count=len(data.splitlines()),
        )
    return result


def _watch_source_event_id(
    *,
    adapter_id: str,
    repository: Path,
    before_path: str | None,
    after_path: str | None,
    before_digest: str | None,
    after_digest: str | None,
) -> str:
    return "watch-" + _sha256(
        {
            "schema_version": 1,
            "adapter_id": adapter_id,
            "repository_id": _repository_identity(repository),
            "before_path": before_path,
            "after_path": after_path,
            "before_digest": before_digest,
            "after_digest": after_digest,
        }
    )


def _correlation_for(
    before: FileState | None,
    after: FileState | None,
    correlations: Mapping[str, Sequence[PipelineCorrelation]],
) -> PipelineCorrelation | None:
    if after is None:
        return None
    empty_digest = hashlib.sha256(b"").hexdigest()
    previous_digest = before.sha256 if before is not None else empty_digest
    matched = {
        correlation
        for correlation in correlations.get(after.path, ())
        if correlation.previous_carrier_digest == previous_digest
        and correlation.appended_carrier_digest == after.sha256
        and correlation.line == after.line_count
    }
    if not matched:
        return None
    if len(matched) != 1:
        actions = {correlation.action_id for correlation in matched}
        if len(actions) != 1:
            raise ToolError("ambiguous-pipeline-correlation", "one file event resolves to multiple pipeline actions")
        return sorted(matched, key=lambda item: item.correlation_id)[0]
    return next(iter(matched))


def _watch_observation(
    *,
    adapter_id: str,
    repository: Path,
    observed_at: str,
    before: FileState | None,
    after: FileState | None,
    correlations: Mapping[str, Sequence[PipelineCorrelation]],
) -> dict[str, object]:
    before_path = before.path if before is not None else None
    after_path = after.path if after is not None else None
    observation: dict[str, object] = {
        "adapter_id": adapter_id,
        "source_event_id": _watch_source_event_id(
            adapter_id=adapter_id,
            repository=repository,
            before_path=before_path,
            after_path=after_path,
            before_digest=before.sha256 if before is not None else None,
            after_digest=after.sha256 if after is not None else None,
        ),
        "observed_at": observed_at,
        "before_path": before_path,
        "after_path": after_path,
    }
    correlation = _correlation_for(before, after, correlations)
    if correlation is not None:
        observation["pipeline"] = {
            "owned": True,
            "action_id": correlation.action_id,
            "kind": "journal",
        }
    return observation


def detect_watch_observations(
    previous: Mapping[str, FileState],
    current: Mapping[str, FileState],
    *,
    adapter_id: str,
    repository: Path | str,
    observed_at: str,
    correlations: Mapping[str, Sequence[PipelineCorrelation]] | None = None,
) -> list[dict[str, object]]:
    """Derive deterministic ADD, REMOVE, MOVE, and UPDATE candidates from scans."""

    resolved_repository = resolve_repository(Path(repository))
    _require_identifier(adapter_id, "adapter_id")
    canonical_time = _canonical_timestamp(observed_at)
    active_correlations = {} if correlations is None else dict(correlations)
    removed = {path: previous[path] for path in sorted(set(previous) - set(current))}
    added = {path: current[path] for path in sorted(set(current) - set(previous))}
    modified = {
        path: (previous[path], current[path])
        for path in sorted(set(previous) & set(current))
        if previous[path].sha256 != current[path].sha256
    }
    observations: list[dict[str, object]] = []

    # One host callback is one observed operation.  When that operation changes
    # more than one file below one non-root folder, preserve it as one folder
    # subject instead of inventing independent file actions.  Journal changes
    # stay singular so exact pipeline correlation can suppress them.
    before_states = list(removed.values()) + [pair[0] for pair in modified.values()]
    after_states = list(added.values()) + [pair[1] for pair in modified.values()]
    logical_width = max(len(before_states), len(after_states))

    def common_folder(states: Sequence[FileState]) -> str | None:
        if not states:
            return None
        common = Path(os.path.commonpath([state.path for state in states]))
        if common.as_posix() in {state.path for state in states}:
            common = common.parent
        value = common.as_posix()
        return None if value in {"", "."} else value

    def folder_state(folder: str, states: Sequence[FileState]) -> FileState:
        entries = [
            {"path": state.path, "sha256": state.sha256}
            for state in sorted(states, key=lambda item: item.path)
        ]
        return FileState(
            path=folder,
            sha256=_sha256(entries),
            identity=f"folder:{folder}",
            line_count=sum(state.line_count for state in states),
        )

    before_folder = common_folder(before_states)
    after_folder = common_folder(after_states)
    changed_paths = {state.path for state in before_states + after_states}
    if (
        logical_width > 1
        and not any(_is_work_journal_path(resolved_repository, path) for path in changed_paths)
        and (before_folder is None or _project_path_eligible(resolved_repository, before_folder))
        and (after_folder is None or _project_path_eligible(resolved_repository, after_folder))
    ):
        observations.append(
            _watch_observation(
                adapter_id=adapter_id,
                repository=resolved_repository,
                observed_at=canonical_time,
                before=folder_state(before_folder, before_states) if before_folder is not None else None,
                after=folder_state(after_folder, after_states) if after_folder is not None else None,
                correlations=active_correlations,
            )
        )
        return observations

    # A unique stable carrier identity establishes one old/new path boundary,
    # including when the carrier was edited during relocation.  This remains
    # adapter-level event correlation; COMMIT_CONTEXT owns MOVE/UPDATE
    # classification and all graph traversal.
    removed_by_identity: dict[str, list[FileState]] = defaultdict(list)
    added_by_identity: dict[str, list[FileState]] = defaultdict(list)
    for state in removed.values():
        removed_by_identity[state.identity].append(state)
    for state in added.values():
        added_by_identity[state.identity].append(state)
    for identity in sorted(set(removed_by_identity) & set(added_by_identity)):
        before_states = removed_by_identity[identity]
        after_states = added_by_identity[identity]
        if len(before_states) == len(after_states) == 1 and not identity.startswith("path:"):
            before = before_states[0]
            after = after_states[0]
            observations.append(
                _watch_observation(
                    adapter_id=adapter_id,
                    repository=resolved_repository,
                    observed_at=canonical_time,
                    before=before,
                    after=after,
                    correlations=active_correlations,
                )
            )
            removed.pop(before.path)
            added.pop(after.path)

    # Equal content safely pairs remaining opaque carriers without assigning
    # semantic meaning to the boundary.
    removed_by_digest: dict[str, list[FileState]] = defaultdict(list)
    added_by_digest: dict[str, list[FileState]] = defaultdict(list)
    for state in removed.values():
        removed_by_digest[state.sha256].append(state)
    for state in added.values():
        added_by_digest[state.sha256].append(state)
    for digest in sorted(set(removed_by_digest) & set(added_by_digest)):
        before_states = removed_by_digest[digest]
        after_states = added_by_digest[digest]
        if len(before_states) == len(after_states) == 1:
            before = before_states[0]
            after = after_states[0]
            observations.append(
                _watch_observation(
                    adapter_id=adapter_id,
                    repository=resolved_repository,
                    observed_at=canonical_time,
                    before=before,
                    after=after,
                    correlations=active_correlations,
                )
            )
            removed.pop(before.path)
            added.pop(after.path)

    for path in sorted(removed):
        observations.append(
            _watch_observation(
                adapter_id=adapter_id,
                repository=resolved_repository,
                observed_at=canonical_time,
                before=removed[path],
                after=None,
                correlations=active_correlations,
            )
        )
    for path in sorted(added):
        observations.append(
            _watch_observation(
                adapter_id=adapter_id,
                repository=resolved_repository,
                observed_at=canonical_time,
                before=None,
                after=added[path],
                correlations=active_correlations,
            )
        )
    for path in sorted(modified):
        before, after = modified[path]
        observations.append(
            _watch_observation(
                adapter_id=adapter_id,
                repository=resolved_repository,
                observed_at=canonical_time,
                before=before,
                after=after,
                correlations=active_correlations,
            )
        )
    return sorted(observations, key=lambda item: str(item["source_event_id"]))


def _read_pipeline_correlations(path: Path) -> dict[str, tuple[PipelineCorrelation, ...]]:
    """Replay the exact active Journal-transition suppression frontier."""

    if not path.exists():
        return {}
    registrations: dict[str, PipelineCorrelation] = {}
    active: dict[str, bool] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line:
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: invalid JSON") from error
        record = _require_mapping(value, "pipeline correlation")
        if record.get("schema_version") != 1:
            raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: unsupported schema_version")
        correlation_id = _require_string(record.get("correlation_id"), "correlation_id")
        event = record.get("event")
        if event == "retired":
            if correlation_id not in registrations:
                raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: retirement precedes registration")
            if record.get("action_id") != registrations[correlation_id].action_id:
                raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: retirement action differs")
            active[correlation_id] = False
            continue
        if event != "registered":
            raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: event must be registered or retired")
        transition = _require_mapping(record.get("transition"), "transition")
        correlation = PipelineCorrelation(
            correlation_id=correlation_id,
            action_id=_require_string(record.get("action_id"), "action_id"),
            event_id=_require_string(transition.get("event_id"), "event_id"),
            event_digest=_require_string(transition.get("event_digest"), "event_digest"),
            carrier=_canonical_path(transition.get("carrier"), "carrier") or "",
            line=transition.get("line") if isinstance(transition.get("line"), int) else 0,
            previous_carrier_digest=_require_string(
                transition.get("previous_carrier_digest"), "previous_carrier_digest"
            ),
            appended_carrier_digest=_require_string(
                transition.get("appended_carrier_digest"), "appended_carrier_digest"
            ),
        )
        expected_id = _sha256(
            {
                "action_id": correlation.action_id,
                "transition": {
                    "event_id": correlation.event_id,
                    "event_digest": correlation.event_digest,
                    "carrier": correlation.carrier,
                    "line": correlation.line,
                    "previous_carrier_digest": correlation.previous_carrier_digest,
                    "appended_carrier_digest": correlation.appended_carrier_digest,
                },
            }
        )
        if expected_id != correlation_id:
            raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: correlation_id digest differs")
        previous = registrations.get(correlation_id)
        if previous is not None and previous != correlation:
            raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: correlation identity collision")
        registrations[correlation_id] = correlation
        active[correlation_id] = True
    grouped: dict[str, list[PipelineCorrelation]] = defaultdict(list)
    for correlation_id, correlation in registrations.items():
        if active.get(correlation_id):
            grouped[correlation.carrier].append(correlation)
    return {
        carrier: tuple(sorted(values, key=lambda item: item.correlation_id))
        for carrier, values in grouped.items()
    }


def watch_triggers(
    *,
    repository: Path | str,
    adapter: AdapterSpec,
    environment: Mapping[str, str] | None = None,
    poll_interval: float = 1.0,
    maximum_polls: int | None = None,
    pipeline_correlation_path: Path | None = None,
    stop: threading.Event | None = None,
) -> Iterable[list[dict[str, object]]]:
    """Yield native Codex polling-adapter handoffs until stopped.

    The caller owns downstream execution.  Each yielded list is already
    deduplicated and may be empty only when no source change was observed.
    """

    if adapter.application != "codex":
        raise ToolError("unsupported-native-adapter", "watch supports only the native Codex adapter")
    if poll_interval <= 0:
        raise ToolError("invalid-poll-interval", "poll_interval must be greater than zero")
    if maximum_polls is not None and maximum_polls < 0:
        raise ToolError("invalid-maximum-polls", "maximum_polls must not be negative")
    resolved_repository = resolve_repository(Path(repository))
    correlation_path = pipeline_correlation_path or _runtime_directory(resolved_repository) / PIPELINE_CORRELATIONS_NAME
    previous = scan_governed_files(resolved_repository)
    polls = 0
    while maximum_polls is None or polls < maximum_polls:
        if stop is not None and stop.is_set():
            return
        time.sleep(poll_interval)
        current = scan_governed_files(resolved_repository)
        correlations = _read_pipeline_correlations(correlation_path)
        observations = detect_watch_observations(
            previous,
            current,
            adapter_id=adapter.adapter_id,
            repository=resolved_repository,
            observed_at=dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            correlations=correlations,
        )
        previous = current
        polls += 1
        if observations:
            yield emit_triggers(observations, adapter=adapter, repository=resolved_repository, environment=environment)


def _runtime_directory(repository: Path) -> Path:
    return repository / RUNTIME_DIRECTORY


def _runtime_root(repository: Path) -> Path:
    return repository / ".caprmedio_runtime"


def _tools_runtime_root(repository: Path) -> Path:
    return repository / ".caprmedio_runtime/tools"


def _registry_path(repository: Path) -> Path:
    return _runtime_directory(repository) / REGISTRY_NAME


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _read_registry(repository: Path) -> dict[str, AdapterSpec]:
    path = _registry_path(repository)
    if not path.exists():
        return {}
    try:
        document = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as error:
        raise ToolError("invalid-adapter-registry", f"{path}: invalid TOML") from error
    if document.get("schema_version") != TOOL_SCHEMA_VERSION:
        raise ToolError("invalid-adapter-registry", "adapter registry schema_version is unsupported")
    adapters = document.get("adapters")
    if not isinstance(adapters, Mapping):
        raise ToolError("invalid-adapter-registry", "adapter registry requires [adapters]")
    result: dict[str, AdapterSpec] = {}
    for adapter_id, values in adapters.items():
        if not isinstance(values, Mapping):
            raise ToolError("invalid-adapter-registry", f"adapter {adapter_id} must be a table")
        result[str(adapter_id)] = AdapterSpec(
            adapter_id=str(adapter_id),
            application=_require_string(values.get("application"), f"adapter {adapter_id}.application"),
            host_session_env=_require_string(values.get("host_session_env"), f"adapter {adapter_id}.host_session_env"),
            fallback_session_env=(
                _require_string(values["fallback_session_env"], f"adapter {adapter_id}.fallback_session_env")
                if values.get("fallback_session_env") is not None
                else None
            ),
            enabled=values.get("enabled") is True,
        )
    return result


def _render_registry(adapters: Mapping[str, AdapterSpec]) -> str:
    lines = [f"schema_version = {TOOL_SCHEMA_VERSION}", ""]
    for adapter_id in sorted(adapters):
        adapter = adapters[adapter_id]
        lines.extend(
            [
                f'[adapters.{_quoted(adapter.adapter_id)}]',
                f"application = {_quoted(adapter.application)}",
                f"host_session_env = {_quoted(adapter.host_session_env)}",
            ]
        )
        if adapter.fallback_session_env is not None:
            lines.append(f"fallback_session_env = {_quoted(adapter.fallback_session_env)}")
        lines.extend([f"enabled = {'true' if adapter.enabled else 'false'}", ""])
    return "\n".join(lines)


def _atomic_write(path: Path, content: str, *, repository: Path | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = atomic_tempfile(path, "commit_trigger", repository=repository)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def _atomic_write_if_changed(path: Path, content: str, *, repository: Path | None = None) -> bool:
    """Preserve an already-current Carrier without requiring write access."""

    try:
        if path.read_text(encoding="utf-8") == content:
            return False
    except FileNotFoundError:
        pass
    _atomic_write(path, content, repository=repository)
    return True


def _hook_control_path(repository: Path) -> Path:
    return _runtime_directory(repository) / HOOK_CONTROL_NAME


def _read_hook_control(repository: Path) -> dict[str, object]:
    path = _hook_control_path(repository)
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {"schema_version": 1, "mode": "running", "generation": 0, "reason": "default"}
    except (OSError, json.JSONDecodeError):
        return {"schema_version": 1, "mode": "tripped", "generation": 0, "reason": "invalid-control-state"}
    if (
        not isinstance(document, Mapping)
        or document.get("schema_version") != 1
        or document.get("mode") not in {"running", "stopped", "tripped"}
        or not isinstance(document.get("generation"), int)
        or int(document["generation"]) < 0
    ):
        return {"schema_version": 1, "mode": "tripped", "generation": 0, "reason": "invalid-control-state"}
    return dict(document)


def _write_hook_control(repository: Path, *, mode: str, generation: int, reason: str) -> dict[str, object]:
    document: dict[str, object] = {
        "schema_version": 1,
        "mode": mode,
        "generation": generation,
        "reason": reason,
        "changed_at": dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }
    _atomic_write(_hook_control_path(repository), _canonical_json(document) + "\n")
    return document


def _trip_hook_control(repository: Path, reason: str) -> dict[str, object]:
    current = _read_hook_control(repository)
    if current["mode"] != "running":
        return current
    return _write_hook_control(
        repository,
        mode="tripped",
        generation=int(current["generation"]) + 1,
        reason=reason,
    )


def _transient_hook_files(repository: Path) -> list[Path]:
    runtime = _runtime_directory(repository)
    return sorted(
        path
        for directory in (runtime / "hook_snapshots", runtime / "session_baselines")
        if directory.is_dir()
        for path in directory.glob("*.json")
        if path.is_file()
    )


def hook_control(
    repository: Path | str,
    operation: str,
    *,
    apply: bool = False,
    reason: str | None = None,
) -> dict[str, object]:
    """Inspect or operate the Hook circuit without invoking Hook work."""

    root = resolve_repository(Path(repository))
    current = _read_hook_control(root)
    transient = _transient_hook_files(root)
    if operation == "status":
        return {"repository": root.as_posix(), "control": current, "transient_file_count": len(transient)}
    if operation not in {"stop", "start", "reload"}:
        raise ToolError("unknown-control-operation", f"unknown Hook control operation: {operation}")
    next_mode = "stopped" if operation == "stop" else "running"
    result: dict[str, object] = {
        "repository": root.as_posix(),
        "operation": operation,
        "apply": apply,
        "previous": current,
        "proposed_mode": next_mode,
        "transient_file_count": len(transient),
        "removed_transient_files": 0,
    }
    if not apply:
        return result
    generation = int(current["generation"]) + 1
    if operation == "reload":
        _write_hook_control(root, mode="stopped", generation=generation, reason=reason or "manual-reload")
        removed = 0
        for path in transient:
            try:
                path.unlink()
            except FileNotFoundError:
                continue
            removed += 1
        generation += 1
        result["removed_transient_files"] = removed
    result["control"] = _write_hook_control(
        root,
        mode=next_mode,
        generation=generation,
        reason=reason or f"manual-{operation}",
    )
    return result


def runtime_package_status(repository: Path | str) -> dict[str, object]:
    try:
        return installation_status(repository)
    except InstallationError as error:
        raise ToolError(error.code, error.message) from error


def _codex_home(environment: Mapping[str, str] | None = None) -> Path:
    source = os.environ if environment is None else environment
    configured = source.get("CODEX_HOME")
    return Path(configured).expanduser().resolve() if configured else (Path.home() / ".codex").resolve()


def _local_codex_activation(repository: Path) -> str | None:
    completed = subprocess.run(
        ["git", "-C", str(repository), "config", "--local", "--get", CODEX_ACTIVATION_KEY],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode == 1:
        return None
    if completed.returncode != 0:
        raise ToolError("git-config-failed", (completed.stderr or completed.stdout).strip() or "cannot read Codex activation")
    return completed.stdout.strip()


def _set_local_codex_activation(repository: Path, value: str | None) -> None:
    command = ["git", "-C", str(repository), "config", "--local"]
    command += ["--unset-all", CODEX_ACTIVATION_KEY] if value is None else [CODEX_ACTIVATION_KEY, value]
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    accepted = {0, 5} if value is None else {0}
    if completed.returncode not in accepted:
        raise ToolError("git-config-failed", (completed.stderr or completed.stdout).strip() or "cannot update Codex activation")


def _managed_hook_command(phase: str, adapter_id: str) -> str:
    arguments = " ".join(shlex.quote(value) for value in ("codex-hook", phase, "--adapter-id", adapter_id))
    return (
        "root=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0; "
        f'activation=$(git -C "$root" config --local --get {shlex.quote(CODEX_ACTIVATION_KEY)} 2>/dev/null) || exit 0; '
        f'[ "$activation" = {shlex.quote(CODEX_ACTIVATION_VALUE)} ] || exit 0; '
        f'launcher="$root/{STABLE_TRIGGER_LAUNCHER}"; '
        '[ -x "$launcher" ] || exit 0; '
        f'exec "$launcher" {arguments}'
    )


def _managed_hook_group(phase: str, adapter_id: str) -> dict[str, object]:
    return {
        "matcher": CODEX_HOOK_MATCHER,
        "hooks": [
            {
                "type": "command",
                "command": _managed_hook_command(phase, adapter_id),
                "timeout": CODEX_HOOK_TIMEOUT_SECONDS,
                "statusMessage": f"CAPRMEDIO auto-commit {phase}",
            }
        ],
    }


def _is_managed_hook_group(value: object) -> bool:
    if not isinstance(value, Mapping):
        return False
    hooks = value.get("hooks")
    if not isinstance(hooks, list):
        return False
    return any(
        isinstance(hook, Mapping)
        and isinstance(hook.get("command"), str)
        and any(
            marker in str(hook["command"])
            for marker in (
                ".caprmedio_runtime/tools/bin/commit-trigger",
                ".caprmedio_runtime/tools/releases/",
                ".caprmedio_install/bin/commit-trigger",
                ".caprmedio_install/releases/",
                ".caprmedio_runtime/installed/tools/auto_commit/",
                CODEX_ACTIVATION_KEY,
            )
        )
        and " codex-hook " in str(hook["command"])
        for hook in hooks
    )


def _hook_document(adapter_id: str, existing: Mapping[str, Any] | None = None) -> dict[str, Any]:
    document = dict(existing or {})
    document.setdefault("description", "User-level Codex hooks.")
    raw_hooks = document.get("hooks")
    hooks = dict(raw_hooks) if isinstance(raw_hooks, Mapping) else {}
    for event, phase in (
        ("PreToolUse", "pre"),
        ("PostToolUse", "post"),
        ("SessionStart", "start"),
        ("Stop", "stop"),
    ):
        groups = hooks.get(event)
        retained = [group for group in groups if not _is_managed_hook_group(group)] if isinstance(groups, list) else []
        hooks[event] = [*retained, _managed_hook_group(phase, adapter_id)]
    document["hooks"] = hooks
    return document


def _without_managed_hooks(document: Mapping[str, Any]) -> tuple[dict[str, Any], bool]:
    result = dict(document)
    raw_hooks = result.get("hooks")
    hooks = dict(raw_hooks) if isinstance(raw_hooks, Mapping) else {}
    changed = False
    for event in ("PreToolUse", "PostToolUse", "SessionStart", "Stop"):
        groups = hooks.get(event)
        if not isinstance(groups, list):
            continue
        retained = [group for group in groups if not _is_managed_hook_group(group)]
        changed = changed or len(retained) != len(groups)
        if retained:
            hooks[event] = retained
        else:
            hooks.pop(event, None)
    result["hooks"] = hooks
    return result, changed


def _read_hook_document(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as error:
        raise ToolError("codex-hook-config-invalid", f"{path}: invalid JSON") from error
    if not isinstance(value, dict):
        raise ToolError("codex-hook-config-invalid", f"{path}: root must be an object")
    return value


def install_codex_hooks(repository: Path, adapter_id: str) -> dict[str, object]:
    runtime_config = _tools_runtime_root(repository) / "hooks" / "codex" / "hooks.json"
    project_config = repository / ".codex" / "hooks.json"
    user_config = _codex_home() / "hooks.json"
    managed = _hook_document(adapter_id)
    _atomic_write_if_changed(runtime_config, json.dumps(managed, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    merged = _hook_document(adapter_id, _read_hook_document(user_config))
    user_carrier_changed = _atomic_write_if_changed(
        user_config,
        json.dumps(merged, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        repository=repository,
    )

    project_changed = False
    if project_config.is_symlink() and project_config.resolve() == runtime_config.resolve():
        project_config.unlink()
        project_changed = True
    elif project_config.is_file() and not project_config.is_symlink():
        project_document = _read_hook_document(project_config)
        retained, changed = _without_managed_hooks(project_document)
        if changed:
            remaining = retained.get("hooks")
            if not remaining and project_document.get("description") == "Project-local Codex hooks.":
                project_config.unlink()
            else:
                _atomic_write(project_config, json.dumps(retained, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
            project_changed = True
    _set_local_codex_activation(repository, CODEX_ACTIVATION_VALUE)
    return {
        "registered": True,
        "carrier": user_config.as_posix(),
        "carrier_kind": "merged-user-config",
        "carrier_changed": user_carrier_changed,
        "canonical_fragment": runtime_config.relative_to(repository).as_posix(),
        "project_carrier_removed": project_changed,
        "activation": CODEX_ACTIVATION_VALUE,
    }


def uninstall_codex_hooks(repository: Path) -> dict[str, object]:
    runtime_config = _tools_runtime_root(repository) / "hooks" / "codex" / "hooks.json"
    project_config = repository / ".codex" / "hooks.json"
    changed = False
    if project_config.is_symlink() and project_config.resolve() == runtime_config.resolve():
        project_config.unlink()
        changed = True
    elif project_config.is_file():
        document = _read_hook_document(project_config)
        raw_hooks = document.get("hooks")
        hooks = dict(raw_hooks) if isinstance(raw_hooks, Mapping) else {}
        retained, stripped = _without_managed_hooks(document)
        changed = changed or stripped
        _atomic_write(project_config, json.dumps(retained, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    try:
        runtime_config.unlink()
    except FileNotFoundError:
        pass
    _set_local_codex_activation(repository, None)
    return {
        "registered": False,
        "changed": changed,
        "shared_user_carrier_preserved": True,
        "carrier": (_codex_home() / "hooks.json").as_posix(),
    }


def codex_hooks_status(repository: Path, adapter_id: str) -> dict[str, object]:
    user_config = _codex_home() / "hooks.json"
    fragment = _tools_runtime_root(repository) / "hooks" / "codex" / "hooks.json"
    try:
        document = _read_hook_document(user_config)
    except ToolError:
        document = {}
    raw_hooks = document.get("hooks")
    hooks = raw_hooks if isinstance(raw_hooks, Mapping) else {}
    phases = {
        event: any(group == _managed_hook_group(phase, adapter_id) for group in hooks.get(event, []) if isinstance(group, Mapping))
        for event, phase in (
            ("PreToolUse", "pre"),
            ("PostToolUse", "post"),
            ("SessionStart", "start"),
            ("Stop", "stop"),
        )
    }
    return {
        "registered": all(phases.values()) and _local_codex_activation(repository) == CODEX_ACTIVATION_VALUE,
        "carrier": user_config.as_posix(),
        "canonical_fragment": fragment.relative_to(repository).as_posix(),
        "canonical_fragment_present": fragment.is_file(),
        "activation": _local_codex_activation(repository),
        "phases": phases,
        "project_carrier_present": (repository / ".codex/hooks.json").exists(),
    }


def _local_git_hooks_path(repository: Path) -> str | None:
    completed = subprocess.run(
        ["git", "-C", str(repository), "config", "--local", "--get", "core.hooksPath"],
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode == 1:
        return None
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout).strip()
        raise ToolError("git-config-failed", detail or "cannot read repository-local core.hooksPath")
    return completed.stdout.strip()


def _managed_git_hook_script(repository: Path, hook_name: str) -> str:
    if hook_name not in GIT_HOOK_NAMES:
        raise ToolError("git-hook-invalid", f"unsupported Git Hook: {hook_name}")
    status = runtime_package_status(repository)
    if status.get("installed") is not True:
        raise ToolError("tools-not-installed", "run INSTALL_TOOLS before installing Git Hooks")
    tool = Path(str(status["package_root"])) / "COMMIT_CHANGE_SET" / "commit_change_set.py"
    return "\n".join(
        [
            "#!/bin/sh",
            GIT_HOOK_MARKER,
            "set -eu",
            'repository=$(git rev-parse --show-toplevel)',
            'git_directory=$(git rev-parse --absolute-git-dir)',
            f'legacy="$git_directory/hooks/{hook_name}"',
            'if [ -x "$legacy" ]; then',
            '  "$legacy" "$@"',
            "fi",
            "exec "
            + " ".join(
                [
                    shlex.quote(sys.executable),
                    "-I",
                    "-B",
                    f'"$repository/{tool.as_posix()}"',
                    "--repository",
                    '"$repository"',
                    "git-hook",
                    hook_name,
                    '"$@"',
                ]
            ),
            "",
        ]
    )


def install_git_hooks(repository: Path) -> dict[str, object]:
    existing = _local_git_hooks_path(repository)
    if existing not in {None, MANAGED_GIT_HOOKS_PATH}:
        raise ToolError(
            "git-hooks-path-conflict",
            f"repository already uses a different local core.hooksPath: {existing}",
        )
    directory = repository / MANAGED_GIT_HOOKS_PATH
    directory.mkdir(parents=True, exist_ok=True)
    carriers: list[str] = []
    for hook_name in GIT_HOOK_NAMES:
        carrier = directory / hook_name
        _atomic_write(carrier, _managed_git_hook_script(repository, hook_name))
        carrier.chmod(0o755)
        carriers.append(carrier.relative_to(repository).as_posix())
    completed = subprocess.run(
        ["git", "-C", str(repository), "config", "--local", "core.hooksPath", MANAGED_GIT_HOOKS_PATH],
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout).strip()
        raise ToolError("git-config-failed", detail or "cannot register runtime-owned Git Hooks")
    return {
        "registered": True,
        "hooks_path": MANAGED_GIT_HOOKS_PATH,
        "carriers": carriers,
        "preserved_default_hooks": True,
    }


def uninstall_git_hooks(repository: Path) -> dict[str, object]:
    existing = _local_git_hooks_path(repository)
    changed = False
    if existing == MANAGED_GIT_HOOKS_PATH:
        completed = subprocess.run(
            ["git", "-C", str(repository), "config", "--local", "--unset-all", "core.hooksPath"],
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode not in {0, 5}:
            detail = (completed.stderr or completed.stdout).strip()
            raise ToolError("git-config-failed", detail or "cannot remove runtime-owned Git Hook registration")
        changed = True
    directory = repository / MANAGED_GIT_HOOKS_PATH
    removed: list[str] = []
    for hook_name in GIT_HOOK_NAMES:
        carrier = directory / hook_name
        try:
            first_lines = carrier.read_text(encoding="utf-8").splitlines()[:2]
        except FileNotFoundError:
            continue
        if GIT_HOOK_MARKER not in first_lines:
            raise ToolError("git-hook-carrier-conflict", f"refusing to remove unrecognized runtime Hook carrier: {carrier}")
        carrier.unlink()
        removed.append(carrier.relative_to(repository).as_posix())
    return {
        "registered": False,
        "changed": changed or bool(removed),
        "hooks_path": MANAGED_GIT_HOOKS_PATH,
        "removed": removed,
        "preserved_default_hooks": True,
    }


def _write_registry(repository: Path, adapters: Mapping[str, AdapterSpec]) -> None:
    path = _registry_path(repository)
    if not adapters:
        try:
            path.unlink()
        except FileNotFoundError:
            return
        return
    _atomic_write(path, _render_registry(adapters))


def adapter_operation(
    repository: Path | str,
    operation: str,
    *,
    adapter: AdapterSpec | None = None,
    adapter_id: str | None = None,
    apply: bool = False,
    manage_host_hooks: bool = False,
) -> dict[str, object]:
    """Inspect or explicitly change reconstructible adapter registration state."""

    resolved_repository = resolve_repository(Path(repository))
    registered = _read_registry(resolved_repository)
    if operation == "status":
        codex_status = codex_hooks_status(resolved_repository, "codex-file-events")
        git_hooks_path = _local_git_hooks_path(resolved_repository)
        git_hook_carriers = [resolved_repository / MANAGED_GIT_HOOKS_PATH / name for name in GIT_HOOK_NAMES]
        return {
            "repository": resolved_repository.as_posix(),
            "registry": _registry_path(resolved_repository).relative_to(resolved_repository).as_posix(),
            "adapters": [
                {
                    "adapter_id": entry.adapter_id,
                    "application": entry.application,
                    "host_session_env": entry.host_session_env,
                    "fallback_session_env": entry.fallback_session_env,
                    "enabled": entry.enabled,
                }
                for entry in (registered[key] for key in sorted(registered))
            ],
            "host_hook_registered": codex_status["registered"],
            "host_hook_carrier": codex_status["carrier"],
            "host_hook_phases": codex_status["phases"],
            "host_hook_project_carrier_present": codex_status["project_carrier_present"],
            "host_hook_activation": "host-controlled-unverified",
            "host_hook_operator_action": "Restart or resume each Codex task and review the changed user hooks once with /hooks.",
            "git_hooks_registered": git_hooks_path == MANAGED_GIT_HOOKS_PATH and all(path.is_file() and os.access(path, os.X_OK) for path in git_hook_carriers),
            "git_hooks_path": git_hooks_path,
            "git_hook_carriers": [path.relative_to(resolved_repository).as_posix() for path in git_hook_carriers],
            "installation": runtime_package_status(resolved_repository),
        }

    if operation == "install":
        if adapter is None:
            raise ToolError("missing-adapter", "install requires an adapter specification")
        previous = registered.get(adapter.adapter_id)
        if previous is not None and previous != adapter:
            raise ToolError("adapter-already-registered", f"adapter {adapter.adapter_id} is already registered differently")
        proposed = dict(registered)
        proposed[adapter.adapter_id] = adapter
        effect = "already-installed" if previous is not None else "register-adapter"
    else:
        selected_id = _require_identifier(adapter_id, "adapter_id")
        previous = registered.get(selected_id)
        if previous is None:
            if operation == "uninstall":
                return {"repository": resolved_repository.as_posix(), "effect": "already-uninstalled", "adapter_id": selected_id}
            raise ToolError("adapter-not-registered", f"adapter {selected_id} is not registered")
        proposed = dict(registered)
        if operation == "enable":
            proposed[selected_id] = AdapterSpec(
                selected_id, previous.application, previous.host_session_env, previous.fallback_session_env, True
            )
            effect = "enable-adapter"
        elif operation == "disable":
            proposed[selected_id] = AdapterSpec(
                selected_id, previous.application, previous.host_session_env, previous.fallback_session_env, False
            )
            effect = "disable-adapter"
        elif operation == "uninstall":
            del proposed[selected_id]
            effect = "unregister-adapter"
        else:
            raise ToolError("unknown-operation", f"unknown adapter operation: {operation}")

    hook_result: dict[str, object] | None = None
    if apply and manage_host_hooks and operation == "install":
        assert adapter is not None
        hook_result = {
            "codex": install_codex_hooks(resolved_repository, adapter.adapter_id),
            "git": install_git_hooks(resolved_repository),
        }
    if apply:
        _write_registry(resolved_repository, proposed)
    if apply and manage_host_hooks and operation == "uninstall" and not proposed:
        hook_result = {
            "codex": uninstall_codex_hooks(resolved_repository),
            "git": uninstall_git_hooks(resolved_repository),
        }
    return {
        "repository": resolved_repository.as_posix(),
        "effect": effect,
        "adapter_id": adapter.adapter_id if adapter is not None else adapter_id,
        "apply": apply,
        "host_hooks": hook_result,
    }


def emit_from_registered_adapter(
    observations: Iterable[Mapping[str, Any]],
    *,
    repository: Path | str,
    adapter_id: str,
    environment: Mapping[str, str] | None = None,
) -> list[dict[str, object]]:
    """Emit from one enabled registered adapter; disabled adapters emit nothing."""

    resolved_repository = resolve_repository(Path(repository))
    selected = _read_registry(resolved_repository).get(_require_identifier(adapter_id, "adapter_id"))
    if selected is None:
        return []
    return emit_triggers(observations, adapter=selected, repository=resolved_repository, environment=environment)


def _hook_payload() -> dict[str, Any]:
    raw = sys.stdin.buffer.read(2 * 1024 * 1024 + 1)
    if len(raw) > 2 * 1024 * 1024:
        raise ToolError("codex-hook-input-too-large", "Codex hook input exceeds 2 MiB")
    try:
        value = json.loads(raw or b"{}")
    except json.JSONDecodeError as error:
        raise ToolError("codex-hook-input-invalid", "Codex hook input is not valid JSON") from error
    return dict(_require_mapping(value, "Codex hook input"))


def _hook_snapshot_path(repository: Path, payload: Mapping[str, Any]) -> Path:
    session_id = _require_string(payload.get("session_id"), "session_id")
    tool_use_id = _require_string(payload.get("tool_use_id"), "tool_use_id")
    key = _sha256({"schema_version": 1, "session_id": session_id, "tool_use_id": tool_use_id})
    return _runtime_directory(repository) / "hook_snapshots" / f"{key}.json"


def _session_baseline_path(repository: Path, payload: Mapping[str, Any]) -> Path:
    session_id = _validate_uuid(payload.get("session_id"), "session_id")
    key = _sha256({"schema_version": 1, "session_id": session_id})
    return _runtime_directory(repository) / "session_baselines" / f"{key}.json"


def _frontier_document(frontier: Mapping[str, FileState]) -> dict[str, dict[str, object]]:
    return {
        path: {
            "path": state.path,
            "sha256": state.sha256,
            "identity": state.identity,
            "line_count": state.line_count,
        }
        for path, state in sorted(frontier.items())
    }


def _frontier_from_document(value: object) -> dict[str, FileState]:
    document = _require_mapping(value, "frontier")
    result: dict[str, FileState] = {}
    for path, raw in document.items():
        state = _require_mapping(raw, f"frontier.{path}")
        if state.get("path") != path:
            raise ToolError("codex-hook-snapshot-invalid", "frontier path identity differs")
        sha256 = _require_string(state.get("sha256"), f"frontier.{path}.sha256")
        identity = _require_string(state.get("identity"), f"frontier.{path}.identity")
        line_count = state.get("line_count")
        if not re.fullmatch(r"[0-9a-f]{64}", sha256) or not isinstance(line_count, int) or line_count < 0:
            raise ToolError("codex-hook-snapshot-invalid", f"frontier state is invalid: {path}")
        result[str(path)] = FileState(str(path), sha256, identity, line_count)
    return result


def _write_session_baseline(
    repository: Path,
    payload: Mapping[str, Any],
    frontier: Mapping[str, FileState],
    *,
    active: bool,
) -> Path:
    path = _session_baseline_path(repository, payload)
    document = {
        "schema_version": 1,
        "session_id": _validate_uuid(payload.get("session_id"), "session_id"),
        "active": active,
        "frontier": _frontier_document(frontier),
    }
    _atomic_write(path, _canonical_json(document) + "\n")
    return path


def _read_session_baseline(path: Path) -> tuple[str, bool, dict[str, FileState]]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ToolError("codex-session-baseline-missing", "Codex session baseline is missing") from error
    except json.JSONDecodeError as error:
        raise ToolError("codex-session-baseline-invalid", f"{path}: invalid JSON") from error
    document = _require_mapping(value, "session baseline")
    if document.get("schema_version") != 1 or not isinstance(document.get("active"), bool):
        raise ToolError("codex-session-baseline-invalid", f"{path}: invalid schema")
    session_id = _validate_uuid(document.get("session_id"), "session_id")
    return session_id, bool(document["active"]), _frontier_from_document(document.get("frontier"))


def _other_active_sessions(repository: Path, current: Path) -> list[str]:
    directory = current.parent
    if not directory.is_dir():
        return []
    result: list[str] = []
    for path in sorted(directory.glob("*.json")):
        if path == current:
            continue
        session_id, active, _ = _read_session_baseline(path)
        if active:
            result.append(session_id)
    return result


def _git_dirty_governed_paths(repository: Path) -> set[str]:
    commands = (
        ["git", "-C", str(repository), "diff", "--name-only", "--no-renames", "-z", "HEAD", "--"],
        ["git", "-C", str(repository), "ls-files", "--others", "--exclude-standard", "-z"],
    )
    result: set[str] = set()
    for command in commands:
        completed = subprocess.run(command, check=False, capture_output=True)
        if completed.returncode != 0:
            raise ToolError("git-status-failed", completed.stderr.decode("utf-8", "replace").strip() or "cannot read governed Git state")
        result.update(
            relative
            for value in completed.stdout.split(b"\0")
            if value
            for relative in (value.decode("utf-8"),)
            if _project_path_eligible(repository, relative)
        )
    return result


def _observation_intersects_paths(observation: Mapping[str, Any], paths: set[str]) -> bool:
    return any(value in paths for value in (observation.get("before_path"), observation.get("after_path")) if isinstance(value, str))


def _hook_log(repository: Path, value: Mapping[str, Any]) -> None:
    path = _runtime_root(repository) / "logs" / "commit_trigger" / f"{dt.date.today().isoformat()}.ndjson"
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o600)
    try:
        payload = (_canonical_json(value) + "\n").encode("utf-8")
        offset = 0
        while offset < len(payload):
            written = os.write(descriptor, payload[offset:])
            if written <= 0:
                raise OSError("could not append Codex hook log")
            offset += written
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _hook_eligible(repository: Path, observation: Mapping[str, Any]) -> bool:
    paths = [observation.get("before_path"), observation.get("after_path")]
    selected = [value for value in paths if isinstance(value, str)]
    return bool(selected) and all(_project_path_eligible(repository, value) for value in selected)


def _import_commit_change_set() -> Any:
    for path in (PACKAGE_ROOT, PACKAGE_ROOT / "COMMIT_CONTEXT", PACKAGE_ROOT / "APPEND_CHANGE_RECORDS", PACKAGE_ROOT / "COMMIT_CHANGE_SET"):
        if str(path) not in sys.path:
            sys.path.insert(0, str(path))
    try:
        import commit_change_set
    except ImportError as error:
        raise ToolError("peer-tool-unavailable", "COMMIT_CHANGE_SET is not importable from the installed runtime") from error
    return commit_change_set


def _commit_hook_observations(
    repository: Path,
    selected: AdapterSpec,
    observations: Sequence[Mapping[str, Any]],
    *,
    session_uuid: str,
) -> list[dict[str, str]]:
    with_session = [
        {**observation, "llm_session": {"app": selected.application, "uuid": session_uuid}}
        for observation in observations
    ]
    triggers = emit_triggers(with_session, adapter=selected, repository=repository, environment={})
    if not triggers:
        return []
    committer = _import_commit_change_set()
    commits: list[dict[str, str]] = []
    for trigger in triggers:
        try:
            result = committer.run(repository, {"trigger": trigger}, apply=True)
        except Exception as error:
            _hook_log(
                repository,
                {
                    "schema_version": 1,
                    "event": "auto_commit_failed",
                    "trigger_id": trigger["trigger_id"],
                    "error_code": str(getattr(error, "code", "unexpected-error")),
                },
            )
            raise ToolError("auto-commit-failed", str(error)) from error
        commits.append({"trigger_id": str(trigger["trigger_id"]), "commit": str(result["commit"])})
    _hook_log(repository, {"schema_version": 1, "event": "auto_commit_completed", "commits": commits})
    return commits


def _run_codex_hook(
    repository: Path | str,
    phase: str,
    adapter_id: str,
    payload: Mapping[str, Any],
    *,
    deadline: float,
    control_generation: int,
) -> dict[str, object]:
    root = resolve_repository(Path(repository))
    cwd = Path(str(payload.get("cwd") or root)).expanduser().resolve()
    if cwd != root and root not in cwd.parents:
        return {"phase": phase, "effect": "outside-repository", "commit_count": 0}
    selected = _read_registry(root).get(_require_identifier(adapter_id, "adapter_id"))
    if selected is None or not selected.enabled:
        return {"phase": phase, "effect": "adapter-not-enabled", "commit_count": 0}
    session_uuid = _validate_uuid(payload.get("session_id"), "session_id")
    baseline_path = _session_baseline_path(root, payload)
    current_frontier = scan_governed_files(
        root,
        deadline=deadline,
        control_generation=control_generation,
    )
    if phase == "start":
        if baseline_path.is_file():
            _, _, baseline = _read_session_baseline(baseline_path)
            _write_session_baseline(root, payload, baseline, active=True)
            effect = "baseline-resumed"
        else:
            _write_session_baseline(root, payload, current_frontier, active=True)
            effect = "baseline-created"
        return {"phase": phase, "effect": effect, "commit_count": 0}
    if phase == "stop":
        if not baseline_path.is_file():
            return {"phase": phase, "effect": "no-session-baseline", "commit_count": 0}
        _, _, previous = _read_session_baseline(baseline_path)
        other_sessions = _other_active_sessions(root, baseline_path)
        if other_sessions:
            return {
                "phase": phase,
                "effect": "ambiguous-session-ownership",
                "commit_count": 0,
                "other_sessions": other_sessions,
            }
        observed_at = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        dirty_paths = _git_dirty_governed_paths(root)
        observations = [
            observation
            for observation in detect_watch_observations(
                previous,
                current_frontier,
                adapter_id=selected.adapter_id,
                repository=root,
                observed_at=observed_at,
                correlations=_read_pipeline_correlations(_runtime_directory(root) / PIPELINE_CORRELATIONS_NAME),
            )
            if _hook_eligible(root, observation) and _observation_intersects_paths(observation, dirty_paths)
        ]
        commits = _commit_hook_observations(root, selected, observations, session_uuid=session_uuid)
        _write_session_baseline(
            root,
            payload,
            scan_governed_files(root, deadline=deadline, control_generation=control_generation),
            active=False,
        )
        return {
            "phase": phase,
            "effect": "reconciled" if commits else "no-eligible-uncommitted-change",
            "commit_count": len(commits),
            "commits": commits,
        }
    if phase not in {"pre", "post"}:
        raise ToolError("codex-hook-phase-invalid", "Codex hook phase must be start, pre, post, or stop")
    snapshot_path = _hook_snapshot_path(root, payload)
    if phase == "pre":
        if not baseline_path.is_file() or not _read_session_baseline(baseline_path)[1]:
            _write_session_baseline(root, payload, current_frontier, active=True)
        snapshot = {
            "schema_version": 1,
            "session_id": _require_string(payload.get("session_id"), "session_id"),
            "tool_use_id": _require_string(payload.get("tool_use_id"), "tool_use_id"),
            "frontier": _frontier_document(current_frontier),
        }
        _atomic_write(snapshot_path, _canonical_json(snapshot) + "\n")
        return {"phase": phase, "effect": "snapshot", "commit_count": 0}
    if not snapshot_path.is_file():
        return {"phase": phase, "effect": "no-pre-snapshot", "commit_count": 0}
    try:
        snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ToolError("codex-hook-snapshot-invalid", "Codex pre-hook snapshot is invalid JSON") from error
    snapshot_path.unlink()
    if not isinstance(snapshot, Mapping) or snapshot.get("schema_version") != 1:
        raise ToolError("codex-hook-snapshot-invalid", "Codex pre-hook snapshot schema is invalid")
    if snapshot.get("session_id") != payload.get("session_id") or snapshot.get("tool_use_id") != payload.get("tool_use_id"):
        raise ToolError("codex-hook-snapshot-mismatch", "Codex pre/post hook identities differ")
    previous = _frontier_from_document(snapshot.get("frontier"))
    observed_at = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    observations = [
        observation
        for observation in detect_watch_observations(
            previous,
            current_frontier,
            adapter_id=selected.adapter_id,
            repository=root,
            observed_at=observed_at,
            correlations=_read_pipeline_correlations(_runtime_directory(root) / PIPELINE_CORRELATIONS_NAME),
        )
        if _hook_eligible(root, observation)
    ]
    commits = _commit_hook_observations(root, selected, observations, session_uuid=session_uuid)
    _write_session_baseline(
        root,
        payload,
        scan_governed_files(root, deadline=deadline, control_generation=control_generation),
        active=True,
    )
    if not commits:
        return {"phase": phase, "effect": "no-eligible-change", "commit_count": 0}
    return {"phase": phase, "effect": "committed", "commit_count": len(commits), "commits": commits}


def codex_hook(repository: Path | str, phase: str, adapter_id: str, payload: Mapping[str, Any]) -> dict[str, object]:
    """Run one fail-open Codex Hook behind the persistent recovery circuit."""

    root = resolve_repository(Path(repository))
    control = _read_hook_control(root)
    if control["mode"] != "running":
        return {
            "phase": phase,
            "effect": "circuit-open",
            "commit_count": 0,
            "control": control,
        }
    generation = int(control["generation"])
    deadline = time.monotonic() + CODEX_HOOK_BUDGET_SECONDS
    completed = threading.Event()

    def trip_on_timeout() -> None:
        if not completed.is_set():
            _trip_hook_control(root, "hook-time-budget-exceeded")

    watchdog = threading.Timer(CODEX_HOOK_BUDGET_SECONDS, trip_on_timeout)
    watchdog.daemon = True
    watchdog.start()
    try:
        return _run_codex_hook(
            root,
            phase,
            adapter_id,
            payload,
            deadline=deadline,
            control_generation=generation,
        )
    except Exception as error:
        code = str(getattr(error, "code", "unexpected-hook-failure"))
        tripped = _trip_hook_control(root, code)
        return {
            "phase": phase,
            "effect": "circuit-tripped",
            "commit_count": 0,
            "diagnostic": {"code": code, "message": str(error)},
            "control": tripped,
        }
    finally:
        completed.set()
        watchdog.cancel()
        watchdog.join()


def _envelope(*, ok: bool, mode: str, result: object | None = None, diagnostic: ToolError | None = None) -> dict[str, object]:
    diagnostics: list[dict[str, str]] = []
    if diagnostic is not None:
        diagnostics.append({"code": diagnostic.code, "message": diagnostic.message})
    payload: dict[str, object] = {
        "schema_version": TOOL_SCHEMA_VERSION,
        "tool": {"capability_id": CAPABILITY_ID, "kind": TOOL_KIND},
        "ok": ok,
        "mode": mode,
        "diagnostics": diagnostics,
    }
    if result is not None:
        payload["result"] = result
    return payload


def _load_observations(path: str) -> list[Mapping[str, Any]]:
    try:
        raw = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        decoded = json.loads(raw)
    except (OSError, json.JSONDecodeError) as error:
        raise ToolError("invalid-input", f"cannot read JSON observations: {error}") from error
    if isinstance(decoded, Mapping) and "observations" in decoded:
        decoded = decoded["observations"]
    if isinstance(decoded, Mapping):
        return [_require_mapping(decoded, "observation")]
    if not isinstance(decoded, list):
        raise ToolError("invalid-input", "observations input must be an object or list")
    return [_require_mapping(item, "observation") for item in decoded]


def _describe() -> dict[str, object]:
    return {
        "capability_id": CAPABILITY_ID,
        "kind": TOOL_KIND,
        "read_only_observe": True,
        "canonical_script": "002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER/commit_trigger.py",
        "input_schema": {
            "observe": {
                "type": "object",
                "required": ["adapter_id", "source_event_id", "observed_at"],
                "properties": {
                    "adapter_id": {"type": "string"},
                    "source_event_id": {"type": "string"},
                    "observed_at": {"type": "string", "format": "date-time"},
                    "before_path": {"type": ["string", "null"]},
                    "after_path": {"type": ["string", "null"]},
                    "llm_session": {
                        "type": "object",
                        "required": ["app", "uuid"],
                        "properties": {"app": {"type": "string"}, "uuid": {"type": "string", "format": "uuid"}},
                    },
                    "pipeline": {
                        "type": "object",
                        "properties": {
                            "owned": {"const": True},
                            "action_id": {"type": "string"},
                            "kind": {"enum": ["journal", "runtime-state"]},
                        },
                    },
                },
            }
        },
        "commands": {
            "describe": {"effects": []},
            "observe": {"input": "JSON object or {observations: [...]}"},
            "watch": {
                "input": "enabled native Codex adapter and polling controls",
                "effects": [],
                "result": "one read-only handoff envelope per detected source boundary",
            },
            "codex-hook": {
                "input": "Codex hook JSON on stdin",
                "effects": ["bounded session baseline", "pre snapshot", "immediate auto-commit", "stop reconciliation", "automatic circuit trip"],
            },
            "control status": {"effects": []},
            "control stop": {"effects": ["Hook circuit state"]},
            "control start": {"effects": ["Hook circuit state"]},
            "control reload": {"effects": ["Hook circuit state", "reconstructible transient cleanup"]},
            "adapter install": {"input": "adapter identity and host session resolver", "effects": ["runtime registry", "Codex Hook registration", "install-owned Git Hook registration"]},
            "adapter status": {"effects": []},
            "adapter enable": {"effects": ["runtime registry"]},
            "adapter disable": {"effects": ["runtime registry"]},
            "adapter uninstall": {"effects": ["runtime registry"]},
        },
        "result_envelope": {"schema_version": TOOL_SCHEMA_VERSION, "diagnostics": "ordered machine-readable diagnostics"},
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", default=".", help="repository root or a path within it")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("describe", help="return machine-readable Tool capability metadata")
    observe = commands.add_parser("observe", help="emit deduplicated trigger handoffs without mutation")
    observe.add_argument("--adapter-id", required=True)
    observe.add_argument("--input", required=True, help="JSON file path or - for stdin")
    watch = commands.add_parser("watch", help="poll native Codex governed source changes without mutation")
    watch.add_argument("--adapter-id", required=True)
    watch.add_argument("--poll-interval", type=float, default=1.0)
    watch.add_argument("--max-events", type=int)
    watch.add_argument("--max-polls", type=int)
    watch.add_argument(
        "--pipeline-correlation-file",
        help="optional NDJSON action/path suppression frontier; default is the Tool runtime path",
    )
    codex = commands.add_parser("codex-hook", help="execute one Codex lifecycle adapter phase")
    codex.add_argument("phase", choices=("start", "pre", "post", "stop"))
    codex.add_argument("--adapter-id", required=True)
    control = commands.add_parser("control", help="operate the Hook recovery circuit without invoking Hook work")
    control_commands = control.add_subparsers(dest="control_command", required=True)
    control_commands.add_parser("status")
    for name in ("stop", "start", "reload"):
        mutation = control_commands.add_parser(name)
        mutation.add_argument("--reason")
        mutation.add_argument("--apply", action="store_true")
    adapter = commands.add_parser("adapter", help="manage explicit host-adapter registration")
    adapter_commands = adapter.add_subparsers(dest="adapter_command", required=True)
    install = adapter_commands.add_parser("install")
    install.add_argument("--adapter-id", required=True)
    install.add_argument("--application", required=True)
    install.add_argument("--host-session-env", required=True)
    install.add_argument("--fallback-session-env")
    install.add_argument("--disabled", action="store_true")
    install.add_argument("--apply", action="store_true")
    adapter_commands.add_parser("status")
    for name in ("enable", "disable", "uninstall"):
        mutation = adapter_commands.add_parser(name)
        mutation.add_argument("--adapter-id", required=True)
        mutation.add_argument("--apply", action="store_true")
    return parser


def cli(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "describe":
            result = _describe()
            mode = "read-only"
        elif args.command == "observe":
            triggers = emit_from_registered_adapter(
                _load_observations(args.input),
                repository=args.repository,
                adapter_id=args.adapter_id,
            )
            result = {
                "handoffs": [
                    {"interface": "COMMIT_CHANGE_SET", "trigger": trigger}
                    for trigger in triggers
                ],
                "trigger_count": len(triggers),
            }
            mode = "read-only"
        elif args.command == "watch":
            if args.max_events is not None and args.max_events < 0:
                raise ToolError("invalid-maximum-events", "max_events must not be negative")
            if args.max_events == 0:
                result = {"handoffs": [], "trigger_count": 0, "stream": "watch", "stopped": "event-limit"}
                mode = "read-only"
                print(_canonical_json(_envelope(ok=True, mode=mode, result=result)))
                return 0
            resolved_repository = resolve_repository(Path(args.repository))
            registered = _read_registry(resolved_repository)
            selected = registered.get(_require_identifier(args.adapter_id, "adapter_id"))
            if selected is None or not selected.enabled:
                # Disabled and uninstalled adapters are intentionally silent.
                result = {"handoffs": [], "trigger_count": 0, "stopped": "adapter-not-enabled"}
                mode = "read-only"
            else:
                emitted = 0
                for triggers in watch_triggers(
                    repository=resolved_repository,
                    adapter=selected,
                    poll_interval=args.poll_interval,
                    maximum_polls=args.max_polls,
                    pipeline_correlation_path=(Path(args.pipeline_correlation_file) if args.pipeline_correlation_file else None),
                ):
                    if not triggers:
                        continue
                    remaining = None if args.max_events is None else args.max_events - emitted
                    selected_triggers = triggers if remaining is None else triggers[:remaining]
                    if not selected_triggers:
                        break
                    emitted += len(selected_triggers)
                    print(
                        _canonical_json(
                            _envelope(
                                ok=True,
                                mode="read-only",
                                result={
                                    "handoffs": [
                                        {"interface": "COMMIT_CHANGE_SET", "trigger": trigger}
                                        for trigger in selected_triggers
                                    ],
                                    "trigger_count": len(selected_triggers),
                                    "stream": "watch",
                                },
                            )
                        ),
                        flush=True,
                    )
                    if args.max_events is not None and emitted >= args.max_events:
                        return 0
                result = {"handoffs": [], "trigger_count": 0, "stream": "watch", "stopped": "poll-limit-or-interrupt"}
                mode = "read-only"
        elif args.command == "codex-hook":
            result = codex_hook(args.repository, args.phase, args.adapter_id, _hook_payload())
            mode = "apply"
        elif args.command == "control":
            result = hook_control(
                args.repository,
                args.control_command,
                apply=bool(getattr(args, "apply", False)),
                reason=getattr(args, "reason", None),
            )
            mode = "apply" if bool(getattr(args, "apply", False)) else "read-only"
        elif args.adapter_command == "status":
            result = adapter_operation(args.repository, "status")
            mode = "read-only"
        elif args.adapter_command == "install":
            spec = AdapterSpec(
                args.adapter_id,
                args.application,
                args.host_session_env,
                args.fallback_session_env,
                not args.disabled,
            )
            result = adapter_operation(
                args.repository,
                "install",
                adapter=spec,
                apply=args.apply,
                manage_host_hooks=True,
            )
            mode = "apply" if args.apply else "dry-run"
        else:
            result = adapter_operation(
                args.repository,
                args.adapter_command,
                adapter_id=args.adapter_id,
                apply=args.apply,
                manage_host_hooks=True,
            )
            mode = "apply" if args.apply else "dry-run"
    except ToolError as error:
        print(_canonical_json(_envelope(ok=False, mode="read-only", diagnostic=error)))
        return 2
    except KeyboardInterrupt:
        print(
            _canonical_json(
                _envelope(
                    ok=True,
                    mode="read-only",
                    result={"handoffs": [], "trigger_count": 0, "stream": "watch", "stopped": "interrupt"},
                )
            )
        )
        return 0
    print(_canonical_json(_envelope(ok=True, mode=mode, result=result)))
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
