---
atom_id: CA-D-272
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Plan/Type: Task/Dependency/Relation Serialization"
  depends_on:
    - "Task Dependency"
version: 8
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Task Dependencies as Direct Relations

**every** Task Dependency **must** be serialized once under `relations.depends_on` on its dependent Task Atom as one unique canonical reference **to** its prerequisite Task Atom.
