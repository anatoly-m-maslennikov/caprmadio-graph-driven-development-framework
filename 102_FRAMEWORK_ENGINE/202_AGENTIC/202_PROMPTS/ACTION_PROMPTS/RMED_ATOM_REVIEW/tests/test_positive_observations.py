"""Quote provenance checks; these fixtures do not simulate semantic judgment."""
from copy import deepcopy
import unittest

from test_split_evaluation import SOURCE_TEXT, RULE_TEXT, contract, part, source


def context5():
    return contract.ReviewContext({
        'confidence_threshold': .99,
        'review_constraints': {'report_contract': 5},
        'sources': [source('mock.md', 'MOCK-R-001', SOURCE_TEXT),
                    source('rule.md', 'MOCK-R-002', RULE_TEXT)],
    })


def response(group='cce'):
    report = part(group)
    report.update(contract_version=5, context_sha256=context5().sha256)
    for check in report['checks']:
        check['positive_observations'] = [{
            'location': 'body:5:## Claim', 'excerpt': 'Atom must comply.',
            'authority': 'MOCK-R-002@1',
            'rule_excerpt': 'Atom means a governed statement.',
        }]
    return report


def nonpassing_response(status):
    report = response()
    check = report['checks'][0]
    if status == 'failed':
        check.update(status='failed', findings=[{
            'kind': 'violation', 'location': 'body:5:## Claim',
            'excerpt': 'Atom must comply.', 'reason': 'Synthetic test failure.',
            'proposed_fix': 'Repair the synthetic test condition.', 'confidence': .99,
        }])
        report['result'] = 'failed'
    else:
        check['status'] = 'blocked'
        report.update(result='blocked', coverage_gaps=[{
            'check_id': 'cce', 'kind': 'reviewer_incomplete',
            'reason': 'Synthetic incomplete review.'}])
    return report


