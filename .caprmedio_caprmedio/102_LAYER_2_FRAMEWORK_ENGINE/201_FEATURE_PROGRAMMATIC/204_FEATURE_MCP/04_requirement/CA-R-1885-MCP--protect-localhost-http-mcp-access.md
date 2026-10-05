---
atom_id: CA-R-1885
content_role: Requirement
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 17:12:15 +0000"
subjects:
  governs: "MCP/HTTP endpoint/Access boundary"
  depends_on: [MCP, HTTP, Operator, Permission, Credential, Request, Tool]
relations:
  relates_to: [CA-R-1118]
---
# Summary

protect localhost HTTP MCP access

## Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

## Claim

the HTTP endpoint **must** admit a Request **only** with a valid transport Credential and an admitted Host and Origin, while preserving the existing Operator authorization and Tool permission boundaries.

## Details

1. use a shared local bearer Token, supplied at runtime; it grants transport access, not Operator identity or permission to mutate.
2. publish the Docker port on host loopback **only**. Requests with an absent Origin are allowed for non-browser clients; a present Origin must be loopback-allowlisted.
3. missing configuration, absent or invalid bearer Tokens, hostile Hosts and hostile Origins fail closed before Tool handling.
4. keep Credentials out of discovery, results, diagnostics, logs, command arguments, image contents and committed carriers.
