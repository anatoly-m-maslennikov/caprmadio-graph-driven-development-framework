---
atom_id: CA-P-1623
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Implement Release Version from reviewed RMED"
  depends_on: [Workflow, Action, Tool, Methodology, Implementation, Projection, Skill, Journal]
version: 1
updated_at: "2026-10-05 01:43:00 +0000"
relations:
  is_decomposition_of: [CA-P-1620]
  blocks: [CA-P-1624]
---
# Summary

Implement Release Version from reviewed RMED

## Objective

Within <=15 minutes per bounded implementation slice, implement the independently accepted Release Version contract using existing components.

## Details

Own only the release capability implementation/tests and necessary additive discovery/MCP/orchestrator bindings. Begin with golden E2E tests and mocks for complete copy/compile/test/install/Skill/image flow and non-happy cases. Preserve current fifteen-route contracts unless reviewed source explicitly extends them. Bind full package Version/digests and enforce source/settings/Journal preservation, rollback and no old-image deletion before successful new installation/image verification. Do not provision around C449, retry C447, publish images, deploy or force-remove shared images. Decompose into <=15-minute slices before work exceeding the bound.

## Definition of Done

Reviewed source is implemented with focused passing golden tests, source-current bindings, truthful shared Run outputs and exact implementation diff. Mock/development proof is labeled separately from actual install/Docker proof.
