---
atom_id: CA-P-908
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Entity and Artifact Taxonomy Authority
    occurrent:
      - Entity and Artifact Taxonomy Update
  depends_on:
    occurrent:
      - CA-P-906
version: 1
updated_at: 2026-08-28 21:11:50 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Update Entity and Artifact Taxonomy Authority

**when** CA-P-906 is Done, **then** the Assignee **must** make the Entity and Artifact taxonomy express the accepted open identity and Artifact-kind boundaries.

## Scope

`((every CA-P-905 frontier entry assigned to ENTITY_AND_ARTIFACT_TAXONOMY) union (every replacement or new authority Atom created from such an entry))`

## Definition of Done

the Task is **not done if** (Entity is equated with Artifact **or** Base Entity and Dependent Entity lack an identity-based distinction **or** the Base-Entity subtype registry is declared exhaustive **or** Artifact, Atom, Journal, Projection, Relational Artifact, Relational Atom, Scope Unit, Epic, Actor, or Property is placed contrary to the accepted boundaries **or** an allowed value or graph-relation role is promoted to a new root Entity kind solely because of that function **or** Relational Atom is equated with Relational Artifact **or** Scope Unit or Epic is treated as an Atom **or** Entity is required to bear at least one Property **or** a Property occurrence may have zero or multiple immediate bearers **or** any Carrier-specific Claim remains assigned to this Task instead of CA-P-913 **or** any replaced conflicting authority remains active).

## Details

govern `Entity BEARS 0..* Property` as the inverse view of `Property occurrence IS_BORNE_BY exactly one Entity`. keep Artifact and Actor under Base Entity; keep Property under Dependent Entity; keep Atom, Journal, Projection, and Relational Artifact under Artifact; keep Relational Atom under Atom; keep Scope Unit and Epic under Relational Artifact. assign Carrier classification and every other Carrier-specific Claim exclusively to Delivery through CA-P-913. leave Claim and Artifact Revision identity constraints to their specialized authority instead of silently closing their taxonomy here. treat Property, allowed-value, graph-role, State, and Classification functions as orthogonal unless exact authority declares a compatible subtype or disjointness constraint. allow compatible multiple inheritance without collapsing the distinct Relational Atom and Relational Artifact kinds.
