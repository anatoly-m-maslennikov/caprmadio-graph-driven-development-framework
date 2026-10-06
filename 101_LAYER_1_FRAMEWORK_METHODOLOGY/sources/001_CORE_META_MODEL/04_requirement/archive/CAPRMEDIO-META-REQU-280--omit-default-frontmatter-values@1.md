---
subject_scopes:
  - artifact-model
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-273--use-canonical-carrier-address-as-authority
---
# Omit default frontmatter values

A frontmatter property whose applicable default is defined by active authority
must be omitted when its resolved value equals that default. Consumers resolve
the omitted property from the same authority; non-default values remain
explicit, and absence has no implied meaning where no default is defined.
