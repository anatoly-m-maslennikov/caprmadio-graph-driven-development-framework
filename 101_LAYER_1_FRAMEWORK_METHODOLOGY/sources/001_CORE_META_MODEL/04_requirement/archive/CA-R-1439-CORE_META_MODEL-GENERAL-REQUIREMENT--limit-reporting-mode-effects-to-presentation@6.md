---
subjects:
  governs: "Framework Instance Settings/interaction/reporting mode/effects"
  depends_on:
    - "Framework Instance Settings/interaction/reporting mode"
    - "Artifact"
version: 6
updated_at: "2026-09-11 18:18:55 +0400"
relations:
  child_of:
    - "CA-R-1402"
atom_id: "CA-R-1439"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Limit reporting mode effects to presentation

the interaction reporting mode **must** affect presentation **only**, **without** changing authorization, Artifact creation, workflow routing, validation, **or** safety behavior.
