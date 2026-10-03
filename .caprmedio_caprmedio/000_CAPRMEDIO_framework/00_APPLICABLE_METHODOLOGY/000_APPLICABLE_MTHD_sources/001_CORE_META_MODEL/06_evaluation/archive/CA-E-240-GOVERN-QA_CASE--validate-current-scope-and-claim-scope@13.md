---
subjects:
  governs:
    occurrent:
      - Scope Reference Validation
  depends_on:
    continuant:
      - Atom/Current Scope
      - Atom/Current Scope/Owner
      - Atom/Current Scope/Governed Subject Set
      - Atom/Claim Scope
      - Atom/Claim Scope/Scope Unit Set
atom_id: CA-E-240
cce_version: cce_1
cce_form: evaluation
version: 13
updated_at: 2026-09-02 03:30:00 +0400
relations: {}
---
# Validate Current Scope and Claim Scope

## Claim checked

**every** Atom resolves **`=1`** Current Scope with **`=1`** Current Scope Owner **and** **`=1`** Governed Subject Set, **and** one atomic **or** composite Claim Scope with **`=1`** Claim Scope Unit Set, **without** making a referenced Entity bearer-dependent.

## Test case

create a Current-scope Atom, a parent-owned establishing Goal for a direct child, an Operator-owned Project Goal with no Scope Unit Current Scope Owner, a subsequent Goal, composite Claim Scopes, **and** one permitted Demand. **then** omit **or** duplicate a Current Scope component, reorder the same Governed Subject Set, leave a reference unresolved, make a referenced Scope Unit bearer-dependent, separate Goal admission from Scope Unit establishment, recreate an established Scope Unit, **and** use a forbidden Goal **or** Demand target.

## Acceptance criteria

**every** valid fixture resolves **`=1`** Current Scope, **`=1`** Claim Scope, **and** canonical component equality independent of authored Subject order. **every** invalid fixture fails with the incorrect reference, ownership, Subject set, establishment, **or** relational fact identified.

## Failure disposition

record a Concern naming the invalid Atom **and** Scope fact.
