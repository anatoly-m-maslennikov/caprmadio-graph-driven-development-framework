"""Focused regressions for the one layout-plus-Subjects admission."""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / 'tests')]

from evaluation_contract import ReviewContext, merge_evaluations
from layout_repair_gate import authority_digest
from layout_subject_repair_gate import admit_layout_subject_recoding
from test_layout_repair_gate import fixture as layout_fixture, rebind
from test_repair_gate import source


def _subject_finding():
    return dict(kind='omission', obligation_id='direct-dependency', entity='Atom Context',
                location='body:preamble', excerpt='Atom context',
                reason='A substantive Atom Context mention lacks its direct dependency.',
                proposed_fix='Add the direct dependency once.', confidence=1.0)


def combined_fixture(*, role='Requirement'):
    """Adapt the existing layout fixture into the one admitted composite delta."""
    data = layout_fixture(role=role)
    # First reuse the established layout fixture to bind the extended legacy
    # Claim and final Markdown.  DEPENDS_ON and its authority are introduced
    # only after that ordinary fixture rebind, because its helper intentionally
    # keeps one-rule authority lists.
    original_record = data['context']['sources'][0]
    original_record['text'] = original_record['text'].replace(
        'Atom must comply.\n', 'Atom must comply. Atom Context.\n')
    output = data['proposal']['outputs'][0]
    output['text'] = output['text'].replace('Atom must comply.\n',
                                            'Atom must comply. Atom Context.\n')
    from context_builder import body_sections, markdown
    original_body = markdown(original_record['text'])
    data['section_mapping']['source_body_sha256'] = hashlib.sha256(original_body.encode()).hexdigest()
    data['section_mapping']['sections'][2]['source_span'][1] = len(original_body)
    rebind(data)

    definition = source('atom-context.md', 'MOCK-R-003',
        '---\nstatus: active\ncontent_role: Requirement\nsubjects:\n  governs: Atom Context\n---\n'
        '# Definition\n\nAtom Context means the governed context in which an Atom is reviewed. '
        'Substantive mentions require direct dependencies.\n')
    for packet_name in ('context', 'final_context'):
        packet = data[packet_name]
        packet['sources'].append(copy.deepcopy(definition))
        packet['authority_bindings'].append(packet['sources'][-1]['binding'])
    output['text'] = output['text'].replace('  governs: Atom\n',
        '  governs: Atom\n  depends_on: ["Atom Context"]\n')
    final_record = data['final_context']['sources'][0]
    final_record['text'] = output['text']
    final_record['binding'].update(path=output['path'], atom_id=output['atom_id'], version=output['version'],
                                   sha256=hashlib.sha256(output['text'].encode()).hexdigest())
    original_location = list(body_sections(original_record['text']))[-1]
    final_location = next(address for address in body_sections(output['text'])
                          if address.endswith('## Claim'))
    for report_name, location in (('evaluation', original_location), ('final_evaluation', final_location)):
        for part in data[report_name]['parts']:
            for check in part['checks']:
                if check['id'] == 'subjects':
                    check['subject_inventory']['mentions'].append(dict(
                        location=location, excerpt='Atom must comply. Atom Context.', entity='Atom Context',
                        resolution='resolved', resolution_basis='identity',
                        rationale='Literal occurrence is anchored by the bound Entity definition.',
                        definitions=[dict(authority='MOCK-R-003@1',
                            excerpt='Atom Context means the governed context in which an Atom is reviewed.')]))
    for part in data['evaluation']['parts']:
        for check in part['checks']:
            if check['id'] == 'subjects':
                check.update(status='failed', findings=[_subject_finding()])
                check['obligation_resolutions'] = [dict(
                    id='direct-dependency', state='missing', local_required=True,
                    reason='The direct dependency is absent locally.',
                    support=[dict(authority='MOCK-R-003@1',
                        excerpt='Substantive mentions require direct dependencies.')])]
                part['result'] = 'failed'
    for packet_name, report_name in (('context', 'evaluation'), ('final_context', 'final_evaluation')):
        packet = data[packet_name]
        review_context = ReviewContext(packet)
        for part in data[report_name]['parts']:
            part.update(source=packet['sources'][0]['binding'], context_sha256=review_context.sha256,
                        authority_sources=[record['binding'] for record in packet['sources'][1:]])
        data[report_name] = merge_evaluations(data[report_name]['parts'], context=review_context)
    original_context, final_context = ReviewContext(data['context']), ReviewContext(data['final_context'])
    expected = dict(source=data['evaluation']['source'], context_sha256=original_context.sha256,
                    final_context_sha256=final_context.sha256, outputs=[data['final_evaluation']['source']])
    data['proposal'].update(source=expected['source'], context_sha256=original_context.sha256)
    data['preflight'].update(expected)
    data['preflight']['identity_assessment'].update(expected)
    data['preflight']['final_review'].update(source=expected['outputs'][0], context_sha256=final_context.sha256)
    from layout_repair_gate import _digest
    data['preflight']['final_review']['evaluation_sha256'] = _digest(data['final_evaluation'])
    data['preflight']['freshness'].update(source=expected['source'], authority_sha256=authority_digest(data['context']))
    data['proposal']['disposition'] = 'layout_subject_recoding'
    data['permission']['dispositions'] = ['layout_subject_recoding']
    data['proposal']['resolutions'] = [
        dict(check_id=row['id'], finding_index=index,
             reason='Resolved by the exact final layout and dependency correction.')
        for row in data['evaluation']['checks']
        for index, _ in enumerate(row['findings'])
    ]
    return data


