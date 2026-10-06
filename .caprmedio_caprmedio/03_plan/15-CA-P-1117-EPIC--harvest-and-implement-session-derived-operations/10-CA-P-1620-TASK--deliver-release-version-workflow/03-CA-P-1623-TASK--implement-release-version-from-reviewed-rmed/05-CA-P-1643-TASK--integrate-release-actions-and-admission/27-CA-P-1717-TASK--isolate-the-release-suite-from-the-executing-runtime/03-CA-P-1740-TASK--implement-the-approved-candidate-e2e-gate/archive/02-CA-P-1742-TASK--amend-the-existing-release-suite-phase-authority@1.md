---
atom_id: CA-P-1742
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
updated_at: "2026-10-05 20:50:41 +0000"
subjects:
  governs: "Candidate E2E Release gate/Amend the existing Release suite phase authority"
  depends_on: [Implementation, Evaluation, Workflow, Action, Docker Image, Test Suite, Journal]
relations:
  is_decomposition_of: [CA-P-1740]
  blocks: [CA-P-1747, CA-P-1748]
---
# Summary

Amend the existing Release suite phase authority

## Objective

Separate the closed Unit Gate and final complete gate in the existing Suite and image-build authority.

## Details

Own R1886/M343/E586/D579/D564 and full predecessor archives. Preserve the complete module inventory, source/current-control proofs and candidate identity. Unit evidence gates image construction; Unit plus E2E evidence gates promotion. ETA <=15 minutes.

## Definition of Done

The owned source or implementation is independently accepted and actual scoped verification is saved. Mock or source acceptance does not close live Docker, complete-suite, installation or promotion gates.

## Pre-execution review

Root accepts this bounded decomposition of the Operator-approved host E2E design. Respect the stated dependency and file-ownership boundaries. The existing isolated Unit executor, current public manifest, pending Runs and retained N remain protected.
