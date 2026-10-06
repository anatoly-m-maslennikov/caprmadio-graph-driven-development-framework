---
subjects:
  governs: "Session-State Envelope"
  depends_on:
    - "runtime"
version: 17
updated_at: "2026-09-10 07:34:05 +0400"
relations: {}
atom_id: "CAPRMEDIO-GOV-REQU-371"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define the bounded session-state envelope

the bounded session-state envelope **must** contain **only** routing invariants, current scope, applicable settings, compact session state, **and** references needed **to** load active authority on demand.
