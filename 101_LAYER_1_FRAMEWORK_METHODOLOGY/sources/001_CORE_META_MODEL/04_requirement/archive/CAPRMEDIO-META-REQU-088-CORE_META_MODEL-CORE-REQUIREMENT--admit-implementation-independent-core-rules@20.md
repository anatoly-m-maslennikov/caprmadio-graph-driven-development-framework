---
subjects:
  governs: "authority"
  depends_on: []
version: 20
updated_at: "2026-09-10 06:29:38 +0400"
relations:
  child_of:
    - CA-M-001
atom_id: "CAPRMEDIO-META-REQU-088"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Admit implementation-independent Core rules

a reusable model rule belongs **in** CORE_META_MODEL **only** **when** it establishes reusable methodology authority **and** remains independent of implementation choices outside the Entity explicitly governed by its Claim. a Carrier format, mechanism, portability boundary, **or** external constraint **may** be named **when** that Entity itself is governed, but **must not** become a hidden prerequisite of unrelated Claims. Project-specific implementation choices **must not** be imported as reusable methodology authority.
