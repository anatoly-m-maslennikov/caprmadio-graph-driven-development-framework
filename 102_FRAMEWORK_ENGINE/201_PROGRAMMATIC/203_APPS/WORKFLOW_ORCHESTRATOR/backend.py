"""DBOS is the durable scheduler; existing Run evidence remains the observed history."""
import json
from pathlib import Path
import signal
import threading
import uuid

from contracts import (Enqueue, EnqueueSelected, RecoverSelectedRelease, RecoverSelectedReleaseStatus,
                       ResolveReleaseUnknownEffect, Status)
from agent import CodexAgent
from engine import Coordinator, execute_phase, runtime_fingerprint
from runtime_config import (control_directory, docker_runtime, implementation_mock_runtime,
                            release_host_runtime)
from remote_agent import RemoteAgent
from selected_execution import SelectedExecution, canonical_json
from selected_native_providers import SelectedNativeProviders

APPLICATION = 'caprmedio-orchestrator'
QUEUE = 'base-revise'
WORKFLOW = 'rmed-atoms-base-revise-independent'
APP_VERSION = 'base-revise-v5-selected-v1-docker-project-mount'
SELECTED_WORKFLOW = 'selected-workflow-execution'
RECOVERY_WORKFLOW = 'selected-release-recovery'

# This identity is intentionally unrelated to the native or Docker scheduler.
# The control directory is selected in ``runtime_config``; retaining separate
# DBOS identities here also prevents an already-persisted ordinary workflow
# from being picked up by the explicitly started Release host worker.
RELEASE_HOST_APPLICATION = 'caprmedio-release-host'
RELEASE_HOST_QUEUE = 'release-host'
RELEASE_HOST_APP_VERSION = 'release-host-v1-selected-v1'
RELEASE_HOST_SELECTED_WORKFLOW = 'release-host-selected-workflow-execution'
RELEASE_HOST_RECOVERY_WORKFLOW = 'release-host-selected-release-recovery'


def _scheduler_identity():
    if release_host_runtime():
        return {
            'application': RELEASE_HOST_APPLICATION,
            'queue': RELEASE_HOST_QUEUE,
            'app_version': RELEASE_HOST_APP_VERSION,
            'selected_workflow': RELEASE_HOST_SELECTED_WORKFLOW,
            'recovery_workflow': RELEASE_HOST_RECOVERY_WORKFLOW,
        }
    return {
        'application': APPLICATION,
        'queue': QUEUE,
        'app_version': APP_VERSION,
        'selected_workflow': SELECTED_WORKFLOW,
        'recovery_workflow': RECOVERY_WORKFLOW,
    }


def _release_host_bridge():
    """Load the Release-host binding boundary only in its explicit namespace.

    Its small API is deliberately split: validation is read-only, while claim
    publishes the per-Run binding only after the selected request is frozen.
    Both receive the canonical request digest, never caller-authored transport
    state.
    """
    import release_host_bridge
    return release_host_bridge


def _release_host_frozen_request_digest(frozen):
    """Digest the exact frozen outer request retained by the transport carrier."""
    request = frozen.get('request') if isinstance(frozen, dict) else None
    if not isinstance(request, dict):
        raise RuntimeError('Release host Run lacks an exact frozen request')
    return _release_host_bridge().request_digest(request)


def _validate_release_host_admission(root, frozen, frozen_request_digest):
    """Read-only preflight: source/route was checked by SelectedExecution."""
    bridge = _release_host_bridge()
    bridge.availability(root)
    # Calculate the exact persisted carrier identity before its first write.
    # The equality check prevents an accidental caller-controlled digest from
    # being used for the retained host binding.
    if bridge.request_digest(frozen['request']) != frozen_request_digest:
        raise RuntimeError('Release host frozen request digest is inconsistent')
    return bridge.transport(root)


def _claim_release_host_binding(root, frozen, frozen_request_digest):
    request = frozen.get('request') if isinstance(frozen, dict) else None
    run_id = request.get('run_id') if isinstance(request, dict) else None
    if not isinstance(run_id, str):
        raise RuntimeError('Release host Run lacks a valid frozen identity')
    return _release_host_bridge().retain_binding(
        root, run_id=run_id, frozen_request_digest=frozen_request_digest,
    )


