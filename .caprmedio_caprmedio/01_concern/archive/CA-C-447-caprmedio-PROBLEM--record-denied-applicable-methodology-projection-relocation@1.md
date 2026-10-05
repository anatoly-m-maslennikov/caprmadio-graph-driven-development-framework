---
atom_id: CA-C-447
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: 2026-10-04 23:51:27
subjects:
  governs: "Applicable Methodology Projection relocation"
  depends_on: [Projection, Implementation, Evaluation]
relations:
  concern_about: [CA-P-1549, CA-P-1556, CA-P-1519, CA-P-1123]
---
# Summary

Record denied Applicable Methodology Projection relocation

## Concern

The first Applicable Methodology role-directory relocation was denied by the filesystem. The affected migration remains incomplete.

## Evidences

CA-P-1549 encountered rename EPERM, errno 1, Operation not permitted, from .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/04_requirement to .caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY/04_requirement. It stopped immediately without retry or alternate method. The earlier 102 registered Projection moves are byte-verified and committed in 615b49250, not rolled back. The 963 original Applicable Methodology source links remain valid and unchanged. CA-P-1556 saves an evidence-only map of this partial state; its helper has no relocation operations.

## Blast radius

Full carrier-cutover and image closure cannot claim the denied migration complete. Independent native capabilities and queue work continue. The active managed profile does not allow permission escalation; no equivalent move, deletion or rewrite bypass is authorized.
