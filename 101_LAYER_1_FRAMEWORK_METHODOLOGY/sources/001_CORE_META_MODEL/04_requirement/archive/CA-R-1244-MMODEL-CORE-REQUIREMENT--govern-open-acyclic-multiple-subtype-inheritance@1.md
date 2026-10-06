---
atom_id: CA-R-1244
cce_version: cce_1
cce_form: conditional
subjects:
  governs:
    continuant:
      - SUBTYPE_OF
  depends_on:
    continuant:
      - Term System
version: 1
updated_at: 2026-08-28 22:12:45 +0400
relations: {}
---
# Govern Open Acyclic Multiple Subtype Inheritance

**if** an Entity has one or more SUBTYPE_OF parents, **then** the open SUBTYPE_OF graph **must** remain acyclic, every compatible parent invariant **must** apply conjunctively, and any inherited conflict **must** invalidate the candidate subtype.
