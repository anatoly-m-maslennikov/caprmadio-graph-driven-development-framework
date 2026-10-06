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
atom_id: CA-E-240
cce_version: cce_1
cce_form: evaluation
version: 8
updated_at: 2026-08-26 15:38:45 +0400
relations:
  evaluation_for:
    - CA-R-877
    - CA-R-947
    - CA-R-950
---
# Validate Current Scope and Claim Scope

## Claim checked

Every Atom has one Current Scope ownership position and one Claim Scope interpreted under its Atom Type.

## Test case

Construct one Current-scope Atom, one parent-owned Job for a direct child, one external Project Job, and one permitted Demand. Then omit, duplicate, or misplace each Scope and try forbidden ancestor, descendant, and non-direct Job targets.

## Acceptance criteria

Every valid fixture resolves exactly one Current Scope position and one Claim Scope. Every invalid fixture fails with the incorrect Scope fact identified.

## Failure disposition

Record a Concern naming the invalid Atom and Scope fact.
