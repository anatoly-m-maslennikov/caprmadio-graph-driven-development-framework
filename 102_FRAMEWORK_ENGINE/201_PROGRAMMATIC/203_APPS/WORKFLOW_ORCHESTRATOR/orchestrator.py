"""Explicit local worker and short-lived queue client for independent Workflow Runs."""
import argparse
import fcntl
import json
import os
import secrets
from pathlib import Path
import subprocess
import sys
from typing import Annotated

from pydantic import Field, TypeAdapter
from contracts import (Enqueue, EnqueueSelected, RecoverSelectedRelease, RecoverSelectedReleaseStatus,
                       ResolveReleaseUnknownEffect, Status)
from backend import (enqueue, enqueue_selected, recover_selected_release,
                     recover_selected_release_status, resolve_release_unknown_effect, status, worker,
                     RELEASE_HOST_APP_VERSION)
from engine import Coordinator, runtime_fingerprint
from release_host_bridge import (directory as release_host_directory, fixed_interpreter,
                                 has_binding as release_host_has_binding, invoke as invoke_release_host,
                                 publish_transport, subprocess_environment)
from runtime_config import control_directory, docker_runtime, release_host_runtime

Request = Annotated[Enqueue | EnqueueSelected | RecoverSelectedRelease | ResolveReleaseUnknownEffect | RecoverSelectedReleaseStatus | Status, Field(discriminator='operation')]
ADAPTER = TypeAdapter(Request)


def run(root, request):
    request = ADAPTER.validate_python(request)
    # A Release host binding is an explicit transport choice.  It must be
    # selected before Docker routing, while the fixed-host subprocess bypasses
    # this branch to reach its own DBOS namespace without recursion.
    if not release_host_runtime():
        if (isinstance(request, EnqueueSelected)
                and request.execution.get('operation_route') == 'release_version'):
            return invoke_release_host(root, request.model_dump())
        if (isinstance(request, (RecoverSelectedRelease, ResolveReleaseUnknownEffect,
                                 RecoverSelectedReleaseStatus, Status))
                and release_host_has_binding(root, request.run_id)):
            return invoke_release_host(root, request.model_dump())
    if not docker_runtime() and not release_host_runtime():
        from docker_bridge import MARKER, invoke
        if Coordinator(root, None).store.path(MARKER).exists():
            return invoke(root, request.model_dump())
    if isinstance(request, Enqueue):
        return enqueue(root, request)
    if isinstance(request, EnqueueSelected):
        return enqueue_selected(root, request)
    if isinstance(request, RecoverSelectedRelease):
        return recover_selected_release(root, request)
    if isinstance(request, ResolveReleaseUnknownEffect):
        return resolve_release_unknown_effect(root, request)
    if isinstance(request, RecoverSelectedReleaseStatus):
        return recover_selected_release_status(root, request)
    return status(root, request)


def _worker_paths(root, *, release_host):
    """Keep detached worker evidence in the scheduler namespace it owns."""
    engine = Coordinator(root, None)
    if release_host:
        directory = release_host_directory(engine.root, create=True)
        return engine, directory, directory / 'worker.log'
    directory = engine.store.path(control_directory())
    directory.mkdir(parents=True, exist_ok=True)
    return engine, directory, engine.store.path('.caprmedio_install/workflow_orchestrator/worker.log')


def _start_worker(root, *, release_host):
    engine, directory, log_path = _worker_paths(root, release_host=release_host)
    operation = 'release-worker' if release_host else 'worker'
    if release_host:
        command = [str(fixed_interpreter(engine.root)), str(Path(__file__).resolve()),
                   '--project-root', str(engine.root), operation]
        environment = subprocess_environment(engine.root)
    else:
        command = [sys.executable, str(Path(__file__).resolve()),
                   '--project-root', str(engine.root), operation]
        environment = None
    with log_path.open('ab') as log:
        child = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=log,
                                 stderr=log, start_new_session=True, env=environment)
    if release_host:
        publish_transport(engine.root)
    return {'release_worker_pid' if release_host else 'worker_pid': child.pid,
            'outcome': 'starting',
            'log_path': str(log_path.relative_to(engine.root))}


def _foreground_worker(root, *, release_host):
    if release_host:
        # This is a foreground CLI process, not the MCP server process.  The
        # explicit command owns its process-local namespace selection.
        os.environ['CAPRMEDIO_RUNTIME_NAMESPACE'] = 'release-host'
        os.environ.pop('CAPRMEDIO_AGENT_MODE', None)
    engine, directory, _ = _worker_paths(root, release_host=release_host)
    if release_host:
        publish_transport(engine.root)
    lock = directory / 'worker.lock'
    with lock.open('a') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        (directory / 'worker.ready').unlink(missing_ok=True)
        identity = {'pid': os.getpid(), 'state': 'starting'}
        if release_host:
            identity.update(start_token=secrets.token_hex(32),
                            application_version=RELEASE_HOST_APP_VERSION,
                            runtime_fingerprint=runtime_fingerprint(engine.root))
        engine.save(directory / 'worker.json', identity)
        shutdown_incomplete = False
        try:
            if release_host:
                from release_host_health import HealthShutdownIncomplete
                try:
                    worker(engine.root, ready_file=directory / 'worker.ready',
                           release_start_token=identity['start_token'])
                except HealthShutdownIncomplete:
                    shutdown_incomplete = True
                    raise
            else:
                worker(engine.root, ready_file=directory / 'worker.ready')
        finally:
            if not shutdown_incomplete:
                (directory / 'worker.ready').unlink(missing_ok=True)
                engine.save(directory / 'worker.json', {**identity, 'state': 'stopped'})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-root', required=True, type=Path)
    parser.add_argument('--input', default='-')
    parser.add_argument('operation', choices=['worker', 'start-worker', 'release-worker',
                        'start-release-worker', 'enqueue', 'enqueue_selected',
                        'recover_selected_release', 'resolve_release_unknown_effect',
                        'recover_selected_release_status', 'status'])
    args = parser.parse_args()
    if args.operation in ('worker', 'start-worker', 'release-worker', 'start-release-worker'):
        release = args.operation in ('release-worker', 'start-release-worker')
        if args.operation.startswith('start-'):
            print(json.dumps(_start_worker(args.project_root, release_host=release)))
        else:
            _foreground_worker(args.project_root, release_host=release)
    else:
        raw = sys.stdin.read() if args.input == '-' else Path(args.input).read_text()
        request = json.loads(raw)
        if 'operation' in request and request['operation'] != args.operation:
            parser.error('Operation conflicts with request')
        request['operation'] = args.operation
        print(json.dumps(run(args.project_root, request), default=str))


if __name__ == '__main__':
    main()
