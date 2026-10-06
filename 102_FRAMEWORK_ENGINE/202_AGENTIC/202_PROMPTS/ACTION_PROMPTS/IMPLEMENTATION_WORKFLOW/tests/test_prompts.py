"""Static contract checks for the short Implementation Workflow prompts."""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[6]
SOURCE = ROOT / '.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations'
EXCLUDED = {'archive', 'archived', 'draft', 'drafts', 'done', 'canceled', 'cancelled'}


def atom(atom_id):
    paths = [p for p in SOURCE.rglob(atom_id + '-*.md') if not (set(p.relative_to(SOURCE).parts) & EXCLUDED)]
    if len(paths) != 1:
        raise AssertionError(f'{atom_id}: expected one source, found {len(paths)}')
    text = paths[0].read_text(encoding='utf-8')
    if not re.search(r'^atom_id: ' + re.escape(atom_id) + '$', text, re.M):
        raise AssertionError(f'{atom_id}: missing explicit source identity')
    if not re.search(r'^status: Active$', text, re.M):
        raise AssertionError(f'{atom_id}: source is not Active')
    return text


class PromptContracts(unittest.TestCase):
    @staticmethod
    def actions():
        spec = importlib.util.spec_from_file_location('implementation_actions', HERE / 'implementation_actions.py')
        actions = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(actions)
        return actions

    @staticmethod
    def packet(actions, context='Isolated'):
        methods = [row['path'] for row in actions.current_source_bindings()
                   if row['atom_id'].startswith('CA-M-')]
        candidate = {'id': 'candidate-1'}
        phase = 'implementation'
        authorization = {
            'authorization_ref': 'authorizations/implementation-fixture.json',
            'authorization_freshness': {'state': 'current', 'digest': 'a' * 64},
            'request_id': 'implementation-fixture',
            'operation_route': 'run_implementation_workflow',
            'proposal_receipt_digest': 'b' * 64,
            'parameters_digest': 'c' * 64,
            'target_frontier_digest': 'd' * 64,
            'effects_digest': 'e' * 64,
            'definition_manifest': {'manifest_ref': 'fixture/implementation.json',
                                    'manifest_digest': 'f' * 64},
            'source_freshness': {'selected_binding_ref': 'fixture/implementation-bindings.json',
                                 'selected_binding_digest': '1' * 64},
        }
        return {
            'context': context, 'source_bindings': actions.current_source_bindings(),
            'permissions': {
                'allowed': True,
                'retry': {'authorization_ref': authorization['authorization_ref'],
                          'source_ref': 'CA-M-295:default-settings',
                          'task_ref': authorization['request_id'],
                          'epic_ref': authorization['definition_manifest']['manifest_ref']},
            }, 'operator_authorization': authorization, 'handoff_complete': True,
            'plan_item': {'plan_id': 'plan-1', 'item_id': 'item-1',
                          'dod': ['implemented and checked'], 'owned_paths': ['.'],
                          'estimated_minutes': 14},
            'requirements': actions.prepare_input_bindings(['CA-R-1843']),
            'delivery': actions.prepare_input_bindings(['CA-D-544']),
            'evaluations': actions.prepare_input_bindings(['CA-E-563']),
            'method_projection': actions.prepare_method_projection(methods),
            'red': {'expectation': 'ready is true', 'fixtures': ['fixture'],
                    'commands': ['python fixture_test.py'], 'scope': 'selected item'},
            'candidate': candidate, 'phase': phase,
            'golden_e2e': ['disposable executable assertion'],
            'baseline_command': 'python fixture_test.py',
            'confidence': {'observed': 1.0, 'effective': 0.9, 'source': 'default-settings'},
            'retry': {'consumed': 0, 'effective_limit': 1, 'source': 'CA-M-295:default-settings',
                      'remaining_failure': True, 'admitted': True},
            'coverage': {'required': ['CA-E-563'], 'checked': [], 'complete': False,
                         'candidate': candidate, 'phase': phase},
            'retained_state': {'retry': 0}, 'evidence': ['baseline'],
        }
    @classmethod
    def setUpClass(cls):
        cls.workflow = atom('CA-O-016')
        cls.nodes = set(re.search(r'^- nodes: (.+)\.$', cls.workflow, re.M)[1].split(', '))
        cls.prompts = {p.name.removesuffix('.prompt.md'): p.read_text(encoding='utf-8') for p in HERE.glob('*.prompt.md')}

    def test_exact_current_step_coverage(self):
        self.assertEqual(self.nodes, set(self.prompts))
        self.assertEqual(len(self.nodes), 7)
        self.assertNotIn('CA-O-098', self.nodes)

    def test_bindings_and_context_match_sources(self):
        for step, prompt in self.prompts.items():
            with self.subTest(step=step):
                binding = re.search(r'^Step: (CA-O-\d+) \| Action: (CA-O-\d+) \| Context: (Integrated|Isolated)$', prompt, re.M)
                self.assertIsNotNone(binding)
                self.assertEqual(binding[1], step)
                source = atom(step)
                action = re.search(r'invoking \*\*=1\*\* Action, (CA-O-\d+)', source)[1]
                context = re.search(r'\*\*in\*\* (Integrated|Isolated) context', source)[1]
                self.assertEqual(binding[2], action)
                self.assertEqual(binding[3], context)
                self.assertIn('type: Action\n', atom(action))

    def test_result_labels_match_workflow_edges(self):
        for step, prompt in self.prompts.items():
            with self.subTest(step=step):
                expected = set(re.findall(r'^\| ' + re.escape(step) + r' \| (\w+) \|', self.workflow, re.M))
                actual = re.search(r'^Results: (.+)$', prompt, re.M)[1].split(' | ')
                self.assertEqual(expected, set(actual))
                self.assertEqual(len(actual), len(set(actual)))

    def test_prompts_are_short_and_grounded(self):
        for step, prompt in self.prompts.items():
            with self.subTest(step=step):
                self.assertTrue(prompt.startswith('# System Prompt\n'))
                self.assertLessEqual(len(prompt.split()), 160)
                self.assertIn('pinned authority and input packet', prompt)
                self.assertNotIn('methods_ready', prompt)
                self.assertNotRegex(prompt, r'\b(?:TODO|TBD)\b|\{\{')
                self.assertIn('permission', prompt)
                self.assertIn('Return', prompt)

    def test_testing_and_learning_boundaries(self):
        tests = self.prompts['CA-O-092']
        self.assertIn('E2E tests first', tests)
        self.assertIn('golden corpus', tests)
        self.assertIn('Mock external boundaries, not the implementation', tests)
        self.assertIn('Do not create or promote M Atoms', self.prompts['CA-O-099'])
        self.assertIn('Method learning is separate', self.prompts['CA-O-091'])
        self.assertIn('initial failed Evaluation consumes zero retries', self.prompts['CA-O-096'])

    def test_preparation_packet_separates_what_how_and_checks(self):
        prompt = self.prompts['CA-O-091']
        for fragment in ('R + D implementation targets', 'E separately as checks',
                         'all active Ms', 'into one file', 'full content and source bindings',
                         'completeness and freshness', 'does not establish applicability'):
            self.assertIn(fragment, prompt)
        authority = atom('CA-O-017')
        for fragment in ('**=1** file', 'full frontmatter **and** Markdown content',
                         'complete active Method inventory', 'separately as check authority'):
            self.assertIn(fragment, authority)
        readme = (HERE / 'README.md').read_text(encoding='utf-8')
        for fragment in ('**what to implement**', '**how to implement**', '**what to check**',
                         'same verified file binding downstream'):
            self.assertIn(fragment, readme)

    def test_reviewed_source_frontier_is_current(self):
        bindings = json.loads((HERE / 'source_bindings.json').read_text(encoding='utf-8'))
        self.assertEqual(bindings['schema_version'], 1)
        self.assertEqual(bindings['workflow'], 'CA-O-016')
        ids = [row['atom_id'] for row in bindings['sources']]
        self.assertEqual(len(ids), len(set(ids)))
        required = {
            'CA-R-1843', 'CA-R-1844', 'CA-R-1845', 'CA-R-1846',
            'CA-M-326', 'CA-M-327', 'CA-M-328', 'CA-M-329',
            'CA-E-563', 'CA-E-564', 'CA-E-565', 'CA-E-566',
            'CA-D-544', 'CA-D-545', 'CA-D-546', 'CA-O-016',
        } | self.nodes
        for prompt in self.prompts.values():
            required.add(re.search(r'Action: (CA-O-\d+)', prompt)[1])
        self.assertEqual(set(ids), required)
        for row in bindings['sources']:
            with self.subTest(atom=row['atom_id']):
                path = (ROOT / row['path']).resolve()
                self.assertTrue(path.is_relative_to(ROOT))
                raw = path.read_bytes()
                self.assertEqual(hashlib.sha256(raw).hexdigest(), row['sha256'], 'Authority changed: review prompts before refreshing bindings')
                self.assertEqual(int(re.search(r'^version: (\d+)$', raw.decode('utf-8'), re.M)[1]), row['version'])

    def test_prompt_runtime_contract_is_not_live_llm_proof(self):
        readme = (HERE / 'README.md').read_text(encoding='utf-8')
        self.assertIn('Mock Agent tests are not live LLM proof.', readme)
        self.assertIn('implementation_actions.py', readme)

    def test_queue_uses_replaceable_agent_and_truthful_envelope(self):
        actions = self.actions()
        packet = self.packet(actions)
        seen = []
        def agent(prompt, supplied):
            seen.append((prompt, supplied))
            return {'result': 'implemented',
                    'outputs': {'candidate': supplied['candidate'], 'phase': supplied['phase'],
                                'changed_paths': ['a.py']}, 'evidence': ['change']}
        actual = actions.implement_selected_queue('CA-O-093', packet, agent)
        self.assertEqual(actual['result'], 'implemented')
        self.assertEqual(actual['context'], 'Isolated')
        self.assertEqual(actual['evidence'], ['baseline', 'change'])
        self.assertEqual(len(seen), 1)
        self.assertEqual(set(actions.ACTION_HANDLERS), {'CA-O-017', 'CA-O-018', 'CA-O-019', 'CA-O-020', 'CA-O-089', 'CA-O-024', 'CA-O-021'})

    def test_queue_blocks_context_missing_test_first_or_retry_overrun(self):
        actions = self.actions()
        base = self.packet(actions)
        base.pop('context')
        self.assertEqual(actions.implement_selected_queue('CA-O-092', base, lambda *_: {'result': 'prepared'})['result'], 'blocked')
        retry = {**self.packet(actions, 'Integrated'),
                 'retry': {'consumed': 1, 'effective_limit': 1,
                           'source': 'CA-M-295:default-settings', 'remaining_failure': True,
                           'admitted': True}}
        self.assertEqual(actions.implement_selected_queue('CA-O-096', retry)['result'], 'retry_blocked')

    def test_queue_rejects_conflicting_legacy_r_d_aliases(self):
        actions = self.actions()
        packet = self.packet(actions)
        packet['requirements_delivery'] = list(packet['requirements'])
        actual = actions.implement_selected_queue(
            'CA-O-093', packet,
            lambda *_: {'result': 'implemented',
                         'outputs': {'candidate': 'c1', 'changed_paths': ['a.py']},
                         'evidence': ['change']},
        )
        self.assertEqual(actual['result'], 'blocked')

    def test_queue_rejects_stale_pins_projection_and_label_only_success(self):
        actions = self.actions()
        packet = self.packet(actions)
        packet['source_bindings'] = packet['source_bindings'][:-1]
        self.assertEqual(actions.implement_selected_queue('CA-O-093', packet, lambda *_: {'result': 'implemented'})['result'], 'blocked')
        packet = self.packet(actions)
        packet['method_projection']['sources'][0]['sha256'] = '0' * 64
        self.assertEqual(actions.implement_selected_queue('CA-O-093', packet, lambda *_: {'result': 'implemented'})['result'], 'blocked')
        packet = self.packet(actions)
        self.assertEqual(actions.implement_selected_queue('CA-O-093', packet, lambda *_: {'result': 'implemented', 'outputs': {}, 'evidence': []})['result'], 'blocked')

    def test_golden_agent_retains_initial_failure_and_final_command_output(self):
        actions = self.actions()
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            implementation = work / 'implementation.py'
            test_script = work / 'golden_test.py'
            implementation.write_text('def ready():\n    return False\n', encoding='utf-8')
            test_script.write_text('from implementation import ready\nassert ready()\n', encoding='utf-8')
            command = [sys.executable, str(test_script)]
            retained = {}
            def agent(prompt, _packet):
                step = re.search(r'Step: (CA-O-\d+)', prompt)[1]
                if step == 'CA-O-092':
                    initial = subprocess.run(command, cwd=work, capture_output=True, text=True)
                    retained['initial'] = {'returncode': initial.returncode, 'stderr': initial.stderr}
                    return {'result': 'prepared', 'outputs': {'golden_e2e': ['ready'], 'commands': [command], 'expected_outcomes': ['pass after implementation']}, 'evidence': [retained['initial']]}
                if step == 'CA-O-093':
                    implementation.write_text('def ready():\n    return True\n', encoding='utf-8')
                    return {'result': 'implemented',
                            'outputs': {'candidate': _packet['candidate'], 'phase': _packet['phase'],
                                        'changed_paths': [str(implementation)]},
                            'evidence': [{'changed': str(implementation)}]}
                final = subprocess.run(command, cwd=work, capture_output=True, text=True)
                return {'result': 'passed', 'outputs': {'candidate': {'id': 'candidate-1'},
                                                        'commands': [command],
                                                        'checks': [{'returncode': final.returncode, 'stdout': final.stdout, 'stderr': final.stderr}],
                                                        'coverage': {'complete': True, 'checked': ['CA-E-563']}},
                        'evidence': [{'phase': 'final', 'returncode': final.returncode}]}
            prepared_packet = self.packet(actions)
            prepared_packet['golden_e2e'], prepared_packet['baseline_command'] = ['ready'], command
            prepared = actions.implement_selected_queue('CA-O-092', prepared_packet, agent)
            implemented = actions.implement_selected_queue('CA-O-093', self.packet(actions), agent)
            evaluated = actions.implement_selected_queue('CA-O-094', self.packet(actions, 'Integrated'), agent)
            self.assertEqual((prepared['result'], implemented['result'], evaluated['result']), ('prepared', 'implemented', 'passed'))
            self.assertEqual(retained['initial']['returncode'], 1)
            self.assertEqual(evaluated['outputs']['checks'][0]['returncode'], 0)

    def test_packet_admission_requires_complete_red_plan_and_authority_bindings(self):
        actions = self.actions()
        for field in ('requirements', 'method_projection', 'plan_item', 'red',
                      'candidate', 'phase', 'confidence', 'retry'):
            with self.subTest(field=field):
                packet = self.packet(actions)
                packet.pop(field)
                launched = []
                actual = actions.implement_selected_queue(
                    'CA-O-093', packet, lambda *_: launched.append('launched'))
                self.assertEqual(actual['result'], 'blocked')
                self.assertEqual(launched, [])

        packet = self.packet(actions)
        packet['requirements'] = ['CA-R-1843']
        actual = actions.implement_selected_queue(
            'CA-O-093', packet, lambda *_: {'result': 'implemented',
                                            'outputs': {'candidate': packet['candidate'],
                                                        'changed_paths': ['a.py']},
                                            'evidence': ['change']})
        self.assertEqual(actual['result'], 'blocked')

        packet = self.packet(actions)
        packet['method_projection']['sources'] = packet['method_projection']['sources'][:-1]
        actual = actions.implement_selected_queue(
            'CA-O-093', packet, lambda *_: {'result': 'implemented',
                                            'outputs': {'candidate': packet['candidate'],
                                                        'changed_paths': ['a.py']},
                                            'evidence': ['change']})
        self.assertEqual(actual['result'], 'blocked')

    def test_optional_delivery_and_evaluation_cardinality_is_step_scoped(self):
        actions = self.actions()
        packet = self.packet(actions)
        packet['delivery'] = []
        packet['evaluations'] = []
        implemented = actions.implement_selected_queue(
            'CA-O-093', packet, lambda *_: {'result': 'implemented',
                                            'outputs': {'candidate': packet['candidate'], 'phase': packet['phase'],
                                                        'changed_paths': ['a.py']},
                                            'evidence': ['change']})
        self.assertEqual(implemented['result'], 'implemented')

        prepared = actions.implement_selected_queue(
            'CA-O-092', packet, lambda *_: {'result': 'prepared',
                                            'outputs': {'golden_e2e': ['case'],
                                                        'commands': ['test'],
                                                        'expected_outcomes': ['pass']},
                                            'evidence': ['prepared']})
        self.assertEqual(prepared['result'], 'blocked')

    def test_retry_admission_requires_effective_source_and_confidence_gate(self):
        actions = self.actions()
        packet = self.packet(actions, 'Integrated')
        packet['remaining_failure'] = True
        packet['retry'].update(remaining_failure=True, admitted=False)
        blocked = actions.implement_selected_queue('CA-O-096', packet)
        self.assertEqual(blocked['result'], 'retry_blocked')

        packet = self.packet(actions, 'Integrated')
        packet['confidence']['observed'] = 0.5
        blocked = actions.implement_selected_queue('CA-O-096', packet)
        self.assertEqual(blocked['result'], 'retry_blocked')

        packet = self.packet(actions, 'Integrated')
        decision = actions.implement_selected_queue(
            'CA-O-096', packet,
            lambda *_: {'result': 'retry_permitted',
                        'outputs': {'decision': 'retry_permitted',
                                    'limit_provenance': packet['retry']['source'],
                                    'consumed': 0},
                        'evidence': ['retry-gate']},
            trusted_execution_authorization=packet['operator_authorization'])
        self.assertEqual(decision['result'], 'retry_permitted')

    def test_retry_rejects_fake_approval_and_unbound_permission(self):
        actions = self.actions()
        packet = self.packet(actions, 'Integrated')
        blocked = actions.implement_selected_queue('CA-O-096', packet)
        self.assertEqual(blocked['result'], 'retry_blocked')

        packet = self.packet(actions, 'Integrated')
        packet['operator_retry_approval'] = {'approved': True, 'source': 'operator'}
        packet['permissions']['retry'] = True
        blocked = actions.implement_selected_queue('CA-O-096', packet)
        self.assertEqual(blocked['result'], 'retry_blocked')

        packet = self.packet(actions, 'Integrated')
        packet['permissions']['retry']['authorization_ref'] = 'authorizations/other.json'
        blocked = actions.implement_selected_queue('CA-O-096', packet)
        self.assertEqual(blocked['result'], 'retry_blocked')

    def test_performed_success_rejects_fake_candidate_or_phase_identity(self):
        actions = self.actions()
        for field, value in (('candidate', {'id': 'other-candidate'}),
                             ('phase', 'other-phase')):
            with self.subTest(field=field):
                packet = self.packet(actions)
                response = {'result': 'implemented',
                            'outputs': {'candidate': packet['candidate'], 'phase': packet['phase'],
                                        'changed_paths': ['a.py']},
                            'evidence': ['change']}
                response['outputs'][field] = value
                blocked = actions.implement_selected_queue('CA-O-093', packet, lambda *_: response)
                self.assertEqual(blocked['result'], 'blocked')

    def test_performed_success_is_bound_to_packet_scope_and_coverage(self):
        actions = self.actions()
        packet = self.packet(actions, 'Integrated')
        outside = actions.implement_selected_queue(
            'CA-O-094', packet,
            lambda *_: {'result': 'passed',
                        'outputs': {'candidate': packet['candidate'], 'commands': ['test'],
                                    'checks': [{'returncode': 0}],
                                    'coverage': {'complete': True, 'checked': ['CA-E-563']}},
                        'evidence': ['pass']})
        self.assertEqual(outside['result'], 'passed')

        packet = self.packet(actions, 'Integrated')
        packet['coverage']['required'] = ['CA-E-563', 'CA-E-564']
        incomplete = actions.implement_selected_queue(
            'CA-O-094', packet,
            lambda *_: {'result': 'passed',
                        'outputs': {'candidate': packet['candidate'], 'commands': ['test'],
                                    'checks': [{'returncode': 0}],
                                    'coverage': {'complete': True, 'checked': ['CA-E-563']}},
                        'evidence': ['pass']})
        self.assertEqual(incomplete['result'], 'blocked')


if __name__ == '__main__':
    unittest.main()
