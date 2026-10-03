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
---
# Summary

Express Cardinality with Comparison Operators **and** Integer Literals

## Scope

numeric Cardinality Constraint authoring.

## Claim

**to** author one numeric Cardinality Constraint, the Author **must** serialize one canonical comparison CCE Operator immediately followed by one Nonnegative Integer Literal as a prefix immediately **before** the counted Entity **or** expression; examples: **`=1`** Author, **`>=1`** Requirement Atom, **`<=1`** Type, **`>=0`** Property.

## Details
