---
subjects:
  governs: "Atom/Subjects"
  depends_on:
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Entity"
version: 12
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
---
# Resolve Every Direct Subject Target Once

**every** direct GOVERNS value **and** **every** direct DEPENDS_ON value **in** an Atom's Subjects Property **must** resolve **to** **`=1`** canonical Entity. resolution **must not** require an intermediate Subject/Entity **or** Subject/Reference Property **or** a repeated target-kind field.
