"""Original-to-final admission regressions, not semantic repair assessments."""
import copy
import unittest

from test_repair_gate import (
    RECODING_SOURCE_TEXT, RULE_TEXT, admit_proposal, caller_preflight, contract,
    current_part, gap, refreshed, source,
)


def composition_inputs(*, role='Requirement', old_type=None, source_path=None):
    original = RECODING_SOURCE_TEXT.replace(
        'content_role: Requirement\ntype: Requirement\n',
        f'content_role: {role}\ntype: {old_type or role}\n')
    original += 'Main Content carries this rule.\n'
    source_path = source_path or f'core/MOCK-R-001-CORE-{role.upper()}--atom-rule.md'
    output_path = source_path.replace(f'-{role.upper()}--', '--', 1)
    original_source = source(source_path, 'MOCK-R-001', original)
    dependency_definition = source('main-content.md', 'MOCK-R-003',
        '---\nstatus: active\ncontent_role: Requirement\nsubjects:\n  governs: Main Content\n---\n'
        '# Definition\n\nMain Content means the body carrying an Atom Claim.\n'
        'Substantive mentions require direct dependencies.')
    review_context = contract.ReviewContext({'confidence_threshold': 0.99,
        'review_constraints': {'report_contract': 5}, 'sources': [
            original_source, source('rule.md', 'MOCK-R-002', RULE_TEXT), dependency_definition]})
    parts = [current_part(group, original_source['binding'], review_context)
             for group in contract.GROUPS]
    findings = {
        'properties': dict(kind='violation', location='type', excerpt=f'type: {old_type or role}',
            reason='Ordinary role must omit its role-echo Type.',
            proposed_fix='Remove the role-echo Type and filename token.', confidence=1.0),
        'subjects': dict(kind='omission', obligation_id='main-content-dependency',
            entity='Main Content', location='Details', excerpt='Main Content',
            reason='The substantive Main Content mention lacks its direct dependency.',
            proposed_fix='Add the missing dependency once.', confidence=1.0),
    }
    for part in parts:
        part['authority_sources'].append(dependency_definition['binding'])
        for check in part['checks']:
            if check['id'] == 'subjects':
                check['obligation_resolutions'] = [dict(id='main-content-dependency',
                    state='missing', local_required=True, reason='The dependency is absent locally.',
                    support=[dict(authority='MOCK-R-003@1',
                        excerpt='Substantive mentions require direct dependencies.')])]
                check['subject_inventory']['mentions'].append(dict(
                    location='Details', excerpt='Main Content', entity='Main Content',
                    resolution='resolved', resolution_basis='meaning',
                    rationale='Literal substantive use of the bound Entity definition.',
                    definitions=[dict(authority='MOCK-R-003@1',
                        excerpt='Main Content means the body carrying an Atom Claim.')]))
            if check['id'] in findings:
                check.update(status='failed', findings=[findings[check['id']]])
                part['result'] = 'failed'
    evaluation = contract.merge_evaluations(parts, context=review_context)
    final = refreshed(original.replace(f'type: {old_type or role}\n', '')).replace(
        '  governs: Atom\n', '  governs: Atom\n  depends_on: ["Main Content"]\n')
    proposal = dict(source=evaluation['source'], context_sha256=review_context.sha256,
        disposition='revision', confidence=1.0, before_summary='Atom rule', after_summary='Atom rule',
        outputs=[dict(path=output_path, atom_id='MOCK-R-001', version=1, text=final)],
        resolutions=[dict(check_id=check_id, finding_index=0, reason=f'Resolve {check_id} in final text.')
                     for check_id in findings],
        preservation=['Preserves Summary, Claim, Scope and all substantive Details.'])
    permission = dict(paths=list(dict.fromkeys([source_path, output_path])), dispositions=['revision'],
                      provenance='Synthetic exact caller permission.')
    return review_context, evaluation, proposal, permission


