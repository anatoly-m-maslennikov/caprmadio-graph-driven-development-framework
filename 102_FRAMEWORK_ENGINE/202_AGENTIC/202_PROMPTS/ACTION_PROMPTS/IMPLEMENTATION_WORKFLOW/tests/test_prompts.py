"""Static contract checks for the short Implementation Workflow prompts."""
import hashlib
import json
import re
import unittest
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
        required = {'CA-O-016', 'CA-M-285', 'CA-E-389', 'CA-E-390', 'CA-R-1601', 'CA-D-487'} | self.nodes
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


if __name__ == '__main__':
    unittest.main()
