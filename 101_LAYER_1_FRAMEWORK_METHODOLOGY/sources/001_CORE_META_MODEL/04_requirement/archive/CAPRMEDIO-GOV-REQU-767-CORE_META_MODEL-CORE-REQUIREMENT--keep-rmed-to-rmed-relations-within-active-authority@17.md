---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 17
updated_at: 2026-09-07 09:59:57 +0000
relations:
  child_of:
    - CA-R-1051
atom_id: "CAPRMEDIO-GOV-REQU-767"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Keep RMED-to-RMED Relations within Active Authority

**if** a direct relation is authored by an Active Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery) **and** targets an Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery), **then** the target Atom **must** be Active.
