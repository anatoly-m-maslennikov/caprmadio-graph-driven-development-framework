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
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-184-PROJECT_CONFIGURATION-STEP--aggregate-the-full-release-gate.md
  source_atom_id: CA-O-184
  source_atom_revision: 2
  source_sha256: 12e81e759876d93a674c04c75b0faf07288a966c38815c318e2dda023341e6e5
  original_relations_sha256: 144bb2af640a8af7e963af40a03df36bdce9f2fa019370cb9b1710b61085ad84
---
# Summary

Aggregate the full Release Gate

## Step

This Step invokes CA-O-183 once after CA-O-182, binding CA-O-185 closed-unit, CA-O-186 image-canary and CA-O-182 host Candidate E2E receipts to one exact candidate before CA-O-178 promotion.

## Details

It cannot promote or retire. Any unavailable, mismatched, stale, failed, partial or recording-blocked constituent stops the Workflow before promotion and preserves recovery evidence without implicit retry.
