---
atom_id: CA-C-469
content_role: Concern
type: Problem
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 16:34:05 +0400"
subjects:
  governs: "First Framework runtime and project-local ca Skill absence"
  depends_on: [Runtime, Framework Package, Skill, Docker Image, Journal, Action]
relations:
  concern_about: [CA-P-1620, CA-P-1624, CA-P-1714]
---
# Summary

The first Framework runtime and project-local ca Skill are absent

## Concern

The Project has no `.caprmedio_runtime/framework/current.toml`, retained Framework release, or `.agents/skills/ca` carrier. Release Version correctly refuses to invent N, so it cannot establish its N-to-N+1 rollback boundary until the separate explicit initialization capability is implemented and evidenced. The bootstrap selector is the only activation point; a copied Skill without it is a truthful partial state, not an installed runtime.

## Evidences

At 2026-10-05 16:23:09 +0400, all three required initial carriers were absent in the Project worktree. Existing Release source requires a complete retained N package and matching project-local Skill before its candidate suite, staging, promotion, and retirement phases.

## Blast radius

CA-P-1624 cannot provide actual Release Version package, Skill, image, or rollback proof. Existing source authority and the fifteen already selected Workflow routes remain unchanged; initialization is a separate explicit Action, not a sixteenth-plus selected route.

## Disposition

The first-installation carrier has a distinct but exact bootstrap-to-N+1 compatibility proof in CA-D-575: the retained selector and actual package-manifest bytes identify N, while the bootstrap manifest's existing candidate-snapshot field remains the sealed source-context digest. This does not add a Release Version route, generic manifest exception, or inferred success state. The remaining question is empirical only: an explicit first installation must still produce and retain those carriers before a real N-to-N+1 run can be evidenced.
