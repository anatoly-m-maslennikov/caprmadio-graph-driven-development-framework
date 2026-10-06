---
subjects:
  governs: "Directory Carrier"
  depends_on:
    - "Artifact"
    - "Structural Entity"
    - "Atom/Revision"
version: 3
updated_at: "2026-09-20 23:55:10 +0000"
relations: {"relates_to": ["CA-D-259", "CA-D-460"]}
atom_id: "CA-D-464"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Represent One Governed Object with Each Directory Carrier

**every** represented Directory Carrier **must** carry **`=1`** governed object Revision: either one Structural Entity Revision **or**, where an applicable Delivery rule permits it, one Atom Revision; it **must not** establish a second object merely because it contains subordinate Carriers.
