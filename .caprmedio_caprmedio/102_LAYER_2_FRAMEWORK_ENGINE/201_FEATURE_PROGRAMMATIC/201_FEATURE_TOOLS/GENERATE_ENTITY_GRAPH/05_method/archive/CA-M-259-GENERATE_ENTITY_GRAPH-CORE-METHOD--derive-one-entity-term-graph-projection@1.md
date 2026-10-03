---
atom_id: CA-M-259
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - projection-pipeline
version: 1
updated_at: 2026-09-04 03:10:59 +0400
relations:
  method_for:
    - CA-R-1387
---
# Derive one Entity and Term graph Projection

## Procedure

1. Resolve exactly one caller-selected folder or equivalent source frontier, its settings, and its Carrier digests. Reject an absent, ambiguous, escaping, or unreadable frontier.
2. Parse each readable Carrier without mutation. Record every unknown or unparseable region with its path and diagnostic instead of dropping it.
3. Extract declared Terms, direct-parent declarations, and direct dependency declarations with source lineage. Preserve unresolved references explicitly.
4. Build the direct-parent tree, direct dependency graph, and complete dependency-Term closure. Detect cycles, multiple-parent or other declared cardinality violations, and unreachable or unresolved nodes.
5. Sort every node, edge, diagnostic, and lineage entry by stable canonical keys. Mark the result non-authoritative and bind it to the complete source-frontier identity and settings digest.
6. Return the Projection without mutation unless an explicit output path or one registered unambiguous destination was supplied. On persistence, reject an authority destination and replace exactly one Projection Carrier atomically.

## Outcome

The result is reproducible as-is graph data that `GRAPH_APP` may consume read-only; it is neither an Atom nor an analysis and has no authority.
