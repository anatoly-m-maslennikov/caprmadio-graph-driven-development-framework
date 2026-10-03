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
      - Atom/Claim/Scope
version: 7
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-384-CORE_META_MODEL-CORE-EVALUATION--validate-composite-claims-and-derived-summaries.md
---
# Validate Composite Claims and Derived Summaries

the Evaluation **must** reject an Atom **if** it has zero **or** multiple Claims, multiple Claim Scopes, an independently replaceable component inside one Claim, ambiguous composite grouping, a non-deterministic Scope Expression, **or** a Summary that is **not** reproducibly source-faithful to the complete Claim **and** any Claim Scope.
