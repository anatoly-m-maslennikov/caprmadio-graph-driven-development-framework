---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Scope Unit/Name"
  depends_on:
    - "Project"
    - "Project Name"
    - "Project Settings"
    - "CCE"
priority: medium
version: 1
updated_at: "2026-09-17 23:41:55 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How does Scope Unit Name case apply to the Project Name?

does CA-M-299's uppercase Scope Unit reference convention exclude the Project Name, whose exact Operator-selected spelling is owned by Project Settings?

## Evidence

CA-M-299 requires the exact uppercase Scope Unit Name for a reference **and** assigns ordinary-English meaning **to** the otherwise identical lowercase word. CAPRMEDIO-META-REQU-619 **and** CAPRMEDIO-META-REQU-675 instead make Project Name an Operator-selected initialization value. the Operator explicitly distinguishes the Project `caprmedio` from the Framework `CAPRMEDIO`; the current Project Core CA-M-296 uses that lowercase Project reference. a generic uppercase rewrite would lose this accepted distinction.

## Principle check

CA-M-002 requires one canonical representation; CA-M-006 requires coherent names **and** references. preserve the selected Project Name **and** the Framework/Project distinction. these Principles do **not** justify inventing a second uppercase Project identity **or** silently treating the Project as excluded from Scope Unit rules.

## Disposition

preserve current names, Settings, **and** Claims. resolve whether Project Name is an explicit exception **to** this language-use convention **or** a separately governed name Property **before** amending the convention. no Project rename, Settings mutation, new Scope Unit, **or** filename migration is authorized by this finding.
## Inspected source Revisions

- `CA-M-299@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-299-CORE_META_MODEL-METHOD--distinguish-scope-unit-names-from-ordinary-english.md`; SHA-256 `a08244bcc461e319756437cbd24a1e7f75aaf32376d6689c821d9dfadb1c540c`.
- `CAPRMEDIO-META-REQU-619@17`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-619-CORE_META_MODEL-CORE-REQUIREMENT--define-project-settings.md`; SHA-256 `7855feedc15fabbd33ddb5c973606a40b45a2a1b3e1caafe0f87a89e1c4a2a11`.
- `CAPRMEDIO-META-REQU-675@17`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-675-CORE_META_MODEL-CORE-REQUIREMENT--partition-operator-settings-between-settings-artifacts.md`; SHA-256 `48173167bb3c39dae4a86263e449ac4d45333fe3ec1c02590e3fdb60ec79da08`.
- `CA-M-296@2`: `.caprmedio_caprmedio/05_method/CA-M-296-CORE-METHOD--do-not-rely-on-memory-files.md`; SHA-256 `81a7cd908ef53de8b6000c72eedaad66ce9fc317c9c5796f1c2e7ff0d558e010`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
