---
atom_id: CA-R-1836
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:45 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Terms Graph"
  depends_on: [Tool, Workflow, Action, Term, Governed Term, Definition Atom, Projection, Relation Kind, Artifact, Journal]
relations:
  relates_to: [CA-O-136, CA-O-137, CA-O-138, CA-R-1387, CA-M-259, CA-R-1335, CA-R-1454, CA-E-382]
---
# Summary

Build faithful Terms Graph projections

## Scope

One selected `GENERATE_ENTITY_GRAPH` Terms Graph build/confirmation request and its non-authoritative derived output.

## Claim

The builder **must** represent all and only selected governed Terms and admitted Terms-graph Relations in a namespace distinct from Entities Graph, retaining defining authority and every selected dependency/ancestor path, including cycles and unresolved or conflicting evidence.

## Details

The strict request binds graph kind `terms`, exact source frontier and selection (including optional governed-only/narrower view), representation configuration, target derived-output destination, existing output/evidence if any, capability/permission evidence, and Run/Journal references. Term membership requires governing definition evidence; spelling, capitalization, filenames, Subject reuse, an Entity edge, or a referenced path cannot invent a Term or meaning. The output retains each native Term's canonical identity, defining Claim/Atom Revision/location/digest, admitted Relation metadata and direction, external references, direct dependency/parent Relations, and deterministic transitive dependency and ancestor sets.

The `terms_graph` namespace contains only Terms-graph nodes and admitted Relations. Its diagnostics explicitly retain malformed, missing, unreadable, stale, unresolved, conflicting, cardinality-violating, self-referential, and cyclic source facts. A faithful conflict/cycle representation is diagnostic data, not a valid complete graph, and neither hierarchy repair nor source editing is allowed.

`built` or `no_op` is permitted only when exact selected coverage, source/definition currentness, fidelity, graph validity, permission, and durable recording all pass. Any unmet quality condition returns its truthful non-complete outcome and affected frontier; an authorized limited diagnostic output remains non-authoritative and incomplete/invalid as applicable.

### Sources

- CA-O-136 v2, CA-O-137 v2, CA-O-138 v1.
- CA-R-1387 v8 and CA-M-259 v7 provide the existing reproducibility and persistence baseline.
