"""Incomplete-review regressions, not semantic Entity inference tests."""
import unittest

from audit_literal_coverage import audit


SOURCE = '''---
subjects:
  governs: Action
  depends_on: [Step, Tool]
---
# Summary
Action and Step
## Claim
Tool calls execute the Action.
'''


def report(mentions):
    return {'checks': [{'id': 'subjects', 'subject_inventory': {'mentions': mentions}}]}


class LiteralCoverageQA(unittest.TestCase):
    def test_first_ambiguity_does_not_cover_the_rest(self):
        mentions = [{'location': 'Claim', 'excerpt': 'Tool calls'}]
        gaps = audit(SOURCE, report(mentions))
        self.assertEqual([g['literal_anchor'] for g in gaps], ['Action', 'Step', 'Action'])

    def test_compound_reference_needs_inspection_not_separate_entities(self):
        raw = SOURCE.replace('Tool calls execute the Action.', 'Step/Invocation executes the Action.')
        mentions = [
            {'location': 'Summary', 'excerpt': 'Action and Step'},
            {'location': 'Claim', 'excerpt': 'the Action'}]
        self.assertEqual(audit(raw, report(mentions)), [])

    def test_same_quote_in_other_section_is_not_coverage(self):
        mentions = [{'location': 'Claim', 'excerpt': 'Action'}]
        gaps = audit(SOURCE, report(mentions))
        self.assertIn({'section': 'body:1:# Summary', 'literal_anchor': 'Action'}, gaps)


if __name__ == '__main__':
    unittest.main()
