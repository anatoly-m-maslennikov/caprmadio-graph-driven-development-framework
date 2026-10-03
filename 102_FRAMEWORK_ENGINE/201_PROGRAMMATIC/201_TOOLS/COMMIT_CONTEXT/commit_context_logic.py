#!/usr/bin/env python3
"""Pure, read-only context gathering for the COMMIT_CONTEXT Finder.

This module deliberately has no command-line entry point.  Both the standalone
Finder and COMMIT_CHANGE_SET import :func:`gather_context` so a Hook trigger is
resolved once, in one way, regardless of which public interface receives it.
"""

from __future__ import annotations

import datetime as dt
import functools
import hashlib
import json
import os
import re
import subprocess
import sys
import tomllib
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Mapping, Sequence
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


MODULE_PATH = Path(__file__).resolve()
PACKAGE_ROOT = MODULE_PATH.parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))
from artifact_metadata import atom_identifier

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
JOURNAL_EVENT_SCHEMA_VERSION = 3
CONTEXT_SCHEMA_VERSION = 3
GITHUB_USERNAME = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?")
APP_NAME = re.compile(r"[a-z][a-z0-9_-]{0,62}")
SHA256 = re.compile(r"[0-9a-f]{64}")


class ContextError(RuntimeError):
    """One stable, machine-readable rejection from the Finder."""

    def __init__(self, code: str, message: str, **details: Any) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details

    def diagnostic(self) -> dict[str, Any]:
        result: dict[str, Any] = {"code": self.code, "message": self.message}
        if self.details:
            result["details"] = self.details
        return result


@dataclass(frozen=True)
class Carrier:
    """A parsed governed carrier from one selected source frontier."""

    path: str
    filename: str
    identity: str
    version: int
    sha256: str
    relations: dict[str, tuple[str, ...]]
    lifecycle: str
    structural_scope: str
    body: bytes
    kind: str = "file"
    declared_version: bool = True
    entries: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class RepositoryPaths:
    """Configured durable and local roots for one governed Project."""

    control_root: Path
    framework_root: Path
    journal_root: Path
    runtime_root: Path
    temporary_root: Path
    legacy_migration_roots: tuple[Path, ...]

    @property
    def governed_roots(self) -> tuple[Path, ...]:
        return (self.framework_root, self.control_root)


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def digest(value: Any) -> str:
    payload = value if isinstance(value, bytes) else canonical_json(value)
    return hashlib.sha256(payload).hexdigest()


def repository_root(root: Path) -> Path:
    candidate = root.expanduser().resolve()
    if not (candidate / SETTINGS_PATH).is_file():
        raise ContextError("repository_root_invalid", "repository has no configured CAPRMEDIO Project settings", root=str(candidate))
    if not (candidate / ".git").exists():
        raise ContextError("repository_git_missing", "repository has no Git metadata", root=str(candidate))
    paths = configured_repository_paths(candidate)
    if not (candidate / paths.control_root).is_dir():
        raise ContextError(
            "repository_root_invalid",
            "repository has no configured CAPRMEDIO Project carrier root",
            root=str(candidate),
            control_root=paths.control_root.as_posix(),
        )
    return candidate


def repository_identity(root: Path) -> str:
    """Return the same stable repository identity sealed by COMMIT_TRIGGER."""

    root = root.expanduser().resolve()
    git_directory = git_text(root, ["rev-parse", "--git-dir"])
    assert git_directory is not None
    resolved_git = (root / git_directory).resolve()
    return digest({"repository_root": root.as_posix(), "git_directory": resolved_git.as_posix()})


