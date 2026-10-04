---
subjects:
  governs: "CAPRMEDIO Graph"
  depends_on:
    - "Single Source of Truth"
    - "Projection"
    - "Atom"
    - "Atom/Claim"
    - "Structural Entity"
    - "Journal"
    - "Relation"
    - "Relation Kind"
version: 7
updated_at: "2026-09-30 19:57:23 +0000"
relations:
  evaluation_for:
    - CA-R-1437
    - CA-R-1470
    - CA-R-1471
    - CA-R-1746
atom_id: "CA-E-466"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-466-CORE_META_MODEL-QA_CASE--validate-single-source-of-truth-in-secondary-graphs.md
---
# Summary
Validate Single Source of Truth in secondary graphs

## Scope
source authority **in** secondary graph representations.

## Claim
the Evaluation **must** distinguish authoritative source facts from their secondary graph representations **and** reject a Projection that acquires independent authority for a represented fact.

### Test cases

| Case | Expected result |
|---|---|
| **`=1`** source Claim represented **in** multiple graphs | pass **if** **all** representations retain the same source identity **and** applicable Revision |
| two independently maintained authoritative declarations for the same fact **in** the same context, even **when** their values agree | fail |
| different Claims **or** different source facts used by a derived result | no Single Source of Truth failure merely because there are multiple source Atoms |
| a permitted derived Relation with identified derivation authority **and** source inputs, but no separately authored declaration for its computed result | pass this source-authority check |
| a derived edge with no admitted derivation authority **or** missing required source evidence | fail **or** report unresolved evidence; do **not** invent a source declaration |
| a source Atom reached through another Projection | pass **if** ultimate source traceability is retained |
| a Journal event **or** structural fact represented **in** a graph | pass **if** its existing source authority remains intact; do **not** fabricate an Atom Claim as historical **or** observed evidence |
| a projected fact corrected independently while its source **and** governing derivation remain unchanged | fail |

passing this source-authority Evaluation does **not** establish graph-specific Relation validity, completeness, **or** the truth of a recorded outcome; those remain subject **to** their applicable Evaluations.

## Details
