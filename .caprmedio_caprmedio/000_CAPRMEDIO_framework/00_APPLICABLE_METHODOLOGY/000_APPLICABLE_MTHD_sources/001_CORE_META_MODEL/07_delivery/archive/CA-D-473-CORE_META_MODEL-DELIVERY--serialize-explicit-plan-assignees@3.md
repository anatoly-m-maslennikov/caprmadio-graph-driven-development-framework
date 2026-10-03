---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Assignee/Carrier"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Assignee"
    - "File Carrier"
version: 3
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"relates_to": ["CA-R-1584", "CA-R-1585"]}
atom_id: "CA-D-473"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Serialize explicit Plan Assignees

a Plan File Carrier **may** serialize **=1** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585 for its own work rather than copying the default.
