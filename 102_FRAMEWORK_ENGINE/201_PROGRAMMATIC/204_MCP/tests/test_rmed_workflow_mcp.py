"""Real stdio protocol with mock Atoms; no live review or Agent dispatch."""
from pathlib import Path
import sys
import tempfile
import unittest

from mcp import Client, StdioServerParameters

ROOT = Path(__file__).resolve().parents[4]
SERVER = ROOT / '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py'


class MCPWorkflow(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        tmp = ROOT / '.caprmedio_tmp/tests/workflow-mcp'
        tmp.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=tmp, ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / '.git').mkdir()
        control = self.root / '.caprmedio_caprmedio'
        control.mkdir()
        (control / 'caprmedio_project_settings.toml').write_text(
            '[paths]\njournal_root=".caprmedio_caprmedio/work_journal"\n')
        (self.root / 'atom.md').write_text('mock original atom')
        (self.root / 'rules.md').write_text('mock applicable criteria')

    async def test_stdio_gather_check_fix_report(self):
        params = StdioServerParameters(command=sys.executable,
            args=[str(SERVER), '--project-root', str(self.root)])
        async with Client(params) as client:
            tools = await client.list_tools()
            self.assertEqual({tool.name for tool in tools.tools}, {
                'rmed_atoms_base_revise', 'discover_tools', 'discover_operations',
                'get_execution_context', 'get_execution_status',
                'resume_execution_context', 'watch_execution', 'workflow_orchestrator',
                'reload_mcp_implementation', 'get_mcp_reload_status'})
            schema = next(tool for tool in tools.tools if tool.name == 'workflow_orchestrator').input_schema
            encoded_schema = __import__('json').dumps(schema)
            self.assertIn('allow_replacements', encoded_schema)
            self.assertFalse(schema['$defs']['Enqueue']['properties']['allow_replacements']['default'])
            discovered = await client.call_tool('discover_tools', {'request': {'query': 'missing'}})
            self.assertFalse(discovered.is_error)
            self.assertEqual(discovered.structured_content['matches'], [])

            async def call(**request):
                result = await client.call_tool('rmed_atoms_base_revise', {'request': request})
                self.assertFalse(result.is_error, str(result))
                return result.structured_content

            help_result = await call(operation='describe')
            self.assertIn('gather', help_result['steps'])
            started = await call(operation='start', run_id='mcp-mock', request={'scope': 'MOCK'},
                author='mock-operator', session={'app': 'test', 'uuid': 'mock-session'}, scope='MOCK')
            self.assertEqual(started['outcome'], 'running')
            await call(operation='gather', run_id='mcp-mock',
                selection=[{'atom_id': 'MOCK-R-1', 'path': 'atom.md'}], criteria_paths=['rules.md'])
            context = await call(operation='context', run_id='mcp-mock', ordinal=0, stage='check')
            self.assertEqual(context['source_content'], 'mock original atom')
            report = {'workflow_run_id': 'mcp-mock', 'atom_id': 'MOCK-R-1',
                'source': context['source'], 'criteria_sha256': context['criteria_sha256'],
                'checks': {name: {'status': 'passed', 'evidence': 'mock quotation'} for name in
                           ('properties', 'cce', 'scope', 'claim', 'details', 'summary')},
                'findings': [{'id': 'f1', 'check': 'cce', 'evidence': 'mock quote'}],
                'blockers': [], 'corrections': [], 'unresolved_findings': [{'finding_id': 'f1'}],
                'rejected_findings': [], 'fix_blockers': [], 'result': 'issues'}
            report['checks']['cce']['status'] = 'failed'
            submitted = await call(operation='submit', run_id='mcp-mock', ordinal=0,
                                   stage='check', report=report)
            self.assertEqual(submitted['progress']['checked'], 1)
            self.assertEqual(submitted['progress']['completed'], 0)
            await call(operation='context', run_id='mcp-mock', ordinal=0, stage='fix')
            (self.root / 'atom.md').write_text('authorized mock correction')
            report.update(result='fixed_not_rechecked',
                corrections=[{'finding_id': 'f1', 'change': 'mock correction'}], unresolved_findings=[])
            await call(operation='submit', run_id='mcp-mock', ordinal=0, stage='fix',
                       report=report, after_paths=['atom.md'])
            final = await call(operation='finish', run_id='mcp-mock', outcome='completed')
            self.assertEqual(final['progress']['completed'], 1)
            self.assertEqual(final['recording_blockers'], [])
            rendered = await call(operation='report', run_id='mcp-mock')
            self.assertIn('mock quotation', rendered['markdown'])
            self.assertIn('fixed_not_rechecked', rendered['markdown'])
            self.assertTrue((self.root / final['report_path']).is_file())
            observed = await client.call_tool('get_execution_status', {'request': {
                'run_id': 'mcp-mock', 'include_results': True}})
            self.assertFalse(observed.is_error)
            self.assertEqual(observed.structured_content['outcome'], 'completed')
            self.assertEqual(observed.structured_content['results'][0]['result'], 'fixed_not_rechecked')
            watched = await client.call_tool('watch_execution', {'request': {'run_id': 'mcp-mock'}})
            self.assertFalse(watched.is_error)
            self.assertTrue(watched.structured_content['terminal'])
            replay = await client.call_tool('watch_execution', {'request': {
                'run_id': 'mcp-mock', 'cursor': watched.structured_content['cursor']}})
            self.assertEqual(replay.structured_content['notifications'], [])

    async def test_protocol_rejects_unknown_fields_and_path_escape(self):
        async with Client(StdioServerParameters(command=sys.executable,
                args=[str(SERVER), '--project-root', str(self.root)])) as client:
            for request in ({'operation': 'describe', 'surprise': True},
                            {'operation': 'status', 'run_id': '../escape'}):
                result = await client.call_tool('rmed_atoms_base_revise', {'request': request})
                self.assertTrue(result.is_error)


if __name__ == '__main__':
    unittest.main()
