---
subjects:
  governs: "Hub Atom"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Type"
    - "Atom/Content Role: Plan/Type: Plan/Subtype"
    - "Atom/Global Tier"
version: 3
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"relates_to": ["CA-R-1579", "CA-R-1534"]}
atom_id: "CA-R-1578"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define Hub Atom as a derived description

Hub Atom **means** a derived description of an Atom with **>0** outgoing `DECOMPOSES_INTO` Relations; it does **not** introduce another Type, Subtype, stored classification, identity, **or** authority tier. related Atoms retain their own Claims rather than becoming parts of the Hub Claim.
