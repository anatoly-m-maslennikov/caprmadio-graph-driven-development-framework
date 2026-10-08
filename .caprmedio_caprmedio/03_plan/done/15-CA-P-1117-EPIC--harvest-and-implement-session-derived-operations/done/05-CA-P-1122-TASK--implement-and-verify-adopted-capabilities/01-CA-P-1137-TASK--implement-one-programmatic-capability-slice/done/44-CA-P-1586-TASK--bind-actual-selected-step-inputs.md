---
atom_id: CA-P-1586
content_role: Plan
type: Plan
label: Task
work_sequence_number: 44
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Bind actual selected Step inputs"
  depends_on: [Workflow, Action, Implementation, Evaluation, Journal]
version: 2
updated_at: "2026-10-05 00:21:02 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1519]
---
# Summary

Bind actual selected Step inputs

## Objective

Within <=15 minutes, deliver actual same-Run predecessor results and trusted frozen Project context to their already-declared selected Steps.

## Details

- Own only selected_execution.py narrow O015 retained-result context and O016 trusted-root wrapper plus focused test_selected_step_inputs.py. O144@2 consumes O143 actual cutover effects/resulting revisions and same-Run authorized proposal/checks. Supply structural_prior_results only from actually completed shared Action receipts, with source/action/step identities, result_ref and native result; never caller-asserted receipts or new public expected-post fields. Coordinate exact input shape with native structural owner. O016 handler receives selected_project_root=self.root from the trusted graph runner, in coordination with P1583. Preserve sealed parameters, failed-seal safety and all other routes. No Tool/PROMPTS/fixture/source/MCP/Plan/Journal edits, commits, FPF, harvesting, broad refactor or live effects. Apply patch, preserve others, inherit 90%.

## Saved result

Saved executor-retained structural_prior_results from actual sealed completed Action receipts and the trusted selected_project_root binding for Implementation handlers. Focused selected-step input tests passed 3/3; compiler recording tests passed 2/2. Real W06 completed all six Steps with changed references. Forced O143 seal failure blocked O144 and replayed no effects.

## Definition of Done

Source-declared Steps receive exact actual trusted inputs; current reference-changing W06 and selected Project root validation are proved without authority inference.
