---
subjects:
  - relation-model
  - evaluation
  - atom-boundary
atom_id: CA-E-239
cce_version: cce_1
cce_form: evaluation
version: 6
updated_at: 2026-08-23 01:44:00
relations:
  evaluation_for:
    - CA-R-878
    - CA-R-885
---
# Validate a forward ordered dependency

## Claim checked

An ordered dependency flows from an earlier Producer to a later Consumer, and the stored relation points from Consumer to Producer.

## Test case

Create three ordered peer Scope Units. Declare the first as Producer and the third as Consumer. Store `depends_on` from the third to the first. Reverse the production flow, reverse the stored relation, use equal order, and omit the dependency in separate fixtures.

## Acceptance criteria

Only the earlier-Producer, later-Consumer fixture with the Consumer-to-Producer stored relation passes. Order alone creates no dependency.

## Failure disposition

Record a Concern naming the invalid ordered dependency.
