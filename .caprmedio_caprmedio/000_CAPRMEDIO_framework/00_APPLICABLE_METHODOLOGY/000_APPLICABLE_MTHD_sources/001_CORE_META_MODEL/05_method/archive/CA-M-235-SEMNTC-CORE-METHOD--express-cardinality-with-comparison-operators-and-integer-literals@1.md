---
atom_id: CA-M-235
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Cardinality Constraint Authoring
  depends_on:
    continuant:
      - Cardinality Constraint
      - CCE Operator Registry
      - Nonnegative Integer Literal
version: 1
updated_at: 2026-08-29 00:40:53 +0400
relations: {}
---
# Express Cardinality with Comparison Operators and Integer Literals

**to** author one numeric Cardinality Constraint, the Author **must** serialize one canonical comparison CCE Operator immediately followed by one Nonnegative Integer Literal; examples: **`=1`**, **`>=1`**, **`<=1`**, **`>=0`**.
