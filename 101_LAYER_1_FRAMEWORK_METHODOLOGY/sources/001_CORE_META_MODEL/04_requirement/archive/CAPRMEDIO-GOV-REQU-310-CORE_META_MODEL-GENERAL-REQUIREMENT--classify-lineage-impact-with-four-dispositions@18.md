---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 18
updated_at: "2026-09-14 06:21:07 +0400"
relations:
  relates_to:
atom_id: "CAPRMEDIO-GOV-REQU-310"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 10
---
# Classify lineage impact with four dispositions

**when** an Atom receives a new accepted Revision, **every** directly dependent child reached by the Impact Review **must** receive **`=1`** disposition from (`compatible`, `update_required`, `replacement_required`, `uncertain`).
