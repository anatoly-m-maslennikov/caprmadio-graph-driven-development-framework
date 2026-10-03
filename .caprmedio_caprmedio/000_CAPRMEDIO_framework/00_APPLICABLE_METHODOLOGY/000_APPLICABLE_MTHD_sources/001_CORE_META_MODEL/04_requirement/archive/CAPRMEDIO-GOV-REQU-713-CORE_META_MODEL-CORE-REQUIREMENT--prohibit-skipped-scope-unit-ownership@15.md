---
subjects:
  governs: "scope-topology"
  depends_on:
    - "authority"
version: 15
updated_at: "2026-09-10 04:16:18 +0400"
relations: {}
atom_id: "CAPRMEDIO-GOV-REQU-713"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Prohibit skipped Scope Unit ownership

a Scope Unit **must not** own a descendant Scope Unit through a stored structural-parent relation **when** another active Scope Unit lies between them.
