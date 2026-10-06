---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Assignee"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Actor"
    - "Hub Atom"
version: 3
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"relates_to": ["CA-R-1575"]}
atom_id: "CA-R-1584"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Require an effective Assignee for Plan work

**every** Plan Atom with its own work content **must** have **=1** effective Assignee; a pure Hub **without** its own work does **not** require an additional Assignee merely because it organizes other Plans.
