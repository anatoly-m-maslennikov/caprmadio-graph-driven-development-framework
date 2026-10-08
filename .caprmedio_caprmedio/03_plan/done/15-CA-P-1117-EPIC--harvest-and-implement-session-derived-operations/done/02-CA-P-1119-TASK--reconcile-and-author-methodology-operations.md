---
atom_id: CA-P-1119
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: METHODOLOGY_SOURCES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Session-derived operational capability delivery"
  depends_on:
    - "Operations"
    - "Implementation"
version: 4
updated_at: "2026-10-04 18:16:52 +0000"
relations:
  is_decomposition_of:
    - CA-P-1117
  blocks:
    - CA-P-1158
    - CA-P-1160
    - CA-P-1120
    - CA-P-1121
    - CA-P-1133
    - CA-P-1135
---
# Summary

Reconcile and author methodology operations

## Objective

Bind the thirteen Workflows selected in CA-P-1117 v3 to existing source Operations; author only missing or incorrect definitions and required Actions, then obtain independent source review. Reusable Operations belong to CORE_META_MODEL and caprmedio-specific Operations to PROJECT_CONFIGURATION. Both are authoritative sources, not the derived Applicable Methodology.

Use retained evidence only where directly relevant to those selected Workflows. No further harvesting, all-candidate reconciliation, or delivery of the five extra authored assessment Actions is required. Define Workflow/Action Run journaling and the three main Projection Workflows as part of this source scope.

CA-P-1130's completed reconciliation remains retained history. CA-P-1131 and its legacy closure are excluded from this stage's required decomposition by the Operator's scope amendment; no failed directory move is bypassed or reported repaired. CA-P-1132 / CA-P-1157 must bind the selected source frontier instead. Create bounded authoring leaves only for actual source gaps, and retain independent review before dependent RMED execution.

### Work decomposition

This is a composite task, not a fifteen-minute executable leaf. Its initial child files partition the work; add more <=15-minute one-file subtasks for remaining evidence, capability slices, reviews or failures. Roll-up effort depends on the frozen inventory. Inherit CA-P-1117 execution controls and its autonomous-confidence threshold; do not copy or override inherited values.

Before marking this task Done, verify full-stage coverage and update the next dependent task(s) from actual results. A blocked child remains unfinished, has a C/Problem, and does not authorize bypassing this parent's gate.

## Details

### Source-stage acceptance

P1132 is accepted and Done after all required authoring/review/repair leaves, source findings and recovered evidence were disposed. A1142 plus final P1483 binds current thirteen-request Operations and the shared Journal contract. P1130 remains retained completed reconciliation; P1131/C410 remain excluded and unfinished rather than falsely completed. Source destinations and precise revisions are accepted for the next PROGRAMMATIC/PROMPTS specification packets. This closes source work only: RMED review, code, functional Docker/MCP and actual Run evidence remain required.

### Definition of Done

This Plan is not Done until all thirteen selected Workflows and their required Actions have a traceable existing-or-authored source disposition, correct destination, independent review and findings disposition, including all-Run journaling and the three Projection behaviors. Every newly required authoring/review/repair leaf must be Done. The Operator-excluded legacy authoring closure and unrelated harvest capabilities are not required children.