def git(root: Path, arguments: Sequence[str], *, allow_failure: bool = False) -> bytes | None:
    completed = subprocess.run(
        ["git", "-C", str(root), *arguments],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode == 0:
        return completed.stdout
    if allow_failure:
        return None
    raise ContextError(
        "git_read_failed",
        "Git read failed while gathering commit context",
        command=list(arguments),
        stderr=completed.stderr.decode("utf-8", errors="replace").strip(),
    )


def git_text(root: Path, arguments: Sequence[str], *, allow_failure: bool = False) -> str | None:
    payload = git(root, arguments, allow_failure=allow_failure)
    return None if payload is None else payload.decode("utf-8", errors="strict").strip()


def _git_batch_blobs(root: Path, object_names: Sequence[str]) -> dict[str, bytes | None]:
    """Read many Git blobs through one cat-file process."""

    if not object_names:
        return {}
    completed = subprocess.run(
        ["git", "-C", str(root), "cat-file", "--batch"],
        input="".join(f"{name}\n" for name in object_names).encode("utf-8"),
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        raise ContextError(
            "git_read_failed",
            "Git batch read failed while gathering commit context",
            command=["cat-file", "--batch"],
            stderr=completed.stderr.decode("utf-8", errors="replace").strip(),
        )
    payload = completed.stdout
    cursor = 0
    result: dict[str, bytes | None] = {}
    for name in object_names:
        boundary = payload.find(b"\n", cursor)
        if boundary < 0:
            raise ContextError("git_read_failed", "Git batch read returned a truncated object header")
        header = payload[cursor:boundary]
        cursor = boundary + 1
        if header.endswith(b" missing"):
            result[name] = None
            continue
        fields = header.rsplit(b" ", 2)
        if len(fields) != 3 or fields[1] != b"blob" or not fields[2].isdigit():
            raise ContextError(
                "git_read_failed",
                "Git batch read returned an unexpected object header",
                header=header.decode("utf-8", errors="replace"),
            )
        size = int(fields[2])
        end = cursor + size
        if end >= len(payload) or payload[end : end + 1] != b"\n":
            raise ContextError("git_read_failed", "Git batch read returned truncated object content")
        result[name] = payload[cursor:end]
        cursor = end + 1
    return result


def relative_path(value: Any, *, name: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        raise ContextError("trigger_path_invalid", f"{name} must be a non-empty repository-relative path or null")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path.as_posix() in {".", ""}:
        raise ContextError("trigger_path_invalid", f"{name} is not a safe repository-relative path", path=value)
    return path.as_posix()


def required_mapping(value: Any, *, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ContextError("trigger_field_invalid", f"{name} must be an object")
    return value


def required_string(value: Any, *, name: str) -> str:
    if not isinstance(value, str) or not value:
        raise ContextError("trigger_field_invalid", f"{name} must be a non-empty string")
    return value


def parse_uuid(value: Any, *, name: str) -> str:
    text = required_string(value, name=name)
    # UUID formatting is intentionally checked without importing a provider SDK.
    if not re.fullmatch(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", text):
        raise ContextError("llm_session_uuid_invalid", f"{name} must be a canonical UUID", value=text)
    return text.lower()


def parse_instant(value: Any, *, name: str) -> dt.datetime:
    text = required_string(value, name=name)
    normalized = text[:-1] + "+00:00" if text.endswith("Z") else text
    try:
        moment = dt.datetime.fromisoformat(normalized)
    except ValueError as error:
        raise ContextError("occurred_at_invalid", f"{name} must be an ISO-8601 timestamp", value=text) from error
    if moment.tzinfo is None or moment.utcoffset() is None:
        raise ContextError("occurred_at_timezone_missing", f"{name} must be timezone-qualified", value=text)
    return moment


def format_instant(moment: dt.datetime) -> str:
    rendered = moment.isoformat(timespec="seconds")
    return rendered[:-6] + "Z" if rendered.endswith("+00:00") else rendered


def configured_timezone(root: Path) -> tuple[str, dt.tzinfo]:
    try:
        settings = tomllib.loads((root / SETTINGS_PATH).read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ContextError("project_settings_missing", "project settings are required for context gathering") from error
    except tomllib.TOMLDecodeError as error:
        raise ContextError("project_settings_invalid", "project settings are not valid TOML") from error
    name = settings.get("artifact_timestamps", {}).get("timezone", "local")
    if not isinstance(name, str) or not name:
        raise ContextError("timezone_invalid", "artifact timestamp timezone must be a non-empty string")
    if name == "local":
        local = dt.datetime.now().astimezone().tzinfo
        assert local is not None
        return name, local
    if name == "UTC":
        return name, dt.UTC
    try:
        return name, ZoneInfo(name)
    except ZoneInfoNotFoundError as error:
        raise ContextError("timezone_invalid", "configured artifact timestamp timezone is unknown", timezone=name) from error


def _configured_relative_path(paths: Mapping[str, Any], key: str, default: str) -> Path:
    value = paths.get(key, default)
    if not isinstance(value, str) or not value:
        raise ContextError("project_paths_invalid", f"{key} must be a non-empty string")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path.as_posix() in {"", "."}:
        raise ContextError("project_paths_invalid", f"{key} must be repository-relative", value=value)
    return path


@functools.cache
def configured_repository_paths(root: Path) -> RepositoryPaths:
    try:
        settings = tomllib.loads((root / SETTINGS_PATH).read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ContextError("project_settings_missing", "project settings are required for path resolution") from error
    except tomllib.TOMLDecodeError as error:
        raise ContextError("project_settings_invalid", "project settings are not valid TOML") from error
    paths = settings.get("paths", {})
    if not isinstance(paths, Mapping):
        raise ContextError("project_paths_invalid", "paths must be a TOML table")
    control = _configured_relative_path(paths, "control_root", ".caprmedio_caprmedio")
    framework = _configured_relative_path(paths, "framework_root", ".caprmedio_framework")
    journal = _configured_relative_path(paths, "journal_root", ".caprmedio_caprmedio/work_journal")
    runtime = _configured_relative_path(paths, "runtime_root", ".caprmedio_runtime")
    temporary = _configured_relative_path(paths, "temporary_root", ".caprmedio_tmp")
    if control != SETTINGS_PATH.parent:
        raise ContextError("project_paths_invalid", "control_root must own the Project settings Carrier", value=control.as_posix())
    if journal.parts[: len(control.parts)] != control.parts or journal == control:
        raise ContextError("project_paths_invalid", "journal_root must be a descendant of control_root", value=journal.as_posix())
    legacy_raw = paths.get("legacy_migration_roots", [".caprmedio"])
    if not isinstance(legacy_raw, list) or not all(isinstance(value, str) for value in legacy_raw):
        raise ContextError("project_paths_invalid", "legacy_migration_roots must be an array of strings")
    legacy = tuple(_configured_relative_path({"value": value}, "value", value) for value in legacy_raw)
    roots = (control, framework, runtime, temporary, *legacy)
    if len({path.as_posix() for path in roots}) != len(roots):
        raise ContextError("project_paths_invalid", "configured roots must be distinct")
    return RepositoryPaths(control, framework, journal, runtime, temporary, legacy)


def configured_paths(root: Path) -> tuple[Path, Path]:
    paths = configured_repository_paths(root)
    return paths.journal_root, paths.runtime_root


def _path_is_within(path: Path, root: Path) -> bool:
    return path == root or path.parts[: len(root.parts)] == root.parts


def is_journal_path(root: Path, path: str, *, require_carrier: bool = False) -> bool:
    candidate = Path(path)
    if candidate.is_absolute() or not candidate.parts or ".." in candidate.parts:
        return False
    journal = configured_repository_paths(root).journal_root
    return _path_is_within(candidate, journal) and (not require_carrier or candidate.suffix == ".ndjson")


def is_forbidden_commit_path(root: Path, path: str) -> bool:
    candidate = Path(path)
    if candidate.is_absolute() or not candidate.parts or ".." in candidate.parts:
        return True
    configured = configured_repository_paths(root)
    return any(_path_is_within(candidate, forbidden) for forbidden in (configured.runtime_root, configured.temporary_root))


def split_frontmatter(data: bytes, *, path: str) -> str:
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ContextError("carrier_encoding_invalid", "governed Markdown carrier must be UTF-8", path=path) from error
    if not text.startswith("---\n"):
        raise ContextError("carrier_frontmatter_missing", "governed Markdown carrier requires YAML frontmatter", path=path)
    boundary = text.find("\n---\n", 4)
    if boundary < 0:
        raise ContextError("carrier_frontmatter_invalid", "governed Markdown carrier frontmatter is unterminated", path=path)
    return text[4:boundary]


def yaml_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_relations(frontmatter: str, *, path: str) -> dict[str, tuple[str, ...]]:
    lines = frontmatter.splitlines()
    try:
        start = next(index for index, line in enumerate(lines) if line == "relations:")
    except StopIteration:
        return {}
    relations: dict[str, list[str]] = {}
    current: str | None = None
    for line in lines[start + 1 :]:
        if line and not line.startswith((" ", "\t")):
            break
        match = re.fullmatch(r"  ([a-z][a-z0-9_]*):\s*", line)
        if match:
            current = match.group(1)
            if current in relations:
                raise ContextError("relations_invalid", "duplicate relation kind in carrier", path=path, relation_type=current)
            relations[current] = []
            continue
        match = re.fullmatch(r"    -\s+(.+?)\s*", line)
        if match and current is not None:
            target = yaml_scalar(match.group(1))
            if not target:
                raise ContextError("relations_invalid", "relation endpoint is empty", path=path, relation_type=current)
            relations[current].append(target)
            continue
        if line.strip():
            raise ContextError("relations_invalid", "relation frontmatter must use canonical YAML lists", path=path, line=line)
    return {kind: tuple(values) for kind, values in relations.items()}


def frontmatter_scalar(frontmatter: str, key: str) -> str | None:
    matches = re.findall(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", frontmatter)
    if len(matches) > 1:
        raise ContextError("carrier_frontmatter_invalid", "duplicate frontmatter scalar", property=key)
    return yaml_scalar(matches[0]) if matches else None


def derive_identity(filename: str, frontmatter: str) -> str:
    return atom_identifier(filename, frontmatter_scalar(frontmatter, "atom_id"))


def carrier_from_bytes(path: str, data: bytes) -> Carrier:
    if not path.endswith(".md"):
        raise ContextError("carrier_kind_invalid", "COMMIT_CONTEXT currently accepts governed Markdown carriers", path=path)
    frontmatter = split_frontmatter(data, path=path)
    raw_version = frontmatter_scalar(frontmatter, "version")
    if raw_version is None or not raw_version.isdecimal() or int(raw_version) < 1:
        raise ContextError("carrier_version_invalid", "governed Markdown carrier requires a positive version", path=path)
    relative = Path(path)
    return Carrier(
        path=relative.as_posix(),
        filename=relative.name,
        identity=derive_identity(relative.name, frontmatter),
        version=int(raw_version),
        sha256=digest(data),
        relations=parse_relations(frontmatter, path=path),
        lifecycle="archived" if "archive" in relative.parts else "active",
        structural_scope=relative.parent.as_posix(),
        body=data,
    )


def _git_ignores(root: Path, path: str) -> bool:
    completed = subprocess.run(
        ["git", "-C", str(root), "check-ignore", "--no-index", "-q", "--", path],
        check=False,
        capture_output=True,
    )
    if completed.returncode in {0, 1}:
        return completed.returncode == 0
    raise ContextError(
        "git_ignore_check_failed",
        "Git ignore rules could not be evaluated",
        path=path,
        stderr=completed.stderr.decode("utf-8", "replace").strip(),
    )


def _git_ignored_paths(root: Path, paths: Sequence[str]) -> set[str]:
    if not paths:
        return set()
    completed = subprocess.run(
        ["git", "-C", str(root), "check-ignore", "--no-index", "-z", "--stdin"],
        input=b"".join(path.encode("utf-8") + b"\0" for path in paths),
        check=False,
        capture_output=True,
    )
    if completed.returncode not in {0, 1}:
        raise ContextError(
            "git_ignore_check_failed",
            "Git ignore rules could not be evaluated",
            stderr=completed.stderr.decode("utf-8", "replace").strip(),
        )
    return {value.decode("utf-8") for value in completed.stdout.split(b"\0") if value}


def _project_path_allowed_before_ignore(root: Path, path: str) -> bool:
    candidate = Path(path)
    if candidate.is_absolute() or not candidate.parts or ".." in candidate.parts:
        return False
    configured = configured_repository_paths(root)
    if is_journal_path(root, path) or is_forbidden_commit_path(root, path):
        return False
    if candidate.parts[0].startswith(".") and len(candidate.parts) > 1:
        admitted = (*configured.governed_roots, *configured.legacy_migration_roots)
        if not any(_path_is_within(candidate, root_path) for root_path in admitted):
            return False
    return True


def project_path_eligible(root: Path, path: str) -> bool:
    return _project_path_allowed_before_ignore(root, path) and not _git_ignores(root, path)


def project_paths_eligible(root: Path, paths: Sequence[str]) -> set[str]:
    candidates = [path for path in paths if _project_path_allowed_before_ignore(root, path)]
    return set(candidates).difference(_git_ignored_paths(root, candidates))


def _git_revision(root: Path, path: str) -> int:
    payload = git(root, ["log", "--follow", "--format=%H", "HEAD", "--", path], allow_failure=True) or b""
    return max(1, len([line for line in payload.splitlines() if line]))


def project_file_carrier(root: Path, path: str, data: bytes, *, committed: bool) -> Carrier:
    try:
        return carrier_from_bytes(path, data)
    except ContextError:
        relative = Path(path)
        return Carrier(
            path=relative.as_posix(),
            filename=relative.name,
            identity=f"file:{relative.as_posix()}",
            version=_git_revision(root, path) if committed else 1,
            sha256=digest(data),
            relations={},
            lifecycle="active",
            structural_scope=relative.parent.as_posix(),
            body=data,
            kind="file",
            declared_version=False,
        )


def _entry_rows(root: Path, folder: str, *, committed: bool) -> tuple[tuple[str, str], ...]:
    if committed:
        payload = git(root, ["ls-tree", "-r", "-z", "--name-only", "HEAD", "--", folder]) or b""
        paths = [value.decode("utf-8") for value in payload.split(b"\0") if value]
    else:
        payload = git(root, ["ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", folder]) or b""
        paths = [value.decode("utf-8") for value in payload.split(b"\0") if value]
    prefix = folder.rstrip("/") + "/"
    candidates = [
        path
        for path in sorted(paths)
        if path.startswith(prefix) and _project_path_allowed_before_ignore(root, path)
    ]
    candidates = sorted(project_paths_eligible(root, candidates))
    committed_blobs = _git_batch_blobs(root, [f"HEAD:{path}" for path in candidates]) if committed else {}
    rows: list[tuple[str, str]] = []
    for path in candidates:
        if committed:
            data = committed_blobs[f"HEAD:{path}"]
        else:
            data = state_blob(root, path, "working")
        if data is not None:
            rows.append((path, digest(data)))
    return tuple(rows)


def folder_carrier(root: Path, path: str, *, committed: bool) -> Carrier | None:
    entries = _entry_rows(root, path, committed=committed)
    if not entries:
        return None
    relative = Path(path)
    body = canonical_json(
        [
            {"path": Path(entry).relative_to(relative).as_posix(), "sha256": sha256}
            for entry, sha256 in entries
        ]
    )
    return Carrier(
        path=relative.as_posix(),
        filename=relative.name,
        identity=f"folder:{relative.as_posix()}",
        version=_git_revision(root, path) if committed else 1,
        sha256=digest(body),
        relations={},
        lifecycle="active",
        structural_scope=relative.parent.as_posix(),
        body=body,
        kind="folder",
        declared_version=False,
        entries=entries,
    )


def committed_folder_exists(root: Path, path: str) -> bool:
    return bool(_entry_rows(root, path, committed=True))


def committed_object_kind(root: Path, path: str) -> str | None:
    payload = git(root, ["cat-file", "-t", f"HEAD:{path}"], allow_failure=True)
    if payload is None:
        return None
    value = payload.decode("utf-8").strip()
    return value or None


def registry_path(root: Path) -> Path:
    del root
    return PACKAGE_ROOT / "caprmedio_relation_types.toml"


def relation_registry(root: Path) -> dict[str, Mapping[str, Any]]:
    path = registry_path(root)
    try:
        registry = tomllib.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ContextError("relation_registry_missing", "canonical relation registry is missing", path=str(path)) from error
    except tomllib.TOMLDecodeError as error:
        raise ContextError("relation_registry_invalid", "canonical relation registry is invalid TOML", path=str(path)) from error
    rows = registry.get("relation_types")
    if not isinstance(rows, list):
        raise ContextError("relation_registry_invalid", "relation registry requires relation_types rows", path=str(path))
    required = {
        "direct_name",
        "inverse_name",
        "declaration_carrier",
        "source_lifecycles",
        "target_lifecycles",
        "owner",
        "direct_direction",
        "upstream_endpoint",
        "source_classes",
        "target_classes",
        "cardinality",
        "authority_effect",
        "transitive",
        "symmetric",
        "authority_modes",
        "status",
        "exclusive_meaning",
    }
    by_direct: dict[str, Mapping[str, Any]] = {}
    inverses: set[str] = set()
    for row in rows:
        if not isinstance(row, Mapping):
            raise ContextError("relation_registry_invalid", "relation registry row must be an object", path=str(path))
        missing = sorted(required.difference(row))
        if missing:
            raise ContextError("relation_registry_incomplete", "relation registry row has missing fields", path=str(path), missing=missing)
        direct = row["direct_name"]
        inverse = row["inverse_name"]
        if not isinstance(direct, str) or not isinstance(inverse, str) or not direct or not inverse:
            raise ContextError("relation_registry_invalid", "relation names must be non-empty strings", path=str(path))
        declaration_carrier = row["declaration_carrier"]
        if not isinstance(declaration_carrier, str) or declaration_carrier not in {"atom_carrier", "work_journal_event"}:
            raise ContextError(
                "relation_registry_invalid",
                "relation declaration carrier is invalid",
                path=str(path),
                relation_type=direct,
                declaration_carrier=declaration_carrier,
            )
        if direct in by_direct or inverse in inverses:
            raise ContextError("relation_registry_ambiguous", "relation registry has duplicate direct or inverse names", relation_type=direct)
        by_direct[direct] = row
        inverses.add(inverse)
    overlap = sorted(set(by_direct).intersection(inverses))
    if overlap:
        raise ContextError("relation_registry_ambiguous", "an inverse relation name is authored as direct", relation_types=overlap)
    return by_direct


def is_active_path(path: str) -> bool:
    parts = Path(path).parts
    return path.endswith(".md") and "archive" not in parts and "drafts" not in parts


def working_graph(root: Path, *, override_path: str | None = None, override: bytes | None = None) -> dict[str, Carrier]:
    graph: dict[str, Carrier] = {}
    ambiguous: set[str] = set()
    configured = configured_repository_paths(root)
    paths = sorted(path for governed in configured.governed_roots for path in (root / governed).rglob("*.md"))
    for path in paths:
        relative = path.relative_to(root).as_posix()
        if not is_active_path(relative):
            continue
        data = override if override_path == relative and override is not None else path.read_bytes()
        # A Markdown carrier is not an Atom merely because it lives below the
        # control root.  Current Atoms use canonical YAML frontmatter; legacy
        # TOML-frontmatter packets and narrative Markdown remain outside the
        # authority graph and are handled by repository validators instead.
        if not data.startswith((b"---\n", b"---\r\n")):
            continue
        boundary = data.find(b"\n---\n", 4)
        if boundary >= 0 and re.search(rb"(?m)^projection:\s*$", data[4:boundary]):
            continue
        try:
            carrier = carrier_from_bytes(relative, data)
        except ContextError:
            # Context gathering validates its selected subject strictly.  An
            # unrelated malformed candidate is not authority for that subject
            # and remains the responsibility of repository-wide validators.
            continue
        for key in {carrier.identity, carrier.filename, carrier.filename.removesuffix(".md")}:
            if key in ambiguous:
                continue
            if key in graph and graph[key].path != carrier.path:
                graph.pop(key)
                ambiguous.add(key)
                continue
            graph[key] = carrier
    return graph


def committed_graph(root: Path) -> dict[str, Carrier]:
    configured = configured_repository_paths(root)
    payload = git(
        root,
        ["ls-tree", "-r", "-z", "--name-only", "HEAD", "--", *(path.as_posix() for path in configured.governed_roots)],
    )
    assert payload is not None
    graph: dict[str, Carrier] = {}
    ambiguous: set[str] = set()
    for raw_path in payload.split(b"\0"):
        if not raw_path:
            continue
        relative = raw_path.decode("utf-8")
        if not is_active_path(relative):
            continue
        data = git(root, ["show", f"HEAD:{relative}"])
        assert data is not None
        if not data.startswith((b"---\n", b"---\r\n")):
            continue
        boundary = data.find(b"\n---\n", 4)
        if boundary >= 0 and re.search(rb"(?m)^projection:\s*$", data[4:boundary]):
            continue
        try:
            carrier = carrier_from_bytes(relative, data)
        except ContextError:
            continue
        for key in {carrier.identity, carrier.filename, carrier.filename.removesuffix(".md")}:
            if key in ambiguous:
                continue
            if key in graph and graph[key].path != carrier.path:
                graph.pop(key)
                ambiguous.add(key)
                continue
            graph[key] = carrier
    return graph


def state_blob(root: Path, path: str | None, state: str) -> bytes | None:
    if path is None:
        return None
    if state == "committed":
        return git(root, ["show", f"HEAD:{path}"], allow_failure=True)
    if state == "staged":
        return git(root, ["show", f":{path}"], allow_failure=True)
    if state == "working":
        absolute = root / path
        if absolute.is_symlink():
            return os.readlink(absolute).encode("utf-8")
        return absolute.read_bytes() if absolute.is_file() else None
    raise AssertionError(f"unknown carrier state: {state}")


def staged_or_working_result(root: Path, path: str) -> tuple[bytes | None, str]:
    working = state_blob(root, path, "working")
    staged = state_blob(root, path, "staged")
    if working is None:
        return (None, "removed")
    changed_from_index = git(root, ["diff", "--quiet", "--", path], allow_failure=True) is None
    if changed_from_index or staged is None:
        return (working, "working")
    return (staged, "staged")


def validate_trigger(root: Path, trigger: Mapping[str, Any]) -> dict[str, Any]:
    if trigger.get("schema_version") != 1:
        raise ContextError("trigger_schema_invalid", "COMMIT_CONTEXT requires a schema-version 1 COMMIT_TRIGGER")
    trigger_id = required_string(trigger.get("trigger_id"), name="trigger_id")
    if not SHA256.fullmatch(trigger_id):
        raise ContextError("trigger_id_invalid", "trigger_id must be a SHA-256 hex digest")
    adapter = required_mapping(trigger.get("adapter"), name="adapter")
    adapter_id = required_string(adapter.get("id"), name="adapter.id")
    source_event_id = required_string(trigger.get("source_event_id"), name="source_event_id")
    repository = required_mapping(trigger.get("repository"), name="repository")
    reported_root = required_string(repository.get("root"), name="repository.root")
    if Path(reported_root).expanduser().resolve() != root:
        raise ContextError("trigger_repository_mismatch", "trigger repository.root does not match the selected repository", trigger_root=reported_root, root=str(root))
    identity = required_string(repository.get("identity"), name="repository.identity")
    if not SHA256.fullmatch(identity):
        raise ContextError("repository_identity_invalid", "repository.identity must be a SHA-256 hex digest")
    actual_identity = repository_identity(root)
    if identity != actual_identity:
        raise ContextError(
            "trigger_repository_identity_mismatch",
            "trigger repository.identity does not identify the selected repository",
        )
    expected_trigger_id = digest(
        {
            "schema_version": 1,
            "adapter_id": adapter_id,
            "source_event_id": source_event_id,
            "repository_id": identity,
        }
    )
    if trigger_id != expected_trigger_id:
        raise ContextError("trigger_id_mismatch", "trigger_id does not match its sealed identity fields")
    observed_at = parse_instant(trigger.get("observed_at"), name="observed_at")
    session = required_mapping(trigger.get("llm_session"), name="llm_session")
    app = required_string(session.get("app"), name="llm_session.app").lower()
    if not APP_NAME.fullmatch(app):
        raise ContextError("llm_session_app_invalid", "llm_session.app is not canonical", app=app)
    return {
        "trigger_id": trigger_id,
        "adapter": {"id": adapter_id},
        "source_event_id": source_event_id,
        "repository": {"root": str(root), "identity": identity},
        "observed_at": format_instant(observed_at),
        "before_path": relative_path(trigger.get("before_path"), name="before_path"),
        "after_path": relative_path(trigger.get("after_path"), name="after_path"),
        "llm_session": {"app": app, "uuid": parse_uuid(session.get("uuid"), name="llm_session.uuid")},
        "author": trigger.get("author"),
    }


def resolve_author(root: Path, trigger: Mapping[str, Any], environment: Mapping[str, str] | None) -> str:
    explicit = trigger.get("author")
    if explicit is not None:
        author = required_string(explicit, name="author")
    else:
        env = os.environ if environment is None else environment
        candidates = [env.get(name) for name in ("CAPRMEDIO_GITHUB_USERNAME", "GITHUB_ACTOR", "GITHUB_USER")]
        configured = git_text(root, ["config", "--get", "github.username"], allow_failure=True)
        candidates.append(configured)
        values = sorted({candidate for candidate in candidates if candidate})
        if len(values) != 1:
            raise ContextError("journal_author_unresolved", "current full GitHub username cannot be resolved unambiguously", candidates=values)
        author = values[0]
    if not GITHUB_USERNAME.fullmatch(author):
        raise ContextError("journal_author_invalid", "author must be a full GitHub username", author=author)
    return author


def resolve_relations(
    source: Carrier,
    graph: Mapping[str, Carrier],
    registry: Mapping[str, Mapping[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    detailed: list[dict[str, Any]] = []
    diagnostics: list[dict[str, Any]] = []
    for relation_type, raw_targets in source.relations.items():
        row = registry.get(relation_type)
        if row is None:
            diagnostics.append(
                ContextError(
                    "relation_kind_unresolved",
                    "logger preserved the file change without resolving an unknown relation kind",
                    relation_type=relation_type,
                    path=source.path,
                ).diagnostic()
            )
        elif row["declaration_carrier"] != "atom_carrier":
            diagnostics.append(
                ContextError(
                    "relation_declaration_carrier_not_atom",
                    "logger did not read a Journal-declared relation from Atom frontmatter",
                    relation_type=relation_type,
                    path=source.path,
                    declaration_carrier=row["declaration_carrier"],
                ).diagnostic()
            )
            continue
        elif row["status"] != "active" or source.lifecycle not in row["source_lifecycles"]:
            diagnostics.append(
                ContextError(
                    "relation_rule_not_applicable",
                    "logger did not enforce the relation registry while recording the file change",
                    relation_type=relation_type,
                    path=source.path,
                ).diagnostic()
            )
        for raw_target in raw_targets:
            key = raw_target.removesuffix(".md")
            if "@" in key:
                key, stated_version = key.rsplit("@", 1)
            else:
                stated_version = None
            target = graph.get(key) or graph.get(Path(key).name) or graph.get(Path(key).name.removesuffix(".md"))
            if target is None:
                diagnostics.append(
                    ContextError(
                        "relation_target_unresolved",
                        "logger preserved the file change without resolving a missing or ambiguous relation target",
                        relation_type=relation_type,
                        target=raw_target,
                    ).diagnostic()
                )
                continue
            if row is not None and target.lifecycle not in row["target_lifecycles"]:
                diagnostics.append(
                    ContextError(
                        "relation_target_rule_not_applicable",
                        "logger did not enforce target lifecycle eligibility while recording the file change",
                        relation_type=relation_type,
                        target=target.filename,
                    ).diagnostic()
                )
            if stated_version is not None and (not stated_version.isdecimal() or int(stated_version) != target.version):
                diagnostics.append(
                    ContextError(
                        "relation_target_version_differs",
                        "logger used the observable target version without rejecting the file change",
                        relation_type=relation_type,
                        target=target.filename,
                        stated_version=stated_version,
                        observed_version=target.version,
                    ).diagnostic()
                )
            detailed.append(
                {
                    "relation_type": relation_type,
                    "filename": target.filename,
                    "version": target.version,
                    "path": target.path,
                    "sha256": target.sha256,
                    "registry": (
                        {
                            "direct_direction": row["direct_direction"],
                            "upstream_endpoint": row["upstream_endpoint"],
                            "inverse_name": row["inverse_name"],
                            "declaration_carrier": row["declaration_carrier"],
                        }
                        if row is not None
                        else {}
                    ),
                }
            )
    detailed.sort(key=lambda value: (value["relation_type"], value["filename"], value["version"]))
    unique: list[dict[str, Any]] = []
    seen: set[tuple[str, str, int]] = set()
    for value in detailed:
        key = (value["relation_type"], value["filename"], value["version"])
        if key in seen:
            diagnostics.append(
                ContextError(
                    "relation_target_duplicate_ignored",
                    "logger ignored one duplicate relation target while recording the file change",
                    relation_type=value["relation_type"],
                    target=value["filename"],
                ).diagnostic()
            )
            continue
        seen.add(key)
        unique.append(value)
    detailed = unique
    sources = [{key: relation[key] for key in ("relation_type", "filename", "version")} for relation in detailed]
    return detailed, sources, diagnostics


def scan_prior_events(root: Path, journal_relative: Path, before: Carrier | None) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    if before is None:
        return None, None
    payload = git(root, ["ls-tree", "-r", "-z", "--name-only", "HEAD", "--", journal_relative.as_posix()]) or b""
    carrier_paths = [value.decode("utf-8") for value in payload.split(b"\0") if value and value.endswith(b".ndjson")]
    candidates: list[tuple[str, int, dict[str, Any]]] = []
    for carrier_relative in sorted(carrier_paths):
        carrier_data = state_blob(root, carrier_relative, "committed")
        if carrier_data is None:
            continue
        for line_number, line in enumerate(carrier_data.decode("utf-8").splitlines(), 1):
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise ContextError("journal_syntax_invalid", "Journal contains invalid JSON while resolving prior state", path=carrier_relative, line=line_number) from error
            if record.get("schema_version") not in {2, JOURNAL_EVENT_SCHEMA_VERSION}:
                continue
            if record.get("event") not in {"completed", "recovered"}:
                continue
            sealed_digest = record.get("event_digest")
            unsigned = dict(record)
            unsigned.pop("event_digest", None)
            if not isinstance(sealed_digest, str) or not SHA256.fullmatch(sealed_digest) or digest(unsigned) != sealed_digest:
                raise ContextError(
                    "journal_event_digest_invalid",
                    "Journal event digest is invalid while resolving prior state",
                    path=carrier_relative,
                    line=line_number,
                )
            result = record.get("result")
            observed = present_result(before)
            if not isinstance(result, Mapping) or any(result.get(key) != value for key, value in observed.items() if key != "version"):
                continue
            event_id = record.get("event_id")
            if not isinstance(event_id, str):
                continue
            candidates.append((str(record.get("occurred_at", "")), line_number, record))
    if not candidates:
        return None, None
    candidates.sort(key=lambda item: (item[0], item[1], str(item[2].get("event_id"))))
    record = candidates[-1][2]
    result = record["result"]
    assert isinstance(result, Mapping)
    return record, dict(result)


def recovery_candidate(
    *,
    action_id: str,
    before: Carrier | None,
    git_base: Mapping[str, str],
    author: str,
    occurred_at: str,
    llm_session: Mapping[str, str],
    structural_scope: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    if before is None:
        raise ContextError("recovery_insufficient", "a non-ADD change has no recoverable preceding carrier")
    result = present_result(before)
    evidence = {
        "git": {"base_commit": git_base["commit"], "path": before.path, "sha256": before.sha256},
        "carrier": {
            "identity": before.identity,
            "kind": before.kind,
            "filename": before.filename,
            "version": before.version,
            "sha256": before.sha256,
        },
    }
    evidence_digest = digest(evidence)
    event_id = digest({"schema_version": JOURNAL_EVENT_SCHEMA_VERSION, "action_id": action_id, "event": "recovered", "kind": "governed_project_state", "subject_kind": before.kind, "result": result, "evidence_digest": evidence_digest})
    recovery = {
        "event_id": event_id,
        "result": result,
        "evidence": evidence,
        "evidence_digest": evidence_digest,
        "contradictions": [],
    }
    record_unsigned = {
        "schema_version": JOURNAL_EVENT_SCHEMA_VERSION,
        "event_id": event_id,
        "action_id": action_id,
        "event": "recovered",
        "kind": "governed_project_state",
        "subject_kind": before.kind,
        "author": author,
        "occurred_at": occurred_at,
        "llm_session": dict(llm_session),
        "structural_scope": structural_scope,
        "result": result,
        "recovery_evidence": evidence,
    }
    record = {**record_unsigned, "event_digest": digest(record_unsigned)}
    return recovery, record


def present_result(carrier: Carrier) -> dict[str, Any]:
    result: dict[str, Any] = {
        "state": "present",
        "filename": carrier.filename,
        "version": carrier.version,
        "path": carrier.path,
        "sha256": carrier.sha256,
    }
    if carrier.kind == "folder":
        result["entries"] = [
            {"path": path, "sha256": sha256}
            for path, sha256 in carrier.entries
        ]
    return result


def removed_result(carrier: Carrier) -> dict[str, Any]:
    return {"state": "removed", "filename": carrier.filename, "version": carrier.version}


def action_type(before: Carrier | None, result: Carrier | None) -> str:
    if before is None and result is not None:
        return "ADD"
    if before is not None and result is None:
        return "REMOVE"
    if before is None or result is None:
        raise AssertionError("unreachable carrier state")
    moved = Path(before.path).parent != Path(result.path).parent
    updated = before.filename != result.filename or before.sha256 != result.sha256
    if moved and updated:
        return "MOVE+UPDATE"
    if moved:
        return "MOVE"
    if updated:
        return "UPDATE"
    raise ContextError("no_governed_file_change", "trigger resolves to no lifecycle, structural, or carrier-state change", identity=result.identity)


def event_message(event: Mapping[str, Any], previous_result: Mapping[str, Any] | None) -> str:
    raw_sources = event.get("sources")
    if not isinstance(raw_sources, list):
        raise ContextError("event_sources_invalid", "structured event sources must be an array")
    grouped: dict[str, list[tuple[str, int]]] = {}
    for item in raw_sources:
        if not isinstance(item, Mapping):
            raise ContextError("event_sources_invalid", "structured event source must be an object")
        relation_type = item.get("relation_type")
        filename = item.get("filename")
        version = item.get("version")
        if not isinstance(relation_type, str) or not isinstance(filename, str) or not isinstance(version, int):
            raise ContextError("event_sources_invalid", "structured event source fields are invalid")
        grouped.setdefault(relation_type, []).append((filename, version))
    upstream = "0" if not grouped else "; ".join(
        f"{kind}=" + ", ".join(f"{name}@{version}" for name, version in sorted(entries))
        for kind, entries in sorted(grouped.items())
    )
    action = event.get("action_type")
    result = event.get("result")
    if action not in {"ADD", "MOVE", "UPDATE", "MOVE+UPDATE", "REMOVE"} or not isinstance(result, Mapping):
        raise ContextError("event_projection_invalid", "event action_type or result is invalid")
    filename = result.get("filename")
    version = result.get("version")
    if not isinstance(filename, str) or not isinstance(version, int):
        raise ContextError("event_projection_invalid", "event result requires filename and version")
    current = f"{filename}@{version}"
    if action in {"MOVE", "MOVE+UPDATE"}:
        if previous_result is None:
            raise ContextError("previous_result_missing", "move projection requires the preceding result")
        prior_path = previous_result.get("path")
        current_path = result.get("path")
        if not isinstance(prior_path, str) or not isinstance(current_path, str):
            raise ContextError("previous_result_invalid", "move projection requires previous and present paths")
        affected = f"{prior_path}@{previous_result['version']} -> {current_path}@{version}"
    elif action == "UPDATE" and previous_result is not None and previous_result.get("filename") != filename:
        affected = f"{previous_result['filename']}@{previous_result['version']} -> {current}"
    else:
        affected = current
    return f"{upstream} | {action} | {affected}"


def predicted_partitions(root: Path, journal_relative: Path, author: str, local_date: str, count: int) -> list[dict[str, Any]]:
    directory = root / journal_relative
    pattern = re.compile(re.escape(f"{author}-{local_date}-part-") + r"([1-9][0-9]*)\.ndjson$")
    counts: dict[int, int] = {}
    if directory.is_dir():
        for path in directory.iterdir():
            match = pattern.fullmatch(path.name)
            if match and path.is_file():
                counts[int(match.group(1))] = len([line for line in path.read_text(encoding="utf-8").splitlines() if line])
    part = max(counts, default=1)
    if part not in counts:
        counts[part] = 0
    result: list[dict[str, Any]] = []
    for _ in range(count):
        if counts[part] >= 100:
            part += 1
            counts.setdefault(part, 0)
        counts[part] += 1
        result.append(
            {
                "author": author,
                "local_date": local_date,
                "part": part,
                "path": (journal_relative / f"{author}-{local_date}-part-{part}.ndjson").as_posix(),
                "predicted_line": counts[part],
            }
        )
    return result


def lease_prediction(root: Path, runtime_relative: Path) -> dict[str, Any]:
    path = root / runtime_relative / "commit_change_set" / "lease.json"
    if not path.exists():
        return {"available": True, "path": path.relative_to(root).as_posix(), "holder_action_id": None}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ContextError("apply_lease_invalid", "repository apply lease state is unreadable", path=path.relative_to(root).as_posix()) from error
    holder = value.get("action_id") if isinstance(value, Mapping) else None
    if not isinstance(holder, str) or not holder:
        raise ContextError("apply_lease_invalid", "repository apply lease state has no action_id", path=path.relative_to(root).as_posix())
    return {"available": False, "path": path.relative_to(root).as_posix(), "holder_action_id": holder}


def gather_context(root: Path, trigger: Mapping[str, Any], *, environment: Mapping[str, str] | None = None) -> dict[str, Any]:
    """Return one deterministic sealed schema-v2 context without mutating state.

    ``trigger`` is the exact schema-v1 COMMIT_TRIGGER handoff payload.  All
    filesystem and Git access is read-only; callers may safely use this function
    for a standalone inspection or from COMMIT_CHANGE_SET orchestration.
    """

    root = repository_root(root)
    configured_repository_paths.cache_clear()
    normalized = validate_trigger(root, trigger)
    before_path = normalized["before_path"]
    after_path = normalized["after_path"]
    if before_path is None and after_path is None:
        raise ContextError("trigger_no_file_candidate", "trigger must name a before_path or after_path")

    for candidate in (before_path, after_path):
        if candidate is not None and not project_path_eligible(root, candidate):
            raise ContextError("project_path_ineligible", "trigger path is outside the Git-admitted project frontier", path=candidate)

    before_object_kind = committed_object_kind(root, before_path) if before_path is not None else None
    before_is_tree = before_object_kind == "tree"
    before_is_folder = before_is_tree and before_path is not None and committed_folder_exists(root, before_path)
    after_is_folder = after_path is not None and (root / after_path).is_dir()
    before_data = state_blob(root, before_path, "committed") if before_object_kind == "blob" else None
    result_data: bytes | None = None
    result_state: str | None = None
    if after_path is not None and not after_is_folder:
        result_data, result_state = staged_or_working_result(root, after_path)
    elif after_is_folder:
        result_state = "working"
    before = (
        folder_carrier(root, before_path, committed=True)
        if before_is_folder and before_path is not None
        else project_file_carrier(root, before_path, before_data, committed=True)
        if before_path is not None and before_data is not None
        else None
    )
    result = (
        folder_carrier(root, after_path, committed=False)
        if after_is_folder and after_path is not None
        else project_file_carrier(root, after_path, result_data, committed=False)
        if after_path is not None and result_data is not None
        else None
    )

    if before is None and result is not None and before_path is None:
        assert after_path is not None
        committed_kind = committed_object_kind(root, after_path)
        if committed_kind == "tree":
            before = folder_carrier(root, after_path, committed=True)
        elif committed_kind == "blob":
            committed_same_path = state_blob(root, after_path, "committed")
            if committed_same_path is not None:
                before = project_file_carrier(root, after_path, committed_same_path, committed=True)
    if before is not None and result is not None and before.identity != result.identity:
        if before.kind != result.kind:
            raise ContextError("multiple_project_identities", "trigger before and after paths resolve to different subject kinds", before=before.kind, after=result.kind)
        result = replace(result, identity=before.identity)
    if result is not None and not result.declared_version:
        result = replace(result, version=(before.version + 1 if before is not None else 1))
    if before is None and result is None:
        raise ContextError("governed_project_path_missing", "trigger candidates do not resolve to a Git-trackable file or non-empty folder")

    change = action_type(before, result)
    subject = result or before
    assert subject is not None
    if before is not None and result is not None and before_path == after_path and before.body == result.body:
        raise ContextError("no_governed_project_change", "trigger resolves to no project-path change", identity=subject.identity)

    git_base = git_text(root, ["rev-parse", "HEAD"])
    tree = git_text(root, ["rev-parse", "HEAD^{tree}"])
    assert git_base is not None and tree is not None
    author = resolve_author(root, normalized, environment)
    timezone_name, timezone = configured_timezone(root)
    occurred = parse_instant(normalized["observed_at"], name="observed_at")
    occurred_at = format_instant(occurred)
    local_date = occurred.astimezone(timezone).date().isoformat()
    journal_relative, runtime_relative = configured_paths(root)

    if change == "REMOVE" and subject.kind == "file" and subject.declared_version:
        graph = committed_graph(root)
        relation_source = before
    elif change != "REMOVE" and subject.kind == "file" and subject.declared_version:
        graph = working_graph(root, override_path=result.path if result is not None else None, override=result.body if result is not None else None)
        relation_source = result
    else:
        graph = {}
        relation_source = before if change == "REMOVE" else result
    assert relation_source is not None
    relation_diagnostics: list[dict[str, Any]] = []
    if relation_source.relations:
        try:
            registry = relation_registry(root)
        except ContextError as error:
            registry = {}
            relation_diagnostics.append(error.diagnostic())
    else:
        registry = {}
    relations, sources, resolved_relation_diagnostics = resolve_relations(relation_source, graph, registry)
    relation_diagnostics.extend(resolved_relation_diagnostics)
    current_result = removed_result(before) if change == "REMOVE" else present_result(result)  # type: ignore[arg-type]

    action_id = digest({"schema_version": CONTEXT_SCHEMA_VERSION, "trigger_id": normalized["trigger_id"], "identity": subject.identity})
    prior_record, prior_result = scan_prior_events(root, journal_relative, before)
    if prior_result is not None and before is not None and not before.declared_version:
        prior_version = prior_result.get("version")
        if isinstance(prior_version, int) and prior_version >= 1:
            before = replace(before, version=prior_version)
            if result is not None and not result.declared_version:
                result = replace(result, version=prior_version + 1)
            subject = result or before
            current_result = removed_result(before) if change == "REMOVE" else present_result(result)  # type: ignore[arg-type]
    recovery: dict[str, Any] | None = None
    predicted_records: list[dict[str, Any]] = []
    if change == "ADD":
        previous_event_id = None
        prior_result = None
    elif prior_record is not None:
        previous_event_id = prior_record["event_id"]
    else:
        recovery, recovery_record = recovery_candidate(
            action_id=action_id,
            before=before,
            git_base={"commit": git_base, "tree": tree},
            author=author,
            occurred_at=occurred_at,
            llm_session=normalized["llm_session"],
            structural_scope=subject.structural_scope,
        )
        previous_event_id = recovery["event_id"]
        prior_result = recovery["result"]
        predicted_records.append(recovery_record)

    event_core: dict[str, Any] = {
        "schema_version": JOURNAL_EVENT_SCHEMA_VERSION,
        "action_id": action_id,
        "event": "completed",
        "kind": "governed_project_change",
        "subject_kind": subject.kind,
        "author": author,
        "occurred_at": occurred_at,
        "llm_session": normalized["llm_session"],
        "structural_scope": subject.structural_scope,
        "action_type": change,
        "sources": sources,
        "result": current_result,
    }
    if previous_event_id is not None:
        event_core["previous_result_event"] = previous_event_id
    event_unsigned = {"event_id": digest(event_core), **event_core}
    event = {**event_unsigned, "event_digest": digest(event_unsigned)}
    predicted_records.append(event)

    # R804 seals both the selected governed carrier and its direct relation
    # frontier.  The minimal event ``sources`` list is intentionally smaller;
    # it is not enough to prove that a path or content digest remained current.
    # A removal binds the last committed present carrier while recording its
    # result state as removed, so the Journal event can remain a tombstone.
    source_carrier = before if change == "REMOVE" else result
    assert source_carrier is not None
    source_frontier = {
        "identity": source_carrier.identity,
        "kind": source_carrier.kind,
        "state": "removed" if change == "REMOVE" else "present",
        "filename": source_carrier.filename,
        "version": source_carrier.version,
        "path": source_carrier.path,
        "sha256": source_carrier.sha256,
    }
    source_frontier_sha256 = digest(source_frontier)
    relation_frontier = [
        {key: relation[key] for key in ("relation_type", "filename", "version", "path", "sha256", "registry")}
        for relation in relations
    ]
    context_core: dict[str, Any] = {
        "schema_version": CONTEXT_SCHEMA_VERSION,
        "action_id": action_id,
        "trigger": normalized,
        "subject": {"identity": subject.identity, "kind": subject.kind, "selected_state": result_state or "committed"},
        "structural_scope": subject.structural_scope,
        "action_type": change,
        "sources": sources,
        "result": current_result,
        "llm_session": normalized["llm_session"],
        "author": author,
        "occurred_at": occurred_at,
        "timezone": timezone_name,
        "local_date": local_date,
        "git_base": {"commit": git_base, "tree": tree},
        "frontier": {
            "source_sha256": source_frontier_sha256,
            "relations_sha256": digest(relation_frontier),
        },
    }
    if previous_event_id is not None:
        context_core["previous_result_event"] = previous_event_id
    context = {
        "context_id": digest(context_core),
        **context_core,
        "relations": relations,
        "snapshots": {
            "committed": present_result(before) if before is not None else None,
            "staged": present_result(result) if result is not None and result_state == "staged" else None,
            "working": present_result(result) if result is not None and result_state == "working" else None,
        },
        "validation": {"valid": True, "diagnostics": relation_diagnostics},
        "predictions": {
            "journal_records": predicted_records,
            "journal_partitions": predicted_partitions(root, journal_relative, author, local_date, len(predicted_records)),
            "lease": lease_prediction(root, runtime_relative),
            "git_message": event_message(event, prior_result),
        },
    }
    if recovery is not None:
        context["recovery"] = recovery
    if prior_result is not None:
        # Ephemeral context only: this is needed to project move/rename syntax and
        # is deliberately not copied into the current Work Journal event.
        context["previous_result"] = prior_result
    return context


def validate_context(context: Mapping[str, Any]) -> None:
    """Check the immutable fields peers must not reconstruct or redefine."""

    required = {
        "schema_version",
        "context_id",
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
        "validation",
        "predictions",
    }
    missing = sorted(required.difference(context))
    if missing:
        raise ContextError("context_field_missing", "sealed context is missing required fields", fields=missing)
    if context.get("schema_version") != CONTEXT_SCHEMA_VERSION:
        raise ContextError("context_schema_invalid", "sealed context has an unsupported schema version")
    for field in ("context_id", "action_id"):
        if not isinstance(context.get(field), str) or not SHA256.fullmatch(context[field]):
            raise ContextError("context_identity_invalid", "sealed context identity is invalid", field=field)
    if context.get("action_type") not in {"ADD", "MOVE", "UPDATE", "MOVE+UPDATE", "REMOVE"}:
        raise ContextError("context_action_invalid", "sealed context action_type is invalid")
    session = required_mapping(context.get("llm_session"), name="context.llm_session")
    if not APP_NAME.fullmatch(required_string(session.get("app"), name="context.llm_session.app")):
        raise ContextError("llm_session_app_invalid", "sealed context application is invalid")
    parse_uuid(session.get("uuid"), name="context.llm_session.uuid")
    parse_instant(context.get("occurred_at"), name="context.occurred_at")
    if not GITHUB_USERNAME.fullmatch(required_string(context.get("author"), name="context.author")):
        raise ContextError("journal_author_invalid", "sealed context author is invalid")
    result = required_mapping(context.get("result"), name="context.result")
    if result.get("state") == "present":
        for field in ("filename", "version", "path", "sha256"):
            if field not in result:
                raise ContextError("context_result_invalid", "present result is incomplete", field=field)
    elif result.get("state") == "removed":
        if "path" in result or "sha256" in result:
            raise ContextError("context_result_invalid", "removed result contains present-only fields")
    else:
        raise ContextError("context_result_invalid", "result state is invalid")

    trigger = required_mapping(context.get("trigger"), name="context.trigger")
    subject = required_mapping(context.get("subject"), name="context.subject")
    subject_identity = required_string(subject.get("identity"), name="context.subject.identity")
    subject_kind = subject.get("kind")
    if subject_kind not in {"file", "folder"}:
        raise ContextError("context_subject_kind_invalid", "sealed context subject kind must be file or folder")
    expected_action_id = digest(
        {
            "schema_version": CONTEXT_SCHEMA_VERSION,
            "trigger_id": trigger.get("trigger_id"),
            "identity": subject_identity,
        }
    )
    if context["action_id"] != expected_action_id:
        raise ContextError("action_identity_mismatch", "action_id does not match trigger and subject identity")

    core_fields = (
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
    context_core = {field: context[field] for field in core_fields}
    if "previous_result_event" in context:
        context_core["previous_result_event"] = context["previous_result_event"]
    if context["context_id"] != digest(context_core):
        raise ContextError("context_identity_mismatch", "context_id does not match its sealed authoritative fields")

    frontier = required_mapping(context.get("frontier"), name="context.frontier")
    relations = context.get("relations")
    if not isinstance(relations, list):
        raise ContextError("context_relations_invalid", "context.relations must be an ordered array")
    detailed_frontier: list[dict[str, Any]] = []
    compact_sources: list[dict[str, Any]] = []
    for relation in relations:
        row = required_mapping(relation, name="context.relations item")
        try:
            detailed_frontier.append(
                {key: row[key] for key in ("relation_type", "filename", "version", "path", "sha256", "registry")}
            )
            compact_sources.append({key: row[key] for key in ("relation_type", "filename", "version")})
        except KeyError as error:
            raise ContextError("context_relations_invalid", "detailed relation frontier is incomplete", field=error.args[0]) from error
    if context.get("sources") != compact_sources:
        raise ContextError("context_sources_invalid", "sources are not the compact detailed-relation projection")
    if frontier.get("relations_sha256") != digest(detailed_frontier):
        raise ContextError("context_relation_frontier_mismatch", "relation frontier digest does not match detailed relations")

    source_frontier: dict[str, Any] = {
        "identity": subject_identity,
        "kind": subject_kind,
        "state": "removed" if result.get("state") == "removed" else "present",
        "filename": result.get("filename"),
        "version": result.get("version"),
    }
    if result.get("state") == "present":
        source_frontier.update({"path": result.get("path"), "sha256": result.get("sha256")})
    else:
        snapshots = required_mapping(context.get("snapshots"), name="context.snapshots")
        committed = required_mapping(snapshots.get("committed"), name="context.snapshots.committed")
        source_frontier.update({"path": committed.get("path"), "sha256": committed.get("sha256")})
    if frontier.get("source_sha256") != digest(source_frontier):
        raise ContextError("context_source_frontier_mismatch", "source frontier digest does not match selected carrier")

    predictions = required_mapping(context.get("predictions"), name="context.predictions")
    records = predictions.get("journal_records")
    if not isinstance(records, list) or not records:
        raise ContextError("context_events_invalid", "predicted Journal records must be a non-empty array")
    completed_records: list[Mapping[str, Any]] = []
    for raw_record in records:
        record = required_mapping(raw_record, name="context Journal record")
        event_digest = record.get("event_digest")
        unsigned = dict(record)
        unsigned.pop("event_digest", None)
        if not isinstance(event_digest, str) or not SHA256.fullmatch(event_digest) or digest(unsigned) != event_digest:
            raise ContextError("context_event_digest_mismatch", "predicted Journal record digest is invalid")
        if record.get("action_id") != context["action_id"]:
            raise ContextError("context_event_action_mismatch", "predicted Journal record action differs from context")
        if record.get("author") != context["author"] or record.get("occurred_at") != context["occurred_at"]:
            raise ContextError("context_event_provenance_mismatch", "predicted Journal record provenance differs from context")
        if record.get("llm_session") != context["llm_session"] or record.get("structural_scope") != context["structural_scope"]:
            # A recovered baseline uses the preceding carrier's Structural
            # scope, so only current change events must equal the current scope.
            if record.get("event") != "recovered" or record.get("llm_session") != context["llm_session"]:
                raise ContextError("context_event_provenance_mismatch", "predicted Journal record scope or session differs")
        if record.get("event") == "completed" and record.get("kind") == "governed_project_change":
            event_core = dict(unsigned)
            event_id = event_core.pop("event_id", None)
            if not isinstance(event_id, str) or event_id != digest(event_core):
                raise ContextError("context_event_identity_mismatch", "completed event_id does not match its structured event")
            completed_records.append(record)
    if len(completed_records) != 1:
        raise ContextError("context_events_invalid", "context must predict exactly one completed governed_project_change")
    completed = completed_records[0]
    if completed.get("subject_kind") != subject_kind:
        raise ContextError("context_event_projection_mismatch", "completed event subject kind differs from context")
    for field in ("action_type", "sources", "result"):
        if completed.get(field) != context.get(field):
            raise ContextError("context_event_projection_mismatch", f"completed event {field} differs from context")
    if completed.get("previous_result_event") != context.get("previous_result_event"):
        raise ContextError("context_event_projection_mismatch", "completed event predecessor differs from context")
