---
atom_id: CA-P-1825
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 1
updated_at: "2026-10-07 21:19:22 +0000"
subjects:
  governs: "Write restoration golden and regression tests"
  depends_on: [Action, Tool, Framework Package, Docker Image, Journal, Operator]
relations:
  is_decomposition_of: [CA-P-1820]
  blocks: [CA-P-1822, CA-P-1823, CA-P-1824]
---
# Summary

Write restoration golden and regression tests

## Objective

Create real-byte retained-N golden fixtures and tests for the accepted restoration ABI before implementation; observe expected initial failures, then retain complete success/refusal/partial/recovery and existing-boundary regression coverage.

## Details

The Operator explicitly approved rebuilding the missing selected image from verified retained N and registering its verified image digest. Preserve N's package, Version, public ca Skill, original proof and historical Journal. N21 remains unknown and is not replayed. No release gate is waived. Root owns Git, source admission and serialized runtime effects; independent workers own their assigned source scopes.

Work estimate: <=15 minutes; add a necessary remainder before expanding beyond this bound. Source RMED is reviewed before implementation. Test-first acceptance uses honest local doubles separately from actual Docker proof.

## Definition of Done

Tests cover unchanged package/Skill, same and different image IDs, filtered context, tamper/drift/shared-lock cases, timeout/partial/recording recovery and O180 preservation. Initial missing-implementation failure is retained; final focused tests pass without claiming real Docker proof.

