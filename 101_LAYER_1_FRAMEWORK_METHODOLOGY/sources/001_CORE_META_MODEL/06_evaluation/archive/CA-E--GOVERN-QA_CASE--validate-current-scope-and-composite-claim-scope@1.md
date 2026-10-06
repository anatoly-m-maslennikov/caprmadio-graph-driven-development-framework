---
subjects:
  declared:
    continuant:
      - scope-topology
    occurrent:
      - evaluation
  prerequisite:
    continuant:
      - artifact-model
cce_version: cce_1
cce_form: evaluation
version: 1
updated_at: 2026-08-24 15:36:03
relations: {}
---
# Validate Current Scope and composite Claim Scope

## Claim checked

Every Atom has one Current Scope ownership position and one Claim Scope set of governed entities, including when a composite Scope Expression selects that set.

## Test case

Construct Atoms with one Current Scope and Claim Scopes selected by one identity, a parenthesized union, a parenthesized intersection, an exclusion, and a property filter. Then omit or duplicate the Current Scope, leave one Scope Expression unresolved or give it multiple alternative interpretations, remove required grouping, and use each forbidden relational target.

## Acceptance criteria

Every valid fixture resolves one Current Scope position and exactly one Claim Scope set. Every invalid fixture fails with the incorrect ownership, expression, resolution, or relational fact identified.

## Failure disposition

Record a Concern naming the invalid Atom and Scope fact.
