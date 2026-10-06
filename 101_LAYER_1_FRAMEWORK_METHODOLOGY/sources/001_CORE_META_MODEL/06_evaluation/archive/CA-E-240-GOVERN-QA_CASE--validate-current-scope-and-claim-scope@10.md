---
subjects:
  governs:
    occurrent:
      - Scope Reference Validation
  depends_on:
    continuant:
      - Atom/Current Scope
      - Atom/Claim Scope
atom_id: CA-E-240
cce_version: cce_1
cce_form: evaluation
version: 10
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Validate Current Scope and Claim Scope

## Claim checked

**every** Atom resolves one Current Scope reference **and** one atomic **or** composite Claim Scope **without** making a referenced Entity bearer-dependent.

## Test case

create a Current-scope Atom, a parent-owned establishing Job for a direct child, an Operator-owned Project Job with empty Current Scope, a subsequent Job, composite Claim Scopes, **and** one permitted Demand. **then** omit **or** duplicate **every** Scope, leave a reference unresolved, make a referenced Scope Unit bearer-dependent, separate Job admission from Scope Unit establishment, recreate an established Scope Unit, **and** use a forbidden Job **or** Demand target.

## Acceptance criteria

**every** valid fixture resolves **`=1`** Current Scope **and** one Claim Scope. **every** invalid fixture fails with the incorrect reference, ownership, establishment, **or** relational fact identified.

## Failure disposition

record a Concern naming the invalid Atom **and** Scope fact.
