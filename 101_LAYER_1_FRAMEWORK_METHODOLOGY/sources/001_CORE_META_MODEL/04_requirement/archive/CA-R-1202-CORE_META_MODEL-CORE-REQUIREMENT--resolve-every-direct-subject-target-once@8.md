---
atom_id: CA-R-1202
cce_version: cce_1
cce_form: cardinality
subjects:
  governs: "Atom/Subjects"
  depends_on:
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Entity"
    - "Action"
    - "Process"
version: 8
updated_at: "2026-09-13 02:05:21 +0400"
relations: {}
---
# Resolve Every Direct Subject Target Once

**every** direct GOVERNS value **and** **every** direct DEPENDS_ON value **in** an Atom's Subjects Property **must** resolve **to** **`=1`** canonical target **in** the Entity, Action, **or** Process domain. resolution **must not** require an intermediate Subject/Entity **or** Subject/Reference Property **or** a repeated target-kind field.
