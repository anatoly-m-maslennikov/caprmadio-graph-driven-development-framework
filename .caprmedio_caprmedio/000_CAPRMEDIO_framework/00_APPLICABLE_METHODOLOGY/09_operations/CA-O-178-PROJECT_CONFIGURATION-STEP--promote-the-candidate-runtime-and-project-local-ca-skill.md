---
atom_id: CA-O-178
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: promote candidate runtime and Skill"
  depends_on: [Workflow, Step, Action, Version, Framework Package, Skill, Permission, Journal]
version: 3
updated_at: "2026-10-05 21:41:23 +0000"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-169]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-178-PROJECT_CONFIGURATION-STEP--promote-the-candidate-runtime-and-project-local-ca-skill.md
  source_atom_id: CA-O-178
  source_atom_revision: 3
  source_sha256: 3d413b7913f871fcaa8fe6fb10e091db8b296dd49f96cd570290a1cb74343782
  original_relations_sha256: 4a7aab972e708c440d2f546dc2c51322bfc83e7c8cb16d917b379901e2b55af0
---
# Summary

Promote the candidate runtime and project-local ca Skill

## Step

This Step invokes CA-O-169 once with phase `promote`, binding CA-O-184's exact passing Full Gate aggregate, the same frozen N/N+1 identities, candidate manifest, source frontier, compiled output, staged package, immutable image and parent lineage, explicit promotion permission, and CA-D-563's complete hook-free `ca` directory payload for `.agents/skills/ca`.

## Details

Only this post-proof Step may select N+1 runtime and replace N's active project-local `.agents/skills/ca` Skill. It does not install hooks, alter global settings, register MCP, retire an image, force recovery or retry; a failed or partial promotion retains actual N/N+1 state and Journal evidence for the later exact retirement decision.
