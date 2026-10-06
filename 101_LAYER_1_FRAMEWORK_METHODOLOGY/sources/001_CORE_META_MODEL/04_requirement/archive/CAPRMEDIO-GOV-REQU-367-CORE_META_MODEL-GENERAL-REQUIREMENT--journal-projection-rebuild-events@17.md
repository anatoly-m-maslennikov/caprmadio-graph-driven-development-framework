---
subjects:
  governs: "Projection Rebuild"
  depends_on:
    - "Work Journal/Action"
    - "Projection"
    - "Journal/Record"
version: 17
updated_at: "2026-09-17 04:08:48 +0000"
relations: {}
atom_id: "CAPRMEDIO-GOV-REQU-367"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Journal Projection Rebuild Events

**every** Projection Rebuild **must** have **`=1`** Work Journal Action whose terminal Event records the rebuild outcome.

acceptance of that Event into the Journal does **not**, by itself, make the Projection current. currentness remains subject **to** the Projection's applicable source **and** validation requirements; the accepted Event preserves the observed outcome **without** replacing those requirements.
