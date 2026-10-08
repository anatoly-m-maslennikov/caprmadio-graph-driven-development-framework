"""Focused unit tests for the first-cut TCP diagnostic."""

from __future__ import annotations

import errno
import json
import socket
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


TEST_ROOT = Path(__file__).resolve().parent
if str(TEST_ROOT) not in sys.path:
    sys.path.insert(0, str(TEST_ROOT))

from first_cut_http_connectivity import connectivity_report, safe_published_service_snapshot


class FirstCutHttpConnectivityTests(unittest.TestCase):
    url = "http://127.0.0.1:18092/mcp"

    @staticmethod
    def snapshot():
        return {
            "token": "must-not-appear",
            "services": [
                {"Service": "worker", "State": "running", "token": "must-not-appear"},
                {"Service": "mcp-http", "State": "running", "Health": "healthy",
                 "Publishers": "127.0.0.1:18092->8092/tcp", "token": "must-not-appear"},
            ],
        }

    def test_success_reports_only_advertised_address_and_safe_service_fields(self):
        socket_object = object()
        with patch("first_cut_http_connectivity.socket.create_connection") as connect:
            connect.return_value.__enter__.return_value = socket_object
            result = connectivity_report(self.url, self.snapshot())
        self.assertEqual(("127.0.0.1", 18092), connect.call_args.args[0])
        self.assertEqual(2, connect.call_args.kwargs["timeout"])
        self.assertEqual("reachable", result["tcp"])
        self.assertEqual(
            [{"State": "running", "Health": "healthy", "Publishers": "127.0.0.1:18092->8092/tcp"}],
            result["published_services"],
        )
        self.assertNotIn("must-not-appear", json.dumps(result))

    def test_connection_refused_reports_class_and_errno_without_error_text(self):
        with patch("first_cut_http_connectivity.socket.create_connection", side_effect=ConnectionRefusedError(errno.ECONNREFUSED, "do not report this")):
            result = connectivity_report(self.url, self.snapshot())
        self.assertEqual("unreachable", result["tcp"])
        self.assertEqual("ConnectionRefusedError", result["exception_class"])
        self.assertEqual(errno.ECONNREFUSED, result["errno"])
        self.assertNotIn("do not report this", json.dumps(result))

    def test_permission_denied_reports_class_and_errno_without_error_text(self):
        with patch("first_cut_http_connectivity.socket.create_connection", side_effect=PermissionError(errno.EPERM, "do not report this")):
            result = connectivity_report(self.url, self.snapshot())
        self.assertEqual("PermissionError", result["exception_class"])
        self.assertEqual(errno.EPERM, result["errno"])
        self.assertNotIn("do not report this", json.dumps(result))

    def test_unsafe_url_is_rejected_before_socket_connect(self):
        with patch("first_cut_http_connectivity.socket.create_connection") as connect:
            with self.assertRaisesRegex(ValueError, "explicit loopback"):
                connectivity_report("http://attacker.invalid:18092/mcp", self.snapshot())
        connect.assert_not_called()

    def test_bearer_like_service_values_are_redacted_and_structure_is_safe(self):
        snapshot = {
            "services": [
                {"Service": "mcp-http", "State": "Bearer sensitive-state", "Health": ["not", "serializable"],
                 "Publishers": "token=secret-publisher", "Other": "ignored"},
            ],
        }
        self.assertEqual(
            [{"State": "[redacted]", "Publishers": "[redacted]"}],
            safe_published_service_snapshot(snapshot),
        )

    def test_compose_publisher_rows_keep_only_safe_mapping_fields_and_integer_ports(self):
        snapshot = {
            "services": [
                {"Service": "mcp-http", "State": "running", "Publishers": [
                    {"URL": "127.0.0.1:18092->8092/tcp", "TargetPort": 8092,
                     "PublishedPort": 18092, "Protocol": "tcp", "secret": "must-not-appear"},
                ]},
            ],
        }
        result = safe_published_service_snapshot(snapshot)
        self.assertEqual(
            [{"State": "running", "Publishers": [
                {"URL": "127.0.0.1:18092->8092/tcp", "TargetPort": 8092,
                 "PublishedPort": 18092, "Protocol": "tcp"},
            ]}],
            result,
        )
        self.assertIsInstance(result[0]["Publishers"][0]["PublishedPort"], int)
        self.assertNotIn("must-not-appear", json.dumps(result))


if __name__ == "__main__":
    unittest.main()
