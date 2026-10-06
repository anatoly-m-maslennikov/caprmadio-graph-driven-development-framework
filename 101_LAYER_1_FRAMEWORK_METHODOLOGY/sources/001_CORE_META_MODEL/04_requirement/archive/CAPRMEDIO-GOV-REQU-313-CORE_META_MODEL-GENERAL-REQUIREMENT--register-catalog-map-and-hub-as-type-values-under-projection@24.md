---
subjects:
  governs: "Projection/Type"
  depends_on:
    - "Projection"
    - "Type"
    - "Projection/Type: Catalog"
    - "Projection/Type: Map"
    - "Projection/Type: Hub"
    - "Atom/Claim"
version: 24
updated_at: "2026-09-13 14:15:09 +0400"
relations: {}
atom_id: "CAPRMEDIO-GOV-REQU-313"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Register Catalog, Map, and Hub as Type Values under Projection

Catalog, Map, **and** Hub **must** be distinct Type values under Projection with no authority over linked Artifact Claims.

a derived terminology list **or** vocabulary diagnostic index **must** use Catalog as its Projection Type; its purpose **and** selected population do **not** admit another Type.
