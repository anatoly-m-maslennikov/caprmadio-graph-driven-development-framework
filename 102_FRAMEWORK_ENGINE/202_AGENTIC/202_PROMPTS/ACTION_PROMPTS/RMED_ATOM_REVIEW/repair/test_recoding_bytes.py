"""Independent-review regressions for narrow carrier repairs."""
import copy
import unittest

from test_repair_gate import (
    admit_proposal, caller_preflight, context, inputs, recoding_inputs,
)


class CarrierPreservationTests(unittest.TestCase):
    def test_recoding_rejects_equal_yaml_with_changed_representation(self):
        for mutation in ('quotes', 'comment', 'order', 'spaces'):
            review_context, evaluation, proposal, permission = recoding_inputs()
            raw = proposal['outputs'][0]['text']
            if mutation == 'quotes':
                raw = raw.replace('content_role: Requirement', 'content_role: "Requirement"')
            elif mutation == 'comment':
                raw = raw.replace('content_role: Requirement', '# inserted comment\ncontent_role: Requirement')
            elif mutation == 'order':
                raw = raw.replace('atom_id: MOCK-R-001\nversion: 1', 'version: 1\natom_id: MOCK-R-001')
            else:
                raw = raw.replace('content_role: Requirement', 'content_role:  Requirement')
            proposal['outputs'][0]['text'] = raw
            with self.subTest(mutation=mutation), self.assertRaisesRegex(ValueError, 'frontmatter bytes'):
                admit_proposal(evaluation, proposal, context=review_context, permission=permission,
                               preflight=caller_preflight(proposal))

    def test_replacement_and_split_reject_predecessor_path_reuse(self):
        for disposition in ('replacement', 'split'):
            evaluation, proposal, permission = inputs()
            proposal['disposition'] = disposition
            permission['dispositions'] = [disposition]
            output = proposal['outputs'][0]
            output['atom_id'] = 'MOCK-R-010'
            output['text'] = output['text'].replace('MOCK-R-001', 'MOCK-R-010')
            if disposition == 'split':
                other = copy.deepcopy(output)
                other.update(path='other.md', atom_id='MOCK-R-011',
                             text=other['text'].replace('MOCK-R-010', 'MOCK-R-011'))
                proposal['outputs'].append(other)
                permission['paths'].append('other.md')
            with self.subTest(disposition=disposition), self.assertRaisesRegex(ValueError, 'predecessor path'):
                admit_proposal(evaluation, proposal, context=context(), permission=permission,
                               preflight=caller_preflight(proposal))


if __name__ == '__main__':
    unittest.main()
