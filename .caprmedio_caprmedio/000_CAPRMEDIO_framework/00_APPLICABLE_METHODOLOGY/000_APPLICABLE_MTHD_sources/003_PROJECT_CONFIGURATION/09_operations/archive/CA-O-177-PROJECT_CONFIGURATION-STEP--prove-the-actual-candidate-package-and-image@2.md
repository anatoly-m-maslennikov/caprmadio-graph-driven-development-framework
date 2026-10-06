---
atom_id: CA-O-177
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: prove candidate"
  depends_on: [Workflow, Step, Action, Docker Image, Framework Package, Methodology, Skill, Journal]
version: 2
updated_at: 2026-10-06 00:00:00 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-168]
---
# Summary

Run the candidate image canary

## Step

This Step invokes CA-O-168 once with phase `candidate_image_canary`, binding CA-O-176's exact candidate image digest and staged complete package, Methodology and hook-free Skill. It is the frozen-container canary only; it is not host Candidate E2E or Full Gate aggregation.

## Details

The result must prove the actual candidate image and staged complete package, not only source files, a manifest or build success. The Step never recurses into CA-O-164, changes N/N+1 bindings, selects runtime/Skill, removes images or uses an unbound external/paid CLI. Missing or unsafe proof stops truthfully before CA-O-182.