def _validate_release_host_binding(root, run_id, frozen_request_digest, *, require_available=True):
    bridge = _release_host_bridge()
    # Check the retained host choice first.  A shared selected carrier with no
    # such choice is foreign and must be refused without even consulting the
    # host scheduler state.
    binding = bridge.binding(root, run_id=run_id, frozen_request_digest=frozen_request_digest)
    if require_available:
        bridge.availability(root)
    else:
        # Worker dispatch occurs before its own ready marker is published, so
        # it validates the explicit transport marker and exact Run binding
        # without racing that readiness publication.
        bridge.transport(root)
    return binding


def _preflight_release_host_run_ownership(root, run_id, selected):
    """Prove a shared selected Run is already owned by this host scheduler.

    ``SelectedExecution`` intentionally keeps canonical Run evidence in one
    shared store.  A matching selected request therefore cannot identify its
    executor.  Existing shared state is admitted only after its exact host
    binding and the host DBOS workflow both prove prior host ownership.
    """
    path = selected.run_directory(run_id) / 'selected_request.json'
    if not path.exists() and not path.is_symlink():
        return None
    if not path.is_file() or path.is_symlink():
        raise RuntimeError('Release host shared selected Run carrier is invalid')
    frozen = selected.load(run_id)
    request = frozen.get('request') if isinstance(frozen, dict) else None
    if not isinstance(request, dict) or request.get('run_id') != run_id:
        raise RuntimeError('Release host shared selected Run carrier has a foreign identity')
    _validate_release_host_binding(root, run_id, _release_host_frozen_request_digest(frozen))
    transport = client(root)
    try:
        handle = transport.retrieve_workflow(run_id)
        queue_status = handle.get_status()
        workflow_input = getattr(queue_status, 'input', None)
        if (getattr(queue_status, 'name', None) != RELEASE_HOST_SELECTED_WORKFLOW
                or getattr(queue_status, 'queue_name', None) != RELEASE_HOST_QUEUE
                or not isinstance(workflow_input, dict)
                or tuple(workflow_input.get('args', ())) != (run_id,)
                or workflow_input.get('kwargs') != {}):
            raise RuntimeError('Release host binding lacks exact host scheduler provenance')
    finally:
        transport.destroy()
    return frozen


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
    return DBOSClient(system_database_url=url, application_name=_scheduler_identity()['application'],
                      retry_connection_errors=False)


def _release_host_has_pending_work(root):
    """Observe every nonterminal host-queue workflow through DBOSClient only."""
    transport = client(root)
    try:
        rows = transport.list_workflows(
            status=['PENDING', 'ENQUEUED'], application_name=RELEASE_HOST_APPLICATION,
            queue_name=RELEASE_HOST_QUEUE, limit=1, load_input=False, load_output=False,
        )
    finally:
        transport.destroy()
    return bool(rows)


def _release_host_admission_fence(root):
    """Use the shutdown-owned fence only in the isolated release-host namespace."""
    from release_host_shutdown import admission_fence
    return admission_fence(root)


def enqueue(root, request):
    request = Enqueue.model_validate(request)
    if release_host_runtime():
        raise RuntimeError('Release host accepts only source-admitted Release selected requests')
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
    scheduler = _scheduler_identity()
    if release_host_runtime():
        existing = _preflight_release_host_run_ownership(root, request.run_id, selected)
        # Validate all immutable request and source bindings before creating a
        # selected-run carrier.  In particular, a foreign route is never
        # frozen into the host namespace merely to obtain a scheduler status.
        frozen = selected._validated_freeze(request.model_dump())
        if frozen['graph'].get('route') != 'release_version':
            raise RuntimeError('Release host accepts only the exact frozen Release route')
        if existing is not None and canonical_json(existing) != canonical_json(frozen):
            raise RuntimeError('Release host Run ID already binds a different selected request')
        frozen_request_digest = _release_host_frozen_request_digest(frozen)
        _validate_release_host_admission(root, frozen, frozen_request_digest)
        frozen = selected.freeze(request.model_dump())
        # Freeze repeats validation, then the binding carries that exact frozen
        # outer request digest before any scheduler admission.
        if _release_host_frozen_request_digest(frozen) != frozen_request_digest:
            raise RuntimeError('Release host frozen request changed before transport binding')
        _claim_release_host_binding(root, frozen, frozen_request_digest)
    else:
        frozen = None
    # The selected coordinator owns a separate durable request carrier so it
    # cannot reinterpret Base Revise request.json state.
    if frozen is None:
        frozen = selected.freeze(request.model_dump())
    if release_host_runtime():
        with _release_host_admission_fence(root) as require_dispatch_open:
            require_dispatch_open()
            transport = client(root)
            try:
                transport.enqueue({'queue_name': scheduler['queue'], 'workflow_name': scheduler['selected_workflow'],
                                   'workflow_id': request.run_id, 'app_version': scheduler['app_version']}, request.run_id)
            finally:
                transport.destroy()
    else:
        transport = client(root)
        try:
            transport.enqueue({'queue_name': scheduler['queue'], 'workflow_name': scheduler['selected_workflow'],
                               'workflow_id': request.run_id, 'app_version': scheduler['app_version']}, request.run_id)
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


