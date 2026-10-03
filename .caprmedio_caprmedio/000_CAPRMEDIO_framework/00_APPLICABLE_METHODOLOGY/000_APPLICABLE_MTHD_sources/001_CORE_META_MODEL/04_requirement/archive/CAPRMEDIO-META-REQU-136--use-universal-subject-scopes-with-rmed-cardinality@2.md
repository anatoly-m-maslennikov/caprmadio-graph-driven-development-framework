---
subject_scopes:
  - artifact-model
version: 2
updated_at: 2026-08-18 00:02:46
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-268--require-one-subject-scope-on-every-atom
  child_of:
    - CAPRMEDIO-REQU-045--separate-hierarchy-dimensions
    - CAPRMEDIO-META-REQU-098--scope-path-does-not-change-semantic-coordinates
    - CAPRMEDIO-META-REQU-111--nine-content-roles-with-plan
    - CAPRMEDIO-META-REQU-157--narrowest-common-scope-ownership
---
# Use universal Subject scopes with RMED cardinality

Every Atom must declare a non-empty `subject_scopes` list selected from the
vocabulary governed for its structural owner. Requirement, Method, Evaluation,
and Delivery Atoms must declare exactly one Subject scope because each owns one
independently replaceable specification claim. Every other Content role may
declare one or more Subject scopes when its role-specific atomic unit genuinely
spans them.

Subject scopes classify semantic subjects for discovery and review. They do
not change structural ownership, Applicability, authority, priority,
lifecycle, or relations. Duplicate, unknown, fallback, and semantically
irrelevant values are invalid.
