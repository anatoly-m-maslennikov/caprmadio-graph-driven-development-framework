"""Persist one gather/check/fix Run. Dispatch and Atom edits belong to the caller.

The internal state is a recovery cache; confirmed execution events belong to the
shared Project Journal. Markdown reports are full projections of saved evidence.
No function in this module evaluates or edits an Atom.
"""
from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import uuid
from zoneinfo import ZoneInfo

TOOLS = Path(__file__).resolve().parents[5] / '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS'
sys.path.insert(0, str(TOOLS))
from project_runtime import atomic_tempfile  # noqa: E402 - repository path bootstrap
from work_journal import (append_sealed_events, configured_journal_root,  # noqa: E402
                          with_event_digest, validate_sealed_event, validate_partition)
from workflow_progress import report_progress, summarize_progress  # noqa: E402

WORKFLOW = 'RMED Atoms Base Revise'
RUN_ID = re.compile(r'[A-Za-z0-9][A-Za-z0-9_-]{0,127}\Z')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False).encode()


def block(value):
    text = encoded(value).decode()
    fence = '`' * max(3, max((len(x) + 1 for x in re.findall(r'`+', text)), default=3))
    return f'{fence}json\n{text}\n{fence}\n'


def render_report(state):
    """Full evidence, including pending records; never truncate or invent verdicts."""
    lines = ['# Run\n', block({key: state[key] for key in (
        'workflow_name', 'workflow_run_id', 'definition', 'started_at', 'updated_at',
        'outcome', 'recording_blockers')}), '## Selection\n',
        block({key: state[key] for key in ('request', 'selection', 'gathered', 'exclusions')}),
        '## Rules\n', block(state['criteria']), '## Results\n', block(state['progress']),
        '## Atom Reports\n']
    if not state['selection']:
        lines.append('No Atoms selected.\n' if state['gathered'] else 'Selection pending.\n')
    for i, atom in enumerate(state['selection']):
        lines += [f'### {i + 1}: {atom["atom_id"]}\n', block({
            'source': atom['source'], 'report': state['reports'][i] or {'result': 'pending'},
            'after': state['after'][i], 'history': state['history'][i]})]
    lines += ['## Remaining Work\n', block({
        'pending': [i for i, row in enumerate(state['reports']) if not report_progress(row)['complete']],
        'gather_blockers': state['gather_blockers'], 'handoffs': state['handoffs'],
        'reason': state.get('reason'), 'recording_blockers': state['recording_blockers']}),
        '## Journal\n', block({'path': state['journal'], 'workflow_run_id': state['workflow_run_id'],
            'events': state['events']})]
    return '\n'.join(lines)


