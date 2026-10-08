---
atom_id: CA-P-1582
content_role: Plan
type: Plan
label: Task
work_sequence_number: 41
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Complete compiler publication recording"
  depends_on: [Workflow, Action, Implementation, Evaluation, Journal]
version: 2
updated_at: "2026-10-04 23:52:49 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1519]
---
# Summary

Complete compiler publication recording

## Objective

Within <=15 minutes, let a truly applied compiler publication take its declared success edge only after its actual shared Action Run seals.

## Details

- Own selected_execution.py's compiler publication/shared terminal handoff and test_selected_compiler_recording.py only. Preserve other native branches and all concurrent edits.
- Native pending_recording/APPLIED is not itself completion. Fix the impossible handoff where the same Action is first sealed interrupted_pending and then asked for a completed receipt; use the existing actual shared recorder, with no alternate writer, forged receipt or replay.
- A failed seal remains recording_pending and the applied effect cannot rerun. Preserve cancellation, currentness and actual effect references. Prove both successful real seal and failed-seal safety; actual W13 uses freshly assessed expected_source_frontier_digest.
- No fixture, Tool, source, MCP, Plan, Journal or commit edits. Coordinate any one separately required Implementation wrapper hunk with root. Apply patch, inherit 90%, no FPF, harvesting or paid/live Project effects.

## Saved result

Native pending_recording/APPLIED publication now requests actual completed shared Action receipt before the completed-publication graph edge. Failed append remains pending and cannot replay applied effects. Existing strict compiler recording tests 2/2 pass; disposable freshly assessed W13 preview/freeze/dispatch completes with real Core/Extension/Project Configuration projection bytes. Only compiler branch changed, no image/queue/MCP claim.

## Definition of Done

Actual recorded compiler publication completes the declared graph; failed recording retains the precise pending boundary without effect replay.
