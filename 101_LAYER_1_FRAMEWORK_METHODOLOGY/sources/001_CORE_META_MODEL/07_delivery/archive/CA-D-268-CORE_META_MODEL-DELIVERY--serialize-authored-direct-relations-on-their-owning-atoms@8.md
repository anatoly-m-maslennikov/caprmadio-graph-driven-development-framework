---
atom_id: CA-D-268
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Direct Relation Serialization"
  depends_on:
    - "Atom/Relation Owner"
version: 8
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Authored Direct Relations on Their Owning Atoms

**every** authored direct semantic relation **must** be serialized once under `relations.<RELATION_KIND>` on the Atom that owns its declared direction as a nonempty unordered collection of unique canonical target references **in** deterministic canonical order; target position **must not** add, remove, **or** alter a direct relation **or** dependency.
