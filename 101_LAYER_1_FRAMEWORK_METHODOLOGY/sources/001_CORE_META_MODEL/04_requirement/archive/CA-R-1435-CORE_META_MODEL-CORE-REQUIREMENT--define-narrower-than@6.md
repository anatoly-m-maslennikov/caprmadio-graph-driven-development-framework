---
subjects:
  governs: "NARROWER_THAN"
  depends_on:
    - "Term"
    - "Terms Graph"
    - "Relation"
    - "Property"
    - "Definition Atom"
version: 6
updated_at: "2026-09-13 03:24:04 +0400"
relations: {}
atom_id: "CA-R-1435"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define NARROWER_THAN

a NARROWER_THAN Relation from Term A **to** Term B **in** the Terms Graph **means** that, under their governing definitions, **if** Term A applies **to** a referent, **then** Term B applies **to** the same referent; this Relation does **not** express Property ownership **or** allowed-value membership.
