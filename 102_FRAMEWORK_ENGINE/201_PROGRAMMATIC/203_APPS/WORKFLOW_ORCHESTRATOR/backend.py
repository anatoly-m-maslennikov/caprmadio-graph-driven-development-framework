"""DBOS is the durable scheduler; existing Run evidence remains the observed history."""
import json
from pathlib import Path
import signal
import threading
import uuid

from contracts import Enqueue, EnqueueSelected, RecoverSelectedRelease, RecoverSelectedReleaseStatus, Status
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
RECOVERY_WORKFLOW = 'selected-release-recovery'


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


def _release_request_identity(execution):
    """Use the shared selected-Run canonical request digest, never a new seal."""
    import sys
    tools_root = Path(__file__).resolve().parents[2] / '201_TOOLS'
    if str(tools_root) not in sys.path:
        sys.path.insert(0, str(tools_root))
    from workflow_run_support import _canonical_digest
    return _canonical_digest(execution)


def recover_selected_release(root, request):
    """Queue one sealed Release recovery without creating another canonical Run."""
    request = RecoverSelectedRelease.model_validate(request)
    selected = SelectedExecution(root)
    frozen = selected.load(request.run_id)
    saved = frozen.get('request', {}) if isinstance(frozen, dict) else {}
    if (not isinstance(saved, dict) or saved.get('run_id') != request.run_id
            or not isinstance(saved.get('execution'), dict)
            or saved['execution'].get('operation_route') != 'release_version'):
        raise RuntimeError('recovery is admitted only for an existing frozen Release Version Run')
    identity = _release_request_identity(saved['execution'])
    if identity != request.request_identity:
        raise RuntimeError('recovery request identity does not match the frozen Release request')
    # DBOS caches a completed workflow by its control identity.  This is an
    # explicit new delivery attempt, so it needs a fresh scheduler handle;
    # the canonical Run and sealed frozen request identity stay unchanged.
    transport_id = uuid.uuid4().hex
    transport = client(root)
    try:
        transport.enqueue({'queue_name': QUEUE, 'workflow_name': RECOVERY_WORKFLOW,
                           'workflow_id': transport_id, 'app_version': APP_VERSION},
                          request.run_id, identity)
        # Observe the new scheduler identity, never the prior selected Run's
        # cached DBOS workflow result.
        recovery_transport_status = _observe_recovery_transport(transport, transport_id, request.run_id, identity)
    finally:
        transport.destroy()
    canonical_state = status(root, Status(run_id=request.run_id))
    journal_refs, pending_reason = _canonical_recovery_observation(canonical_state)
    response = {'operation': request.operation, 'workflow_run_id': request.run_id,
                'canonical_run': canonical_state, 'canonical_journal_refs': journal_refs,
                'recovery_transport_handle': transport_id,
                'recovery_transport_status': recovery_transport_status}
    # This describes only the newly created scheduler delivery.  In particular,
    # a successful delivery is not evidence that the canonical Release Run is
    # complete; callers must use ``canonical_run`` and its Journal references
    # for that conclusion.
    response['disposition'] = {
        'ENQUEUED': 'queued',
        'PENDING': 'queued',
        'SUCCESS': 'transport_succeeded',
        'ERROR': 'transport_failed',
        'CANCELLED': 'transport_cancelled',
    }.get(recovery_transport_status['scheduler_status'], 'transport_terminal')
    response['blocked_or_pending_reason'] = pending_reason
    return response


def _observe_recovery_transport(transport, transport_id, run_id, request_identity):
    handle = transport.retrieve_workflow(transport_id)
    queue_status = handle.get_status()
    workflow_input = getattr(queue_status, 'input', None)
    if (getattr(queue_status, 'name', None) != RECOVERY_WORKFLOW
            or getattr(queue_status, 'queue_name', None) != QUEUE
            or not isinstance(workflow_input, dict)
            or tuple(workflow_input.get('args', ())) != (run_id, request_identity)
            or workflow_input.get('kwargs') != {}):
        raise RuntimeError('recovery transport does not bind the exact Release recovery workflow and frozen Run')
    result = {'scheduler_status': queue_status.status}
    if queue_status.status == 'SUCCESS':
        result['result'] = handle.get_result()
    return result


def _canonical_recovery_observation(canonical_state):
    """Expose only sealed shared receipts, never an inferred Journal reference."""
    selected_result = canonical_state.get('selected_result') if isinstance(canonical_state, dict) else None
    receipts = selected_result.get('event_receipts', []) if isinstance(selected_result, dict) else []
    if not isinstance(receipts, list):
        refs = []
    else:
        refs = [receipt.get('event_id') for receipt in receipts if isinstance(receipt, dict)
                and isinstance(receipt.get('event_id'), str) and receipt['event_id']]
        if len(refs) != len(receipts) or len(set(refs)) != len(refs):
            refs = []
    reason = canonical_state.get('reason') if isinstance(canonical_state, dict) else None
    if not isinstance(reason, str) or not reason:
        reason = selected_result.get('reason') if isinstance(selected_result, dict) else None
    if not isinstance(reason, str) or not reason:
        pending_ids = selected_result.get('pending_event_ids') if isinstance(selected_result, dict) else None
        if (selected_result.get('disposition') == 'recording_pending' if isinstance(selected_result, dict) else False) and (
                isinstance(pending_ids, list) and pending_ids
                and all(isinstance(event_id, str) and event_id for event_id in pending_ids)):
            reason = 'canonical selected Run has pending sealed event recording'
    return refs, reason if isinstance(reason, str) and reason else None


def recover_selected_release_status(root, request):
    request = RecoverSelectedReleaseStatus.model_validate(request)
    frozen = SelectedExecution(root).load(request.run_id)
    saved = frozen.get('request', {}) if isinstance(frozen, dict) else {}
    execution = saved.get('execution') if isinstance(saved, dict) else None
    if not isinstance(execution, dict) or execution.get('operation_route') != 'release_version':
        raise RuntimeError('recovery status is admitted only for an existing frozen Release Version Run')
    identity = _release_request_identity(execution)
    transport = client(root)
    try:
        transport_status = _observe_recovery_transport(transport, request.recovery_transport_handle, request.run_id, identity)
    finally:
        transport.destroy()
    canonical_state = status(root, Status(run_id=request.run_id))
    journal_refs, pending_reason = _canonical_recovery_observation(canonical_state)
    return {'operation': request.operation, 'workflow_run_id': request.run_id,
            'canonical_run': canonical_state, 'recovery_transport_handle': request.recovery_transport_handle,
            'recovery_transport_status': transport_status, 'canonical_journal_refs': journal_refs,
            'blocked_or_pending_reason': pending_reason}


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

    @DBOS.workflow(name=RECOVERY_WORKFLOW)
    def recover_selected_release(run_id, request_identity):
        return selected_providers.recover_release(run_id, request_identity)


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
