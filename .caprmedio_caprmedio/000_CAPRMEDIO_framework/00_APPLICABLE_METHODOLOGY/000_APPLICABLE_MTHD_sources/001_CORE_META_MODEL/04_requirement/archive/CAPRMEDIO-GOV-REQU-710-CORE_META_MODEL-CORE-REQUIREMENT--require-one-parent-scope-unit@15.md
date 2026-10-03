---
subjects:
  governs: "scope-topology"
  depends_on:
    - "authority"
version: 15
updated_at: "2026-09-10 04:16:18 +0400"
relations: {}
atom_id: "CAPRMEDIO-GOV-REQU-710"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Require one parent Scope Unit

**every** Scope Unit except a Scope Unit root **must** have **`=1`** direct parent Scope Unit.
