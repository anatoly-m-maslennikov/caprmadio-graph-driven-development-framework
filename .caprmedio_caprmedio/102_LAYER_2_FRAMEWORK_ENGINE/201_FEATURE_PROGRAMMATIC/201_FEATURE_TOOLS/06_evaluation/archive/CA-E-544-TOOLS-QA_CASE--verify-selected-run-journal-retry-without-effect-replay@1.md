---
atom_id: CA-E-544
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
  governs: "WORKFLOW_OPERATIONS/RUN_SUPPORT/journal recovery"
  depends_on: [Journal, Action, Workflow Run, Evaluation]
relations:
  evaluation_for: [CA-R-1824]
---
# Summary

Verify selected Run Journal retry without effect replay

## Scope

Storage recovery of a terminal selected-Run event after its domain effect has
already occurred.

## Claim

An append failure retains identical pending evidence and a retry appends once
without rerunning its completed Action.

## Test case

Inject a terminal append failure after one Action effect. Capture its sealed
payload, effect counter, pending carrier, and Journal. Retry first with the
identical event and then with changed bytes under the same Event identity.

## Acceptance criteria

- Failure leaves the canonical Journal unchanged, retains one durable pending
  payload with diagnostic/effect references, and reports recording pending.
- The identical retry produces exactly one receipt/event, clears or reconciles
  the pending state, and leaves the effect counter unchanged.
- The conflicting retry fails without overwriting Journal bytes, receipt, or
  pending original. No recovery path invokes the Action executor or resets
  authorization. A separately admissible recovery Event retains a distinct
  identity and cannot replace the original terminal payload.
- Derived log views expose incomplete coverage before durable append and one
  canonical event after it.

## Details

Fault injection occurs at the append boundary only. The Action effect counter
and sealed pending bytes remain independent observations throughout recovery.
The checked assertion is the Claim above.

## Failure disposition

Reject duplicate appends, lost pending evidence, byte overwrite, invented
recovery facts, or any Action replay caused by storage recovery.
