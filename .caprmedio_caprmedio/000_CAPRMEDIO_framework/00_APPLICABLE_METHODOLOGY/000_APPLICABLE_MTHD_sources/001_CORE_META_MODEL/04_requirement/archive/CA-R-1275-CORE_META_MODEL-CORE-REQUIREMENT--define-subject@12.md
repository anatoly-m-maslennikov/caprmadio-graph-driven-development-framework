---
subjects:
  governs: "Subject"
  depends_on:
    - "Atom"
    - "Entity"
    - "Term"
    - "Relation"
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Subject Path"
version: 12
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
---
# Define Subject

a Subject **means** a direct Relation between an Atom **and** an Entity, typed as GOVERNS **or** DEPENDS_ON.

- the Atom is the source; the Entity is the target identified by its full canonical Subject Path.
- the Subject is the Relation, **not** its target, its target's path, **or** a Term used **in** that path.
- the Relation creates no intermediate Subject object **and** no additional target identity; it does **not** make the target bearer-dependent on the source Atom.
