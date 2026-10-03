---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - artifact-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 6
updated_at: 2026-08-29 01:16:37 +0400
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-289--keep-projections-versionless
  child_of:
    - CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
---
# Projections have updated at

**every** Projection has one unambiguous `updated_at` identifying its latest completed rebuild. Its governed generator **or** generation procedure **and** declared configuration identify how to rebuild it. A Projection records dependency provenance **only** **when** its registered job needs that information; no Projection is required to persist a blanket source frontier.
