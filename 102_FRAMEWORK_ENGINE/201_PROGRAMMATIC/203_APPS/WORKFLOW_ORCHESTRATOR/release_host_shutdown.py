"""Private idle-only Release-host shutdown; health is never a control channel."""
from contextlib import contextmanager
from collections import deque
import fcntl
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

import release_host_health as health

_HOST = Path('.caprmedio_install/workflow_orchestrator/release-host')
_IDENTITY = frozenset(('pid', 'start_token', 'application_version', 'runtime_fingerprint', 'state'))
_REQUEST = frozenset(('operation', 'nonce', 'deadline_monotonic', *_IDENTITY))
_NAME = re.compile(r'^([0-9a-f]{64})\.json$')
_OPERATION = 'stop-release-worker'
_POLL = 0.01


class ShutdownError(RuntimeError):
    """The shutdown target or admission cannot be authenticated."""


class ShutdownIncomplete(health.HealthShutdownIncomplete):
    """The listener has not joined: DBOS and stopping evidence must remain."""


def _paths(root, *, create=False):
    host = health._root(root)
    for part in _HOST.parts:
        host = host / part
        health._directory(host, create=False)
    channel = host / 'shutdown'
    health._directory(channel, create=create)
    requests, replies = channel / 'requests', channel / 'replies'
    health._directory(requests, create=create)
    health._directory(replies, create=create)
    return host, channel, requests, replies


def _read(path):
    try:
        return health._read_message(path)
    except (health.HealthError, health._CarrierChanged) as error:
        raise ShutdownError('shutdown carrier unavailable or invalid') from error


def _identity(value):
    try:
        return health._identity(value)
    except health.HealthError as error:
        raise ShutdownError('shutdown ready identity invalid') from error


def _published(host):
    identity = _identity(_read(host / 'worker.ready'))
    if _read(host / 'worker.json') != identity:
        raise ShutdownError('shutdown published identity changed')
    return identity


def _marker(value):
    if set(value) != {'nonce', *_IDENTITY} or value.get('state') != 'stopping':
        raise ShutdownError('shutdown stopping marker malformed')
    if not isinstance(value.get('nonce'), str) or health._HEX_64.fullmatch(value['nonce']) is None:
        raise ShutdownError('shutdown stopping nonce invalid')
    _identity({key: ('ready' if key == 'state' else value[key]) for key in _IDENTITY})
    return value


def require_dispatch_open(root):
    host, channel, _, _ = _paths(root, create=True)
    path = channel / 'stopping.json'
    if health._lstat(path) is None:
        return
    marker = _marker(_read(path))
    current = _published(host)
    if all(marker[key] == current[key] for key in _IDENTITY - {'state'}):
        raise ShutdownError('Release host is stopping; dispatch closed')
    # An old identity cannot fence an independently started replacement.


@contextmanager
def admission_fence(root, *, timeout=30):
    _, channel, _, _ = _paths(root, create=True)
    descriptor = None
    deadline = time.monotonic() + max(0, min(float(timeout), 30))
    try:
        descriptor = os.open(channel / 'admission.lock', os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW | os.O_NONBLOCK, 0o600)
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise ShutdownError('shutdown admission fence unsafe')
        while True:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.monotonic() >= deadline:
                    raise ShutdownError('shutdown admission fence timeout')
                time.sleep(_POLL)
        yield lambda: require_dispatch_open(root)
    except OSError as error:
        raise ShutdownError('shutdown admission fence inaccessible') from error
    finally:
        if descriptor is not None:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            finally:
                os.close(descriptor)


