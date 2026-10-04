---
atom_id: CA-E-541
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
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

Exercise: an authorized Execute request for one selected operation route and
parameters, with and without optional exact expected revisions; a default
preview; an unselected Tool-shaped request; and a request whose resolved source
digest, permission, or Operator approval changes before dispatch/recovery.

## Acceptance criteria

- Only the valid Execute request creates the actual Run and its `Started`
  evidence with the supplied Initiative and source binding.
- Preview and denied/unselected/stale requests return stable non-start results
  with no fabricated execution record.
- A changed source or context blocks remaining dispatch for revalidation,
  preserves prior effects/bindings, and neither substitutes a newer Version nor
  reuses old approval.

## Details

The fixture records the selected-source registry lookup and the sealed
authorization/currentness comparisons; it does not substitute a mocked route
for the admitted route contract. The checked assertion is the Claim above.

## Failure disposition

Reject an implementation that infers a route, auto-starts from observation,
loses Initiative context, or starts work after currentness/authorization fails.
