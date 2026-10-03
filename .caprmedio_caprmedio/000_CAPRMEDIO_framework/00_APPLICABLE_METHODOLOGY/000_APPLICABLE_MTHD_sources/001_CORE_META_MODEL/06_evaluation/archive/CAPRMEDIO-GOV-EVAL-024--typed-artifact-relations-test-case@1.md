---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CAPRMEDIO-GOV-METH-023--typed-artifact-relations
---

# Test Case — Validate typed artifact relations

Deterministic proof must accept every canonical relation, legacy sealed
`child_of`, multiple distinct targets, and valid `projection_of` ranges. It
must reject unknown relation types, malformed or duplicate edges, authored
inverse relations, unresolved targets, self-relations, incompatible structural
replacement combinations, invalid range frontiers, and cycles where the
relation semantics require acyclicity.

Generated traceability must contain canonical forward typed edges, translate
legacy `child_of` compatibility input, derive commit `implementation_of` edges,
and store neither authored nor generated inverse relation names.

This emitted Test definition is immutable. Runs and evidence are separate.

## Primary claim

Deterministic validation proves the typed-relation vocabulary, direction, integrity, compatibility, projection ranges, and generated traceability contract.
