"""Mock Agents; the DBOS integration uses a real SQLite queue in separate processes."""
from copy import deepcopy
import json
import os
from pathlib import Path
import subprocess
import sys
import signal
import tempfile
import time
import unittest

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
from contracts import Enqueue  # noqa: E402
from engine import Coordinator, Interrupted  # noqa: E402


def report(context, issues=False):
    result = {key: context[key] for key in ('workflow_run_id', 'atom_id', 'source', 'criteria_sha256')}
    result.update(checks={name: {'status': 'passed', 'evidence': 'mock quotation'}
                          for name in ('properties', 'cce', 'scope', 'claim', 'details', 'summary')},
                  findings=[], blockers=[], corrections=[], unresolved_findings=[],
                  rejected_findings=[], fix_blockers=[], coverage_gaps=[], result='checked_clean')
    if issues:
        result['checks']['cce']['status'] = 'failed'
        result.update(findings=[{'id': 'f1', 'check': 'cce', 'evidence': 'mock quote'}],
                      unresolved_findings=[{'finding_id': 'f1'}], result='issues')
    return result


class MockAgent:
    def __init__(self, issues=False):
        self.issues, self.calls = issues, []

    def execute(self, context, phase, directory, timeout):
        self.calls.append(phase)
        if phase == 'check':
            return {'report_json': json.dumps(report(context, self.issues)),
                    'candidate_content': None, 'confidence': 99.0}
        saved = deepcopy(context['report'])
        saved.update(result='fixed_not_rechecked', corrections=[{'finding_id': 'f1', 'change': 'mock fix'}],
                     unresolved_findings=[])
        candidate = context['source_content'].replace('bad wording', 'good wording').replace(
            '2026-10-01T00:00:00Z', '2026-10-03T15:30:00Z')
        return {'report_json': json.dumps(saved), 'candidate_content': candidate, 'confidence': 99.0}


