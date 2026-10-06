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
version: 3
updated_at: "2026-09-15 01:47:49 +0400"
relations:
  evaluation_for:
    - CA-R-1470
    - CA-R-1471
    - CA-R-1437
    - CAPRMEDIO-META-REQU-657
---
# Validate Single Source of Truth in secondary graphs

the Evaluation **must** distinguish authoritative source facts from their secondary graph representations **and** reject a Projection that acquires independent authority for a represented fact.

## Test cases

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
