---
subjects:
  governs: "CAPRMEDIO Main Skill/Host Invocation"
  depends_on:
    - "CAPRMEDIO Main Skill"
version: 7
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
---
# Serialize Main Skill Invocation per Host

for the CAPRMEDIO Main Skill, the Host Invocation **must** serialize as `$ca` **in** Codex; **if** a Claude compatibility Extension **or** Operator-provided compatibility layer is separately authorized by the Operator, **then** its Host Invocation **must** serialize as `/ca` **in** Claude.
