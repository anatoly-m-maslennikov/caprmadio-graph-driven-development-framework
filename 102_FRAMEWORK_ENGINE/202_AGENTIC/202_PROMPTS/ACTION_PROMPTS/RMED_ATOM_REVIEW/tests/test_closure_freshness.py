"""Closure checks use live bytes; semantic judgments remain reviewer work."""
import hashlib
import tempfile
import unittest
from pathlib import Path

from closure_freshness import audit_bindings, close_batch


class ClosureFreshnessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'rule.md').write_text('version: 1\nold content\n')
        self.binding = {'path': 'rule.md', 'sha256': hashlib.sha256(
            (self.root / 'rule.md').read_bytes()).hexdigest()}
        self.admission = {'admission': 'accepted', 'evaluations': [{
            'source': self.binding, 'authority_sources': [self.binding],
            'parts': [{'prompt_sha256': self.binding['sha256']}]}]}

    def test_matching_bytes_pass_without_mutation(self):
        self.assertEqual(audit_bindings(self.root, [self.binding]), [])

    def test_same_version_changed_bytes_are_stale(self):
        (self.root / 'rule.md').write_text('version: 1\nnew formatting\n')
        issues = audit_bindings(self.root, [self.binding])
        self.assertEqual(issues[0]['kind'], 'stale_binding')
        self.assertEqual(self.binding['sha256'], issues[0]['expected_sha256'])

    def test_missing_file_blocks(self):
        self.binding['path'] = 'absent.md'
        self.assertEqual(audit_bindings(self.root, [self.binding])[0]['kind'], 'unreadable_binding')

    def test_empty_or_invalid_bindings_do_not_pass(self):
        self.assertTrue(audit_bindings(self.root, []))
        self.assertTrue(audit_bindings(self.root, [{'path': '../escape', 'sha256': 'x'}]))

    def test_conflicting_pins_block(self):
        other = dict(self.binding, sha256='0' * 64)
        self.assertTrue(audit_bindings(self.root, [self.binding, other]))

    def test_symlink_outside_root_is_not_read(self):
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as outside:
            target = Path(outside) / 'external'
            target.write_text('outside')
            (self.root / 'link').symlink_to(target)
            self.assertEqual(audit_bindings(self.root, [dict(self.binding, path='link')])[0]['kind'],
                             'invalid_binding')

    def test_every_closure_group_is_required(self):
        self.assertEqual(close_batch(self.root, {'admission': 'accepted'}, {})['result'], 'blocked')

    def test_pass_needs_fresh_candidates_rules_settings_and_prompts(self):
        groups = {key: [self.binding] for key in ('candidates', 'authority', 'settings', 'prompts')}
        result = close_batch(self.root, self.admission, groups)
        self.assertEqual(result['result'], 'fresh')
        self.assertFalse(result['completion_verified'])
        (self.root / 'rule.md').write_text('changed')
        result = close_batch(self.root, self.admission, groups)
        self.assertEqual(result['result'], 'blocked')
        self.assertEqual({x['group'] for x in result['issues']}, set(groups))

    def test_fresh_bytes_cannot_upgrade_failed_review(self):
        groups = {key: [self.binding] for key in ('candidates', 'authority', 'settings', 'prompts')}
        for status in ('failed', 'blocked', 'rejected'):
            self.assertEqual(close_batch(self.root, {'admission': status}, groups)['result'], 'blocked')

    def test_bare_acceptance_tag_is_not_admission_evidence(self):
        groups = {key: [self.binding] for key in ('candidates', 'authority', 'settings', 'prompts')}
        result = close_batch(self.root, {'admission': 'accepted'}, groups)
        self.assertEqual(result['result'], 'blocked')
        self.assertFalse(result['completion_verified'])

    def test_unrelated_pin_cannot_substitute_for_admitted_evidence(self):
        (self.root / 'unrelated.txt').write_text('unrelated')
        pin = {'path': 'unrelated.txt', 'sha256': hashlib.sha256(b'unrelated').hexdigest()}
        for group in ('candidates', 'authority', 'prompts'):
            groups = {key: [self.binding] for key in ('candidates', 'authority', 'settings', 'prompts')}
            groups[group] = [pin]
            with self.subTest(group=group):
                self.assertEqual(close_batch(self.root, self.admission, groups)['result'], 'blocked')