class RunEvidence:
    def __init__(self, root, *, max_file_bytes=8 * 1024 * 1024):
        self.root = Path(root).resolve(strict=True)
        self.max_file_bytes = max_file_bytes

    def path(self, relative):
        path = Path(relative)
        if path.is_absolute() or '..' in path.parts or not path.parts:
            raise ValueError('unsafe repository-relative path')
        current = self.root
        for part in path.parts:
            if part == '.env' or part.startswith('.env.') or part.endswith('.env'):
                raise ValueError('secret carriers are outside workflow scope')
            current /= part
            if current.is_symlink():
                raise ValueError('symlink carriers are outside workflow scope')
        return current

    def observe(self, relative):
        path = self.path(relative)
        with path.open('rb') as handle:
            raw = handle.read(self.max_file_bytes + 1)
        if len(raw) > self.max_file_bytes:
            raise ValueError('file exceeds admitted read limit')
        return {'path': str(path.relative_to(self.root)), 'sha256': digest(raw)}

    def _directory(self, run_id):
        if not RUN_ID.fullmatch(run_id):
            raise ValueError('unsafe workflow run id')
        return self.path(f'.caprmedio_tmp/rmed-base-revise/{run_id}')

    @contextmanager
    def _lock(self, run_id):
        directory = self._directory(run_id)
        directory.mkdir(parents=True, exist_ok=True)
        lock = self.path(str((directory / '.lock').relative_to(self.root)))
        with lock.open('a') as handle:
            try:
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as error:
                raise ValueError('run busy; retry the same request') from error
            try:
                yield
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)

    def _atomic(self, path, raw):
        self.path(str(path.relative_to(self.root)))
        self.path('.caprmedio_tmp/rmed-base-revise/atomic')
        descriptor, name = atomic_tempfile(path, 'rmed-base-revise', repository=self.root)
        try:
            with os.fdopen(descriptor, 'wb') as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(name, path)
        finally:
            if os.path.exists(name):
                os.unlink(name)

    def _save(self, state):
        directory = self._directory(state['workflow_run_id'])
        self._atomic(directory / 'progress.json', encoded(state))
        for i, row in enumerate(state['reports']):
            if row is not None:
                self._atomic(directory / 'reports' / f'{i + 1:04}.json', encoded(row))

    def load(self, run_id):
        path = self._directory(run_id) / 'progress.json'
        self.path(str(path.relative_to(self.root)))
        return json.loads(path.read_text())

    def _write_report(self, state):
        self._atomic(self.path(state['report_path']), render_report(state).encode())

    def _sync(self, state):
        state['recording_blockers'] = []
        # Recovery state and immutable outbox are saved before external effects.
        self._save(state)
        for entry in state['events']:
            if entry['receipt'] is not None:
                continue
            try:
                self.path(state['journal'])
                self.path('.caprmedio_runtime')
                entry['receipt'] = append_sealed_events(self.root, [entry['event']],
                    author=state['author'], local_date=entry['event']['occurred_at'][:10],
                    timezone=state['timezone'])[0]
            except (OSError, RuntimeError, ValueError) as error:
                state['recording_blockers'].append({'stage': 'journal',
                    'event_id': entry['event']['event_id'], 'error': str(error)})
                break  # Retain event order; retry storage only, never the Action.
        self._save(state)
        try:
            self._write_report(state)
        except (OSError, ValueError, RuntimeError) as error:
            state['recording_blockers'].append({'stage': 'report', 'error': str(error)})
        self._save(state)
        return deepcopy(state)

    def sync(self, run_id):
        with self._lock(run_id):
            return self._sync(self.load(run_id))

    def _event(self, state, event, step, outcome, details):
        now = datetime.now(ZoneInfo(state['timezone'])).isoformat()
        value = with_event_digest({'schema_version': 4, 'kind': 'workflow_execution',
            'event_id': str(uuid.uuid4()), 'action_id': state['workflow_run_id'],
            'event': event, 'author': state['author'], 'occurred_at': now,
            'llm_session': state['session'], 'structural_scope': state['scope'],
            'workflow_run_id': state['workflow_run_id'], 'workflow_name': WORKFLOW,
            'step': step, 'outcome': outcome, 'report_path': state['report_path'], 'details': details})
        validate_sealed_event(value)
        state['events'].append({'event': value, 'receipt': None})
        state['updated_at'] = now

    def start(self, run_id, request, *, author, session, scope, timezone='UTC', definition=None):
        with self._lock(run_id):
            path = self._directory(run_id) / 'progress.json'
            if path.exists():
                raise ValueError('run already exists; resume it instead')
            now = datetime.now(ZoneInfo(timezone)).isoformat()
            validate_partition(author, now[:10], timezone)
            journal = configured_journal_root(self.root).as_posix()
            self.path(journal)
            state = {'workflow_name': WORKFLOW, 'workflow_run_id': run_id,
                'request': request, 'author': author, 'session': session, 'scope': scope,
                'timezone': timezone, 'definition': definition or {'atom_id': 'CA-O-104'},
                'started_at': now, 'updated_at': now, 'outcome': 'running',
                'report_path': f'tmp/{WORKFLOW}/{run_id}.md', 'journal': journal,
                'selection': [], 'exclusions': [], 'gathered': False, 'gather_blockers': [],
                'criteria': [], 'criteria_sha256': None, 'reports': [], 'after': [], 'history': [],
                'fix_admissions': {}, 'handoffs': [], 'events': [], 'recording_blockers': [],
                'progress': {'total': 0, 'reported': 0, 'checked': 0, 'completed': 0,
                             'complete': False, 'states': {}}}
            self._event(state, 'started', 'run', 'running', {'request': request})
            return self._sync(state)

    @staticmethod
    def _running(state):
        if state['outcome'] != 'running':
            raise ValueError('run is terminal; preserve its evidence')

    def gather(self, run_id, selection, criteria_paths, *, exclusions=None, blockers=None):
        with self._lock(run_id):
            state = self.load(run_id)
            self._running(state)
            if state['gathered']:
                raise ValueError('selection is frozen; use the saved queue')
            if not criteria_paths:
                raise ValueError('current criteria are required')
            if len({row['path'] for row in selection}) != len(selection):
                raise ValueError('duplicate source in selection')
            state['selection'] = [{'atom_id': row['atom_id'], 'source': self.observe(row['path'])}
                                  for row in selection]
            state['criteria'] = [self.observe(path) for path in criteria_paths]
            state['criteria_sha256'] = digest(encoded(state['criteria']))
            state['exclusions'], state['gather_blockers'] = exclusions or [], blockers or []
            state['reports'] = [None for _ in selection]
            state['after'] = [[] for _ in selection]
            state['history'] = [[] for _ in selection]
            state['gathered'] = True
            state['progress'] = summarize_progress(state['reports'])
            if state['gather_blockers']:
                state['progress']['complete'] = False
            self._event(state, 'progressed', 'gather', 'blocked' if blockers else 'ready',
                        {'count': len(selection), 'blockers': blockers or []})
            return self._sync(state)

    def _fresh(self, state, ordinal, *, source=True):
        for binding in state['criteria']:
            if self.observe(binding['path']) != binding:
                raise ValueError('stale criteria; old report remains historical')
        if source:
            binding = state['selection'][ordinal]['source']
            if self.observe(binding['path']) != binding:
                raise ValueError('stale source; old report remains historical')

    def fix_context(self, run_id, ordinal):
        with self._lock(run_id):
            state = self.load(run_id)
            self._running(state)
            row = state['reports'][ordinal]
            if not row or report_progress(row)['complete']:
                raise ValueError('no pending fix')
            self._fresh(state, ordinal, source=False)
            current_sources = state['after'][ordinal] or [state['selection'][ordinal]['source']]
            for source in current_sources:
                if self.observe(source['path']) != source:
                    raise ValueError('stale source; old report remains historical')
            state['fix_admissions'][str(ordinal)] = digest(encoded(row))
            self._save(state)
            return {'source': state['selection'][ordinal]['source'], 'report': row,
                    'current_sources': current_sources,
                    'criteria': state['criteria'], 'criteria_sha256': state['criteria_sha256']}

    def record(self, run_id, ordinal, report, *, stage, after_paths=None):
        with self._lock(run_id):
            state = self.load(run_id)
            if type(ordinal) is not int or ordinal < 0 or ordinal >= len(state['reports']):
                raise ValueError('ordinal outside frozen selection')
            previous = state['reports'][ordinal]
            if previous == report:
                return self._sync(state)  # Retry the acknowledgement, not the effect.
            self._running(state)
            if stage not in {'check', 'fix'}:
                raise ValueError('stage must be check or fix')
            atom = state['selection'][ordinal]
            for key, expected in (('workflow_run_id', run_id), ('source', atom['source']),
                ('atom_id', atom['atom_id']), ('criteria_sha256', state['criteria_sha256'])):
                if report.get(key) != expected:
                    raise ValueError(f'report {key} does not match admitted input')
            self._fresh(state, ordinal, source=stage == 'check')
            self._preserve_initial_evidence(state, ordinal, previous, report, stage, after_paths)
            if previous:
                state['history'][ordinal].append(previous)
            state['reports'][ordinal] = deepcopy(report)
            state['progress'] = summarize_progress(state['reports'])
            if state['gather_blockers']:
                state['progress']['complete'] = False
            self._event(state, 'progressed', stage, report['result'], {'ordinal': ordinal})
            return self._sync(state)

    def _preserve_initial_evidence(self, state, ordinal, previous, report, stage, after_paths):
        if stage == 'check' and previous:
            self._preserve_check(previous, report)
        if stage == 'fix':
            if state['fix_admissions'].get(str(ordinal)) != digest(encoded(previous)):
                raise ValueError('obtain fresh fix context before applying corrections')
            for field in ('checks', 'findings', 'blockers', 'coverage_gaps'):
                if report.get(field) != previous.get(field):
                    raise ValueError('fix must preserve initial check evidence')
            for field in ('corrections', 'rejected_findings'):
                saved = previous.get(field, [])
                if report.get(field, [])[:len(saved)] != saved:
                    raise ValueError('retain recorded finding dispositions when continuing')
            if report.get('corrections') and not after_paths:
                raise ValueError('applied corrections require after source observations')
            state['after'][ordinal] = [self.observe(path) for path in (after_paths or [])]

    @staticmethod
    def _preserve_check(previous, report):
        if report_progress(previous)['check_complete']:
            raise ValueError('initial check already concluded; no recheck')
        for name, result in previous['checks'].items():
            if result['status'] in {'passed', 'failed'} and report['checks'].get(name) != result:
                raise ValueError('completed initial checks are immutable; no recheck')
        saved = previous.get('findings', [])
        if report.get('findings', [])[:len(saved)] != saved:
            raise ValueError('retain initial findings when continuing unfinished checks')

    def handoff(self, run_id, note):
        with self._lock(run_id):
            state = self.load(run_id)
            self._running(state)
            if not isinstance(note, str) or not note.strip():
                raise ValueError('handoff requires remaining work')
            if state['handoffs'] and state['handoffs'][-1] == note:
                return self._sync(state)
            state['handoffs'].append(note)
            self._event(state, 'progressed', 'handoff', 'continuing', {'note': note})
            return self._sync(state)

    def finish(self, run_id, outcome, *, reason=None):
        with self._lock(run_id):
            state = self.load(run_id)
            if outcome not in {'completed', 'interrupted', 'failed'}:
                raise ValueError('invalid terminal outcome')
            if state['outcome'] == outcome:
                return self._sync(state)
            self._running(state)
            if outcome == 'completed' and not state['progress']['complete']:
                raise ValueError('selection still has unfinished work')
            if outcome != 'completed' and not reason:
                raise ValueError('non-completion requires a reason')
            state['outcome'], state['reason'] = outcome, reason
            self._event(state, outcome, 'run', outcome, {'reason': reason})
            return self._sync(state)
