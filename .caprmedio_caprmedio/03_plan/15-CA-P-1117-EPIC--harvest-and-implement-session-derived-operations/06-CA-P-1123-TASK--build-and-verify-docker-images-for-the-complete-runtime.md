---
atom_id: CA-P-1123
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Session-derived operational capability delivery"
  depends_on:
    - "Operations"
    - "Implementation"
version: 2
updated_at: "2026-10-04 15:51:44 +0000"
relations:
  is_decomposition_of:
    - CA-P-1117
  blocks:
    - CA-P-1173
    - CA-P-1124
    - CA-P-1147
---
# Summary

Build and verify Docker images for the complete runtime

## Objective

Build and functionally verify Docker images for the thirteen selected Workflows in CA-P-1117 v3 and every Action, Tool, prompt, MCP interface and runtime dependency they actually use, including reused implementations. The Operator's scope amendment excludes container-testing unrelated existing Tools and harvested capabilities.

Exercise image-based mutation and no-op paths on controlled mock Projects, the Implementation Workflow, Revert, all three Projection builders, and Workflow/Action Journal persistence and recovery. Keep image identity, Run/Action IDs and result evidence. A successful image build or host-only test is insufficient. Runtime Project-data mounts are allowed; undeclared host implementation mounts and baked secrets are not.

### Work decomposition

This is a composite task, not a fifteen-minute executable leaf. Its initial child files partition the work; add more <=15-minute one-file subtasks for remaining evidence, capability slices, reviews or failures. Roll-up effort depends on the frozen inventory. Inherit CA-P-1117 execution controls and its autonomous-confidence threshold; do not copy or override inherited values.

Before marking this task Done, verify full-stage coverage and update the next dependent task(s) from actual results. A blocked child remains unfinished, has a C/Problem, and does not authorize bypassing this parent's gate.

## Details

### Definition of Done

This Plan is not Done if any selected Workflow or required support/MCP path is absent from the scoped inventory, lacks passing image-based functional and Journal evidence, or requires undeclared host implementation code/dependencies. All three Projection builders, Revert and the Implementation Workflow need actual runtime evidence, not a build-only claim. Required verification/review/repair leaves must be Done; unrelated runtime inventory is excluded.
