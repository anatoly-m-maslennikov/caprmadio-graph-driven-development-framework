---
atom_id: CA-D-577
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 18:00:00 +0400"
subjects:
  governs: "Release Version recovery request/Carrier"
  depends_on: [Carrier, Release Version, Workflow Run, Operator, Permission, Journal, Queue, DBOS, Implementation]
relations:
  delivery_for: [CA-R-1883, CA-M-340, CA-O-164]
  relates_to: [CA-D-521, CA-D-574]
---
# Summary

carry typed Release recovery requests

## Scope

the WORKFLOW_ORCHESTRATOR request and retained-state Carriers for recovering one frozen **Release Version** Workflow Run.

## Claim

the Release recovery request Carrier **must** contain only the typed operation, existing Run ID and sealed request identity needed to reopen an existing frozen Release Run.

## Details

- request schema: `operation: recover_selected_release`, `run_id` and `request_identity`. No arbitrary execution object, definition selection, Action payload, source path, permission grant, executor choice or effect instruction is admitted.
- the request is retained with the existing frozen selected request, dispatch intent, typed Release checkpoint, Action progress and result references in that Run's configured orchestrator state directory.
- canonical Workflow, Step and Action starts, recovered pending events, effects and terminal facts remain schema-v5 Work Journal records. The request Carrier, queue and DBOS state are transport and observation records, not a second Run Journal.
- the request response reports the same Run ID, operation disposition, canonical Journal references and blocked or pending reason where applicable. It does not claim a new Run, completion or recovered effect without exact canonical evidence.
- a separate read-only observation Carrier contains only `operation: recover_selected_release_status`, the same existing `run_id` and one returned recovery transport handle. It reads that exact DBOS handle and verifies its Release-recovery workflow binding and frozen Run identity; it neither queues, starts nor records a Run. Canonical Journal state remains separately reported and no prior canonical scheduler result is presented as recovery output.
