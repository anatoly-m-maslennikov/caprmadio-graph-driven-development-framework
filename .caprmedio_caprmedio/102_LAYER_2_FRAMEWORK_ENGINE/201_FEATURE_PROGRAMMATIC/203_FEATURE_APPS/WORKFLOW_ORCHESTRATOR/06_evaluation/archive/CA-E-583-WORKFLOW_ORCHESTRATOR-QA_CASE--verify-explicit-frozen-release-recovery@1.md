---
atom_id: CA-E-583
content_role: Evaluation
type: QA Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 17:17:04 +0400"
subjects:
  governs: "Release Version recovery request/evaluation"
  depends_on: [Release Version, Workflow Run, Step Run, Action Run, Operator, Permission, Journal, Source, Queue, DBOS, Implementation]
relations:
  evaluation_for: [CA-R-1883, CA-M-340, CA-D-577]
  relates_to: [CA-E-493, CA-D-574, CA-O-164]
---
# Summary

verify explicit frozen Release recovery

## Scope

the typed recovery admission and continuation boundary for one existing **CA-O-164** Release Workflow Run.

## Claim

the Evaluation **must** verify that Release recovery accepts only the exact frozen Run and preserves canonical Journal identity without replaying uncertain effects or creating extra Run facts.

## Details

- submit a recovery request for an existing interrupted Release Run and verify the sealed request identity, source freshness and current route-bound Operator authorization are required.
- submit a different Run ID, changed request identity, stale source, revoked permission, unknown field or arbitrary continuation payload and verify recovery blocks before an effect, start or terminal Journal event.
- recover one valid sealed pending Action event and verify the shared recorder appends its original bytes and receipt only. Verify changed Run, phase, outcome, result reference or effect reference blocks recovery.
- reopen a completed Workflow and verify it returns its original terminal result with no new Workflow, Step or Action start or terminal event.
- present an unresolved in-progress or uncertain effect and verify recovery returns blocked or pending without native effect replay. Verify queue and DBOS records do not override the canonical Journal.
- observe one queued recovery transport, then its success or failure, and verify the exact returned handle and frozen Run binding are required. Verify the original Run's cached DBOS result is reported only as canonical history, never as the recovery transport result.
