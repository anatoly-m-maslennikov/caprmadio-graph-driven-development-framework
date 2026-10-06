---
subjects:
  governs: "Atom/Claim/Target Scope Unit"
  depends_on:
    - "Atom/Claim"
    - "Scope Unit"
    - "Project Structure"
version: 20
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  child_of:
    - CAPRMEDIO-REQU-045
atom_id: "CA-R-718"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Separate Atom Claim Scope from structural ownership

an Atom's Claim Target Scope Unit reference **and** applicability restrictions **in** its Claim text **must not**, by themselves, establish an additional edge **in** the Scope Unit tree **or** alter structural-parent ownership.
