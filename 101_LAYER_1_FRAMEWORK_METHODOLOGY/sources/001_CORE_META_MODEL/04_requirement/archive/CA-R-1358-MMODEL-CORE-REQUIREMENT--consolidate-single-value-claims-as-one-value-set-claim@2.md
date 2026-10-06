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
      - Atom/Current Scope
      - Atom/Claim Scope
      - Claim Value Set
      - IS_ALLOWED_VALUE_OF
version: 2
updated_at: 2026-09-01 22:26:54 +0400
relations:
  child_of:
    - CA-R-918
    - CA-R-919
---
# Consolidate Single-Value Claims as One Value-Set Claim

multiple Claims with the same Current Scope, Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.