def rebind_final(data):
    """Rebind the exact final source/review after an output-byte test mutation."""
    output = data['proposal']['outputs'][0]
    data['final_context']['sources'][0]['text'] = output['text']
    data['final_context']['sources'][0]['binding']['path'] = output['path']
    data['final_context']['sources'][0]['binding']['atom_id'] = output['atom_id']
    data['final_context']['sources'][0]['binding']['version'] = output['version']
    data['final_context']['sources'][0]['binding']['sha256'] = hashlib.sha256(output['text'].encode()).hexdigest()
    final_context = ReviewContext(data['final_context'])
    for part in data['final_evaluation']['parts']:
        part['source'] = data['final_context']['sources'][0]['binding']
        part['context_sha256'] = final_context.sha256
        part['authority_sources'] = [record['binding'] for record in data['final_context']['sources'][1:]]
    data['final_evaluation'] = merge_evaluations(data['final_evaluation']['parts'], context=final_context)
    original_context = ReviewContext(data['context'])
    binding = data['final_evaluation']['source']
    expected = dict(source=data['evaluation']['source'], context_sha256=original_context.sha256,
                    final_context_sha256=final_context.sha256, outputs=[binding])
    data['proposal'].update(source=expected['source'], context_sha256=original_context.sha256)
    data['preflight'].update(expected)
    data['preflight']['identity_assessment'].update(expected)
    data['preflight']['final_review'].update(source=binding, context_sha256=final_context.sha256)
    from layout_repair_gate import _digest
    data['preflight']['final_review']['evaluation_sha256'] = _digest(data['final_evaluation'])
    data['preflight']['freshness'].update(source=expected['source'],
                                          authority_sha256=authority_digest(data['context']))


