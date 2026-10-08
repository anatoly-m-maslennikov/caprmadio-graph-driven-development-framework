---
atom_id: CA-C-501
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
  governs: "Repair graph limitation terminals"
  depends_on: [Implementation, Evaluation, Action, Workflow Run, Journal]
relations:
  concern_about: [CA-P-1795, CA-P-1794, CA-P-1655]
---
# Summary

Repair graph limitation terminals

## Concern

graph-build native stale, incomplete and conflicting outcomes can escape the selected graph transition table or imply a completed Action.

## Evidences

the final source-to-code review confirmed this bounded discrepancy. independent adjudication separated it from unsupported status-transition and authorization-model proposals. focused fixture results establish repair behavior, not actual release completion.

## Blast radius

the affected selected capability and its current release candidate. installed N, historical Events and frozen test snapshots remain preserved.

## Decision

map native limitations to interrupted pending terminal results, retain native evidence and verify both graph routes with real recorder fixtures.

## Result

both graph routes pass the three limitation outcomes: one regression with six subcases. the independent review accepts the truthful interrupted-pending terminal mapping and retained native evidence. this resolves the bounded code discrepancy; it is not evidence of actual release promotion.
