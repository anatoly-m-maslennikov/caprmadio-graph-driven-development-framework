---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Recursive Decomposition"
  depends_on:
    - "Atom/Content Role: Plan/Direct Work Decomposition"
version: 4
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"relates_to": ["CA-R-1579", "CA-R-1536"]}
atom_id: "CA-R-1537"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Derive Recursive Plan Decomposition by Transitive Closure

recursive Plan work decomposition **means** the transitive closure of direct `DECOMPOSES_INTO` Relations; it **must not** be authored as a second direct relation set.
