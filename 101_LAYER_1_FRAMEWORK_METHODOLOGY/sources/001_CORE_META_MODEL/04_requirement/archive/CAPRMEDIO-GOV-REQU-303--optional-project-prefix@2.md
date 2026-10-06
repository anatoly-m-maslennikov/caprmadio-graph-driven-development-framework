---
subject_scopes:
  - artifact-catalog
project_settings:
  artifacts:
    identity:
      project_prefix_enabled: true
version: 2
updated_at: 2026-08-18 20:19:17
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-420--optional-project-prefix
  relates_to:
    - CAPRMEDIO-GOV-REQU-300--semantic-immutability-and-lossless-recoding
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Configure an optional project prefix

`.caprmedio/caprmedio_project_settings.toml` records whether artifact identities use a project
prefix and records its value when enabled.

Project initialization recommends:

- no prefix for one small project with one artifact namespace; and
- a prefix for a monorepo, multiple CAPRMEDIO projects in one repository, or any
  shared namespace where otherwise valid identities could collide.

Changing the setting after governed identities exist requires one complete
lossless whole-graph migration. It updates active and archived identities,
filenames, relations, Projection and Journal references, settings,
Implementation references, Ops records, and commit provenance together. The
project never retains two accepted identity vocabularies.

## Rationale

A small single-project repository gains no disambiguation from a mandatory
prefix, while a shared namespace requires one.
