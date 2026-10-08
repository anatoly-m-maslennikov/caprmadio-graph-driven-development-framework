---
atom_id: CA-C-502
content_role: Concern
type: Problem
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 17:23:10 +0000"
subjects:
  governs: "Stop on pending Action recording"
  depends_on: [Implementation, Evaluation, Action, Workflow Run, Journal]
relations:
  concern_about: [CA-P-1796, CA-P-1794, CA-P-1655]
---
# Summary

Stop on pending Action recording

## Concern

a structural Workflow can advance after its Action terminal Journal append failed, exposing the next mutation without durable evidence.

## Evidences

the final source-to-code review confirmed this bounded discrepancy. independent adjudication separated it from unsupported status-transition and authorization-model proposals. focused fixture results establish repair behavior, not actual release completion.

## Blast radius

the affected selected capability and its current release candidate. installed N, historical Events and frozen test snapshots remain preserved.

## Decision

stop before any following Action or transition when the actual terminal recorder returns recording_pending; preserve recording-only recovery.

## Result

the structural receipt regression passes four injected pre-cutover terminal-append failures. no following mutation or effect replay occurs; the independent review accepts the common pending-receipt stop gate. this resolves the bounded code discrepancy; it is not evidence of actual release promotion.
