---
atom_id: CA-R-1837
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:31:30 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Quality disposition"
  depends_on: [Tool, Projection, Artifact, Journal, Workflow Run, Step Run]
relations:
  relates_to: [CA-R-1835, CA-R-1836, CA-O-134, CA-O-137, CA-R-1387, CA-E-432, CA-E-433]
---
# Summary

Enforce projection quality and truthful outcomes

## Scope

The common quality gate and result disposition of the two graph builders.

## Claim

`GENERATE_ENTITY_GRAPH` **must not** return `built` or `no_op` when any required selection, source, fidelity, graph-validity, currentness, permission, persistence, or recording condition is unmet.

## Details

The result carries stable, sorted graph data plus a per-condition disposition: `pass`, `fail`, `unresolved`, or `not_applicable`, with source references and diagnostics. Complete requested coverage, exact source frontier/settings digest, graph-kind namespace, validation disposition, output identity/revision if persisted, and non-authoritative status are mandatory result fields. Identical readable source bytes and settings produce byte-identical semantic output in stable canonical order.

Unknown/malformed/unreadable regions, stale inputs/prior projections, unresolved endpoints, conflicts, cycles, self-references, and cardinality defects are never silently omitted, repaired, converted to absence, or used to widen the selection. `no_op` additionally proves that an existing output matches the exact current request and passed all required checks. A capability or permission failure, ambiguous destination, unresolved Journal receipt, or stale output is not `no_op`.

Immediately before publication, the builder rechecks that every bound selected source identity, Revision, location, and digest is unchanged; a mismatch returns `stale` or `blocked` and never silently substitutes, repairs, or modifies source authority. The builder may publish only to an explicit or unambiguously configured derived-output destination; it rejects authority/Journal destinations, traversal, symlink escape, ambiguity, and authoritative-output requests. It reports actual output effects and pending/confirmed shared receipt references without fabricating a mutation, completed Run, or recovery.

### Sources

- CA-O-134 v2 and CA-O-137 v2, result/effects clauses.
- CA-R-1387 v8, CA-M-259 v7, CA-E-432 v7, and CA-E-433 v8.
