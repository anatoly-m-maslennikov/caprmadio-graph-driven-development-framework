---
atom_id: CA-E-267
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - operational-diagnostic
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:12:00 +0400
relations:
  evaluation_for:
    - CA-M-163
  derived_from:
    - CA-A-053
---
# Verify structured diagnostic schema

## Claim checked

One PROGRAMMATIC operational diagnostic uses an admitted severity and provides
the actionable contextual fields required by its declared schema.

## Applicable conditions

Apply when a component emits a diagnostic for normal operation, degraded
operation, failure, recovery, or diagnostic detail.

## Test case

Evaluate one emitted diagnostic record for a declared component event.

## Acceptance criteria

Pass only when the record uses ERROR, WARNING, INFO, or DEBUG, includes its
declared actionable contextual fields, and does not repurpose Journal history
as an operational diagnostic.

## Failure disposition

Reject the diagnostic path until its schema and severity are corrected.
