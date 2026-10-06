---
atom_id: CA-R-1281
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Projection/Type: Atom Subjects Graph"
  depends_on:
    - "Projection"
    - "Atom"
    - "Atom/Subjects"
    - "Subject Path"
    - "Entity"
    - "Action"
    - "Process"
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Relation"
    - "Relation Kind"
    - "CAPRMEDIO Graph"
    - "Artifact/Revision"
version: 5
updated_at: "2026-09-13 14:31:04 +0400"
relations: {}
---
# Define Atom Subjects Graph

Atom Subjects Graph **means** the Type value under Projection whose instances are non-authoritative CAPRMEDIO Graphs derived from selected current Atom Subjects, with Atom nodes linked by direct GOVERNS **and** DEPENDS_ON references **to** their canonical Entity, Action, **or** Process targets.

**every** represented link retains the source Atom identity, exact Subject Path, canonical target identity, Relation Kind, direction, **and** source Artifact Revision. its Relation Kinds **and** endpoint constraints remain governed by their existing graph-qualified authority; naming this Projection Type does **not** admit another Relation Kind owner **or** an independently authored relation fact. represented targets retain their Entity, Action, **or** Process identities **without** an intermediate Subject object **or** duplicated target definitions.
