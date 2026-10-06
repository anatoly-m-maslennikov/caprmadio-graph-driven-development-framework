---
subjects:
  governs: "Atom/Subjects"
  depends_on:
    - "GOVERNS"
version: 11
updated_at: "2026-09-13 02:05:21 +0400"
relations: {}
atom_id: "CA-R-1201"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Require One Governed Subject on Every Atom

**every** Atom **must** declare **`=1`** direct GOVERNS target **in** its Subjects Property.
