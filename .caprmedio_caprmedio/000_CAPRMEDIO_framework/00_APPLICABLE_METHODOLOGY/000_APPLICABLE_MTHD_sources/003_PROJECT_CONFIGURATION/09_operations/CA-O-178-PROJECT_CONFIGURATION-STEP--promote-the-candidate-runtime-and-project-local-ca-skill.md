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
version: 1
updated_at: 2026-10-05 06:13:05 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-169]
---
# Summary

Promote the candidate runtime and project-local ca Skill

## Step

This Step invokes CA-O-169 once with phase `promote`, binding CA-O-177's complete candidate proof, exact N/N+1 identities, explicit promotion permission and the staged package plus CA-D-563's complete hook-free `ca` directory payload for `.agents/skills/ca`.

## Details

Only this post-proof Step may select N+1 runtime and replace N's active project-local `.agents/skills/ca` Skill. It does not install hooks, alter global settings, register MCP, retire an image, force recovery or retry; a failed or partial promotion retains actual N/N+1 state and Journal evidence for the later exact retirement decision.
