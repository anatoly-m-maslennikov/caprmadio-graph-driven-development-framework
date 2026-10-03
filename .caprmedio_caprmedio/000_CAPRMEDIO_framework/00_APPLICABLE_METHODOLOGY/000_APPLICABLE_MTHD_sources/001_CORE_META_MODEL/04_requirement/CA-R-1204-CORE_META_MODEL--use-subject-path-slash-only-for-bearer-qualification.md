---
subjects:
  governs: "Subject Path"
  depends_on:
    - "Dependent Entity"
    - "IS_BORNE_BY"
    - "Entity"
version: 14
updated_at: "2026-10-02 21:30:43 +0400"
relations: {}
atom_id: "CA-R-1204"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Use Subject Path Slash Only for Bearer Qualification

## Scope

a Subject Path.

## Claim

**in** a Subject Path, `/` **must** express **only** **`=1`** IS_BORNE_BY edge from the following Dependent Entity occurrence **to** the immediately preceding qualified Entity occurrence.

## Details
