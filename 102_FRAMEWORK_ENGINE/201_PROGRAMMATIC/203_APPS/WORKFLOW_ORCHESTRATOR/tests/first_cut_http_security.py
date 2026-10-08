"""Narrow authenticated-HTTP security probe for the first Docker cut.

The caller owns endpoint lifecycle and the ephemeral bearer token.  This
module neither persists nor renders that token, and it has no Docker, MCP, or
Journal side effects of its own.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener


REQUIRED_RETAINED_ROUTE_TOOLS = frozenset({
    "create_atom",
    "update_atom",
    "replace_atom",
    "change_atom_status",
    "run_implementation_workflow",
    "build_applicable_methodology",
})
REQUIRED_TOOLS = REQUIRED_RETAINED_ROUTE_TOOLS | {"workflow_orchestrator"}


class FirstCutHttpSecurityError(RuntimeError):
    """The bounded HTTP transport contract was not observed."""


HealthRequest = Callable[[str, Mapping[str, str]], int]
McpRequest = Callable[[str, Mapping[str, str], Mapping[str, object]], int]
McpToolList = Callable[[str, str], Iterable[str]]
RecordingBoundary = Callable[[], object]


class _RejectRedirects(HTTPRedirectHandler):
    """Treat redirects as probe failures rather than following untrusted URLs."""

    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def _health_url(mcp_url: str) -> str:
    if not isinstance(mcp_url, str):
        raise FirstCutHttpSecurityError("HTTP MCP URL is invalid")
    try:
        parsed = urlsplit(mcp_url)
        valid = (
            parsed.scheme == "http"
            and parsed.hostname == "127.0.0.1"
            and parsed.port is not None
            and 1 <= parsed.port <= 65535
            and parsed.path == "/mcp"
            and not parsed.query
            and not parsed.fragment
            and parsed.username is None
            and parsed.password is None
        )
    except ValueError:
        valid = False
    if not valid:
        raise FirstCutHttpSecurityError("HTTP MCP URL must be explicit loopback http://127.0.0.1:<port>/mcp")
    return f"http://127.0.0.1:{parsed.port}/health"


def _urllib_status(
    url: str,
    headers: Mapping[str, str],
    *,
    method: str = "GET",
    data: bytes | None = None,
) -> int:
    request = Request(url, headers=dict(headers), method=method, data=data)
    try:
        opener = build_opener(ProxyHandler({}), _RejectRedirects())
        with opener.open(request, timeout=10) as response:  # nosec B310: caller supplies local Docker URL
            return int(response.status)
    except HTTPError as error:
        try:
            return int(error.code)
        finally:
            error.close()
    except URLError as error:
        raise FirstCutHttpSecurityError("HTTP security probe could not reach the endpoint") from error


def _mcp_status(url: str, headers: Mapping[str, str], payload: Mapping[str, object]) -> int:
    """Send one rejected MCP operation without following a proxy or redirect."""
    request_headers = {
        "Accept": "application/json, text/event-stream",
        "Content-Type": "application/json",
        **headers,
    }
    return _urllib_status(
        url,
        request_headers,
        method="POST",
        data=json.dumps(payload, separators=(",", ":")).encode("utf-8"),
    )


def assert_stale_token_rejected(
    mcp_url: str,
    stale_token: str,
    session_id: str,
    *,
    health_request: HealthRequest = _urllib_status,
    mcp_request: McpRequest = _mcp_status,
) -> None:
    """Prove a restarted service rejects a prior session's former bearer token."""
    if not isinstance(stale_token, str) or not stale_token:
        raise FirstCutHttpSecurityError("stale HTTP bearer token is unavailable")
    if not isinstance(session_id, str) or not session_id:
        raise FirstCutHttpSecurityError("prior HTTP session identifier is unavailable")
    if not callable(health_request) or not callable(mcp_request):
        raise FirstCutHttpSecurityError("HTTP stale-token probe callbacks are unavailable")
    health_url = _health_url(mcp_url)
    stale_headers = {"Authorization": f"Bearer {stale_token}"}
    if health_request(health_url, stale_headers) != 401:
        raise FirstCutHttpSecurityError("previous HTTP bearer token remained valid after restart")
    continuation_headers = {**stale_headers, "Mcp-Session-Id": session_id}
    payload = {
        "jsonrpc": "2.0",
        "id": "stale-token-continuation",
        "method": "tools/call",
        "params": {"name": "reload_mcp_implementation", "arguments": {}},
    }
    if mcp_request(mcp_url, continuation_headers, payload) != 401:
        raise FirstCutHttpSecurityError("previous HTTP session continuation remained valid after restart")


