---
atom_id: CA-R-1358
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "Atom/Scope"
    - "Atom/Claim/Scope"
    - "Claim Value Set"
    - "Property"
    - "IS_ALLOWED_VALUE_OF"
version: 8
updated_at: "2026-09-10 06:59:09 +0400"
relations:
  child_of:
    - CA-R-918
    - CA-R-919
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Consolidate Single-Value Claims as One Value-Set Claim

multiple Claims with the same Atom Scope, Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.
