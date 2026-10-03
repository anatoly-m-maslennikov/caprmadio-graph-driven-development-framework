"""Source/implementation bindings; these checks do not simulate agent judgment."""
import hashlib
import json
from pathlib import Path
import tomllib
import unittest

import yaml

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[4]
AUTHORITY = ROOT / '.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/202_FEATURE_PROMPTS'
ROLES = {'CA-R-1801': 'Requirement', 'CA-R-1802': 'Requirement', 'CA-R-1803': 'Requirement',
         'CA-M-317': 'Method', 'CA-E-524': 'Evaluation',
         'CA-D-509': 'Delivery', 'CA-D-510': 'Delivery', 'CA-D-511': 'Delivery'}


def source(identifier):
    paths = [p for p in AUTHORITY.rglob(identifier + '-*.md') if 'archive' not in p.parts]
    if len(paths) != 1:
        raise AssertionError((identifier, paths))
    raw = paths[0].read_bytes()
    return paths[0], raw, yaml.safe_load(raw.decode().split('---', 2)[1])


class PromptSpecification(unittest.TestCase):
    def test_registered_scope_keeps_explicit_existing_paths(self):
        structure = tomllib.loads((ROOT / '.caprmedio_caprmedio/project_structure.toml').read_text())
        units = {row['scope_unit_name']: row for row in structure['scope_units']}
        unit = units['PROMPTS']
        self.assertEqual(unit['parent'], 'AGENTIC')
        self.assertEqual(unit['scope_unit_type'], 'Unordered')
        self.assertNotIn('local_order', unit)
        self.assertEqual(unit['structural_level'], units['AGENTIC']['structural_level'] + 1)
        self.assertEqual(ROOT / unit['authority_path'], AUTHORITY)
        self.assertEqual(unit['delivery_path'], '102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS')

    def test_prompt_rmed_is_active_and_bound(self):
        bindings = {row['atom_id']: row for row in json.loads((HERE / 'source_bindings.json').read_text())['sources']}
        for identifier, role in ROLES.items():
            with self.subTest(atom=identifier):
                path, raw, metadata = source(identifier)
                self.assertEqual(metadata['atom_id'], identifier)
                self.assertEqual(metadata['content_role'], role)
                self.assertEqual(metadata['status'], 'Active')
                self.assertEqual(metadata['current_scope_unit'], 'PROMPTS')
                self.assertEqual(metadata['claim_target_scope_unit'], 'PROMPTS')
                self.assertEqual(metadata['local_tier'], 'Standard')
                self.assertEqual(metadata['global_tier'], 11)
                self.assertEqual([line for line in raw.decode().splitlines() if line.startswith('## ')],
                                 ['## Scope', '## Claim', '## Details'])
                self.assertEqual(bindings[identifier]['path'], path.relative_to(ROOT).as_posix())
                self.assertEqual(bindings[identifier]['sha256'], hashlib.sha256(raw).hexdigest())

    def test_operations_stay_in_methodology(self):
        bindings = {row['atom_id']: row for row in json.loads((HERE / 'source_bindings.json').read_text())['sources']}
        for identifier in ('CA-O-104', 'CA-O-105', 'CA-O-106', 'CA-O-108', 'CA-O-109', 'CA-O-110', 'CA-O-111'):
            self.assertIn('/000_APPLICABLE_MTHD_sources/', bindings[identifier]['path'])
            self.assertNotIn('/202_FEATURE_PROMPTS/', bindings[identifier]['path'])

    def test_delivery_files_exist_and_completion_fields_match(self):
        delivery = source('CA-D-509')[1].decode()
        for filename in ('CA-O-108.prompt.md', 'CA-O-109.prompt.md', 'CA-O-110.prompt.md',
                         'README.md', 'source_bindings.json', 'workflow_progress.py'):
            self.assertIn(filename, delivery)
            self.assertTrue((HERE / filename).is_file())
        report_delivery = source('CA-D-510')[1].decode()
        for field in ('reported_result', 'check_complete', 'complete', 'unresolved_findings'):
            self.assertIn('`' + field + '`', report_delivery)

    def test_engine_evaluation_targets_its_rmd(self):
        _, raw, metadata = source('CA-E-524')
        self.assertEqual(metadata['type'], 'QA Case')
        self.assertEqual(set(metadata['relations']['evaluation_for']), set(ROLES) - {'CA-E-524'})
        for case in ('readable unheaded content', 'independent Claims', 'genuine ambiguity',
                     'partial fixes', 'complete fixes', 'clean Atom'):
            self.assertIn(case, raw.decode())


if __name__ == '__main__':
    unittest.main()
