---
atom_id: CA-E-546
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Summary Handoff"
  depends_on: ["Atom", "Atom/Summary", "Atom/Revision"]
version: 2
updated_at: "2026-10-04 23:01:23 +0400"
relations:
  evaluation_for: [CA-R-1825, CA-R-1826]
---
# Summary

Verify Summary-to-Replace handoff

## Scope

One sealed Update request that changes its Summary.

## Claim

Use one sealed CA-D-527 Update request whose proposed Summary differs. Verify it ends as a terminal non-effect `replace_handoff` with the exact predecessor and complete proposed successor inputs, performs no same-ID Update, invokes no Replace, and preserves the predecessor unchanged. Verify that a separately admitted new CA-D-527 Replace request needs fresh exact definition, input, currentness, and permission bindings before the native Tool applies it; the Update request's permission cannot authorize that Replace. Verify the admitted Replace preserves every successor Carrier, explicit predecessor/successor lineage, and observed history. Verify an unchanged Summary selects Update only when its native class permits it.

## Details

### Acceptance criteria

No Summary-changing request silently mutates the existing Atom identity or inherits Replace permission. The terminal handoff has no applied effect; a successful separately admitted Replace names the predecessor and every successor Carrier. Preview has neither mutation nor invented history.
