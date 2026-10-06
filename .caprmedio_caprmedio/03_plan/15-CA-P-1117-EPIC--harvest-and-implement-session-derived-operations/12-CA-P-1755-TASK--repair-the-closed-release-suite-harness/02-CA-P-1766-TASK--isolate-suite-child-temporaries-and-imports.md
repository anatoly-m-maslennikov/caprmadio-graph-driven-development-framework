---
atom_id: CA-P-1766
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
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
  governs: "Isolate suite child temporaries and imports"
  depends_on: [Implementation, Evaluation, Workflow, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1755]
  blocks: []
---
# Summary

Isolate suite child temporaries and imports

## Objective

Isolate suite child temporaries and imports under the parent's exact source contract.

## Details

suite_driver_repair exclusively owns RELEASE_VERSION/run_release_suite.py and tests/test_run_release_suite.py.

Estimated execution slice <=15 minutes. Preserve other workers' changes. Root alone owns index, commits and actual shared runtime effects. Tests and disposable smoke evidence are not release promotion.

## Definition of Done

Fixed child scratch and same-name flat-module import regressions pass without candidate-byte changes.

## Pre-execution review

Root accepts this exclusive bounded assignment as the minimal current parent repair. Preserve installed N and truthful observed effects.
