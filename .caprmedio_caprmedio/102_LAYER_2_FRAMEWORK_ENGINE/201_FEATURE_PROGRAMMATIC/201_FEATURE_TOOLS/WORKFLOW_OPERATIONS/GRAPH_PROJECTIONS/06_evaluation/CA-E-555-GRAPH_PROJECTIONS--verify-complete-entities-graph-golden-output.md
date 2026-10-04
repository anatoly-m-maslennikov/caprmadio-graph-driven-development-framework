---
atom_id: CA-E-555
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
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Entities Graph golden case"
  depends_on: [Tool, Entity, Property, Projection, Project Structure, Relation Kind]
relations:
  evaluation_for: [CA-R-1835, CA-R-1837, CA-R-1838]
---
# Summary

Verify complete Entities Graph golden output

## Scope

Functional complete-case proof for the Entities Graph builder.

## Claim

The golden case **must** prove exact selected Entity/Property/Relation and declared Scope Unit representation with traceability, deterministic output, and a truthful `built` result.

## Details

Use a selected readable fixture with multiple Entities, bearer-qualified identities, complete Property facts, admitted native/external Relations, and declared Project Structure records. Assert all and only selected nodes/edges, complete property values, exact Atom/Claim or Project Structure path/revision/digest evidence, separate `entities_graph` namespace, selection boundary, non-authoritative status, valid complete coverage, and shared receipt references. Generate twice from identical bytes/settings and compare canonical semantic output byte-for-byte. Confirm that no source or Journal byte changes. This carrier specifies functional proof, not a runtime pass.
