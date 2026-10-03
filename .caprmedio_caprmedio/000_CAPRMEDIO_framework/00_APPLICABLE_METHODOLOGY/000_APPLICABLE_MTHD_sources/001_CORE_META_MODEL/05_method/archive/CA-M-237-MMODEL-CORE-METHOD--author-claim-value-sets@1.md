---
atom_id: CA-M-237
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Claim Value Set Authoring
  depends_on:
    continuant:
      - Atom/Claim
      - Claim Value Set
      - Subject Expression
version: 1
updated_at: 2026-09-01 22:26:54 +0400
relations:
  child_of:
    - CA-M-115
---
# Author Claim Value Sets

**to** author one Claim Value Set, the Author **must**:

1. identify **`=1`** Property X within **`=1`** Claim;
2. write its finite allowed-value set as `X: (A, B, C)`;
3. include **`>=1`** unique canonical values **and** treat their order as non-authoritative;
4. retain the complete set in **`=1`** Claim **only** **if** **all** values **must** be accepted, replaced, **and** retired together;
5. interpret `:` as Claim Value-Set syntax inside that Claim **and** as **`=1`** IS_ALLOWED_VALUE_OF relation **only** inside a Subject Expression.
