---
atom_id: CA-E-384
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - Atom/Claim
  depends_on:
    continuant:
      - Atom
      - "Atom/Content Role: Evaluation"
      - Atom/Claim/Structural Entity
      - Atom/Summary
      - Scope Expression
      - Scope Unit
version: 9
updated_at: "2026-09-12 16:07:47 +0400"
relations:
  evaluation_for:
    - CA-R-919
    - CA-R-1270
    - CA-R-1271
---
# Validate Composite Claims and Derived Summaries

the Evaluation **must** reject an Atom **if** it has **`!=1`** Claims, **`!=1`** resolved Claim Structural Entities, an independently replaceable component inside **`=1`** Claim, ambiguous composite grouping, a non-deterministic Scope Expression, **or** a Summary that is **not** reproducibly source-faithful **to** the complete Claim **and** its Claim Structural Entity. evaluate restrictions **to** selected sibling Scope Units under CA-E-461 separately from these rejection criteria.
