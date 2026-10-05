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
version: 3
updated_at: "2026-10-05 21:41:23 +0000"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-167]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-175-PROJECT_CONFIGURATION-STEP--stage-the-candidate-framework-package-and-ca-skill.md
  source_atom_id: CA-O-175
  source_atom_revision: 3
  source_sha256: 7a03ec026e8feb913e2d3925c9d555c42e22585b765fa67b42c45a3a7633c539
  original_relations_sha256: e3e023ec734e75ff4523c956b834281950799ed69175a6f55dba128b16ed5b41
---
# Summary

Stage the candidate Framework package and ca Skill

## Step

This Step invokes CA-O-167 once with phase `stage_candidate`, binding CA-O-185's closed unit-gate result, CA-O-173's exact compiled candidate output, complete package manifest and CA-D-563's complete hook-free `ca` directory payload for eventual project-local target `.agents/skills/ca`.

## Details

It stages the complete candidate package and complete hook-free `ca` directory without selecting N+1 as active runtime or replacing N's active `.agents/skills/ca` Skill. A target mismatch, incomplete Methodology or Skill directory, hook, partial staging, permission failure or missing Journal receipt stops before image build, promotion or retirement.
