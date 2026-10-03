---
subjects:
  governs: "Atom/Claim/Target Scope"
  depends_on:
    - "Atom/Scope"
    - "Atom/Claim/Target Scope"
    - "Atom/Governed Subject"
    - "Current-scope Atom"
    - "Relational Atom"
    - "Scope Unit"
cce_version: cce_1
cce_form: evaluation
version: 1
updated_at: "2026-09-15 23:56:42 +0400"
relations:
  evaluation_for:
    - CA-R-718
    - CA-R-919
    - CA-R-922
    - CA-R-923
    - CA-R-1271
    - CA-R-1364
    - CA-R-1446
    - CA-D-367
---
# Validate Claim Target Scope Semantics

## Claim checked

**every** Atom Claim resolves **`=1`** atomic **or** composite Claim Target Scope independently of Atom ownership **and** Subject identity.

## Test case

create a Current-scope Atom with omitted Claim Target Scope representation, a Relational Atom with an explicit different target, an Atom with one composite Target Scope, a parent-owned Goal targeting its direct child Scope Unit, **and** an admitted Atom without a containing Scope Unit and with an explicit target. **then** omit a required nondefault target, provide two target values, leave a target unresolved, substitute the Atom's owner **or** Governed Subject for its target, **or** create a Scope Unit tree edge from targeting alone.

## Acceptance criteria

**every** valid fixture resolves **`=1`** Claim Target Scope; the omitted representation resolves **to** the current Scope Unit without losing semantic value, the explicit different target yields a Relational Atom, **and** no target changes ownership **or** Scope Unit ancestry. **every** invalid fixture fails with the affected Atom **and** unresolved, duplicate, substituted, **or** structurally misused target identified.

## Failure disposition

record a Concern naming the invalid Atom **and** Claim Target Scope fact.
