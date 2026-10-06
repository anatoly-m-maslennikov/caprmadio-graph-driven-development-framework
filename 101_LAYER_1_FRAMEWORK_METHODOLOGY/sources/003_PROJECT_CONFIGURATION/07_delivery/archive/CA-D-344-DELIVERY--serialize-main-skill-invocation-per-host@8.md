---
subjects:
  governs: "CAPRMEDIO Main Skill/Host Invocation"
  depends_on:
    - "CAPRMEDIO Main Skill"
version: 8
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
atom_id: "CA-D-344"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Serialize Main Skill Invocation per Host

for the CAPRMEDIO Main Skill, the Host Invocation **must** serialize as `$ca` **in** Codex; **if** a Claude compatibility Extension **or** Operator-provided compatibility layer is separately authorized by the Operator, **then** its Host Invocation **must** serialize as `/ca` **in** Claude.
