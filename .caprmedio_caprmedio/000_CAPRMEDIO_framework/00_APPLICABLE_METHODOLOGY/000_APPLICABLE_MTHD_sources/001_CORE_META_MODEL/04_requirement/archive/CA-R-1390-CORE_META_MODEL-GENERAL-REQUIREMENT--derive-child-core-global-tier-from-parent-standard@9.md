---
subjects:
  governs: "Atom/Global Tier"
  depends_on:
    - "Atom/Local Tier: Core"
    - "Scope Unit"
    - "Structural Parent Relation"
version: 9
updated_at: "2026-09-10 06:59:09 +0400"
relations: {}
atom_id: "CA-R-1390"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Derive Child Core Global Tier from Parent Standard

a Core Atom scoped **to** a non-Project Scope Unit **must** have a Global Tier one greater than the Standard Global Tier of its direct parent Scope Unit.
