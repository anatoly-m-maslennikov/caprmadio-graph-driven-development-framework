---
subjects:
  governs: "Scope Expression/Canonical Scope Signature"
  depends_on:
    - "Scope Expression"
    - "Atom"
    - "Atom/Identifier"
    - "Artifact/Carrier"
    - "CCE Operator"
version: 13
updated_at: "2026-10-02 22:23:29 +0400"
relations: {}
atom_id: "CA-R-1361"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1361-CORE_META_MODEL--define-canonical-scope-signature.md
  source_atom_id: CA-R-1361
  source_atom_revision: 13
  source_sha256: 7e5fce4d3eeafe4bc4cab3f4fcd972c5e3a94b5ba86fc96f3d0285d7737a977f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Canonical Scope Signature

## Scope

parenthesized Scope Expression occurrences considered for a Canonical Scope Signature.

## Claim

a Canonical Scope Signature **means** a derived non-authoritative comparison value for **`=1`** parenthesized Scope Expression occurrence satisfying **all** of the following boundaries.

## Details

### admitted expression

- a group **contains** **`>=2`** operands **and** uses **`=1`** Boolean Operator value from (**`and`**, **`or`**). its operands are joined **only** by repetitions of that Operator.
- an operand is an exact Atom ID **or** a nested parenthesized group with the same Boolean Operator as its containing group.
- **every** exact Atom ID resolves **to** **`=1`** active Atom Carrier inside the selected source frontier.

### canonical value

- the value preserves whether the root Boolean Operator is **`and`** **or** **`or`**.
- the value represents the flattened same-operator group as unique exact Atom IDs **in** canonical lexical order.
- groups that differ **only** by same-operator nesting, repeated exact Atom IDs, **or** operand order have the same value.

### exclusions

mixed Boolean Operators, **without**, **where**, **all**, **every** other CCE Operator, functions, Entity-kind selectors, descendant **or** dynamic selectors, unresolved identities, a changing source frontier, **and** unparseable prose are outside this signature domain.
