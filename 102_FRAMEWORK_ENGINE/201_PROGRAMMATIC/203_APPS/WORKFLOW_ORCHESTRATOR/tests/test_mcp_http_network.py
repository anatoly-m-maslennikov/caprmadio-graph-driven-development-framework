"""The opt-in HTTP ingress must not widen worker or Agent networking."""

from pathlib import Path
import unittest

import yaml


DOCKER = Path(__file__).resolve().parents[1] / "docker"


class MCPHTTPNetworkTests(unittest.TestCase):
    def setUp(self):
        self.base = yaml.safe_load((DOCKER / "compose.yaml").read_text())
        self.http = yaml.safe_load((DOCKER / "mcp-http.compose.yaml").read_text())

    def test_http_has_a_dedicated_publication_bridge(self):
        network = self.http["networks"]["http_publication"]
        self.assertEqual("bridge", network["driver"])
        self.assertIs(False, network["internal"])
        self.assertEqual(["runtime", "http_publication"],
                         self.http["services"]["mcp-http"]["networks"])

    def test_internal_worker_agent_and_stdio_networks_are_unchanged(self):
        self.assertIs(True, self.base["networks"]["runtime"]["internal"])
        self.assertEqual({"mcp-http"}, set(self.http["services"]))
        for name in ("worker", "agent", "mcp"):
            with self.subTest(service=name):
                self.assertEqual(["runtime"], self.base["services"][name]["networks"])
                self.assertNotIn("ports", self.base["services"][name])

    def test_http_keeps_exact_loopback_and_container_boundaries(self):
        service = self.http["services"]["mcp-http"]
        self.assertEqual(
            ["127.0.0.1:${CAPRMEDIO_MCP_HTTP_PORT:?Set an explicit HTTP MCP port}:8092"],
            service["ports"],
        )
        self.assertTrue(service["read_only"])
        self.assertEqual(["ALL"], service["cap_drop"])
        self.assertIn("no-new-privileges:true", service["security_opt"])
        self.assertNotIn("network_mode", service)
        self.assertEqual({"/project", "/project/.git"},
                         {mount["target"] for mount in service["volumes"]})


if __name__ == "__main__":
    unittest.main()
