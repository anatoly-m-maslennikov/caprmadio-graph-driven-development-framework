---
atom_id: CA-C-503
content_role: Concern
type: Problem
current_scope_unit: PROMPTS
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 17:23:10 +0000"
subjects:
  governs: "Require preparation Evaluation authority"
  depends_on: [Implementation, Evaluation, Action, Workflow Run, Journal]
relations:
  concern_about: [CA-P-1797, CA-P-1794, CA-P-1655]
---
# Summary

Require preparation Evaluation authority

## Concern

Implementation preparation can admit a missing, stale or wrong-role Evaluation binding before agent dispatch.

## Evidences

the final source-to-code review confirmed this bounded discrepancy. independent adjudication separated it from unsupported status-transition and authorization-model proposals. focused fixture results establish repair behavior, not actual release completion.

## Blast radius

the affected selected capability and its current release candidate. installed N, historical Events and frozen test snapshots remain preserved.

## Decision

require the bound Evaluation at preparation and test missing, stale and wrong-role bindings before any agent call.

## Result

the preparation test rejects missing, stale and wrong-role Evaluation bindings before dispatch. the focused prompt-contract suite passes 20 tests and selected-project-binding suite passes seven; independent review accepts the repair. this resolves the bounded code discrepancy; it is not evidence of actual release promotion.
