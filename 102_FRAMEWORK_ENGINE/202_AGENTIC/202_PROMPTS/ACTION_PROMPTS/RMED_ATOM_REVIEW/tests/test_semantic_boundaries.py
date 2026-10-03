"""Regress false semantic passes observed in the unchanged same20 run."""
import unittest

from test_split_evaluation import SOURCE_TEXT, RULE_TEXT, contract, part, source
from context_builder import body_sections, body_section_texts
from semantic_boundaries import unavailable_sections


def bind_body(raw):
    if not raw.startswith('---\n'):
        raw = '---\nsubjects:\n  governs: Atom\n  depends_on: []\n---\n' + raw
    candidate = source('mock.md', 'MOCK-R-001', raw)
    context = contract.ReviewContext({'confidence_threshold': .99, 'sources': [
        candidate, source('rule.md', 'MOCK-R-002', RULE_TEXT)]})
    response = part('coherence')
    response.update(source=candidate['binding'], context_sha256=context.sha256)
    response['checks'][0]['subject_inventory']['sections_reviewed'] = body_sections(raw)
    mention = response['checks'][0]['subject_inventory']['mentions'][0]
    mention['location'] = next(address for address, text in body_section_texts(raw).items()
                               if mention['excerpt'] in text)
    return response, context


def block_dependent_checks(response, raw):
    for row in response['checks']:
        if row['id'] in unavailable_sections(raw):
            row['status'] = 'blocked'
            response['coverage_gaps'].append({'check_id': row['id'],
                'kind': 'layout_dependency', 'reason': 'Required local section is absent or ambiguous.'})
    response['result'] = 'blocked'


class SemanticBoundaries(unittest.TestCase):
    def test_same20_legacy_shape_cannot_pass_governed_entity(self):
        raw = '# Atom rule\n\nAtom must comply.\n'
        response, ctx = bind_body(raw)
        block_dependent_checks(response, raw)
        contract.validate_part(response, context=ctx)
        row = next(row for row in response['checks'] if row['id'] == 'governed_entity')
        row['status'] = 'passed'
        response['coverage_gaps'] = [g for g in response['coverage_gaps'] if g['check_id'] != 'governed_entity']
        with self.assertRaisesRegex(ValueError, 'governed_entity.*sections'):
            contract.validate_part(response, context=ctx)

    def test_missing_scope_blocks_summary_even_with_claim_and_summary(self):
        raw = SOURCE_TEXT.replace('## Scope\nAtoms\n', '')
        response, ctx = bind_body(raw)
        block_dependent_checks(response, raw)
        summary = next(row for row in response['checks'] if row['id'] == 'summary')
        summary['status'] = 'passed'
        response['coverage_gaps'] = [g for g in response['coverage_gaps'] if g['check_id'] != 'summary']
        with self.assertRaisesRegex(ValueError, 'summary.*Scope'):
            contract.validate_part(response, context=ctx)

    def test_unrelated_missing_context_does_not_replace_layout_evidence(self):
        raw = '# Atom rule\nAtom must comply.\n'
        response, ctx = bind_body(raw)
        block_dependent_checks(response, raw)
        for gap in response['coverage_gaps']:
            gap['kind'] = 'unresolved_interpretation'
        with self.assertRaisesRegex(ValueError, 'layout dependency'):
            contract.validate_part(response, context=ctx)

    def test_fenced_heading_does_not_supply_claim(self):
        raw = SOURCE_TEXT.replace('## Claim\nAtom must comply.', '```markdown\n## Claim\nAtom must comply.\n```')
        self.assertIn('## Claim', unavailable_sections(raw)['governed_entity'])

    def test_duplicate_claim_is_ambiguous_not_available(self):
        self.assertIn('claim', unavailable_sections(SOURCE_TEXT + '\n## Claim\nAtom second.\n'))

    def test_complete_structure_still_needs_semantic_judgment(self):
        self.assertEqual({}, unavailable_sections(SOURCE_TEXT))
        response, ctx = bind_body(SOURCE_TEXT)
        contract.validate_part(response, context=ctx)

    def test_subjects_and_role_remain_independently_assessable(self):
        missing = unavailable_sections('# Atom rule\nAtom must comply.\n')
        self.assertNotIn('subjects', missing)
        self.assertNotIn('content_role', missing)


if __name__ == '__main__':
    unittest.main()
