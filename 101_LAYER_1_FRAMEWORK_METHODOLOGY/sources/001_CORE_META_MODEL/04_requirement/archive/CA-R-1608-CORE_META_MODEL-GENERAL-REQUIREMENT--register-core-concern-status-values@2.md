---
atom_id: CA-R-1608
content_role: Requirement
type: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Atom/Content Role: Concern/Status"
  depends_on:
    - "Atom/Content Role: Concern"
    - "Artifact/Revision/Status"
version: 2
updated_at: "2026-09-23 21:34:42 +0000"
relations:
  relates_to:
    - CA-R-1308
    - CA-R-1313
    - CA-R-1336
---
# Summary

Register Core Concern Status Values

## Claim

the Core allowed values of `Atom/Content Role: Concern/Status` **must** be exactly (`draft`, `active`, `resolved`, `canceled`).
