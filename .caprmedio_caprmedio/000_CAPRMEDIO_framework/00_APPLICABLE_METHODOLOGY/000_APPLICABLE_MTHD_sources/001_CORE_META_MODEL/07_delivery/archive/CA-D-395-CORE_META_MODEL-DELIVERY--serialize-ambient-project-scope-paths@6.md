---
subjects:
  governs: "Carrier/Representation"
  depends_on:
    - "Project"
    - "Scope Unit"
version: 6
updated_at: "2026-09-10 20:55:21 +0400"
relations: {}
atom_id: "CA-D-395"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Serialize Ambient Project Scope Paths

a Carrier encoding of `scope_path` **must** omit the ambient current Project **and** use an empty path for Project Scope.
