---
cce_version: cce_1
cce_form: prohibition
subjects:
  governs:
    continuant:
      - Artifact/Type
  depends_on:
    continuant:
      - Artifact
      - Type
      - SUBTYPE_OF
version: 7
updated_at: 2026-09-04 14:07:21 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-151--admit-only-materially-distinct-framework-constructs
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
  replacement_of:
    - CAPRMEDIO-META-REQU-727--permit-an-optional-direct-subtype-without-self-subtyping
---
# Prohibit Artifact subtypes

an Artifact Type value **must not** use SUBTYPE_OF to establish its admission as an Artifact.
