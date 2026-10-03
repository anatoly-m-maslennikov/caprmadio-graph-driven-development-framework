#!/usr/bin/env python3
"""Start every enabled CAPRMEDIO background service from the installed registry."""

from __future__ import annotations

import argparse
import json
import os
import re
import signal
import subprocess
import sys
import time
import tomllib
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve()
TOOLS_ROOT = SCRIPT_PATH.parents[1]
for parent in SCRIPT_PATH.parents:
    if parent.name in {".caprmedio_install", ".caprmedio_runtime"}:
        sys.pycache_prefix = str(parent.parent / ".caprmedio_tmp/cache/python")
        break
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from framework_installation import (  # noqa: E402
    InstallationError,
    RUNTIME_DIRECTORY,
    TEMP_DIRECTORY,
    TOOLS_RUNTIME_DIRECTORY,
    installation_status,
    resolve_repository,
)
from project_runtime import atomic_tempfile  # noqa: E402


TOOL_ID = "START_BACKGROUND_SERVICES"
TOOL_KIND = "doer"
TOOL_SCHEMA_VERSION = 1
REGISTRY_NAME = "background_services.toml"
SERVICE_ID = re.compile(r"[a-z][a-z0-9_-]{0,63}\Z")
PLACEHOLDER = re.compile(r"\{(python|repository|tools_runtime_root|tools_root|runtime_root|temporary_root)\}")


class ToolError(RuntimeError):
    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)


@dataclass(frozen=True)
class Service:
    service_id: str
    command: tuple[str, ...]
    working_directory: str
    enabled: bool
    startup_grace_seconds: float


def _json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _envelope(*, ok: bool, mode: str, result: Mapping[str, Any] | None = None, error: Exception | None = None) -> dict[str, Any]:
    diagnostics: list[dict[str, str]] = []
    if error is not None:
        diagnostics.append(
            {
                "code": str(getattr(error, "code", "service-start-failed")),
                "message": str(getattr(error, "message", error)),
            }
        )
    return {
        "schema_version": TOOL_SCHEMA_VERSION,
        "tool": {"capability_id": TOOL_ID, "kind": TOOL_KIND},
        "ok": ok,
        "mode": mode,
        "diagnostics": diagnostics,
        "result": dict(result or {}),
    }


