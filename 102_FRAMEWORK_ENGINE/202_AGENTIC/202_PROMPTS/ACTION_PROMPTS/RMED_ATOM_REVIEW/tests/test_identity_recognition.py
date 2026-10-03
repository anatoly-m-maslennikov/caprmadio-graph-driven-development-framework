"""Literal identity recognition must neither need nor pretend to prove meaning."""
import unittest

from test_split_evaluation import part, context, contract, source, SOURCE_TEXT


class IdentityRecognition(unittest.TestCase):
    def test_exact_literal_can_use_active_taxonomy_admission(self):
        raw = '---\nstatus: Active\ncontent_role: Requirement\nsubjects:\n  governs: Atom\n---\n# Classification\nThe Term Atom is narrower than Artifact.\n'
        rule = source('rule.md', 'MOCK-R-002', raw)
        ctx = contract.ReviewContext({'confidence_threshold': .99, 'sources': [
            source('mock.md', 'MOCK-R-001', SOURCE_TEXT), rule]})
        response = part('coherence')
        response.update(context_sha256=ctx.sha256, authority_sources=[rule['binding']])
        mention = response['checks'][0]['subject_inventory']['mentions'][0]
        mention.update(resolution_basis='identity', definitions=[{
            'authority': 'MOCK-R-002@1', 'excerpt': 'The Term Atom is narrower than Artifact.'}])
        contract.validate_part(response, context=ctx)

    def test_identity_mode_cannot_resolve_a_paraphrase(self):
        response = part('coherence')
        mention = response['checks'][0]['subject_inventory']['mentions'][0]
        mention.update(resolution_basis='identity', excerpt='must comply')
        with self.assertRaisesRegex(ValueError, 'exact canonical literal'):
            contract.validate_part(response, context=context())

    def test_missing_resolution_basis_cannot_silently_prove_meaning(self):
        response = part('coherence')
        response['checks'][0]['subject_inventory']['mentions'][0].pop('resolution_basis')
        with self.assertRaisesRegex(ValueError, 'resolution basis'):
            contract.validate_part(response, context=context())

    def test_prior_contract_is_not_relabelled(self):
        response = part('coherence')
        response['contract_version'] = 3
        with self.assertRaisesRegex(ValueError, 'contract_version 4'):
            contract.validate_part(response, context=context())


if __name__ == '__main__':
    unittest.main()
