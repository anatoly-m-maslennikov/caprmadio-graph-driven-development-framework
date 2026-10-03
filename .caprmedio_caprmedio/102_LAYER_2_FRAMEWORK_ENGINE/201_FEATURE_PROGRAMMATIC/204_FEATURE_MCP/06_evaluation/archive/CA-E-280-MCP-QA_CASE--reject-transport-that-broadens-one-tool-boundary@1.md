---
atom_id: CA-E-280
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
    - CA-M-174
  derived_from:
    - CA-A-057
---
# Reject transport that broadens one Tool boundary

## Claim checked

MCP cannot alter a canonical Tool's authority, cardinality, failure, or side-effect boundary.

## Test case

Forward one Atom Doer request while attempting to substitute a broader target set or success for a partial Tool outcome.

## Acceptance criteria

The request is rejected or the exact Tool outcome is retained; no broader or fabricated success crosses the boundary.

## Failure disposition

Stop the invocation and record the attempted semantic alteration.
