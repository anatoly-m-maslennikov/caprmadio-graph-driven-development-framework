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
      - SUBKIND_OF
version: 8
updated_at: 2026-09-04 23:24:00 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-151--admit-only-materially-distinct-framework-constructs
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
  replacement_of:
    - CAPRMEDIO-META-REQU-727--permit-an-optional-direct-subtype-without-self-subtyping
---
# Prohibit Artifact subkinds

an Artifact Type value **must not** use SUBKIND_OF to establish its admission as an Artifact.
