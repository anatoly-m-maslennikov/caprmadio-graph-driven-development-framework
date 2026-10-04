---
atom_id: CA-R-1823
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 22:39:38 +0400"
subjects:
  governs: "WORKFLOW_OPERATIONS/RUN_SUPPORT/outcomes"
  depends_on: [Workflow Run, Step Run, Action, Journal, Operator, Implementation]
relations:
  relates_to: [CA-R-1520, CA-R-1643, CA-R-1720]
---
# Summary

Report truthful selected Run outcomes

## Scope

Lifecycle evidence and caller results for actual selected Runs, including
recording-pending evidence. It does not decide a Workflow's domain result.

## Claim

RUN_SUPPORT **must** expose and persist the actual start, ongoing state, and
one truthful terminal outcome of every actual selected Run without presenting
unpersisted evidence, a no-op, cancellation, or partial effect as completion.

## Details

- Map Journal Event Type exactly as follows: `Started` records an actual start;
  `Progressed` records nonterminal progress or a recording-pending blocker;
  `Completed` records a successful effect or successful no-op; `Failed`
  records a confirmed failed result, including one with partial effects;
  `Abandoned` records an actual authorized cancellation; `Interrupted` retains
  an unsettled actual Run; and `Recovered` records only independently
  established historical facts under CA-R-1644. No new Event Type is created.
- The separate outcome classification is `completed`, `no_op`, `failed`,
  `cancelled`, `partial`, or `interrupted_pending`. It is a truthful result
  field, not a new authority Status. `partial` is required for a failed,
  canceled, or unfinished non-complete execution with any performed or
  uncertain effect. A successful completed effect is `completed`; `failed`
  asserts confirmed zero effect only when that fact is known.
- Terminal evidence retains safe input, result, change/effect, and report
  references, plus redaction facts but never secrets. A no-op retains no
  fictitious Artifact change reference. An actual cancellation retains its
  reason and effects known at cancellation.
- A Run whose terminal fact cannot yet be durably appended remains
  `recording_pending`, with its completed/failed domain result separate from
  its Journal state. It must not be returned as journaled or fully complete.
  An unstarted denial is not a canceled Run.
