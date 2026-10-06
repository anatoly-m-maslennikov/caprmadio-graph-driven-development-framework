---
subjects:
  governs: "Atom/Revision/Status: Draft/Filename"
  depends_on:
    - "Atom/Identifier"
version: 11
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
atom_id: "CA-D-288"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Serialize Draft Atom Filenames with an Empty Number

**every** Project-owned Draft Atom filename **must** use `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>--` **before** its mutable components **and** **must not** carry an assigned Atom ID.
