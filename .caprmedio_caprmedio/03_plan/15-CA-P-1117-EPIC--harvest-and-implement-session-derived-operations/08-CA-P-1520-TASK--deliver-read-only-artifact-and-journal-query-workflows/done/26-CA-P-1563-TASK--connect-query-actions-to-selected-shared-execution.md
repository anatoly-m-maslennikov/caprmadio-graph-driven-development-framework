---
atom_id: CA-P-1563
content_role: Plan
type: Plan
label: Task
work_sequence_number: 26
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Connect query Actions to selected shared execution"
  depends_on: [Workflow, Action, Implementation, Evaluation, Journal]
version: 2
updated_at: "2026-10-04 23:11:38 +0000"
relations:
  is_decomposition_of: [CA-P-1527]
  blocks: [CA-P-1527, CA-P-1528]
---
# Summary

Connect query Actions to selected shared execution

## Objective

Within <=15 minutes, wire native queries to the existing interpreter and real shared Run lifecycle.

## Details

Inputs: accepted P1547 Tool proof, P1543/P1552 source, current O158-163 and query R/M/E/D. Own query_actions.py, query adapters and necessary pre-Run preparation in selected_execution.py, plus test_selected_query_execution.py. Preserve P1559 compiler handling and all other adapters; root has released its prior ownership. Use the existing native Tools and sole parser, no second executor or Journal serialization. Capture the Journal source in the worker after admission and before its own first Workflow/Action event, using the existing lazy shared session. Retain the opaque process-local capability for stable pages; unknown handles after restart fail truthfully without recapture or caller-record trust. Artifact queries use their actual retained source snapshots. Return native diagnostics/default IDs/selected fetch and record actual Workflow/Step/Action results only for admitted execution. Preview and denied input create no Run, event or effects. Prove real shared recorder lineage, own-event/later-append exclusion, invalid filters, read-only/secret boundaries and continuation tampering. If standalone Action or durable restart support lacks admitted source, report the precise remainder rather than inventing it. Do not edit manifest, MCP, backend, source, Query Tool internals or the golden fixture owned by P1562.

You are not alone; preserve others and use apply_patch. Inherit 90% and mechanical Git exception. Root saves Plans/commits. No FPF, harvesting, source-gap expansion or permission bypass.

## Definition of Done

Native query execution uses one admitted shared Run path and stable pre-own-event snapshots; unproved transport/image/restart cases are stated explicitly.

## Result

query_actions.py and the existing selected executor invoke the two actual native Tools with the closed `parameters.query_request` carrier. The Journal source is captured after admission and before the first real shared Run start; continuation consumes the exact process-local opaque handle and fails after restart without recapture. Source-bound success labels follow the current graph. Five focused shared-recorder tests passed, including genuine Workflow/Step/Action lineage, pre-own-event/later-append exclusion, invalid diagnostics, selected Artifact fields and continuation tamper/restart refusals. The native Journal/Artifact/parser suites passed 37/37. The selected regression suite passed 19/20, with its sole obsolete thirteen-route assertion assigned to P1569. No separate standalone Action dispatcher, complete fifteen-route queue/MCP result or immutable-image proof is claimed; those retain their own gates.
