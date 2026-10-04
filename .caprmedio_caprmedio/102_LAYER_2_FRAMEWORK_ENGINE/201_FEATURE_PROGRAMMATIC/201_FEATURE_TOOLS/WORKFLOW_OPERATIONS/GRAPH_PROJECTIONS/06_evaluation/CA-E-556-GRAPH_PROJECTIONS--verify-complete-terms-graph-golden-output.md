---
atom_id: CA-E-556
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
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Terms Graph golden case"
  depends_on: [Tool, Term, Governed Term, Definition Atom, Projection, Relation Kind]
relations:
  evaluation_for: [CA-R-1836, CA-R-1837, CA-R-1838]
---
# Summary

Verify complete Terms Graph golden output

## Scope

Functional complete-case proof for the Terms Graph builder.

## Claim

The golden case **must** prove exact governed-Term and admitted-Relation representation, deterministic ancestor/dependency sets, separated namespace, and a truthful `built` result.

## Details

Use a selected readable fixture with governed Definitions, admitted Terms-graph Relations, direct parents/dependencies, and non-cyclic transitive ancestor/dependency closures. Assert all and only selected Terms and internal Relations, defining Claim/Atom path/revision/digest evidence, separate `terms_graph` namespace, stable direct and transitive sets, non-authoritative status, valid complete coverage, and shared receipt references. Generate twice from identical bytes/settings and compare canonical semantic output byte-for-byte; assert no source or Journal mutation. This carrier specifies functional proof, not a runtime pass.
