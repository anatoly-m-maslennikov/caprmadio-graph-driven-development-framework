"""Constrained executor using existing Workflow prompts, report admission and Journal."""
import hashlib
import json
from pathlib import Path
import re
import sys
import tomllib

from contracts import AgentOutput, Enqueue

TOOLS = Path(__file__).resolve().parents[2] / '201_TOOLS'
sys.path.insert(0, str(TOOLS / 'RMED_ATOMS_BASE_REVISE'))
sys.path.insert(0, str(TOOLS / 'VALIDATE_ATOMS'))
from rmed_atoms_base_revise import run as coordinate, validate_report, PROMPTS  # noqa: E402
from workflow_evidence import RunEvidence, encoded  # noqa: E402
from workflow_progress import report_progress  # noqa: E402
from validate_atoms_workers.parsing import parse_carrier, CarrierError  # noqa: E402
from coverage import assess  # noqa: E402
from replacement import Replacement  # noqa: E402
from runtime_config import control_directory  # noqa: E402


class Interrupted(RuntimeError):
    """An admitted Run needs an Operator decision or recovery evidence."""


def execute_phase(run_id, phase, count, action, coverage):
    """Account for unfinished work without hiding the original Action failure."""
    try:
        for ordinal in range(count):
            action(run_id, ordinal)
    except (ValueError, RuntimeError, OSError) as error:
        coverage(run_id, phase, str(error))
        raise
    coverage(run_id, phase)


def summary(body):
    match = re.search(r'^# Summary\s*\n(.*?)(?=^## |\Z)', body, re.MULTILINE | re.DOTALL)
    if not match:
        raise Interrupted('Structured Summary is required for automated fixes')
    return match.group(1).strip()


