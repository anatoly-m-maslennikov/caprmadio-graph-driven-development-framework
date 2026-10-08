"""One-shot, non-authenticated TCP diagnostics for the first-cut HTTP proof."""

from __future__ import annotations

import re
import socket
from collections.abc import Mapping
from urllib.parse import urlsplit


_REDACTED = "[redacted]"
_SECRET_VALUE = re.compile(r"(?i)\b(?:bearer\s+|token\s*[=:]\s*|secret\s*[=:]\s*)\S+")
_STATUS_FIELDS = ("State", "Health", "Publishers")
_PUBLISHER_FIELDS = ("URL", "TargetPort", "PublishedPort", "Protocol")


def _advertised_loopback(url: str) -> tuple[str, int]:
    """Validate the sole admitted published endpoint before opening a socket."""
    if not isinstance(url, str):
        raise ValueError("HTTP MCP URL must be explicit loopback http://127.0.0.1:<port>/mcp")
    try:
        parsed = urlsplit(url)
        port = parsed.port
    except ValueError as error:
        raise ValueError("HTTP MCP URL must be explicit loopback http://127.0.0.1:<port>/mcp") from error
    if not (
        parsed.scheme == "http"
        and parsed.hostname == "127.0.0.1"
        and port is not None
        and 1 <= port <= 65535
        and parsed.path == "/mcp"
        and not parsed.query
        and not parsed.fragment
        and parsed.username is None
        and parsed.password is None
    ):
        raise ValueError("HTTP MCP URL must be explicit loopback http://127.0.0.1:<port>/mcp")
    return "127.0.0.1", port


def _safe_value(value: object) -> str | int | float | bool | None:
    """Keep diagnostics serializable without allowing bearer-like data through."""
    if not isinstance(value, (str, int, float, bool)) and value is not None:
        return None
    if isinstance(value, str):
        return _SECRET_VALUE.sub(_REDACTED, value)
    return value


def _safe_publishers(value: object) -> str | int | float | bool | list[dict[str, object]] | None:
    """Allow Compose's structured published-port rows without retaining extra data."""
    if not isinstance(value, list):
        return _safe_value(value)
    publishers = []
    for publisher in value:
        if not isinstance(publisher, Mapping):
            continue
        row = {}
        for field in _PUBLISHER_FIELDS:
            safe = _safe_value(publisher.get(field))
            if safe is not None:
                row[field] = safe
        publishers.append(row)
    return publishers


def safe_published_service_snapshot(snapshot: object) -> list[dict[str, object]]:
    """Return allowlisted status fields for the HTTP service only."""
    if not isinstance(snapshot, Mapping):
        return []
    services = snapshot.get("services")
    if not isinstance(services, list):
        return []
    result = []
    for service in services:
        if not isinstance(service, Mapping) or service.get("Service") != "mcp-http":
            continue
        row = {}
        for field in _STATUS_FIELDS:
            value = _safe_publishers(service.get(field)) if field == "Publishers" else _safe_value(service.get(field))
            if value is not None:
                row[field] = value
        result.append(row)
    return result


def connectivity_report(url: str, runtime_status: dict) -> dict[str, object]:
    """Attempt one direct TCP connect; this never authenticates or invokes MCP."""
    host, port = _advertised_loopback(url)
    result: dict[str, object] = {
        "host": host,
        "port": port,
        "published_services": safe_published_service_snapshot(runtime_status),
    }
    try:
        with socket.create_connection((host, port), timeout=2):
            result["tcp"] = "reachable"
    except OSError as error:
        result["tcp"] = "unreachable"
        result["exception_class"] = type(error).__name__
        result["errno"] = error.errno
    return result
