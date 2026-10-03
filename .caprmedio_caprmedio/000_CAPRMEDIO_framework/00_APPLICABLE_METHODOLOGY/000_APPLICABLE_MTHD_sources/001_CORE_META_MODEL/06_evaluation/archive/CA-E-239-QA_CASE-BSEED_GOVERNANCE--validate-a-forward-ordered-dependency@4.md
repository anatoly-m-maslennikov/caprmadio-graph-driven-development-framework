---
subject_scopes:
  - relation-model
version: 4
updated_at: 2026-08-22 06:00:00
relations:
  child_of:
    - CA-E-001-PRINCIPLE-EVALUATION--make-accepted-requirements-checkable
    - CA-E-206-EVAL_APPROACH--require-usable-inputs-for-reliance
  evaluation_for:
    - CA-R-878
    - CA-R-885
    - CA-R-914
    - CA-R-915
    - CA-R-916
---
# Validate a forward ordered dependency

## Claim checked

A declared dependency between peer ordered Scope Units flows only from a lower to a higher `local_order`, may skip intermediate units, and is never inferred from order alone.

## Test case

Create three peer ordered Scope Units with Local Orders one, two, and three. Declare that unit three depends on unit one and create a Demand For Atom with Current Scope unit three and Claim Scope unit one. Then reverse each direction, target a peer with the same order, omit the declared dependency, and retain only the units' ordering.

## Acceptance criteria

The declared one-to-three dependency and three-to-one Demand pass. The reverse and same-order cases fail. The absent dependency remains absent, and no dependency is synthesized from ordering alone.

## Failure disposition

Record a Concern naming the invalid edge and stop acceptance of that dependency declaration.
