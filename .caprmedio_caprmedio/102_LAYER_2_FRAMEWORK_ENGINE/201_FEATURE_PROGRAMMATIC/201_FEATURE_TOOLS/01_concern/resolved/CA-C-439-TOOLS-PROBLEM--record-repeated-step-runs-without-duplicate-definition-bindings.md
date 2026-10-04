---
atom_id: CA-C-439
content_role: Concern
type: Problem
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 22:18:37 +0000"
subjects:
  governs: "Repeated Step Run definition binding recording"
  depends_on: [Workflow, Step, Action, Run, Journal]
relations:
  concern_about: [CA-P-1540, CA-P-1541, CA-P-1517]
---
# Summary

Record repeated Step Runs without duplicate definition bindings

## Concern

CA-P-1540's real shared-session authorized-loop test fails before its handler. Its distinct predeclared revisit Run identities repeat the same current definition Revision, while RunExecutionSession._bindings_for includes one definition binding per requested Run. The canonical Journal correctly rejects those duplicated definition bindings.

## Evidences

The worker reports 18 passing and 1 failing test in test_selected_execution.py; the failure is test_shared_session_authorized_loop_uses_distinct_predeclared_visit_ids. The source recorder constructs Workflow bindings from every requested Run without canonical deduplication.

## Blast radius

Authorized retry/revisit execution could not start truthfully through the shared Journal. CA-P-1541 now deduplicates exact definition revisions while retaining distinct Run identities and lineage, rejecting conflicting pins before dispatch. Root verified 20 selected-execution, 7 shared-Run, 4 schema-v5 and 2 repeat-binding tests, all passing. No Journal schema or permission relaxation was used. This recorded defect is resolved; aggregate image/MCP proof remains separate.
