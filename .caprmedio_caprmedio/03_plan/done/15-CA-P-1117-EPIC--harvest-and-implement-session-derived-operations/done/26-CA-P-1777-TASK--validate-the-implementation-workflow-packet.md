---
atom_id: CA-P-1777
content_role: Plan
type: Plan
label: Task
work_sequence_number: 26
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 2
updated_at: "2026-10-06 05:43:54 +0000"
subjects:
  governs: "Implementation Workflow packet admission"
  depends_on: [Implementation, Evaluation, Workflow, Plan, Permission]
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1655, CA-P-1721]
---
# Summary

Validate the Implementation Workflow packet

## Objective

Enforce the admitted Implementation packet and result-evidence boundary before the selected Workflow treats work as performed successfully.

## Details

1. Read the exact O094/E519/M295 requirements and implement one shared packet validator in the owning Action boundary.
2. Bind the selected R/D/E and complete active-M projection, Plan and Definition of Done, candidate/phase and effective confidence/retry/permission evidence as those sources require.
3. Validate performed-success coverage against the current admitted input; reject incomplete or conflicting evidence.
4. Add focused positive and negative tests and obtain independent acceptance.

Do not invent cardinalities, maintain a second independent validator, change current report locations or fabricate Journal facts. The outer selected executor retains Run recording. One worker owns Action code/tests and only the relevant Implementation adapter sections; lifecycle adapter sections have another owner. Estimated bounded repair slice <=15 minutes.

## Definition of Done

The source-governed packet boundary has regression coverage and independently accepted evidence. Required actual Docker/queue/Journal proof remains in the existing runtime gate.

## Pre-execution review

The restored two-route audit found shallow list/response checks where current authority requires source-bound packet and coverage evidence. DRY and truthful acceptance favor one owning validator, with incomplete work reported instead of accepted. CA-C-493 retains the finding.

## Results

The shared validator checks current R/D/E and full active-M bindings, Plan/DoD/owned paths, candidate/phase, confidence, retry and coverage before dispatch. Retry uses the separately retained sealed outer authorization, not an approval boolean. Implemented/repaired results must match the admitted candidate and phase. Twenty-six prompt/selected-project, twenty O016, twelve W09/native/Revert integration and one wrapper tests passed. Independent review accepted the repaired boundaries and independently passed 19 prompt, 20 O016 and seven native-provider cases. Actual Docker/queue/Journal proof remains separately required.
