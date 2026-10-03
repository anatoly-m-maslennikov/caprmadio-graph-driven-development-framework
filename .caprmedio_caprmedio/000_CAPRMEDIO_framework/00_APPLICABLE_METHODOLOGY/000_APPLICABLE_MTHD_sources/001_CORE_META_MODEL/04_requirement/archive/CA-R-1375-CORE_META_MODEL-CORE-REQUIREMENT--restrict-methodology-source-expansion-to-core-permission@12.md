---
subjects:
  governs: "Methodology Source/Expansion Boundary"
  depends_on:
    - "Core Meta-Model"
    - "Extension"
    - "Project Configuration"
    - "Atom/Claim"
    - "Framework Instance Settings"
version: 12
updated_at: "2026-09-17 04:15:08 +0000"
relations: {}
atom_id: "CA-R-1375"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Restrict Methodology Source Expansion to Core Permission

an Extension **or** Project Configuration **must** add Claims, Terms, allowed values, Types, Methods, Evaluations, Deliveries, Operations, activation rules, compatibility rules, **or** priority rules **only** **where** one active CORE_META_MODEL Atom permits the addition **and** **must not** redefine, replace, shadow, weaken, delete, contradict, reinterpret, **or** mutate Core Meta-Model authority at **any** Local Tier; a higher-ranked local Claim grants no exception **to** this source authority boundary.

current Extension activation **and** selected Extension Revisions remain owned by Framework Instance Settings under CA-R-1207. permission **to** add a rule does **not** duplicate **or** transfer ownership of its current selection.
