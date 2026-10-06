---
subjects:
  governs: "Atom/Revision/Updated At"
  depends_on:
    - "Atom/Revision"
    - "Artifact/Carrier"
version: 3
updated_at: "2026-09-17 02:03:25 +0000"
relations:
  child_of:
    - CA-R-1416
atom_id: "CA-R-1492"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Preserve Updated At for formatting-only changes

a change **to** an Atom Carrier that changes **only** formatting **or** lossless serialization **must** preserve the Atom's Updated At value.
