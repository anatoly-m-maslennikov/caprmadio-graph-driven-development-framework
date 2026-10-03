---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Relation Kind/Registry Entry"
  depends_on:
    - "Relation"
    - "CAPRMEDIO Graph"
    - "Evaluation"
priority: medium
version: 1
updated_at: "2026-09-17 21:33:05 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which Relation metadata fields must the commit fixture require?

which current graph-qualified registry rules require the inverse name, declaration Carrier **and** upstream endpoint used by E-184's negative fixture?

## Evidence and Principle check

R-806 requires owning graph kind, directions, endpoint classes **and** contexts, cardinality, authority effect, transitivity, applicability, Status **and** exclusive purpose. E-184 assumes a universal named inverse, declaration Carrier **and** upstream endpoint. an inverse direction is **not** necessarily an independently declared inverse name; an upstream endpoint is meaningful **only** **in** its registered ordering domain under R-808. coherence requires the exact graph-qualified schema, **not** an invented common field. DRY prohibits a second registry authority; information preservation protects **any** real Carrier constraint **before** dropping it.

## Disposition

preserve E-184 **and** its fail-closed, exact-missing-field **and** no-mutation conditions. bind its missing-field fixtures **to** the current registered relation schema **and** D-defined Carrier **before** replacing the legacy field assumptions. do **not** force **all** graphs **to** acquire an upstream ordering **or** silently invent inverse declarations. this does **not** settle C-199's separate redundant-transitive-edge fixture.

## Inspected source Revisions

- `CA-E-184@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-184-TOOLS-QA_CASE--reject-incomplete-relation-kind-metadata.md`; SHA-256 `a317960e65d2f024750f668f87e0396834ddaa2229f6a4c97bbcf588ccd5ac4b`.
- `CA-R-806@18`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-806-CORE_META_MODEL-GENERAL-REQUIREMENT--register-complete-relation-kind-metadata.md`; SHA-256 `90d4dfd9ecee45ec0d2e6c1f358a233beb624a47867942167cd9603000af325b`.
- `CA-R-808@14`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-808-CORE_META_MODEL-CORE-REQUIREMENT--apply-relation-direction-within-its-ordering-domain.md`; SHA-256 `404ed241b90342046d701d1fdeba28d3e7df5118c25d80507e0369f649830cb2`.
- `CA-C-199@1`: `.caprmedio_caprmedio/01_concern/CA-C-199-QUESTION--which-relation-kind-supports-the-redundant-transitive-edge-fixture.md`; SHA-256 `0fec961d1863c13bc1d2afc314aa745ce2120f9c2ea5e6136349fefd72f7c3bb`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
