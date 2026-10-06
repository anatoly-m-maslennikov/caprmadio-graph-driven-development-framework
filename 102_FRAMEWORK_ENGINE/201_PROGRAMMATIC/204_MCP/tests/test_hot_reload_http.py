"""HTTP transport and access-boundary tests for the existing reload gateway."""
import asyncio
from pathlib import Path
import sys
import tempfile
import unittest

import httpx2
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client
from starlette.testclient import TestClient

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
from http_server import create_app  # noqa: E402


class HTTPGatewayTests(unittest.TestCase):
    def setUp(self):
        directory = APP.parents[2] / '.caprmedio_tmp/tests/mcp-http'
        directory.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=directory, ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'mock.py'
        self.source.write_text(
            'from mcp.server import MCPServer\nserver=MCPServer("mock")\n'
            '@server.tool()\ndef echo() -> dict: return {"value":"ok"}\n'
            'server.run(transport="stdio")\n')
        self.client = TestClient(create_app(self.root, token='token', implementation=self.source))
        self.client.__enter__()
        self.addCleanup(self.client.__exit__, None, None, None)

    def headers(self, token='token', **extra):
        return {'authorization': f'Bearer {token}', 'host': '127.0.0.1:8092', **extra}

    def test_rejects_missing_or_invalid_bearer_before_mcp(self):
        for headers in ({}, self.headers('wrong')):
            response = self.client.get('/health', headers=headers)
            self.assertEqual(401, response.status_code)
        self.assertEqual(200, self.client.get('/health', headers=self.headers()).status_code)
        self.client.app.gateway.active = None
        self.assertEqual(503, self.client.get('/health', headers=self.headers()).status_code)

    def test_hostile_host_is_rejected_before_initialize(self):
        response = self.client.post('/mcp', headers=self.headers(host='attacker.invalid'), json={})
        self.assertEqual(421, response.status_code)
        response = self.client.get('/health', headers=self.headers(origin='https://attacker.invalid'))
        self.assertEqual(403, response.status_code)

    def test_initialization_uses_the_existing_gateway(self):
        response = self.client.post('/mcp', headers={**self.headers(), 'accept': 'application/json, text/event-stream'},
            json={'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {
                'protocolVersion': '2025-11-25', 'capabilities': {}, 'clientInfo': {'name': 'test', 'version': '1'}}})
        self.assertEqual(200, response.status_code)
        self.assertIn('mcp-session-id', response.headers)


if __name__ == '__main__':
    unittest.main()


class HTTPProtocolTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        directory = APP.parents[2] / '.caprmedio_tmp/epic-resume-http'
        directory.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=directory, ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'mock.py'
        self.write('A', 'echo')
        self.app = create_app(self.root, token='token', implementation=self.source)

    def write(self, version, name):
        self.source.write_text(
            'import asyncio\nfrom mcp.server import MCPServer\nserver=MCPServer("mock")\n'
            f'@server.tool(name="{name}", structured_output=True)\n'
            'async def echo(delay: float = 0.0) -> dict[str, str]:\n'
            '    await asyncio.sleep(delay)\n'
            f'    return {{"version": "{version}"}}\n'
            'server.run(transport="stdio")\n')

    def write_environment(self):
        self.source.write_text(
            'import os\nfrom mcp.server import MCPServer\nserver=MCPServer("mock")\n'
            '@server.tool(name="environment", structured_output=True)\n'
            'def environment() -> dict[str, str]:\n'
            '    return {"token": os.environ.get("CAPRMEDIO_MCP_HTTP_SECRET_TOKEN", "absent")}\n'
            'server.run(transport="stdio")\n')

    async def session(self):
        client = httpx2.AsyncClient(
            transport=httpx2.ASGITransport(app=self.app),
            base_url='http://127.0.0.1:8092',
            headers={'Authorization': 'Bearer token'},
        )
        transport = streamable_http_client('http://127.0.0.1:8092/mcp', http_client=client)
        streams = await transport.__aenter__()
        session = ClientSession(*streams)
        await session.__aenter__()
        await session.initialize()
        return client, transport, session

    async def close_session(self, client, transport, session):
        await session.__aexit__(None, None, None)
        await transport.__aexit__(None, None, None)
        await client.aclose()

    async def test_sdk_tools_call_reload_and_inflight_generation(self):
        async with self.app.starlette_app.router.lifespan_context(self.app.starlette_app):
            client, transport, session = await self.session()
            try:
                self.assertEqual({'echo', 'reload_mcp_implementation', 'get_mcp_reload_status'},
                                 {tool.name for tool in (await session.list_tools()).tools})
                self.assertEqual('A', (await session.call_tool('echo')).structured_content['version'])
                old_call = asyncio.create_task(session.call_tool('echo', {'delay': 0.4}))
                await asyncio.sleep(0.05)
                self.write('B', 'echo_new')
                reload = await session.call_tool('reload_mcp_implementation',
                    {'request': {'operation': 'reload', 'request_id': 'http-reload'}})
                self.assertEqual('reloaded', reload.structured_content['outcome'])
                self.assertEqual('A', (await old_call).structured_content['version'])
                self.assertEqual('B', (await session.call_tool('echo_new')).structured_content['version'])
            finally:
                await self.close_session(client, transport, session)
        self.assertTrue(all(generation.task.done() for generation in self.app.gateway.generations))

    async def test_authenticated_session_continuation_and_rotation(self):
        async with self.app.starlette_app.router.lifespan_context(self.app.starlette_app):
            client, transport, session = await self.session()
            try:
                self.assertEqual('A', (await session.call_tool('echo')).structured_content['version'])
                bad = await client.post('/mcp', headers={'Authorization': 'Bearer changed',
                    'accept': 'application/json, text/event-stream', 'content-type': 'application/json'}, json={})
                self.assertEqual(401, bad.status_code)
            finally:
                await self.close_session(client, transport, session)

    async def test_http_token_is_not_forwarded_to_implementation(self):
        self.write_environment()
        async with self.app.starlette_app.router.lifespan_context(self.app.starlette_app):
            client, transport, session = await self.session()
            try:
                self.assertEqual('absent', (await session.call_tool('environment')).structured_content['token'])
            finally:
                await self.close_session(client, transport, session)
