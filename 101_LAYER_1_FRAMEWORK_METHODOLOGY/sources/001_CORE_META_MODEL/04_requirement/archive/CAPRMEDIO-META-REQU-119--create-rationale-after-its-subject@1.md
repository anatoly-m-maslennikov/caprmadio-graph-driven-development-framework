---
subject_scopes:
  - artifact-model
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-274--place-rationale-in-analysis
  child_of:
    - CAPRMEDIO-META-REQU-114--preserve-content-role-boundaries-through-caprmedio-loop
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
---
# Requirement — Create Rationale after its subject

A Rationale is an Analysis Atom created only after every specification Atom it explains already exists. The Rationale stores the directed relation to its subjects; specification Atoms contain neither embedded rationale nor persisted rationale backlinks.

Rationale is explanatory rather than normative. Changing an obligation, boundary, Method, Evaluation condition, Delivery rule, or acceptance meaning requires a new applicable specification Atom rather than a Rationale.

## Primary claim

A Rationale follows and points to its pre-existing specification subjects without modifying them.
