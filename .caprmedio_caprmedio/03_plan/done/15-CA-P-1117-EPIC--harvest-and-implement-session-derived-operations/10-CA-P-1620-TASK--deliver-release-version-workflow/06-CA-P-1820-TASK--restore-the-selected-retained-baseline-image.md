---
atom_id: CA-P-1820
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
  governs: "Restore the selected retained baseline image"
  depends_on: [Action, Tool, Framework Package, Docker Image, Journal, Operator]
relations:
  is_decomposition_of: [CA-P-1620]
  blocks: [CA-P-1623]
---
# Summary

Restore the selected retained baseline image

## Objective

Deliver and execute the narrowly authorized same-package image restoration so the full required Release chain can continue. Required children CA-P-1821 through CA-P-1826 cover source authority, test-first fixtures, retained producer, closed direct Journal/publication integration, coordinator and actual restoration.

## Details

The Operator explicitly approved rebuilding the missing selected image from verified retained N and registering its verified image digest. Preserve N's package, Version, public ca Skill, original proof and historical Journal. N21 remains unknown and is not replayed. No release gate is waived. Root owns Git, source admission and serialized runtime effects; independent workers own their assigned source scopes.

Work estimate: composite; execute its bounded children. Source RMED is reviewed before implementation. Test-first acceptance uses honest local doubles separately from actual Docker proof.

## Definition of Done

All required children are Done with independently accepted source/code, actual verified image and canonical direct-Action receipts. The selected binding is accepted by the unchanged retained reader and installed-N image admission. This composite does not close the Release or Epic; subsequent fresh Release, runtime coverage, final audit and closure remain required.

