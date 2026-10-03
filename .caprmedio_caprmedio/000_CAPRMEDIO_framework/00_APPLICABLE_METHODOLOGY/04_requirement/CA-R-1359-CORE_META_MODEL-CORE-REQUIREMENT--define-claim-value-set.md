---
atom_id: CA-R-1359
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - Claim Value Set
  depends_on:
    continuant:
      - Atom/Claim
      - Property
      - IS_ALLOWED_VALUE_OF
version: 2
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-1270
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1359-CORE_META_MODEL-CORE-REQUIREMENT--define-claim-value-set.md
---
# Define Claim Value Set

a Claim Value Set **means** one Claim expression **in** the form `X: (A, B, C)`, **where** X identifies **`=1`** Property **and** `(A, B, C)` identifies one finite unordered set of **`>=1`** unique canonical values allowed by X; the value order carries no authority, **and** the complete set **must** have one authority unit **and** lifecycle by accepting, replacing, **and** retiring **all** values together as one Claim.
