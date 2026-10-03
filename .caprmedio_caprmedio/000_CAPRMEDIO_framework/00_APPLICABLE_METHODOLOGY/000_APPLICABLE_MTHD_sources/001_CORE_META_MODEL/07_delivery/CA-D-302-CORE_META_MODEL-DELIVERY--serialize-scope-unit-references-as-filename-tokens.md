---
subjects:
  governs: "Atom/Scope/Filename Token"
  depends_on:
    - "Scope Unit/Name"
    - "Project Configuration"
version: 13
updated_at: "2026-09-29 22:20:38 +0000"
relations: {}
atom_id: "CA-D-302"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary
Serialize Scope Unit References as Filename Tokens

## Scope
Scope Unit references serialized **in** Atom filenames.

## Claim

**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Project Configuration.

## Details
