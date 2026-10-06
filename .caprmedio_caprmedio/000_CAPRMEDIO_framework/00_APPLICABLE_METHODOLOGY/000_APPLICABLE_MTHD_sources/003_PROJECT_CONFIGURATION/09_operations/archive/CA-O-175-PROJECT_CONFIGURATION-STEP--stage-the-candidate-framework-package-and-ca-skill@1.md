---
atom_id: CA-O-175
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: stage candidate package and Skill"
  depends_on: [Workflow, Step, Action, Framework Package, Methodology, Skill, Delivery, Journal]
version: 1
updated_at: 2026-10-05 06:13:05 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-167]
---
# Summary

Stage the candidate Framework package and ca Skill

## Step

This Step invokes CA-O-167 once with phase `stage_candidate`, binding CA-O-174's complete test result, CA-O-173's exact compiled candidate output, complete package manifest and CA-D-563's complete hook-free `ca` directory payload for eventual project-local target `.agents/skills/ca`.

## Details

It stages the complete candidate package and complete hook-free `ca` directory without selecting N+1 as active runtime or replacing N's active `.agents/skills/ca` Skill. A target mismatch, incomplete Methodology or Skill directory, hook, partial staging, permission failure or missing Journal receipt stops before image build, promotion or retirement.
