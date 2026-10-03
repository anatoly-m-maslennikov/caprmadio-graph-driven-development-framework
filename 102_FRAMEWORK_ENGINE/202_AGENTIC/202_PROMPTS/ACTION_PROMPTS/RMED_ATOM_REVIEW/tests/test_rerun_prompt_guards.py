"""Instruction regressions; real reviewer results are separate run evidence."""
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]


class RerunPromptGuards(unittest.TestCase):
    def test_title_and_operator_alias_boundaries(self):
        prompt = (HERE / 'evaluate_cce.prompt.md').read_text()
        for text in ('title-like Summary', 'bound alias rule', 'two plausible readings',
                     'grammatical referent'):
            self.assertIn(text, prompt)

    def test_summary_omission_is_not_automatically_broadening(self):
        prompt = (HERE / 'evaluate_coherence.prompt.md').read_text()
        self.assertIn('second standalone universal Claim', prompt)
        self.assertIn('positively asserts or implies', prompt)
        self.assertIn('Always allow X', prompt)

    def test_relation_registry_is_not_required_for_shape_review(self):
        prompt = (HERE / 'evaluate_properties.prompt.md').read_text()
        self.assertIn('Absence of a graph-kind registry does not block', prompt)
        self.assertIn('explicit local', prompt)

    def test_default_fix_does_not_require_a_closure_or_recheck_gate(self):
        prompt = (HERE / 'CA-O-110.prompt.md').read_text()
        self.assertIn('fixed_not_rechecked', prompt)
        self.assertIn('does not recheck saved output', prompt)
        self.assertNotIn('closure_freshness.close_batch', prompt)

    def test_new_runs_require_operator_precheck_including_summary(self):
        prompt = (HERE / 'evaluate_atom.prompt.md').read_text()
        self.assertIn('review_constraints.operator_precheck', prompt)
        self.assertIn('includes Summary', prompt)

    def test_context_and_composite_cases_are_not_automatically_missing(self):
        prompt = (HERE / 'evaluate_coherence.prompt.md').read_text()
        self.assertIn('Cases of one disposition rule', prompt)
        self.assertIn('Read Scope and Claim together', prompt)

    def test_compact_vocabulary_is_not_a_complete_entity_registry(self):
        prompt = (HERE / 'evaluate_cce.prompt.md').read_text()
        self.assertIn('lowercase compound suffix', prompt)
        self.assertIn('absence alone proves no spelling violation', prompt)

    def test_prose_cardinality_is_reviewed_without_rewriting_narrative(self):
        prompt = (HERE / 'evaluate_cce.prompt.md').read_text()
        self.assertIn('"two IDs" and "one identity"', prompt)
        self.assertIn('execution frequency as Entity cardinality', prompt)
