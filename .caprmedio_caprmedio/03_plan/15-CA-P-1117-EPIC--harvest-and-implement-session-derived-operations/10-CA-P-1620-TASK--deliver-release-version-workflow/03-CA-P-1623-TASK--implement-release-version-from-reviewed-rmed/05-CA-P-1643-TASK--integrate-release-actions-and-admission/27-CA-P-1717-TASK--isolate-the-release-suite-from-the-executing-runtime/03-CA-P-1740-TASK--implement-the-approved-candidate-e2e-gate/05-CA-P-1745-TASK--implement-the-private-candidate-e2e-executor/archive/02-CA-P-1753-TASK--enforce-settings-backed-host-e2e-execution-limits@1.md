---
atom_id: CA-P-1753
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
  governs: "Candidate E2E Release gate/Enforce settings-backed host E2E execution limits"
  depends_on: [Implementation, Evaluation, Workflow, Action, Docker Image, Test Suite, Journal]
relations:
  is_decomposition_of: [CA-P-1745]
  blocks: [CA-P-1754]
---
# Summary

Enforce settings-backed host E2E execution limits

## Objective

Resolve exactly D582's six Framework Instance settings with individual canonical defaults. Enforce inspect, harness and cleanup timeouts and stdout/stderr/JUnit caps while reading; overflow, timeout and uncertain cleanup are non-passing. Bind the current settings and refuse before/after changes; retained disposable directories alone are allowed.

## Details

Ownership: RELEASE_VERSION/release_e2e_gate.py plus private context/Driver only if needed. Expected execution slice <=15 minutes. Workers share the checkout and preserve edits outside their exclusive scope. Root owns integration and Git. Source/currentness, permission and missing evidence guards remain intact.

## Definition of Done

Six-setting fallback/type/finite/positive/overflow/timeout/cleanup tests pass; no caller override or invented seventh setting is admitted.

## Pre-execution review

Root selects this bounded decomposition to finish the accepted R1890/M346/E589/D582 contract, not a narrower smoke-test substitute. Existing retained N, public routes, pending Runs and canonical Journal history remain protected.
