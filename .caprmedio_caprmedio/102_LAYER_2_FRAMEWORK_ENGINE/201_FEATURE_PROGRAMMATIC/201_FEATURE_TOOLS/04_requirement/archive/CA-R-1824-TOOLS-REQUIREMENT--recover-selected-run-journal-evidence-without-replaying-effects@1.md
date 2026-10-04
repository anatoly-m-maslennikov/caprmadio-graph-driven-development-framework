---
atom_id: CA-R-1824
content_role: Requirement
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
  depends_on: [Journal, Workflow Run, Action, Initiative, Implementation]
relations:
  relates_to: [CA-R-812, CA-R-1644, CA-R-1720]
---
# Summary

Recover selected Run Journal evidence without replaying effects

## Scope

Durable append and recovery of selected-Run evidence through the existing
Project Work Journal. It excludes a second execution log or Journal.

## Claim

RUN_SUPPORT **must** use the existing sealed Work Journal append/receipt
boundary for selected-Run evidence, retain failed terminal append evidence, and
retry only the identical pending event without replaying its Action effect.

## Details

- Seal a canonical payload and Event identity before an append attempt. Store
  pending terminal evidence durably in the existing Work Journal runtime state
  with its immutable payload digest, actual result/effect references, append
  diagnostic, and retry linkage; that state is recovery evidence, not another
  historical Journal or derived Process Log.
- Retry recording only with the same Event identity and canonical payload.
  `work_journal.append_sealed_events` must return one existing or newly durable
  receipt for an identical retry. The same Event identity with different bytes
  is an identity collision: retain the pending evidence, report the conflict,
  and never overwrite or mutate accepted history. A later `Recovered` event is
  separately admissible only for independently established facts under
  CA-R-1644 and has its own identity; it never substitutes for or changes the
  original pending terminal event.
- The storage-retry operation cannot invoke an Action executor, dispatch a
  Step, create a Run, reset authorization, or change an effect. A new execution
  attempt needs a separately admitted request under CA-R-1821.
- Artifact Change Log and Process Log are reconstructed views referencing the
  canonical Event identities. A failed append or incomplete view coverage is
  visible; no caller may manufacture a view record, receipt, time, outcome, or
  effect to claim recovery.
