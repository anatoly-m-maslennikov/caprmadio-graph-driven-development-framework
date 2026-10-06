---
atom_id: CA-E-239
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Ordered Dependency Validation
  depends_on:
    continuant:
      - Ordered Dependency
      - Scope Unit/Order
version: 11
updated_at: 2026-09-04 23:11:19 +0400
relations:
  evaluation_for:
    - CA-R-878
    - CA-R-885
---
# Validate a Forward Ordered Dependency

## Claim checked

an ordered dependency flows from an earlier Producer to a later Consumer, **and** the stored relation points from Consumer to Producer.

## Test case

Create three ordered peer Scope Units. Declare the first as Producer **and** the third as Consumer. Store `depends_on` from the third to the first. Reverse the production flow, reverse the stored relation, use equal order, **and** omit the dependency **in** separate fixtures.

## Acceptance criteria

**only** the earlier-Producer, later-Consumer fixture with the Consumer-to-Producer stored relation passes. Order alone creates no dependency.

## Failure disposition

Record a Concern naming the invalid ordered dependency.
