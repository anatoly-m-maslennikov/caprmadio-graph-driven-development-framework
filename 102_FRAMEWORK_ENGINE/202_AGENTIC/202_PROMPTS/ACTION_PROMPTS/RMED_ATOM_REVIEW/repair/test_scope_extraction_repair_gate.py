"""Focused staged regressions for exact Scope extraction plus DEPENDS_ON repair.

These tests exercise an isolated proposal gate only.  They do not bind or
evaluate a real Atom and never permit a source write.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
REPAIR = HERE
PACKAGE = HERE.parent
sys.path[:0] = [str(HERE), str(PACKAGE), str(HERE / 'tests')]

from context_builder import body_sections, markdown
from evaluation_contract import GROUPS, ReviewContext, merge_evaluations
from layout_repair_gate import authority_digest
from repair_gate import _summary
from test_repair_gate import RULE_TEXT, legacy_part, refreshed, source
from scope_extraction_preview import admit_scope_extraction_preview
from scope_extraction_repair_gate import admit_scope_extraction_subject_recoding


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def source_body():
    return ('# Atom rule\n\n**every** Atom other than a Project Goal Atom **must** '
            'comply with Atom Context.\n')


def final_body():
    return ('# Summary\nAtom rule\n\n## Scope\nAtom other than a Project Goal Atom.\n\n'
            '## Claim\n\n**every** Atom **must** comply with Atom Context.\n\n## Details\n')


def map_for(original, candidate):
    body, proposed = markdown(original), markdown(candidate)
    selector = 'Atom other than a Project Goal Atom'
    claim = '**every** Atom **must** comply with Atom Context.\n'
    title_end = body.index('\n') + 1
    selector_start = body.index(selector)
    summary_end = proposed.index('\n\n## Scope') + 1
    scope_start = proposed.index(selector + '.', proposed.index('## Scope'))
    reduced_claim = '\n' + claim
    claim_start = proposed.index(reduced_claim, proposed.index('## Claim'))
    return {
        'source_body_sha256': hashlib.sha256(body.encode()).hexdigest(),
        'proposed_body_sha256': hashlib.sha256(proposed.encode()).hexdigest(),
        'sections': [
            {'heading': '# Summary', 'source_span': [0, title_end],
             'proposed_span': [0, summary_end], 'state': 'legacy_h1_to_summary_value',
             'provenance': 'Exact original H1 and generated Summary.'},
            {'heading': '## Scope', 'source_span': [selector_start, selector_start + len(selector)],
             'proposed_span': [scope_start, scope_start + len(selector) + 1],
             'state': 'extracted_applicability', 'provenance': 'Exact source selector.',
             'source_text': selector, 'proposed_text': selector + '.'},
            {'heading': '## Claim', 'source_span': [title_end, len(body)],
             'proposed_span': [claim_start, claim_start + len(reduced_claim)],
             'state': 'selector_reduced_to_bearer',
             'provenance': 'The exact original assertion with only its selector reduced.'},
            {'heading': '## Details', 'source_span': None, 'proposed_span': None,
             'state': 'unassessed_absent', 'provenance': 'No Details prose exists.'},
        ],
    }


def rebind_mapping(data):
    """Bind the supplied map to current source/output bytes, without endorsing them."""
    original = data['context']['sources'][0]['text']
    proposed = markdown(data['proposal']['outputs'][0]['text'])
    body = markdown(original)
    mapping = data['section_mapping']
    mapping['source_body_sha256'] = hashlib.sha256(body.encode()).hexdigest()
    mapping['proposed_body_sha256'] = hashlib.sha256(proposed.encode()).hexdigest()
    mapping['sections'][0]['proposed_span'] = [0, proposed.index('\n\n## Scope') + 1]
    scope_start = proposed.index('## Scope\n') + len('## Scope\n')
    scope_end = proposed.index('\n\n## Claim', scope_start)
    mapping['sections'][1]['proposed_span'] = [scope_start, scope_end]
    mapping['sections'][1]['proposed_text'] = proposed[scope_start:scope_end]
    claim_start = proposed.index('## Claim\n') + len('## Claim\n')
    claim_end = proposed.index('\n## Details\n', claim_start)
    mapping['sections'][2]['proposed_span'] = [claim_start, claim_end]


def rebind_final(data):
    """Rebind a synthetic full final review after output-byte mutation."""
    output = data['proposal']['outputs'][0]
    record = data['final_context']['sources'][0]
    record['text'] = output['text']
    record['binding'].update(path=output['path'], atom_id=output['atom_id'], version=output['version'],
                             sha256=hashlib.sha256(output['text'].encode()).hexdigest())
    ctx = ReviewContext(data['final_context'])
    for part in data['final_evaluation']['parts']:
        part.update(source=record['binding'], context_sha256=ctx.sha256,
                    authority_sources=[row['binding'] for row in data['final_context']['sources'][1:]])
    data['final_evaluation'] = merge_evaluations(data['final_evaluation']['parts'], context=ctx)
    original_ctx = ReviewContext(data['context'])
    binding = data['final_evaluation']['source']
    expected = {'source': data['evaluation']['source'], 'context_sha256': original_ctx.sha256,
                'final_context_sha256': ctx.sha256, 'outputs': [binding]}
    data['proposal'].update(source=expected['source'], context_sha256=original_ctx.sha256)
    data['preflight'].update(expected)
    data['preflight']['identity_assessment'].update(expected)
    data['preflight']['final_review'].update(source=binding, context_sha256=ctx.sha256,
                                              evaluation_sha256=digest(data['final_evaluation']))
    data['preflight']['final_freshness'].update(source=binding,
                                                authority_sha256=authority_digest(data['final_context']))
    rebind_mapping(data)


def rebind_original(data):
    """Rebind a synthetic original review after source-byte mutation."""
    record = data['context']['sources'][0]
    record['binding']['sha256'] = hashlib.sha256(record['text'].encode()).hexdigest()
    ctx = ReviewContext(data['context'])
    for part in data['evaluation']['parts']:
        part.update(source=record['binding'], context_sha256=ctx.sha256,
                    authority_sources=[row['binding'] for row in data['context']['sources'][1:]])
    data['evaluation'] = merge_evaluations(data['evaluation']['parts'], context=ctx)
    final_ctx = ReviewContext(data['final_context'])
    expected = {'source': data['evaluation']['source'], 'context_sha256': ctx.sha256,
                'final_context_sha256': final_ctx.sha256, 'outputs': [data['final_evaluation']['source']]}
    data['proposal'].update(source=expected['source'], context_sha256=ctx.sha256)
    data['preflight'].update(expected)
    data['preflight']['identity_assessment'].update(expected)
    data['preflight']['freshness'].update(source=expected['source'],
                                          authority_sha256=authority_digest(data['context']))
    rebind_mapping(data)


def add_original_finding(data, check_id, finding):
    """Add a contract-valid synthetic original finding and rebind its report."""
    for part in data['evaluation']['parts']:
        for row in part['checks']:
            if row['id'] == check_id:
                row.update(status='failed', findings=row['findings'] + [finding])
                part['result'] = 'failed'
                data['proposal']['resolutions'].append({
                    'check_id': check_id, 'finding_index': len(row['findings']) - 1,
                    'reason': 'Synthetic resolution binding for staged negative coverage.'})
    rebind_original(data)


def fixture():
    path = 'core/MOCK-R-001-CORE-REQUIREMENT--atom-rule.md'
    header = ('---\natom_id: MOCK-R-001\nversion: 1\n'
              'updated_at: "2026-09-26T00:00:00Z"\nsubjects:\n  governs: Atom\n'
              'content_role: Requirement\ntype: Requirement\n---\n')
    original = source(path, 'MOCK-R-001', header + source_body())
    final_header = refreshed(header.replace('type: Requirement\n', ''))
    final_text = final_header + final_body()
    final_text = final_text.replace('  governs: Atom\n',
                                    '  governs: Atom\n  depends_on: ["Atom Context"]\n')
    final = source(path.replace('-REQUIREMENT--', '--'), 'MOCK-R-001', final_text)
    rule = source('rule.md', 'MOCK-R-002', RULE_TEXT + '\nRequired Summary, Scope, Claim and Details headings.')
    definition = source('atom-context.md', 'MOCK-R-003',
        '---\nstatus: active\ncontent_role: Requirement\nsubjects:\n  governs: Atom Context\n---\n'
        '# Definition\n\nAtom Context means the governed context in which an Atom is reviewed. '
        'Substantive mentions require direct dependencies.\n')
    resources = {'rules': {'path': 'rules.toml', 'text': 'rule = true\n',
                           'sha256': hashlib.sha256(b'rule = true\n').hexdigest()}}
    packet = {'confidence_threshold': .99, 'review_constraints': {'report_contract': 5},
              'sources': [original, rule, definition],
              'authority_bindings': [rule['binding'], definition['binding']],
              'resources': resources,
              'preflight': {'rules': {'state': 'available', 'reason': 'Bound rules.'},
                            'principles': {'state': 'available', 'reason': 'Bound Principles.'}},
              'principle_admissions': [
                  {'binding': rule['binding'], 'applicable_to': [path],
                   'reason': 'Rule applies to the mock carrier.', 'provenance': 'Synthetic fixture.'},
                  {'binding': definition['binding'], 'applicable_to': [path],
                   'reason': 'Definition applies to the mock carrier.', 'provenance': 'Synthetic fixture.'},
              ]}
    final_packet = copy.deepcopy(packet)
    final_packet['sources'][0] = final
    final_packet['principle_admissions'] = [
        {'binding': rule['binding'], 'applicable_to': [final['binding']['path']],
         'reason': 'Rule applies to the mock candidate.', 'provenance': 'Synthetic fixture.'},
        {'binding': definition['binding'], 'applicable_to': [final['binding']['path']],
         'reason': 'Definition applies to the mock candidate.', 'provenance': 'Synthetic fixture.'},
    ]
    context, final_context = ReviewContext(packet), ReviewContext(final_packet)

    def report(record, ctx, legacy):
        parts = [legacy_part(group) for group in GROUPS]
        sections = body_sections(record['text'])
        claim_location = sections[-1] if legacy else next(x for x in sections if x.endswith('## Claim'))
        for part in parts:
            part.update(contract_version=5, source=record['binding'], context_sha256=ctx.sha256,
                        authority_sources=[rule['binding'], definition['binding']])
            for row in part['checks']:
                row['positive_observations'] = [
                    {'location': claim_location, 'excerpt': 'Atom Context.', 'authority': 'MOCK-R-002@1',
                     'rule_excerpt': 'Atom means a governed statement.'}]
                if row['id'] == 'subjects':
                    row['subject_inventory']['sections_reviewed'] = sections
                    row['subject_inventory']['mentions'][0].update(
                        location=claim_location, excerpt='Atom Context.')
                    row['subject_inventory']['mentions'].append({
                        'location': claim_location, 'excerpt': 'Atom Context.', 'entity': 'Atom Context',
                        'resolution': 'resolved', 'resolution_basis': 'identity',
                        'rationale': 'Literal occurrence is bound to the definition.',
                        'definitions': [{'authority': 'MOCK-R-003@1',
                                         'excerpt': 'Atom Context means the governed context in which an Atom is reviewed.'}]})
                if legacy and row['id'] in ('scope', 'claim', 'details', 'governed_entity', 'alignment', 'summary'):
                    row.update(status='blocked', positive_observations=[])
                    part['coverage_gaps'].append({'check_id': row['id'], 'kind': 'layout_dependency',
                                                  'reason': 'Registered section absent.'})
                    part['result'] = 'blocked'
                if legacy and row['id'] == 'subjects':
                    row.update(status='failed', findings=[{
                        'kind': 'omission', 'obligation_id': 'direct-dependency', 'entity': 'Atom Context',
                        'location': claim_location, 'excerpt': 'Atom Context.',
                        'reason': 'A substantive Atom Context mention lacks its direct dependency.',
                        'proposed_fix': 'Add the direct dependency once.', 'confidence': 1.0}],
                        obligation_resolutions=[{
                            'id': 'direct-dependency', 'state': 'missing', 'local_required': True,
                            'reason': 'The direct dependency is absent locally.',
                            'support': [{'authority': 'MOCK-R-003@1',
                                         'excerpt': 'Substantive mentions require direct dependencies.'}]}])
                    part['result'] = 'failed'
                if legacy and row['id'] == 'properties':
                    row.update(status='failed', findings=[{
                        'kind': 'violation', 'location': 'frontmatter', 'excerpt': 'type: Requirement',
                        'reason': 'Role echo is not a specialized Type.', 'proposed_fix': 'Omit role echo.',
                        'confidence': 1.0}], obligation_resolutions=[])
                    for heading in ('# Summary', '## Scope', '## Claim', '## Details'):
                        obligation_id = 'CA-D-479:' + heading
                        row['findings'].append({
                            'kind': 'omission', 'obligation_id': obligation_id, 'location': 'body:preamble',
                            'excerpt': f'Absent {heading}', 'reason': 'Registered heading absent locally.',
                            'proposed_fix': f'Add {heading}.', 'confidence': 1.0})
                        row['obligation_resolutions'].append({
                            'id': obligation_id, 'state': 'missing', 'local_required': True,
                            'reason': 'Heading absent locally.',
                            'support': [{'authority': 'MOCK-R-002@1',
                                         'excerpt': 'Required Summary, Scope, Claim and Details headings.'}]})
                    part['result'] = 'failed'
            statuses = [row['status'] for row in part['checks']]
            part['result'] = ('failed' if 'failed' in statuses
                              else 'blocked' if 'blocked' in statuses else 'passed')
        return merge_evaluations(parts, context=ctx)

    evaluation, final_evaluation = report(original, context, True), report(final, final_context, False)
    mapping = map_for(original['text'], final['text'])
    proposal = {'source': original['binding'], 'context_sha256': context.sha256,
                'disposition': 'scope_extraction_subject_recoding', 'confidence': .99,
                'before_summary': _summary(final['text']), 'after_summary': _summary(final['text']),
                'outputs': [{'path': final['binding']['path'], 'atom_id': 'MOCK-R-001', 'version': 1,
                             'text': final['text']}],
                'resolutions': [{'check_id': row['id'], 'finding_index': index,
                                 'reason': 'Resolved by the exact final extraction and dependency correction.'}
                                for row in evaluation['checks'] for index, _ in enumerate(row['findings'])],
                'preservation': ['Exact legacy condition is moved only by the staged extraction proof.']}
    permission = {'paths': [path, final['binding']['path']],
                  'dispositions': ['scope_extraction_subject_recoding'], 'provenance': 'Exact permission.'}
    expected = {'source': original['binding'], 'context_sha256': context.sha256,
                'final_context_sha256': final_context.sha256, 'outputs': [final['binding']]}
    preflight = {**expected, 'provenance': 'Bound current evidence.', 'attempt': 0, 'retry_budget': 0,
                 'authority_aliases': [],
                 'freshness': {'source': original['binding'], 'authority_sha256': authority_digest(packet),
                               'provenance': 'Original source and authority were re-read.'},
                 'final_freshness': {'source': final['binding'],
                                     'authority_sha256': authority_digest(final_packet),
                                     'provenance': 'Final candidate and authority were re-read.'},
                 'final_review': {'source': final['binding'], 'context_sha256': final_context.sha256,
                                  'evaluation_sha256': digest(final_evaluation), 'independent': True,
                                  'provenance': 'Separate final evaluator.'},
                 'identity_assessment': {**expected, 'classification': 'carrier_only',
                    'confidence': .99, 'independent': True, 'provenance': 'Separate full-delta reviewer.',
                    'scope_equivalence': {
                        'result': 'equivalent', 'source_excerpt': 'Atom other than a Project Goal Atom',
                        'final_scope': 'Atom other than a Project Goal Atom.',
                        'independent': True,
                        'reason': 'The exact original selector is the exact final Scope.',
                        'support': [{'authority': 'MOCK-R-002@1',
                                     'excerpt': 'Atom means a governed statement.'}]}}}
    return {'evaluation': evaluation, 'proposal': proposal, 'context': packet,
            'final_evaluation': final_evaluation, 'final_context': final_packet,
            'section_mapping': mapping, 'permission': permission, 'preflight': preflight}


class ScopeExtractionPreviewTests(unittest.TestCase):
    def test_exact_span_bound_preview_is_no_write(self):
        data = fixture()
        original = data['context']['sources'][0]
        final = data['proposal']['outputs'][0]['text']
        virtual = original['text'].removesuffix(markdown(original['text'])) + markdown(final)
        before = copy.deepcopy((original, virtual, data['section_mapping']))
        result = admit_scope_extraction_preview(original['binding'], original['text'], virtual,
                                                section_mapping=data['section_mapping'])
        self.assertEqual(result['result'], 'preview')
        self.assertFalse(result['source_mutation_permitted'])
        self.assertEqual(before, (original, virtual, data['section_mapping']))

    def test_every_source_and_proposed_span_is_exact(self):
        for index, field in ((0, 'source_span'), (0, 'proposed_span'), (1, 'source_span'),
                             (1, 'proposed_span'), (2, 'source_span'), (2, 'proposed_span')):
            data = fixture()
            data['section_mapping']['sections'][index][field][0] += 1
            original = data['context']['sources'][0]
            virtual = original['text'].removesuffix(markdown(original['text'])) + markdown(data['proposal']['outputs'][0]['text'])
            with self.subTest(index=index, field=field):
                self.assertEqual(admit_scope_extraction_preview(original['binding'], original['text'], virtual,
                    section_mapping=data['section_mapping'])['result'], 'rejected')

    def test_compound_or_conditional_source_is_fail_closed(self):
        data = fixture()
        original = data['context']['sources'][0]
        for old, new in (('other than a Project Goal Atom', 'other than a Goal or Demand'),
                         ('other than a Project Goal Atom', 'other than a Goal if accepted')):
            raw = original['text'].replace(old, new)
            binding = dict(original['binding'], sha256=hashlib.sha256(raw.encode()).hexdigest())
            with self.subTest(new=new):
                self.assertEqual(admit_scope_extraction_preview(binding, raw, raw,
                    section_mapping=data['section_mapping'])['result'], 'rejected')

    def test_unicode_selector_is_explicitly_unsupported(self):
        data = fixture()
        original = data['context']['sources'][0]
        raw = original['text'].replace('Project Goal', 'Prøject Goal')
        binding = dict(original['binding'], sha256=hashlib.sha256(raw.encode()).hexdigest())
        result = admit_scope_extraction_preview(binding, raw, raw, section_mapping=data['section_mapping'])
        self.assertEqual(result['result'], 'rejected')
        self.assertIn('unsupported source', result['reason'])


class ScopeExtractionRepairGateTests(unittest.TestCase):
    def test_exact_composition_is_candidate_only(self):
        data = fixture()
        before = copy.deepcopy(data)
        result = admit_scope_extraction_subject_recoding(**data)
        self.assertEqual(result['result'], 'candidate')
        self.assertFalse(result['source_mutation_permitted'])
        self.assertEqual(before, data)

    def test_rejects_condition_scope_claim_or_summary_rewrites(self):
        for old, new in (('other than a Project Goal Atom.', 'other than a Goal.'),
                         ('**every** Atom **must**', '**some** Atom **must**'),
                         ('comply with Atom Context.', 'may comply with Atom Context.'),
                         ('# Summary\nAtom rule', '# Summary\nOther rule')):
            data = fixture()
            output = data['proposal']['outputs'][0]
            output['text'] = output['text'].replace(old, new)
            with self.subTest(old=old), self.assertRaises(ValueError):
                admit_scope_extraction_subject_recoding(**data)

    def test_fully_rebound_scope_and_claim_rewrites_reach_extraction_proof(self):
        for old, new in (
                ('Atom other than a Project Goal Atom.', 'Atom other than a Different Goal Atom.'),
                ('comply with Atom Context.', 'conform with Atom Context.')):
            data = fixture()
            data['proposal']['outputs'][0]['text'] = data['proposal']['outputs'][0]['text'].replace(old, new)
            rebind_final(data)
            with self.subTest(old=old), self.assertRaisesRegex(ValueError, 'exact Scope extraction proof rejected'):
                admit_scope_extraction_subject_recoding(**data)

    def test_fully_rebound_compound_source_reaches_fail_closed_grammar(self):
        data = fixture()
        old = 'Atom other than a Project Goal Atom'
        new = 'Atom other than a Goal or Demand'
        data['context']['sources'][0]['text'] = data['context']['sources'][0]['text'].replace(old, new)
        data['proposal']['outputs'][0]['text'] = data['proposal']['outputs'][0]['text'].replace(old, new)
        rebind_original(data)
        rebind_final(data)
        body = markdown(data['context']['sources'][0]['text'])
        selector_start = body.index(new)
        title_end = body.index('\n') + 1
        data['section_mapping']['sections'][1].update(
            source_span=[selector_start, selector_start + len(new)], source_text=new)
        data['section_mapping']['sections'][2]['source_span'] = [title_end, len(body)]
        data['preflight']['identity_assessment']['scope_equivalence'].update(
            source_excerpt=new, final_scope=new + '.')
        with self.assertRaisesRegex(ValueError, 'compound or conditional selectors'):
            admit_scope_extraction_subject_recoding(**data)

    def test_rejects_gap_bypass_reports_freshness_and_nonindependence(self):
        for mutation in ('non_layout_gap', 'final_gap', 'final_freshness', 'identity', 'scope_independence', 'final_review'):
            data = fixture()
            if mutation == 'non_layout_gap':
                data['evaluation']['parts'][0]['coverage_gaps'].append(
                    {'check_id': 'scope', 'kind': 'reviewer_incomplete', 'reason': 'Unresolved.'})
            elif mutation == 'final_gap':
                data['final_evaluation']['coverage_gaps'] = [
                    {'check_id': 'scope', 'kind': 'layout_dependency', 'reason': 'Missing.'}]
            elif mutation == 'final_freshness':
                data['preflight']['final_freshness']['authority_sha256'] = '0' * 64
            elif mutation == 'identity':
                data['preflight']['identity_assessment']['independent'] = False
            elif mutation == 'scope_independence':
                data['preflight']['identity_assessment']['scope_equivalence']['independent'] = False
            else:
                data['preflight']['final_review']['independent'] = False
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                admit_scope_extraction_subject_recoding(**data)

    def test_fully_rebound_cce_finding_cannot_be_withdrawn_by_final_pass(self):
        data = fixture()
        location = next(row for row in data['evaluation']['checks'] if row['id'] == 'subjects')['findings'][0]['location']
        add_original_finding(data, 'cce', {
            'kind': 'violation', 'location': location, 'excerpt': 'comply',
            'reason': 'Synthetic unrelated CCE defect in preserved predicate.',
            'proposed_fix': 'Change the predicate.', 'confidence': 1.0})
        with self.assertRaisesRegex(ValueError, 'unadmitted original finding: cce'):
            admit_scope_extraction_subject_recoding(**data)

    def test_nonrepaired_subject_and_property_findings_reject_after_rebinding(self):
        data = fixture()
        location = next(row for row in data['evaluation']['checks'] if row['id'] == 'subjects')['findings'][0]['location']
        add_original_finding(data, 'subjects', {
            'kind': 'violation', 'entity': 'Atom', 'location': location, 'excerpt': 'Atom',
            'reason': 'Synthetic unsupported Subjects defect.', 'proposed_fix': 'Change GOVERNS.',
            'confidence': 1.0})
        with self.assertRaisesRegex(ValueError, 'unadmitted Subjects finding'):
            admit_scope_extraction_subject_recoding(**data)
        data = fixture()
        add_original_finding(data, 'properties', {
            'kind': 'violation', 'location': 'frontmatter', 'excerpt': 'content_role: Requirement',
            'reason': 'Synthetic unsupported property defect.', 'proposed_fix': 'Change content role.',
            'confidence': 1.0})
        with self.assertRaisesRegex(ValueError, 'unadmitted Properties finding'):
            admit_scope_extraction_subject_recoding(**data)

    def test_real_heading_omissions_and_dep_fix_remain_admitted(self):
        data = fixture()
        result = admit_scope_extraction_subject_recoding(**data)
        self.assertEqual(result['result'], 'candidate')

    def test_r154_and_r920_property_finding_shapes_remain_exactly_admitted(self):
        variants = {
            'R154': {
                '# Summary': 'CA-D-479:# Summary', '## Scope': 'CA-D-479:## Scope',
                '## Claim': 'CA-D-479:## Claim', '## Details': 'CA-D-479:## Details'},
            'R920': {
                '# Summary': 'CA-D-479:Summary', '## Scope': 'CA-D-479:Scope',
                '## Claim': 'CA-D-479:Claim', '## Details': 'CA-D-479:Details'},
        }
        for name, ids in variants.items():
            data = fixture()
            data['context']['sources'][0]['text'] = data['context']['sources'][0]['text'].replace(
                'type: Requirement\n', 'type: "Requirement"\n')
            for part in data['evaluation']['parts']:
                for row in part['checks']:
                    if row['id'] != 'properties':
                        continue
                    row['findings'][0]['excerpt'] = 'type: "Requirement"'
                    for finding in row['findings'][1:]:
                        heading = finding['obligation_id'].removeprefix('CA-D-479:')
                        finding['obligation_id'] = ids[heading]
                    for obligation in row['obligation_resolutions']:
                        heading = obligation['id'].removeprefix('CA-D-479:')
                        obligation['id'] = ids[heading]
            rebind_original(data)
            with self.subTest(report_shape=name):
                self.assertEqual(admit_scope_extraction_subject_recoding(**data)['result'], 'candidate')

    def test_requires_a_real_depends_on_delta_and_exact_scope_evidence(self):
        data = fixture()
        # The synthetic original report retains its explicit Subjects finding,
        # but both fully rebound carriers now contain the same dependency. This
        # reaches the comparator rather than relying on a stale final binding.
        for part in data['evaluation']['parts']:
            for row in part['checks']:
                if row['id'] == 'subjects':
                    row['findings'][0].update(kind='violation', subject_issue='governs',
                                              reason='Synthetic governing mismatch fixture.')
                    row['obligation_resolutions'] = []
        data['context']['sources'][0]['text'] = data['context']['sources'][0]['text'].replace(
            '  governs: Atom\n', '  governs: Atom\n  depends_on: ["Atom Context"]\n')
        rebind_original(data)
        with self.assertRaisesRegex(ValueError, 'actual DEPENDS_ON correction'):
            admit_scope_extraction_subject_recoding(**data)
        data = fixture()
        data['preflight']['identity_assessment']['scope_equivalence']['source_excerpt'] = 'Atom Context'
        with self.assertRaises(ValueError):
            admit_scope_extraction_subject_recoding(**data)

    def test_fully_rebound_governs_change_reaches_dependency_comparator(self):
        data = fixture()
        data['proposal']['outputs'][0]['text'] = data['proposal']['outputs'][0]['text'].replace(
            '  governs: Atom\n', '  governs: Atom Context\n')
        data['proposal']['outputs'][0]['text'] = data['proposal']['outputs'][0]['text'].replace(
            '  depends_on: ["Atom Context"]\n', '  depends_on: ["Atom"]\n')
        rebind_final(data)
        with self.assertRaisesRegex(ValueError, 'preserve GOVERNS'):
            admit_scope_extraction_subject_recoding(**data)


if __name__ == '__main__':
    unittest.main()

