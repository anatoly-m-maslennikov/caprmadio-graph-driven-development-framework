---
subject_scope: identity
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-GOV-REQU-292--explicit-methodology-synchronization
    - CAPRMEDIO-GOV-REQU-300--semantic-immutability-and-lossless-recoding
    - CAPRMEDIO-GOV-REQU-303--optional-project-prefix
    - CAPRMEDIO-GOV-REQU-323--register-caprmedio-type-prefixes
---
# Migrate the framework prefix to CAPRMEDIO

The framework project's canonical project prefix is `CAPRMEDIO`. A governed,
deterministic, lossless migration must replace the former `CAPRMEDIO` project
prefix across active and archived artifact IDs, filenames, relations,
Projections, Journals, settings, schemas, tools, tests, documentation, installed
methodology, and Git-bound provenance that embeds the governed identity.

The migration changes identity encoding rather than the semantic claims carried
by admitted Atoms. It must preserve reference closure, one-to-one old-to-new
mapping, content other than identity-bound references, rollback evidence, and
second-run idempotency. Git history remains the provenance of prior spellings;
active carriers must not retain compatibility aliases after cutover.

Artifacts establishing this requirement may retain the former prefix until the
migration is executed, because the new prefix was not authoritative when their
identities were admitted.

## Rationale

The canonical framework identity and its project-owned artifact graph must
converge without pretending that historical Git objects were created under the
new name.
