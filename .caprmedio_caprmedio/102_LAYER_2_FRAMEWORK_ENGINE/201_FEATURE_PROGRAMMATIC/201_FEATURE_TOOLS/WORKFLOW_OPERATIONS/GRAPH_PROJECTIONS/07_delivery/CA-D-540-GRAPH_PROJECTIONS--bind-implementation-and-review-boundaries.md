---
atom_id: CA-D-540
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:45 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Delivery boundary"
  depends_on: [Tool, Workflow, Action, Projection, Journal, Implementation]
relations:
  delivery_for: [CA-E-555, CA-E-556, CA-E-557, CA-E-558]
---
# Summary

Bind implementation and review boundaries

## Scope

The implementation gate and integration boundary for graph projection delivery.

## Claim

No implementation work may begin until independent RMED review accepts this packet; later implementation must reuse shared Run/Journal support and prove all four functional cases through the real exposed Tool/MCP and required Docker image.

## Details

The implementation owns parsing, construction, canonical serialization, derived-output persistence, result assembly, and tests at the CA-D-538 entrypoint. It consumes source authority and selected Workflow/Step/Action/Run bindings without implementing source repair, authority mutation, or a second Journal schema. Functional delivery is incomplete until CA-E-555 through CA-E-558 have executed, including complete, incomplete/conflicting, cycle/malformed/self-reference, determinism, and nonmutation cases. This RMED carrier is a specification gate, not runtime-success evidence.
