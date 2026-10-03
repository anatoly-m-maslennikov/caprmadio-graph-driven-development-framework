---
atom_id: CA-R-1359
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Claim Value Set"
  depends_on:
    - "Atom/Claim"
    - "Property"
    - "IS_ALLOWED_VALUE_OF"
version: 4
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - CA-R-1270
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define Claim Value Set

a Claim Value Set **means** one Claim expression **in** the form `X: (A, B, C)`, **where** X identifies **`=1`** Property **and** `(A, B, C)` identifies one finite unordered set of **`>=1`** unique canonical values allowed by X; the value order carries no authority, **and** the complete set **must** have one authority unit **and** lifecycle by accepting, replacing, **and** retiring **all** values together as one Claim.