def _safe_relative(value: object, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ToolError("service-registry-invalid", f"{field} must be a non-empty repository-relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path.as_posix() in {"", "."}:
        if path.as_posix() == ".":
            return "."
        raise ToolError("service-registry-invalid", f"{field} must not escape the repository")
    return path.as_posix()


def _load_services(registry: Path) -> list[Service]:
    try:
        document = tomllib.loads(registry.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ToolError("service-registry-missing", f"installed service registry is missing: {registry}") from error
    except tomllib.TOMLDecodeError as error:
        raise ToolError("service-registry-invalid", f"invalid TOML: {registry}") from error
    if document.get("schema_version") != 1:
        raise ToolError("service-registry-invalid", "service registry schema_version is unsupported")
    raw_services = document.get("services")
    if not isinstance(raw_services, list):
        raise ToolError("service-registry-invalid", "services must be an array of tables")
    services: list[Service] = []
    seen: set[str] = set()
    for index, raw in enumerate(raw_services):
        if not isinstance(raw, Mapping):
            raise ToolError("service-registry-invalid", f"services[{index}] must be a table")
        service_id = raw.get("id")
        if not isinstance(service_id, str) or not SERVICE_ID.fullmatch(service_id):
            raise ToolError("service-registry-invalid", f"services[{index}].id is invalid")
        if service_id in seen:
            raise ToolError("service-registry-invalid", f"duplicate service id: {service_id}")
        seen.add(service_id)
        command = raw.get("command")
        if not isinstance(command, list) or not command or not all(isinstance(token, str) and token for token in command):
            raise ToolError("service-registry-invalid", f"service {service_id} requires a non-empty string command array")
        grace = raw.get("startup_grace_seconds", 0.25)
        if not isinstance(grace, (int, float)) or isinstance(grace, bool) or not 0 <= float(grace) <= 30:
            raise ToolError("service-registry-invalid", f"service {service_id} startup_grace_seconds is invalid")
        enabled = raw.get("enabled", True)
        if not isinstance(enabled, bool):
            raise ToolError("service-registry-invalid", f"service {service_id} enabled must be boolean")
        services.append(
            Service(
                service_id=service_id,
                command=tuple(command),
                working_directory=_safe_relative(raw.get("working_directory", "."), f"service {service_id}.working_directory"),
                enabled=enabled,
                startup_grace_seconds=float(grace),
            )
        )
    return sorted(services, key=lambda service: service.service_id)


def _replace_placeholders(token: str, values: Mapping[str, str]) -> str:
    rendered = PLACEHOLDER.sub(lambda match: values[match.group(1)], token)
    if "{" in rendered or "}" in rendered:
        raise ToolError("service-registry-invalid", f"unknown or unmatched command placeholder: {token}")
    return rendered


def _resolved_service(root: Path, service: Service, installed: Mapping[str, Any]) -> dict[str, Any]:
    tools_runtime_root = root / TOOLS_RUNTIME_DIRECTORY
    runtime_root = root / RUNTIME_DIRECTORY
    temporary_root = root / TEMP_DIRECTORY
    tools_root = root / str(installed["package_root"])
    values = {
        "python": sys.executable,
        "repository": str(root),
        "tools_runtime_root": str(tools_runtime_root),
        "tools_root": str(tools_root),
        "runtime_root": str(runtime_root),
        "temporary_root": str(temporary_root),
    }
    command = [_replace_placeholders(token, values) for token in service.command]
    working_directory = root if service.working_directory == "." else root / service.working_directory
    if not working_directory.is_dir() or root not in (working_directory.resolve(), *working_directory.resolve().parents):
        raise ToolError("service-working-directory-invalid", f"service {service.service_id} working directory is unavailable")
    executable = Path(command[0])
    if command[0] != sys.executable:
        resolved_executable = executable if executable.is_absolute() else working_directory / executable
        try:
            resolved_executable.resolve().relative_to(tools_runtime_root.resolve())
        except ValueError as error:
            raise ToolError(
                "service-dependency-outside-tools-runtime",
                f"service {service.service_id} executable is outside .caprmedio_runtime/tools",
            ) from error
    elif len(command) < 2:
        raise ToolError("service-registry-invalid", f"service {service.service_id} Python command has no installed script")
    if command[0] == sys.executable:
        script_tokens = [token for token in command[1:] if not token.startswith("-")]
        if not script_tokens:
            raise ToolError("service-registry-invalid", f"service {service.service_id} Python command has no installed script")
        try:
            Path(script_tokens[0]).resolve().relative_to(tools_runtime_root.resolve())
        except ValueError as error:
            raise ToolError(
                "service-dependency-outside-tools-runtime",
                f"service {service.service_id} script is outside .caprmedio_runtime/tools",
            ) from error
    return {
        "id": service.service_id,
        "command": command,
        "working_directory": str(working_directory),
        "startup_grace_seconds": service.startup_grace_seconds,
    }


def _state_path(root: Path, service_id: str) -> Path:
    return root / RUNTIME_DIRECTORY / "services" / service_id / "state.toml"


def _read_state(path: Path) -> dict[str, Any] | None:
    try:
        state = tomllib.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except tomllib.TOMLDecodeError as error:
        raise ToolError("service-state-invalid", f"invalid runtime service state: {path}") from error
    if state.get("schema_version") != 1 or not isinstance(state.get("pid"), int):
        raise ToolError("service-state-invalid", f"invalid runtime service state: {path}")
    return state


def _alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _atomic_state(path: Path, *, service_id: str, pid: int, command: Sequence[str], release: str) -> None:
    content = "\n".join(
        [
            "schema_version = 1",
            f"service_id = {json.dumps(service_id)}",
            f"pid = {pid}",
            f"release = {json.dumps(release)}",
            "command = [" + ", ".join(json.dumps(token) for token in command) + "]",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(path, "start_background_services")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def service_status(root: Path) -> dict[str, Any]:
    root = resolve_repository(root)
    installed = installation_status(root)
    if not installed.get("installed"):
        raise ToolError("tools-not-installed", "run INSTALL_TOOLS before starting background services")
    registry = root / str(installed["package_root"]) / REGISTRY_NAME
    services = _load_services(registry)
    rows: list[dict[str, Any]] = []
    for service in services:
        resolved = _resolved_service(root, service, installed)
        state = _read_state(_state_path(root, service.service_id))
        pid = int(state["pid"]) if state is not None else None
        rows.append({**resolved, "enabled": service.enabled, "pid": pid, "running": pid is not None and _alive(pid)})
    return {
        "release": installed["release"],
        "registry": registry.relative_to(root).as_posix(),
        "service_count": len(rows),
        "enabled_count": sum(1 for row in rows if row["enabled"]),
        "running_count": sum(1 for row in rows if row["running"]),
        "services": rows,
    }


def start_services(root: Path, *, apply: bool) -> dict[str, Any]:
    root = resolve_repository(root)
    installed = installation_status(root)
    if not installed.get("installed"):
        raise ToolError("tools-not-installed", "run INSTALL_TOOLS before starting background services")
    registry = root / str(installed["package_root"]) / REGISTRY_NAME
    services = [service for service in _load_services(registry) if service.enabled]
    resolved = [_resolved_service(root, service, installed) for service in services]
    existing: list[dict[str, Any]] = []
    pending: list[dict[str, Any]] = []
    for row in resolved:
        state = _read_state(_state_path(root, str(row["id"])))
        if state is not None and _alive(int(state["pid"])):
            existing.append({**row, "effect": "already-running", "pid": int(state["pid"])})
        else:
            pending.append(row)
    if not apply:
        return {
            "release": installed["release"],
            "registry": registry.relative_to(root).as_posix(),
            "planned_start_count": len(pending),
            "already_running_count": len(existing),
            "services": [*existing, *({**row, "effect": "start"} for row in pending)],
        }
    started: list[tuple[subprocess.Popen[bytes], Path]] = []
    results = list(existing)
    try:
        for row in pending:
            directory = root / RUNTIME_DIRECTORY / "services" / str(row["id"])
            directory.mkdir(parents=True, exist_ok=True)
            stdout = (directory / "stdout.log").open("ab", buffering=0)
            stderr = (directory / "stderr.log").open("ab", buffering=0)
            environment = {
                **os.environ,
                "PYTHONPYCACHEPREFIX": str(root / ".caprmedio_tmp/cache/python"),
                "CAPRMEDIO_REPOSITORY": str(root),
                "CAPRMEDIO_TOOLS_RUNTIME_ROOT": str(root / TOOLS_RUNTIME_DIRECTORY),
                "CAPRMEDIO_RUNTIME_ROOT": str(root / RUNTIME_DIRECTORY),
                "CAPRMEDIO_TEMP_ROOT": str(root / ".caprmedio_tmp"),
            }
            try:
                process = subprocess.Popen(
                    list(row["command"]),
                    cwd=str(row["working_directory"]),
                    env=environment,
                    stdin=subprocess.DEVNULL,
                    stdout=stdout,
                    stderr=stderr,
                    start_new_session=True,
                )
            finally:
                stdout.close()
                stderr.close()
            state_path = _state_path(root, str(row["id"]))
            started.append((process, state_path))
            time.sleep(float(row["startup_grace_seconds"]))
            returncode = process.poll()
            if returncode is not None:
                raise ToolError("service-exited-during-start", f"service {row['id']} exited with status {returncode}")
            _atomic_state(
                state_path,
                service_id=str(row["id"]),
                pid=process.pid,
                command=list(row["command"]),
                release=str(installed["release"]),
            )
            results.append({**row, "effect": "started", "pid": process.pid})
    except BaseException:
        for process, state_path in reversed(started):
            if process.poll() is None:
                try:
                    os.killpg(process.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
            try:
                state_path.unlink()
            except FileNotFoundError:
                pass
        raise
    # Ownership is now represented by the runtime PID state rather than by a
    # short-lived Popen object in this launcher process.
    for process, _recorded_state_path in started:
        process.returncode = 0
    return {
        "release": installed["release"],
        "registry": registry.relative_to(root).as_posix(),
        "started_count": sum(1 for row in results if row["effect"] == "started"),
        "already_running_count": sum(1 for row in results if row["effect"] == "already-running"),
        "services": results,
    }


def _describe() -> dict[str, Any]:
    return {
        "capability_id": TOOL_ID,
        "kind": TOOL_KIND,
        "registry": REGISTRY_NAME,
        "tools_runtime_root": TOOLS_RUNTIME_DIRECTORY.as_posix(),
        "runtime_root": RUNTIME_DIRECTORY.as_posix(),
        "temporary_root": TEMP_DIRECTORY.as_posix(),
        "commands": {
            "describe": {"mode": "read-only"},
            "status": {"mode": "read-only"},
            "run": {"mode": "dry-run unless --apply", "effect": "start every enabled installed service"},
        },
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", default=".")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("describe")
    commands.add_parser("status")
    run = commands.add_parser("run")
    run.add_argument("--apply", action="store_true")
    return parser


def cli(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    mode = "read-only"
    try:
        if args.command == "describe":
            result = _describe()
        elif args.command == "status":
            result = service_status(Path(args.repository))
        else:
            mode = "apply" if args.apply else "dry-run"
            result = start_services(Path(args.repository), apply=args.apply)
        print(_json(_envelope(ok=True, mode=mode, result=result)))
        return 0
    except (ToolError, InstallationError) as error:
        print(_json(_envelope(ok=False, mode=mode, error=error)))
        return 2


if __name__ == "__main__":
    raise SystemExit(cli())
