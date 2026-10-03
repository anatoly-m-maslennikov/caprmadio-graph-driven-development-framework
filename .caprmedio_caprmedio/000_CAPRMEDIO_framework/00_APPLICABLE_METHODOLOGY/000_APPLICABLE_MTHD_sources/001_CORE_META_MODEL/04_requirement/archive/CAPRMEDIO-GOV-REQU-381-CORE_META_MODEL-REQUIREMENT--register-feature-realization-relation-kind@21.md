---
subjects:
  governs: "Feature Realization Relation"
  depends_on:
    - "atom-boundary"
    - "relation-model"
version: 21
updated_at: "2026-09-11 22:30:02 +0400"
relations:
  child_of:
    - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
    - CAPRMEDIO-META-REQU-152-CORE_META_MODEL-CORE-REQUIREMENT--preserve-strict-semantic-distinctions
atom_id: "CAPRMEDIO-GOV-REQU-381"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 11
---
# Register feature realization relation kind

`feature_realization` **must** be registered as a typed relation that maps a declared SPEC Feature Scope Unit **to** its applicable native Realization targets **without** making those targets Scope Units.
