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
version: 1
updated_at: 2026-10-05 06:13:05 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-168]
---
# Summary

Prove the actual candidate package and image

## Step

This Step invokes CA-O-168 once with phase `prove_candidate`, binding CA-O-176's exact candidate image digest and the staged complete package, Methodology, hook-free Skill and actual release verification contract.

## Details

The result must prove the actual candidate image and staged complete package, not only source files, a manifest or build success. The Step never recurses into CA-O-164, changes N/N+1 bindings, selects runtime/Skill, removes images or uses an unbound external/paid CLI. Missing or unsafe proof stops truthfully.
