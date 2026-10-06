---
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "Atom"
    - "Atom/Content Role: Evaluation"
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Summary"
    - "Scope Expression"
    - "Scope Unit"
version: 14
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  evaluation_for:
    - CA-R-1596
    - CA-R-1270
    - CA-R-1271
---
# Validate Composite Claims and Derived Summaries

the Evaluation **must** reject an Atom **if** it has **`!=1`** Claims, **`!=1`** resolved Claim Target Scope Units, an independently replaceable component inside **`=1`** Claim, ambiguous composite grouping, a non-deterministic Scope Expression, **or** a Summary that is **not** reproducibly source-faithful **to** the complete Claim, including its textual applicability restrictions, **and** its Claim Target Scope Unit. evaluate restrictions **to** selected sibling Scope Units under CA-E-461 separately from these rejection criteria.
