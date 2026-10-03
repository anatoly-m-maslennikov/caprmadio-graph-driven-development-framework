---
subjects:
  governs: "Claim Value Set"
  depends_on:
    - "Atom/Claim"
    - "Property"
    - "IS_ALLOWED_VALUE_OF"
version: 7
updated_at: "2026-09-10 03:25:26 +0400"
relations:
  child_of:
    - CA-R-1270
---
# Define Claim Value Set

a Claim Value Set **means** one Claim expression **in** the form `X: (A, B, C)`, **where** X identifies **`=1`** Property **and** `(A, B, C)` identifies one finite unordered set of **`>=1`** unique canonical values allowed by X; the value order carries no authority, **and** the complete set **must** have one authority unit **and** lifecycle by accepting, replacing, **and** retiring **all** values together as one Claim.
