---
atom_id: CA-D-531
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Dispatch Interface"
  depends_on: ["Tool", "Authorization", "Atom"]
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
relations:
  delivery_for: [CA-R-1825, CA-R-1827]
---
# Summary

Deliver sealed lifecycle dispatch interface

## Scope

The future Project-local MCP entrypoint contract; no executable carrier is supplied by this specification.

## Claim

The entrypoint accepts one request containing target selector, expected current Version/digest, requested result/operation, optional predecessor, and `apply=false` by default. Its response returns the selected native operation, model resolution, seal, diagnostics, `replace_handoff` where required, and the result contract of CA-R-1828. `apply=true` is accepted only with the explicitly authorized sealed MCP envelope.

## Details

For an admitted Status change, diagnostics include broken active references and active referrers without silently repairing them or suppressing the authorized transition.
