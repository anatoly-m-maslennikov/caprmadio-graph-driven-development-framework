---
atom_id: CA-O-173
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: compile candidate Methodology"
  depends_on: [Workflow, Step, Action, Applicable Methodology, Compiler, Delivery, Journal]
version: 1
updated_at: 2026-10-05 06:13:05 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-166]
---
# Summary

Compile the candidate Applicable Methodology

## Step

This Step invokes CA-O-166 once with phase `compile`, binding only the complete delivered source manifest from CA-O-172, the reviewed selected-snapshot compiler Tool boundary and the canonical candidate Projection contract. A later derived runtime Methodology delivery is not compiler output authority.

## Details

This is not another compiler graph: CA-O-166 uses the reviewed Tool boundary required for a selected pinned snapshot while preserving the existing canonical compiler authority. A changed frontier, incomplete delivery, unbound Tool/layout or canonical Projection mismatch stops without runtime installation, image work or promotion.
