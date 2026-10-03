---
atom_id: CA-E-256
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - deterministic-transformation
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:12:00 +0400
relations:
  evaluation_for:
    - CA-M-157
  derived_from:
    - CA-A-053
---
# Verify deterministic transformation from declared inputs

## Claim checked

One declared deterministic PROGRAMMATIC transformation produces its result and
failure values from explicit declared inputs without an implicit host
observation or external effect.

## Applicable conditions

Apply when a component parses, classifies, validates, plans, projects,
formats, or otherwise transforms explicit input into a result.

## Test case

Evaluate one transformation twice with the same declared input while varying
an otherwise irrelevant host observation.

## Acceptance criteria

Pass only when both results and failure values are equivalent and the
transformation reports no filesystem, process, clock, environment, network,
persistence, or logging-export effect.

## Failure disposition

Stop treating the unit as deterministic and assign its missing observation or
effect boundary to the appropriate owner.
