---
subjects:
  governs: "Cardinality Constraint Authoring"
  depends_on:
    - "Cardinality Constraint"
    - "CCE Operator Registry"
    - "Nonnegative Integer Literal"
version: 11
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-235"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-235-CORE_META_MODEL--express-cardinality-with-comparison-operators-and-integer-literals.md
  source_atom_id: CA-M-235
  source_atom_revision: 11
  source_sha256: 738043ae13bf80391f1bd5ac62b179a7f68df6b6203474f322e78d8469f8456d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Express Cardinality with Comparison Operators **and** Integer Literals

## Scope

numeric Cardinality Constraint authoring.

## Claim

**to** author one numeric Cardinality Constraint, the Author **must** serialize one canonical comparison CCE Operator immediately followed by one Nonnegative Integer Literal as a prefix immediately **before** the counted Entity **or** expression; examples: **`=1`** Author, **`>=1`** Requirement Atom, **`<=1`** Type, **`>=0`** Property.

## Details
