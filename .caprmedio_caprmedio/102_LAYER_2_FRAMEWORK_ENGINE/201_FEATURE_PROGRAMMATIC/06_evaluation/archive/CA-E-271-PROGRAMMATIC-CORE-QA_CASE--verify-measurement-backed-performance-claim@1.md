---
atom_id: CA-E-271
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - performance-measurement
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:12:00 +0400
relations:
  evaluation_for:
    - CA-M-165
  derived_from:
    - CA-A-053
---
# Verify measurement-backed performance claim

## Claim checked

One PROGRAMMATIC performance claim is supported by a representative workload,
preserved baseline, observed distribution, and comparable observation.

## Applicable conditions

Apply when a component proposes or assesses a performance-sensitive change.
No numerical budget is implied where no bounded owner has admitted one.

## Test case

Evaluate one claimed performance change against its selected surface and
recorded baseline.

## Acceptance criteria

Pass only when the workload input, environment, baseline, observed
distribution, and comparison threshold are recoverable and support the stated
claim.

## Failure disposition

Reject the performance claim without a representative baseline; do not invent
a numeric budget.