def _release_host_frozen(root, run_id, *, expected_identity=None, require_available=True,
                         require_current=True):
    """Validate one retained host Run before DBOS access.

    Effects must still re-admit the frozen request against current source.
    Observation instead authenticates the saved request and its retained host
    binding, so a later legitimate source refresh cannot erase history.
    """
    selected = SelectedExecution(root)
    frozen = selected.load(run_id)
    request = frozen.get('request') if isinstance(frozen, dict) else None
    execution = request.get('execution') if isinstance(request, dict) else None
    graph = frozen.get('graph') if isinstance(frozen, dict) else None
    if (not isinstance(execution, dict) or request.get('run_id') != run_id
            or not isinstance(graph, dict) or graph.get('route') != 'release_version'
            or execution.get('operation_route') != 'release_version'):
        raise RuntimeError('Release host Run is not an exact frozen Release request')
    request_identity = _release_request_identity(execution)
    if expected_identity is not None and request_identity != expected_identity:
        raise RuntimeError('Release host request identity does not match the frozen Release request')
    if require_current:
        # Effects need a second route check immediately before dispatch or
        # recovery so stale source cannot be replayed.
        selected._revalidate(frozen)
    _validate_release_host_binding(
        root, run_id, _release_host_frozen_request_digest(frozen),
        require_available=require_available,
    )
    return frozen, request_identity


def recover_selected_release(root, request):
    """Queue one sealed Release recovery without creating another canonical Run."""
    request = RecoverSelectedRelease.model_validate(request)
    scheduler = _scheduler_identity()
    if release_host_runtime():
        _frozen, identity = _release_host_frozen(
            root, request.run_id, expected_identity=request.request_identity,
        )
    else:
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
    def enqueue_recovery():
        transport = client(root)
        try:
            transport.enqueue({'queue_name': scheduler['queue'], 'workflow_name': scheduler['recovery_workflow'],
                               'workflow_id': transport_id, 'app_version': scheduler['app_version']},
                              request.run_id, identity)
            # Observe the new scheduler identity, never the prior selected Run's
            # cached DBOS workflow result.
            return _observe_recovery_transport(
                transport, transport_id, request.run_id, identity,
                workflow_name=scheduler['recovery_workflow'], queue_name=scheduler['queue'],
            )
        finally:
            transport.destroy()
    if release_host_runtime():
        with _release_host_admission_fence(root) as require_dispatch_open:
            require_dispatch_open()
            recovery_transport_status = enqueue_recovery()
    else:
        recovery_transport_status = enqueue_recovery()
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


def resolve_release_unknown_effect(root, request):
    """Close the sole admitted unknown Release effect through the native guard.

    The native boundary owns all carrier/Journaling checks and its private
    cancellation callback.  This adapter proves the guard before entering the
    helper; the helper then repeats it under the per-Run Journal lock before
    it calls the legitimate DBOS cancellation boundary and writes history.
    """
    request = ResolveReleaseUnknownEffect.model_validate(request)
    from release_unknown_effect_resolution import resolve_release_unknown_effect as resolve
    sealed = request.model_dump()
    preflight = resolve.preflight(Path(root), sealed)
    if isinstance(preflight, dict):
        return preflight
    return resolve(Path(root), sealed)


