---
atom_id: CA-D-268
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Atom/Direct Relation Serialization
  depends_on:
    continuant:
      - Atom/Relation Owner
version: 1
updated_at: 2026-08-28 23:15:00 +0400
relations: {}
---
# Serialize Authored Direct Relations on Their Owning Atoms

every authored direct semantic relation **must** be serialized once under `relations.<RELATION_KIND>` on the Atom that owns its declared direction as a nonempty list of unique canonical target references.
