---
atom_id: CA-O-174
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: run complete tests"
  depends_on: [Workflow, Step, Action, Test, Applicable Methodology, Journal]
version: 1
updated_at: 2026-10-05 06:13:05 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-168]
---
# Summary

Run the complete candidate release test suite

## Step

This Step invokes CA-O-168 once with phase `run_tests`, binding CA-O-173's complete compiled candidate Projection, the frozen source digest and the full declared release suite.

## Details

The suite must be complete for the declared release boundary; focused, cached, host-only or historical results are not a substitute. It completes before candidate runtime/package or Skill staging and cannot select N+1. A failed, blocked, unsafe, unavailable or unjournalable result stops before staging, image work, promotion or retirement and preserves actual evidence without retry.