def runtime_fingerprint(root=None):
    """Bind the selected implementation and Action prompts, not a second description."""
    app = Path(__file__).resolve().parent
    project_root = Path(root).resolve(strict=True) if root is not None else app.parents[3]
    paths = [app / name for name in ('contracts.py', 'engine.py', 'agent.py', 'backend.py',
        'coverage.py', 'replacement.py', 'remote_agent.py', 'runtime_config.py')]
    paths.extend(app / 'docker' / name for name in (
        'agent_service.py', 'entrypoint.py', 'Dockerfile', 'compose.yaml',
        'auth.compose.yaml', 'mock.compose.yaml'))
    paths.extend(app.parents[3] / name for name in ('pyproject.toml', 'uv.lock'))
    paths.extend(PROMPTS / f'CA-O-{number}.prompt.md' for number in (108, 109, 110))
    manifest = json.loads((PROMPTS / 'source_bindings.json').read_text())
    definition = next(row for row in manifest['sources'] if row['atom_id'] == 'CA-O-104')
    definition_path = RunEvidence(project_root).path(definition['path'])
    observations = [
        {'path': str(path.relative_to(app.parents[3])),
         'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
        for path in paths]
    observations.append({'path': definition['path'],
        'sha256': hashlib.sha256(definition_path.read_bytes()).hexdigest()})
    manifest_path = PROMPTS / 'source_bindings.json'
    observations.append({'path': str(manifest_path.relative_to(app.parents[3])),
        'sha256': hashlib.sha256(manifest_path.read_bytes()).hexdigest()})
    return hashlib.sha256(encoded(observations)).hexdigest()


class Coordinator:
    def __init__(self, root, agent):
        self.root = Path(root).resolve(strict=True)
        self.store, self.agent = RunEvidence(self.root), agent

    def run_directory(self, run_id):
        # Validate the ID through the existing carrier boundary.
        self.store._directory(run_id)
        return self.store.path(f'{control_directory()}/runs/{run_id}')

    def save(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.store._atomic(path, encoded(value))

    def freeze(self, request):
        request = Enqueue.model_validate(request)
        path = self.run_directory(request.run_id) / 'request.json'
        if path.exists():
            saved = json.loads(path.read_text())
            if saved['request'] != request.model_dump():
                raise ValueError('Run ID already binds a different request')
            return saved
        if len({row.path for row in request.selection}) != len(request.selection):
            raise ValueError('Duplicate selected path')
        if len({row.atom_id for row in request.selection}) != len(request.selection):
            raise ValueError('Duplicate selected Atom ID')
        registry = self.store.path('.caprmedio_caprmedio/operators_registry.toml')
        if registry.is_file():
            names = {row['name'] for row in tomllib.loads(registry.read_text()).get('operators', [])}
            if request.author not in names:
                raise ValueError('Author is not in operators_registry')
        observations = [self.store.observe(row.path) for row in request.selection]
        for row in request.selection:
            self.validate_selected(row)
        rules = [self.store.observe(path) for path in request.criteria_paths]
        value = {'request': request.model_dump(), 'selection_bindings': observations,
                 'rule_bindings': rules, 'runtime_fingerprint': runtime_fingerprint(self.root)}
        self.save(path, value)
        return value

    def validate_selected(self, row):
        """Known out-of-scope sources are rejected; malformed candidates remain checkable."""
        path = self.store.path(row.path)
        try:
            parsed = parse_carrier(path.read_bytes(), path)
        except CarrierError:
            return
        metadata = parsed.metadata
        if metadata.get('atom_id') and metadata['atom_id'] != row.atom_id:
            raise ValueError('Selected Atom ID differs from its carried identity')
        if metadata.get('status') and str(metadata['status']).lower() != 'active':
            raise ValueError('Base Revise selects active Atoms')
        if metadata.get('content_role') and metadata['content_role'] not in (
                'Requirement', 'Method', 'Evaluation', 'Delivery'):
            raise ValueError('Base Revise selects RMED Atoms')

    def request(self, run_id):
        value = json.loads((self.run_directory(run_id) / 'request.json').read_text())
        if value['runtime_fingerprint'] != runtime_fingerprint(self.root):
            raise Interrupted('Action prompts or implementation changed after enqueue')
        return Enqueue.model_validate(value['request']), value

    def gather(self, run_id):
        request, frozen = self.request(run_id)
        try:
            existing = self.store.load(run_id)
            if existing['gathered']:
                return coordinate(self.root, {'operation': 'status', 'run_id': run_id})
        except FileNotFoundError:
            pass
        for source in frozen['selection_bindings'] + frozen['rule_bindings']:
            if self.store.observe(source['path']) != source:
                raise Interrupted('Source or rule changed after enqueue')
        try:
            state = self.store.load(run_id)
        except FileNotFoundError:
            coordinate(self.root, {'operation': 'start', 'run_id': run_id,
                'request': request.model_dump(), 'author': request.journal_author or request.author,
                'session': {'app': 'workflow-orchestrator', 'uuid': run_id},
                'scope': request.scope, 'timezone': 'Asia/Tbilisi'})
            state = self.store.load(run_id)
        if not state['gathered']:
            coordinate(self.root, {'operation': 'gather', 'run_id': run_id,
                'selection': [row.model_dump() for row in request.selection],
                'criteria_paths': request.criteria_paths})
        return coordinate(self.root, {'operation': 'status', 'run_id': run_id})

    def dispatch(self, run_id, ordinal, phase):
        request, _ = self.request(run_id)
        folder = self.run_directory(run_id) / f'{ordinal}-{phase}'
        folder.mkdir(parents=True, exist_ok=True)
        accepted = folder / 'accepted.json'
        if accepted.exists():
            return json.loads(accepted.read_text())
        if (folder / 'intent.json').exists():
            raise Interrupted('Unacknowledged Agent dispatch; reconcile before retry')
        context = coordinate(self.root, {'operation': 'context', 'run_id': run_id,
                                        'ordinal': ordinal, 'stage': phase})
        context['confidence_threshold'] = request.confidence_threshold
        context['allow_fixes'] = request.allow_fixes
        context['allow_replacements'] = request.allow_replacements
        self.save(folder / 'intent.json', {'context': context, 'phase': phase})
        output = AgentOutput.model_validate(self.agent.execute(
            context, phase, folder, request.agent_timeout_seconds)).model_dump()
        if output['confidence'] < request.confidence_threshold:
            raise Interrupted('Agent confidence is below requested threshold')
        report = json.loads(output['report_json'])
        validate_report(report)
        for key in ('workflow_run_id', 'atom_id', 'source', 'criteria_sha256'):
            if report.get(key) != context.get(key):
                raise Interrupted(f'Agent report changed {key}')
        if phase == 'check' and output['candidate_content'] is not None:
            raise Interrupted('Check returned an edit proposal')
        value = {'context': context, 'report': report, 'candidate_content': output['candidate_content']}
        self.save(accepted, value)
        return value

    def check(self, run_id, ordinal):
        state = self.store.load(run_id)
        if report_progress(state['reports'][ordinal])['check_complete']:
            return state['reports'][ordinal]
        value = self.dispatch(run_id, ordinal, 'check')
        if value['report']['result'] not in ('checked_clean', 'issues', 'blocked'):
            raise Interrupted('Invalid check phase result')
        coordinate(self.root, {'operation': 'submit', 'run_id': run_id, 'ordinal': ordinal,
                              'stage': 'check', 'report': value['report']})
        return value['report']

    def admit_candidate(self, value):
        context, candidate = value['context'], value['candidate_content']
        before = context['source_content'].encode()
        raw = candidate.encode()
        if len(raw) > self.store.max_file_bytes:
            raise Interrupted('Oversized candidate')
        path = self.store.path(context['source']['path'])
        previous, proposed = parse_carrier(before, path), parse_carrier(raw, path)
        if proposed.metadata.get('atom_id') != context['atom_id'] or proposed.metadata.get('atom_id') != previous.metadata.get('atom_id'):
            raise Interrupted('Changed Atom identity requires replacement permission')
        if summary(previous.body) != summary(proposed.body):
            raise Interrupted('Changed Summary requires replacement permission')
        if proposed.metadata.get('version') != previous.metadata.get('version'):
            raise Interrupted('Version-changing fix requires a governed revision-history transition')
        for key in ('status', 'current_scope_unit', 'content_role'):
            if proposed.metadata.get(key) != previous.metadata.get(key):
                raise Interrupted(f'Changed {key} is outside this fix permission')
        if raw != before and proposed.metadata.get('updated_at') == previous.metadata.get('updated_at'):
            raise Interrupted('Changed candidate requires updated_at refresh')
        return path, raw

    def fix(self, run_id, ordinal):
        state = self.store.load(run_id)
        if report_progress(state['reports'][ordinal])['complete']:
            return state['reports'][ordinal]
        request, _ = self.request(run_id)
        if not request.allow_fixes:
            raise Interrupted('Fixes were not delegated; findings remain recorded')
        if not report_progress(state['reports'][ordinal])['check_complete']:
            raise Interrupted('Initial check has unfinished coverage')
        value = self.dispatch(run_id, ordinal, 'fix')
        report = value['report']
        for field in ('checks', 'findings', 'blockers', 'coverage_gaps'):
            if report.get(field) != value['context']['report'].get(field):
                raise Interrupted('Fix changed initial check evidence')
        if report['result'] not in ('fixed_not_rechecked', 'replaced_not_rechecked') or not report_progress(report)['complete']:
            raise Interrupted('Fix did not account for every finding')
        if report['result'] == 'replaced_not_rechecked':
            after_paths = self.apply_replacement(run_id, ordinal, value)
        else:
            after_paths = self.apply_candidate(value)
        if report.get('corrections') and not after_paths:
            raise Interrupted('Corrections require an admitted candidate')
        coordinate(self.root, {'operation': 'submit', 'run_id': run_id, 'ordinal': ordinal,
                              'stage': 'fix', 'report': report, 'after_paths': after_paths})
        return report

    def apply_replacement(self, run_id, ordinal, value):
        request, _ = self.request(run_id)
        if not request.allow_fixes or not request.allow_replacements:
            raise Interrupted('Replacement was not delegated; set allow_replacements=true')
        candidate = value['candidate_content']
        if candidate is None:
            raise Interrupted('Replacement requires a complete candidate')
        context = value['context']
        path = self.store.path(context['source']['path'])
        previous = parse_carrier(context['source_content'].encode(), path)
        proposed = parse_carrier(candidate.encode(), path)
        if len(candidate.encode()) > self.store.max_file_bytes:
            raise Interrupted('Oversized candidate')
        if proposed.metadata.get('atom_id') != previous.metadata.get('atom_id'):
            raise Interrupted('Replacement Agent must retain the input ID; the executor allocates its successor')
        for key in ('status', 'current_scope_unit', 'content_role', 'local_tier', 'global_tier'):
            if proposed.metadata.get(key) != previous.metadata.get(key):
                raise Interrupted(f'Changed {key} is outside this fix permission')
        if summary(previous.body) == summary(proposed.body):
            raise Interrupted('Replacement requires a changed Summary, not an ordinary revision')
        for binding in context['criteria']:
            if self.store.observe(binding['path']) != binding:
                raise Interrupted('Rules changed before replacement admission')
        evidence = Replacement(self, run_id, ordinal).apply(value, request, summary(proposed.body))
        value['report']['replacement'] = evidence
        return [evidence['archived']['path'], evidence['successor']['path']]

    def apply_candidate(self, value):
        """Reconcile the before/after hashes before the sole source write."""
        after_paths = []
        if value['candidate_content'] is not None:
            path, raw = self.admit_candidate(value)
            before = value['context']['source']
            after = hashlib.sha256(raw).hexdigest()
            for binding in value['context']['criteria']:
                if self.store.observe(binding['path']) != binding:
                    raise Interrupted('Rules changed before edit admission')
            current = self.store.observe(before['path'])['sha256']
            if current not in (before['sha256'], after):
                raise Interrupted('Source changed before edit admission')
            if current == before['sha256']:
                self.store._atomic(path, raw)
            after_paths = [before['path']]
        return after_paths

    def finish(self, run_id, outcome='completed', reason=None):
        return coordinate(self.root, {'operation': 'finish', 'run_id': run_id,
                                     'outcome': outcome, 'reason': reason})

    def coverage_gate(self, run_id, phase, failure_reason=None):
        request, frozen = self.request(run_id)
        state = self.store.load(run_id)
        gate = state.get('coverage_gates', {}).get(phase)
        if gate is None:
            gate = assess(request, frozen, state, phase)
            if failure_reason:
                gate['result'] = 'ask_operator'
                question = gate['operator_question'] or 'How should we resolve this failed Step?'
                gate['operator_question'] = f'{question} Action failure: {failure_reason}'
            self.store.record_coverage(run_id, gate)
        if gate['result'] != 'covered':
            raise Interrupted(gate['operator_question'])
        return gate

    def execute(self, run_id):
        try:
            self.gather(run_id)
            state = self.store.load(run_id)
            if state['outcome'] != 'running':
                return coordinate(self.root, {'operation': 'status', 'run_id': run_id})
            self.coverage_gate(run_id, 'gather')
            execute_phase(run_id, 'check', len(state['selection']), self.check, self.coverage_gate)
            execute_phase(run_id, 'fix', len(state['selection']), self.fix, self.coverage_gate)
            return self.finish(run_id)
        except (ValueError, RuntimeError, OSError) as error:
            try:
                return self.finish(run_id, 'interrupted', str(error))
            except FileNotFoundError:
                self.save(self.run_directory(run_id) / 'blocked.json', {'reason': str(error)})
                return {'workflow_run_id': run_id, 'outcome': 'interrupted', 'reason': str(error)}
