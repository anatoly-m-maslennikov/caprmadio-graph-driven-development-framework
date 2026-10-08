"""Local-profile admission: integrity tests, not simulated LLM judgments."""
from copy import deepcopy
import unittest

from test_split_evaluation import contract, part as legacy_part, source, SOURCE_TEXT, RULE_TEXT
from operator_precheck import word_inventory

REGISTRY = '''1. statement form: **to**, **means**
2. modality: **must**, **must not**, **may**
3. condition: **if**, **then**, **when**, **otherwise**
4. temporal: **before**, **after**, **until**, **unless**
5. quantification: **all**, **every**, **any**, **none**
6. logic: **and**, **or**, **not**, **without**, **where**
7. restriction: **only**
8. predicate: **in**, **not in**, **is empty**, **is not empty**, **contains**, **starts with**, **ends with**
9. comparison: **`=`**, **`!=`**, **`<`**, **`<=`**, **`>`**, **`>=`**
'''


def prechecked_packet():
    packet = packet6()
    registry = source('registry.md', 'MOCK-M-003', REGISTRY)
    packet['sources'].append(registry)
    packet['authority_bindings'].append(registry['binding'])
    packet['review_constraints'].update(operator_precheck=word_inventory(REGISTRY),
                                        operator_registry='MOCK-M-003@1')
    return packet


def packet6():
    candidate = source('mock.md', 'MOCK-R-001', SOURCE_TEXT)
    rule = source('rule.md', 'MOCK-R-002', RULE_TEXT)
    return {
        'confidence_threshold': .99,
        'review_constraints': {'report_contract': 6, 'review_profile': 'atom_local'},
        'sources': [candidate, rule],
        'candidate_bindings': [candidate['binding']],
        'authority_bindings': [rule['binding']],
    }


def context6():
    return contract.ReviewContext(packet6())


def part6(group):
    report = legacy_part(group)
    report.update(contract_version=6, review_profile='atom_local', context_sha256=context6().sha256)
    report['checks'] = [r for r in report['checks'] if r['id'] in contract.LOCAL_GROUPS[group]]
    for row in report['checks']:
        row.pop('subject_inventory', None)
        row['positive_observations'] = [{
            'location': 'body:5:## Claim', 'excerpt': 'Atom must comply.',
            'authority': 'MOCK-R-002@1', 'rule_excerpt': 'Atom means a governed statement.',
        }]
    return report


