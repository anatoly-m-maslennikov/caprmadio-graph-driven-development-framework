---
subject_scopes:
  - artifact-model
tier: core
version: 4
updated_at: 2026-08-21 02:55:24
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-D-003-PRINCIPLE-DELIVERY--provide-one-project-graph-as-the-operating-model
---
# Let the dependent atom own the relation

When one Atom depends semantically on a pre-existing artifact, the dependent Atom stores the directed relation to that upstream subject. Creating the dependent Atom must not require modifying the upstream artifact.

The relation direction records dependency and provenance, not the visual order of CAPRMEDIO Content roles. A later-created Rationale may therefore point to an earlier-created Requirement even though Analysis precedes Requirement in the framework mnemonic.

The dependent Atom stores the only persisted relation to its pre-existing semantic subject.
