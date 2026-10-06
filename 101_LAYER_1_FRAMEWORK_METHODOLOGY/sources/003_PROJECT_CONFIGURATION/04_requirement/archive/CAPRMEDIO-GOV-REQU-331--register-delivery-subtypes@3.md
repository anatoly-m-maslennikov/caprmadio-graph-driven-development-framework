---
subject_scopes:
  - artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
project_settings:
  artifacts:
    enabled_subtypes:
      - delivery:release_definition
      - delivery:environment_definition
version: 3
updated_at: 2026-08-19 04:33:37
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register Delivery subtypes

GOV must register `release_definition` and `environment_definition` as direct subtypes of the internal `delivery` Atom Type.

| Subtype | Governed unit |
| --- | --- |
| `release_definition` | One independently replaceable rule for packaging, distribution, publication, release, or promotion. |
| `environment_definition` | One independently replaceable rule for a target environment, its topology, or its configuration sourcing. |

A factual release, deployment, or environment state is Ops rather than Delivery.
