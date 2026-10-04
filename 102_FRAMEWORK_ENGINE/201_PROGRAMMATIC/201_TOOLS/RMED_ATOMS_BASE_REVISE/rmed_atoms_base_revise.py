"""Canonical coordination Tool. No Agent launcher, Atom writer, or recheck loop."""
from pathlib import Path
import json
import sys
from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter

ROOT = Path(__file__).resolve().parents[4]
PROMPTS = ROOT / '102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW'
sys.path.insert(0, str(PROMPTS))
from workflow_evidence import RunEvidence  # noqa: E402 - repository path bootstrap
from workflow_progress import CHECKS, report_progress  # noqa: E402


class Input(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)


class Describe(Input):
    operation: Literal['describe']


class Run(Input):
    run_id: str = Field(pattern=r'^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$')


class Session(Input):
    app: str = Field(min_length=1)
    uuid: str = Field(min_length=1)


class Start(Run):
    operation: Literal['start']
    request: dict[str, Any]
    author: str
    session: Session
    scope: str = Field(min_length=1)
    timezone: str = 'UTC'


class Selected(Input):
    atom_id: str = Field(min_length=1, max_length=256, pattern=r'^[^\r\n]+$')
    path: str


class Gather(Run):
    operation: Literal['gather']
    selection: list[Selected] = Field(max_length=10000)
    criteria_paths: list[str] = Field(min_length=1, max_length=1000)
    exclusions: list[Any] = Field(default_factory=list)
    blockers: list[Any] = Field(default_factory=list)


class Context(Run):
    operation: Literal['context']
    ordinal: int = Field(ge=0)
    stage: Literal['check', 'fix']


class Submit(Run):
    operation: Literal['submit']
    ordinal: int = Field(ge=0)
    stage: Literal['check', 'fix']
    report: dict[str, Any]
    after_paths: list[str] = Field(default_factory=list, max_length=1000)


class Inspect(Run):
    operation: Literal['status', 'sync', 'report']


class Handoff(Run):
    operation: Literal['handoff']
    note: str = Field(min_length=1)


class Finish(Run):
    operation: Literal['finish']
    outcome: Literal['completed', 'interrupted', 'failed']
    reason: str | None = None


Request = Annotated[Describe | Start | Gather | Context | Submit | Inspect | Handoff | Finish,
                    Field(discriminator='operation')]
ADAPTER = TypeAdapter(Request)


def validate_report(row):
    """Carrier admission only; never substitute for the six agentic checks."""
    if set(row.get('checks', {})) != set(CHECKS):
        raise ValueError('report must include all six check slots, including blocked ones')
    for value in row['checks'].values():
        if not isinstance(value, dict) or value.get('status') not in {'passed', 'failed', 'blocked', 'pending'}:
            raise ValueError('invalid check result')
        if not value.get('evidence'):
            raise ValueError('each check requires evidence or an explicit absence/blocker')
    for field in ('findings', 'blockers', 'corrections', 'rejected_findings',
                  'unresolved_findings', 'fix_blockers'):
        if not isinstance(row.get(field), list):
            raise ValueError(f'report requires {field} list')
    for field in ('findings', 'corrections', 'rejected_findings'):
        if any(not isinstance(item, dict) for item in row[field]):
            raise ValueError(f'{field} entries must be objects')
    if row.get('result') not in {'checked_clean', 'issues', 'blocked',
                                'fixed_not_rechecked', 'replaced_not_rechecked'}:
        raise ValueError('invalid report result')
    # Fail closed on malformed disposition references before persisting input.
    report_progress(row)


def short_status(state):
    result = {key: state[key] for key in ('workflow_name', 'workflow_run_id', 'outcome',
        'gathered', 'progress', 'report_path', 'recording_blockers')}
    result['coverage_gates'] = state.get('coverage_gates', {})
    result['reason'] = state.get('reason')
    result['operator_question'] = next((row['operator_question'] for row in
        result['coverage_gates'].values() if row.get('operator_question')), None)
    return result


def execution_context(store, request):
    state = store.load(request.run_id)
    store._running(state)
    if request.ordinal >= len(state['selection']):
        raise ValueError('ordinal outside frozen selection')
    if request.stage == 'fix':
        context = store.fix_context(request.run_id, request.ordinal)
    else:
        if report_progress(state['reports'][request.ordinal])['check_complete']:
            raise ValueError('initial check already concluded; no recheck in this workflow')
        store._fresh(state, request.ordinal)
        context = {'source': state['selection'][request.ordinal]['source'],
            'report': state['reports'][request.ordinal], 'criteria': state['criteria'],
            'criteria_sha256': state['criteria_sha256']}
    sources = context.get('current_sources', [context['source']])
    context.update(workflow_run_id=request.run_id,
        atom_id=state['selection'][request.ordinal]['atom_id'],
        prompt=(PROMPTS / f'CA-O-{109 if request.stage == "check" else 110}.prompt.md').read_text(),
        source_content=store.path(sources[0]['path']).read_text(),
        current_sources_content=[{'source': source, 'content': store.path(source['path']).read_text()}
                                 for source in sources],
        rule_content=[{'path': row['path'], 'content': store.path(row['path']).read_text()}
                      for row in state['criteria']])
    return context


def run(root: Path, request: Request | dict) -> dict:
    """Execute only the requested coordination operation under one configured root."""
    request = ADAPTER.validate_python(request)
    store = RunEvidence(root)
    if isinstance(request, Describe):
        return {'workflow': 'RMED Atoms Base Revise', 'execution': 'caller-coordinated',
            'steps': {name: (PROMPTS / f'CA-O-{number}.prompt.md').read_text()
                      for name, number in (('gather', 108), ('check', 109), ('fix', 110))},
            'operations': ['start', 'gather', 'context', 'submit', 'status', 'handoff',
                           'finish', 'report', 'sync'],
            'instructions': 'Use only for an Operator-authorized Run. Start, execute gather in '
                'the calling session, submit the selected paths/current criteria, obtain one '
                'check context per Atom, launch fresh reviewers, submit reports, obtain fix '
                'context for reported issues, apply authorized fixes in the caller, submit '
                'corrections, finish. No recheck. sync retries recording only. Ordinals are zero-based.'}
    if isinstance(request, Start):
        bindings = json.loads((PROMPTS / 'source_bindings.json').read_text())
        definition = next(row for row in bindings['sources'] if row['atom_id'] == 'CA-O-104')
        state = store.start(request.run_id, request.request, author=request.author,
            session=request.session.model_dump(), scope=request.scope, timezone=request.timezone,
            definition=definition)
    elif isinstance(request, Gather):
        state = store.gather(request.run_id, [row.model_dump() for row in request.selection],
            request.criteria_paths, exclusions=request.exclusions, blockers=request.blockers)
    elif isinstance(request, Context):
        return execution_context(store, request)
    elif isinstance(request, Submit):
        validate_report(request.report)
        state = store.record(request.run_id, request.ordinal, request.report,
                             stage=request.stage, after_paths=request.after_paths)
    elif isinstance(request, Handoff):
        state = store.handoff(request.run_id, request.note)
    elif isinstance(request, Finish):
        state = store.finish(request.run_id, request.outcome, reason=request.reason)
    elif request.operation == 'sync':
        state = store.sync(request.run_id)
    else:
        state = store.load(request.run_id)
        if request.operation == 'report':
            return {**short_status(state), 'markdown': store.path(state['report_path']).read_text()}
    return short_status(state)
