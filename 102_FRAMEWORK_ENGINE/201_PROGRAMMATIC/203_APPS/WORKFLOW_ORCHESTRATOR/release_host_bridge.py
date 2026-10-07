"""Fail-closed transport for explicitly started host-only Release execution."""

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from typing import Mapping
import fcntl


NAMESPACE = "release-host"
DIRECTORY = ".caprmedio_install/workflow_orchestrator/release-host"
MARKER = f"{DIRECTORY}/transport.json"
BINDINGS = f"{DIRECTORY}/bindings"
READY = f"{DIRECTORY}/worker.ready"
DATABASE = f"{DIRECTORY}/dbos.sqlite"
FIXED_INTERPRETER = ".caprmedio_runtime/host-tests/bin/python"
_RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$")
_DIGEST = re.compile(r"^[0-9a-f]{64}$")


class ReleaseHostUnavailable(RuntimeError):
    """The deliberately selected host executor is not safe to use."""


def _root(root: str | Path) -> Path:
    return Path(root).resolve(strict=True)


def _component(root: Path, relative: str, *, create: bool = False) -> Path:
    """Resolve a control carrier without following a mutable control symlink."""
    current = root
    for part in Path(relative).parts:
        current = current / part
        if current.is_symlink():
            raise ReleaseHostUnavailable("Release host transport state must not be symlinked")
        if current.exists() and not current.is_dir():
            raise ReleaseHostUnavailable("Release host transport state must be directories")
        if create:
            current.mkdir(exist_ok=True)
    return current


def directory(root: str | Path, *, create: bool = False) -> Path:
    root_path = _root(root)
    return _component(root_path, DIRECTORY, create=create)


def marker_path(root: str | Path) -> Path:
    return directory(root) / "transport.json"


def binding_path(root: str | Path, run_id: str) -> Path:
    _validate_run_id(run_id)
    return _component(_root(root), BINDINGS, create=False) / f"{run_id}.json"


def _validate_run_id(run_id: object) -> str:
    if not isinstance(run_id, str) or _RUN_ID.fullmatch(run_id) is None:
        raise ValueError("Release host binding needs a valid Workflow Run ID")
    return run_id


def request_digest(request: Mapping[str, object]) -> str:
    """The immutable full outer request, not an inferred scheduler payload."""
    if not isinstance(request, Mapping):
        raise ValueError("Release host binding needs a request mapping")
    try:
        encoded = json.dumps(dict(request), sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False, allow_nan=False).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise ValueError("Release host binding request is not canonical JSON") from error
    return hashlib.sha256(encoded).hexdigest()