class OrchestratorTests(unittest.TestCase):
    def setUp(self):
        temporary = APP.parents[3] / '.caprmedio_tmp/tests/workflow-orchestrator'
        temporary.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        control = self.root / '.caprmedio_caprmedio'
        control.mkdir()
        from engine import PROMPTS
        bindings = json.loads((PROMPTS / 'source_bindings.json').read_text())
        definition = next(row['path'] for row in bindings['sources'] if row['atom_id'] == 'CA-O-104')
        self.definition = self.root / definition
        self.definition.parent.mkdir(parents=True, exist_ok=True)
        self.definition.write_bytes((APP.parents[3] / definition).read_bytes())
        (control / 'caprmedio_project_settings.toml').write_text(
            '[paths]\ncontrol_root=".caprmedio_caprmedio"\njournal_root=".caprmedio_caprmedio/_journal"\n')
        (self.root / 'atom.md').write_text(
            '---\natom_id: MOCK-R-1\nversion: 1\nstatus: Active\nupdated_at: "2026-10-01T00:00:00Z"\n---\n'
            '# Summary\nA stable summary\n\n## Scope\nMOCK\n\n## Claim\nbad wording\n')
        (self.root / 'rules.md').write_text('mock rules')
        self.request = Enqueue(run_id='mock-run', selection=[{'atom_id': 'MOCK-R-1', 'path': 'atom.md'}],
                               criteria_paths=['rules.md'], author='mock-operator', scope='MOCK',
                               confidence_threshold=90.0, allow_fixes=True)

    def test_runtime_binding_uses_selected_project_definition(self):
        from engine import runtime_fingerprint
        engine = Coordinator(self.root, MockAgent())
        engine.freeze(self.request)
        original = runtime_fingerprint(self.root)
        self.definition.write_text(self.definition.read_text() + '\nChanged mock Workflow\n')
        self.assertNotEqual(original, runtime_fingerprint(self.root))
        with self.assertRaisesRegex(Interrupted, 'changed after enqueue'):
            engine.request(self.request.run_id)

    def test_prompt_report_example_uses_the_production_contract(self):
        from engine import PROMPTS, validate_report
        prompt = (PROMPTS / 'CA-O-109.prompt.md').read_text()
        example = json.loads(prompt.split('```json\n', 1)[1].split('```', 1)[0])
        validate_report(example)
        self.assertIn('passed | failed | blocked | pending', prompt)
        example['checks']['claim']['status'] = 'pass'
        with self.assertRaisesRegex(ValueError, 'invalid check result'):
            validate_report(example)
        gather = (PROMPTS / 'CA-O-108.prompt.md').read_text()
        self.assertIn('actual Project Operator registry', gather)
        self.assertIn('Status admission rules', gather)
        fix = (PROMPTS / 'CA-O-110.prompt.md').read_text()
        self.assertIn('Findings carry id', fix)

    def test_local_evidence_in_criteria_is_bound_and_given_to_agent(self):
        control = self.root / '.caprmedio_caprmedio'
        registry = '.caprmedio_caprmedio/operators_registry.toml'
        structure = '.caprmedio_caprmedio/project_structure.toml'
        (control / 'operators_registry.toml').write_text(
            '[[operators]]\nname="mock-operator"\nrole="project owner"\n')
        (control / 'project_structure.toml').write_text(
            '[[scope_units]]\nscope_unit_name="MOCK"\n')
        (self.root / 'status.md').write_text('Requirement Status: Draft, Active, Archived')
        request = self.request.model_copy(update={'criteria_paths': [
            'rules.md', registry, structure, 'status.md']})

        class EvidenceAgent(MockAgent):
            def execute(self, context, phase, directory, timeout):
                material = {row['path']: row['content'] for row in context['rule_content']}
                assert 'mock-operator' in material[registry]
                assert 'MOCK' in material[structure]
                assert 'Active' in material['status.md']
                return super().execute(context, phase, directory, timeout)

        engine = Coordinator(self.root, EvidenceAgent())
        frozen = engine.freeze(request)
        self.assertEqual(len(frozen['rule_bindings']), 4)
        self.assertEqual(engine.execute(request.run_id)['outcome'], 'completed')

    def test_clean_run_no_fix_no_recheck(self):
        agent = MockAgent()
        engine = Coordinator(self.root, agent)
        engine.freeze(self.request)
        result = engine.execute(self.request.run_id)
        self.assertEqual(result['outcome'], 'completed')
        self.assertEqual(agent.calls, ['check'])
        gates = engine.store.load(self.request.run_id)['coverage_gates']
        self.assertEqual(set(gates), {'gather', 'check', 'fix'})
        self.assertTrue(all(gate['coverage_percent'] == 100 for gate in gates.values()))

    def test_fix_preserves_initial_check(self):
        agent = MockAgent(issues=True)
        engine = Coordinator(self.root, agent)
        engine.freeze(self.request)
        result = engine.execute(self.request.run_id)
        self.assertEqual(result['outcome'], 'completed')
        self.assertEqual(agent.calls, ['check', 'fix'])
        self.assertIn('good wording', (self.root / 'atom.md').read_text())
        self.assertEqual(engine.store.load(self.request.run_id)['reports'][0]['checks']['cce']['status'], 'failed')

    def test_no_fix_permission_interrupts(self):
        request = self.request.model_copy(update={'allow_fixes': False})
        engine = Coordinator(self.root, MockAgent(issues=True))
        engine.freeze(request)
        result = engine.execute(request.run_id)
        self.assertEqual(result['outcome'], 'interrupted')
        self.assertIn('bad wording', (self.root / 'atom.md').read_text())

    def test_incomplete_check_asks_operator_before_fix(self):
        class PartialAgent(MockAgent):
            def execute(self, context, phase, directory, timeout):
                self.calls.append(phase)
                value = report(context)
                value['checks']['details']['status'] = 'blocked'
                value['checks']['details']['evidence'] = 'insufficient context'
                value['result'] = 'blocked'
                return {'report_json': json.dumps(value), 'candidate_content': None, 'confidence': 99.0}
        agent = PartialAgent()
        engine = Coordinator(self.root, agent)
        engine.freeze(self.request)
        result = engine.execute(self.request.run_id)
        self.assertEqual(result['outcome'], 'interrupted')
        self.assertEqual(agent.calls, ['check'])
        gate = engine.store.load(self.request.run_id)['coverage_gates']['check']
        self.assertLess(gate['coverage_percent'], 100)
        self.assertIn('MOCK-R-1/details', gate['missing'])
        self.assertIn('How should', result['operator_question'])

    def test_dispatch_failure_is_not_hidden_by_coverage_gate(self):
        class FailingAgent(MockAgent):
            def execute(self, context, phase, directory, timeout):
                self.calls.append(phase)
                raise RuntimeError('Codex initialization failed before model execution')
        for durable in (False, True):
            with self.subTest(durable=durable):
                request = self.request.model_copy(update={'run_id': f'launch-failure-{durable}'})
                agent = FailingAgent()
                engine = Coordinator(self.root, agent)
                original = (self.root / 'atom.md').read_bytes()
                engine.freeze(request)
                if durable:
                    from backend import execute_plan
                    result = execute_plan(engine, request.run_id, engine.gather, engine.check,
                                          engine.fix, engine.finish, engine.coverage_gate)
                else:
                    result = engine.execute(request.run_id)
                self.assertEqual(result['outcome'], 'interrupted')
                self.assertIn('initialization failed', result['reason'])
                self.assertIn('initialization failed', result['operator_question'])
                self.assertIn('check coverage is incomplete', result['reason'])
                self.assertEqual(agent.calls, ['check'])
                self.assertEqual((self.root / 'atom.md').read_bytes(), original)
                saved = engine.store.load(request.run_id)
                self.assertLess(saved['coverage_gates']['check']['coverage_percent'], 100)
                self.assertIn('initialization failed',
                              (self.root / saved['report_path']).read_text())

    def test_gather_mismatch_is_not_full_coverage(self):
        engine = Coordinator(self.root, MockAgent())
        engine.freeze(self.request)
        engine.gather(self.request.run_id)
        state = engine.store.load(self.request.run_id)
        state['selection'] = []
        engine.store._save(state)
        with self.assertRaisesRegex(Interrupted, 'gather coverage is incomplete'):
            engine.coverage_gate(self.request.run_id, 'gather')

    def test_missing_fix_disposition_asks_operator(self):
        class UnresolvedAgent(MockAgent):
            def execute(self, context, phase, directory, timeout):
                value = super().execute(context, phase, directory, timeout)
                if phase == 'fix':
                    row = json.loads(value['report_json'])
                    row.update(corrections=[], unresolved_findings=[{'finding_id': 'f1'}], result='blocked')
                    value.update(report_json=json.dumps(row), candidate_content=None)
                return value
        engine = Coordinator(self.root, UnresolvedAgent(issues=True))
        engine.freeze(self.request)
        result = engine.execute(self.request.run_id)
        self.assertEqual(result['outcome'], 'interrupted')
        self.assertIn('fix coverage is incomplete', result['reason'])
        self.assertIn('bad wording', (self.root / 'atom.md').read_text())

    def test_version_change_preserves_authoritative_source(self):
        class RevisionAgent(MockAgent):
            def execute(self, context, phase, directory, timeout):
                value = super().execute(context, phase, directory, timeout)
                if phase == 'fix':
                    value['candidate_content'] = value['candidate_content'].replace('version: 1', 'version: 2')
                return value
        engine = Coordinator(self.root, RevisionAgent(issues=True))
        original = (self.root / 'atom.md').read_bytes()
        engine.freeze(self.request)
        result = engine.execute(self.request.run_id)
        self.assertEqual(result['outcome'], 'interrupted')
        self.assertEqual((self.root / 'atom.md').read_bytes(), original)

    def test_duplicate_request_requires_identical_content(self):
        engine = Coordinator(self.root, MockAgent())
        engine.freeze(self.request)
        engine.freeze(self.request)
        with self.assertRaises(ValueError):
            engine.freeze(self.request.model_copy(update={'scope': 'OTHER'}))

    def test_traversal_rejected_before_admission(self):
        request = self.request.model_copy(update={'criteria_paths': ['../outside']})
        with self.assertRaises(ValueError):
            Coordinator(self.root, MockAgent()).freeze(request)

    def test_uncertain_dispatch_never_relaunched(self):
        engine = Coordinator(self.root, MockAgent())
        engine.freeze(self.request)
        engine.gather(self.request.run_id)
        folder = engine.run_directory(self.request.run_id) / '0-check'
        folder.mkdir()
        (folder / 'intent.json').write_text('{}')
        result = engine.execute(self.request.run_id)
        self.assertEqual(result['outcome'], 'interrupted')
        self.assertEqual(engine.agent.calls, [])

    def test_source_drift_blocks(self):
        engine = Coordinator(self.root, MockAgent())
        engine.freeze(self.request)
        (self.root / 'atom.md').write_text('changed after enqueue')
        result = engine.execute(self.request.run_id)
        self.assertEqual(result['outcome'], 'interrupted')

    def test_applied_edit_recovery_does_not_relaunch_agent(self):
        agent = MockAgent(issues=True)
        engine = Coordinator(self.root, agent)
        engine.freeze(self.request)
        engine.gather(self.request.run_id)
        engine.check(self.request.run_id, 0)
        value = engine.dispatch(self.request.run_id, 0, 'fix')
        path, raw = engine.admit_candidate(value)
        engine.store._atomic(path, raw)  # Simulate a crash before the fix report acknowledgement.
        saved = path.read_bytes()
        engine.fix(self.request.run_id, 0)
        self.assertEqual(path.read_bytes(), saved)
        self.assertEqual(agent.calls, ['check', 'fix'])
        self.assertEqual(engine.finish(self.request.run_id)['outcome'], 'completed')

    def test_summary_replacement_is_blocked(self):
        engine = Coordinator(self.root, MockAgent(issues=True))
        engine.freeze(self.request)
        engine.gather(self.request.run_id)
        engine.check(self.request.run_id, 0)
        value = engine.dispatch(self.request.run_id, 0, 'fix')
        value['candidate_content'] = value['candidate_content'].replace('A stable summary', 'New Summary')
        with self.assertRaisesRegex(Interrupted, 'Summary'):
            engine.admit_candidate(value)

    def test_replacement_requires_fix_permission(self):
        from pydantic import ValidationError
        self.assertFalse(self.request.allow_replacements)
        with self.assertRaises(ValidationError):
            Enqueue.model_validate({**self.request.model_dump(),
                                   'allow_fixes': False, 'allow_replacements': True})

    def test_enqueue_pins_the_worker_version_supporting_replacements(self):
        from unittest.mock import Mock, patch
        from backend import APP_VERSION, enqueue
        transport = Mock()
        request = self.request.model_copy(update={'allow_replacements': True})
        with patch('backend.client', return_value=transport), patch('backend.status', return_value={'outcome': 'queued'}):
            self.assertEqual(enqueue(self.root, request)['outcome'], 'queued')
        options = transport.enqueue.call_args.args[0]
        self.assertEqual(options['app_version'], APP_VERSION)
        saved = json.loads((Coordinator(self.root, None).run_directory(request.run_id) / 'request.json').read_text())
        self.assertTrue(saved['request']['allow_replacements'])

    def replacement_engine(self):
        class ReplacementAgent(MockAgent):
            def execute(self, context, phase, directory, timeout):
                value = super().execute(context, phase, directory, timeout)
                if phase == 'fix':
                    assert context['allow_replacements'] is True
                    row = json.loads(value['report_json'])
                    row['result'] = 'replaced_not_rechecked'
                    value['report_json'] = json.dumps(row)
                    value['candidate_content'] = value['candidate_content'].replace(
                        'A stable summary', 'a corrected Summary').replace('version: 1', 'version: 2')
                return value
        request = self.request.model_copy(update={'allow_replacements': True})
        engine = Coordinator(self.root, ReplacementAgent(issues=True))
        engine.freeze(request)
        return engine, request

    def test_opted_in_replacement_records_both_carriers(self):
        engine, request = self.replacement_engine()
        result = engine.execute(request.run_id)
        self.assertEqual(result['outcome'], 'completed')
        state = engine.store.load(request.run_id)
        evidence = state['reports'][0]['replacement']
        self.assertEqual(evidence['predecessor_atom_id'], 'MOCK-R-1')
        self.assertEqual(evidence['successor_atom_id'], 'MOCK-R-2')
        self.assertFalse((self.root / 'atom.md').exists())
        archived = (self.root / evidence['archived']['path']).read_text()
        successor = (self.root / evidence['successor']['path']).read_text()
        self.assertIn('status: Archived', archived)
        self.assertIn('version: 1', archived)
        self.assertIn('atom_id: MOCK-R-2', successor)
        self.assertIn('version: 1', successor)
        self.assertIn('good wording', successor)
        self.assertEqual(len(state['after'][0]), 2)
        self.assertEqual(engine.agent.calls, ['check', 'fix'])
        self.assertTrue(all(row['receipt'] for row in state['events']))
        self.assertIn('MOCK-R-2', (self.root / state['report_path']).read_text())
        journal = list((self.root / '.caprmedio_caprmedio/_journal').glob('*.ndjson'))
        events = [json.loads(line) for path in journal for line in path.read_text().splitlines()]
        replacement = next(row for row in events if row.get('predecessor_atom_id') == 'MOCK-R-1')
        self.assertEqual(replacement['successor_atom_ids'], ['MOCK-R-2'])

    def test_replacement_recovery_reuses_id_and_does_not_dispatch_again(self):
        engine, request = self.replacement_engine()
        engine.gather(request.run_id)
        engine.check(request.run_id, 0)
        value = engine.dispatch(request.run_id, 0, 'fix')
        from unittest.mock import patch
        from replacement import Replacement
        original = Replacement.publish
        calls = []
        def crash_after_one(instance, path, raw):
            original(instance, path, raw)
            calls.append(path)
            if len(calls) == 1:
                raise OSError('fixture crash after archive publication')
        with patch.object(Replacement, 'publish', crash_after_one):
            with self.assertRaisesRegex(OSError, 'fixture crash'):
                engine.apply_replacement(request.run_id, 0, value)
        engine.fix(request.run_id, 0)
        state = engine.store.load(request.run_id)
        self.assertEqual(state['reports'][0]['replacement']['successor_atom_id'], 'MOCK-R-2')
        self.assertEqual(engine.agent.calls, ['check', 'fix'])
        self.assertEqual(engine.finish(request.run_id)['outcome'], 'completed')

    def test_replacement_skips_existing_and_reserved_ids(self):
        (self.root / 'history.md').write_text('retired reference MOCK-R-8')
        engine, request = self.replacement_engine()
        self.assertEqual(engine.execute(request.run_id)['outcome'], 'completed')
        state = engine.store.load(request.run_id)
        self.assertEqual(state['reports'][0]['replacement']['successor_atom_id'], 'MOCK-R-9')

    def test_replacement_preserves_unrelated_scope_and_checks_collisions(self):
        engine, request = self.replacement_engine()
        engine.gather(request.run_id)
        engine.check(request.run_id, 0)
        value = engine.dispatch(request.run_id, 0, 'fix')
        value['candidate_content'] = value['candidate_content'].replace(
            'version: 2', 'version: 2\ncurrent_scope_unit: OTHER')
        with self.assertRaisesRegex(Interrupted, 'current_scope_unit'):
            engine.apply_replacement(request.run_id, 0, value)
        self.assertTrue((self.root / 'atom.md').exists())

    def test_replacement_collision_preserves_source_and_competing_destination(self):
        engine, request = self.replacement_engine()
        engine.gather(request.run_id)
        engine.check(request.run_id, 0)
        value = engine.dispatch(request.run_id, 0, 'fix')
        from replacement import Replacement
        replacement = Replacement(engine, request.run_id, 0)
        with replacement.lock():
            plan = replacement.plan(value, request, 'a corrected Summary')
        target = self.root / plan['successor']['path']
        target.write_text('competing destination')
        original = (self.root / 'atom.md').read_bytes()
        with self.assertRaisesRegex(ValueError, 'destination changed'):
            engine.apply_replacement(request.run_id, 0, value)
        self.assertEqual(target.read_text(), 'competing destination')
        self.assertEqual((self.root / 'atom.md').read_bytes(), original)

    def test_replacement_result_without_permission_never_changes_source(self):
        engine, request = self.replacement_engine()
        request = request.model_copy(update={'run_id': 'replacement-denied', 'allow_replacements': False})
        engine.freeze(request)
        engine.gather(request.run_id)
        value = {'context': {'source': engine.store.observe('atom.md'),
                 'source_content': (self.root / 'atom.md').read_text()},
                 'candidate_content': 'unused'}
        with self.assertRaisesRegex(Interrupted, 'not delegated'):
            engine.apply_replacement(request.run_id, 0, value)
        self.assertTrue((self.root / 'atom.md').exists())

    def test_codex_subprocess_adapter_with_mock_executable(self):
        from agent import CodexAgent

        class FixtureCodex(CodexAgent):
            def command(self, directory):
                actual = super().command(directory)
                return [sys.executable, str(APP / 'tests/fake_codex.py'), *actual[1:]]

        agent = FixtureCodex()
        engine = Coordinator(self.root, agent)
        engine.freeze(self.request)
        self.assertEqual(engine.execute(self.request.run_id)['outcome'], 'completed')
        command = agent.command(self.root)
        self.assertEqual(command[command.index('--sandbox') + 1], 'read-only')
        self.assertNotIn('--dangerously-bypass-approvals-and-sandbox', command)
        overrides = [command[index + 1] for index, token in enumerate(command) if token == '-c']
        self.assertIn('sqlite_home=' + json.dumps(str(self.root / 'codex-state')), overrides)
        self.assertIn('log_dir=' + json.dumps(str(self.root / 'codex-logs')), overrides)
        self.assertTrue((engine.run_directory(self.request.run_id) / '0-check/codex-state').is_dir())

    def test_codex_launch_failure_has_safe_diagnostics(self):
        from agent import CodexAgent

        class FixtureCodex(CodexAgent):
            def command(self, directory):
                return [sys.executable, str(APP / 'tests/fake_codex.py'), *super().command(directory)[1:]]

        context = {'fixture_launch_failure': True}
        with self.assertRaisesRegex(RuntimeError, 'initialization failed') as raised:
            FixtureCodex().execute(context, 'check', self.root, 5)
        self.assertIn('stderr.log', str(raised.exception))
        self.assertNotIn('fixture-private-value', str(raised.exception))

    def test_agent_timeout_is_explicit(self):
        from agent import CodexAgent

        class FixtureCodex(CodexAgent):
            def command(self, directory):
                return [sys.executable, str(APP / 'tests/fake_codex.py'), *super().command(directory)[1:]]

        context = {'workflow_run_id': 'fixture', 'atom_id': 'MOCK-R-1',
                   'source': {}, 'criteria_sha256': 'mock', 'fixture_timeout': True}
        with self.assertRaisesRegex(RuntimeError, 'timed out'):
            FixtureCodex().execute(context, 'check', self.root, 1)

    def test_detached_idle_worker_survives_start_client_exit(self):
        started = subprocess.run([sys.executable, str(APP / 'orchestrator.py'),
                                  '--project-root', str(self.root), 'start-worker'],
                                 capture_output=True, text=True, timeout=15)
        self.assertEqual(started.returncode, 0, started.stderr)
        pid = json.loads(started.stdout)['worker_pid']
        ready = self.root / '.caprmedio_install/workflow_orchestrator/worker.ready'
        state = self.root / '.caprmedio_install/workflow_orchestrator/worker.json'
        try:
            deadline = time.monotonic() + 20
            while not ready.exists() and time.monotonic() < deadline:
                time.sleep(0.1)
            self.assertTrue(ready.exists())
            os.kill(pid, 0)
            self.assertFalse((self.root / '.caprmedio_tmp/rmed-base-revise').exists())
        finally:
            os.kill(pid, signal.SIGTERM)
            deadline = time.monotonic() + 15
            while time.monotonic() < deadline:
                if state.exists() and json.loads(state.read_text()).get('state') == 'stopped':
                    break
                time.sleep(0.1)
            self.assertEqual(json.loads(state.read_text())['state'], 'stopped')

    def test_real_queue_survives_client_disconnect_and_worker_restart(self):
        from backend import status
        from contracts import Status
        ready = self.root / 'ready'
        process = None

        def start_worker():
            log = (self.root / 'worker.log').open('a')
            child = subprocess.Popen([sys.executable, str(APP / 'tests/mock_worker.py'),
                                      str(self.root), str(ready)], stdout=subprocess.DEVNULL,
                                     stderr=log)
            log.close()
            deadline = time.monotonic() + 25
            while not ready.exists() and time.monotonic() < deadline and child.poll() is None:
                time.sleep(0.1)
            self.assertTrue(ready.exists(), (self.root / 'worker.log').read_text())
            return child

        try:
            process = start_worker()
            process.terminate()
            process.wait(timeout=15)
            ready.unlink()
            # Enqueue while no worker exists; this client then exits completely.
            client = subprocess.run([sys.executable, str(APP / 'orchestrator.py'),
                                     '--project-root', str(self.root), 'enqueue'],
                                    input=self.request.model_dump_json(), text=True,
                                    capture_output=True, timeout=15)
            self.assertEqual(client.returncode, 0, client.stderr)
            self.assertEqual(json.loads(client.stdout)['outcome'], 'queued')
            process = start_worker()
            deadline = time.monotonic() + 20
            result = {}
            while time.monotonic() < deadline:
                result = status(self.root, Status(run_id=self.request.run_id))
                if result['outcome'] in ('completed', 'interrupted', 'failed'):
                    break
                time.sleep(0.2)
            self.assertEqual(result.get('outcome'), 'completed', result)
            self.assertIn('good wording', (self.root / 'atom.md').read_text())
            self.assertTrue((self.root / result['report_path']).is_file())
        finally:
            if process and process.poll() is None:
                process.terminate()
                process.wait(timeout=15)


if __name__ == '__main__':
    unittest.main()
