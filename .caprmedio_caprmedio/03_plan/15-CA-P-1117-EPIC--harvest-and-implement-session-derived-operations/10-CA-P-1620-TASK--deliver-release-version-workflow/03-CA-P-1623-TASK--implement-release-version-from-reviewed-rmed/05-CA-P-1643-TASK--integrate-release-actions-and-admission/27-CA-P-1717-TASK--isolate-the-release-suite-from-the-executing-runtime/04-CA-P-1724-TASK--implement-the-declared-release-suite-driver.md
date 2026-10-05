---
atom_id: CA-P-1724
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-05 18:22:01 +0000"
subjects:
  governs: "Release suite delivery/Implement the declared Release suite driver"
  depends_on: [Implementation, Evaluation, Methodology, Manifest, Test Suite]
relations:
  is_decomposition_of: [CA-P-1717]
---
# Summary

Implement the declared Release suite driver

## Objective

Implement the accepted complete-suite driver and maintained module-level probe rules.

## Details

Own only RELEASE_VERSION/run_release_suite.py and release_suite_bindings.json. Execute every declared testcase in fresh per-module children, attest exact sealed sources, emit one JUnit row per actual testcase, and fail closed for unavailable prerequisites. Reuse unittest and standard-library facilities. Expected bounded work: <=15 minutes; decompose if needed.

## Definition of Done

The driver satisfies the accepted RMED and deterministic E2E corpus without hidden exclusions or synthetic full-suite success.
