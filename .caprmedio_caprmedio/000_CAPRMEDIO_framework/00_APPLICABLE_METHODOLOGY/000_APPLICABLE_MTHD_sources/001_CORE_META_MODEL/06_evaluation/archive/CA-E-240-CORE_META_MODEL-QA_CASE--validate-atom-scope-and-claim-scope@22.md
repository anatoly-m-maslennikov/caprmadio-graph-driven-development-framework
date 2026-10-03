---
subjects:
  governs: "Scope Reference Validation"
  depends_on:
    - "Atom/Scope"
    - "Atom/Governed Subject"
    - "Atom/Claim/Scope"
    - "Atom/Claim/Scope/Scope Unit Set"
    - "Structural Parent Relation"
    - "Subject"
cce_version: cce_1
cce_form: evaluation
version: 22
updated_at: "2026-09-13 02:05:21 +0400"
relations:
  evaluation_for:
    - CA-R-1014
    - CA-R-920
    - CA-R-919
    - CA-R-1363
    - CA-R-1201
    - CA-R-923
    - CA-R-947
    - CA-R-944
    - CA-R-946
    - CA-D-269
    - CA-D-367
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Atom Scope and Claim Scope

## Claim checked

**every** Atom resolves **`=1`** Atom Scope, **`=1`** Atom Governed Subject, **and** **`=1`** resolved atomic **or** composite Claim Scope **without** making a referenced Subject bearer-dependent.

## Test case

create a Current-scope Atom, a parent-owned Goal for a direct child, an Operator-owned Project Goal with no Scope Unit Atom Scope, composite Claim Scopes, **and** one permitted Demand. **then** omit **or** duplicate an Atom Scope component **or** GOVERNS Subject, reorder dependency references alongside **`=1`** GOVERNS Subject **and** prerequisite DEPENDS_ON Subjects **without** changing their canonical target identities **or** direct Relation Kinds, leave a reference unresolved, make a referenced Scope Unit bearer-dependent, **and** use a forbidden Goal **or** Demand target.

## Acceptance criteria

**every** valid fixture resolves **`=1`** Atom Scope **and** **`=1`** Claim Scope, resolves an omitted Claim Scope representation **to** the current Scope for a Current-scope Atom, classifies an explicitly represented different Claim Scope as a Relational Atom, **and** preserves canonical component equality independent of authored Subject order. **every** invalid fixture fails with the incorrect reference, ownership, Subject declaration, **or** relational fact identified.

## Failure disposition

record a Concern naming the invalid Atom **and** Scope fact.
