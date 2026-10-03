"""Bookkeeping regressions; no simulated semantic evaluation or recheck."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from workflow_progress import CHECKS, report_progress, summarize_progress


def report():
    return {'checks': {name: {'status': 'passed'} for name in CHECKS},
            'blockers': [], 'findings': [], 'unresolved_findings': [],
            'result': 'checked_clean'}


class WorkflowProgress(unittest.TestCase):
    def test_complete_clean_report(self):
        self.assertTrue(report_progress(report())['complete'])

    def test_edits_do_not_complete_skipped_checks(self):
        row = report()
        row['checks']['claim']['status'] = 'blocked'
        row['blockers'] = [{'check': 'claim', 'reason': 'Claim not assessed'}]
        row.update(result='fixed_not_rechecked', corrections=[{'finding_index': 0}])
        saved = deepcopy(row)
        progress = report_progress(row)
        self.assertFalse(progress['complete'])
        self.assertFalse(progress['check_complete'])
        self.assertEqual(progress['state'], 'blocked')
        self.assertEqual(progress['reported_result'], 'fixed_not_rechecked')
        self.assertEqual(row, saved)

    def test_missing_check_or_missing_gap_inventory_is_incomplete(self):
        for missing in ('claim', 'blockers'):
            row = report()
            if missing == 'blockers':
                del row['blockers']
            else:
                del row['checks'][missing]
            self.assertFalse(report_progress(row)['complete'])

    def test_safe_fix_does_not_hide_unresolved_findings(self):
        row = report()
        row.update(result='fixed_not_rechecked', unresolved_findings=[{'finding_index': 1}])
        self.assertFalse(report_progress(row)['complete'])
        del row['unresolved_findings']
        self.assertFalse(report_progress(row)['complete'])

    def test_complete_failed_checks_can_be_fixed_without_recheck(self):
        row = report()
        row['checks']['properties']['status'] = 'failed'
        row.update(result='fixed_not_rechecked', findings=[{'check': 'properties'}],
                   corrections=[{'finding_index': 0}])
        self.assertTrue(report_progress(row)['complete'])
        self.assertEqual(report_progress(row)['state'], 'fixed_not_rechecked')
        row['result'] = 'replaced_not_rechecked'
        self.assertTrue(report_progress(row)['complete'])

    def test_known_defects_remain_distinct_from_missing_coverage(self):
        row = report()
        row['checks']['claim']['status'] = 'failed'
        row.update(result='issues', findings=[{'check': 'claim'}])
        progress = report_progress(row)
        self.assertTrue(progress['check_complete'])
        self.assertFalse(progress['complete'])
        self.assertEqual(progress['state'], 'needs_fix')

    def test_processed_is_not_completed(self):
        gap = report()
        gap['checks']['scope']['status'] = 'blocked'
        gap['result'] = 'fixed_not_rechecked'
        result = summarize_progress([report(), gap, None])
        self.assertEqual(result['reported'], 2)
        self.assertEqual(result['completed'], 1)
        self.assertEqual(result['total'], 3)
        self.assertFalse(result['complete'])

    def test_every_finding_needs_its_own_disposition(self):
        row = report()
        row.update(result='fixed_not_rechecked', findings=[{'id': 'one'}, {'id': 'two'}],
                   corrections=[{'finding_id': 'one'}])
        self.assertFalse(report_progress(row)['complete'])
        row['rejected_findings'] = [{'finding_id': 'two', 'reason': 'Quoted rule admits it'}]
        self.assertTrue(report_progress(row)['complete'])

    def test_one_correction_can_cover_multiple_findings(self):
        row = report()
        row.update(result='fixed_not_rechecked', findings=[{}, {}],
                   corrections=[{'finding_indexes': [0, 1]}])
        self.assertTrue(report_progress(row)['complete'])

    def test_rejection_requires_reason_and_may_be_the_only_disposition(self):
        row = report()
        row.update(result='fixed_not_rechecked', findings=[{}],
                   rejected_findings=[{'finding_index': 0}])
        self.assertFalse(report_progress(row)['complete'])
        row['rejected_findings'][0]['reason'] = 'Applicable rule permits the current text'
        self.assertTrue(report_progress(row)['complete'])

    def test_fix_blocker_does_not_erase_initial_coverage(self):
        row = report()
        row.update(result='fixed_not_rechecked', findings=[{}],
                   corrections=[{'finding_index': 0}], fix_blockers=['Operator approval'])
        result = report_progress(row)
        self.assertTrue(result['check_complete'])
        self.assertFalse(result['complete'])

    def test_conflicting_unknown_and_duplicate_dispositions_fail_closed(self):
        for dispositions in ([{'finding_index': 9}],
                             [{'finding_index': 0}, {'finding_index': 0}]):
            row = report()
            row.update(result='fixed_not_rechecked', findings=[{}], corrections=dispositions)
            self.assertFalse(report_progress(row)['complete'])

    def test_prompts_preserve_three_steps_and_complete_first_check(self):
        root = Path(__file__).resolve().parents[1]
        checker = ' '.join((root / 'CA-O-109.prompt.md').read_text().split())
        fixer = ' '.join((root / 'CA-O-110.prompt.md').read_text().split())
        self.assertIn('Missing headings are properties defects', checker)
        self.assertIn('readable content', checker)
        self.assertIn('unfinished checks', fixer)
        self.assertIn('does not recheck saved output', fixer)


if __name__ == '__main__':
    unittest.main()
