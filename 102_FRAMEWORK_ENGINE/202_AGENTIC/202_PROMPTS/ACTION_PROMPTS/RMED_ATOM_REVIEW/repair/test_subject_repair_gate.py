"""Carrier-only dependency repairs require exact independent final evidence."""
import copy
import hashlib
import unittest

from test_composed_revision import composition_inputs
from test_layout_repair_gate import digest
from evaluation_contract import merge_evaluations
from review_evidence import ReviewContext
from layout_repair_gate import authority_digest
from subject_repair_gate import admit_subject_recoding


def fixture():
    ctx, evaluation, proposal, permission = composition_inputs()
    packet = dict(confidence_threshold=.99, review_constraints={'report_contract': 5},
        sources=copy.deepcopy(list(ctx._sources.values())),
        resources={}, preflight={'authority': {'state': 'available', 'reason': 'Synthetic bound rules.'}})
    packet['authority_bindings'] = [s['binding'] for s in packet['sources'][1:]]
    final_packet = copy.deepcopy(packet)
    final_packet['sources'][0] = dict(binding={}, text=proposal['outputs'][0]['text'])
    proposal['disposition'] = 'subject_recoding'
    permission['dispositions'] = ['subject_recoding']
    final_eval = copy.deepcopy(evaluation)
    for part in final_eval['parts']:
        part.update(result='passed', coverage_gaps=[])
        for row in part['checks']:
            row.update(status='passed', findings=[], obligation_resolutions=[])
    data = dict(evaluation=evaluation, proposal=proposal, context=packet, final_context=final_packet,
                final_evaluation=final_eval, permission=permission, preflight={})
    rebind(data)
    return data


def rebind(data):
    output = data['proposal']['outputs'][0]
    final_record = data['final_context']['sources'][0]
    final_record.update(text=output['text'], binding=dict(path=output['path'], atom_id=output['atom_id'],
        version=output['version'], sha256=hashlib.sha256(output['text'].encode()).hexdigest()))
    for packet_name, report_name in (('context', 'evaluation'), ('final_context', 'final_evaluation')):
        packet = data[packet_name]
        for record in packet['sources']:
            record['binding']['sha256'] = hashlib.sha256(record['text'].encode()).hexdigest()
        packet['authority_bindings'] = [s['binding'] for s in packet['sources'][1:]]
        ctx = ReviewContext(packet)
        for part in data[report_name]['parts']:
            part.update(source=packet['sources'][0]['binding'], context_sha256=ctx.sha256,
                        authority_sources=packet['authority_bindings'])
        data[report_name] = merge_evaluations(data[report_name]['parts'], context=ctx)
    original_ctx, final_ctx = ReviewContext(data['context']), ReviewContext(data['final_context'])
    data['proposal'].update(source=data['evaluation']['source'], context_sha256=original_ctx.sha256)
    expected = dict(source=data['evaluation']['source'], outputs=[final_record['binding']],
                    context_sha256=original_ctx.sha256, final_context_sha256=final_ctx.sha256)
    data['preflight'] = dict(expected, provenance='Caller bound exact original and final.',
        attempt=0, retry_budget=0, authority_aliases=[],
        freshness=dict(source=expected['source'], authority_sha256=authority_digest(data['context']),
                       provenance='Caller re-read source and authority.'),
        final_review=dict(source=final_record['binding'], context_sha256=final_ctx.sha256,
            evaluation_sha256=digest(data['final_evaluation']), independent=True, provenance='Separate final reviewer.'),
        identity_assessment=dict(expected, classification='carrier_only', confidence=.99,
                                 independent=True, provenance='Separate full-delta identity reviewer.'))


