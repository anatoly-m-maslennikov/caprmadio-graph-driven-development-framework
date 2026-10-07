---
atom_id: CA-P-1826
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-07 21:05:19 +0000"
subjects:
  governs: "Verify and execute the authorized baseline restoration"
  depends_on: [Action, Tool, Framework Package, Docker Image, Journal, Operator]
relations:
  is_decomposition_of: [CA-P-1820]
---
# Summary

Verify and execute the authorized baseline restoration

## Objective

Independently review the assembled code against the accepted RMED/O, refresh necessary source admission, then execute the single Operator-authorized native restoration and verify its actual image/proof/selector/Journal result.

## Details

The Operator explicitly approved rebuilding the missing selected image from verified retained N and registering its verified image digest. Preserve N's package, Version, public ca Skill, original proof and historical Journal. N21 remains unknown and is not replayed. No release gate is waived. Root owns Git, source admission and serialized runtime effects; independent workers own their assigned source scopes.

Work estimate: <=15 minutes; add a necessary remainder before expanding beyond this bound. Source RMED is reviewed before implementation. Test-first acceptance uses honest local doubles separately from actual Docker proof.

## Definition of Done

Actual immutable build/inspect/canary and canonical started/terminal receipts prove the selected unchanged N package works with the verified result. All retained identities/currentness checks pass. A new source-bound Release can be admitted; no Unit, E2E, Full Gate, promotion or Epic closure is implied.

