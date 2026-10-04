---
atom_id: CA-P-1569
content_role: Plan
type: Plan
label: Task
work_sequence_number: 27
current_scope_unit: caprmedio
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Actual selected Action result observation"
  depends_on: [Action, Run, Journal, MCP, Implementation, Evaluation]
version: 2
updated_at: "2026-10-04 23:29:13 +0000"
relations:
  is_decomposition_of: [CA-P-1527]
  blocks: [CA-P-1527, CA-P-1528]
---
# Summary

Observe actual selected Action results

## Objective

Within <=15 minutes, finish the existing get_selected_action_run observation helper without adding execution authority.

## Details

- Own only its adapter observation in selected_routes.py, a narrow read-only selected_action_observation.py helper in WORKFLOW_ORCHESTRATOR if necessary, and directly focused tests. Separately repair the obsolete exact thirteen-route assertion in test_selected_execution.py to the accepted fifteen inventory; no production executor edits.
- Follow R1848/D547/D548 and actual shared Run/queue artifacts. Locate only actual selected Action identities and their source-bound parent Run, confirmed canonical Journal facts and durable result/progress references. Preserve unknown, unstarted, failed, incomplete and recording-pending dispositions; do not infer completion from a result file or scheduler acknowledgement.
- Return safe, redacted bounded observations for the selected Project. Reject path traversal, secret selection, ambiguous identity and unsupported references. Do not enumerate unrelated files or disclose unbound outputs. No dispatch, worker, mutation, pending-event replay or Journal write.
- Prove actual disposable completed and failed/pending observations, unknown and unsafe input refusals, no-effect read-only behavior, and existing helper compatibility. Coordinate P1563's query result fields without editing its files.
- Preserve concurrent work and use apply_patch. Root saves Plans/commits. Inherit 90%; no FPF, harvesting, broad audit or live Project mutation. Source ambiguity remains a named blocker, not invented authority.

## Definition of Done

The already-declared helper returns truthful current saved Action observations with focused proof; full route/image and standalone Action dispatch are separate.

## Result

The existing MCP helper now invokes selected_action_observation.py, which binds exact saved Action/Step/Workflow identity to the current manifest, safe result/progress refs and matching sealed canonical Journal receipts. It reports unreceipted progress as recording_pending and preserves completed, failed, unknown, unstarted, unsafe and stale dispositions. No observer dispatch, effect, worker, replay or Journal write was added. Five focused disposable observation tests, twelve MCP route tests and twenty current selected-execution regressions passed; compilation and diff checks passed. Only the stale route inventory assertion was changed in the existing selected test. No live Project observation or image/standalone dispatch proof is claimed.
