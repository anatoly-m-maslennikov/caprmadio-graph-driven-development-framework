---
atom_id: CA-E-546
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Summary Handoff"
  depends_on: ["Atom", "Atom/Summary", "Atom/Revision"]
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
relations:
  evaluation_for: [CA-R-1825, CA-R-1826]
---
# Summary

Verify Summary-to-Replace handoff

## Scope

One sealed Update request that changes its Summary.

## Claim

Verify the dispatcher returns `replace_handoff` with the exact predecessor and proposed successor inputs, performs no same-ID update, and preserves the predecessor unchanged in preview. Apply an admitted Replace through the native Tool and verify explicit predecessor/successor lineage and observed history. Verify an unchanged Summary selects Update only when its native class permits it.

## Details

### Acceptance criteria

No Summary-changing request silently mutates the existing Atom identity. Replace results have both carrier identities; preview has neither mutation nor invented history.
