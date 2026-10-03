"""Lossless Summary rendering does not replace its identity-bearing value."""
import unittest

from test_repair_gate import caller_preflight
from test_local_repair import local_inputs
from repair_gate import _same_summary_value, admit_proposal


class SummaryRendering(unittest.TestCase):
    def test_plain_and_strong_text_keep_the_exact_same_value(self):
        for before, after in (
            ('Record provenance only when required', 'Record provenance **only** **when** required'),
            ('Terms in CORE_META_MODEL', 'Terms **in** CORE_META_MODEL'),
            ('Keep A', 'Keep **A**'),
            ('Keep **A**', 'Keep A'),
        ):
            with self.subTest(before=before, after=after):
                self.assertTrue(_same_summary_value(before, after))

    def test_actual_word_case_punctuation_and_space_changes_still_fail(self):
        for after in ('Other rule', '**atom** rule', 'Atom rule.', 'Atom  rule',
                      'Atom **new** rule', 'Atom **rule**\nextra'):
            with self.subTest(after=after):
                self.assertFalse(_same_summary_value('Atom rule', after))

    def test_unsupported_markup_is_not_losslessly_inferred(self):
        for after in ('Atom *rule*', 'Atom ***rule***', 'Atom ** rule **',
                      'Atom `rule`', 'Atom [rule](target)', 'Atom <b>rule</b>',
                      r'Atom \**rule**', 'Atom **rule', 'Atom rule**'):
            with self.subTest(after=after):
                self.assertFalse(_same_summary_value('Atom rule', after))

    def test_local_formatting_admission_preserves_identity_and_no_write_permission(self):
        context, evaluation, proposal, permission = local_inputs()
        proposal['outputs'][0]['text'] = proposal['outputs'][0]['text'].replace(
            'Atom rule', 'Atom **rule**')
        proposal['after_summary'] = 'Atom **rule**'
        result = admit_proposal(evaluation, proposal, context=context,
                                permission=permission, preflight=caller_preflight(proposal))
        self.assertEqual(result['result'], 'candidate')
        self.assertFalse(result['source_mutation_permitted'])

    def test_actual_summary_change_is_still_replacement_only(self):
        context, evaluation, proposal, permission = local_inputs()
        proposal['outputs'][0]['text'] = proposal['outputs'][0]['text'].replace(
            'Atom rule', 'Atom **new** rule')
        proposal['after_summary'] = 'Atom **new** rule'
        with self.assertRaisesRegex(ValueError, 'Summary change requires replacement'):
            admit_proposal(evaluation, proposal, context=context,
                           permission=permission, preflight=caller_preflight(proposal))


if __name__ == '__main__':
    unittest.main()
