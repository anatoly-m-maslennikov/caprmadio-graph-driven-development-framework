"""Reject internally inconsistent completed reviews, not infer missing Entities."""
import unittest

from test_split_evaluation import SOURCE_TEXT, RULE_TEXT, contract, gap, part, source
from context_builder import body_sections, markdown


def response(governs='Atom', dependencies=()):
    import json
    raw = ('---\nsubjects:\n  governs: ' + json.dumps(governs)
           + '\n  depends_on: ' + json.dumps(list(dependencies)) + '\n---\n' + markdown(SOURCE_TEXT))
    candidate = source('mock.md', 'MOCK-R-001', raw)
    ctx = contract.ReviewContext({'confidence_threshold': .99, 'sources': [
        candidate, source('rule.md', 'MOCK-R-002', RULE_TEXT)]})
    report = part('coherence')
    report.update(source=candidate['binding'], context_sha256=ctx.sha256)
    report['checks'][0]['subject_inventory']['sections_reviewed'] = body_sections(raw)
    return report, ctx


def finding(entity, issue):
    return dict(kind='violation', subject_issue=issue, entity=entity, confidence=1.0,
                location='subjects', excerpt=entity, reason='Synthetic explicit comparison.',
                proposed_fix='Apply the evidence-backed synthetic correction.')


class SubjectAccounting(unittest.TestCase):
    def test_complete_pass_must_not_silently_retain_uninventoried_dependency(self):
        report, ctx = response(dependencies=('Hidden',))
        with self.assertRaisesRegex(ValueError, 'unaccounted declared'):
            contract.validate_part(report, context=ctx)

    def test_complete_pass_must_not_silently_skip_resolved_missing_target(self):
        report, ctx = response(governs='Hidden')
        with self.assertRaisesRegex(ValueError, 'unaccounted resolved'):
            contract.validate_part(report, context=ctx)

    def test_governs_correction_accounts_for_coordinated_old_and_new_targets(self):
        report, ctx = response(governs='Hidden')
        report['checks'][0].update(status='failed', findings=[finding('Atom', 'governs')])
        report['result'] = 'failed'
        contract.validate_part(report, context=ctx)

    def test_unresolved_inventory_never_forces_an_extra_subject_deletion(self):
        report, ctx = response(dependencies=('Hidden',))
        report['checks'][0]['subject_inventory']['complete'] = False
        report['checks'][0]['status'] = 'blocked'
        report.update(result='blocked', coverage_gaps=[gap('subjects', 'Possible contextual reference unresolved')])
        contract.validate_part(report, context=ctx)

    def test_known_unrelated_failure_does_not_hide_another_unaccounted_target(self):
        report, ctx = response(dependencies=('Atom', 'Hidden'))
        report['checks'][0].update(status='failed', findings=[finding('Atom', 'duplicate')])
        report['result'] = 'failed'
        with self.assertRaisesRegex(ValueError, 'unaccounted declared'):
            contract.validate_part(report, context=ctx)

    def test_duplicate_declared_targets_cannot_pass(self):
        report, ctx = response(dependencies=('Atom',))
        with self.assertRaisesRegex(ValueError, 'duplicate declared'):
            contract.validate_part(report, context=ctx)

    def test_exact_current_governs_cannot_be_reported_as_a_governs_mismatch(self):
        report, ctx = response()
        report['checks'][0].update(status='failed', findings=[finding('Atom', 'governs')])
        report['result'] = 'failed'
        with self.assertRaisesRegex(ValueError, 'already GOVERNS'):
            contract.validate_part(report, context=ctx)

    def test_malformed_governs_does_not_crash_subject_comparison(self):
        report, ctx = response(governs=['Atom'])
        with self.assertRaisesRegex(ValueError, 'unaccounted resolved'):
            contract.validate_part(report, context=ctx)


if __name__ == '__main__':
    unittest.main()