def _request(value, identity, now):
    if not isinstance(value, dict) or set(value) != _REQUEST:
        raise ShutdownError('shutdown request malformed')
    if value.get('operation') != _OPERATION or value.get('state') != 'ready':
        raise ShutdownError('shutdown operation invalid')
    _identity({key: value[key] for key in _IDENTITY})
    if not isinstance(value.get('nonce'), str) or health._HEX_64.fullmatch(value['nonce']) is None:
        raise ShutdownError('shutdown request nonce invalid')
    deadline = value.get('deadline_monotonic')
    if (isinstance(deadline, bool) or not isinstance(deadline, (int, float))
            or not math.isfinite(deadline) or not now < deadline <= now + 30):
        raise ShutdownError('shutdown deadline expired or invalid')
    if any(value.get(key) != identity[key] for key in _IDENTITY):
        raise ShutdownError('shutdown request targets a different worker')
    return dict(value)


def _messages(directory):
    messages = {}
    with os.scandir(directory) as entries:
        for entry in entries:
            match = _NAME.fullmatch(entry.name)
            status = entry.stat(follow_symlinks=False)
            if entry.name == '.DS_Store' and stat.S_ISREG(status.st_mode):
                continue
            if match is None or not stat.S_ISREG(status.st_mode) or status.st_size > 4096:
                raise ShutdownError('shutdown request directory unsafe')
            messages[match[1]] = Path(entry.path)
            if len(messages) > 64:
                raise ShutdownError('shutdown request capacity exceeded')
    return messages


def _create(path, value, channel):
    try:
        health._atomic_create(path, value, channel)
    except (health.HealthError, OSError) as error:
        raise ShutdownError('shutdown publication refused') from error


def _replace(path, expected, value, channel):
    if _read(path) != expected:
        raise ShutdownError('shutdown carrier changed before replacement')
    raw = json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
    if len(raw) > 4096:
        raise ShutdownError('shutdown carrier oversized')
    descriptor, name = tempfile.mkstemp(prefix='.shutdown-', dir=channel)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, 'wb') as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        if _read(path) != expected:
            raise ShutdownError('shutdown carrier changed before publication')
        temporary.replace(path)
        health._sync_directory(path.parent)
    finally:
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            pass


class _Listener:
    def __init__(self, root, identity, has_work, request_stop):
        self.root, self.identity = root, _identity(identity)
        self.has_work, self.request_stop = has_work, request_stop
        self.paths = _paths(root, create=True)
        self.stop = threading.Event()
        self.seen = deque(maxlen=64)
        self.thread = threading.Thread(target=self._listen, name='release-host-shutdown', daemon=True)
        self.thread.start()

    def _listen(self):
        while not self.stop.is_set():
            try:
                self._once()
            except (ShutdownError, health.HealthError, OSError):
                pass
            self.stop.wait(_POLL)

    def _once(self):
        host, channel, requests, replies = _paths(self.root, create=False)
        for nonce, path in _messages(requests).items():
            if nonce in self.seen or health._lstat(replies / f'{nonce}.json') is not None:
                continue
            try:
                request = _request(_read(path), self.identity, time.monotonic())
                if request['nonce'] != nonce:
                    continue
                with admission_fence(self.root, timeout=max(0, request['deadline_monotonic'] - time.monotonic())):
                    if self.stop.is_set() or _published(host) != self.identity:
                        return
                    current_request = _request(_read(path), self.identity, time.monotonic())
                    if current_request != request:
                        continue
                    marker_path = channel / 'stopping.json'
                    marker = _marker(_read(marker_path)) if health._lstat(marker_path) is not None else None
                    if marker and all(marker[key] == self.identity[key] for key in _IDENTITY - {'state'}):
                        continue
                    try:
                        busy = bool(self.has_work())
                    except Exception:
                        continue  # Unknown scheduler state cannot authorize stop.
                    if (self.stop.is_set()
                            or _request(_read(path), self.identity, time.monotonic()) != request
                            or _published(host) != self.identity):
                        continue
                    reply = {**request, 'disposition': 'busy' if busy else 'accepted'}
                    if not busy:
                        stopping = {'nonce': nonce, **self.identity, 'state': 'stopping'}
                        if marker is None:
                            _create(marker_path, stopping, channel)
                        else:
                            _replace(marker_path, marker, stopping, channel)
                    _create(replies / f'{nonce}.json', reply, channel)
                    self.seen.append(nonce)
                    health._unlink_exact(path, request)
                    if not busy:
                        self.request_stop()
                        self.stop.set()
                        return
            except (ShutdownError, health.HealthError, OSError):
                continue

    def close(self):
        self.stop.set()
        self.thread.join(timeout=1)
        if self.thread.is_alive():
            raise ShutdownIncomplete('Release host shutdown listener did not join')