class LayoutSubjectRepairGateTests(unittest.TestCase):
    def test_exact_composed_admission_is_one_no_write_candidate(self):
        for role in ('Requirement', 'Method', 'Delivery'):
            data = combined_fixture(role=role)
            before = copy.deepcopy(data)
            with self.subTest(role=role):
                result = admit_layout_subject_recoding(**data)
                self.assertEqual(result['result'], 'candidate')
                self.assertFalse(result['source_mutation_permitted'])
                self.assertEqual(len(result['outputs']), 1)
                self.assertEqual(result['resolved_layout_gaps'][0]['original_gap']['kind'], 'layout_dependency')
                self.assertEqual(before, data)

    def test_requires_the_original_confirmed_subjects_finding_and_exact_disposition(self):
        data = combined_fixture()
        for part in data['evaluation']['parts']:
            for check in part['checks']:
                if check['id'] == 'subjects':
                    check.update(status='passed', findings=[], obligation_resolutions=[])
                    check['subject_inventory']['mentions'] = [
                        mention for mention in check['subject_inventory']['mentions']
                        if mention.get('entity') != 'Atom Context']
        for part in data['evaluation']['parts']:
            statuses = [check['status'] for check in part['checks']]
            part['result'] = ('blocked' if 'blocked' in statuses
                              else 'failed' if 'failed' in statuses else 'passed')
        data['evaluation'] = merge_evaluations(data['evaluation']['parts'], context=ReviewContext(data['context']))
        with self.assertRaisesRegex(ValueError, 'Subjects finding'):
            admit_layout_subject_recoding(**data)
        for disposition in ('revision', 'recoding', 'layout_recoding', 'subject_recoding', None):
            data = combined_fixture()
            data['proposal']['disposition'] = disposition
            data['permission']['dispositions'] = [disposition] if disposition else []
            with self.subTest(disposition=disposition), self.assertRaises(ValueError):
                admit_layout_subject_recoding(**data)

    def test_rejects_any_delta_beyond_layout_dependency_and_optional_role_echo(self):
        # These deltas are fully rebound to the final candidate/context before
        # admission.  Their rejection therefore reaches the layout/identity
        # proof rather than merely observing a stale final report hash.
        mutations = {
            'governs': ('governs: Atom', 'governs: Other'),
            'body_claim': ('Atom Context.', 'Atom Context. Extra Claim bytes.'),
            'summary': ('# Summary\nAtom rule', '# Summary\nOther rule'),
            'id': ('atom_id: MOCK-R-001', 'atom_id: MOCK-R-999'),
            'version': ('version: 1', 'version: 2'),
            'relation': ('content_role: Requirement', 'relations: ["Other"]\ncontent_role: Requirement'),
            'scope': ('## Scope\nAtoms.', '## Scope\nOnly reviewed Atoms.'),
            'metadata': ('content_role: Requirement', 'content_role: "Requirement"'),
        }
        for name, (old, new) in mutations.items():
            data = combined_fixture()
            output = data['proposal']['outputs'][0]
            output['text'] = output['text'].replace(old, new)
            if name == 'id':
                output['atom_id'] = 'MOCK-R-999'
            elif name == 'version':
                output['version'] = 2
            if name != 'governs':
                rebind_final(data)
            with self.subTest(name=name), self.assertRaises(ValueError):
                admit_layout_subject_recoding(**data)
        data = combined_fixture()
        output = data['proposal']['outputs'][0]
        output['path'] = 'core/arbitrary.md'
        data['permission']['paths'].append(output['path'])
        with self.assertRaises(ValueError):
            admit_layout_subject_recoding(**data)

    def test_rejects_missing_dependency_change_nonlayout_original_gaps_and_bad_final(self):
        data = combined_fixture()
        data['proposal']['outputs'][0]['text'] = data['proposal']['outputs'][0]['text'].replace(
            '  depends_on: ["Atom Context"]\n', '')
        with self.assertRaises(ValueError):
            admit_layout_subject_recoding(**data)
        data = combined_fixture()
        data['evaluation']['parts'][0]['checks'][0]['status'] = 'blocked'
        data['evaluation']['parts'][0].update(result='blocked', coverage_gaps=[
            dict(check_id='cce', kind='reviewer_incomplete', reason='Unfinished review.')])
        data['evaluation'] = merge_evaluations(data['evaluation']['parts'], context=ReviewContext(data['context']))
        with self.assertRaisesRegex(ValueError, 'layout_dependency'):
            admit_layout_subject_recoding(**data)
        for mutation in ('failed', 'gap'):
            data = combined_fixture()
            if mutation == 'failed':
                data['final_evaluation']['checks'][0]['status'] = 'failed'
            else:
                data['final_evaluation']['coverage_gaps'] = [
                    dict(check_id='scope', kind='layout_dependency', reason='Missing.')]
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                admit_layout_subject_recoding(**data)

    def test_rejects_stale_context_or_weak_assessments_and_missing_permission(self):
        for mutation in ('resources', 'principles', 'authority', 'identity', 'scope', 'provenance', 'multiple', 'permission'):
            data = combined_fixture()
            if mutation == 'resources':
                resource = data['final_context']['resources']['rules']
                resource['text'] = 'rule = false\n'
                resource['sha256'] = hashlib.sha256(resource['text'].encode()).hexdigest()
            elif mutation == 'principles':
                data['final_context']['principle_admissions'] = []
                data['context']['principle_admissions'] = [
                    dict(binding=data['context']['authority_bindings'][0], applicable_to=[data['proposal']['source']['path']])]
            elif mutation == 'authority':
                data['final_context']['preflight']['rules']['state'] = 'unavailable'
            elif mutation == 'identity':
                data['preflight']['identity_assessment']['confidence'] = .98
            elif mutation == 'scope':
                data['preflight']['identity_assessment']['scope_equivalence']['result'] = 'changed'
            elif mutation == 'provenance':
                data['preflight']['identity_assessment']['provenance'] = ''
            elif mutation == 'multiple':
                data['proposal']['outputs'].append(copy.deepcopy(data['proposal']['outputs'][0]))
                data['proposal']['outputs'][1]['path'] = 'core/second.md'
                data['permission']['paths'].append('core/second.md')
            else:
                data['permission']['paths'].pop()
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                admit_layout_subject_recoding(**data)

    def test_rebound_authority_and_resource_drift_still_reject(self):
        data = combined_fixture()
        rule = data['final_context']['sources'][1]
        rule['text'] += '\nUnchanged applicability cannot be assumed.\n'
        rule['binding']['sha256'] = hashlib.sha256(rule['text'].encode()).hexdigest()
        rebind_final(data)
        with self.assertRaisesRegex(ValueError, 'authority'):
            admit_layout_subject_recoding(**data)
        data = combined_fixture()
        resource = data['final_context']['resources']['rules']
        resource['text'] = 'rule = false\n'
        resource['sha256'] = hashlib.sha256(resource['text'].encode()).hexdigest()
        rebind_final(data)
        with self.assertRaisesRegex(ValueError, 'authority resources'):
            admit_layout_subject_recoding(**data)


if __name__ == '__main__':
    unittest.main()
