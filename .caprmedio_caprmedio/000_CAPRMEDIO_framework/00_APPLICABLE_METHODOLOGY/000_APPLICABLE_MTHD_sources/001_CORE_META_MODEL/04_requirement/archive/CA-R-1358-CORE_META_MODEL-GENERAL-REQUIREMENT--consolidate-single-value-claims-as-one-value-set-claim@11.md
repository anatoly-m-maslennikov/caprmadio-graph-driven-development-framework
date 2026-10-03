---
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "Atom/Scope"
    - "Atom/Claim"
    - "Claim Value Set"
    - "Property"
    - "IS_ALLOWED_VALUE_OF"
version: 11
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  child_of:
    - CA-R-918
    - CA-R-1596
---
# Consolidate Single-Value Claims as One Value-Set Claim

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.
