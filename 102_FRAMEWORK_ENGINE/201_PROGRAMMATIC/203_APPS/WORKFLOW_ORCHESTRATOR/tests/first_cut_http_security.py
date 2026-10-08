"""Narrow authenticated-HTTP security probe for the first Docker cut.

The caller owns endpoint lifecycle and the ephemeral bearer token.  This
module neither persists nor renders that token, and it has no Docker, MCP, or
Journal side effects of its own.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
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


def _urllib_status(url: str, headers: Mapping[str, str]) -> int:
    request = Request(url, headers=dict(headers), method="GET")
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


def probe_first_cut_http_security(
    mcp_url: str,
    token: str,
    *,
    list_tools: McpToolList,
    health_request: HealthRequest = _urllib_status,
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
    if not callable(list_tools) or not callable(health_request):
        raise FirstCutHttpSecurityError("HTTP probe callbacks are unavailable")
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

    health_status = health_request(health_url, {"Authorization": f"Bearer {token}"})
    if health_status != 200:
        raise FirstCutHttpSecurityError("authenticated health probe did not return 200")
    names = frozenset(str(name) for name in list_tools(mcp_url, token))
    missing = REQUIRED_TOOLS - names
    if missing:
        raise FirstCutHttpSecurityError("authenticated MCP tool list is incomplete")
    return {
        "denied_statuses": tuple(observed_denied),
        "health_status": health_status,
        "tool_names": tuple(sorted(names)),
    }


__all__ = [
    "FirstCutHttpSecurityError",
    "REQUIRED_RETAINED_ROUTE_TOOLS",
    "REQUIRED_TOOLS",
    "probe_first_cut_http_security",
]