def start_listener(root, identity, *, has_work, request_stop):
    """Caller owns singleton lock and DBOS lifecycle; this creates no work."""
    return _Listener(root, identity, has_work, request_stop)


def _local(nonce, disposition):
    return {'operation': _OPERATION, 'nonce': nonce, 'disposition': disposition}


def _probe_before_deadline(root, identity, deadline):
    """Bound authentication even if a denied health capacity lock stalls."""
    finished = threading.Event()
    errors = []
    def probe():
        try:
            health.probe_worker(root, identity)
        except Exception as error:
            errors.append(error)
        finally:
            finished.set()
    thread = threading.Thread(target=probe, name='release-host-stop-authentication', daemon=True)
    thread.start()
    remaining = max(0, deadline - time.monotonic())
    if not finished.wait(remaining) or errors or time.monotonic() >= deadline:
        raise ShutdownError('shutdown health authentication unavailable before deadline')


@contextmanager
def _stopped_proof(host, identity):
    descriptor = os.open(host / 'worker.lock', os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    acquired = False
    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise ShutdownError('shutdown singleton carrier unsafe')
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            acquired = True
        except BlockingIOError:
            pass
        yield acquired and _read(host / 'worker.json') == {**identity, 'state': 'stopped'}
    finally:
        if acquired:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
        os.close(descriptor)


def stop_worker(root, timeout=30):
    """Authenticate exact live identity, request idle shutdown, then prove exit."""
    nonce = secrets.token_hex(32)
    if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or not math.isfinite(timeout) or not 0 < timeout <= 30:
        return _local(nonce, 'pending')
    deadline = time.monotonic() + timeout
    request = path = None
    try:
        host, channel, requests, replies = _paths(root, create=False)
        identity = _published(host)
        _probe_before_deadline(root, identity, deadline)
        if _published(host) != identity or time.monotonic() >= deadline:
            return _local(nonce, 'pending')
        request = {'operation': _OPERATION, 'nonce': nonce, 'deadline_monotonic': deadline, **identity}
        path, reply_path = requests / f'{nonce}.json', replies / f'{nonce}.json'
        with admission_fence(root, timeout=max(0, deadline - time.monotonic())) as check:
            check()
            if len(_messages(requests)) >= 64:
                return _local(nonce, 'pending')
            _create(path, request, channel)
        accepted = {**request, 'disposition': 'accepted'}
        while time.monotonic() < deadline:
            _paths(root, create=False)
            if health._lstat(reply_path) is not None:
                reply = _read(reply_path)
                if reply == {**request, 'disposition': 'busy'}:
                    return _local(nonce, 'busy')
                if reply != accepted:
                    return _local(nonce, 'pending')
                with _stopped_proof(host, identity) as proved:
                    if proved:
                        final = {'operation': _OPERATION, 'nonce': nonce, **identity,
                                 'state': 'stopped', 'disposition': 'stopped', 'lock_released': True}
                        _replace(reply_path, accepted, final, channel)
                        health._unlink_exact(channel / 'stopping.json', {'nonce': nonce, **identity, 'state': 'stopping'})
                        return final
            time.sleep(min(_POLL, max(0, deadline - time.monotonic())))
        return _local(nonce, 'pending')
    except (ShutdownError, health.HealthError, OSError, ValueError):
        return _local(nonce, 'pending')
    finally:
        if path is not None and request is not None:
            try:
                health._unlink_exact(path, request)
            except (health.HealthError, OSError):
                pass  # A denied owned-request cleanup cannot escape closed output.
