---
atom_id: CA-D-386
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Carrier"
  depends_on:
    - "Atom/Content Role"
    - "Priority"
    - "Atom Collection/Type: Epic"
version: 3
updated_at: "2026-09-10 20:54:34 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Concern Priority

a Concern Atom Carrier **must** serialize **`=1`** selected Priority as `priority` with the lowercase value `high`, `medium`, **or** `low`. **every** Epic, Task, Action Policy, **and** non-Concern Content Role Atom Carrier **must** omit `priority`; virtual `highest` **must not** be stored.
