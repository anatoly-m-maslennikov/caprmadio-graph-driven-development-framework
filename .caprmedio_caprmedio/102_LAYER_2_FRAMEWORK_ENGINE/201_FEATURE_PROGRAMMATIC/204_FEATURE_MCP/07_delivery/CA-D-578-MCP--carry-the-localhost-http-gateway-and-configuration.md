---
atom_id: CA-D-578
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 17:12:15 +0000"
subjects:
  governs: "MCP/HTTP endpoint/Carrier"
  depends_on: [MCP, HTTP, Gateway, Implementation, Credential, Request, Session, Docker Runtime]
relations:
  delivery_for: [CA-R-1884, CA-R-1885, CA-M-341, CA-M-342]
---
# Summary

carry the localhost HTTP Gateway and configuration

## Scope

the HTTP server, opt-in Docker service, configuration and connection carriers.

## Claim

the additional HTTP endpoint **must** be carried by the existing MCP Gateway entrypoint and an opt-in Docker service, with explicit public-port and runtime-secret configuration.

## Details

1. deliver HTTP support beside `hot_reload.py` under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/`; `server.py --transport stdio` remains the default. The additional transport is `streamable-http`, with path `/mcp` and container port `8092`.
2. keep the existing `mcp` Compose service unchanged; add `mcp-http` with the same restricted image and Project mounts, no Docker socket, and a dedicated authenticated health check.
3. the opt-in `docker/mcp-http.compose.yaml` overlay publishes `127.0.0.1:${CAPRMEDIO_MCP_HTTP_PORT}:8092`. Require an explicitly selected integer host port in `1..65535`; there is no new implicit public-port default. Loading this overlay is explicit and does not change normal worker/stdio startup.
4. supply the Token through `CAPRMEDIO_MCP_HTTP_SECRET_TOKEN` at runtime. Store persistent secrets in an Operator-managed gitignored `.env` file or Vault, never in RMED, images or committed configuration. The runtime does not guess or read such a file; explicit environment injection is required. Restart the HTTP service explicitly after Token rotation.
5. support explicit `mcp-http-start`, `mcp-http-stop` and `mcp-http-status` lifecycle operations in the existing Docker runtime adapter. Return the safe connection URL `http://127.0.0.1:<port>/mcp`, readiness and service state, never the Token. HTTP startup does not require or implicitly start the Codex Agent service.
6. authentication uses the standard `Authorization: Bearer <token>` header for every HTTP request. Permit loopback Host values and loopback HTTP Origins; no Origin is required for non-browser clients. Rejections expose no credential value.
7. test delivery belongs in `204_MCP/tests/test_hot_reload_http.py` and a Docker HTTP configuration/lifecycle test module. Existing stdio tests are retained. Docker absence or denial remains a failed/incomplete real-container gate, not a successful fixture result.
