---
subjects:
  governs: "Atom/Global Tier"
  depends_on:
    - "Atom"
    - "Scope Unit"
    - "Atom/Content Role"
version: 3
updated_at: "2026-09-21 15:52:17 +0000"
relations: {"relates_to": ["CA-R-1444", "CA-R-917"]}
atom_id: "CA-R-1573"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Govern greater Global Tiers within each Scope Unit

**in** **every** Scope Unit, **every** Atom at Global Tier `N` **must** govern **all** Atoms at Global Tiers **`>N`**, across **all** Content Roles.
