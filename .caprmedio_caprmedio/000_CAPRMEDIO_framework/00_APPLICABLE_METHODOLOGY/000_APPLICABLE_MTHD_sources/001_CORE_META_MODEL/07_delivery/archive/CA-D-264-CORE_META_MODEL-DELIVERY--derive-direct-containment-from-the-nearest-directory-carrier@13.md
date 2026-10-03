---
subjects:
  governs: "Structural Entity/Direct Containment"
  depends_on:
    - "Containment Relation Pair"
    - "Directory Carrier/Nesting"
version: 13
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
atom_id: "CA-D-264"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Derive Direct Containment from the Nearest Directory Carrier

an Artifact Revision whose canonical Carrier is nested below a Directory Carrier **must** derive one direct `CONTAINS` **and** `IS_CONTAINED_BY` relation pair with the Structural Entity Revision carried by its nearest ancestor Directory Carrier.
