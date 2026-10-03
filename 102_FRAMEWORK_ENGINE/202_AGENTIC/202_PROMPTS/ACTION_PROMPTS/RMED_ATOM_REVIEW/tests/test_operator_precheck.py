import unittest
from operator_precheck import rendering_candidates, validate_operator_coverage, word_inventory

OPS = ['must not', 'must', 'only', 'when', 'and', 'in']
SOURCE = '''---
version: 1
---
# Summary
Record Projection dependency provenance only when required
## Scope
provenance.
## Claim
the Atom **must not** lose provenance **when** required.
## Details
'''


class OperatorPrecheckTests(unittest.TestCase):
    def test_registry_requires_all_categories(self):
        with self.assertRaisesRegex(ValueError, 'complete'):
            word_inventory('1. modality: **must**')

    def test_indented_literals_and_list_continuations_need_classification(self):
        # Never blanket-mask indentation: the second example is list prose.
        base = SOURCE.replace('only when', '**only** **when**')
        raw = base + '\n    must stay literal\n\n- prose\n    and a continuation\n'
        candidates = rendering_candidates(raw, OPS)
        self.assertEqual([x['excerpt'] for x in candidates], ['must', 'and'])
        with self.assertRaisesRegex(ValueError, 'coverage'):
            validate_operator_coverage({'status': 'passed'}, raw, OPS)

    def test_summary_is_included_and_intact_multiword_bold_is_excluded(self):
        self.assertEqual([x['excerpt'] for x in rendering_candidates(SOURCE, OPS)], ['only', 'when'])

    def test_code_headings_and_word_fragments_are_excluded(self):
        raw = SOURCE.replace('only when', '**only** **when**') + '''
### only when
`only when` remains literal.
```text
only when
```
inside ordinary rendering.
read-only and-code append-only facts.
'''
        self.assertEqual(rendering_candidates(raw, OPS), [])

    def test_unquoted_prose_examples_need_review_not_automatic_failure(self):
        candidates = rendering_candidates(SOURCE, OPS)
        check = {'status': 'passed', 'operator_observations': [dict(x,
            disposition='literal_example', reason='Mock illustration, not a real judgment') for x in candidates]}
        validate_operator_coverage(check, SOURCE, OPS)

    def test_old_generic_pass_cannot_skip_summary_candidates(self):
        with self.assertRaisesRegex(ValueError, 'coverage'):
            validate_operator_coverage({'status': 'passed'}, SOURCE, OPS)

    def test_repeated_occurrences_need_separate_dispositions(self):
        candidates = rendering_candidates(SOURCE + '\nonly again.\n', OPS)
        self.assertEqual(len(candidates), 3)

    def test_incomplete_review_is_allowed_to_report_blocked(self):
        validate_operator_coverage({'status': 'blocked'}, SOURCE, OPS)

    def test_empty_reason_or_shifted_offsets_do_not_establish_pass(self):
        candidates = rendering_candidates(SOURCE, OPS)
        for mutate in (lambda x: x.update(reason=''), lambda x: x.update(offset=0)):
            observed = [dict(x, disposition='non_operator_usage', reason='specific') for x in candidates]
            mutate(observed[0])
            with self.assertRaises(ValueError):
                validate_operator_coverage({'status': 'passed', 'operator_observations': observed}, SOURCE, OPS)
