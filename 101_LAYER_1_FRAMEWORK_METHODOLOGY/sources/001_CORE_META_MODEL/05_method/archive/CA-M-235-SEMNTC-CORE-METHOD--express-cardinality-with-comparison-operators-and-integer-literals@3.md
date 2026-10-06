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
version: 3
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Express Cardinality with Comparison Operators and Integer Literals

**to** author one numeric Cardinality Constraint, the Author **must** serialize one canonical comparison CCE Operator immediately followed by one Nonnegative Integer Literal as a prefix immediately **before** the counted Entity **or** expression; examples: **`=1`** Author, **`>=1`** Requirement Atom, **`<=1`** Type, **`>=0`** Property.
