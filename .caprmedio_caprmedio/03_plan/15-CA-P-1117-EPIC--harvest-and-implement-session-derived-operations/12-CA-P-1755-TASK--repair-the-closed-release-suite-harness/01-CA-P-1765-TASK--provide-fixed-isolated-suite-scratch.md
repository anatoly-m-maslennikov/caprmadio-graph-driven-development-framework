---
atom_id: CA-P-1765
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-06 03:53:17 +0000"
subjects:
  governs: "Provide fixed isolated suite scratch"
  depends_on: [Implementation, Evaluation, Workflow, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1755]
  blocks: []
---
# Summary

Provide fixed isolated suite scratch

## Objective

Provide fixed isolated suite scratch under the parent's exact source contract.

## Details

suite_scratch_executor exclusively owns RELEASE_VERSION/release_suite_execution.py and tests/test_release_suite_execution.py.

Estimated execution slice <=15 minutes. Preserve other workers' changes. Root alone owns index, commits and actual shared runtime effects. Tests and disposable smoke evidence are not release promotion.

## Definition of Done

Fixed bounded tmpfs regression and actual disposable Docker scratch smoke pass; source bind stays read-only.

## Pre-execution review

Root accepts this exclusive bounded assignment as the minimal current parent repair. Preserve installed N and truthful observed effects.
