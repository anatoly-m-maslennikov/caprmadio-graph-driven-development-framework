---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Type"
  depends_on:
    - "Core Meta-Model"
    - "Project Configuration"
    - "Atom/Content Role"
    - "Artifact/Carrier"
priority: medium
version: 1
updated_at: "2026-09-17 15:13:27 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which configured Types may Core Meta-Model Atoms use?

which Type admission **and** exact filename mapping let the Core Meta-Model remain usable **without** this Project Configuration?

## Evidence

Evaluation Approach is defined **in** Project Configuration, while Core Meta-Model E-207, E-249, E-440, **and** E-441 use `EVAL_APPROACH` **in** their filenames. the current D-400 mapping spells that Type `EVALUATION_APPROACH`; it does **not** admit `EVAL_APPROACH` as a second canonical token. QA Case admission also lives **in** Project Configuration while GOV-EVAL-009 uses `QA_CASE` **in** Core. the recent E-440/E-441 owner repair retained their prior Type tokens; it did **not** establish standalone Core Type admission.

## Principle check

CA-M-002 requires one admission owner **and** one canonical representation; CA-M-006 requires role, Type **and** Carrier agreement; R-1375 requires expansion **without** redefinition of Core. a generic `EVALUATION` filename does **not**, by itself, prove a complete default-Type admission that can replace these qualified values. implementation or broad-case wording alone does **not** authorize moving every configured Type into Core.

## Disposition

preserve the affected Claims **and** all existing Type definitions. establish whether Core should admit the necessary shared Type **or** use an already admitted Core value, **then** migrate carriers without changing Claim identity **or** Summary by inference. do **not** retain an undocumented token alias, silently depend on this Project Configuration, **or** claim that the earlier owner moves finished Type normalization.

## Inspected source Revisions

- `CA-E-207` Version 9: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-207-CORE_META_MODEL-EVAL_APPROACH--evaluate-priority-governed-alternative-selection.md`; SHA-256 `fbdcdd2052528011e19706e139cb6a6139c98e036bda9e9a3b18873da86c0bb5`.
- `CA-E-249` Version 9: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-249-CORE_META_MODEL-GENERAL-EVAL_APPROACH--evaluate-methodology-expansion-mappings.md`; SHA-256 `82f3bcf7b94400c3baea216aa85957e372067596e82dd4c0fac9ebba8c4eb168`.
- `CA-E-440` Version 9: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-440-CORE_META_MODEL-GENERAL-EVAL_APPROACH--evaluate-governing-atom-change-approval.md`; SHA-256 `941b3285ccb89de9358d73e36f161676cbcf28ff68d3f3a357f0dde33d8b6cab`.
- `CA-E-441` Version 7: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-441-CORE_META_MODEL-GENERAL-EVAL_APPROACH--evaluate-retry-budget-and-escalation.md`; SHA-256 `4e9ab359859321e0f71896df4c1f742655e6da53b8f1a73f1e851c639ac56e57`.
- `CAPRMEDIO-GOV-EVAL-009` Version 14: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CAPRMEDIO-GOV-EVAL-009-CORE_META_MODEL-QA_CASE--effective-priority-selection.md`; SHA-256 `5a405ac18b548a2c05991f71b3351c6d2dacffc25d0570c595589202ef8fd0c0`.
- `CAPRMEDIO-GOV-REQU-748` Version 20: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CAPRMEDIO-GOV-REQU-748--register-type-values-for-evaluation-atoms.md`; SHA-256 `e4df1d27207d9153fab49e516e34603a02a73ab1075195fdef4c379cd65bc9fb`.
- `CAPRMEDIO-R-793` Version 17: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CAPRMEDIO-R-793-REQUIREMENT-BSEED_GOVERNANCE--define-evaluation-approach-as-a-type-value-for-evaluation-atoms.md`; SHA-256 `b492d691538bf1a4a7ffcf9fb60132a803302ed65951bc8f8a358d3f18128ac4`.
- `CA-D-400` Version 6: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-400-PROJECT_CONFIGURATION-DELIVERY--serialize-evaluation-type-tokens.md`; SHA-256 `c3e1be91d906484b9888d95167c33083e72856a87f804014260662e604591b88`.
- `CA-R-1375` Version 10: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1375-CORE_META_MODEL-CORE-REQUIREMENT--restrict-methodology-source-expansion-to-core-permission.md`; SHA-256 `d0b9f7290157c2e279b3692c7efb290b29e378ff9cbaeeb4ad0aafb0c15fa900`.
