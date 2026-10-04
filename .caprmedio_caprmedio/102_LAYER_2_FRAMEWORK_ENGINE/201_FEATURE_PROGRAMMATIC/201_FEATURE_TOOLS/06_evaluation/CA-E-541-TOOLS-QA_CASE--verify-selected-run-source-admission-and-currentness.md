---
atom_id: CA-E-541
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 23:03:24 +0400"
subjects:
  governs: "WORKFLOW_OPERATIONS/RUN_SUPPORT/source admission"
  depends_on: [Workflow, Action, Operator, Initiative, Journal, Evaluation]
relations:
  evaluation_for: [CA-R-1821]
---
# Summary

Verify selected Run source admission and currentness

## Scope

The shared RUN_SUPPORT admission boundary for selected operation routes and
their current Operator authorization.

## Claim

RUN_SUPPORT starts only an explicitly selected, current, Operator-authorized
selected Run in its sealed Initiative context.

## Test case

Exercise a golden read-only preview for one selected route with typed
parameters, target frontier, requested effects, a declared current
selected-source binding, and the complete definition-manifest reference/digest.
Then execute it with a freshly issued authorization bound to that exact preview
receipt, request ID, and all four digests. Exercise optional exact expected
definition revisions, an unselected Tool-shaped request, a missing proposal
receipt, an alias mode, and a repeated request ID with changed canonical input.
Between preview and execute, independently change each source registry/binding,
definition manifest, target frontier, effects digest, and authorization
freshness evidence.

## Acceptance criteria

- Default preview is read-only and returns one sealed proposal receipt with the
  request ID plus route, source-freshness, parameters, target-frontier, effects,
  and definition-manifest digests. It has no actual Run ID or Event identity.
- Only literal `execute` with the matching current proposal receipt and
  authorization creates the actual Run IDs and its `Started` evidence with the
  supplied Initiative and admitted bindings. The fixture asserts the returned
  actual IDs, not merely requested IDs.
- Missing, altered, unselected, stale, alias-mode, or request-ID-conflicting
  inputs return stable non-start results with no fabricated execution record or
  effect. A changed source/context blocks dispatch for revalidation, preserves
  prior bindings, and neither substitutes a newer Version nor reuses approval.

## Details

The fixture records the exact selected-source registry and selected-binding
references/versions/digests, complete manifest reference/digest, sealed preview
receipt, authorization bindings, and currentness comparisons. It does not
substitute a mocked route for the admitted route contract. The checked assertion
is the Claim above.

## Failure disposition

Reject an implementation that infers a route, creates a Run/Event for preview,
auto-starts from observation, loses Initiative context, accepts non-`execute`
mutation, or starts after any exact currentness/authorization comparison fails.
