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
version: 4
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-235-CORE_META_MODEL-CORE-METHOD--express-cardinality-with-comparison-operators-and-integer-literals.md
---
# Express Cardinality with Comparison Operators and Integer Literals

**to** author one numeric Cardinality Constraint, the Author **must** serialize one canonical comparison CCE Operator immediately followed by one Nonnegative Integer Literal as a prefix immediately **before** the counted Entity **or** expression; examples: **`=1`** Author, **`>=1`** Requirement Atom, **`<=1`** Type, **`>=0`** Property.
