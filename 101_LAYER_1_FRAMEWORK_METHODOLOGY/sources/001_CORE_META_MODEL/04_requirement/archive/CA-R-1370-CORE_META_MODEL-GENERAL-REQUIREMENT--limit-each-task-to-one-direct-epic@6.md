---
atom_id: CA-R-1370
cce_version: cce_1
cce_form: cardinality
subjects:
  governs: "Atom/Content Role: Plan/Type: Task/Epic Membership"
  depends_on:
    - "Atom Collection/Type: Epic/Direct Membership"
version: 6
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Limit Each Task to One Direct Epic

**every** Atom with Content Role Plan **and** Type Task **must** be a direct member of **`<=1`** Epic.
