"""Regression evidence from the random-20 audit; not LLM-judgment simulation."""
import copy
import json
import unittest
from pathlib import Path

from test_split_evaluation import context, contract, gap, merge_evaluations, part

HERE = Path(__file__).resolve().parents[1]


class ReviewRegressions(unittest.TestCase):
    def test_self_reference_preserves_term_case_without_entity_resolution(self):
        cce = (HERE / 'evaluate_cce.prompt.md').read_text()
        self.assertIn('`Term` is itself a Term', cce)
        self.assertIn('`Evaluation` remains a Term inside E Atoms', cce)
        self.assertIn('Entity-target resolution is deferred', cce)

    def test_citation_shape_is_local_without_target_lookup(self):
        cce = (HERE / 'evaluate_cce.prompt.md').read_text()
        self.assertIn('complete filename without `.md` or directory path', cce)
        self.assertIn('Do not fetch the cited Atom', cce)
        self.assertIn('Missing target inventories do not block', cce)

    def test_no_alignment_or_entity_inventory_in_current_coherence(self):
        text = (HERE / 'evaluate_coherence.prompt.md').read_text()
        self.assertIn('No subject_inventory, governed_entity, alignment, content_role', text)
        self.assertIn('resolving the wider graph is not this review', text)
        self.assertNotIn('allowed_value_evidence:', text)
        self.assertNotIn('candidate_definition_evidence', text)

    def test_composite_claim_and_scope_are_not_split_by_punctuation(self):
        text = (HERE / 'evaluate_coherence.prompt.md').read_text()
        self.assertIn('Multiple sentences, bullets, conditions or values', text)
        self.assertIn('sharing one Subject does not prove atomicity', text)
        self.assertIn('Never turn required outcomes into applicability preconditions', text)
        self.assertIn('exclude noncompliant cases', text)

    def test_only_confirmed_defects_enter_findings(self):
        for name in ('cce','properties','coherence'):
            text = (HERE / f'evaluate_{name}.prompt.md').read_text()
            self.assertIn('confirmed defects only', text.casefold())
            self.assertIn('coverage_gaps', text)

    def test_context_is_content_not_an_arbitrary_key_name(self):
        for name in ('cce','properties','coherence'):
            text = (HERE / f'evaluate_{name}.prompt.md').read_text()
            self.assertIn('content, not container key names', text)
            self.assertIn('unrelated', text)

    def test_local_properties_do_not_resolve_authors_or_graphs(self):
        text = (HERE / 'evaluate_properties.prompt.md').read_text()
        self.assertIn('Do not infer lexical sorting', text)
        self.assertIn('No Operator registry lookup', text)
        self.assertIn('shape only, not Entity validity or coverage', text)
        self.assertIn('no existence, status, inverse or graph checks', text)
        self.assertIn('Properties owns missing, duplicate, or misplaced headings',
                      (HERE / 'evaluate_coherence.prompt.md').read_text())

    def test_cce_keeps_the_previous_rendering_guards(self):
        text = (HERE / 'evaluate_cce.prompt.md').read_text()
        for phrase in ('not every bold word', 'Inventory all capitalized sentence, bullet, and table-cell starts',
                       'justify each retained exact-case token against bound authority', 'Do not sample starts',
                       'Set coordination in Scope still uses operators', 'Table headers are not sentence/list starts',
                       '"before/after states" by syntactic function'):
            self.assertIn(phrase, text)

    def test_summary_keeps_known_defects_when_coverage_is_blocked(self):
        evaluations = []
        parts = [part(group) for group in contract.GROUPS]
        prop = parts[1]
        finding = {"kind": "omission", "obligation_id": "scope-heading", "location": "body", "excerpt": "missing Scope",
                   "reason": "required section absent", "proposed_fix": "add Scope",
                   "confidence": 1.0}
        prop["checks"][0].update(status="blocked", findings=[finding])
        prop["checks"][0]["obligation_resolutions"] = [{"id": "scope-heading", "state": "missing",
            "local_required": True, "reason": "Required local heading absent",
            "support": [{"authority": "MOCK-R-002@1", "excerpt": "Required Scope heading."}]}]
        prop.update(result="blocked", coverage_gaps=[gap("properties", "Missing structure context")])
        evaluations.append(merge_evaluations(parts))
        before = copy.deepcopy(evaluations)
        summary = contract.summarize_evaluations(evaluations, context=context())
        self.assertEqual(summary["atoms_with_confirmed_findings"], 1)
        self.assertEqual(summary["atoms_with_coverage_gaps"], 1)
        self.assertEqual(summary["fully_passed_atoms"], 0)
        self.assertEqual(summary["check_counts"]["properties"]["atoms_with_findings"], 1)
        self.assertEqual(evaluations, before)

    def test_summary_rejects_duplicate_sources_and_inconsistent_outer_result(self):
        evaluation = merge_evaluations([part(group) for group in contract.GROUPS])
        with self.assertRaises(ValueError):
            contract.summarize_evaluations([evaluation, evaluation], context=context())
        evaluation["result"] = "failed"
        with self.assertRaises(ValueError):
            contract.summarize_evaluations([evaluation], context=context())

    def test_summary_counts_mixed_results_without_adding_overlapping_groups(self):
        evaluations = []
        for index in range(3):
            parts = [part(group) for group in contract.GROUPS]
            for entry in parts:
                entry["source"]["path"] = f"mock-{index}.md"
            if index == 1:
                for entry in parts[:2]:
                    entry["checks"][0].update(status="failed", findings=[{
                        "kind": "violation",
                        "location": "body", "excerpt": "bad fixture", "reason": "invalid",
                        "proposed_fix": "repair fixture", "confidence": 1.0}])
                    entry["result"] = "failed"
            if index == 2:
                parts[1]["checks"][0]["status"] = "blocked"
                parts[1].update(result="blocked", coverage_gaps=[gap("properties", "missing context")])
            evaluations.append(merge_evaluations(parts))
        summary = contract.summarize_evaluations(evaluations, context=context())
        self.assertEqual(summary["atoms"], 3)
        self.assertEqual(summary["fully_passed_atoms"], 1)
        self.assertEqual(summary["atoms_with_confirmed_findings"], 1)
        self.assertEqual(summary["atoms_with_coverage_gaps"], 1)
        self.assertEqual(summary["check_counts"]["properties"], {
            "passed": 1, "failed": 1, "blocked": 1, "atoms_with_findings": 1, "findings": 1})
        self.assertEqual(contract.summarize_evaluations([], context=context())["atoms"], 0)

    def test_adjudication_examples_are_not_new_authority(self):
        cases = json.loads((HERE / "tests/fixtures/adjudication_cases.json").read_text())
        self.assertEqual(len(cases), 17)
        self.assertEqual(len({c["id"] for c in cases}), 17)
        self.assertTrue(all(c["classification"] in {"defect", "gap", "not_a_defect"} for c in cases))


if __name__ == "__main__":
    unittest.main()
