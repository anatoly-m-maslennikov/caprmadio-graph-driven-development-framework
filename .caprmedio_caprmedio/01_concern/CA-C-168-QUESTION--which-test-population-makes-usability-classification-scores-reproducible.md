---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Content Role: Evaluation"
  depends_on:
    - "Framework Instance Settings"
    - "Project Settings"
    - "Carrier"
    - "Operator"
priority: medium
version: 1
updated_at: "2026-09-17 17:46:41 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which test population makes usability classification scores reproducible?

which classification cases, expected answers, participants, **and** scoring boundary make the existing settings **and** storage usability Evaluations reproducible?

## Evidence

`CAPRMEDIO-GOV-EVAL-002` requires **>=90**% correct classifications of Project choices versus Methodology definitions. `CAPRMEDIO-GOV-EVAL-003` requires **>=90**% correct storage classifications **and** separate mandatory no-canonical-runtime **and** Journal-view checks. neither inspected Atom fixes the evaluated population, its denominator, expected-answer authority, treatment of an unanswered classification, **or** how multiple participants contribute **to** the score. changing that population can change the verdict **without** changing the evaluated behavior.

the percentage is an Evaluation acceptance criterion, **not** an Autonomous Confidence Threshold. no current Operator direction establishes that it should be moved **to** Framework Instance Settings, changed, **or** deleted.

## Principle check

CA-M-006 requires a coherent interpretation of the same score, CA-M-005 rejects an invented benchmark **or** extra registry, **and** CA-R-1490 protects the existing usability intent **and** mandatory Journal safeguards. CA-M-264 requires recoverable Evaluation inputs **and** falsifying conditions. these constrain the repair but do **not** select the missing cases **or** participant aggregation rule.

## Disposition

preserve both Evaluations **and** their current acceptance percentage. define **or** identify the owning test-case authority **before** claiming reproducible usability readiness. keep the mandatory truth-boundary **and** Journal-view checks independent of the aggregate score; do **not** treat a high score as permission **to** pass a failed mandatory condition. do **not** mutate Settings **or** fabricate observed participant results.

## Inspected source Revisions

- `CAPRMEDIO-GOV-EVAL-002@17`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CAPRMEDIO-GOV-EVAL-002-CORE_META_MODEL-QA_CASE--settings-artifact-usability.md`; SHA-256 `8f83d9a387e2a710803b67e14ba01275b5aa43958a16c91d9a37f06fdd32fa72`.
- `CAPRMEDIO-GOV-EVAL-003@14`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CAPRMEDIO-GOV-EVAL-003-CORE_META_MODEL-QA_CASE--storage-boundary-interpretability.md`; SHA-256 `4f09697652ee6b2740c84e88945a370d7db93ffcea0fd629483e228f94c10537`.
- `CA-M-264@5`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-264-CORE_META_MODEL-METHOD--write-evaluations-with-reproducible-falsification.md`; SHA-256 `c0bb91fd998ac17be25cae64e2285e4fdf60f7a94fb208e3a6afda5f0132d7b0`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
