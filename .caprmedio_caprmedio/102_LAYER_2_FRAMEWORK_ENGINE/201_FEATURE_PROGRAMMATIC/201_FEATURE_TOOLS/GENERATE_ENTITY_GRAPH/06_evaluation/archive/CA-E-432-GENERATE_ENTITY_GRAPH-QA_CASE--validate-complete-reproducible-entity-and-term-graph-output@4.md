---
atom_id: CA-E-432
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Entity Graph Projection"
  depends_on: []
version: 4
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-R-1387
    - CA-M-259
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate complete reproducible Entity and Term graph output

## Test case

Generate twice from identical fixtures containing declared Terms, one parent chain, direct dependencies with transitive closure, an unresolved reference, a dependency cycle, a cardinality violation, and an unparseable Carrier.

## Acceptance criteria

The two semantic outputs are byte-identical and stably ordered. They contain every declared Term, direct parent, direct edge, closure edge, cycle, violation, unresolved reference, unparseable region, source path and digest, frontier identity, settings digest, and explicit non-authoritative status.
