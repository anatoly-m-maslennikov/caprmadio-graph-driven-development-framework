---
atom_id: CAPRMEDIO-GOV-REQU-312
subjects:
  governs:
    continuant:
      - relation-model
  depends_on:
    continuant:
      - atom-boundary
cce_version: cce_1
cce_form: obligation
version: 9
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
  relates_to:
    - CAPRMEDIO-META-REQU-097-CORE_META_MODEL-REQUIREMENT--requirement-keep-provenance-separate-from-evidence
    - CAPRMEDIO-GOV-REQU-310-CORE_META_MODEL-REQUIREMENT--classify-lineage-impact-with-four-dispositions
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-312-CORE_META_MODEL-REQUIREMENT--record-one-lineage-impact-analysis-per-changed-atom-revision.md
---
# Record one Lineage Impact Analysis per changed atom revision

**every** `refinement`, `semantic_revision`, **or** `replacement` of an admitted Atom **must** produce **`=1`** Lineage Impact Analysis Atom whose primary conclusion is the impact state of that exact changed parent Revision, while a `carrier_only` change **must** require lossless-recoding Verification instead.
