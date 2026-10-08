---
atom_id: CA-P-1714
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-05 16:34:05 +0400"
subjects:
  governs: "Initialize first Framework runtime and project-local ca Skill"
  depends_on: [Action, Tool, Framework Package, Runtime, Methodology, Skill, Docker Image, Journal, Evaluation]
relations:
  is_decomposition_of: [CA-P-1620]
  blocks: [CA-P-1624]
---
# Summary

Initialize the first Framework runtime and project-local ca Skill

## Objective

Implement and prove the explicit first runtime installation required before the ordinary N-to-N+1 Release Version Workflow can operate.

## Details

Implement CA-R-1881, CA-M-338, CA-E-581, CA-D-575, and CA-O-180 as a separate Tools capability. Test the empty success path and every required refusal before attempting this Project's first installation. Verify actual immutable image labels against the package manifest and source-context digests; publish the hook-free Skill before the selector, which is the only activation point. Preserve source authority and settings; do not add a selected workflow route or weaken the Release Version N-to-N+1 gates. If production publication hits a denied atomic directory operation, retain the actual partial state and Journal evidence and leave this Task Active.

## Definition of Done

An empty Project has a complete content-addressed Framework package, active selector, hook-free project-local `ca` Skill, matching immutable image, and canonical Action Run proof. Repeated or nonempty-state initialization preserves existing carriers and returns a truthful refusal. The ordinary Release Version Workflow then has a verified active N baseline; fixture-only evidence does not close CA-P-1624.