class SubjectRepairGateTests(unittest.TestCase):
    def test_exact_dependency_and_role_echo_repair_is_candidate_only(self):
        data = fixture()
        before = copy.deepcopy(data)
        result = admit_subject_recoding(**data)
        self.assertEqual(result['result'], 'candidate')
        self.assertFalse(result['source_mutation_permitted'])
        self.assertEqual(result['outputs'][0]['version'], 1)
        self.assertEqual(result['original_evaluation_sha256'], digest(data['evaluation']))
        self.assertEqual(result['final_evaluation_sha256'], digest(data['final_evaluation']))
        self.assertEqual(before, data)

    def test_block_dependency_list_is_supported(self):
        data = fixture()
        data['proposal']['outputs'][0]['text'] = data['proposal']['outputs'][0]['text'].replace(
            '  depends_on: ["Main Content"]', '  depends_on:\n    - "Main Content"')
        rebind(data)
        self.assertEqual(admit_subject_recoding(**data)['result'], 'candidate')

    def test_consistently_bound_other_frontmatter_body_and_version_changes_reject(self):
        for old, new, error in (('Main Content carries this rule.', 'Main Content carries another rule.', 'Markdown'),
                ('Atom rule', 'Another Summary', 'Summary|Markdown'),
                ('updated_at:', 'author: Different\nupdated_at:', 'frontmatter|metadata'),
                ('content_role: Requirement', 'content_role: "Requirement"', 'frontmatter bytes'),
                ('version: 1', 'version: 2', 'version|metadata'),
                ('content_role: Requirement', 'content_role: Requirement\ntype: Boundary', 'Type|path')):
            data = fixture()
            output = data['proposal']['outputs'][0]
            output['text'] = output['text'].replace(old, new)
            if old == 'version: 1':
                output['version'] = 2
            rebind(data)
            with self.subTest(old=old), self.assertRaisesRegex(ValueError, error):
                admit_subject_recoding(**data)

    def test_governs_change_rejects_even_with_consistently_passed_report(self):
        data = fixture()
        data['proposal']['outputs'][0]['text'] = data['proposal']['outputs'][0]['text'].replace(
            'governs: Atom\n  depends_on: ["Main Content"]', 'governs: "Main Content"\n  depends_on: [Atom]')
        rebind(data)
        with self.assertRaisesRegex(ValueError, 'GOVERNS'):
            admit_subject_recoding(**data)

    def test_actual_type_change_rejects(self):
        data = fixture()
        data['context']['sources'][0]['text'] = data['context']['sources'][0]['text'].replace(
            'type: Requirement', 'type: Boundary')
        rebind(data)
        with self.assertRaisesRegex(ValueError, 'Type|path'):
            admit_subject_recoding(**data)

    def test_authority_drift_is_rejected_after_consistent_rebinding(self):
        data = fixture()
        data['final_context']['sources'][1]['text'] += '\nChanged authority.\n'
        rebind(data)
        with self.assertRaisesRegex(ValueError, 'authority'):
            admit_subject_recoding(**data)

    def test_any_original_gap_and_raw_disagreement_block(self):
        data = fixture()
        data['evaluation']['checks'] = copy.deepcopy(data['evaluation']['checks'])
        data['evaluation']['checks'][1]['findings'][0]['reason'] = 'Unretained reason.'
        with self.assertRaisesRegex(ValueError, 'raw parts'):
            admit_subject_recoding(**data)
        data = fixture()
        part = data['evaluation']['parts'][0]
        part['checks'][0]['status'] = 'blocked'
        part.update(result='blocked', coverage_gaps=[dict(check_id='cce', kind='reviewer_incomplete', reason='Unfinished.')])
        data['evaluation'] = merge_evaluations(data['evaluation']['parts'], context=ReviewContext(data['context']))
        with self.assertRaisesRegex(ValueError, 'coverage'):
            admit_subject_recoding(**data)

    def test_final_evaluation_must_pass_and_match_raw_parts(self):
        for mutation in ('failed', 'raw', 'binding'):
            data = fixture()
            if mutation == 'failed':
                part = data['final_evaluation']['parts'][0]
                part['checks'][0].update(status='failed', findings=[dict(kind='violation', location='Claim',
                    excerpt='must', reason='Remaining defect.', proposed_fix='Correct it.', confidence=1.0)])
                part['result'] = 'failed'
                data['final_evaluation'] = merge_evaluations(data['final_evaluation']['parts'], context=ReviewContext(data['final_context']))
            elif mutation == 'raw':
                data['final_evaluation']['parts'].pop()
            else:
                data['final_evaluation']['source']['sha256'] = '0' * 64
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                admit_subject_recoding(**data)

    def test_resolution_permission_and_external_full_delta_evidence_are_mandatory(self):
        for mutation in ('resolution', 'permission', 'carrier_only', 'version_assessment', 'independent', 'final_review', 'freshness', 'retry'):
            data = fixture()
            preflight = data['preflight']
            if mutation == 'resolution':
                data['proposal']['resolutions'].pop()
            elif mutation == 'permission':
                data['permission']['paths'].pop()
            elif mutation == 'carrier_only':
                preflight['identity_assessment']['classification'] = 'refinement'
            elif mutation == 'version_assessment':
                preflight['identity_assessment']['outputs'] = []
            elif mutation == 'independent':
                preflight['identity_assessment']['independent'] = False
            elif mutation == 'final_review':
                del preflight['final_review']
            elif mutation == 'freshness':
                del preflight['freshness']
            else:
                preflight['attempt'] = 1
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                admit_subject_recoding(**data)


if __name__ == '__main__':
    unittest.main()
