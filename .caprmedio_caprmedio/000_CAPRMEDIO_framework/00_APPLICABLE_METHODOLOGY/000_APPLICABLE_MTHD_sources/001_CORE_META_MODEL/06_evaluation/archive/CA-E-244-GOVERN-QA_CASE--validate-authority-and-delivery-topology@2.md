---
atom_id: CA-E-244
cce_version: cce_1
cce_form: evaluation
version: 2
updated_at: 2026-08-22 17:04:18
relations:
  evaluation_for:
    - CA-R-770
    - CA-R-774
    - CA-R-776
    - CA-R-952
    - CA-R-973
    - CA-R-974
---
# Validate authority and Delivery topology

## Claim checked

Authority directories encode structural markers only under `.caprmedio/`, while root Delivery directories encode only optional Layer order and Unit Name.

## Test case

Resolve the three Bootstrap Seed Layer authority directories, six Project Layer authority-to-root pairs, `.caprmedio/FEATURE_FIELD/` to `/FIELD/`, and the three Bootstrap Seed Delivery exceptions. Then add a structural marker to a root Delivery folder, remove one from an authority folder, or replace an exact Unit Name with a readable rendering.

## Acceptance criteria

Only the exact registered authority and Delivery topology passes.

## Failure disposition

Record a Concern naming the mismatched Scope Unit and path.
