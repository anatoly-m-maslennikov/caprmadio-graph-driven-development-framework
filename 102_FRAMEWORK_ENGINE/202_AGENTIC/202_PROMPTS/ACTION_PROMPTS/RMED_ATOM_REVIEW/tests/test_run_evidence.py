"""Golden mock runs: evidence recording, not simulated semantic evaluation."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
from workflow_evidence import RunEvidence, render_report  # noqa: E402
from work_journal import append_sealed_events, validate_sealed_event, WorkJournalError  # noqa: E402
from workflow_progress import CHECKS  # noqa: E402


def checked(source, criteria):
    return {'atom_id': 'MOCK-R-1', 'source': source, 'criteria_sha256': criteria,
            'workflow_run_id': 'mock-run', 'result': 'checked_clean',
            'checks': {name: {'status': 'passed', 'evidence': 'mock evidence ' + name}
                       for name in CHECKS}, 'blockers': [], 'findings': [],
            'corrections': [], 'rejected_findings': [], 'unresolved_findings': [],
            'fix_blockers': []}


class RunEvidenceTests(unittest.TestCase):
    def setUp(self):
        temporary_root = HERE.parents[4] / '.caprmedio_tmp/tests/workflow-evidence'
        temporary_root.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(dir=temporary_root, ignore_cleanup_errors=True)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / '.git').mkdir()
        control = self.root / '.caprmedio_caprmedio'
        control.mkdir()
        (control / 'caprmedio_project_settings.toml').write_text(
            '[paths]\ncontrol_root=".caprmedio_caprmedio"\n'
            'journal_root=".caprmedio_caprmedio/_journal"\n')
        (self.root / 'atom.md').write_text('mock atom')
        (self.root / 'rules.md').write_text('mock rules')
        self.store = RunEvidence(self.root)
        self.identity = dict(author='mock-operator', session={'app': 'mock', 'uuid': 'mock-session'},
                             scope='MOCK', timezone='UTC')

    def start(self, selection=True):
        self.store.start('mock-run', {'scope': 'MOCK'}, **self.identity)
        return self.store.gather('mock-run', [{'atom_id': 'MOCK-R-1', 'path': 'atom.md'}]
                                 if selection else [], ['rules.md'])

    def test_clean_run_full_report_and_shared_journal(self):
        state = self.start()
        row = checked(state['selection'][0]['source'], state['criteria_sha256'])
        state = self.store.record('mock-run', 0, row, stage='check')
        state = self.store.finish('mock-run', 'completed')
        self.assertEqual(state['outcome'], 'completed')
        path = self.root / 'tmp/RMED Atoms Base Revise/mock-run.md'
        text = path.read_text()
        for section in ('# Run', '## Selection', '## Rules', '## Results',
                        '## Atom Reports', '## Remaining Work', '## Journal'):
            self.assertIn(section, text)
        self.assertIn('mock evidence claim', text)
        self.assertIn('MOCK-R-1', text)
        events = [json.loads(line) for p in self.root.rglob('*.ndjson')
                  for line in p.read_text().splitlines()]
        self.assertEqual([e['event'] for e in events],
                         ['started', 'progressed', 'progressed', 'completed'])
        self.assertEqual({e['workflow_run_id'] for e in events}, {'mock-run'})
        self.assertTrue(all(e['report_path'] == str(path.relative_to(self.root)) for e in events))

    def test_empty_run_and_pending_atoms_are_not_hidden(self):
        state = self.start(False)
        self.assertTrue(self.store.finish('mock-run', 'completed')['progress']['complete'])
        self.assertIn('No Atoms selected', render_report(state))

    def test_blocked_report_keeps_full_text_and_does_not_complete(self):
        state = self.start()
        row = checked(state['selection'][0]['source'], state['criteria_sha256'])
        row['checks']['claim'] = {'status': 'blocked', 'evidence': 'readable ' * 2000}
        row.update(result='blocked', blockers=['ambiguous Claim'])
        state = self.store.record('mock-run', 0, row, stage='check')
        self.assertIn('readable ' * 2000, render_report(state))
        with self.assertRaises(ValueError):
            self.store.finish('mock-run', 'completed')
        state = self.store.finish('mock-run', 'interrupted', reason='Operator decision')
        self.assertEqual(state['outcome'], 'interrupted')

    def test_recording_failure_retains_results_and_retry_does_not_repeat_events(self):
        state = self.start()
        row = checked(state['selection'][0]['source'], state['criteria_sha256'])
        with patch('workflow_evidence.append_sealed_events', side_effect=OSError('mock offline')):
            state = self.store.record('mock-run', 0, row, stage='check')
        self.assertEqual(state['reports'][0], row)
        self.assertTrue(state['recording_blockers'])
        self.assertIsNone(state['events'][-1]['receipt'])
        state = self.store.sync('mock-run')
        self.assertFalse(state['recording_blockers'])
        count = sum(len(p.read_text().splitlines()) for p in self.root.rglob('*.ndjson'))
        self.store.record('mock-run', 0, row, stage='check')
        self.store.sync('mock-run')
        self.assertEqual(count, sum(len(p.read_text().splitlines()) for p in self.root.rglob('*.ndjson')))

    def test_report_write_failure_visible_in_returned_and_saved_state(self):
        with patch.object(self.store, '_write_report', side_effect=OSError('mock full disk')):
            state = self.start()
        self.assertTrue(any(b['stage'] == 'report' for b in state['recording_blockers']))
        self.assertFalse(self.store.sync('mock-run')['recording_blockers'])

    def test_source_or_criteria_drift_blocks_fix_without_recheck(self):
        state = self.start()
        row = checked(state['selection'][0]['source'], state['criteria_sha256'])
        row.update(result='issues', findings=[{'id': 'f1'}])
        row['checks']['claim']['status'] = 'failed'
        self.store.record('mock-run', 0, row, stage='check')
        (self.root / 'rules.md').write_text('changed rules')
        with self.assertRaisesRegex(ValueError, 'stale criteria'):
            self.store.fix_context('mock-run', 0)
        (self.root / 'rules.md').write_text('mock rules')
        (self.root / 'atom.md').write_text('changed source')
        with self.assertRaisesRegex(ValueError, 'stale source'):
            self.store.fix_context('mock-run', 0)

    def test_fix_preserves_initial_checks_and_records_after_state(self):
        state = self.start()
        row = checked(state['selection'][0]['source'], state['criteria_sha256'])
        row.update(result='issues', findings=[{'id': 'f1'}])
        row['checks']['claim']['status'] = 'failed'
        self.store.record('mock-run', 0, row, stage='check')
        self.store.fix_context('mock-run', 0)
        (self.root / 'atom.md').write_text('authorized mock correction')
        row.update(result='fixed_not_rechecked', corrections=[{'finding_id': 'f1', 'change': 'mock fix'}])
        state = self.store.record('mock-run', 0, row, stage='fix', after_paths=['atom.md'])
        self.assertTrue(state['progress']['complete'])
        self.assertEqual(state['reports'][0]['checks']['claim']['status'], 'failed')
        self.assertNotEqual(state['after'][0][0]['sha256'], row['source']['sha256'])

    def test_unsafe_paths_and_existing_run_are_rejected(self):
        for run in ('../escape', '/absolute', 'a/b', '..'):
            with self.assertRaises(ValueError):
                self.store.start(run, {}, **self.identity)
        self.start()
        with self.assertRaisesRegex(ValueError, 'already exists'):
            self.store.start('mock-run', {'different': True}, **self.identity)
        for path in ('../escape.md', '/absolute.md', '.env', 'sub/.env.secret'):
            with self.assertRaises(ValueError):
                self.store.observe(path)

    def test_handoff_keeps_pending_atoms_and_same_run(self):
        self.start()
        state = self.store.handoff('mock-run', 'check ordinal 0 in a fresh context')
        self.assertEqual(state['outcome'], 'running')
        self.assertIn('pending', render_report(state))
        again = self.store.handoff('mock-run', 'check ordinal 0 in a fresh context')
        self.assertEqual(len(state['events']), len(again['events']))
        self.assertEqual({item['event']['workflow_run_id'] for item in state['events']}, {'mock-run'})

    def test_lost_append_acknowledgement_does_not_duplicate_event(self):
        state = self.start()
        row = checked(state['selection'][0]['source'], state['criteria_sha256'])

        def append_then_lose_ack(*args, **kwargs):
            append_sealed_events(*args, **kwargs)
            raise OSError('lost acknowledgement after append')

        with patch('workflow_evidence.append_sealed_events', side_effect=append_then_lose_ack):
            self.store.record('mock-run', 0, row, stage='check')
        before = sum(len(p.read_text().splitlines()) for p in self.root.rglob('*.ndjson'))
        state = self.store.sync('mock-run')
        after = sum(len(p.read_text().splitlines()) for p in self.root.rglob('*.ndjson'))
        self.assertEqual(before, after)
        self.assertIsNotNone(state['events'][-1]['receipt'])

    def test_symlink_target_and_forged_event_digest_rejected(self):
        (self.root / 'linked.md').symlink_to(self.root / 'atom.md')
        with self.assertRaises(ValueError):
            self.store.observe('linked.md')
        state = self.start()
        event = state['events'][0]['event'].copy()
        event['outcome'] = 'forged'
        with self.assertRaises(WorkJournalError):
            validate_sealed_event(event)

    def test_completed_check_cannot_be_silently_rewritten(self):
        state = self.start()
        row = checked(state['selection'][0]['source'], state['criteria_sha256'])
        self.store.record('mock-run', 0, row, stage='check')
        row['checks']['claim']['evidence'] = 'new review'
        with self.assertRaisesRegex(ValueError, 'no recheck'):
            self.store.record('mock-run', 0, row, stage='check')

    def test_partial_fix_handoff_resumes_from_saved_after_without_recheck(self):
        state = self.start()
        row = checked(state['selection'][0]['source'], state['criteria_sha256'])
        row.update(result='issues', findings=[{'id': 'f1'}, {'id': 'f2'}])
        row['checks']['claim']['status'] = 'failed'
        self.store.record('mock-run', 0, row, stage='check')
        self.store.fix_context('mock-run', 0)
        (self.root / 'atom.md').write_text('first correction')
        row.update(result='blocked', corrections=[{'finding_id': 'f1'}],
                   unresolved_findings=[{'finding_id': 'f2'}], fix_blockers=['capacity'])
        self.store.record('mock-run', 0, row, stage='fix', after_paths=['atom.md'])
        self.store.handoff('mock-run', 'finish f2')
        current = self.store.fix_context('mock-run', 0)
        self.assertNotEqual(current['current_sources'][0], row['source'])
        (self.root / 'atom.md').write_text('second correction')
        row.update(result='fixed_not_rechecked',
            corrections=[{'finding_id': 'f1'}, {'finding_id': 'f2'}],
            unresolved_findings=[], fix_blockers=[])
        state = self.store.record('mock-run', 0, row, stage='fix', after_paths=['atom.md'])
        self.assertTrue(state['progress']['complete'])
        self.assertEqual(len(state['history'][0]), 2)


if __name__ == '__main__':
    unittest.main()
