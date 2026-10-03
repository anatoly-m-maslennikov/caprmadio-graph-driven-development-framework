---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - lifecycle-traceability
version: 6
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-090--propagate-atomic-revision-impact-through-lineage
    - CAPRMEDIO-META-REQU-098--scope-path-does-not-change-semantic-coordinates
    - CAPRMEDIO-META-REQU-728--separate-immutable-atom-id-from-mutable-scope
---
# Preserve Atom ID across scope change

A governed scope change of an identified Atom MUST preserve the exact Atom-ID segment in its Carrier filename, create a new Atom Revision, and trigger lineage-impact review for the changed Applicability.
