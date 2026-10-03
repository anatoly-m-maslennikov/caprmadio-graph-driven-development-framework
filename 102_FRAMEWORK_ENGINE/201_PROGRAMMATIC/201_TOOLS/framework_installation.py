"""Shared, non-executable CAPRMEDIO Tool runtime-publication library.

The canonical source is ``102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS`` in the target
repository.  Installed releases are content-addressed and live below
``.caprmedio_runtime/tools``. Persistent operational state belongs below
``.caprmedio_runtime``; disposable staging and cache state belongs below
``.caprmedio_tmp``.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import tomllib
import uuid
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from project_runtime import RUNTIME_DIRECTORY, TEMPORARY_DIRECTORY, atomic_tempfile


SCHEMA_VERSION = 1
PACKAGE = "caprmedio-framework-engine-tools"
SOURCE_DIRECTORY = Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS")
TOOLS_RUNTIME_DIRECTORY = RUNTIME_DIRECTORY / "tools"
TEMP_DIRECTORY = TEMPORARY_DIRECTORY
CURRENT_MANIFEST = "current.toml"
RELEASE_MANIFEST = "manifest.toml"
TOOLS_DIRECTORY = "TOOLS"
INSTALL_ENTRYPOINT = "TOOLS/INSTALL_TOOLS/install_tools.py"
TRIGGER_ENTRYPOINT = "TOOLS/COMMIT_TRIGGER/commit_trigger.py"
SERVICE_ENTRYPOINT = "TOOLS/START_BACKGROUND_SERVICES/start_background_services.py"
REQUIRED_FILES = (
    "framework_installation.py",
    "project_runtime.py",
    "atom_operations.py",
    "background_services.toml",
    "INSTALL_TOOLS/install_tools.py",
    "START_BACKGROUND_SERVICES/start_background_services.py",
    "COMMIT_TRIGGER/commit_trigger.py",
    "COMMIT_CONTEXT/commit_context.py",
    "COMMIT_CONTEXT/commit_context_logic.py",
    "APPEND_CHANGE_RECORDS/append_change_records.py",
    "COMMIT_CHANGE_SET/commit_change_set.py",
    "ATOM_SEARCH/atom_search.py",
    "ATOM_READ/atom_read.py",
    "ATOM_CREATE/atom_create.py",
    "ATOM_UPDATE/atom_update.py",
    "ATOM_MOVE/atom_move.py",
    "ATOM_ARCHIVE/atom_archive.py",
    "ATOM_PROMOTE/atom_promote.py",
    "ATOM_UPGRADE/atom_upgrade.py",
    "MIGRATE_ATOM_IDENTITY/migrate_atom_identity.py",
    "REBIND_ATOM_RELATIONS/rebind_atom_relations.py",
    "CLOSE_ATOM/close_atom.py",
    "REPLACE_ATOM/replace_atom.py",
    "caprmedio_relation_types.toml",
    "lifecycle_intents.py",
    "work_journal.py",
)
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
EXCLUDED_DIRECTORY_NAMES = {"__pycache__", "tests"}
EXCLUDED_FILE_NAMES = {".DS_Store", ".gitkeep"}


class InstallationError(RuntimeError):
    """One stable installation or verification failure."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value: object) -> str:
    payload = value if isinstance(value, bytes) else canonical_json(value).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def resolve_repository(path: Path | str) -> Path:
    candidate = Path(path).expanduser().resolve()
    for root in (candidate, *candidate.parents):
        if (root / ".git").exists():
            return root
    raise InstallationError("repository-not-found", f"cannot resolve Git repository from {candidate}")


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _atomic_write(path: Path, content: str, *, mode: int | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(path, "install_tools")
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        if mode is not None:
            temporary.chmod(mode)
        os.replace(temporary, path)
    except BaseException:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise


def _source_files(source_root: Path) -> list[Path]:
    if not source_root.is_dir() or source_root.is_symlink():
        raise InstallationError("canonical-source-missing", f"canonical Tool source is missing: {source_root}")
    paths: list[Path] = []
    for path in source_root.rglob("*"):
        relative = path.relative_to(source_root)
        if any(part in EXCLUDED_DIRECTORY_NAMES for part in relative.parts):
            continue
        if not path.is_file() or path.is_symlink():
            continue
        if path.name in EXCLUDED_FILE_NAMES or path.suffix in {".pyc", ".pyo"}:
            continue
        paths.append(path)
    return sorted(paths, key=lambda item: item.relative_to(source_root).as_posix())


def source_inventory(repository: Path | str, *, source_root: Path | None = None) -> tuple[list[dict[str, Any]], str]:
    root = resolve_repository(repository)
    canonical = (source_root or (root / SOURCE_DIRECTORY)).resolve()
    files = _source_files(canonical)
    available = {path.relative_to(canonical).as_posix() for path in files}
    missing = [relative for relative in REQUIRED_FILES if relative not in available]
    if missing:
        raise InstallationError("canonical-source-incomplete", "canonical Tool source is missing: " + ", ".join(missing))
    rows: list[dict[str, Any]] = []
    for path in files:
        relative = f"{TOOLS_DIRECTORY}/{path.relative_to(canonical).as_posix()}"
        rows.append(
            {
                "path": relative,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "mode": path.stat().st_mode & 0o777,
            }
        )
    release = digest({"schema_version": SCHEMA_VERSION, "package": PACKAGE, "files": rows})
    return rows, release


def _render_release_manifest(release: str, rows: Sequence[Mapping[str, Any]]) -> str:
    lines = [f"schema_version = {SCHEMA_VERSION}", f"package = {_quoted(PACKAGE)}", f"release = {_quoted(release)}", ""]
    for row in rows:
        lines.extend(
            [
                "[[files]]",
                f"path = {_quoted(str(row['path']))}",
                f"sha256 = {_quoted(str(row['sha256']))}",
                f"mode = {int(row['mode'])}",
                "",
            ]
        )
    return "\n".join(lines)


def _render_current_manifest(release: str) -> str:
    return "\n".join(
        [
            f"schema_version = {SCHEMA_VERSION}",
            f"package = {_quoted(PACKAGE)}",
            f"release = {_quoted(release)}",
            f"tools_root = {_quoted(TOOLS_DIRECTORY)}",
            f"entrypoint = {_quoted(INSTALL_ENTRYPOINT)}",
            "",
        ]
    )


def _safe_manifest_path(value: object, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise InstallationError("install-manifest-invalid", f"{field} must be a non-empty relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path.as_posix() in {"", "."}:
        raise InstallationError("install-manifest-invalid", f"{field} is unsafe")
    return path.as_posix()


def _read_toml(path: Path, code: str) -> dict[str, Any]:
    try:
        document = tomllib.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise InstallationError(code, f"missing manifest: {path}") from error
    except tomllib.TOMLDecodeError as error:
        raise InstallationError(code, f"invalid TOML: {path}") from error
    if not isinstance(document, dict):
        raise InstallationError(code, f"manifest root must be a table: {path}")
    return document


def installation_status(repository: Path | str) -> dict[str, Any]:
    root = resolve_repository(repository)
    tools_runtime_root = root / TOOLS_RUNTIME_DIRECTORY
    current_path = tools_runtime_root / CURRENT_MANIFEST
    if not current_path.is_file():
        return {"installed": False, "tools_runtime_root": TOOLS_RUNTIME_DIRECTORY.as_posix()}
    current = _read_toml(current_path, "current-manifest-invalid")
    release = current.get("release")
    if current.get("schema_version") != SCHEMA_VERSION or current.get("package") != PACKAGE:
        raise InstallationError("current-manifest-invalid", "installed package identity is invalid")
    if not isinstance(release, str) or not SHA256.fullmatch(release):
        raise InstallationError("current-manifest-invalid", "installed release identity is invalid")
    tools_root_name = _safe_manifest_path(current.get("tools_root"), "tools_root")
    entrypoint_name = _safe_manifest_path(current.get("entrypoint"), "entrypoint")
    release_root = tools_runtime_root / "releases" / release
    manifest = _read_toml(release_root / RELEASE_MANIFEST, "release-manifest-invalid")
    if (
        manifest.get("schema_version") != SCHEMA_VERSION
        or manifest.get("package") != PACKAGE
        or manifest.get("release") != release
    ):
        raise InstallationError("release-manifest-invalid", "installed release manifest identity is invalid")
    raw_rows = manifest.get("files")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise InstallationError("release-manifest-invalid", "installed release has no file inventory")
    rows: list[dict[str, Any]] = []
    for raw in raw_rows:
        if not isinstance(raw, Mapping):
            raise InstallationError("release-manifest-invalid", "installed file row must be a table")
        relative = _safe_manifest_path(raw.get("path"), "files.path")
        expected = raw.get("sha256")
        mode = raw.get("mode")
        if not isinstance(expected, str) or not SHA256.fullmatch(expected) or not isinstance(mode, int):
            raise InstallationError("release-manifest-invalid", f"invalid file metadata: {relative}")
        carrier = release_root / relative
        if not carrier.is_file() or carrier.is_symlink():
            raise InstallationError("installed-file-missing", f"installed file is missing: {relative}")
        actual = hashlib.sha256(carrier.read_bytes()).hexdigest()
        if actual != expected:
            raise InstallationError("installed-file-drift", f"installed file digest differs: {relative}")
        actual_mode = carrier.stat().st_mode & 0o777
        if actual_mode != mode:
            raise InstallationError("installed-file-mode-drift", f"installed file mode differs: {relative}")
        rows.append({"path": relative, "sha256": actual, "mode": mode})
    actual_release = digest({"schema_version": SCHEMA_VERSION, "package": PACKAGE, "files": rows})
    if actual_release != release:
        raise InstallationError("release-digest-mismatch", "installed release digest differs from its identity")
    tools_root = release_root / tools_root_name
    entrypoint = release_root / entrypoint_name
    for required in (tools_root, entrypoint, tools_root / "COMMIT_TRIGGER/commit_trigger.py", tools_root / "START_BACKGROUND_SERVICES/start_background_services.py"):
        if not required.exists():
            raise InstallationError("installed-entrypoint-missing", f"installed entrypoint is missing: {required}")
    return {
        "installed": True,
        "verified": True,
        "release": release,
        "tools_runtime_root": TOOLS_RUNTIME_DIRECTORY.as_posix(),
        "release_root": release_root.relative_to(root).as_posix(),
        "package_root": tools_root.relative_to(root).as_posix(),
        "entrypoint": entrypoint.relative_to(root).as_posix(),
        "file_count": len(rows),
    }


def install_release(
    repository: Path | str,
    *,
    apply: bool,
    source_root: Path | None = None,
) -> dict[str, Any]:
    root = resolve_repository(repository)
    canonical = (source_root or (root / SOURCE_DIRECTORY)).resolve()
    rows, release = source_inventory(root, source_root=canonical)
    tools_runtime_root = root / TOOLS_RUNTIME_DIRECTORY
    release_root = tools_runtime_root / "releases" / release
    result = {
        "installed": apply,
        "verified": False,
        "release": release,
        "tools_runtime_root": TOOLS_RUNTIME_DIRECTORY.as_posix(),
        "release_root": release_root.relative_to(root).as_posix(),
        "package_root": (release_root / TOOLS_DIRECTORY).relative_to(root).as_posix(),
        "entrypoint": (release_root / INSTALL_ENTRYPOINT).relative_to(root).as_posix(),
        "file_count": len(rows),
        "planned_effect": "install-or-select-content-addressed-tool-release",
    }
    if not apply:
        return result
    tools_runtime_root.mkdir(parents=True, exist_ok=True)
    staging_root = root / TEMP_DIRECTORY / "install_tools"
    staging_root.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".staging-{uuid.uuid4().hex}-", dir=staging_root))
    try:
        for row in rows:
            relative = Path(str(row["path"]))
            source = canonical / relative.relative_to(TOOLS_DIRECTORY)
            target = staging / relative
            if not target.parent.is_dir():
                target.parent.mkdir(parents=True, exist_ok=True)
            try:
                with source.open("rb") as source_handle, target.open("wb") as target_handle:
                    shutil.copyfileobj(source_handle, target_handle)
            except PermissionError:
                copied = subprocess.run(["cp", str(source), str(target)], capture_output=True, check=False)
                if copied.returncode != 0:
                    raise InstallationError(
                        "release-copy-failed",
                        copied.stderr.decode("utf-8", "replace").strip() or f"cannot copy release file: {relative}",
                    )
            target.chmod(int(row["mode"]))
        _atomic_write(staging / RELEASE_MANIFEST, _render_release_manifest(release, rows), mode=0o644)
        if release_root.exists():
            expected_manifest = _render_release_manifest(release, rows)
            manifest_path = release_root / RELEASE_MANIFEST
            if not manifest_path.is_file() or manifest_path.read_text(encoding="utf-8") != expected_manifest:
                raise InstallationError("installed-release-collision", f"existing release manifest differs: {release}")
            for row in rows:
                carrier = release_root / str(row["path"])
                if (
                    not carrier.is_file()
                    or carrier.is_symlink()
                    or hashlib.sha256(carrier.read_bytes()).hexdigest() != row["sha256"]
                    or carrier.stat().st_mode & 0o777 != row["mode"]
                ):
                    raise InstallationError("installed-release-collision", f"existing release file differs: {row['path']}")
        else:
            release_root.parent.mkdir(parents=True, exist_ok=True)
            try:
                os.replace(staging, release_root)
            except PermissionError:
                release_root.mkdir()
                promoted = subprocess.run(
                    ["cp", "-R", f"{staging}/.", str(release_root)],
                    capture_output=True,
                    check=False,
                )
                if promoted.returncode != 0:
                    raise InstallationError(
                        "release-promotion-failed",
                        promoted.stderr.decode("utf-8", "replace").strip()
                        or f"cannot promote release: {release}",
                    )
        _atomic_write(tools_runtime_root / CURRENT_MANIFEST, _render_current_manifest(release), mode=0o644)
    finally:
        if staging.exists():
            try:
                shutil.rmtree(staging)
            except PermissionError:
                # Some sandboxed hosts permit file cleanup but prohibit
                # directory removal. Reclaim the disposable bytes and leave
                # only empty cleanup remnants in Project Temporary State.
                for carrier in staging.rglob("*"):
                    if carrier.is_file() or carrier.is_symlink():
                        try:
                            carrier.unlink()
                        except (FileNotFoundError, PermissionError):
                            pass
    return installation_status(root)


__all__ = [
    "InstallationError",
    "PACKAGE",
    "RUNTIME_DIRECTORY",
    "TEMP_DIRECTORY",
    "TOOLS_RUNTIME_DIRECTORY",
    "SCHEMA_VERSION",
    "SERVICE_ENTRYPOINT",
    "SOURCE_DIRECTORY",
    "TRIGGER_ENTRYPOINT",
    "canonical_json",
    "digest",
    "install_release",
    "installation_status",
    "resolve_repository",
    "source_inventory",
]
