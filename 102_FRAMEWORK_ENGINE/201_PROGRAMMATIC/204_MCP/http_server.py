"""Authenticated localhost-only Streamable HTTP transport for the MCP gateway."""
import argparse
import asyncio
from contextlib import asynccontextmanager
import hashlib
import hmac
import os
from pathlib import Path
import re

from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

from hot_reload import Gateway
from mcp.server.transport_security import TransportSecuritySettings

PATH = "/mcp"
PORT = 8092
TOKEN_ENV = "CAPRMEDIO_MCP_HTTP_SECRET_TOKEN"
SECURITY = TransportSecuritySettings(
    enable_dns_rebinding_protection=True,
    allowed_hosts=["127.0.0.1:*", "localhost:*", "[::1]:*"],
    allowed_origins=["http://127.0.0.1:*", "http://localhost:*", "http://[::1]:*"],
)


def _require_token(token):
    if not isinstance(token, str) or not token:
        raise ValueError("HTTP MCP token is not configured")
    return token


def token_from_environment():
    return _require_token(os.environ.get(TOKEN_ENV))


class BearerGuard:
    """Apply transport authentication before the MCP ASGI application."""
    def __init__(self, app, token):
        self.app = app
        self.token_digest = hashlib.sha256(_require_token(token).encode()).digest()

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        request = Request(scope, receive)
        authorization = request.headers.get("authorization", "")
        prefix = "Bearer "
        supplied = authorization[len(prefix):] if authorization.startswith(prefix) else ""
        supplied_digest = hashlib.sha256(supplied.encode()).digest()
        authenticated = hmac.compare_digest(supplied_digest, self.token_digest)
        if not authenticated:
            await Response(status_code=401, headers={"WWW-Authenticate": "Bearer"})(scope, receive, send)
            return
        host = request.headers.get("host", "")
        origin = request.headers.get("origin")
        valid_host = re.fullmatch(r"(?:127\.0\.0\.1|localhost|\[::1\])(?::\d+)?", host)
        valid_origin = origin is None or re.fullmatch(
            r"http://(?:127\.0\.0\.1|localhost|\[::1\])(?::\d+)?", origin)
        if not valid_host:
            await Response(status_code=421)(scope, receive, send)
            return
        if not valid_origin:
            await Response(status_code=403)(scope, receive, send)
            return
        await self.app(scope, receive, send)


async def health(request, gateway):
    generation = gateway.active
    if generation is None or generation.task.done():
        return JSONResponse({"ready": False}, status_code=503)
    return JSONResponse({"ready": True})


def create_app(root, token=None, implementation=None):
    token = token if token is not None else token_from_environment()
    token = _require_token(token)
    gateway = Gateway(root, implementation=implementation)
    server = gateway.build_server()
    async def readiness(request):
        return await health(request, gateway)

    app = server.streamable_http_app(
        streamable_http_path=PATH,
        transport_security=SECURITY,
        host="127.0.0.1",
        custom_starlette_routes=[Route("/health", readiness)],
    )
    inner_lifespan = app.router.lifespan_context

    @asynccontextmanager
    async def lifespan(application):
        async with inner_lifespan(application):
            await gateway.initialize()
            try:
                yield
            finally:
                await gateway.close()

    app.router.lifespan_context = lifespan
    guarded = BearerGuard(app, token)
    guarded.gateway = gateway
    guarded.starlette_app = app
    return guarded


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", default=PORT, type=int)
    args = parser.parse_args()
    if args.host != "0.0.0.0" or args.port != PORT:
        raise ValueError("HTTP MCP requires the container bind 0.0.0.0:8092")
    import uvicorn
    uvicorn.run(create_app(args.project_root), host=args.host, port=args.port, log_level="warning")


if __name__ == "__main__":
    main()
