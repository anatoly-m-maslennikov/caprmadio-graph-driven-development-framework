---
atom_id: CA-E-585
content_role: Evaluation
type: QA Case
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 17:12:15 +0000"
subjects:
  governs: "MCP/HTTP endpoint/Security evaluation"
  depends_on: [MCP, HTTP, Credential, Request, Operator, Permission, Tool, Session]
relations:
  evaluation_for: [CA-R-1885, CA-M-342]
---
# Summary

verify HTTP MCP access and secret boundaries

## Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

## Claim

the Evaluation **must** verify that HTTP access failures occur before MCP handling and preserve the existing permission and secret boundaries.

## Details

1. include good Requests and missing, wrong and changed Token cases, hostile Host/Origin cases, absent Origin, and authenticated Session continuations.
2. verify authentication rejection, SDK Host/Origin rejection and no Tool invocation or reload receipt on rejected Requests.
3. verify missing or invalid configuration prevents readiness; token rotation requires an explicit service restart and invalidates the previous Token.
4. check localhost-only Compose mapping, no Docker socket, no baked Token, no secret-bearing command arguments or logs, and unchanged stdio/default worker startup.