def _atomic_json(path: Path, value: Mapping[str, object]) -> None:
    if path.is_symlink():
        raise ReleaseHostUnavailable("Release host transport state must not be symlinked")
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.parent.is_symlink():
        raise ReleaseHostUnavailable("Release host transport state must not be symlinked")
    descriptor, name = tempfile.mkstemp(prefix=f".{path.stem}-", suffix=".json", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(value, handle, sort_keys=True, separators=(",", ":"))
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def _read_json(path: Path, message: str) -> dict[str, object]:
    if path.is_symlink() or not path.is_file():
        raise ReleaseHostUnavailable(message)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ReleaseHostUnavailable(message) from error
    if not isinstance(value, dict):
        raise ReleaseHostUnavailable(message)
    return value


def publish_transport(root: str | Path) -> dict[str, str]:
    """Atomically select this transport after an explicit host-worker start."""
    path = directory(root, create=True) / "transport.json"
    value = {"namespace": NAMESPACE, "transport": NAMESPACE}
    if path.exists() or path.is_symlink():
        # A deliberate restart can reuse an exact carrier, never repair or
        # reinterpret a malformed prior transport selection.
        return transport(root)
    _atomic_json(path, value)
    return value


def transport(root: str | Path) -> dict[str, str]:
    value = _read_json(marker_path(root), "Release host transport marker is unavailable")
    if value != {"namespace": NAMESPACE, "transport": NAMESPACE}:
        raise ReleaseHostUnavailable("Release host transport marker is invalid")
    return {"namespace": NAMESPACE, "transport": NAMESPACE}


def retain_binding(root: str | Path, *, run_id: str, frozen_request_digest: str) -> dict[str, str]:
    """Persist one exact host choice; repeat only the identical admission."""
    run_id = _validate_run_id(run_id)
    if not isinstance(frozen_request_digest, str) or _DIGEST.fullmatch(frozen_request_digest) is None:
        raise ValueError("Release host binding needs an exact frozen request digest")
    bindings = _component(_root(root), BINDINGS, create=True)
    path = bindings / f"{run_id}.json"
    value = {"frozen_request_digest": frozen_request_digest, "namespace": NAMESPACE,
             "run_id": run_id, "transport": NAMESPACE}
    lock = bindings / f"{run_id}.lock"
    if lock.is_symlink():
        raise ReleaseHostUnavailable("Release host Run binding is unavailable")
    with lock.open("a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        if path.exists() or path.is_symlink():
            existing = _read_json(path, "Release host Run binding is unavailable")
            if existing != value:
                raise ReleaseHostUnavailable("Release host Run binding conflicts with the frozen request")
            return value
        _atomic_json(path, value)
    return value


def binding(root: str | Path, *, run_id: str, frozen_request_digest: str | None = None) -> dict[str, str]:
    """Validate an exact retained binding; never infer one from a native Run."""
    run_id = _validate_run_id(run_id)
    value = _read_json(binding_path(root, run_id), "Release host Run binding is unavailable")
    expected = {"namespace": NAMESPACE, "run_id": run_id, "transport": NAMESPACE}
    if any(value.get(key) != item for key, item in expected.items()):
        raise ReleaseHostUnavailable("Release host Run binding is invalid")
    digest = value.get("frozen_request_digest")
    if not isinstance(digest, str) or _DIGEST.fullmatch(digest) is None:
        raise ReleaseHostUnavailable("Release host Run binding is invalid")
    if frozen_request_digest is not None and digest != frozen_request_digest:
        raise ReleaseHostUnavailable("Release host Run binding does not match the frozen request")
    if set(value) != {"frozen_request_digest", "namespace", "run_id", "transport"}:
        raise ReleaseHostUnavailable("Release host Run binding is invalid")
    return {key: value[key] for key in ("frozen_request_digest", "namespace", "run_id", "transport")}


def has_binding(root: str | Path, run_id: str) -> bool:
    """Only routing selection uses this predicate; validation remains mandatory."""
    try:
        path = binding_path(root, run_id)
    except (FileNotFoundError, ValueError):
        return False
    return path.exists() or path.is_symlink()


def fixed_interpreter(root: str | Path) -> Path:
    interpreter = _root(root) / FIXED_INTERPRETER
    if interpreter.is_symlink():
        # The virtualenv's interpreter may be a supported external link; only
        # the Project-owned runtime directory itself is protected above.
        if not interpreter.exists():
            raise ReleaseHostUnavailable("Release host fixed interpreter is unavailable")
    elif not interpreter.is_file():
        raise ReleaseHostUnavailable("Release host fixed interpreter is unavailable")
    return interpreter


def subprocess_environment(root: str | Path, environment: Mapping[str, str] | None = None) -> dict[str, str]:
    """Construct child-only routing state without mutating the MCP process."""
    source = os.environ if environment is None else environment
    value = dict(source)
    value["CAPRMEDIO_RUNTIME_NAMESPACE"] = NAMESPACE
    value.pop("CAPRMEDIO_AGENT_MODE", None)
    value["CAPRMEDIO_PROJECT_ROOT"] = str(_root(root))
    return value


def _worker_is_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except (OSError, ValueError):
        return False
    return True


def _runtime_fingerprint(root: Path) -> str:
    from engine import runtime_fingerprint
    return runtime_fingerprint(root)


def _application_version() -> str:
    from backend import RELEASE_HOST_APP_VERSION
    return RELEASE_HOST_APP_VERSION


def availability(root: str | Path) -> dict[str, object]:
    """Require independently persisted routing, DB and ready-worker evidence."""
    root_path = _root(root)
    transport(root_path)
    ready = _read_json(root_path / READY, "Release host worker is not ready")
    fingerprint = ready.get("runtime_fingerprint")
    if (set(ready) != {"application_version", "pid", "runtime_fingerprint", "state"}
            or ready.get("state") != "ready" or type(ready.get("pid")) is not int
            or ready["pid"] <= 0 or not isinstance(ready.get("application_version"), str)
            or not isinstance(fingerprint, str) or _DIGEST.fullmatch(fingerprint) is None
            or ready["application_version"] != _application_version()):
        raise ReleaseHostUnavailable("Release host worker readiness is invalid")
    state = _read_json(root_path / DIRECTORY / "worker.json", "Release host worker state is unavailable")
    if state != {"pid": ready["pid"], "state": "starting"} or not _worker_is_alive(ready["pid"]):
        raise ReleaseHostUnavailable("Release host worker readiness is invalid")
    try:
        if fingerprint != _runtime_fingerprint(root_path):
            raise ReleaseHostUnavailable("Release host worker runtime fingerprint is stale")
    except ReleaseHostUnavailable:
        raise
    except (OSError, RuntimeError, ValueError) as error:
        raise ReleaseHostUnavailable("Release host worker runtime fingerprint is unavailable") from error
    database = root_path / DATABASE
    if database.is_symlink() or not database.is_file():
        raise ReleaseHostUnavailable("Release host scheduler database is unavailable")
    return {"marker": transport(root_path), "ready": ready}


def _operation(request: Mapping[str, object]) -> tuple[str, str]:
    operation = request.get("operation")
    run_id = request.get("run_id")
    if not isinstance(operation, str) or not isinstance(run_id, str):
        raise ValueError("Release host request must carry an operation and Workflow Run ID")
    return operation, _validate_run_id(run_id)


def _is_unknown_effect_resolution(request: Mapping[str, object]) -> bool:
    """Accept only the one closed N15 control carrier before one-shot CLI use."""
    try:
        from contracts import ResolveReleaseUnknownEffect
        ResolveReleaseUnknownEffect.model_validate(request)
    except (ImportError, TypeError, ValueError):
        return False
    return True


def invoke(root: str | Path, request: Mapping[str, object], *, timeout: int = 60) -> dict[str, object]:
    """Call the fixed local release-host client; no alternate transport is tried."""
    if not isinstance(request, Mapping):
        raise ValueError("Release host request must be a mapping")
    operation, run_id = _operation(request)
    unknown_effect_resolution = operation == "resolve_release_unknown_effect"
    if unknown_effect_resolution:
        if not _is_unknown_effect_resolution(request):
            raise ValueError("unknown-effect resolution requires its exact six-key carrier")
    elif operation == "enqueue_selected":
        execution = request.get("execution")
        if not isinstance(execution, Mapping) or execution.get("operation_route") != "release_version":
            raise ValueError("Release host admits only selected Release Version requests")
    elif operation not in {"status", "recover_selected_release", "resolve_release_unknown_effect",
                           "recover_selected_release_status"}:
        raise ValueError("Release host operation is not supported")
    else:
        binding(root, run_id=run_id)
    # The exceptional resolution is a fixed, host-isolated one-shot CLI.  It
    # does not launch or depend on a worker, which could otherwise pick up the
    # retained pending N15 workflow.  All ordinary Release transport remains
    # binding- and readiness-checked above.
    if not unknown_effect_resolution:
        availability(root)
    command = [str(fixed_interpreter(root)), str(Path(__file__).with_name("orchestrator.py").resolve()),
               "--project-root", str(_root(root)), operation]
    try:
        result = subprocess.run(command, input=json.dumps(dict(request)), capture_output=True,
                                text=True, env=subprocess_environment(root), timeout=timeout, check=False)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise ReleaseHostUnavailable("Release host executor is unavailable; no queue fallback") from error
    if result.returncode:
        raise ReleaseHostUnavailable("Release host queue call failed; no queue fallback")
    try:
        response = json.loads(result.stdout)
    except (TypeError, ValueError) as error:
        raise ReleaseHostUnavailable("Release host queue returned invalid structured output") from error
    if not isinstance(response, dict):
        raise ReleaseHostUnavailable("Release host queue returned invalid structured output")
    return response
