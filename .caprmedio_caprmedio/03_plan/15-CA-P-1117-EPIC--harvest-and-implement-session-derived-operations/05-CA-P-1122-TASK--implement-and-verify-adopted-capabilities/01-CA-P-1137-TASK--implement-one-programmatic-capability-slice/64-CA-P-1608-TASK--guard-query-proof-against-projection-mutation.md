---
atom_id: CA-P-1608
content_role: Plan
type: Plan
label: Task
work_sequence_number: 64
current_scope_unit: caprmedio
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Guard query proof against Projection mutation"
  depends_on: [Tool, Workflow, Action, MCP, Evaluation, Projection]
version: 1
updated_at: "2026-10-05 00:52:31 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1527, CA-P-1528]
---
# Summary

Guard query proof against Projection mutation

## Objective

Within <=15 minutes, repair the prepared query-specific MCP proof so preview, execution and refusal checks detect creation, removal or modification of canonical Project Projections. Own test_selected_query_mcp_e2e.py and its focused mock/source tests only.

## Details

One independently owned Task. Preserve concurrent edits. Root saves the truthful result and validated mechanical commit. C447 and C449 remain distinct protected blockers. No FPF, harvesting, denied-operation retry or broad audit.

## Definition of Done

A deterministic source test detects Projection mutation; candidate bytes and independent source review are recorded. Actual-image cases remain unexecuted under C449, with no substituted runner or permission bypass.

## Result

Done: query-specific Projection fingerprints cover absent/empty roots, directories and regular-file bytes; preview, complete execution and refusal paths compare them. Three focused source tests pass, including a mock silent Projection publication that former source/recorder snapshots would miss. Four image methods remain intentionally unexecuted under C449.

Independent source-only reviewer ACCEPTED saved test_selected_query_mcp_e2e.py, 22529 bytes, SHA256 6475546d81cc4817f0d5bc356d038f22ab142594b4eb83ac9e56f938e6246663. No Tool behavior, host environment, image execution or Journal fact was changed by this repair.
