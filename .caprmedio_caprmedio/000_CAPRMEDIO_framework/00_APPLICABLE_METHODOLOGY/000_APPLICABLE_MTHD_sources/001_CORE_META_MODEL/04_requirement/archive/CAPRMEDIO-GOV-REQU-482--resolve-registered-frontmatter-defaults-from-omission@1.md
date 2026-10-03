---
subject_scopes:
  - carrier-format
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-280--omit-default-frontmatter-values
  relates_to:
    - CAPRMEDIO-GOV-REQU-308--plain-scalar-frontmatter-values
    - CAPRMEDIO-GOV-REQU-329--encode-rmed-applicability-tiers
---
# Resolve registered frontmatter defaults from omission

GOV registers each frontmatter default with its applicability boundary.
Readers resolve an omitted property to that registered default, writers omit
an explicitly supplied default, and validators reject redundant persisted
defaults. Without an applicable registered default, omission means absence.
