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
sys.path.insert(0, str(TOOLS.parent / '204_MCP'))
from capability_discovery.service import Service, Query, Observation, Watch
from unittest.mock import patch


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
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

    def test_catalog_excludes_persistent_journal_and_projection_carriers(self):
        control = self.root / '.caprmedio_caprmedio'
        for relative, identity in (
            ('visible.md', 'CA-O-visible'),
            ('_journal/hidden.md', 'CA-O-journal'),
            ('_projection/hidden.md', 'CA-O-projection'),
        ):
            path = control / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                f'---\natom_id: {identity}\nstatus: Active\ncontent_role: Operations\ntype: Action\n---\n# Summary\nFixture\n'
            )

        result = self.service.discover(Query(), operations=True)

        self.assertEqual(['CA-O-visible'], [row['id'] for row in result['matches']])

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

    def test_admitted_release_route_is_discoverable_and_has_compact_context(self):
        control = self.root / '.caprmedio_caprmedio'
        operation = control / 'release.md'
        operation.write_text(
            '---\natom_id: CA-O-164\nstatus: Active\ncontent_role: Operations\ntype: Workflow\n---\n'
            '# Summary\nRelease selected Framework Version\n'
        )
        manifest = {
            'manifest_ref': '.caprmedio_caprmedio/_projection/selected_workflow_bindings.json',
            'canonical_manifest_sha256': 'a' * 64,
            'source_freshness': {'selected_binding_digest': 'b' * 64},
            'routes': [{'route': 'release_version', 'workflow': {'atom_id': 'CA-O-164'},
                        'ordered_actions': [{'atom_id': 'CA-O-165'}]}],
        }
        self.service.exposed.add('release_version')
        with patch('selected_routes.load_selected_manifest', return_value=manifest):
            tools = self.service.discover(Query(query='release_version'))
            operations = self.service.discover(Query(query='CA-O-164'), operations=True)
            context = self.service.context(type('Request', (), {'id': 'CA-O-164'})())

        self.assertEqual(['release_version'], [row['name'] for row in tools['matches']])
        self.assertEqual('mcp', operations['matches'][0]['availability'])
        self.assertEqual(['release_version'], operations['matches'][0]['tools'])
        self.assertEqual([], context['related_definitions'])
        self.assertTrue(context['context_complete'])
        self.assertEqual('release_version', context['input_schema']['properties']['operation_route']['const'])

    def test_admitted_selected_routes_keep_route_and_workflow_context_exact(self):
        control = self.root / '.caprmedio_caprmedio'
        for identity, role in (('CA-O-127', 'Workflow'), ('CA-O-130', 'Workflow'), ('CA-O-128', 'Action')):
            (control / f'{identity}.md').write_text(
                f'---\natom_id: {identity}\nstatus: Active\ncontent_role: Operations\ntype: {role}\n---\n'
                f'# Summary\n{identity}\n'
            )
        manifest = {
            'manifest_ref': '.caprmedio_caprmedio/_projection/selected_workflow_bindings.json',
            'canonical_manifest_sha256': 'a' * 64,
            'source_freshness': {'selected_binding_digest': 'b' * 64},
            'routes': [
                {'route': 'create_atom', 'workflow': {'atom_id': 'CA-O-127'},
                 'ordered_actions': [{'atom_id': 'CA-O-128'}]},
                {'route': 'update_atom', 'workflow': {'atom_id': 'CA-O-130'},
                 'ordered_actions': [{'atom_id': 'CA-O-128'}]},
            ],
        }
        self.service.exposed.update(('create_atom', 'update_atom'))
        with patch('selected_routes.load_selected_manifest', return_value=manifest):
            route = self.service.context(type('Request', (), {'id': 'create_atom'})())
            workflow = self.service.context(type('Request', (), {'id': 'CA-O-127'})())
            action = self.service.context(type('Request', (), {'id': 'CA-O-128'})())

        for context in (route, workflow, action):
            self.assertTrue(context['context_complete'])
            self.assertEqual('a' * 64, context['definition']['definition_manifest']['manifest_digest'])
        self.assertEqual(['create_atom'], route['definition']['tools'])
        self.assertEqual('create_atom', route['input_schema']['properties']['operation_route']['const'])
        self.assertEqual(['create_atom'], workflow['definition']['tools'])
        self.assertEqual('create_atom', workflow['input_schema']['properties']['operation_route']['const'])
        self.assertEqual(['create_atom', 'update_atom'], action['definition']['tools'])
        self.assertIsNone(action['input_schema'])

    def test_unadmitted_release_route_is_not_synthesized(self):
        manifest = {
            'manifest_ref': '.caprmedio_caprmedio/_projection/selected_workflow_bindings.json',
            'canonical_manifest_sha256': 'a' * 64,
            'source_freshness': {}, 'routes': [],
        }
        self.service.exposed.add('release_version')
        with patch('selected_routes.load_selected_manifest', return_value=manifest):
            self.assertEqual([], self.service.discover(Query(query='release_version'))['matches'])

    def test_generic_selected_route_is_not_synthesized_when_unexposed_or_stale(self):
        manifest = {
            'manifest_ref': '.caprmedio_caprmedio/_projection/selected_workflow_bindings.json',
            'canonical_manifest_sha256': 'a' * 64,
            'source_freshness': {'selected_binding_digest': 'b' * 64},
            'routes': [{'route': 'create_atom', 'workflow': {'atom_id': 'CA-O-127'},
                        'ordered_actions': [{'atom_id': 'CA-O-128'}]}],
        }
        with patch('selected_routes.load_selected_manifest', return_value=manifest):
            self.assertEqual([], self.service.discover(Query(query='create_atom'))['matches'])
        self.service.exposed.add('create_atom')
        with patch('selected_routes.load_selected_manifest', side_effect=ValueError('source pin is stale')):
            self.assertEqual([], self.service.discover(Query(query='create_atom'))['matches'])

    def test_source_only_action_is_not_upgraded_to_an_admitted_selected_route(self):
        control = self.root / '.caprmedio_caprmedio'
        (control / 'action.md').write_text(
            '---\natom_id: CA-O-128\nstatus: Active\ncontent_role: Operations\ntype: Action\n---\n'
            '# Summary\nSource-only Action\n'
        )
        manifest = {
            'manifest_ref': '.caprmedio_caprmedio/_projection/selected_workflow_bindings.json',
            'canonical_manifest_sha256': 'a' * 64,
            'source_freshness': {'selected_binding_digest': 'b' * 64},
            'routes': [{'route': 'create_atom', 'workflow': {'atom_id': 'CA-O-127'},
                        'ordered_actions': [{'atom_id': 'CA-O-999'}]}],
        }
        self.service.exposed.add('create_atom')
        with patch('selected_routes.load_selected_manifest', return_value=manifest):
            context = self.service.context(type('Request', (), {'id': 'CA-O-128'})())

        self.assertNotIn('tools', context['definition'])
        self.assertIsNone(context['input_schema'])

    def test_stale_release_manifest_is_not_synthesized_even_when_exposed(self):
        self.service.exposed.add('release_version')
        with patch('selected_routes.load_selected_manifest', side_effect=ValueError('source pin is stale')):
            self.assertEqual([], self.service.discover(Query(query='release_version'))['matches'])

    def test_admitted_release_route_is_not_advertised_when_unexposed(self):
        manifest = {
            'manifest_ref': '.caprmedio_caprmedio/_projection/selected_workflow_bindings.json',
            'canonical_manifest_sha256': 'a' * 64,
            'source_freshness': {'selected_binding_digest': 'b' * 64},
            'routes': [{'route': 'release_version', 'workflow': {'atom_id': 'CA-O-164'},
                        'ordered_actions': [{'atom_id': 'CA-O-165'}]}],
        }
        with patch('selected_routes.load_selected_manifest', return_value=manifest):
            self.assertEqual([], self.service.discover(Query(query='release_version'))['matches'])

    def test_unknown_properties_rejected(self):
        with self.assertRaises(ValueError):
            Query.model_validate({'query': 'hello', 'extra': True})

    def test_cursor_invalid(self):
        with self.assertRaises(ValueError):
            asyncio.run(self.service.watch(Watch(run_id='one', cursor='invalid')))


if __name__ == '__main__':
    unittest.main()
