---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 12
updated_at: "2026-09-10 06:39:08 +0400"
relations: {}
atom_id: "CA-R-1030"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Prohibit silent non-compatible Impact dispositions

TOOLING **must not** select `update_required`, `replacement_required`, **or** `uncertain` **without** an explicit governed disposition.
