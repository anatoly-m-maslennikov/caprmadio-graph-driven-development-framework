---
atom_id: CA-E-558
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:45 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Persistence and boundary case"
  depends_on: [Tool, Projection, Artifact, Journal, Workflow Run, Step Run]
relations:
  evaluation_for: [CA-R-1837, CA-R-1838]
---
# Summary

Verify determinism, persistence, and nonmutation

## Scope

Functional persistence, `no_op`, destination-rejection, and shared-recording boundary proof for both graph kinds.

## Claim

Only an exact current, complete and validated projection may persist or return `no_op`; all authority and Journal inputs remain unchanged.

## Details

Run description/generation without a destination, then persist to one valid derived destination and repeat through one unambiguous registered destination. Reject authority/Journal destinations, traversal, symlink escape, ambiguous destination, authoritative-output request, stale prior output, and incomplete-quality `no_op`. Compare source/Journal bytes before and after, assert atomic replacement of only the allowed derived output, canonical determinism, retained non-authoritative status, and read-only consumer boundary. Inject unresolved recording and assert a truthful pending/blocking receipt with no completed Run claim or construction replay. This carrier specifies functional proof, not runtime evidence.
