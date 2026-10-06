---
subjects:
  governs: "Structural Parent Relation"
  depends_on:
    - "Scope Unit"
    - "Project Structure"
    - "Structural Entity"
version: 16
updated_at: "2026-09-15 00:05:45 +0000"
relations: {}
atom_id: "CAPRMEDIO-GOV-REQU-717"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Register structural parent relation

the Structural Parent Relation **must** be the kind-independent Structural ownership relation directed from a child **to** its immediate parent. Project Structure owns Scope Unit parent declarations; structural graph views derive the corresponding `structural_parent` edge **without** maintaining a second source. a Carrier's physical containment **must not** silently replace a declared logical parent.
