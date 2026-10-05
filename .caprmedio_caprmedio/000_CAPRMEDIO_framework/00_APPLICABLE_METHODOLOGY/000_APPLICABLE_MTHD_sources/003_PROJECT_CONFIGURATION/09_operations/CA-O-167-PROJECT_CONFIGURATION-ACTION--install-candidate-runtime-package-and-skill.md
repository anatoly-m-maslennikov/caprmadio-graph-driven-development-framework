---
atom_id: CA-O-167
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Install candidate Framework package and project Skill"
  depends_on: [Action, Framework Package, Methodology, Skill, Artifact/Revision, Delivery, Journal]
version: 1
updated_at: 2026-10-05 06:13:05 +0400
relations:
  relates_to: [CA-O-164, CA-O-175, CA-D-563, CA-R-1525, CA-R-1720]
---
# Summary

Stage candidate runtime package and Skill

## Action

Stage candidate runtime package and Skill **means** the Action that performs the one bound `stage_candidate` phase from the compiled, frozen N+1 candidate manifest without selecting N+1 as the active runtime or project Skill.

## Scope

`stage_candidate` prepares the complete declared candidate Framework package at its reviewed non-active `.caprmedio_runtime` candidate package target, including the matching runtime Methodology delivery derived from the canonical candidate Projection and declared package members rather than Engine binaries alone. It also stages CA-D-563's complete hook-free `ca` directory payload for eventual project-local target `.agents/skills/ca`, without replacing N's active project-local Skill.

## Details

The phase requires the exact compiled output, package manifest/digests, staging target identity, permissions and recovery boundary validated by CA-O-165. Preserve the active N runtime and Skill selection until CA-O-169 promotion, along with rollback evidence, Project and framework-instance settings, authoring sources, Journals and unrelated Skills. A missing Methodology member, unbound target, incomplete Skill directory, digest mismatch, hook, partial staging, unavailable permission or failed postcondition is blocked or partial with actual evidence. This Action does not infer a Skill target, install a global Skill, select candidate runtime/Skill, alter global settings, register MCP, test, build an image, promote, remove images or retry itself. Every actual invocation is journaled once.
