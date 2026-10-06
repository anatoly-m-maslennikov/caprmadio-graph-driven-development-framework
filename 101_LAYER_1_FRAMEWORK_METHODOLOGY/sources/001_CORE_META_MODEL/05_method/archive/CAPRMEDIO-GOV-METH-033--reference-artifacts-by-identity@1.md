---
artifact_subtype: implementation_decision
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-METH-023--typed-artifact-relations
---

# Decision — Reference artifacts by identity

Authored semantic relations and prose that identify an atomic or evergreen
artifact use its unique artifact, semantic, rule, or document identity. They
do not encode the carrier's current directory.

A physical path is still valid where location is the subject: a settings
registry resolves an identity to a carrier, a carrier-transition record proves
a move, and a Markdown navigation link lets a reader open the carrier.

## Rationale

Artifact identity survives reorganization; paths do not. Keeping location in
the small set of location-owning carriers makes structural migration bounded
without sacrificing deterministic resolution or GitHub navigation.

## Primary claim

Semantic references to atomic and evergreen artifacts use their unique identity rather than a physical path; paths remain only in resolver registries, carrier-transition records, and navigational links that must locate a file.
