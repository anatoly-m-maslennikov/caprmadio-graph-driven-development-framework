---
atom_id: CA-E-533
content_role: Evaluation
type: QA_CASE
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 20:41:31 +0400"
subjects:
  governs: "MCP/implementation"
  depends_on: [MCP, Tool, Operator, Project, Implementation, Workflow, Atom]
---
# Summary

Verify MCP reload publication and rollback

## Scope

server-side hot reload for the Project-local MCP gateway.

## Claim

the MCP Evaluation **must** verify implementation reload through the real stdio protocol with controlled mock implementations.

## Details

- keep one client connection open; call implementation A, reload B, then call B successfully without reconnect.
- add, remove **and** change a Tool contract; verify the published list **and** negotiated notification.
- submit syntax-invalid code, initialization failure, duplicate Tool names **and** invalid schemas; verify rejection **and** continued service from A.
- reload the same frontier twice; verify unchanged generation **and** no duplicate effects.
- submit an extra field, traversal path **or** alternate Project root; verify rejection before execution.
- distinguish sent notification from unconfirmed client refresh; mocks do **not** prove Codex desktop discovery.

