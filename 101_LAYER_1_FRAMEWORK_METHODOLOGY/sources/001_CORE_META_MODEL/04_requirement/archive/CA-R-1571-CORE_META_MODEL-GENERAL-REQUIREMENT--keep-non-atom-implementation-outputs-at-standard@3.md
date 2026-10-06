---
subjects:
  governs: "Artifact/Local Tier"
  depends_on:
    - "Artifact"
    - "Atom"
    - "Implementation"
    - "Projection"
    - "Atom/Local Tier: Standard"
version: 3
updated_at: "2026-09-21 00:57:42 +0000"
relations: {"relates_to": ["CA-R-660", "CA-R-1568"]}
atom_id: "CA-R-1571"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Keep non-Atom Implementation outputs at Standard

a non-Atom Implementation Artifact **must** resolve **to** Local Tier Standard, including a delivered Projection.

this derived classification does **not** add an Atom Content Role **or** Atom identity **to** the Artifact **and** does **not** change the authority **or** tier of represented source content.
