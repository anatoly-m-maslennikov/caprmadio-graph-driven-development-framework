"""Real stdio protocol with mock Atoms; no live review or Agent dispatch."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest

from mcp import Client, StdioServerParameters

ROOT = Path(__file__).resolve().parents[4]
SERVER = ROOT / '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py'
MCP = SERVER.parent
sys.path.insert(0, str(MCP))

from selected_routes import QUERY_ROUTE_NAMES, SELECTED_ROUTE_NAMES  # noqa: E402


# CA-D-548's eight stable helpers plus its gateway controls remain required.
D548_REQUIRED_TOOLS = frozenset({
    'rmed_atoms_base_revise', 'discover_tools', 'discover_operations',
    'get_execution_context', 'get_execution_status',
    'resume_execution_context', 'watch_execution', 'workflow_orchestrator',
    'reload_mcp_implementation', 'get_mcp_reload_status',
})

# CA-D-547 v5 is the reviewed admission boundary.  This independently fixed
# tuple prevents the registration registry from making its own test pass.
D547_ADMITTED_SELECTED_ROUTES = (
    'create_atom', 'update_atom', 'replace_atom', 'change_atom_status',
    'create_scope_unit', 'rename_scope_unit', 'move_scope_unit', 'remove_scope_unit',
    'run_implementation_workflow', 'revert_changes', 'build_entities_graph',
    'build_terms_graph', 'build_applicable_methodology',
    'find_and_fetch_artifacts', 'find_and_fetch_journal_events',
)
D547_SELECTED_CONTROL_TOOLS = frozenset({
    'get_selected_workflow_run', 'get_selected_action_run',
    'recover_selected_run_recording',
})


class InstalledLayoutImport(unittest.TestCase):
    def test_implementation_imports_from_framework_engine_layout(self):
        """The release copies the Engine without the source-tree numeric prefix."""
        with tempfile.TemporaryDirectory() as temporary:
            installed = Path(temporary) / 'opt/caprmedio-framework/FRAMEWORK_ENGINE'
            shutil.copytree(ROOT / '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC',
                            installed / '201_PROGRAMMATIC',
                            ignore=shutil.ignore_patterns('__pycache__', '.caprmedio_tmp'))
            shutil.copytree(ROOT / '102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW',
                            installed / '202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW',
                            ignore=shutil.ignore_patterns('__pycache__', '.mypy_cache'))
            implementation = installed / '201_PROGRAMMATIC/204_MCP/implementation_server.py'
            result = subprocess.run([sys.executable, '-B', '-c',
                                     'import runpy, sys; sys.path.insert(0, ' +
                                     repr(str(implementation.parent)) +
                                     '); runpy.run_path(' + repr(str(implementation)) + ')'],
                                    capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stderr)


class MCPWorkflow(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        # The sealed Unit mounts the repository read-only; the runner supplies
        # a writable per-module TMPDIR for disposable protocol fixtures.
        self.temp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / '.git').mkdir()
        control = self.root / '.caprmedio_caprmedio'
        control.mkdir()
        (control / 'caprmedio_project_settings.toml').write_text(
            '[paths]\ncontrol_root=".caprmedio_caprmedio"\njournal_root=".caprmedio_caprmedio/_journal"\n')
        (self.root / 'atom.md').write_text('mock original atom')
        (self.root / 'rules.md').write_text('mock applicable criteria')

    def _copy_active_query_bindings(self):
        """Seed this disposable Project from current D-carriers, not a fake exposure list."""
        delivery = ROOT / '.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery'
        bindings = {}
        for source in delivery.glob('*.md'):
            for block in source.read_text(encoding='utf-8').split('```toml')[1:]:
                binding = tomllib.loads(block.split('```', 1)[0]).get('tool_binding')
                if isinstance(binding, dict) and binding.get('mcp_name') in QUERY_ROUTE_NAMES:
                    bindings[binding['mcp_name']] = (source, binding)
        self.assertEqual(set(QUERY_ROUTE_NAMES), set(bindings))
        for source, binding in bindings.values():
            carrier = self.root / source.relative_to(ROOT)
            carrier.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, carrier)
            entrypoint = ROOT / binding['entrypoint']
            self.assertTrue(entrypoint.is_file())
            destination = self.root / binding['entrypoint']
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(entrypoint, destination)

    async def test_real_server_discovery_marks_registered_query_bindings_mcp_available(self):
        self._copy_active_query_bindings()
        params = StdioServerParameters(command=sys.executable,
            args=[str(SERVER), '--project-root', str(self.root)])
        async with Client(params, cache=None) as client:
            registered = {tool.name: tool for tool in (await client.list_tools()).tools}
            self.assertTrue(set(QUERY_ROUTE_NAMES) <= set(registered))
            self.assertTrue(all(registered[name].annotations.read_only_hint for name in QUERY_ROUTE_NAMES))
            discovered = await client.call_tool('discover_tools', {'request': {
                'query': 'find_and_fetch', 'availability': 'mcp'}})
            self.assertFalse(discovered.is_error, str(discovered))
            matches = discovered.structured_content['matches']
            self.assertEqual(set(QUERY_ROUTE_NAMES), {row['mcp_name'] for row in matches})
            self.assertTrue(all(row['availability'] == 'mcp' for row in matches))

    async def test_stdio_gather_check_fix_report(self):
        params = StdioServerParameters(command=sys.executable,
            args=[str(SERVER), '--project-root', str(self.root)])
        async with Client(params) as client:
            tools = await client.list_tools()
            actual_tool_names = {tool.name for tool in tools.tools}
            self.assertEqual(D547_ADMITTED_SELECTED_ROUTES, SELECTED_ROUTE_NAMES)
            self.assertTrue(D548_REQUIRED_TOOLS <= actual_tool_names)
            self.assertTrue(set(D547_ADMITTED_SELECTED_ROUTES) <= actual_tool_names)
            self.assertTrue(D547_SELECTED_CONTROL_TOOLS <= actual_tool_names)
            self.assertTrue(next(tool for tool in tools.tools if tool.name == 'find_and_fetch_artifacts').annotations.read_only_hint)
            self.assertTrue(next(tool for tool in tools.tools if tool.name == 'find_and_fetch_journal_events').annotations.read_only_hint)
            self.assertEqual(
                D548_REQUIRED_TOOLS | set(SELECTED_ROUTE_NAMES) | D547_SELECTED_CONTROL_TOOLS,
                actual_tool_names,
            )
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
