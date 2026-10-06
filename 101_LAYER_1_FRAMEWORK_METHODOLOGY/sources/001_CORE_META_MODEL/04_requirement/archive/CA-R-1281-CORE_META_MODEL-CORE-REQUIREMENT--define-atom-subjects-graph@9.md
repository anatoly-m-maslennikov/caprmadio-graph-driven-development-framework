---
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
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Relation"
    - "Relation Kind"
    - "CAPRMEDIO Graph"
    - "Artifact/Revision"
    - "Subject"
    - "Term"
version: 9
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define Atom Subjects Graph

Atom Subjects Graph **means** the Type value under Projection whose instances are non-authoritative CAPRMEDIO Graphs derived from selected current Atom Subjects, with Atom nodes linked by direct GOVERNS **and** DEPENDS_ON Subject Relations **to** their canonical Entity target nodes. the Subjects are the links, **not** the target nodes **or** intermediate Subject nodes.

**every** represented link retains the source Atom identity, exact Subject Path, canonical target identity, Relation Kind, direction, **and** source Artifact Revision. its Relation Kinds **and** endpoint constraints remain governed by their existing graph-qualified authority; naming this Projection Type does **not** admit another Relation Kind owner **or** an independently authored relation fact. represented targets retain their Entity identities **without** an intermediate Subject object **or** duplicated target definitions.
