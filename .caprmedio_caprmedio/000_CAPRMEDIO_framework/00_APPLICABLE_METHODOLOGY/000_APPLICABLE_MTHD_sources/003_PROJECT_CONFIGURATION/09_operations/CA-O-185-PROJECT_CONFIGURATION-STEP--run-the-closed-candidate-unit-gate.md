---
atom_id: CA-O-185
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: run closed candidate Unit gate"
  depends_on: [Workflow, Step, Action, Test, Applicable Methodology, Journal]
version: 1
updated_at: "2026-10-05 21:41:23 +0000"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-168]
---
# Summary

Run the closed candidate Unit gate

## Step

This Step invokes CA-O-168 once with phase `closed_unit_gate`, binding CA-O-173's exact compiled candidate, frozen N/N+1, candidate manifest, source frontier and the declared Unit partition.

## Details

The Unit partition is complete for every declared testcase except exactly these three host Candidate E2E modules: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py`, and `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py`. Every declared Unit testcase must terminal-pass for this exact candidate; skipped, excluded, missing or zero-coverage testcase is non-pass. Focused, cached, host-only or historical results are not substitutes. This Step cannot select N+1, stage packages, build or remove images, or retry.
