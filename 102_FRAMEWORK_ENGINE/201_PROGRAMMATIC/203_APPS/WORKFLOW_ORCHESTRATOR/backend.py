"""DBOS is the durable scheduler; existing Run evidence remains the observed history."""
import json
from pathlib import Path
import signal
import threading

from contracts import Enqueue, EnqueueSelected, Status
from agent import CodexAgent
from engine import Coordinator, execute_phase, runtime_fingerprint
from runtime_config import control_directory, docker_runtime, implementation_mock_runtime
from remote_agent import RemoteAgent
from selected_execution import SelectedExecution
from selected_native_providers import SelectedNativeProviders

APPLICATION = 'caprmedio-orchestrator'
QUEUE = 'base-revise'
WORKFLOW = 'rmed-atoms-base-revise-independent'
APP_VERSION = 'base-revise-v5-selected-v1-docker-project-mount'
SELECTED_WORKFLOW = 'selected-workflow-execution'


def database(root):
    engine = Coordinator(root, None)
    path = engine.store.path(f'{control_directory()}/dbos.sqlite')
    path.parent.mkdir(parents=True, exist_ok=True)
    return path, f'sqlite:///{path}'


def client(root):
    from dbos import DBOSClient
    path, url = database(root)
    if not path.is_file():
        raise RuntimeError('Start the explicit worker once to initialize its DBOS database')
    return DBOSClient(system_database_url=url, application_name=APPLICATION,
                      retry_connection_errors=False)


def enqueue(root, request):
    request = Enqueue.model_validate(request)
    engine = Coordinator(root, None)
    # Admission is protected against simultaneous clients claiming one ID.
    with engine.store._lock(request.run_id):
        engine.freeze(request)
        transport = client(root)
        try:
            transport.enqueue({'queue_name': QUEUE, 'workflow_name': WORKFLOW,
                               'workflow_id': request.run_id, 'app_version': APP_VERSION}, request.run_id)
        finally:
            transport.destroy()
    return status(root, Status(run_id=request.run_id))


def enqueue_selected(root, request):
    """Freeze a source-bound request before its explicit DBOS queue admission."""
    request = EnqueueSelected.model_validate(request)
    selected = SelectedExecution(root)
    # The selected coordinator owns a separate durable request carrier so it
    # cannot reinterpret Base Revise request.json state.
    frozen = selected.freeze(request.model_dump())
    transport = client(root)
    try:
        transport.enqueue({'queue_name': QUEUE, 'workflow_name': SELECTED_WORKFLOW,
                           'workflow_id': request.run_id, 'app_version': APP_VERSION}, request.run_id)
    finally:
        transport.destroy()
    response = status(root, Status(run_id=request.run_id))
    response.update({'workflow_id': frozen['graph']['workflow']['atom_id'],
                     'selected_route': frozen['graph']['route'],
                     'disposition': 'queued'})
    return response


def status(root, request):
    request = Status.model_validate(request)
    transport = client(root)
    try:
        handle = transport.retrieve_workflow(request.run_id)
        queue_status = handle.get_status()
        response = {'workflow_run_id': request.run_id, 'scheduler_status': queue_status.status,
                    'backend': 'dbos', 'workflow_id': 'CA-O-104'}
        if queue_status.status == 'SUCCESS':
            response['result'] = handle.get_result()
    finally:
        transport.destroy()
    selected = SelectedExecution(root)
    selected_directory = selected.run_directory(request.run_id)
    selected_request = selected_directory / 'selected_request.json'
    if selected_request.is_file():
        frozen = selected._read(selected_request)
        response.update({'workflow_id': frozen['graph']['workflow']['atom_id'],
                         'selected_route': frozen['graph']['route']})
        accepted = selected_directory / 'accepted.json'
        uncertain = selected_directory / 'dispatch_uncertain.json'
        if accepted.is_file():
            result = selected._read(accepted)['result']
            response.update({'selected_result': result, 'outcome': result.get('outcome'),
                             'disposition': result.get('disposition')})
        elif uncertain.is_file():
            response.update({'outcome': 'interrupted_pending', 'disposition': 'recording_pending',
                             'reason': selected._read(uncertain).get('reason')})
        else:
            response.setdefault('outcome', 'queued')
        return response
    engine = Coordinator(root, None)
    try:
        state = engine.store.load(request.run_id)
        response.update({key: state.get(key) for key in ('outcome', 'progress', 'report_path',
                        'recording_blockers', 'reason', 'coverage_gates')})
        response['operator_question'] = next((row['operator_question'] for row in
            state.get('coverage_gates', {}).values() if row.get('operator_question')), None)
    except FileNotFoundError:
        blocked = engine.run_directory(request.run_id) / 'blocked.json'
        if blocked.is_file():
            response.update(outcome='interrupted', reason=json.loads(blocked.read_text())['reason'])
        else:
            response['outcome'] = 'queued' if queue_status.status in ('ENQUEUED', 'PENDING') else 'failed'
    if queue_status.status in ('ERROR', 'CANCELLED'):
        response['recorded_outcome'] = response.get('outcome')
        response['outcome'] = 'failed' if queue_status.status == 'ERROR' else 'interrupted'
    return response


