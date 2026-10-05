---
atom_id: CA-M-341
content_role: Method
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 17:12:15 +0000"
subjects:
  governs: "MCP/HTTP endpoint/Gateway implementation"
  depends_on: [MCP, HTTP, Gateway, Tool, Generation, Session, Implementation]
relations:
  method_for: [CA-R-1884]
---
# Summary

reuse the hot-reload Gateway for HTTP

## Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

## Claim

the HTTP transport implementation **must** reuse the Gateway's existing server handlers and generation lifecycle, so transport selection does not independently redefine Tool behavior.

## Details

1. factor one server-construction boundary for stdio and HTTP; keep implementation generations on their existing subprocess stdio connection.
2. use the installed MCP SDK's Streamable HTTP ASGI application and forward its lifespan; preserve stateful Sessions and the existing reload notifications.
3. close HTTP Sessions and all Gateway generations on shutdown. Do not replay interrupted Tool calls during reload or shutdown.
