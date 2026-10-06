---
subjects:
  governs: "Artifact/Carrier Placement"
  depends_on:
    - "Artifact/Activity"
    - "Artifact/Revision/Status"
    - "Atom/Content Role: Delivery"
version: 3
updated_at: "2026-09-20 23:55:10 +0000"
relations: {"relates_to": ["CA-D-461"]}
atom_id: "CA-D-466"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Place Carriers by Applicable Status Delivery

**when** Activity applies **and** an Artifact has **`=1`** valid current Revision Status, its Carrier placement **must** follow the most specific applicable Delivery rule for that Artifact Type; **only when** no more specific mapping exists, Active uses the canonical current directory **and** another Status uses its lowercase Status subdirectory. **when** Activity does **not** apply, Carrier placement **must not** derive a Status directory from absent Activity.
