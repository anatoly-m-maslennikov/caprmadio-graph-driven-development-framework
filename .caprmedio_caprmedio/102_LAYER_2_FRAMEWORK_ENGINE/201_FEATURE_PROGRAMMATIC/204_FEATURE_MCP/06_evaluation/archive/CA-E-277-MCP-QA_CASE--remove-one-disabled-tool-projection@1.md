---
atom_id: CA-E-277
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - framework-engine-mcp
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:40:00 +0400
relations:
  evaluation_for:
    - CA-M-171
  derived_from:
    - CA-A-057
---
# Remove one disabled Tool projection

## Claim checked

Registry reconciliation removes a projection whose source Tool is disabled.

## Test case

Disable one previously exposed current Tool and regenerate the registry.

## Acceptance criteria

The resulting complete registry excludes that Tool and retains every other eligible current source.

## Failure disposition

Stop when a stale or independently allowlisted projection remains.
