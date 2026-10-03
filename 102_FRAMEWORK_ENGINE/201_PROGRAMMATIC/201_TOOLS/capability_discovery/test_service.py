"""Mock evidence tests; no real Workflow execution."""
import asyncio
import json
from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / 'VALIDATE_ATOMS'))
from capability_discovery.service import Service, Query, Observation, Watch


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir='/private/tmp', ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        control = self.root / '.caprmedio_caprmedio'
        control.mkdir()
        (control / 'caprmedio_project_settings.toml').write_text('[paths]\ncontrol_root=".caprmedio_caprmedio"\n')
        self.service = Service(self.root)

    def test_active_operations_only(self):
        for status in ('Active', 'Draft'):
            (self.root / '.caprmedio_caprmedio' / f'{status}.md').write_text(
                f'---\natom_id: CA-O-{status}\nstatus: {status}\ncontent_role: Operations\ntype: Action\n---\n# Summary\nFind things\n')
        result = self.service.discover(Query(), operations=True)
        self.assertEqual(result['total'], 1)

    def test_traversal_rejected(self):
        with self.assertRaises(ValueError):
            self.service.status(Observation(run_id='../outside'))

    def test_unknown_run_explicit(self):
        with self.assertRaisesRegex(ValueError, 'backend'):
            self.service.status(Observation(run_id='missing'))

    def test_watch_replays_confirmed_only(self):
        folder = self.root / '.caprmedio_tmp/rmed-base-revise/run1'
        folder.mkdir(parents=True)
        state = {'workflow_run_id': 'run1', 'outcome': 'completed',
                 'events': [{'event': {'event_id': 'confirmed'}, 'receipt': {'ok': True}},
                            {'event': {'event_id': 'pending'}, 'receipt': None}]}
        (folder / 'progress.json').write_text(json.dumps(state))
        first = asyncio.run(self.service.watch(Watch(run_id='run1')))
        self.assertEqual(len(first['notifications']), 1)
        second = asyncio.run(self.service.watch(Watch(run_id='run1', cursor=first['cursor'])))
        self.assertEqual(second['notifications'], [])
        self.assertFalse(second['changed'])

    def test_symlink_rejected(self):
        target = self.root / 'target'
        target.write_text('safe')
        link = self.root / 'link'
        link.symlink_to(target)
        with self.assertRaises(ValueError):
            self.service.read(link)

    def test_binding_refresh_and_ambiguity(self):
        control = self.root / '.caprmedio_caprmedio'
        source = control / 'binding.md'
        text = ('---\natom_id: CA-D-1\nstatus: Active\ncontent_role: Delivery\n---\n'
                '# Summary\nDiscover mock\n```toml\n[tool_binding]\nname="MOCK"\n'
                'entrypoint="mock.py"\naction_ids=[]\n```\n')
        source.write_text(text)
        self.assertEqual(self.service.discover(Query())['matches'][0]['availability'], 'missing')
        (self.root / 'mock.py').write_text('mock implementation')
        self.assertEqual(self.service.discover(Query())['matches'][0]['availability'], 'source')
        (control / 'duplicate.md').write_text(text)
        self.assertEqual(self.service.discover(Query())['matches'], [])

    def test_unknown_properties_rejected(self):
        with self.assertRaises(ValueError):
            Query.model_validate({'query': 'hello', 'extra': True})

    def test_cursor_invalid(self):
        with self.assertRaises(ValueError):
            asyncio.run(self.service.watch(Watch(run_id='one', cursor='invalid')))


if __name__ == '__main__':
    unittest.main()
