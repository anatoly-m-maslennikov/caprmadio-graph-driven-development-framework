"""Private, filesystem-only readiness exchange for the release-host worker.

This module deliberately owns no worker lifecycle, DBOS state, workflow, Tool,
HTTP endpoint, or Journal fact.  The foreground worker owns the singleton lock
and starts this listener only after its scheduler is initialized.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Mapping
import json
import math
import os
from pathlib import Path
import re
import secrets
import stat
import tempfile
import threading
import time

try:  # The host worker is POSIX-only, as is its caller-owned singleton lock.
    import fcntl
except ImportError:  # pragma: no cover - makes the failure explicit elsewhere.
    fcntl = None


__all__ = ["HealthError", "HealthShutdownIncomplete", "probe_worker", "start_listener"]


_DIRECTORY = Path(".caprmedio_install/workflow_orchestrator/release-host")
_HEALTH = _DIRECTORY / "health"
_REQUESTS = _HEALTH / "requests"
_REPLIES = _HEALTH / "replies"
_IDENTITY_KEYS = frozenset((
    "pid", "start_token", "application_version", "runtime_fingerprint", "state",
))
_EXCHANGE_KEYS = frozenset(("nonce", "deadline_monotonic", *_IDENTITY_KEYS))
_HEX_64 = re.compile(r"^[0-9a-f]{64}$")
_MESSAGE_NAME = re.compile(r"^([0-9a-f]{64})\.json$")
_MAX_BYTES = 4096
_MAX_PENDING = 64
_MAX_DEADLINE_SECONDS = 2.0
_POLL_SECONDS = 0.01
_CLOSE_JOIN_SECONDS = 1.0


class HealthError(RuntimeError):
    """The private release-host readiness exchange is not trustworthy."""


class HealthShutdownIncomplete(HealthError):
    """The listener is still live, so worker-ready state must be preserved."""


class _DuplicateKey(ValueError):
    pass


class _CarrierChanged(RuntimeError):
    """A peer consumed an otherwise valid carrier during a directory scan."""


def _unique_object(pairs: list[tuple[object, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if not isinstance(key, str) or key in value:
            raise _DuplicateKey("duplicate JSON object key")
        value[key] = item
    return value


def _reject_constant(_: str) -> object:
    raise ValueError("non-finite JSON number")


def _root(root: str | Path) -> Path:
    try:
        return Path(root).resolve(strict=True)
    except (OSError, RuntimeError) as error:
        raise HealthError("Release host health root is unavailable") from error


def _lstat(path: Path) -> os.stat_result | None:
    try:
        return os.lstat(path)
    except FileNotFoundError:
        return None
    except OSError as error:
        raise HealthError("Release host health carrier is inaccessible") from error


def _directory(path: Path, *, create: bool) -> None:
    """Require a real directory without ever following a control symlink."""
    existing = _lstat(path)
    if existing is None:
        if not create:
            raise HealthError("Release host health carrier is unavailable")
        try:
            path.mkdir(mode=0o700)
        except FileExistsError:
            pass
        except OSError as error:
            raise HealthError("Release host health carrier is unavailable") from error
        existing = _lstat(path)
    if existing is None or stat.S_ISLNK(existing.st_mode) or not stat.S_ISDIR(existing.st_mode):
        raise HealthError("Release host health carrier must be real directories")


def _health_paths(root: str | Path, *, create: bool) -> tuple[Path, Path, Path]:
    current = _root(root)
    for part in _HEALTH.parts:
        current = current / part
        _directory(current, create=create)
    requests = current / "requests"
    replies = current / "replies"
    _directory(requests, create=create)
    _directory(replies, create=create)
    return current, requests, replies


def _identity(value: Mapping[str, object]) -> dict[str, object]:
    if not isinstance(value, Mapping) or set(value) != _IDENTITY_KEYS:
        raise HealthError("Release host health identity is malformed")
    pid = value.get("pid")
    token = value.get("start_token")
    version = value.get("application_version")
    fingerprint = value.get("runtime_fingerprint")
    if (type(pid) is not int or pid <= 0
            or not isinstance(token, str) or _HEX_64.fullmatch(token) is None
            or not isinstance(version, str) or not version
            or not isinstance(fingerprint, str) or _HEX_64.fullmatch(fingerprint) is None
            or value.get("state") != "ready"):
        raise HealthError("Release host health identity is invalid")
    return {key: value[key] for key in _IDENTITY_KEYS}


def _deadline(value: object, now: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise HealthError("Release host health deadline is invalid")
    deadline = float(value)
    if not math.isfinite(deadline) or deadline <= now or deadline > now + _MAX_DEADLINE_SECONDS:
        raise HealthError("Release host health request is stale")
    return deadline


def _exchange(value: object, identity: Mapping[str, object], now: float) -> dict[str, object]:
    if not isinstance(value, dict) or set(value) != _EXCHANGE_KEYS:
        raise HealthError("Release host health exchange is malformed")
    nonce = value.get("nonce")
    if not isinstance(nonce, str) or _HEX_64.fullmatch(nonce) is None:
        raise HealthError("Release host health nonce is invalid")
    _deadline(value.get("deadline_monotonic"), now)
    if any(value.get(key) != identity[key] for key in _IDENTITY_KEYS):
        raise HealthError("Release host health identity does not match")
    return {key: value[key] for key in _EXCHANGE_KEYS}


def _message_files(directory: Path) -> dict[str, Path]:
    """List only bounded, regular, nonce-named message carriers."""
    try:
        entries = list(os.scandir(directory))
    except OSError as error:
        raise HealthError("Release host health carrier is inaccessible") from error
    messages: dict[str, Path] = {}
    for entry in entries:
        match = _MESSAGE_NAME.fullmatch(entry.name)
        try:
            status = entry.stat(follow_symlinks=False)
        except FileNotFoundError as error:
            raise _CarrierChanged from error
        except OSError as error:
            raise HealthError("Release host health carrier is inaccessible") from error
        if entry.name == ".DS_Store" and stat.S_ISREG(status.st_mode):
            continue
        if (match is None or stat.S_ISLNK(status.st_mode)
                or not stat.S_ISREG(status.st_mode)):
            raise HealthError("Release host health carrier is unsafe")
        messages[match.group(1)] = Path(entry.path)
    if len(messages) > _MAX_PENDING:
        raise HealthError("Release host health backlog is full")
    return messages


def _read_message(path: Path) -> dict[str, object]:
    # The carrier may be swapped after directory enumeration.  Nonblocking
    # open is essential: a FIFO must fail closed after fstat, never pin the
    # listener and make a timed shutdown look complete.
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    try:
        descriptor = os.open(path, flags)
    except FileNotFoundError as error:
        raise _CarrierChanged from error
    except OSError as error:
        raise HealthError("Release host health carrier is unavailable") from error
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_size > _MAX_BYTES:
            raise HealthError("Release host health carrier is unsafe")
        raw = os.read(descriptor, _MAX_BYTES + 1)
        after = os.fstat(descriptor)
    except OSError as error:
        raise HealthError("Release host health carrier is unavailable") from error
    finally:
        os.close(descriptor)
    if (len(raw) > _MAX_BYTES or after.st_size != before.st_size
            or len(raw) != before.st_size):
        raise HealthError("Release host health carrier is unsafe")
    try:
        decoded = raw.decode("utf-8")
        value = json.loads(decoded, object_pairs_hook=_unique_object, parse_constant=_reject_constant)
    except (UnicodeDecodeError, ValueError, _DuplicateKey) as error:
        raise HealthError("Release host health carrier is malformed") from error
    if not isinstance(value, dict):
        raise HealthError("Release host health carrier is malformed")
    return value


def _scan(paths: tuple[Path, Path, Path], identity: Mapping[str, object], now: float) -> tuple[dict[str, Path], dict[str, Path]]:
    """Read a stable snapshot, tolerating only peer removal during handoff."""
    _, requests_directory, replies_directory = paths
    for _ in range(4):
        try:
            requests = _message_files(requests_directory)
            replies = _message_files(replies_directory)
            for messages in (requests, replies):
                for nonce, path in messages.items():
                    value = _exchange(_read_message(path), identity, now)
                    if value["nonce"] != nonce:
                        raise HealthError("Release host health nonce does not match its carrier")
            return requests, replies
        except _CarrierChanged:
            continue
    raise HealthError("Release host health carrier changed during exchange")


def _sync_directory(directory: Path) -> None:
    try:
        descriptor = os.open(directory, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    except OSError as error:
        raise HealthError("Release host health carrier is unavailable") from error
    try:
        os.fsync(descriptor)
    except OSError as error:
        raise HealthError("Release host health carrier cannot be synchronized") from error
    finally:
        os.close(descriptor)


def _atomic_create(path: Path, value: Mapping[str, object], staging: Path) -> None:
    """Create one message atomically, refusing to replace any prior carrier."""
    existing = _lstat(path)
    if existing is not None:
        raise HealthError("Release host health nonce was replayed")
    try:
        raw = json.dumps(dict(value), sort_keys=True, separators=(",", ":"),
                         ensure_ascii=True, allow_nan=False).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise HealthError("Release host health carrier is malformed") from error
    if len(raw) > _MAX_BYTES:
        raise HealthError("Release host health carrier is oversized")
    descriptor = -1
    temporary: Path | None = None
    try:
        descriptor, name = tempfile.mkstemp(prefix=".health-", suffix=".tmp", dir=staging)
        temporary = Path(name)
        with os.fdopen(descriptor, "wb") as handle:
            descriptor = -1
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.link(temporary, path)
        except FileExistsError as error:
            raise HealthError("Release host health nonce was replayed") from error
        except OSError as error:
            raise HealthError("Release host health carrier cannot be published") from error
        _sync_directory(path.parent)
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        if temporary is not None:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass
            except OSError:
                pass


def _unlink_exact(path: Path, expected: Mapping[str, object]) -> None:
    """Remove only an unchanged regular carrier that this exchange owns."""
    if _lstat(path) is None:
        return
    try:
        value = _read_message(path)
    except (HealthError, _CarrierChanged):
        return
    if value != dict(expected):
        return
    try:
        path.unlink()
    except FileNotFoundError:
        return
    except OSError:
        return


class _CapacityLock:
    def __init__(self, health: Path):
        self._path = health / ".probe.lock"
        self._descriptor: int | None = None

    def __enter__(self) -> "_CapacityLock":
        if fcntl is None:
            raise HealthError("Release host health capacity lock is unavailable")
        status = _lstat(self._path)
        if status is not None and (stat.S_ISLNK(status.st_mode) or not stat.S_ISREG(status.st_mode)):
            raise HealthError("Release host health capacity lock is unsafe")
        flags = os.O_RDWR | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0)
        try:
            self._descriptor = os.open(self._path, flags, 0o600)
            state = os.fstat(self._descriptor)
            if not stat.S_ISREG(state.st_mode):
                raise HealthError("Release host health capacity lock is unsafe")
            fcntl.flock(self._descriptor, fcntl.LOCK_EX)
        except HealthError:
            self.__exit__(None, None, None)
            raise
        except OSError as error:
            self.__exit__(None, None, None)
            raise HealthError("Release host health capacity lock is unavailable") from error
        return self

    def __exit__(self, *_: object) -> None:
        if self._descriptor is not None:
            try:
                fcntl.flock(self._descriptor, fcntl.LOCK_UN)
            except OSError:
                pass
            os.close(self._descriptor)
            self._descriptor = None


class _Listener:
    def __init__(self, paths: tuple[Path, Path, Path], identity: Mapping[str, object]):
        self._paths = paths
        self._identity = dict(identity)
        self._stop = threading.Event()
        self._closed = False
        self._close_lock = threading.Lock()
        self._seen: deque[str] = deque(maxlen=_MAX_PENDING)
        self._seen_set: set[str] = set()
        self._thread = threading.Thread(target=self._listen, name="release-host-health", daemon=True)
        self._thread.start()

    def _remember(self, nonce: str) -> None:
        if len(self._seen) == self._seen.maxlen:
            self._seen_set.discard(self._seen.popleft())
        self._seen.append(nonce)
        self._seen_set.add(nonce)

    def _listen(self) -> None:
        while not self._stop.is_set():
            try:
                self._reply_once()
            except HealthError:
                # A malformed or hostile private carrier is never repaired,
                # reinterpreted, or answered by the listener.
                pass
            self._stop.wait(_POLL_SECONDS)

    def _reply_once(self) -> None:
        now = time.monotonic()
        requests, replies = _scan(self._paths, self._identity, now)
        health, _, replies_directory = self._paths
        for nonce, request_path in requests.items():
            try:
                request = _exchange(_read_message(request_path), self._identity, time.monotonic())
            except _CarrierChanged:
                continue
            if request["nonce"] != nonce or nonce in self._seen_set:
                continue
            if nonce in replies:
                # Existing replies are receipts for another attempt or a
                # replay; never overwrite them.
                self._remember(nonce)
                continue
            if self._stop.is_set():
                return
            _atomic_create(replies_directory / f"{nonce}.json", request, health)
            self._remember(nonce)
            _unlink_exact(request_path, request)

    def _remove_empty_carriers(self) -> None:
        """Best-effort cleanup after the listener has joined; never follows links."""
        health, requests, replies = self._paths
        for path in (health / ".probe.lock",):
            status = _lstat(path)
            if status is not None and stat.S_ISREG(status.st_mode) and not stat.S_ISLNK(status.st_mode):
                try:
                    path.unlink()
                except OSError:
                    pass
        for directory in (replies, requests, health):
            status = _lstat(directory)
            if status is not None and stat.S_ISDIR(status.st_mode) and not stat.S_ISLNK(status.st_mode):
                try:
                    directory.rmdir()
                except OSError:
                    pass

    def close(self) -> None:
        with self._close_lock:
            if self._closed:
                return
            self._stop.set()
            self._thread.join(_CLOSE_JOIN_SECONDS)
            if self._thread.is_alive():
                raise HealthShutdownIncomplete("Release host health listener did not stop")
            self._closed = True
            self._remove_empty_carriers()


def start_listener(root: str | Path, identity: Mapping[str, object]) -> _Listener:
    """Start one private listener after caller-owned DBOS initialization.

    The caller owns the singleton worker lock and removes worker readiness only
    after ``close`` returns.  This helper does not create workers or scheduler
    state.
    """
    checked = _identity(identity)
    paths = _health_paths(root, create=True)
    requests, replies = _message_files(paths[1]), _message_files(paths[2])
    if requests or replies:
        raise HealthError("Release host health backlog is not empty")
    return _Listener(paths, checked)


def probe_worker(root: str | Path, identity: Mapping[str, object]) -> None:
    """Publish one bounded nonce challenge and require its exact ready reply."""
    checked = _identity(identity)
    paths = _health_paths(root, create=False)
    health, requests_directory, replies_directory = paths
    nonce = secrets.token_hex(32)
    deadline = time.monotonic() + _MAX_DEADLINE_SECONDS
    request: dict[str, object] = {
        "nonce": nonce,
        "deadline_monotonic": deadline,
        **checked,
    }
    request_path = requests_directory / f"{nonce}.json"
    reply_path = replies_directory / f"{nonce}.json"
    published = False
    try:
        with _CapacityLock(health):
            current_requests, _ = _scan(paths, checked, time.monotonic())
            if len(current_requests) >= _MAX_PENDING:
                raise HealthError("Release host health backlog is full")
            _atomic_create(request_path, request, health)
            published = True
        while True:
            now = time.monotonic()
            if now >= deadline:
                raise HealthError("Release host health listener did not reply before its deadline")
            current_requests, current_replies = _scan(paths, checked, now)
            reply = current_replies.get(nonce)
            if reply is not None:
                try:
                    value = _exchange(_read_message(reply), checked, now)
                except _CarrierChanged:
                    continue
                if value != request:
                    raise HealthError("Release host health reply does not match its request")
                _unlink_exact(reply, request)
                return
            if nonce not in current_requests:
                raise HealthError("Release host health request disappeared")
            time.sleep(min(_POLL_SECONDS, max(0.0, deadline - now)))
    finally:
        if published:
            _unlink_exact(request_path, request)
            _unlink_exact(reply_path, request)
