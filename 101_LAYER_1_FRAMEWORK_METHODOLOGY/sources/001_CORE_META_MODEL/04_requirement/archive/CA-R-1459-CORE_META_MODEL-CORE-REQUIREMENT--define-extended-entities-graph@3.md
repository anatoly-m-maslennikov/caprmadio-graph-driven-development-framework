---
subjects:
  governs: "Projection/Type: Extended Entities Graph"
  depends_on:
    - "Projection"
    - "Projection/Type: Entities Graph"
    - "Entity"
    - "Atom"
    - "Atom/Subjects"
    - "Subject Path"
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Relation"
    - "Relation Kind"
    - "Artifact/Revision"
version: 3
updated_at: "2026-09-13 13:05:58 +0400"
relations: {}
---
# Define Extended Entities Graph

Extended Entities Graph **means** the Type value under Projection whose instances compose an Entities Graph Projection with representations of the Atoms that govern **or** depend on its represented Entities, using the source Atoms' direct Subjects references **and** canonical identities.

the composite view derives its Atom links **and** Entity structure from their authoritative sources **or** source-traceable upstream Projections. represented Atoms, Entities, **and** Relation facts retain their existing identities **and** source authority; repeated participation does **not** create another Atom, Entity, **or** independently authored Relation fact. the composite Projection Type does **not** become another owner of the represented graph-specific Relation Kinds. this admission establishes the composite Projection's classification **and** source-authority boundary; direct Atom-link mechanics **and** composed navigation remain governed by their corresponding authority.
