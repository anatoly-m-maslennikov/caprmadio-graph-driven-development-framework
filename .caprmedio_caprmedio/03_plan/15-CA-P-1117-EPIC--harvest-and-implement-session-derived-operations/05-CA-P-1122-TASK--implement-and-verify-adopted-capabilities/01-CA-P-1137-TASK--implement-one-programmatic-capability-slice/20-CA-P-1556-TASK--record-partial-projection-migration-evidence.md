---
atom_id: CA-P-1556
content_role: Plan
type: Plan
label: Task
work_sequence_number: 20
current_scope_unit: caprmedio
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Record partial Projection migration evidence"
  depends_on: [Projection, Implementation, Evaluation]
version: 2
updated_at: "2026-10-04 22:46:18 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1549]
---
# Summary

Record partial Projection migration evidence

## Objective

Within <=15 minutes, save an exact accounting of completed moves without retrying the denied operation.

## Details

Saved result: evidence-only map SHA-256 f8529bcc8f385cd7b02d13135507128ad00774045f3f4f63e3c8715b3b40168f records all 102 R100 moves from 615b49250 against exact predecessor 90142fa49141d2a1348a60abd401ecc0126df442 and current bytes: 55,288,394 matching bytes. All 963 original Applicable Methodology links remain unchanged. It explicitly records rename EPERM/errno 1, untouched legacy manifest and no aggregate completion. The helper writes only this map and has no relocation or rollback operations. CA-P-1549 remains Active; this packet did not retry its denied operation.

Inputs: CA-P-1549's partial result and commit 615b49250. Own only the narrow migration helper and .caprmedio_caprmedio/_projection/migration/CA-P-1549-project-projection-carrier-map.json. Compare the 102 moved historical view carriers with their exact Git predecessor bytes, save old/new path and SHA-256 mappings, and explicitly record incomplete Applicable Methodology relocation, unmodified source links, and legacy-manifest remainder. Missing or changed bytes must fail truthfully. Do not move, rename, delete, roll back, rebase or retry any carrier, particularly the denied Applicable Methodology directory operation. Do not change native Implementation, canonical manifest, Journal, authority or other workers' files. Preserve completed moves now committed by another transaction. Root saves Plans and Concerns.

Inherit CA-P-1117's 90% confidence threshold and mechanical Git exception. You are not alone; preserve other edits and use apply_patch. No FPF, harvesting, permission bypass or aggregate completion claim.

## Definition of Done

The durable partial map accurately distinguishes byte-verified completed moves from denied or untouched work.
