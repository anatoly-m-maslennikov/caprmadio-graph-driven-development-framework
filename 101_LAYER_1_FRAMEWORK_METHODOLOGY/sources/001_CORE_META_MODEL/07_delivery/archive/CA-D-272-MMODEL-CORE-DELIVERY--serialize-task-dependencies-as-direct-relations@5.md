---
atom_id: CA-D-272
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Type: Task/Dependency/Relation Serialization"
  depends_on:
    continuant:
      - Task Dependency
version: 5
updated_at: 2026-09-01 23:18:00 +0400
relations: {}
---
# Serialize Task Dependencies as Direct Relations

**every** Task Dependency **must** be serialized once under `relations.depends_on` on its dependent Task Atom as one unique canonical reference **to** its prerequisite Task Atom.
