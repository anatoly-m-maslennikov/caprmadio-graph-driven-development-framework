---
atom_id: CA-C-447
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: resolved
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 09:45:00 +0000"
subjects:
  governs: "Applicable Methodology Projection relocation"
  depends_on: [Projection, Implementation, Evaluation]
relations:
  concern_about: [CA-P-1549, CA-P-1556, CA-P-1519, CA-P-1123]
---
# Summary

Record denied Applicable Methodology Projection relocation

## Concern

The first Applicable Methodology role-directory relocation was denied. The Operator then withdrew that relocation and retained its original canonical framework location.

## Evidences

CA-P-1549 encountered rename EPERM, errno 1, Operation not permitted, from .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/04_requirement to .caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY/04_requirement. It stopped immediately without retry or alternate method. The earlier 102 registered Projection moves are byte-verified and committed in 615b49250, not rolled back. The 963 original Applicable Methodology source links remain valid and unchanged. CA-P-1556 saves an evidence-only map of this partial state; its helper has no relocation operations.

## Blast radius

The historical denied move is not claimed complete. It no longer blocks closure because the Operator selected the original location as an explicit exception. D550@3, D326@15 and Project Structure now retain that location; current compilation and remaining legacy accounting are verified separately. No equivalent move, deletion or permission bypass occurred.

## Disposition

Resolved by the Operator's location decision, not by execution of the denied rename. Preserve the original source folder, canonical role folders, historical migration evidence and extra untracked copy. The extra copy is not selected as another canonical Projection; any reconciliation requires a scoped check.
