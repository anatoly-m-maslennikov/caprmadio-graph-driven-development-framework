---
subject_scopes:
  - artifact-catalog
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-407--single-settings-catalog
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-GOV-REQU-426--omit-update-setting-for-atomic-artifacts
---
# Separate route catalog and project whitelist

One project-local `artifact_catalog.toml` inside the installed methodology owns
the registered artifact types, optional direct subtypes, identity kinds,
derived routes, allowed carriers, and persistence behavior.

`caprmedio_settings.toml` owns only the project selection:

- enabled artifact types and subtypes;
- enabled Governance loci;
- naming options;
- project-specific extensions admitted by the selected governance profile; and
- other operator-controlled workflow settings.

Writers and validators load the catalog first and then apply the settings
whitelist. An unknown, disabled, multiply mapped, or ambiguous type/subtype
fails closed. Project customization changes the project-local catalog through
the governed methodology-customization flow; it does not create a second
classification table in settings, schemas, skills, or tools.

Catalog entries for persisted artifacts declare `commit_on_create`.
`commit_on_update` appears only for entries whose governed content may change
in place and is absent from every atomic entry.

## Rationale

Separating definitions from selection keeps one semantic mapping while allowing
small projects to enable only the artifact vocabulary they need.