class LocalReview(unittest.TestCase):
    def test_bound_operator_precheck_rejects_skipped_rendering(self):
        packet = prechecked_packet()
        ctx = contract.ReviewContext(packet)
        report = part6('cce')
        report['context_sha256'] = ctx.sha256
        with self.assertRaisesRegex(ValueError, 'operator precheck coverage'):
            contract.validate_part(report, context=ctx)

    def test_precheck_cannot_narrow_or_enlarge_bound_inventory(self):
        for inventory in (['must'], word_inventory(REGISTRY) + ['together with']):
            packet = prechecked_packet()
            packet['review_constraints']['operator_precheck'] = inventory
            with self.subTest(inventory=inventory), self.assertRaisesRegex(ValueError, 'differs'):
                contract.ReviewContext(packet)

    def test_precheck_requires_admitted_registry(self):
        for change in ('missing', 'unbound', 'candidate'):
            packet = prechecked_packet()
            if change == 'missing':
                packet['review_constraints'].pop('operator_registry')
            elif change == 'unbound':
                packet['authority_bindings'].pop()
            else:
                packet['review_constraints']['operator_registry'] = 'MOCK-R-001@1'
            with self.subTest(change=change), self.assertRaisesRegex(ValueError, 'bound registry'):
                contract.ReviewContext(packet)

    def test_compact_context_needs_no_graph_or_principles_or_registry(self):
        ctx = context6()
        parts = [part6(g) for g in contract.LOCAL_GROUPS]
        merged = contract.merge_evaluations(parts, context=ctx)
        self.assertEqual(merged['review_profile'], 'atom_local')
        self.assertEqual(merged['result'], 'passed')
        self.assertEqual(len(merged['checks']), 6)
        self.assertEqual(merged['parts'], parts)
        summary = contract.summarize_evaluations([merged], context=ctx)
        self.assertEqual(summary['review_profile'], 'atom_local')
        self.assertEqual(set(summary['check_counts']), {'cce','properties','scope','claim','details','summary'})

    def test_foreign_graph_checks_are_rejected_not_auto_passed(self):
        for excluded in ('subjects','governed_entity','alignment','content_role'):
            report = part6('coherence')
            extra = deepcopy(report['checks'][0]); extra['id'] = excluded
            report['checks'].append(extra)
            with self.subTest(excluded=excluded), self.assertRaises(ValueError):
                contract.validate_part(report, context=context6())

    def test_subject_inventory_cannot_be_smuggled_into_properties(self):
        report = part6('properties')
        report['checks'][0]['subject_inventory'] = {'complete':True,'mentions':[]}
        with self.assertRaisesRegex(ValueError, 'outside'):
            contract.validate_part(report, context=context6())

    def test_profile_and_one_candidate_are_required(self):
        for change in ('missing_profile','wrong_profile','two_candidates','self_admitted'):
            packet = packet6()
            if change == 'missing_profile':
                del packet['review_constraints']['review_profile']
            elif change == 'wrong_profile':
                packet['review_constraints']['review_profile'] = 'full'
            elif change == 'two_candidates':
                packet['candidate_bindings'] *= 2
            else:
                packet['authority_bindings'].extend(packet['candidate_bindings'])
            with self.subTest(change=change), self.assertRaises(ValueError):
                contract.ReviewContext(packet)

    def test_legacy_report_or_wrong_profile_cannot_claim_local_pass(self):
        for change in ('legacy', 'wrong_profile', 'missing_part', 'mixed_source'):
            parts = [part6(g) for g in contract.LOCAL_GROUPS]
            if change == 'legacy': parts[0]['contract_version'] = 5
            elif change == 'wrong_profile': parts[0]['review_profile'] = 'full'
            elif change == 'missing_part': parts.pop()
            else: parts[0]['source']['sha256'] = 'a'*64
            with self.subTest(change=change), self.assertRaises(ValueError):
                contract.merge_evaluations(parts, context=context6())

    def test_generic_pass_and_fabricated_quotes_remain_rejected(self):
        for change in ('missing', 'source', 'rule'):
            report = part6('cce')
            row = report['checks'][0]
            if change == 'missing': row.pop('positive_observations')
            elif change == 'source': row['positive_observations'][0]['excerpt'] = 'invented'
            else: row['positive_observations'][0]['rule_excerpt'] = 'invented'
            with self.subTest(change=change), self.assertRaises(ValueError):
                contract.validate_part(report, context=context6())

    def test_local_failure_and_local_gap_are_both_retained(self):
        parts = [part6(g) for g in contract.LOCAL_GROUPS]
        parts[0]['checks'][0].update(status='failed', findings=[{
            'kind':'violation','location':'body:5:## Claim','excerpt':'must',
            'reason':'Synthetic rendering defect','proposed_fix':'Bold must','confidence':.99}])
        parts[0]['result'] = 'failed'
        parts[1]['checks'][0]['status'] = 'blocked'
        parts[1].update(result='blocked',coverage_gaps=[{
            'check_id':'properties','kind':'reviewer_incomplete','reason':'Parser not run'}])
        merged = contract.merge_evaluations(parts, context=context6())
        self.assertEqual(merged['result'],'failed')
        self.assertEqual(len(merged['coverage_gaps']),1)
        self.assertEqual(len(merged['checks'][0]['findings']),1)

    def test_excluded_global_checker_incomplete_does_not_create_local_gap(self):
        parts = [part6(g) for g in contract.LOCAL_GROUPS]
        for report in parts:
            report['mechanical_evidence'] = [{'result':'incomplete','excluded':'relation targets'}]
        merged = contract.merge_evaluations(parts, context=context6())
        self.assertEqual(merged['result'],'passed')
        self.assertEqual(merged['coverage_gaps'],[])
        self.assertEqual(merged['mechanical_evidence'][0]['result'],'incomplete')

    def test_missing_heading_does_not_block_evidence_based_local_review(self):
        packet = packet6()
        raw = SOURCE_TEXT.replace('## Scope\nAtoms\n','')
        candidate = source('mock.md','MOCK-R-001',raw)
        packet['sources'][0] = candidate; packet['candidate_bindings'] = [candidate['binding']]
        ctx = contract.ReviewContext(packet)
        report = part6('coherence')
        report.update(source=candidate['binding'], context_sha256=ctx.sha256)
        for row in report['checks']:
            row['positive_observations'][0]['location'] = 'body:3:## Claim'
        contract.validate_part(report, context=ctx)

    def test_legacy_body_can_be_reviewed_without_inventing_property_headings(self):
        packet = packet6()
        candidate = source('mock.md', 'MOCK-R-001', '# Atom rule\n\nAtom must comply.\n')
        packet['sources'][0] = candidate
        packet['candidate_bindings'] = [candidate['binding']]
        ctx = contract.ReviewContext(packet)
        report = part6('coherence')
        report.update(source=candidate['binding'], context_sha256=ctx.sha256)
        for row in report['checks']:
            row['positive_observations'][0]['location'] = 'body:1:# Atom rule'
        contract.validate_part(report, context=ctx)
        report['checks'][0]['positive_observations'][0]['location'] = 'body:3:## Scope'
        with self.assertRaisesRegex(ValueError, 'unknown source section'):
            contract.validate_part(report, context=ctx)

    def test_local_layout_alone_cannot_justify_skipped_semantic_check(self):
        report = part6('coherence')
        report['checks'][0]['status'] = 'blocked'
        report.update(result='blocked', coverage_gaps=[{
            'check_id': 'scope', 'kind': 'layout_dependency',
            'reason': 'Scope heading is absent.'}])
        with self.assertRaisesRegex(ValueError, 'layout alone'):
            contract.validate_part(report, context=context6())
        report['coverage_gaps'][0].update(kind='unresolved_interpretation',
            reason='The text supplies two incompatible applicability boundaries.')
        contract.validate_part(report, context=context6())

    def test_unknown_layout_repair_marker_cannot_bypass_local_boundary(self):
        report = part6('coherence')
        report['checks'][0]['status'] = 'blocked'
        report.update(result='blocked', repair_disposition='layout_recoding', coverage_gaps=[{
            'check_id': 'scope', 'kind': 'layout_dependency',
            'reason': 'Scope heading is absent.'}])
        with self.assertRaisesRegex(ValueError, 'layout alone'):
            contract.validate_part(report, context=context6())


if __name__ == '__main__':
    unittest.main()
