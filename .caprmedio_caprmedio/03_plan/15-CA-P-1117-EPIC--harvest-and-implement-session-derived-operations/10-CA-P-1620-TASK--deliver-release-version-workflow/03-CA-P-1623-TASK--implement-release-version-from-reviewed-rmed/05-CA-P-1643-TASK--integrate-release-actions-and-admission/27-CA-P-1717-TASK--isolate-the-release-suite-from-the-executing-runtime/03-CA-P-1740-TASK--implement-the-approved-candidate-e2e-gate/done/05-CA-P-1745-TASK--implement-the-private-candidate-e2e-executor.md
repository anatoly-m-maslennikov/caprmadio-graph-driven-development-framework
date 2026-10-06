---
atom_id: CA-P-1745
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
version: 3
updated_at: "2026-10-05 22:45:36 +0000"
subjects:
  governs: "Candidate E2E Release gate/Implement the private Candidate E2E executor"
  depends_on: [Implementation, Evaluation, Workflow, Action, Docker Image, Test Suite, Journal]
relations:
  is_decomposition_of: [CA-P-1740]
  blocks: [CA-P-1747, CA-P-1748]
---
# Summary

Implement the private Candidate E2E executor

## Objective

Implement the fixed host executor and trusted JUnit-producing driver from accepted source and test-first coverage.

## Details

Own release_e2e_gate.py, run_release_e2e.py and the necessary private sealed harness-context adapter. Reuse existing suite reporting and receipt primitives; accept no caller command/path/environment override. Missing host capability is non-passing. ETA <=15 minutes; decompose before expansion.

## Definition of Done

The owned source or implementation is independently accepted and actual scoped verification is saved. Mock or source acceptance does not close live Docker, complete-suite, installation or promotion gates.

## Pre-execution review

Root accepts this bounded decomposition of the Operator-approved host E2E design. Respect the stated dependency and file-ownership boundaries. The existing isolated Unit executor, current public manifest, pending Runs and retained N remain protected.

## Required decomposition

This composite is not one executable <=15-minute leaf. Complete CA-P-1752, CA-P-1753, CA-P-1754; each owns the files and acceptance stated in its carrier. Prototype/import checks already occurred but are not the complete behavioral test prerequisite. No actual Docker or publication failure is bypassed. The composite remains Active until every required child is Done.

## Recorded verification

Local implementation acceptance is saved in 7874fc864 and 5e0dfee93. The complete private gate module passed 11/11 tests after bounded failed/malformed/empty JUnit retention was fixed; the affected method also passed independently. Narrow D582#10 review accepted the final branch. Earlier context/Driver/phase-map, Runtime image-binding and actual stdio transport results remain retained. Synthetic image/command observations are mock data, not Docker or Release proof. No full-suite, installation, promotion or retirement result is claimed.
