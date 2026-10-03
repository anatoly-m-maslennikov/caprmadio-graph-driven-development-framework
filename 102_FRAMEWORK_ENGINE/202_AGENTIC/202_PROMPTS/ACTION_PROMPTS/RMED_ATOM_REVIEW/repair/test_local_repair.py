"""Local-profile repair boundaries and compatibility with the existing gate."""
from copy import deepcopy
import unittest

from test_repair_gate import (
    inputs, caller_preflight, contract, source, SOURCE_TEXT, RULE_TEXT, admit_proposal,
)
from repair_gate import _local_repair_boundary


def local_inputs():
    evaluation, proposal, permission = inputs()
    records = [source('mock.md','MOCK-R-001',SOURCE_TEXT), source('rule.md','MOCK-R-002',RULE_TEXT)]
    context = contract.ReviewContext({
        'confidence_threshold':.99,
        'review_constraints':{'report_contract':6,'review_profile':'atom_local'},
        'sources':records, 'candidate_bindings':[records[0]['binding']],
        'authority_bindings':[records[1]['binding']],
    })
    parts = deepcopy(evaluation['parts'])
    for report in parts:
        report.update(contract_version=6,review_profile='atom_local',context_sha256=context.sha256)
        report['checks'] = [r for r in report['checks'] if r['id'] in contract.LOCAL_GROUPS[report['evaluator']]]
        for row in report['checks']: row.pop('subject_inventory',None)
    evaluation = contract.merge_evaluations(parts,context=context)
    proposal['context_sha256'] = context.sha256
    return context,evaluation,proposal,permission


class LocalRepair(unittest.TestCase):
    def test_formatting_proposal_is_supported_without_graph_context(self):
        context,evaluation,proposal,permission = local_inputs()
        result = admit_proposal(evaluation,proposal,context=context,permission=permission,
                                preflight=caller_preflight(proposal))
        self.assertEqual(result['result'],'candidate')
        self.assertFalse(result['source_mutation_permitted'])
        self.assertIn('Independent local evaluation',result['next'])
        self.assertNotIn('affected-reference',result['next'])

    def test_entity_target_change_is_rejected(self):
        context,evaluation,proposal,permission = local_inputs()
        proposal['disposition'] = 'revision'; permission['dispositions'] = ['revision']
        proposal['outputs'][0]['text'] = proposal['outputs'][0]['text'].replace('governs: Atom','governs: Artifact')
        with self.assertRaisesRegex(ValueError,'preserve Subject and relation targets'):
            admit_proposal(evaluation,proposal,context=context,permission=permission,
                           preflight=caller_preflight(proposal))

    def test_target_shape_normalization_can_preserve_values(self):
        proposal = {'source':{'path':'mock.md'},'disposition':'revision'}
        original = SOURCE_TEXT.replace('governs: Atom','governs: [Atom]')
        output = {'path':'mock.md','text':SOURCE_TEXT}
        _local_repair_boundary(proposal,output,original)

    def test_new_relations_or_changed_target_values_are_rejected(self):
        proposal = {'source':{'path':'mock.md'},'disposition':'revision'}
        for addition in ('relations: {relates_to: [MOCK-R-002]}\n',
                         'subjects: {governs: Other}\n'):
            output = {'path':'mock.md','text':SOURCE_TEXT.replace('subjects:\n  governs: Atom\n',addition)}
            with self.subTest(addition=addition), self.assertRaises(ValueError):
                _local_repair_boundary(proposal,output,SOURCE_TEXT)

    def test_identity_changes_and_moves_require_separate_handling(self):
        for disposition,path in (('split','mock.md'),('replacement','mock.md'),('revision','new.md')):
            proposal = {'source':{'path':'mock.md'},'disposition':disposition}
            with self.subTest(disposition=disposition,path=path), self.assertRaisesRegex(ValueError,'separate authorized run'):
                _local_repair_boundary(proposal,{'path':path,'text':SOURCE_TEXT},SOURCE_TEXT)


if __name__ == '__main__':
    unittest.main()
