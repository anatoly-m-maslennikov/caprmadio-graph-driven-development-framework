"""Synthetic contract tests for the first-cut authenticated HTTP probe."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import ProxyHandler


TEST_ROOT = Path(__file__).resolve().parent
if str(TEST_ROOT) not in sys.path:
    sys.path.insert(0, str(TEST_ROOT))

from first_cut_http_security import (
    FirstCutHttpSecurityError,
    REQUIRED_TOOLS,
    _RejectRedirects,
    _urllib_status,
    assert_stale_token_rejected,
    probe_first_cut_http_security,
)


class FirstCutHttpSecurityTests(unittest.TestCase):
    url = "http://127.0.0.1:18092/mcp"
    token = "fixture-ephemeral-token"

    def _health(self, calls):
        def request(url, headers):
            calls.append((url, dict(headers)))
            authorization = headers.get("Authorization")
            if authorization != f"Bearer {self.token}":
                return 401
            if headers.get("Host") == "attacker.invalid":
                return 421
            if headers.get("Origin") == "https://attacker.invalid":
                return 403
            return 200
        return request

    def _mcp(self, calls):
        def request(url, headers, payload):
            calls.append((url, dict(headers), dict(payload)))
            authorization = headers.get("Authorization")
            if authorization != f"Bearer {self.token}":
                return 401
            if headers.get("Host") == "attacker.invalid":
                return 421
            if headers.get("Origin") == "https://attacker.invalid":
                return 403
            return 200
        return request

    def test_denial_order_absent_origin_health_and_required_mcp_tools(self):
        calls: list[tuple[str, dict[str, str]]] = []
        mcp_calls = []
        boundary = ["unchanged"]
        result = probe_first_cut_http_security(
            self.url,
            self.token,
            health_request=self._health(calls),
            mcp_request=self._mcp(mcp_calls),
            list_tools=lambda _url, _token: REQUIRED_TOOLS | {"rmed_atoms_base_revise"},
            continuation_session_id="prior-session",
            recording_boundary=lambda: tuple(boundary),
        )
        self.assertEqual((401, 401, 421, 403), result["denied_statuses"])
        self.assertEqual((401, 401, 421, 403, 401), result["mcp_denied_statuses"])
        self.assertEqual(200, result["health_status"])
        self.assertTrue(REQUIRED_TOOLS <= set(result["tool_names"]))
        self.assertEqual(f"{self.url[:-4]}/health", calls[-1][0])
        self.assertEqual({"Authorization": f"Bearer {self.token}"}, calls[-1][1])
        self.assertEqual(self.url, mcp_calls[0][0])
        self.assertEqual("create_atom", mcp_calls[0][2]["params"]["name"])
        self.assertEqual("reload_mcp_implementation", mcp_calls[1][2]["params"]["name"])
        self.assertEqual("prior-session", mcp_calls[-1][1]["Mcp-Session-Id"])

    def test_stale_token_and_prior_session_continuation_are_rejected_without_disclosure(self):
        stale = "old-ephemeral-token"
        calls = []

        def health(_url, headers):
            calls.append(("health", dict(headers)))
            return 401 if headers.get("Authorization") == f"Bearer {stale}" else 200

        def mcp(_url, headers, payload):
            calls.append(("mcp", dict(headers), dict(payload)))
            return 401 if headers.get("Authorization") == f"Bearer {stale}" else 200

        assert_stale_token_rejected(
            self.url,
            stale,
            "prior-session",
            health_request=health,
            mcp_request=mcp,
        )
        self.assertEqual("prior-session", calls[-1][1]["Mcp-Session-Id"])
        self.assertEqual("reload_mcp_implementation", calls[-1][2]["params"]["name"])

        with self.assertRaises(FirstCutHttpSecurityError) as raised:
            assert_stale_token_rejected(self.url, stale, "", health_request=health, mcp_request=mcp)
        self.assertNotIn(stale, str(raised.exception))

    def test_denied_probes_must_not_change_shared_recording_boundary(self):
        calls: list[tuple[str, dict[str, str]]] = []
        observed = [0]

        def boundary():
            observed[0] += 1
            return observed[0]

        with self.assertRaises(FirstCutHttpSecurityError) as raised:
            probe_first_cut_http_security(
                self.url,
                self.token,
                health_request=self._health(calls),
                list_tools=lambda _url, _token: REQUIRED_TOOLS,
                recording_boundary=boundary,
            )
        self.assertNotIn(self.token, str(raised.exception))
        self.assertEqual(4, len(calls))

    def test_incomplete_mcp_list_and_invalid_url_refuse_without_token_disclosure(self):
        with self.assertRaises(FirstCutHttpSecurityError) as incomplete:
            probe_first_cut_http_security(
                self.url,
                self.token,
                health_request=self._health([]),
                list_tools=lambda _url, _token: {"workflow_orchestrator"},
            )
        self.assertNotIn(self.token, str(incomplete.exception))
        with self.assertRaises(FirstCutHttpSecurityError) as invalid_url:
            probe_first_cut_http_security(
                "http://127.0.0.1:18092/not-mcp",
                self.token,
                health_request=self._health([]),
                list_tools=lambda _url, _token: REQUIRED_TOOLS,
            )
        self.assertNotIn(self.token, str(invalid_url.exception))

    def test_omitted_retained_route_and_nonloopback_url_refuse_before_callbacks(self):
        omitted = REQUIRED_TOOLS - {"replace_atom"}
        with self.assertRaises(FirstCutHttpSecurityError) as incomplete:
            probe_first_cut_http_security(
                self.url,
                self.token,
                health_request=self._health([]),
                list_tools=lambda _url, _token: omitted,
            )
        self.assertNotIn(self.token, str(incomplete.exception))

        def must_not_run(*_args, **_kwargs):
            raise AssertionError("nonloopback URL reached a probe callback")

        with self.assertRaises(FirstCutHttpSecurityError) as remote:
            probe_first_cut_http_security(
                "http://attacker.invalid:18092/mcp",
                self.token,
                health_request=must_not_run,
                list_tools=must_not_run,
            )
        self.assertNotIn(self.token, str(remote.exception))

    def test_authenticated_health_request_disables_proxies_and_rejects_redirects(self):
        source_requests: list[tuple[str, dict[str, str]]] = []
        remote_requests: list[str] = []

        class RedirectingOpener:
            def __init__(self, *handlers):
                self._redirect_handler = next(
                    handler for handler in handlers if isinstance(handler, _RejectRedirects)
                )

            def open(self, request, timeout):
                source_requests.append((request.full_url, dict(request.header_items())))
                redirected = self._redirect_handler.redirect_request(
                    request,
                    fp=None,
                    code=302,
                    msg="Found",
                    headers={},
                    newurl="http://attacker.invalid/redirect-target",
                )
                if redirected is not None:
                    remote_requests.append(redirected.full_url)
                raise HTTPError(request.full_url, 302, "Found", {}, None)

        with patch("first_cut_http_security.build_opener") as build_opener:
            build_opener.side_effect = RedirectingOpener
            status = _urllib_status(
                "http://127.0.0.1:18092/health",
                {"Authorization": f"Bearer {self.token}"},
            )

        self.assertEqual(302, status)
        proxy_handler, redirect_handler = build_opener.call_args.args
        self.assertIsInstance(proxy_handler, ProxyHandler)
        self.assertEqual({}, proxy_handler.proxies)
        self.assertIsInstance(redirect_handler, _RejectRedirects)
        self.assertEqual(
            [("http://127.0.0.1:18092/health", {"Authorization": f"Bearer {self.token}"})],
            source_requests,
        )
        self.assertEqual([], remote_requests)
        self.assertIsNone(_RejectRedirects().redirect_request(None, None, 302, "Found", {}, "http://attacker.invalid/"))


if __name__ == "__main__":
    unittest.main()
