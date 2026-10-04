---
atom_id: CA-D-539
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
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Contract"
  depends_on: [Tool, Projection, Artifact, Journal]
relations:
  delivery_for: [CA-R-1835, CA-R-1836, CA-R-1837, CA-R-1838]
---
# Summary

Bind strict graph request and result contract

## Scope

The minimum Tool/MCP request-result boundary for one graph projection request.

## Claim

The Tool **must** reject ambiguous or mixed graph requests and return a result that makes source lineage, graph quality, namespace, effects, and non-authoritative state inspectable.

## Details

The strict request has `graph_kind`, `source_frontier`, `selection`, optional `display_selection`, `representation_configuration`, optional `output_destination`, optional `existing_projection_evidence`, `capability_permission_evidence`, and `run_recording_context`. Unknown fields, absent/ambiguous frontiers, mixed graph kinds, and unbound destination/recording inputs are errors or blocking conditions.

The strict result has `outcome`, exactly one of `entities_graph` or `terms_graph`, `source_frontier_evidence`, `selection_evidence`, `lineage`, `quality_dispositions`, `diagnostics`, `non_authoritative: true`, `output_effects`, `projection_revision` if persisted, and `run_receipt_refs`. It never places Terms in the Entities namespace or vice versa, and it never converts diagnostics into a pass.
