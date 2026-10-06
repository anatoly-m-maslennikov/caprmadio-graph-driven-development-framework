---
subjects:
  governs: "Lineage Impact Analysis"
  depends_on:
    - "Atom"
    - "Artifact/Revision"
    - "Atom Change Classification"
    - "Carrier-Only Recoding"
    - "Verification"
cce_version: cce_1
cce_form: obligation
version: 15
updated_at: "2026-09-17 12:02:45 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CAPRMEDIO-META-REQU-097
    - CAPRMEDIO-GOV-REQU-310
---
# Record one Lineage Impact Analysis per changed atom revision

**every** `refinement`, `semantic_revision`, **or** `replacement` of an admitted Atom **must** produce **`=1`** Lineage Impact Analysis Atom whose primary conclusion is the impact state of that exact changed parent Revision, while a `carrier_only` change **must** require lossless-recoding Verification instead.
