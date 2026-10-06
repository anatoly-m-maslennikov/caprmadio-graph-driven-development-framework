---
atom_id: CA-R-1361
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - Scope Expression/Canonical Scope Signature
  depends_on:
    continuant:
      - Scope Expression
      - Atom/Claim Scope
      - Atom/Carrier
version: 1
updated_at: 2026-09-01 23:45:22 +0400
relations:
  child_of:
    - CA-R-999
---
# Define Canonical Scope Signature

a Canonical Scope Signature **means** one derived non-authoritative comparison value for **`=1`** parenthesized Scope Expression occurrence **only** **when** that occurrence has this restricted grammar: `scope_group ::= (atom_id **or** atom_id [**or** atom_id ...]) **or** (atom_id **and** atom_id [**and** atom_id ...])`; `atom_id ::= one exact Atom ID that resolves **`=1`** active Atom Carrier inside the selected source frontier`; canonicalization flattens nested same-operator groups, removes duplicate exact Atom IDs, sorts the remaining Atom IDs **in** canonical lexical order, preserves **or** **and** **and** distinction, **and** excludes mixed operators, **without**, **where**, **all**, **every** other CCE Operator, function, Entity-kind selector, descendant **or** dynamic selector, unresolved identity, changing source frontier, **or** unparseable prose.
