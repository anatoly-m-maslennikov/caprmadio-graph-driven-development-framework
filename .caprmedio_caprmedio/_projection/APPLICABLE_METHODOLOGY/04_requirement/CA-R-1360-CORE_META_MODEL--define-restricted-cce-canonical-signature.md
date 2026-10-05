---
subjects:
  governs: "Atom/Claim/Canonical Signature"
  depends_on:
    - "Atom/Claim"
    - "CCE Operator"
    - "Subject Path"
version: 9
updated_at: "2026-09-28 15:12:22 +0400"
relations:
  child_of:
    - CA-R-918
atom_id: "CA-R-1360"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1360-CORE_META_MODEL--define-restricted-cce-canonical-signature.md
  source_atom_id: CA-R-1360
  source_atom_revision: 9
  source_sha256: 3baad57dd68218df5bc969b97bbca90296d177f0669f277a32c1d8c1c537b5fc
  original_relations_sha256: 33e20e2e1769e02a63159d23b72e52fbce54f31ee1cf24d437c9d3bcc4fd118c
---
# Summary
Define Restricted CCE Canonical Signature

## Scope
parenthesized restricted Boolean expression occurrences **in** Atom Claims.

## Claim

a Canonical Signature **means** **`=1`** derived non-authoritative comparison value for **`=1`** parenthesized restricted Boolean expression occurrence **in** one Atom Claim, **where** the following constraints apply:

- the grammar is:
  - `group ::= (operand **and** operand [**and** operand ...]) | (operand **or** operand [**or** operand ...])`;
  - `operand ::= atomic predicate | nested group with the same Boolean Operator`;
  - `atomic predicate ::= subject path: value`.
- canonicalization:
  - flattens nested same-operator groups;
  - removes duplicate atomic predicates;
  - sorts the remaining atomic predicates;
  - preserves the root Boolean Operator.
- canonicalization excludes:
  - mixed Boolean Operators;
  - **every** other CCE Operator;
  - unrecognized bold token;
  - unbalanced parentheses;
  - unparseable prose.

## Details
