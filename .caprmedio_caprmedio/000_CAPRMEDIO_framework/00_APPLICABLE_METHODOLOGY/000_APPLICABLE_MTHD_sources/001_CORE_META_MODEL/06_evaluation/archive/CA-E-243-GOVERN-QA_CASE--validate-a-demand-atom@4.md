---
subjects:
  - relation-model
  - artifact-model
  - evaluation
  - atom-boundary
atom_id: CA-E-243
cce_version: cce_1
cce_form: evaluation
version: 4
updated_at: 2026-08-23 01:44:00
relations:
  evaluation_for:
    - CA-R-950
    - CA-R-951
    - CA-R-954
    - CA-R-955
---
# Validate a Demand Atom

## Claim checked

A Demand is owned by a Consumer, targets a permitted Producer Scope, depends on that Producer, and constrains one exact Implementation result only.

## Test case

Construct one valid Demand across separate branches. Then remove its dependency, target an ancestor or descendant, target two results, target a non-Implementation result, and constrain Producer authority outside the selected result.

## Acceptance criteria

Only the fixture with one exact dependency and one exact Implementation result passes.

## Failure disposition

Record a Concern naming the invalid Demand fact.
