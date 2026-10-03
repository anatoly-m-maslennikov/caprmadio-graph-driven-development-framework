---
atom_id: CA-R-1610
content_role: Requirement
type: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Revision/Status"
  depends_on:
    - "Atom/Claim"
    - "Implementation"
    - "Projection"
    - "Single Source of Truth"
    - "Spec Content Roles"
version: 1
updated_at: "2026-09-23 21:40:21 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-R-1470
    - CAPRMEDIO-META-REQU-657
---
# Summary

Keep reverse-engineered RMED provisional

## Claim

RMED Claims reconstructed from existing Implementation **or** its Projections **must** remain proposed Draft Claims **until** accepted through the applicable Atom acceptance authority.

- extraction **or** inference alone does **not** establish Active authority.
- the accepted RMED, **not** the legacy Implementation **or** its Projection, governs subsequent refactoring **and** Evaluation of the result.
