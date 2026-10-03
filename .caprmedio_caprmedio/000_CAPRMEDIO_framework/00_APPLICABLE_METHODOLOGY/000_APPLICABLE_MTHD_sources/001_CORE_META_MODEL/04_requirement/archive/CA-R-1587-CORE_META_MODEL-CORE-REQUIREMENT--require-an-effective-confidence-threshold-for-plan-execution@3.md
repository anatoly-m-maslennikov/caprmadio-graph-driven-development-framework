---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Autonomous Confidence Threshold"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Autonomous Confidence Threshold"
    - "Operator"
    - "Framework Instance Settings"
version: 3
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"relates_to": ["CA-M-271", "CA-R-1044"]}
atom_id: "CA-R-1587"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Require an effective confidence threshold for Plan execution

**every** autonomous Plan execution decision **must** resolve **=1** effective Autonomous Confidence Threshold from its applicable explicit **or** inherited source under CA-M-271.
