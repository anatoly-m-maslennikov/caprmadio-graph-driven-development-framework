---
subject_scopes:
  - artifact-model
tier: core
version: 3
updated_at: 2026-08-20 20:02:11
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-001-PRINCIPLE-METHOD--mece_mutually-exclusive-collectively-exhaustive
    - CA-M-002-PRINCIPLE-METHOD--dry_dont-repeat-yourself
  replacement_of:
    - CAPRMEDIO-META-REQU-726--derive-atom-type-from-content-role
---
# Separate Content role from Artifact Type

Every Atom other than Intent has exactly one Content role and exactly one Type. Content role classifies the Atom's primary semantic contribution; Type identifies its governed kind within that role. Neither coordinate derives from or replaces the other.
