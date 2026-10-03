---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Applicable Methodology/Sources/Project Configuration/Project Customization"
  depends_on:
    - "Core Meta-Model"
    - "Extension"
    - "Artifact/Revision"
    - "Methodology Source/Expansion Boundary"
priority: medium
version: 1
updated_at: "2026-09-17 15:13:27 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How many source Revisions may one Project Customization bind?

does the exact-one source-Revision rule identify a customized package baseline **or** restrict every Project Configuration Claim **to** one source Atom Revision?

## Evidence

R-1226 binds every Project Customization **to** **`=1`** Core Meta-Model **or** Extension revision **without** modifying that revision. it does **not** specify whether that revision is the package baseline **or** an individual Atom. R-1218 **and** R-1375 allow only source-authorized expansion, **not** replacement. a valid addition may depend on multiple governing Atoms even while referring **to** one package release.

## Principle check

CA-M-002 requires one source for each authoritative fact, **not** exactly one prerequisite for every derived Claim; CA-M-006 requires package **and** Atom Revision references **to** remain distinct. the one-Claim boundary does **not** by itself determine source-Revision cardinality.

## Disposition

preserve R-1226 until its source unit **and** permitted composition are explicit. do **not** relax the cardinality by guesswork, conflate package releases with Atom Revisions, allow Core replacement, **or** remove immutable-source traceability while reconciling the rule.

## Inspected source Revisions

- `CA-R-1226` Version 7: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1226-PROJECT_CONFIGURATION-GENERAL-REQUIREMENT--bind-each-project-customization-to-one-source-revision.md`; SHA-256 `4c60fa3ded13dbab86517e2b2b3bae9b0280b01be7c41f0b674c060a781524f7`.
- `CA-R-1218` Version 10: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1218-CORE_META_MODEL-CORE-REQUIREMENT--define-project-configuration.md`; SHA-256 `1cfba24eebb5b36a7030768a9c8abcac59b4918541febf368c8425abe28bb179`.
- `CA-R-1375` Version 10: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1375-CORE_META_MODEL-CORE-REQUIREMENT--restrict-methodology-source-expansion-to-core-permission.md`; SHA-256 `d0b9f7290157c2e279b3692c7efb290b29e378ff9cbaeeb4ad0aafb0c15fa900`.
