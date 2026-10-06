---
atom_id: CA-E-384
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Claim-Boundary Evaluation
  depends_on:
    continuant:
      - Claim
      - Claim Scope
version: 2
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Validate Composite Claims and Derived Summaries

the Evaluation **must** reject an Atom **if** it has zero **or** multiple Claims, zero **or** multiple Claim Scopes, an independently replaceable component inside one Claim, ambiguous composite grouping, a non-deterministic Scope Expression, **or** a Summary that is **not** reproducibly source-faithful to the complete Claim **and** Claim Scope.
