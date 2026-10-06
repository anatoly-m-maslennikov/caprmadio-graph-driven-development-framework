---
atom_id: CA-O-184
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: aggregate Full Gate"
  depends_on: [Workflow, Step, Action, Test, Journal]
version: 2
updated_at: "2026-10-05 21:41:23 +0000"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-183]
---
# Summary

Aggregate the full Release Gate

## Step

This Step invokes CA-O-183 once after CA-O-182, binding CA-O-185 closed-unit, CA-O-186 image-canary and CA-O-182 host Candidate E2E receipts to one exact candidate before CA-O-178 promotion.

## Details

It cannot promote or retire. Any unavailable, mismatched, stale, failed, partial or recording-blocked constituent stops the Workflow before promotion and preserves recovery evidence without implicit retry.
