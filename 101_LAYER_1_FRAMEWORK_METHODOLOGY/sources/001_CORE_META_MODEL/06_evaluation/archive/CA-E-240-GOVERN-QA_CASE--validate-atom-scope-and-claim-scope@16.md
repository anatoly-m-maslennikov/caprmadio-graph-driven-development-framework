---
subjects:
  governs:
    occurrent:
      - Scope Reference Validation
  depends_on:
    continuant:
      - Atom/Scope
      - Atom/Claim/Governed Subject Set
      - Atom/Claim/Scope
      - Atom/Claim/Scope/Scope Unit Set
      - Structural Parent Relation
atom_id: CA-E-240
cce_version: cce_1
cce_form: evaluation
version: 16
updated_at: 2026-09-04 14:07:21 +0400
relations: {}
---
# Validate Atom Scope and Claim Scope

## Claim checked

**every** Atom resolves **`=1`** Atom Scope, **`=1`** Governed Subject Set, **and** **`<=1`** atomic **or** composite Claim Scope **without** making a referenced Entity bearer-dependent.

## Test case

create a Current-scope Atom, a parent-owned Goal for a direct child, an Operator-owned Project Goal with no Scope Unit Atom Scope, composite Claim Scopes, **and** one permitted Demand. **then** omit **or** duplicate an Atom Scope component, reorder the same Governed Subject Set, leave a reference unresolved, make a referenced Scope Unit bearer-dependent, **and** use a forbidden Goal **or** Demand target.

## Acceptance criteria

**every** valid fixture resolves **`=1`** Atom Scope **and** **`<=1`** Claim Scope, classifies a fixture with **`=0`** Claim Scope as a Current-scope Atom, classifies a fixture with **`=1`** Claim Scope as a Relational Atom, **and** preserves canonical component equality independent of authored Subject order. **every** invalid fixture fails with the incorrect reference, ownership, Subject set, **or** relational fact identified.

## Failure disposition

record a Concern naming the invalid Atom **and** Scope fact.
