"""Explicit local worker and short-lived queue client for independent Workflow Runs."""
import argparse
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Annotated

from pydantic import Field, TypeAdapter
from contracts import Enqueue, EnqueueSelected, RecoverSelectedRelease, RecoverSelectedReleaseStatus, Status
from backend import enqueue, enqueue_selected, recover_selected_release, recover_selected_release_status, status, worker
from engine import Coordinator
from runtime_config import control_directory, docker_runtime

Request = Annotated[Enqueue | EnqueueSelected | RecoverSelectedRelease | RecoverSelectedReleaseStatus | Status, Field(discriminator='operation')]
ADAPTER = TypeAdapter(Request)


def run(root, request):
    request = ADAPTER.validate_python(request)
    if not docker_runtime():
        from docker_bridge import MARKER, invoke
        if Coordinator(root, None).store.path(MARKER).exists():
            return invoke(root, request.model_dump())
    if isinstance(request, Enqueue):
        return enqueue(root, request)
    if isinstance(request, EnqueueSelected):
        return enqueue_selected(root, request)
    if isinstance(request, RecoverSelectedRelease):
        return recover_selected_release(root, request)
    if isinstance(request, RecoverSelectedReleaseStatus):
        return recover_selected_release_status(root, request)
    return status(root, request)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-root', required=True, type=Path)
    parser.add_argument('--input', default='-')
    parser.add_argument('operation', choices=['worker', 'start-worker', 'enqueue', 'enqueue_selected', 'recover_selected_release', 'recover_selected_release_status', 'status'])
    args = parser.parse_args()
    if args.operation in ('worker', 'start-worker'):
        engine = Coordinator(args.project_root, None)
        directory = engine.store.path(control_directory())
        directory.mkdir(parents=True, exist_ok=True)
        if args.operation == 'start-worker':
            with engine.store.path('.caprmedio_install/workflow_orchestrator/worker.log').open('ab') as log:
                child = subprocess.Popen([sys.executable, str(Path(__file__).resolve()),
                    '--project-root', str(engine.root), 'worker'], stdin=subprocess.DEVNULL,
                    stdout=log, stderr=log, start_new_session=True)
            print(json.dumps({'worker_pid': child.pid, 'outcome': 'starting',
                              'log_path': '.caprmedio_install/workflow_orchestrator/worker.log'}))
        else:
            lock = directory / 'worker.lock'
            with lock.open('a') as handle:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
                (directory / 'worker.ready').unlink(missing_ok=True)
                engine.save(directory / 'worker.json', {'pid': os.getpid(), 'state': 'starting'})
                try:
                    worker(args.project_root, ready_file=directory / 'worker.ready')
                finally:
                    (directory / 'worker.ready').unlink(missing_ok=True)
                    engine.save(directory / 'worker.json', {'pid': os.getpid(), 'state': 'stopped'})
    else:
        raw = sys.stdin.read() if args.input == '-' else Path(args.input).read_text()
        request = json.loads(raw)
        if 'operation' in request and request['operation'] != args.operation:
            parser.error('Operation conflicts with request')
        request['operation'] = args.operation
        print(json.dumps(run(args.project_root, request), default=str))


if __name__ == '__main__':
    main()
