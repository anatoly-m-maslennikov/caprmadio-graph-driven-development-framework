"""Adversarial tests for the isolated no-write layout-preview validator."""
import copy
import hashlib
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent)]
from layout_preview import admit_layout_preview  # noqa: E402


SOURCE = ('---\natom_id: MOCK-R-001\nversion: 1\nupdated_at: "2026-09-26T00:00:00Z"\n---\n'
          '# Legacy atom\nThe original proposition must remain exactly here.\n')
_FRONTMATTER_END = SOURCE.index('---\n', 4) + 4
HEADER, BODY = SOURCE[:_FRONTMATTER_END], SOURCE[_FRONTMATTER_END:]
CANDIDATE = (HEADER + '# Summary\nLegacy atom\n\n## Scope\nThis rule governs review admission.\n\n'
             '## Claim\nThe original proposition must remain exactly here.\n\n## Details\n')
BINDING = {'path': '04_requirement/mock.md', 'atom_id': 'MOCK-R-001', 'version': 1,
           'sha256': hashlib.sha256(SOURCE.encode()).hexdigest()}


def mapping():
    title_end = BODY.index('\n') + 1
    return {'source_body_sha256': hashlib.sha256(BODY.encode()).hexdigest(), 'sections': [
        {'heading': '# Summary', 'source_span': [0, title_end],
         'state': 'legacy_h1_to_summary_value', 'provenance': 'Bound first body H1.'},
        {'heading': '## Scope', 'source_span': None, 'state': 'unassessed_author_proposal',
         'provenance': 'Caller supplied a temporary layout proposal.',
         'proposed_text': 'This rule governs review admission.'},
        {'heading': '## Claim', 'source_span': [title_end, len(BODY)],
         'state': 'verbatim_carried', 'provenance': 'All remaining original body bytes.'},
        {'heading': '## Details', 'source_span': None, 'state': 'unassessed_absent',
         'provenance': 'No Details prose is proposed.'},
    ]}


class LayoutPreviewTests(unittest.TestCase):
    def test_preview_is_no_write_unclassified_and_inputs_unchanged(self):
        before = copy.deepcopy((BINDING, SOURCE, CANDIDATE, mapping()))
        result = admit_layout_preview(BINDING, SOURCE, CANDIDATE, section_mapping=mapping())
        self.assertEqual(result['result'], 'preview')
        self.assertFalse(result['source_mutation_permitted'])
        self.assertEqual(result['classification'], 'unclassified')
        self.assertFalse(result['equivalence_claimed'])
        self.assertEqual(before, (BINDING, SOURCE, CANDIDATE, mapping()))
        supplied = mapping()
        evidence = admit_layout_preview(BINDING, SOURCE, CANDIDATE, section_mapping=supplied)
        supplied['sections'][1]['proposed_text'] = 'Mutated after admission.'
        self.assertEqual(evidence['section_mapping']['sections'][1]['proposed_text'],
                         'This rule governs review admission.')

    def test_rejects_identity_frontmatter_and_body_rewrites(self):
        cases = []
        changed = dict(BINDING, atom_id='OTHER')
        cases.append((changed, SOURCE, CANDIDATE, mapping()))
        cases.append((BINDING, SOURCE, CANDIDATE.replace('updated_at:', 'created_at:'), mapping()))
        cases.append((BINDING, SOURCE, CANDIDATE.replace('proposition', 'claim'), mapping()))
        cases.append((BINDING, SOURCE, CANDIDATE.replace('here.\n\n## Details',
            'here.\nNew obligation.\n\n## Details'), mapping()))
        cases.append((BINDING, SOURCE, CANDIDATE.replace('## Scope\nThis', '## Scope\n# Injected\nThis'), mapping()))
        for binding, source, candidate, section_map in cases:
            with self.subTest(candidate=candidate):
                self.assertEqual(admit_layout_preview(binding, source, candidate,
                    section_mapping=section_map)['result'], 'rejected')

    def test_rejects_unbound_or_inferred_summary_mapping(self):
        for mutate in ('hash', 'summary_span', 'filename'):
            section_map = mapping()
            if mutate == 'hash':
                section_map['source_body_sha256'] = '0' * 64
            elif mutate == 'summary_span':
                section_map['sections'][0]['source_span'] = [1, BODY.index('\n') + 1]
            else:
                section_map['sections'][0]['source_span'] = None
                section_map['sections'][0]['filename'] = 'mock.md'
            with self.subTest(mutate=mutate):
                self.assertEqual(admit_layout_preview(BINDING, SOURCE, CANDIDATE,
                    section_mapping=section_map)['result'], 'rejected')

    def test_rejects_blank_scope_and_legacy_subheadings(self):
        section_map = mapping()
        section_map['sections'][1]['proposed_text'] = ''
        self.assertEqual(admit_layout_preview(BINDING, SOURCE, CANDIDATE,
            section_mapping=section_map)['result'], 'rejected')
        headed_source = SOURCE + '\n## Existing detail\nDo not relocate me.\n'
        headed_binding = dict(BINDING, sha256=hashlib.sha256(headed_source.encode()).hexdigest())
        self.assertEqual(admit_layout_preview(headed_binding, headed_source, CANDIDATE,
            section_mapping=mapping())['result'], 'rejected')

    def test_rejects_proposed_scope_heading_even_when_candidate_matches_it(self):
        section_map = mapping()
        section_map['sections'][1]['proposed_text'] = '# New obligation\nDo it.'
        candidate = CANDIDATE.replace('This rule governs review admission.',
                                      '# New obligation\nDo it.')
        self.assertEqual(admit_layout_preview(BINDING, SOURCE, candidate,
            section_mapping=section_map)['result'], 'rejected')

    def test_boolean_version_is_not_integer_identity(self):
        raw = SOURCE.replace('version: 1', 'version: true')
        binding = dict(BINDING, sha256=hashlib.sha256(raw.encode()).hexdigest())
        candidate = CANDIDATE.replace('version: 1', 'version: true')
        self.assertEqual(admit_layout_preview(binding, raw, candidate,
            section_mapping=mapping())['result'], 'rejected')

    def test_registered_summary_heading_is_not_a_legacy_summary_value(self):
        raw = SOURCE.replace('# Legacy atom', '# Summary')
        binding = dict(BINDING, sha256=hashlib.sha256(raw.encode()).hexdigest())
        candidate = CANDIDATE.replace('Legacy atom', 'Summary')
        body = raw[_FRONTMATTER_END:]
        section_map = mapping()
        section_map['source_body_sha256'] = hashlib.sha256(body.encode()).hexdigest()
        section_map['sections'][0]['source_span'] = [0, body.index('\n') + 1]
        section_map['sections'][2]['source_span'] = [body.index('\n') + 1, len(body)]
        self.assertEqual(admit_layout_preview(binding, raw, candidate,
            section_mapping=section_map)['result'], 'rejected')
