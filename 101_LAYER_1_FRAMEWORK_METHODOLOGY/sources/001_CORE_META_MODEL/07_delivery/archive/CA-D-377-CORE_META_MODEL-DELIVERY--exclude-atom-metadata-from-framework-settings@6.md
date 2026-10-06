---
subjects:
  governs: "Framework Instance Settings/Carrier/Atom metadata exclusion"
  depends_on:
    - "Framework Instance Settings"
    - "Atom"
    - "Artifact/Revision"
version: 6
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-377"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Exclude Atom metadata from Framework Instance Settings

the Framework Instance Settings TOML Carrier **must not** contain Atom Frontmatter, Atom ID, Atom Revision metadata, Atom relations, rationale, **or** provenance; its Revision binding follows CA-D-360.
