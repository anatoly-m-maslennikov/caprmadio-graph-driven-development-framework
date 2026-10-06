"""Ordinary MCP transport checks, intentionally outside sealed Docker E2E discovery."""
from __future__ import annotations

import sys
import unittest

from mcp import types

from test_selected_workflows_docker_e2e import _stdio_tool_call, _structured_tool_result


class SelectedDockerHarnessTransportTests(unittest.IsolatedAsyncioTestCase):
    async def test_actual_declared_stdio_client_reconnects_and_unwraps_structured_output(self) -> None:
        from mcp import StdioServerParameters
        server = (
            "from mcp.server import MCPServer\nfrom typing import Any\nfrom uuid import uuid4\n"
            "connection_id = str(uuid4())\nserver = MCPServer('selected-harness-transport-check')\n"
            "@server.tool(name='readonly_echo', structured_output=True)\n"
            "def echo(request: dict[str, Any]) -> dict[str, Any]: return {'request': request, 'connection_id': connection_id}\n"
            "server.run(transport='stdio')\n"
        )
        parameters = StdioServerParameters(command=sys.executable, args=["-B", "-c", server])
        first = await _stdio_tool_call(parameters, "readonly_echo", {"sequence": 1})
        second = await _stdio_tool_call(parameters, "readonly_echo", {"sequence": 2})
        self.assertEqual({"sequence": 1}, first["request"])
        self.assertEqual({"sequence": 2}, second["request"])
        self.assertNotEqual(first["connection_id"], second["connection_id"])

    async def test_result_unwrap_never_counts_tool_error_or_text_marker_as_success(self) -> None:
        successful = types.CallToolResult(content=[], structured_content={"actual": "structured"})
        self.assertEqual({"actual": "structured"}, _structured_tool_result(successful))
        for response in (types.CallToolResult(content=[], structured_content={"actual": "structured"}, is_error=True),
                         types.CallToolResult(content=[types.TextContent(type="text", text='{"actual":"marker"}')])):
            with self.assertRaises(AssertionError):
                _structured_tool_result(response)
