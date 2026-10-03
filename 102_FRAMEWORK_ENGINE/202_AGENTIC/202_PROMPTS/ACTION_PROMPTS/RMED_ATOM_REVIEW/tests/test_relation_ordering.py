"""Atom-ID ordering is presentation, never graph semantics."""
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from relation_ordering import atom_id_key, ordered_atom_ids, validate_ordering_policy
from review_evidence import ReviewContext
from test_split_evaluation import source, RULE_TEXT


class RelationOrderingTests(unittest.TestCase):
    def policy(self):
        return {'key': 'atom_id', 'direction': 'ascending', 'source': 'operator_input',
                'instruction': 'just atom ID', 'provenance': 'Operator reply, 2026-09-27'}

    def test_numeric_serial_within_id_prefix(self):
        self.assertEqual(ordered_atom_ids(['CA-R-10', 'CA-R-2', 'CA-R-1']),
                         ['CA-R-1', 'CA-R-2', 'CA-R-10'])

    def test_role_prefix_is_part_of_atom_id(self):
        self.assertEqual(ordered_atom_ids(['CA-R-1441', 'CA-M-279', 'CA-D-408', 'CA-D-407']),
                         ['CA-D-407', 'CA-D-408', 'CA-M-279', 'CA-R-1441'])

    def test_legacy_namespace_remains_an_id(self):
        self.assertEqual(atom_id_key('CAPRMEDIO-GOV-EVAL-003'),
                         ('CAPRMEDIO-GOV-EVAL', 3, 'CAPRMEDIO-GOV-EVAL-003'))

    def test_preserves_exact_strings_and_does_not_mutate_input(self):
        original = ['CA-O-015', 'CA-O-012']
        self.assertEqual(ordered_atom_ids(original), ['CA-O-012', 'CA-O-015'])
        self.assertEqual(original, ['CA-O-015', 'CA-O-012'])

    def test_same_numeric_serial_uses_only_exact_atom_id(self):
        self.assertEqual(ordered_atom_ids(['CA-R-2', 'CA-R-02']), ['CA-R-02', 'CA-R-2'])

    def test_no_path_revision_or_summary_fallback(self):
        for invalid in ['CA-R-2@9', 'CA-R-2.md', '/tmp/CA-R-2', 'CA-R-2--summary',
                        'ca-r-2', '', 'CA-R-x', None, 2]:
            with self.subTest(value=invalid), self.assertRaises(ValueError):
                atom_id_key(invalid)

    def test_no_silent_deduplication_or_invalid_container(self):
        for invalid in [['CA-R-2', 'CA-R-2'], 'CA-R-2', None]:
            with self.subTest(value=invalid), self.assertRaises(ValueError):
                ordered_atom_ids(invalid)

    def test_empty_and_singleton_order(self):
        self.assertEqual(ordered_atom_ids([]), [])
        self.assertEqual(ordered_atom_ids(['CA-R-2']), ['CA-R-2'])

    def test_missing_policy_is_not_an_implicit_default(self):
        self.assertIsNone(validate_ordering_policy(None))
        self.assertEqual(validate_ordering_policy(self.policy()), self.policy())

    def test_only_explicit_caller_atom_id_policy(self):
        for delta in [{'key': 'filename'}, {'direction': 'descending'}, {'source': 'reviewer'},
                      {'instruction': ''}, {'provenance': ''}, {'tie_breaker': 'version'}]:
            with self.subTest(delta=delta), self.assertRaises(ValueError):
                validate_ordering_policy(self.policy() | delta)

    def test_review_context_binds_explicit_policy_in_hash(self):
        packet = {'confidence_threshold': .99,
                  'sources': [source('rule.md', 'MOCK-R-002', RULE_TEXT)]}
        unselected = ReviewContext(packet)
        self.assertIsNone(unselected.relation_ordering)
        packet['relation_ordering'] = self.policy()
        selected = ReviewContext(packet)
        self.assertEqual(selected.relation_ordering, self.policy())
        self.assertNotEqual(selected.sha256, unselected.sha256)
        packet['relation_ordering']['key'] = 'filename'
        self.assertEqual(selected.relation_ordering['key'], 'atom_id')
        with self.assertRaises(ValueError):
            ReviewContext(packet)


if __name__ == '__main__':
    unittest.main()
