---
atom_id: CA-P-1769
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 2
updated_at: "2026-10-06 04:12:31 +0000"
subjects:
  governs: "Move release fixtures to admitted scratch"
  depends_on: [Implementation, Evaluation, Workflow, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1755]
  blocks: []
---
# Summary

Move release fixtures to admitted scratch

## Objective

Move release fixtures to admitted scratch under the parent's exact source contract.

## Details

suite_scratch_executor exclusively owns tests/test_bootstrap_image.py, test_release_e2e_retained.py, test_release_e2e_gate.py and test_release_full_gate.py.

Estimated execution slice <=15 minutes. Preserve other workers' changes. Root alone owns index, commits and actual shared runtime effects. Tests and disposable smoke evidence are not release promotion.

## Definition of Done

The four complete fixture modules pass under the fixed Project scratch convention; no extra mounts or exclusions are added.

## Pre-execution review

Root accepts this exclusive bounded assignment as the minimal current parent repair. Preserve installed N and truthful observed effects.

## Recorded verification

8b8d74bb5; all 32 assigned fixture cases passed (12 bootstrap, 2 retained E2E, 11 E2E gate, 7 Full Gate). No extra source-write mounts were added.
