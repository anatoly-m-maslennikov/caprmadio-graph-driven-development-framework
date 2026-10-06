---
atom_id: CAPRMEDIO-META-REQU-730
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "lifecycle-traceability"
  depends_on: []
version: 13
updated_at: "2026-09-10 20:57:23 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-META-REQU-090
    - CAPRMEDIO-META-REQU-728--separate-immutable-atom-id-from-mutable-scope
---
# Preserve Atom ID across scope change

a governed scope change of an identified Atom **must** preserve its Atom identity, create a new Atom Revision, **and** trigger lineage-impact review for the changed Applicability.
