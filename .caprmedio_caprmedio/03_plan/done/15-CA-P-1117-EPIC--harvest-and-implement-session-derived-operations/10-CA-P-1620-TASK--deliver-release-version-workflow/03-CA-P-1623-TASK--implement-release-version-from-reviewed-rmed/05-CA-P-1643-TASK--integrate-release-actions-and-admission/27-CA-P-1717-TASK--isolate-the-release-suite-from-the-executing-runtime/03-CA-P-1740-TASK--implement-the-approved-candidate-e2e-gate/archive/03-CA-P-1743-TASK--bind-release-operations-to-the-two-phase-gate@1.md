---
atom_id: CA-P-1743
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
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
  governs: "Candidate E2E Release gate/Bind Release Operations to the two-phase gate"
  depends_on: [Implementation, Evaluation, Workflow, Action, Docker Image, Test Suite, Journal]
relations:
  is_decomposition_of: [CA-P-1740]
  blocks: [CA-P-1748]
---
# Summary

Bind Release Operations to the two-phase gate

## Objective

Place Candidate E2E and Full Gate aggregation after candidate image canary and before promotion.

## Details

Own O164/O168/O174-O178 and necessary reserved O181-O184 Action/Step carriers with full predecessor archives. Keep sixteen public Workflows, exact N/candidate lineage and all-Run journaling. A host-capable controller is required; the frozen Docker worker gains no socket. ETA <=15 minutes.

## Definition of Done

The owned source or implementation is independently accepted and actual scoped verification is saved. Mock or source acceptance does not close live Docker, complete-suite, installation or promotion gates.

## Pre-execution review

Root accepts this bounded decomposition of the Operator-approved host E2E design. Respect the stated dependency and file-ownership boundaries. The existing isolated Unit executor, current public manifest, pending Runs and retained N remain protected.
