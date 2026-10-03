---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - framework-engine-mcp
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-30 16:44:07 +0400
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
