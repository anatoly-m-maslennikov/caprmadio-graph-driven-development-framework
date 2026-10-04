---
atom_id: CA-E-543
content_role: Evaluation
type: QA Case
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
  depends_on: [Workflow Run, Action, Journal, Evaluation]
relations:
  evaluation_for: [CA-R-1823]
---
# Summary

Verify truthful selected Run terminal outcomes

## Scope

Terminal and recording-pending outcome evidence for actual selected Runs.

## Claim

Selected Run outcomes use the admitted Event Type mapping and never hide a
no-op, cancellation, interruption, failed append, or partial effect.

## Test case

Run focused fixtures for successful effect, successful no-op, confirmed
zero-effect failure, actual authorized cancellation, interrupted pending Run,
and a failure with one performed or uncertain effect.

## Acceptance criteria

- Each actual start has one truthful terminal classification when settled, with
  `Completed`, `Failed`, or `Abandoned` event evidence as applicable; an
  interrupted Run remains pending rather than guessed terminal.
- No-op has no invented Artifact mutation. Confirmed zero-effect failure is
  distinct from partial; each partial case retains its known/uncertain effects.
- Cancellation retains an actual reason/effects and is not emitted for an
  unstarted denial. Safe result/effect references and redaction facts remain
  inspectable without secret material.
- A terminal result whose receipt is pending reports `recording_pending`, not
  journaled completion.

## Details

The fixture supplies explicit effect observations for every failure/cancellation
case; absence of an observation is preserved as uncertainty rather than
classified as confirmed zero effect. The checked assertion is the Claim above.

## Failure disposition

Reject invented Event Types, false completion, erased partial effects, or a
terminal assertion lacking its actual evidence and receipt state.
