---
subjects:
  governs: "Projection/Carrier/Updated At"
  depends_on: []
version: 10
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
atom_id: "CA-D-310"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Serialize Projection Updated At

**every** Projection Carrier **must** serialize the time of its latest completed rebuild as `updated_at` **in** Project time **without** treating that value alone as proof of currentness.
