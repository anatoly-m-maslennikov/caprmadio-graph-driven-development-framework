---
subjects:
  governs:
    continuant:
      - artifact-model
  depends_on:
    continuant:
      - lifecycle-traceability
atom_id: CA-R-165
cce_version: cce_1
cce_form: cardinality
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 7
updated_at: 2026-08-29 02:40:41 +0400
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-288--give-atoms-explicit-revision-ordinals
  child_of:
    - CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
---
# Give every Atom Revision version and updated at

**every** Atom Revision **must** have **`=1`** positive monotonic `version` **and** **`=1`** unambiguous `updated_at`.
