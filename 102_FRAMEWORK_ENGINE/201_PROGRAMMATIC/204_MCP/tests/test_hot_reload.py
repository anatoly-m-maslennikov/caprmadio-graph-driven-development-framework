"""One real stdio connection across mock implementation generations."""
import asyncio
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from mcp import Client, StdioServerParameters

APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[2]
sys.path.insert(0, str(APP))
from hot_reload import Gateway, Generation, GENERATION_READY_TIMEOUT_SECONDS  # noqa: E402


class HotReload(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        directory = ROOT / '.caprmedio_tmp/tests/mcp-hot-reload'
        directory.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=directory, ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'mock.py'
        self.write('A')

    def write(self, version, name='echo'):
        self.source.write_text(
            'import asyncio\nfrom mcp.server import MCPServer\n'
            'server=MCPServer("mock")\n'
            f'@server.tool(name="{name}", structured_output=True)\n'
            'async def echo(delay: float = 0.0) -> dict[str, str]:\n'
            '    await asyncio.sleep(delay)\n'
            f'    return {{"version": "{version}"}}\n'
            'server.run(transport="stdio")\n')

    def params(self):
        code = ('import sys,asyncio;sys.path.insert(0,sys.argv[1]);'
                'from hot_reload import Gateway;'
                'asyncio.run(Gateway(sys.argv[2],sys.argv[3]).serve())')
        return StdioServerParameters(command=sys.executable,
            args=['-B', '-c', code, str(APP), str(self.root), str(self.source)])

    async def reload(self, client, request_id):
        return await client.call_tool('reload_mcp_implementation',
            {'request': {'operation': 'reload', 'request_id': request_id}})

    async def test_reload_rollback_duplicate_and_schema_change(self):
        async with Client(self.params(), cache=None) as client:
            self.assertEqual((await client.call_tool('echo')).structured_content['version'], 'A')
            self.write('B', 'echo_new')
            response = await self.reload(client, 'change')
            self.assertEqual(response.structured_content['outcome'], 'reloaded')
            self.assertTrue(response.structured_content['registry_changed'])
            self.assertEqual(response.structured_content['client_refresh_status'], 'unconfirmed')
            self.assertEqual({t.name for t in (await client.list_tools()).tools},
                             {'echo_new', 'reload_mcp_implementation', 'get_mcp_reload_status'})
            self.assertEqual((await client.call_tool('echo_new')).structured_content['version'], 'B')
            duplicate = await self.reload(client, 'change')
            self.assertEqual(response.structured_content, duplicate.structured_content)
            unchanged = await self.reload(client, 'same')
            self.assertEqual(unchanged.structured_content['outcome'], 'unchanged')
            self.source.write_text('syntax invalid !')
            failed = await self.reload(client, 'invalid')
            self.assertTrue(failed.is_error)
            self.assertEqual(failed.structured_content['outcome'], 'failed')
            self.assertEqual((await client.call_tool('echo_new')).structured_content['version'], 'B')

    async def test_in_flight_call_remains_on_old_generation(self):
        async with Client(self.params(), cache=None) as client:
            old_call = asyncio.create_task(client.call_tool('echo', {'delay': 2.0}))
            await asyncio.sleep(0.3)
            self.write('B')
            response = await self.reload(client, 'inflight')
            self.assertEqual(response.structured_content['outcome'], 'reloaded')
            self.assertEqual((await old_call).structured_content['version'], 'A')
            self.assertEqual((await client.call_tool('echo')).structured_content['version'], 'B')

    async def test_strict_control_rejects_paths_and_extra_fields(self):
        async with Client(self.params(), cache=None) as client:
            for request in ({'operation': 'reload', 'request_id': '../escape'},
                            {'operation': 'reload', 'request_id': 'safe', 'path': '/tmp'},
                            {'operation': 'reload'}):
                response = await client.call_tool('reload_mcp_implementation', {'request': request})
                self.assertTrue(response.is_error)
            self.assertEqual((await client.call_tool('echo')).structured_content['version'], 'A')

    async def test_invalid_registry_keeps_previous_generation(self):
        async with Client(self.params(), cache=None) as client:
            for index, schema in enumerate(("{'type':'invalid'}", "{'type':'object'}")):
                names = "['dup','dup']" if index else "['bad']"
                self.source.write_text(
                    'import asyncio\nfrom mcp import types\n'
                    'from mcp.server.lowlevel import Server\n'
                    'from mcp.server.stdio import stdio_server\n'
                    'async def tools(ctx,params):\n'
                    f'    return types.ListToolsResult(tools=[types.Tool(name=n,input_schema={schema}) for n in {names}])\n'
                    'async def main():\n'
                    '    server=Server("bad",on_list_tools=tools)\n'
                    '    async with stdio_server() as streams:\n'
                    '        await server.run(*streams,server.create_initialization_options())\n'
                    'asyncio.run(main())\n')
                response = await self.reload(client, f'bad-{index}')
                self.assertEqual(response.structured_content['outcome'], 'failed')
                self.assertEqual((await client.call_tool('echo')).structured_content['version'], 'A')

    async def test_concurrent_reload_is_serialized(self):
        async with Client(self.params(), cache=None) as client:
            self.write('B')
            first, second = await asyncio.gather(self.reload(client, 'parallel-1'),
                                                self.reload(client, 'parallel-2'))
            self.assertEqual({first.structured_content['outcome'], second.structured_content['outcome']},
                             {'reloaded', 'unchanged'})
            self.assertEqual((await client.call_tool('echo')).structured_content['version'], 'B')

    async def test_legacy_client_receives_registry_change_notification(self):
        async with Client(self.params(), cache=None, mode='legacy') as client:
            self.write('B', 'new_echo')
            response = await self.reload(client, 'legacy-change')
            self.assertEqual(response.structured_content['notification_status'], 'sent')
            self.assertEqual({t.name for t in (await client.list_tools()).tools},
                             {'new_echo', 'reload_mcp_implementation', 'get_mcp_reload_status'})

    async def test_status_is_read_only_and_reload_is_separate(self):
        async with Client(self.params(), cache=None) as client:
            tools = {t.name: t for t in (await client.list_tools()).tools}
            self.assertTrue(tools['get_mcp_reload_status'].annotations.read_only_hint)
            self.assertFalse(tools['reload_mcp_implementation'].annotations.read_only_hint)
            self.assertFalse(tools['reload_mcp_implementation'].annotations.destructive_hint)
            status = await client.call_tool('get_mcp_reload_status', {'request': {}})
            self.assertFalse(status.is_error)
            self.assertIsNotNone(status.structured_content['active_generation'])
            self.assertFalse((self.root / '.caprmedio_install/mcp_hot_reload').exists())
            invalid = await client.call_tool('reload_mcp_implementation',
                                            {'request': {'operation': 'status'}})
            self.assertTrue(invalid.is_error)
            invalid = await client.call_tool('get_mcp_reload_status',
                                            {'request': {'operation': 'reload'}})
            self.assertTrue(invalid.is_error)
            self.assertFalse((self.root / '.caprmedio_install/mcp_hot_reload').exists())

    async def test_cold_generation_bootstraps_before_the_legacy_deadline(self):
        """The gateway must not spend the child startup budget on auto-discovery."""
        self.source.write_text(
            'import time\n'
            'time.sleep(11)\n'
            'from mcp.server import MCPServer\n'
            'server=MCPServer("slow")\n'
            '@server.tool(name="echo", structured_output=True)\n'
            'def echo() -> dict[str,str]:\n'
            '    return {"version":"slow"}\n'
            'server.run(transport="stdio")\n')
        async with Client(self.params(), cache=None, mode='legacy',
                          read_timeout_seconds=GENERATION_READY_TIMEOUT_SECONDS) as client:
            self.assertEqual((await client.call_tool('echo')).structured_content['version'], 'slow')

    async def test_generation_uses_the_bounded_legacy_bootstrap(self):
        observed = {}

        class BootstrapClient:
            def __init__(self, params, **kwargs):
                observed['params'] = params
                observed.update(kwargs)

            async def __aenter__(self):
                return self

            async def __aexit__(self, exc_type, exc_value, traceback):
                return None

            async def list_tools(self, cursor=None):
                return SimpleNamespace(tools=[], next_cursor=None)

        with patch('hot_reload.Client', BootstrapClient):
            generation = Generation(params='local-child', fingerprint='test')
            await generation.ready
            generation.stop.set()
            await generation.task

        self.assertEqual(observed, {
            'params': 'local-child', 'cache': None, 'mode': 'legacy',
            'read_timeout_seconds': GENERATION_READY_TIMEOUT_SECONDS,
        })

    async def test_generation_retains_only_explicit_runtime_namespace(self):
        self.source.write_text(
            'import os\nfrom mcp.server import MCPServer\n'
            'server=MCPServer("namespace")\n'
            '@server.tool(name="namespace", structured_output=True)\n'
            'def namespace() -> dict[str,str]:\n'
            '    return {"namespace":os.environ.get("CAPRMEDIO_RUNTIME_NAMESPACE",""),'
            '"secret":os.environ.get("CAPRMEDIO_TEST_SECRET","absent")}\n'
            'server.run(transport="stdio")\n')
        parameters = self.params().model_copy(update={'env': {
            'CAPRMEDIO_RUNTIME_NAMESPACE': 'docker', 'CAPRMEDIO_TEST_SECRET': 'do-not-forward'}})
        async with Client(parameters, cache=None) as client:
            result = (await client.call_tool('namespace')).structured_content
            self.assertEqual(result, {'namespace': 'docker', 'secret': 'absent'})

    async def test_child_failure_is_uncertain_and_not_replayed(self):
        self.source.write_text(
            'import os\nfrom mcp.server import MCPServer\n'
            'server=MCPServer("crash")\n'
            '@server.tool(name="crash", structured_output=True)\n'
            'def crash() -> dict[str,str]:\n'
            f'    open({str(self.root / "calls")!r},"a").write("called\\n")\n'
            '    os._exit(1)\n'
            'server.run(transport="stdio")\n')
        async with Client(self.params(), cache=None) as client:
            response = await client.call_tool('crash')
            self.assertTrue(response.is_error)
            self.assertEqual(response.structured_content['outcome'], 'uncertain')
            self.assertEqual((self.root / 'calls').read_text(), 'called\n')

    async def test_aggregate_shutdown_cancels_a_generation_after_its_five_second_drain(self):
        generation = Generation.__new__(Generation)
        generation.stop = asyncio.Event()
        generation.task = asyncio.create_task(asyncio.sleep(60))
        gateway = Gateway(self.root, self.source)
        gateway.generations = [generation]
        started = asyncio.get_running_loop().time()
        await gateway.close()
        self.assertLess(asyncio.get_running_loop().time() - started, 6)
        self.assertTrue(generation.task.done())
