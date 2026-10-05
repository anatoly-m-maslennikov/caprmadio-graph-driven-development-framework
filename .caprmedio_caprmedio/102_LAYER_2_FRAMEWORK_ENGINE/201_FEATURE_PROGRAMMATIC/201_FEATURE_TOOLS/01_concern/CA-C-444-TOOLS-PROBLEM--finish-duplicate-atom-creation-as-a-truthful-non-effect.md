---
atom_id: CA-C-444
content_role: Concern
type: Problem
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Duplicate Atom Creation Run Completion"
  depends_on: [Atom, Workflow, Run, Journal]
version: 1
updated_at: 2026-10-04 22:40:40
relations: {concern_about: [CA-O-127, CA-O-129, CA-O-128]}
---
# Summary

Finish duplicate Atom creation as a truthful non-effect

## Concern

The selected Create Atom workflow does not finish cleanly after a deterministic Atom ID collision. Its native adapter reports duplicate with an unchanged effect, but shared Run support returns disposition started with execution_error SelectedRunError and interrupted_pending Workflow and Step outcomes. A proven non-effect must not be represented as uncertain mutation or successful creation.

## Evidences

Run storage-i-ca-c-440-20261005-v1 collided with another session's already admitted CA-C-440. Its saved Action result is no-op, native_result.outcome is duplicate, and the effect reason is atom-id-collision with state unchanged. Its accepted.json contains execution_error SelectedRunError, and the Workflow and Step terminal records are interrupted_pending. The existing Concern was not overwritten; the intended legacy-consumer Concern was resubmitted under a fresh identity.

## Blast radius

Concurrent sessions can encounter ordinary identity-allocation collisions. The native refusal protects authority, but the shared lifecycle result path needs a bounded functional test and repair so deterministic duplicates finish with truthful non-effect records. Retain existing Journal and receipt history; do not replay the old request or weaken identity uniqueness checks.
