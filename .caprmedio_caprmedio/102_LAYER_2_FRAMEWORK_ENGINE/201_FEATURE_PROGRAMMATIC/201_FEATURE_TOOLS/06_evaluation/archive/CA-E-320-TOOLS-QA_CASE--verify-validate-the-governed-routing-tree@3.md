---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  evaluation_for:
    - CA-M-202
---
# Verify validate the governed routing tree

## Claim checked

CA-M-202 deterministically blocks routing whenever the governed routing tree violates a declared structural constraint.

## Applicable when

Apply before any changed routing-tree authority is used for route selection.

## Test case

Start with one valid routing tree, then introduce in the same fixture an unreachable leaf, a prohibited cycle, an ambiguous root, an unresolved target, and an incomplete fallback. Validate twice without changing inputs.

## Acceptance criteria

The valid tree permits routing; the invalid tree blocks it and emits exactly one stable attributable issue for each introduced violation; repeated validation preserves issue identity and order.

## Failure disposition

Reject the validator and preserve the routing frontier, declared constraints, expected violations, observed issues, verdict, and repeat-run comparison.
