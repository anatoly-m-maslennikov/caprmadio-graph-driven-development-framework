---
atom_id: CA-C-442
content_role: Concern
type: Conflict
current_scope_unit: WORKFLOW_ORCHESTRATOR
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 22:22:32 +0000"
subjects:
  governs: "Selected queue route admission"
  depends_on: [Workflow, MCP, Implementation, Journal]
relations:
  concern_about: [CA-D-521, CA-D-547, CA-P-1527, CA-P-1551, CA-P-1552]
---
# Summary

Align selected queue admission with fifteen-route scope

## Concern

The accepted MCP contract expands the selected Epic to fifteen routes, but CA-D-521@3 closes enqueue_selected admission to only thirteen registrations. Implementing the two additional routes through the existing queue requires its source admission amendment first.

## Evidences

CA-D-521's Scope and enqueue_selected paragraph explicitly say thirteen. CA-P-1543 accepts the fifteen-route MCP source but correctly does not claim current queue admission/runtime registration. CA-P-1551/1552 bind the narrow source amendment and independent acceptance.

## Blast radius

Query queue integration stays gated until current Delivery authority admits the exact same fifteen-route canonical manifest. No code silently widens the closed source contract or creates a second executor.

