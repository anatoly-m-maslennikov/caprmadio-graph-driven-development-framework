---
subjects:
  governs: "Compatible Lineage Impact Disposition"
  depends_on:
    - "atom-boundary"
    - "relation-model"
version: 14
updated_at: "2026-09-10 06:39:08 +0400"
relations: {}
atom_id: "CA-R-1033"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define compatible Lineage Impact disposition

`compatible` **means** the child remains valid against the parent Revision required by the gate **and** traversal stops on that branch **without** a child update. **if** the gate requires the revised parent, **then** compatibility **must** be established against that new Revision; permission **to** consume a pinned earlier Revision **must not** establish compatibility for a gate that requires the new Revision.
