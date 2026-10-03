---
atom_id: CA-R-1358
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Atom/Claim
  depends_on:
    continuant:
      - Atom/Scope
      - Atom/Claim/Scope
      - Claim Value Set
      - Property
      - IS_ALLOWED_VALUE_OF
version: 5
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-918
    - CA-R-919
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1358-CORE_META_MODEL-CORE-REQUIREMENT--consolidate-single-value-claims-as-one-value-set-claim.md
---
# Consolidate Single-Value Claims as One Value-Set Claim

multiple Claims with the same Atom Scope, Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.
