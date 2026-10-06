"""HTTP MCP compose/lifecycle boundary tests; no Docker daemon is invoked."""
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP / "docker"))
from runtime import Runtime  # noqa: E402


class MCPHTTPRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = APP.parents[3] / ".caprmedio_tmp/tests/mcp-http-runtime"
        self.temporary.mkdir(parents=True, exist_ok=True)

    def root(self):
        directory = tempfile.TemporaryDirectory(dir=self.temporary, ignore_cleanup_errors=True)
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        (root / ".caprmedio_caprmedio").mkdir()
        (root / ".git").mkdir()
        return root

    def test_explicit_port_and_token_are_required_without_agent_auth(self):
        runtime = Runtime(self.root())
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "CAPRMEDIO_MCP_HTTP_PORT"):
                runtime.mcp_http_start()
        with patch.dict(os.environ, {"CAPRMEDIO_MCP_HTTP_PORT": "8099",
                                     "CAPRMEDIO_MCP_HTTP_SECRET_TOKEN": "token"}, clear=True):
            with patch.object(runtime, "call", return_value="") as call:
                result = runtime.mcp_http_start()
        self.assertEqual("http://127.0.0.1:8099/mcp", result["url"])
        self.assertIn("mcp-http", call.call_args.args)
        self.assertTrue(call.call_args.kwargs["http"])

    def test_overlay_is_loopback_only_and_has_no_agent_or_socket(self):
        text = (APP / "docker/mcp-http.compose.yaml").read_text()
        self.assertIn("127.0.0.1:${CAPRMEDIO_MCP_HTTP_PORT", text)
        self.assertIn("CAPRMEDIO_MCP_HTTP_SECRET_TOKEN", text)
        self.assertNotIn("/var/run/docker.sock", text)
        self.assertNotIn("agent_auth", text)
        self.assertIn("no-new-privileges:true", text)


if __name__ == "__main__":
    unittest.main()