def cancel_release_unknown_effect_scheduler(root, request):
    """Cancel only the preflighted N15 DBOS workflow and confirm its status.

    This function is private to the native unknown-effect resolver.  It never
    reads or writes DBOS storage directly and is called only after that helper
    has validated its historical carriers and current authority under lock.
    """
    request = ResolveReleaseUnknownEffect.model_validate(request)
    transport = client(root)
    try:
        transport.cancel_workflow(request.run_id)
        queue_status = transport.retrieve_workflow(request.run_id).get_status()
        if getattr(queue_status, 'status', None) != 'CANCELLED':
            raise RuntimeError('old N15 scheduler workflow did not report CANCELLED')
        return {'workflow_run_id': request.run_id, 'scheduler_status': 'CANCELLED'}
    finally:
        transport.destroy()


def _observe_recovery_transport(transport, transport_id, run_id, request_identity, *,
                                workflow_name=RECOVERY_WORKFLOW, queue_name=QUEUE):
    handle = transport.retrieve_workflow(transport_id)
    queue_status = handle.get_status()
    workflow_input = getattr(queue_status, 'input', None)
    if (getattr(queue_status, 'name', None) != workflow_name
            or getattr(queue_status, 'queue_name', None) != queue_name
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


def _selected_public_outcome(frozen, result, run_id):
    """Read the workflow outcome from canonical selected-Run terminal evidence.

    DBOS ``SUCCESS`` proves only that its scheduler wrapper returned.  It is
    never authority for a selected Workflow result, and neither is a nested
    Action terminal.  Older direct result envelopes predate ``terminal_runs``;
    retain their existing public shape unchanged.
    """
    if not isinstance(result, dict):
        return None, "selected result is not a mapping"
    if "terminal_runs" not in result:
        return result.get("outcome"), None
    if result.get("disposition") == "recording_pending":
        return result.get("outcome"), None
    terminal_runs = result.get("terminal_runs")
    request = frozen.get("request") if isinstance(frozen, dict) else None
    execution = request.get("execution") if isinstance(request, dict) else None
    requested_runs = execution.get("requested_runs") if isinstance(execution, dict) else None
    workflow_bindings = [
        row for row in requested_runs if isinstance(row, dict)
        and row.get("requested_run_id") == run_id and row.get("kind") == "workflow"
    ] if isinstance(requested_runs, list) else []
    if not isinstance(terminal_runs, list) or len(workflow_bindings) != 1:
        return "failed", "canonical Workflow terminal evidence is missing or ambiguous"
    candidates = [
        row for row in terminal_runs if isinstance(row, dict) and row.get("run_id") == run_id
        and ("kind" not in row or row.get("kind") == "workflow")
    ]
    if len(candidates) != 1 or candidates[0].get("disposition") != "terminal":
        return "failed", "canonical Workflow terminal evidence is missing or ambiguous"
    outcome = candidates[0].get("outcome")
    if not isinstance(outcome, str) or not outcome:
        return "failed", "canonical Workflow terminal evidence is incomplete"
    return outcome, None


def recover_selected_release_status(root, request):
    request = RecoverSelectedReleaseStatus.model_validate(request)
    scheduler = _scheduler_identity()
    if release_host_runtime():
        _frozen, identity = _release_host_frozen(root, request.run_id, require_current=False)
    else:
        frozen = SelectedExecution(root).load(request.run_id)
        saved = frozen.get('request', {}) if isinstance(frozen, dict) else {}
        execution = saved.get('execution') if isinstance(saved, dict) else None
        if not isinstance(execution, dict) or execution.get('operation_route') != 'release_version':
            raise RuntimeError('recovery status is admitted only for an existing frozen Release Version Run')
        identity = _release_request_identity(execution)
    transport = client(root)
    try:
        transport_status = _observe_recovery_transport(
            transport, request.recovery_transport_handle, request.run_id, identity,
            workflow_name=scheduler['recovery_workflow'], queue_name=scheduler['queue'],
        )
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
    if release_host_runtime():
        # A host status read must not adopt a native/Docker selected Run or
        # reach the host DBOS database before its retained binding is proven.
        # It observes a saved Run rather than re-admitting an effect, so a
        # legitimate later source refresh does not make saved evidence opaque.
        _release_host_frozen(root, request.run_id, require_current=False)
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
            outcome, terminal_reason = _selected_public_outcome(frozen, result, request.run_id)
            response.update({'selected_result': result, 'outcome': outcome,
                             'disposition': result.get('disposition')})
            if terminal_reason is not None:
                response['reason'] = terminal_reason
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
    if release_host_runtime():
        return register_release_host_execution(DBOS, engine, selected_providers=selected_providers)
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


def register_release_host_execution(DBOS, engine, *, selected_providers=None):
    """Register only the two Release workflows in the host scheduler.

    Route and host-binding validation happens inside the DBOS step immediately
    before provider dispatch, so an injected DBOS payload cannot bypass the
    admission-time validation performed by ``enqueue_selected``.
    """
    selected_providers = selected_providers or SelectedNativeProviders(engine.root)

    @DBOS.step(name='release-host-selected-workflow-dispatch')
    def selected_dispatch(run_id):
        _release_host_frozen(engine.root, run_id, require_available=False)
        return selected_providers.dispatch(run_id)

    @DBOS.step(name='release-host-selected-release-recovery')
    def recover_selected_release(run_id, request_identity):
        _release_host_frozen(
            engine.root, run_id, expected_identity=request_identity, require_available=False,
        )
        return selected_providers.recover_release(run_id, request_identity)

    @DBOS.workflow(name=RELEASE_HOST_SELECTED_WORKFLOW)
    def execute_selected(run_id):
        return selected_dispatch(run_id)

    @DBOS.workflow(name=RELEASE_HOST_RECOVERY_WORKFLOW)
    def recover_selected_release_workflow(run_id, request_identity):
        return recover_selected_release(run_id, request_identity)


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


def worker(root, *, agent=None, ready_file=None, implementation_agent=None,
           release_start_token=None):
    """Explicitly started foreground process; no implicit daemon or hook installation."""
    from dbos import DBOS
    root = Path(root).resolve(strict=True)
    if implementation_agent is None and implementation_mock_runtime():
        from implementation_mock_agent import ImplementationMockAgent
        implementation_agent = ImplementationMockAgent(root)
    _, url = database(root)
    default_agent = None if release_host_runtime() else (RemoteAgent() if docker_runtime() else CodexAgent())
    engine = Coordinator(root, agent or default_agent)
    stop = threading.Event()
    scheduler = _scheduler_identity()
    DBOS(config={'name': scheduler['application'], 'system_database_url': url,
                 'run_admin_server': False, 'enable_otlp': False,
                 'application_version': scheduler['app_version'], 'max_executor_threads': 2})
    register_execution(DBOS, engine, selected_providers=SelectedNativeProviders(
        root, implementation_agent=implementation_agent))

    previous = {number: signal.getsignal(number) for number in (signal.SIGINT, signal.SIGTERM)}
    for number in previous:
        signal.signal(number, lambda *_: stop.set())
    health_listener = shutdown_listener = None
    try:
        DBOS.launch()
        DBOS.register_queue(scheduler['queue'], global_concurrency=1, worker_concurrency=1,
                            polling_interval_sec=0.2)
        if ready_file:
            identity = {'state': 'ready',
                'pid': __import__('os').getpid(),
                'application_version': scheduler['app_version'],
                'runtime_fingerprint': runtime_fingerprint(root)}
            if release_host_runtime():
                from release_host_health import start_listener
                identity['start_token'] = release_start_token
                health_listener = start_listener(root, identity)
                from release_host_shutdown import start_listener as start_shutdown_listener
                shutdown_listener = start_shutdown_listener(
                    root, identity, has_work=lambda: _release_host_has_pending_work(root),
                    request_stop=stop.set,
                )
                engine.save(Path(ready_file).with_name('worker.json'), identity)
            engine.save(Path(ready_file), identity)
        stop.wait()
    finally:
        shutdown_incomplete = None
        try:
            for listener in (shutdown_listener, health_listener):
                if listener is None:
                    continue
                try:
                    listener.close()
                # A listener that cannot prove its join leaves shutdown
                # incomplete; DBOS must remain intact and the foreground
                # wrapper must retain stopping/unknown rather than stopped.
                except Exception as error:
                    shutdown_incomplete = error
        finally:
            try:
                if shutdown_incomplete is None:
                    DBOS.destroy()
            finally:
                for number, handler in previous.items():
                    signal.signal(number, handler)
                if shutdown_incomplete is not None:
                    raise shutdown_incomplete
