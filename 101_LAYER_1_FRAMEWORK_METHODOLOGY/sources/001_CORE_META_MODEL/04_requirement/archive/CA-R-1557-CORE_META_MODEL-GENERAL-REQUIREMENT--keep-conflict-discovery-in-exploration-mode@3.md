---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Operator"
    - "Exploration Mode"
    - "Atom/Content Role: Concern"
version: 3
updated_at: "2026-09-21 00:39:50 +0000"
relations: {"child_of":["CAPRMEDIO-META-REQU-114"]}
atom_id: "CA-R-1557"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Keep conflict discovery in Exploration Mode

an AI Agent **must** keep a discovered conflict **in** Exploration Mode; it **may** create a Concern for that conflict **only** **when** the Operator requests persistence **or** defers its resolution.
