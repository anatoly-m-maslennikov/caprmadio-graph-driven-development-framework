---
atom_id: CA-P-1822
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
version: 1
updated_at: "2026-10-07 21:05:19 +0000"
subjects:
  governs: "Implement the retained-context image producer"
  depends_on: [Action, Tool, Framework Package, Docker Image, Journal, Operator]
relations:
  is_decomposition_of: [CA-P-1820]
  blocks: [CA-P-1826]
---
# Summary

Implement the retained-context image producer

## Objective

Implement the producer that copies only authenticated persistent retained context and captures actual build, immutable-ID inspect and fixed canary evidence. Reuse existing bootstrap proof shapes and preserve old proof for exact same-ID results.

## Details

The Operator explicitly approved rebuilding the missing selected image from verified retained N and registering its verified image digest. Preserve N's package, Version, public ca Skill, original proof and historical Journal. N21 remains unknown and is not replayed. No release gate is waived. Root owns Git, source admission and serialized runtime effects; independent workers own their assigned source scopes.

Work estimate: <=15 minutes; add a necessary remainder before expanding beyond this bound. Source RMED is reviewed before implementation. Test-first acceptance uses honest local doubles separately from actual Docker proof.

## Definition of Done

Accepted producer tests prove filtered byte/mode currentness, truthful outcomes and canonical proof handling for both ID branches; no live-source input, fake digest or historical-proof overwrite is introduced.

