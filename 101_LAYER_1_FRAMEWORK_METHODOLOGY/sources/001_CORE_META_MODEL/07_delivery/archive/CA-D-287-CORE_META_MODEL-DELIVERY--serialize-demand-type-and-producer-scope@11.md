---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/filename"
  depends_on:
    - "Producer/Scope Unit"
version: 11
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
atom_id: "CA-D-287"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Serialize Demand Type and Producer Scope

**every** Demand Atom filename **must** serialize its Type **and** Producer Scope as `DEMANDS_FROM-<PRODUCER_SCOPE>`.