class ComposedRevisionTests(unittest.TestCase):
    def gate(self, data, *, preflight=None):
        review_context, evaluation, proposal, permission = data
        return admit_proposal(evaluation, proposal, context=review_context, permission=permission,
                              preflight=caller_preflight(proposal) if preflight is None else preflight)

    def test_all_findings_composition_with_exact_elision_is_preview_only(self):
        for role in ('Requirement', 'Method', 'Delivery'):
            for classification in ('refinement', 'semantic_revision'):
                data = composition_inputs(role=role)
                proposal = data[2]
                if classification == 'semantic_revision':
                    proposal['outputs'][0]['version'] = 2
                    proposal['outputs'][0]['text'] = proposal['outputs'][0]['text'].replace('version: 1', 'version: 2')
                preflight = caller_preflight(proposal)
                preflight['identity_assessment']['classification'] = classification
                before = copy.deepcopy(data[1:])
                with self.subTest(role=role, classification=classification):
                    result = self.gate(data, preflight=preflight)
                    self.assertEqual(result['result'], 'candidate')
                    self.assertFalse(result['source_mutation_permitted'])
                    self.assertEqual(result['outputs'][0]['path'], 'core/MOCK-R-001-CORE--atom-rule.md')
                    self.assertIn('Independent full evaluation', result['next'])
                    self.assertIn('history and affected-reference checks', result['next'])
                    self.assertEqual(before, data[1:])

    def test_composition_can_keep_original_path(self):
        data = composition_inputs()
        data[2]['outputs'][0]['path'] = data[2]['source']['path']
        self.assertEqual(self.gate(data)['result'], 'candidate')

    def test_composition_cannot_be_assessed_as_carrier_only(self):
        data = composition_inputs()
        preflight = caller_preflight(data[2])
        preflight['identity_assessment']['classification'] = 'carrier_only'
        with self.assertRaisesRegex(ValueError, 'identity assessment'):
            self.gate(data, preflight=preflight)

    def test_composition_requires_assessment_of_exact_final_output(self):
        data = composition_inputs()
        preflight = caller_preflight(data[2])
        data[2]['outputs'][0]['text'] += '\nAnother necessary clarification.\n'
        with self.assertRaisesRegex(ValueError, 'identity assessment'):
            self.gate(data, preflight=preflight)

    def test_composition_cannot_be_mislabeled_as_isolated_recoding(self):
        data = composition_inputs()
        data[2]['disposition'] = 'recoding'
        data[3]['dispositions'] = ['recoding']
        with self.assertRaisesRegex(ValueError, 'recoding may only remove'):
            self.gate(data)

    def test_composition_keeps_exact_all_findings_resolution(self):
        for mutation in ('missing', 'duplicate', 'unknown', 'empty_reason', 'deferred'):
            data = composition_inputs()
            resolutions = data[2]['resolutions']
            if mutation in ('missing', 'deferred'):
                omitted = resolutions.pop()
                if mutation == 'deferred':
                    data[2]['deferred_findings'] = [omitted]
            elif mutation == 'duplicate':
                resolutions.append(copy.deepcopy(resolutions[0]))
            elif mutation == 'unknown':
                resolutions[-1]['finding_index'] = 9
            else:
                resolutions[-1]['reason'] = ' '
            with self.subTest(mutation=mutation), self.assertRaisesRegex(ValueError, 'resolution'):
                self.gate(data)

    def test_composition_coverage_gap_still_blocks(self):
        data = composition_inputs()
        review_context, evaluation, _, _ = data
        parts = evaluation['parts']
        parts[0]['checks'][0]['status'] = 'blocked'
        parts[0].update(result='blocked', coverage_gaps=[gap('cce', 'Missing authority')])
        data = (review_context, contract.merge_evaluations(parts, context=review_context), *data[2:])
        result = self.gate(data)
        self.assertEqual(result['result'], 'blocked')
        self.assertFalse(result['source_mutation_permitted'])

    def test_composition_requires_permission_for_both_paths(self):
        for omitted in (0, 1):
            data = composition_inputs()
            del data[3]['paths'][omitted]
            with self.subTest(omitted=omitted), self.assertRaisesRegex(ValueError, 'path'):
                self.gate(data)

    def test_composition_rejects_every_other_filename_change(self):
        for path in ('elsewhere/MOCK-R-001-CORE--atom-rule.md',
                     'core/MOCK-R-002-CORE--atom-rule.md',
                     'core/MOCK-R-001-GENERAL--atom-rule.md',
                     'core/MOCK-R-001-CORE--different-summary.md',
                     'core/MOCK-R-001-CORE-REQUIREMENT--renamed.md'):
            data = composition_inputs()
            data[2]['outputs'][0]['path'] = path
            data[3]['paths'].append(path)
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, 'path'):
                self.gate(data)

    def test_filename_elision_requires_final_token_and_matching_role_echo(self):
        for source_path, role, old_type in (
                ('core/MOCK-R-001-REQUIREMENT-CORE--atom-rule.md', 'Requirement', None),
                ('core/MOCK-R-001-CORE-METHOD--atom-rule.md', 'Requirement', None),
                ('core/MOCK-R-001-CORE-REQUIREMENT--atom-rule.md', 'Requirement', 'Boundary'),
                ('core/MOCK-R-001-CORE-EVALUATION--atom-rule.md', 'Evaluation', None)):
            data = composition_inputs(role=role, old_type=old_type, source_path=source_path)
            data[2]['outputs'][0]['path'] = 'core/MOCK-R-001-CORE--atom-rule.md'
            data[3]['paths'].append(data[2]['outputs'][0]['path'])
            with self.subTest(source_path=source_path, role=role, old_type=old_type), self.assertRaises(ValueError):
                self.gate(data)

    def test_elision_requires_type_absence_and_same_role_in_final(self):
        for replacement in ('type: Requirement\n', 'type: Boundary\n', 'type: null\n',
                            'type: []\n', 'content_role: Method\n'):
            data = composition_inputs()
            output = data[2]['outputs'][0]
            if replacement.startswith('content_role:'):
                output['text'] = output['text'].replace('content_role: Requirement\n', replacement)
            else:
                output['text'] = output['text'].replace('content_role: Requirement\n',
                                                       'content_role: Requirement\n' + replacement)
            with self.subTest(replacement=replacement), self.assertRaises(ValueError):
                self.gate(data)

    def test_same_path_revision_rejects_specialized_type_changes(self):
        for old_type, new_type in (('Boundary', None), ('Boundary', 'Constraint'),
                                   ('Requirement', 'Boundary')):
            data = composition_inputs(old_type=old_type)
            output = data[2]['outputs'][0]
            output['path'] = data[2]['source']['path']
            if new_type is not None:
                output['text'] = output['text'].replace('content_role: Requirement\n',
                                                       f'content_role: Requirement\ntype: {new_type}\n')
            with self.subTest(old_type=old_type, new_type=new_type), self.assertRaisesRegex(ValueError, 'Type'):
                self.gate(data)

    def test_composition_rejects_changed_summary(self):
        data = composition_inputs()
        data[2]['after_summary'] = 'Another rule'
        data[2]['outputs'][0]['text'] = data[2]['outputs'][0]['text'].replace('Atom rule', 'Another rule')
        with self.assertRaisesRegex(ValueError, 'Summary'):
            self.gate(data)

    def test_isolated_recoding_rejects_arbitrary_authorized_rename(self):
        data = composition_inputs()
        proposal = data[2]
        proposal['disposition'] = 'recoding'
        data[3]['dispositions'] = ['recoding']
        proposal['outputs'][0].update(path='new-name.md', text=refreshed(
            data[0].source_text(proposal['source']).replace('type: Requirement\n', '')))
        data[3]['paths'].append('new-name.md')
        with self.assertRaisesRegex(ValueError, 'path'):
            self.gate(data)

    def test_role_tokens_in_directory_and_summary_are_not_removed(self):
        data = composition_inputs(source_path=
            'core-REQUIREMENT--rules/MOCK-R-001-CORE-REQUIREMENT--a-REQUIREMENT--rule.md')
        proposal = data[2]
        output = proposal['outputs'][0]
        # Override the fixture's simple default path construction: only the
        # basename prefix's final token is the carrier Type coordinate.
        output['path'] = 'core-REQUIREMENT--rules/MOCK-R-001-CORE--a-REQUIREMENT--rule.md'
        data[3]['paths'].append(output['path'])
        self.assertEqual(self.gate(data)['result'], 'candidate')
        for bad in ('core--rules/MOCK-R-001-CORE--a-REQUIREMENT--rule.md',
                    'core-REQUIREMENT--rules/MOCK-R-001-CORE--a--rule.md'):
            output['path'] = bad
            data[3]['paths'].append(bad)
            with self.subTest(path=bad), self.assertRaisesRegex(ValueError, 'path'):
                self.gate(data)


if __name__ == '__main__':
    unittest.main()
