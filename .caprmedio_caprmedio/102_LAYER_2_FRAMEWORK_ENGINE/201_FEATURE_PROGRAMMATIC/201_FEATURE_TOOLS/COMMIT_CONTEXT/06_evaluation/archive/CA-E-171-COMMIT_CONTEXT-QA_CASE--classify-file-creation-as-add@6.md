---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 6
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-804
---
# Classify file creation as ADD

## Claim checked

Creation of one governed file identity is classified only as `ADD`.

## Test case

Supply a trigger whose resulting staged graph contains one new governed file with no matching identity in the committed graph.

## Acceptance criteria

The sealed context reports `ADD`, names the resulting filename and version, and resolves upstream relations from the resulting staged graph.

## Failure disposition

Reject classification and report the observed competing or missing change set.
