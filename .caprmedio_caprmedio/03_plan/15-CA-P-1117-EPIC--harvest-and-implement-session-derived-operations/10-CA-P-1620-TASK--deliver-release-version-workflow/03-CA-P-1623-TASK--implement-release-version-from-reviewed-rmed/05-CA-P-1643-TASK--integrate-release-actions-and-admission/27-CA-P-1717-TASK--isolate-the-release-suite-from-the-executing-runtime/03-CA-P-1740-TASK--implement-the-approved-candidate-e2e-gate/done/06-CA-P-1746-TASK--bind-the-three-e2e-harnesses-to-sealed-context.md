---
atom_id: CA-P-1746
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 2
updated_at: "2026-10-05 22:45:36 +0000"
subjects:
  governs: "Candidate E2E Release gate/Bind the three E2E harnesses to sealed context"
  depends_on: [Implementation, Evaluation, Workflow, Action, Docker Image, Test Suite, Journal]
relations:
  is_decomposition_of: [CA-P-1740]
  blocks: [CA-P-1748]
---
# Summary

Bind the three E2E harnesses to sealed context

## Objective

Run each declared E2E harness only against the sealed candidate image and dedicated writable scratch.

## Details

Own only the three APP/WORKFLOW_ORCHESTRATOR E2E harness files and necessary bounded Runtime constructor binding/tests. Remove mutable-tag admission and ambient opt-in acceptance; source workspace remains sealed read-only. Coordinate exact context API with P1745. ETA <=15 minutes.

## Definition of Done

The owned source or implementation is independently accepted and actual scoped verification is saved. Mock or source acceptance does not close live Docker, complete-suite, installation or promotion gates.

## Pre-execution review

Root accepts this bounded decomposition of the Operator-approved host E2E design. Respect the stated dependency and file-ownership boundaries. The existing isolated Unit executor, current public manifest, pending Runs and retained N remain protected.

## Recorded verification

Local implementation acceptance is saved in 7874fc864 and 5e0dfee93. The complete private gate module passed 11/11 tests after bounded failed/malformed/empty JUnit retention was fixed; the affected method also passed independently. Narrow D582#10 review accepted the final branch. Earlier context/Driver/phase-map, Runtime image-binding and actual stdio transport results remain retained. Synthetic image/command observations are mock data, not Docker or Release proof. No full-suite, installation, promotion or retirement result is claimed.
