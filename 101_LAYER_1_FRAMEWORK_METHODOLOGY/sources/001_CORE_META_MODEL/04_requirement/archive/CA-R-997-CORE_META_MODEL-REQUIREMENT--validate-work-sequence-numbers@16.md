---
subjects:
  governs: "Work Sequence Number"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Work Sequence Number"
    - "Hub Atom"
version: 16
updated_at: "2026-09-22 14:41:44 +0000"
relations:
  child_of:
    - CA-R-991
    - CA-R-992
atom_id: "CA-R-997"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Validate Work Sequence Numbers

**every** supplied Work Sequence Number **must** be a unique positive ordinal among direct Plans decomposing the same Hub **or** sharing the same top-level Plan container.
