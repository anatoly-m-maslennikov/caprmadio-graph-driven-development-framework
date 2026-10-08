---
atom_id: CA-P-1755
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
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
  governs: "Repair the closed Release suite harness"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1717, CA-P-1721]
---
# Summary

Repair the closed Release suite harness

## Objective

Repair fixed isolated scratch, child import isolation and stale fixture bindings while keeping candidate sources read-only.

## Details

RELEASE_VERSION executor/driver and focused tests; workers suite_scratch_executor, suite_driver_repair and release_fixture_repair. O168/O185, D579/D580 and the sealed suite boundary govern. No writable source mount, network or Docker socket.

This is a repair composite, not one aggregate <=15-minute leaf. Its independently bounded assignments are: suite_scratch_executor owns release_suite_execution.py and test_release_suite_execution.py; suite_driver_repair owns run_release_suite.py and test_run_release_suite.py; release_fixture_repair owns test_release_suite_bindings_handoff.py; n5_unit_diagnosis owns release_suite.py and test_release_suite.py. A subsequent fixture-only slice owns test_bootstrap_image.py, test_release_e2e_retained.py, test_release_e2e_gate.py and test_release_full_gate.py. Each assignment has a <=15-minute limit and independent test result. Workers preserve other edits and do not stage or commit. Root owns integration and Git.

## Definition of Done

Focused regressions pass; scratch is writable only in bounded tmpfs; immutable source bytes stay unchanged. The full actual release gate remains P1717/P1721.

## Pre-execution review

Root accepts this bounded repair/restoration against Operator authority, DRY, preservation of valuable information and the latest continuation. Keep installed N intact and distinguish local tests from required actual runtime gates.

## Recorded verification

Local harness repair accepted: 27 executor/driver cases, 26 complete suite-wrapper cases, five binding and twelve neighboring phase cases, and all 32 assigned bootstrap/E2E/full-gate fixture cases passed. The actual Docker scratch smoke preserved read-only source and ephemeral tmpfs. Commits 782afb531, 8b8d74bb5 and 6e4b3acc2 retain the changes. This is not the actual complete candidate Unit gate.
