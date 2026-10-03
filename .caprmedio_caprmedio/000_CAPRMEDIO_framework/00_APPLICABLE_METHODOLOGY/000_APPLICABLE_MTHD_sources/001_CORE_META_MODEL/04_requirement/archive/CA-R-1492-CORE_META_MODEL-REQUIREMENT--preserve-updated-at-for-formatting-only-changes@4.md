---
subjects:
  governs: "Atom/Revision/Updated At"
  depends_on:
    - "Atom/Revision"
    - "Artifact/Carrier"
version: 4
updated_at: "2026-09-28 06:30:40 +0400"
relations:
  child_of:
    - CA-R-1416
atom_id: "CA-R-1492"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Archived"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 11
---
# Preserve Updated At for formatting-only changes

a change **to** an Atom Carrier that changes **only** formatting **or** lossless serialization **must** preserve the Atom's Updated At value.
