---
atom_id: CA-P-1751
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
updated_at: "2026-10-05 21:58:15 +0000"
subjects:
  governs: "Candidate E2E Release gate/Exercise candidate E2E boundaries with golden inputs"
  depends_on: [Implementation, Evaluation, Workflow, Action, Docker Image, Test Suite, Journal]
relations:
  is_decomposition_of: [CA-P-1744]
  blocks: []
---
# Summary

Exercise candidate E2E boundaries with golden inputs

## Objective

Use the presealed fixture to test receipt tamper/removal/cross-candidate binding, exact phase-map membership, no-skip/nonzero testcase JUnit, configured limits, source drift, closed context and immutable image propagation. Test doubles remain non-passing actual Release evidence.

## Details

Ownership: RELEASE_VERSION/test_release_e2e_gate.py, test_release_e2e_context.py and test_run_release_e2e.py. Expected execution slice <=15 minutes. Workers share the checkout and preserve edits outside their exclusive scope. Root owns integration and Git. Source/currentness, permission and missing evidence guards remain intact.

## Definition of Done

Focused behavior tests exercise every specified branch with explicit expected outcomes. Missing fixture or failed cases remain unfinished; no Docker pass is claimed.

## Pre-execution review

Root selects this bounded decomposition to finish the accepted R1890/M346/E589/D582 contract, not a narrower smoke-test substitute. Existing retained N, public routes, pending Runs and canonical Journal history remain protected.
