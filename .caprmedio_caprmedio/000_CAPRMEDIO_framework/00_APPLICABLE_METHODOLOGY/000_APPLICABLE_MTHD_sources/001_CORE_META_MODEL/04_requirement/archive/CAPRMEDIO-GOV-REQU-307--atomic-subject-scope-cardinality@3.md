---
subject_scopes:
  - subject-scope
version: 3
updated_at: 2026-08-20 03:28:51
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-136--use-universal-subject-scopes-with-rmed-cardinality
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-META-REQU-157--narrowest-common-scope-ownership
---
# Govern Atomic Artifact subject scopes

Every Atom stores `subject_scopes` as a non-empty list of unique, unqualified,
lowercase kebab-case tokens. The allowed vocabulary is registered separately
for each `scope_path`. A token never embeds its Structural level, `local_order`,
scope label, or Artifact Type.

Atomic subject-scope cardinality is:

| Content role | `subject_scopes` |
|---|---|
| Requirement, Method, Evaluation, Delivery | exactly one |
| Concern, Analysis, Plan, Implementation, Ops | one or more |

An absent property, empty list, duplicate token, or value outside the owning
scope's vocabulary is invalid. Subject scopes narrow discovery and comparison;
tools must still follow explicit relations before declaring an Atom obsolete,
replaced, resolved, or conflicting.
