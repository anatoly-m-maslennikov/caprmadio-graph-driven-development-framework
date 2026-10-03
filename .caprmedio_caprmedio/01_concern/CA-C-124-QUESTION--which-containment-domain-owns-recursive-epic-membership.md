---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Structural Entity/Recursive Containment"
  depends_on:
    - "Structural Entity/Direct Containment"
    - "Atom Collection/Type: Epic"
    - "Project Structure"
    - "Artifact/Carrier"
priority: medium
version: 1
updated_at: "2026-09-17 04:44:33 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which containment domain owns recursive Epic membership?

how should Epic membership specialize generic Structural Entity containment **without** equating logical Scope Unit parentage with physical Carrier nesting?

## Evidence

- CA-R-1498, replacing CA-D-265, owns the representation-independent transitive-closure invariant. CA-R-1302 repeats transitive closure for Epic membership.
- CA-D-264 derives direct containment for an Artifact Revision from its nearest ancestor Directory Carrier. an Epic is a Structural Entity, **not** an Artifact; this rule does **not** explicitly define nested Epic containment.
- CA-E-426 expects nested Epics, Task members, Status-directory transparency, **and** derived direct/recursive membership. deleting R-1302 as a duplicate **without** reconciling that domain would leave its expected membership derivation incompletely governed.
- CA-R-1483 **and** CA-M-291 reserve logical Scope Unit parentage **to** Project Structure. observed folder nesting **must not** become an independent structural declaration.

## Principle check

CA-M-002 favors one closure rule; CA-M-006 requires graph-specific coherent relations; CA-R-1490 preserves existing membership cases. these do **not** establish that the physical Carrier graph, logical Scope Unit tree, **and** Epic membership view have identical edges.

## Disposition

defer the uncertain deduplication **and** domain unification. preserve R-1302, D-264, D-266, **and** E-426's cases. establish exact direct-edge domains **and** inherited membership semantics **before** retiring the specialized definition. C-117 separately tracks missing Project Structure declarations. no new stored containment graph **or** directory migration is authorized here.
