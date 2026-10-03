---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Applicable Methodology"
  depends_on:
    - "Projection"
    - "Atom/Subjects"
    - "Artifact/Carrier"
priority: medium
version: 1
updated_at: "2026-09-17 14:22:29 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# May Applicable Methodology persist derived Subject indexes?

does the accepted use of derived indexes permit a persistent Subject Index beside Applicable Methodology's projected Atom Carriers, **or** **only** a separately delivered **or** ephemeral Projection?

## Evidence

D-307 explicitly prohibits persistent GOVERNS **or** DEPENDS_ON Subject Index Carriers **in** Applicable Methodology. the Operator later accepted indexes, relations, **and** Subjects as derived information. D-306 preserves projected RMEDO files rather than a monolithic JSON replacement; D-305 prohibits injected Atom metadata. R-1494 **and** D-309 distinguish recoverable source traceability from compulsory embedded **or** persisted bookkeeping. these do **not** explicitly settle the placement of an auxiliary persisted index.

## Principle check

CA-M-002 permits derived representations **without** a second source of authority; CA-M-005 requires a useful purpose for persistence; CA-M-006 requires the specific Delivery restriction **and** its consumers **to** agree. general permission for Projections does **not** identify the intended exception **to** D-307.

## Disposition

preserve D-307 pending this placement decision. do **not** infer a ban on **all** Subject Graphs, remove the specific restriction by analogy, add metadata **to** source-byte copies, create a new mandatory index, **or** change a Tool during this repair.

## Source snapshot

- `CA-D-307@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-307-CORE_META_MODEL-DELIVERY--prohibit-persistent-applicable-methodology-subject-indexes.md`; SHA-256 `d344927f1c4c295f3c172d31f9440c93091913004fabcd8494e10ddaa6fbdf18`.
- `CA-D-306@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-306-CORE_META_MODEL-DELIVERY--materialize-applicable-methodology-as-projected-atom-files.md`; SHA-256 `a8e228f7dbf634d86994e9239c9fe74a0a4b715da0efaf9a254c2ce1c7dc9b41`.
- `CA-D-305@6`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-305-CORE_META_MODEL-CORE-DELIVERY--carry-projected-atoms-without-new-identity.md`; SHA-256 `b7f848ba76318c8dde7a2956a8044407e88af6df1088d8958b53503b75209007`.
- `CA-R-1494@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1494-CORE_META_MODEL-GENERAL-REQUIREMENT--record-projection-dependency-provenance-only-when-required.md`; SHA-256 `feb801116ac608934f692020374e3c5e6a55511b5a110891d8bebf8c83459014`.
- `CA-D-309@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-309-CORE_META_MODEL-CORE-DELIVERY--bind-materialized-representations-to-regeneration-sources.md`; SHA-256 `ee586e1e3ed73e7b096578fa8b611f655de8bb02dbeb7f047b3931d68fe52f84`.