def probe_first_cut_http_security(
    mcp_url: str,
    token: str,
    *,
    list_tools: McpToolList,
    health_request: HealthRequest = _urllib_status,
    mcp_request: McpRequest = _mcp_status,
    continuation_session_id: str | None = None,
    recording_boundary: RecordingBoundary | None = None,
) -> dict[str, object]:
    """Probe denial ordering, localhost origin policy, health, and MCP tools.

    ``recording_boundary`` is sampled around denied requests only, allowing the
    caller to prove that rejected transport probes did not change its shared
    recording state.  Neither the returned evidence nor raised errors include
    the bearer token.
    """
    if not isinstance(token, str) or not token:
        raise FirstCutHttpSecurityError("HTTP bearer token is unavailable")
    if not callable(list_tools) or not callable(health_request) or not callable(mcp_request):
        raise FirstCutHttpSecurityError("HTTP probe callbacks are unavailable")
    if continuation_session_id is not None and (
        not isinstance(continuation_session_id, str) or not continuation_session_id
    ):
        raise FirstCutHttpSecurityError("HTTP continuation session identifier is invalid")
    health_url = _health_url(mcp_url)
    before = recording_boundary() if recording_boundary is not None else None
    denied = (
        ({}, 401),
        ({"Authorization": "Bearer invalid"}, 401),
        ({"Authorization": f"Bearer {token}", "Host": "attacker.invalid"}, 421),
        ({"Authorization": f"Bearer {token}", "Origin": "https://attacker.invalid"}, 403),
    )
    observed_denied: list[int] = []
    for headers, expected in denied:
        observed = health_request(health_url, headers)
        observed_denied.append(observed)
        if observed != expected:
            raise FirstCutHttpSecurityError("HTTP denial policy did not return the expected status")
    if recording_boundary is not None and recording_boundary() != before:
        raise FirstCutHttpSecurityError("denied HTTP probes changed the recording boundary")

    mcp_denied = (
        ({}, {"name": "create_atom", "arguments": {}}, 401),
        ({"Authorization": "Bearer invalid"}, {"name": "reload_mcp_implementation", "arguments": {}}, 401),
        ({"Authorization": f"Bearer {token}", "Host": "attacker.invalid"},
         {"name": "create_atom", "arguments": {}}, 421),
        ({"Authorization": f"Bearer {token}", "Origin": "https://attacker.invalid"},
         {"name": "reload_mcp_implementation", "arguments": {}}, 403),
    )
    if continuation_session_id is not None:
        mcp_denied += ((
            {"Authorization": "Bearer invalid", "Mcp-Session-Id": continuation_session_id},
            {"name": "reload_mcp_implementation", "arguments": {}},
            401,
        ),)
    observed_mcp_denied: list[int] = []
    for index, (headers, arguments, expected) in enumerate(mcp_denied, start=1):
        payload = {
            "jsonrpc": "2.0",
            "id": f"denied-mcp-{index}",
            "method": "tools/call",
            "params": arguments,
        }
        observed = mcp_request(mcp_url, headers, payload)
        observed_mcp_denied.append(observed)
        if observed != expected:
            raise FirstCutHttpSecurityError("HTTP MCP denial policy did not return the expected status")
    if recording_boundary is not None and recording_boundary() != before:
        raise FirstCutHttpSecurityError("denied HTTP MCP probes changed the recording boundary")

    health_status = health_request(health_url, {"Authorization": f"Bearer {token}"})
    if health_status != 200:
        raise FirstCutHttpSecurityError("authenticated health probe did not return 200")
    names = frozenset(str(name) for name in list_tools(mcp_url, token))
    missing = REQUIRED_TOOLS - names
    if missing:
        raise FirstCutHttpSecurityError("authenticated MCP tool list is incomplete")
    return {
        "denied_statuses": tuple(observed_denied),
        "mcp_denied_statuses": tuple(observed_mcp_denied),
        "health_status": health_status,
        "tool_names": tuple(sorted(names)),
    }


__all__ = [
    "FirstCutHttpSecurityError",
    "REQUIRED_RETAINED_ROUTE_TOOLS",
    "REQUIRED_TOOLS",
    "assert_stale_token_rejected",
    "probe_first_cut_http_security",
]
