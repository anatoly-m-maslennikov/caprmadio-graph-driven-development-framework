---
atom_id: CA-M-342
content_role: Method
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 17:12:15 +0000"
subjects:
  governs: "MCP/HTTP endpoint/Access implementation"
  depends_on: [MCP, HTTP, Credential, Request, Operator, Permission, Session]
relations:
  method_for: [CA-R-1885]
---
# Summary

authenticate and bound HTTP MCP Requests

## Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

## Claim

the HTTP access implementation **must** validate the bearer Token and loopback Host/Origin boundary before the existing MCP handlers receive a Request.

## Details

1. use a narrow ASGI bearer guard with constant-time comparison for every HTTP Request, including Session continuations. Forward lifespan unchanged.
2. enable the MCP SDK's DNS-rebinding protection explicitly; a container bind address of `0.0.0.0` does not disable Host/Origin validation.
3. a fixed local Token does not require an OAuth issuer. Obtain its value from the admitted runtime environment and expose no secret in failures.
4. health checks use the same authenticated endpoint and report readiness without running a Workflow or printing a Token.
