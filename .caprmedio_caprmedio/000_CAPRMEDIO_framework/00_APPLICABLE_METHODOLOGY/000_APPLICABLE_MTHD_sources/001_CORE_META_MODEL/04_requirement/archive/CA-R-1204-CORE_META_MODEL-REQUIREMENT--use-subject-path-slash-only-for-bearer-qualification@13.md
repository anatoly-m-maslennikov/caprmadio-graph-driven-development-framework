---
subjects:
  governs: "Subject Path"
  depends_on:
    - "Dependent Entity"
    - "IS_BORNE_BY"
    - "Entity"
version: 13
updated_at: "2026-09-17 17:16:41 +0000"
relations: {}
atom_id: "CA-R-1204"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Use Subject Path Slash Only for Bearer Qualification

**in** a Subject Path, `/` **must** express **only** one IS_BORNE_BY edge from the following Dependent Entity occurrence **to** the immediately preceding qualified Entity occurrence.
