---
atom_id: CA-P-1615
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Resolve and implement whitelisted Atom status changes"
  depends_on: [Atom, Content Role, Status, Carrier, Workflow, Action, Tool, Journal]
version: 2
updated_at: "2026-10-05 02:37:23 +0000"
relations:
  is_decomposition_of: [CA-P-1612]
  blocks: [CA-P-1616]
---
# Summary

Resolve and implement whitelisted Atom status changes

## Objective

Within <=15 minutes, implement the accepted current-status/folder resolver and necessary extensions through the existing generic status Action, Tool, MCP and orchestrator path. Start from a golden E2E corpus and preserve concurrent external lifecycle edits.

## Details

### Inputs

CA-P-1614 and CA-P-1633 accepted complete source pins; current change_status_atom_action and selected route; current parser/model sources and shared Run support. Freeze resolved inputs for admitted execution.

### Bounded decomposition

CA-P-1634 implements the pure source-derived resolver; CA-P-1635 authors its test-first golden corpus; CA-P-1636 binds exact integration touchpoints. These independent leaves can run in parallel. All three block CA-P-1637, which integrates the existing Action/Tool/MCP/orchestrator path and required carrier effects. CA-P-1638 independently reviews complete integration evidence. Completing only the pure helper or source review does not complete this parent. Every leaf is bounded to <=15 minutes and preserves external edits; split unfinished work rather than overstating completion.

### Output and ownership

The existing input Atom/requested Status resolves the current role/type model without caller-invented whitelist authority. The admitted status change moves the complete Carrier to its defined folder, updates metadata, preserves required history and reports no-op/error/reference results. No second implementation or Journal writer.

## Definition of Done

Golden cases cover every declared role and its statuses, specialized models, Draft references, same-status no-op, invalid/missing model, undefined folder, collisions and archival/non-archive movement. Retain actual shared Workflow/Action records. Decompose further if the bound work exceeds15 minutes; no stale-worker/image proof substitution.
