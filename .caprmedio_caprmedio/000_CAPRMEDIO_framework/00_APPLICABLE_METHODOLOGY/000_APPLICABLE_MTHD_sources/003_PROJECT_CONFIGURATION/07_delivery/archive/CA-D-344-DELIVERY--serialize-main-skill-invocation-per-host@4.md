---
atom_id: CA-D-344
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "CAPRMEDIO Main Skill/Host Invocation"
  depends_on:
    - "CAPRMEDIO Main Skill"
version: 4
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Serialize Main Skill Invocation per Host

for the CAPRMEDIO Main Skill, the Host Invocation **must** serialize as `$ca` **in** Codex; **if** a Claude compatibility Extension **or** Operator-provided compatibility layer is separately authorized by the Operator, **then** its Host Invocation **must** serialize as `/ca` **in** Claude.