class PositiveObservations(unittest.TestCase):
    def test_bound_candidate_and_rule_quotes_are_accepted(self):
        contract.validate_part(response(), context=context5())

    def test_generic_pass_without_observation_is_rejected(self):
        report = response()
        report['checks'][0].pop('positive_observations')
        with self.assertRaisesRegex(ValueError, 'positive observations'):
            contract.validate_part(report, context=context5())

    def test_nonpasses_may_omit_or_leave_observations_empty(self):
        for status in ('failed', 'blocked'):
            for observations in ('missing', []):
                report = nonpassing_response(status)
                if observations == 'missing':
                    report['checks'][0].pop('positive_observations')
                else:
                    report['checks'][0]['positive_observations'] = observations
                with self.subTest(status=status, observations=observations):
                    contract.validate_part(report, context=context5())

    def test_nonpass_observations_are_validated_when_supplied(self):
        changes = [
            ({'location': 'body:6:## Claim'}, 'unknown source'),
            ({'excerpt': 'not in this Atom'}, 'absent'),
            ({'rule_excerpt': 'This rule was never written.'}, 'absent'),
        ]
        for status in ('failed', 'blocked'):
            contract.validate_part(nonpassing_response(status), context=context5())
            for change, message in changes:
                report = nonpassing_response(status)
                report['checks'][0]['positive_observations'][0].update(change)
                with self.subTest(status=status, change=change), self.assertRaisesRegex(ValueError, message):
                    contract.validate_part(report, context=context5())

    def test_malformed_nonpass_observations_fail_closed(self):
        for status in ('failed', 'blocked'):
            for observations in (None, 'not a list', [None]):
                report = nonpassing_response(status)
                report['checks'][0]['positive_observations'] = observations
                with self.subTest(status=status, observations=observations), self.assertRaises(ValueError):
                    contract.validate_part(report, context=context5())

    def test_bad_candidate_addresses_and_quotes_are_rejected(self):
        for change, message in [({'location': 'body:6:## Claim'}, 'unknown source'),
                                ({'excerpt': 'not in this Atom'}, 'absent'),
                                ({'excerpt': ''}, 'absent')]:
            report = response()
            report['checks'][0]['positive_observations'][0].update(change)
            with self.subTest(change=change), self.assertRaisesRegex(ValueError, message):
                contract.validate_part(report, context=context5())

    def test_unbound_or_unlisted_rule_and_invented_quote_are_rejected(self):
        for change, message in [({'authority': 'MOCK-R-003@1'}, 'bound check authority'),
                                ({'rule_excerpt': 'This rule was never written.'}, 'absent')]:
            report = response()
            report['checks'][0]['positive_observations'][0].update(change)
            with self.subTest(change=change), self.assertRaisesRegex(ValueError, message):
                contract.validate_part(report, context=context5())
        report = response()
        report['checks'][0]['authority'] = []
        with self.assertRaises(ValueError):
            contract.validate_part(report, context=context5())

    def test_frontmatter_anchor_is_supported_without_inventing_a_body_section(self):
        report = response('properties')
        report['checks'][0]['positive_observations'][0].update(
            location='frontmatter', excerpt='governs: Atom')
        contract.validate_part(report, context=context5())

    def test_frontmatter_only_does_not_support_cce_or_coherence_pass(self):
        for group in ('cce', 'coherence'):
            report = response(group)
            report['checks'][0]['positive_observations'][0].update(
                location='frontmatter', excerpt='governs: Atom')
            with self.subTest(group=group), self.assertRaisesRegex(ValueError, 'unknown source section'):
                contract.validate_part(report, context=context5())

    def test_malformed_or_foreign_gap_is_rejected_without_crashing(self):
        for group in ('cce', 'properties'):
            for gap in (None, [], 'not an object', {
                    'check_id': 'subjects', 'kind': 'unresolved_interpretation',
                    'reason': 'This evaluator has no Subjects check.'}):
                report = response(group)
                report['coverage_gaps'] = [gap]
                with self.subTest(group=group, gap=gap), self.assertRaises(ValueError):
                    contract.validate_part(report, context=context5())
                with self.subTest(direct=True, group=group, gap=gap), self.assertRaises(ValueError):
                    contract.validate_report_quality(report, SOURCE_TEXT,
                        authorities={'MOCK-R-002@1': RULE_TEXT})

    def test_empty_details_can_be_observed_by_its_actual_heading(self):
        report = response()
        report['checks'][0]['positive_observations'][0].update(
            location='body:7:## Details', excerpt='## Details')
        contract.validate_part(report, context=context5())

    def test_frontmatter_quote_cannot_be_claimed_as_body_text(self):
        report = response()
        report['checks'][0]['positive_observations'][0]['excerpt'] = 'governs: Atom'
        with self.assertRaisesRegex(ValueError, 'absent'):
            contract.validate_part(report, context=context5())

    def test_empty_inventory_does_not_establish_interpretive_ambiguity(self):
        report = response('coherence')
        report['checks'][0].update(status='blocked', subject_inventory={
            **report['checks'][0]['subject_inventory'], 'complete': False, 'mentions': []})
        report.update(result='blocked', coverage_gaps=[{
            'check_id': 'subjects', 'kind': 'unresolved_interpretation',
            'reason': 'Frozen entity index has no exact full-target definition anchor.'}])
        with self.assertRaisesRegex(ValueError, 'requires an unresolved mention'):
            contract.validate_part(report, context=context5())
        report['coverage_gaps'][0].update(kind='reviewer_incomplete', reason='Body evidence not yet reviewed.')
        contract.validate_part(report, context=context5())

    def test_genuine_quoted_ambiguity_remains_blocked_not_failed(self):
        report = response('coherence')
        inventory = report['checks'][0]['subject_inventory']
        inventory.update(complete=False, mentions=[{
            'location': 'body:5:## Claim', 'excerpt': 'Atom', 'entity': None,
            'resolution': 'unresolved', 'resolution_basis': None,
            'rationale': 'Synthetic ambiguous referent pending interpretation.', 'definitions': []}])
        report['checks'][0]['status'] = 'blocked'
        report.update(result='blocked', coverage_gaps=[{
            'check_id': 'subjects', 'kind': 'unresolved_interpretation',
            'reason': 'Synthetic quoted referent remains ambiguous.'}])
        contract.validate_part(report, context=context5())

    def test_historical_records_cannot_be_relabelled_into_new_context(self):
        report = part('cce')
        report['context_sha256'] = context5().sha256
        with self.assertRaisesRegex(ValueError, 'contract does not match caller'):
            contract.validate_part(report, context=context5())
        report['contract_version'] = 5
        with self.assertRaisesRegex(ValueError, 'positive observations'):
            contract.validate_part(report, context=context5())

    def test_merge_retains_contract_five_and_raw_parts(self):
        parts = [response(group) for group in contract.GROUPS]
        before = deepcopy(parts)
        merged = contract.merge_evaluations(parts, context=context5())
        self.assertEqual(merged['contract_version'], 5)
        self.assertEqual(merged['parts'], before)
        self.assertEqual(parts, before)

    def test_invalid_caller_contract_settings_fail_closed(self):
        for constraints in (None, [], {'report_contract': True}, {'report_contract': 6}):
            with self.subTest(constraints=constraints), self.assertRaises(ValueError):
                contract.ReviewContext({
                    'confidence_threshold': .99, 'review_constraints': constraints,
                    'sources': [source('mock.md', 'MOCK-R-001', SOURCE_TEXT)]})


if __name__ == '__main__':
    unittest.main()
