---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Work Journal/Event/Previous Result Event"
  depends_on:
    - "Evaluation"
    - "Relation"
priority: medium
version: 1
updated_at: "2026-09-17 21:58:05 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which authority governs immediate prior-result replay?

which active authority should E-198 evaluate for immediate previous-result replay **and** the ban on copied before-state fields?

## Evidence and Principle check

E-198 links **to** GOV-REQU-339, whose current Claim registers Work Journal Event Type values. that Claim does **not** specify the previous-result chain. M-087 governs the general action flow but does **not** supply the detailed replay conditions. D-435 mentions `previous_result_event` while defining replacement-reference encoding; it is **not** a complete replacement for the first-event, immediate-predecessor, no-duplication **and** cycle conditions.

DRY **and** coherence require a link **to** the actual governing Claim, **not** merely an active same-topic Atom. information preservation protects the useful replay **and** provenance constraints. the inspected related Atoms do **not** establish an exact successor for this coverage.

## Disposition

preserve E-198 **and** its current reference evidence **until** the exact replay authority is located **or** explicitly established. do **not** replace GOV-REQU-339 by D-435 solely because both mention Journal fields, invent an earlier replacement **or** remove the replay guarantees. this is a semantically mismatched resolved target, **not** proof that the target ID is missing.

## Inspected source Revisions

- `CA-E-198@13`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/06_evaluation/CA-E-198-TOOLS-QA_CASE--replay-previous-state-without-before-fields.md`; SHA-256 `4f51d7a4e6eb1f302ddbe87da0d8f18fc82cc0c9e97687289f69548e0e15e797`.
- `CAPRMEDIO-GOV-REQU-339@18`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-339-CORE_META_MODEL-GENERAL-REQUIREMENT--register-type-values-for-work-journal-events.md`; SHA-256 `821dab03af48bd3af7536874b77ad4f3c29b078846bcc9565f547ebf384a42ad`.
- `CA-M-087@23`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/05_method/CA-M-087-TOOLS-CORE-IMPL_METHOD--process-one-project-path-action.md`; SHA-256 `6bedb22ca8cf1c404c2b2d9f517e30729cdb9fb15010287ce7126f8ef7dca752`.
- `CA-D-435@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-435-PROJECT_CONFIGURATION-DELIVERY--serialize-atom-replacement-event-references.md`; SHA-256 `02c9de3fdb3fe0a4d1c6cd1864b33ba07530c4079f3210fc6688f2b2b7ff0879`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
