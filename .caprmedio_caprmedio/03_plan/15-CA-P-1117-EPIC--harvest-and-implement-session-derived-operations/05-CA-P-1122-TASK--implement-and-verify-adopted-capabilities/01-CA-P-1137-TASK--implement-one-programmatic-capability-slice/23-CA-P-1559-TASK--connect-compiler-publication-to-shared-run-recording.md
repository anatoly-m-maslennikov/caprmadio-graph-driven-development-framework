---
atom_id: CA-P-1559
content_role: Plan
type: Plan
label: Task
work_sequence_number: 23
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Connect compiler publication to shared Run recording"
  depends_on: [Workflow, Implementation, Evaluation, Projection, Journal]
version: 2
updated_at: "2026-10-04 22:46:18 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1515, CA-P-1519]
---
# Summary

Connect compiler publication to shared Run recording

## Objective

Within <=15 minutes, connect the actual publication handoff to its existing canonical Action Run.

## Details

Saved result: compiler publication reaches its declared completion label only after the existing shared session persists the actual Action terminal receipt. Progress retains source frontier, output digest and paths. Two real shared-recording tests passed in Docker, including injected recording failure returning pending and repeat dispatch without a second publication. Existing selected tests passed; five opt-in image tests were explicitly skipped, not counted as image proof. Post-recovery result promotion remains a later inspection-only handoff, never an effect replay. MCP/image proof remains separate.

Inputs: accepted CA-P-1558 native compiler proof, current compiler pending_recording handoff and accepted CA-O-011 source/RMED. Own only selected_execution.py's compiler adapter and necessary publication handling, plus a dedicated test_selected_compiler_recording.py. Preserve unrelated adapters and queue schemas. Reuse the provided shared Run session and exact existing Action identity; native applied output is not completed publication until actual canonical Run evidence is persisted. Retain native output digest, paths, frontier and evidence. Recording failure must retain truthful pending/uncertain state without reapplying effects, inventing receipts, adding Journal serialization or a second executor. Prove real temporary output effects and one Workflow/Step/Action lineage using the real shared recorder, including recording failure/no replay. No source, compiler module, backend, MCP, manifest or fixture edits. Coordinate selected_execution.py ownership with root before other integration begins.

Inherit CA-P-1117's 90% threshold and mechanical Git exception. You are not alone; preserve others and use apply_patch. Root saves Plans/commits. No FPF, harvesting or permission bypass.

## Definition of Done

Native publication completes only after actual shared recording; failure remains truthfully pending without duplicate effects.
