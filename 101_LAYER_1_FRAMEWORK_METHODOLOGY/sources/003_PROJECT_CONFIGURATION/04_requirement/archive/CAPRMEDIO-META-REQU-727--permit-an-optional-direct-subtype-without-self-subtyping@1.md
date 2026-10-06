---
subject_scopes:
  - artifact-model
version: 1
updated_at: 2026-08-19 04:23:36
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-154--semantic-irreducibility
    - CAPRMEDIO-META-REQU-726--derive-atom-type-from-content-role
---
# Permit an optional direct subtype without self-subtyping

An Atom may have one registered direct subtype that narrows its Type; an Atom without a narrower subtype remains the naked Type and must not receive a synthetic subtype equal to that Type.
