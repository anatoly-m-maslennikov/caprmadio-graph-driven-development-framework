---
subjects:
  governs: "Implementation Binding"
  depends_on:
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Atom/Claim"
version: 4
updated_at: "2026-09-17 11:52:27 +0000"
relations: {}
atom_id: "CA-R-1504"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Keep Evaluation implementation coverage explicit

coverage between Evaluation Atoms **and** their realizations **may** be many-to-many **only** with explicit attribution:

- **`=1`** Evaluation Atom **may** be realized by multiple distinct implementations.
- **`=1`** implementation **may** realize multiple Evaluation Atoms **only** **when** its result remains attributable **to** **every** covered Claim.

a shared implementation **must not** make its covered Claims **or** their result attribution implicit. this Claim governs coverage, **not** a new Carrier **or** a second implementation registry.