def register_execution(DBOS, engine, *, selected_providers=None):
    """Register one admitted recipe with durable phase checkpoints."""
    selected_providers = selected_providers or SelectedNativeProviders(engine.root)
    @DBOS.step(name='base-revise-gather')
    def gather(run_id):
        return engine.gather(run_id)

    @DBOS.step(name='base-revise-check')
    def check(run_id, ordinal):
        return engine.check(run_id, ordinal)

    @DBOS.step(name='base-revise-fix')
    def fix(run_id, ordinal):
        return engine.fix(run_id, ordinal)

    @DBOS.step(name='base-revise-finish')
    def finish(run_id, outcome, reason):
        return engine.finish(run_id, outcome, reason)

    @DBOS.step(name='base-revise-coverage')
    def coverage(run_id, phase, failure_reason=None):
        return engine.coverage_gate(run_id, phase, failure_reason)

    @DBOS.step(name='selected-workflow-dispatch')
    def selected_dispatch(run_id):
        return selected_providers.dispatch(run_id)

    @DBOS.workflow(name=WORKFLOW)
    def execute(run_id):
        return execute_plan(engine, run_id, gather, check, fix, finish, coverage)

    @DBOS.workflow(name=SELECTED_WORKFLOW)
    def execute_selected(run_id):
        return selected_dispatch(run_id)


def execute_plan(engine, run_id, gather, check, fix, finish, coverage):
    try:
        gathered = gather(run_id)
        if gathered['outcome'] != 'running':
            return gathered
        request, _ = engine.request(run_id)
        coverage(run_id, 'gather')
        execute_phase(run_id, 'check', len(request.selection), check, coverage)
        execute_phase(run_id, 'fix', len(request.selection), fix, coverage)
        return finish(run_id, 'completed', None)
    except (ValueError, RuntimeError, OSError) as error:
        try:
            return finish(run_id, 'interrupted', str(error))
        except FileNotFoundError:
            engine.save(engine.run_directory(run_id) / 'blocked.json', {'reason': str(error)})
            return {'workflow_run_id': run_id, 'outcome': 'interrupted', 'reason': str(error)}


def worker(root, *, agent=None, ready_file=None, implementation_agent=None):
    """Explicitly started foreground process; no implicit daemon or hook installation."""
    from dbos import DBOS
    root = Path(root).resolve(strict=True)
    if implementation_agent is None and implementation_mock_runtime():
        from implementation_mock_agent import ImplementationMockAgent
        implementation_agent = ImplementationMockAgent(root)
    _, url = database(root)
    engine = Coordinator(root, agent or (RemoteAgent() if docker_runtime() else CodexAgent()))
    stop = threading.Event()
    DBOS(config={'name': APPLICATION, 'system_database_url': url,
                 'run_admin_server': False, 'enable_otlp': False,
                 'application_version': APP_VERSION, 'max_executor_threads': 2})
    register_execution(DBOS, engine, selected_providers=SelectedNativeProviders(
        root, implementation_agent=implementation_agent))

    previous = {number: signal.getsignal(number) for number in (signal.SIGINT, signal.SIGTERM)}
    for number in previous:
        signal.signal(number, lambda *_: stop.set())
    try:
        DBOS.launch()
        DBOS.register_queue(QUEUE, global_concurrency=1, worker_concurrency=1,
                            polling_interval_sec=0.2)
        if ready_file:
            engine.save(Path(ready_file), {'state': 'ready',
                'pid': __import__('os').getpid(),
                'application_version': APP_VERSION,
                'runtime_fingerprint': runtime_fingerprint(root)})
        stop.wait()
    finally:
        DBOS.destroy()
        for number, handler in previous.items():
            signal.signal(number, handler)
