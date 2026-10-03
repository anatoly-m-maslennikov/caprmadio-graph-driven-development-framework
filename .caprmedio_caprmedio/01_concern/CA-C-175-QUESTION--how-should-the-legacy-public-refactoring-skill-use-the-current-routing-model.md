---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "CAPRMEDIO Routing Tree"
  depends_on:
    - "CAPRMEDIO Direct Route Skill"
    - "Action"
    - "Process"
    - "Operator"
    - "Atom/Content Role"
priority: medium
version: 1
updated_at: "2026-09-17 18:10:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should the legacy public refactoring Skill use the current routing model?

is the public `ca-refactoring` Skill **in** METHODOLOGY-REQU-491 an explicitly admitted Direct Route Skill, **or** should its useful refactoring behavior be invoked through the Main Skill's routing tree?

## Evidence

REQU-491 combines a named public Skill capability, entry conditions, Plan creation **after** acceptance, Implementation/Evaluation chaining, stop conditions, wrapper constraints, a repeated primary Claim, **and** rationale. it also names the legacy `refactoring_plan` Type **and** unresolved shared-runtime authority. R-1356 allows Operator-defined Direct Route Skills bound **to** **`=1`** registered route; R-1354 reserves General System Prompt loading **to** the Main Skill. neither inspected rule establishes the route binding **or** current admission of this legacy public Skill.

## Principle check

CA-M-002 prohibits duplicate methodology **and** runtime authority; CA-M-006 requires coherent routing **and** ownership; CA-R-1490 protects the entry gates, consent, stop behavior, **and** provider-neutral wrapper boundary. role splitting alone would preserve an unverified public interface **and** legacy Plan Type. C-151 already preserves the refactoring verification flow-composition question.

## Disposition

preserve REQU-491 pending exact public-route **and** Plan-Type resolution. then keep the required capability under its Engine owner, reusable flow under O, writing/realization technique under M, **and** rationale **only** **where** independently needed. deduplicate the repeated Claim **without** dropping gates **or** inventing a new Skill, route, Type, **or** permission.

## Inspected source Revisions

- `CAPRMEDIO-METHODOLOGY-REQU-491@7`: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-491-FRAMEWORK_METHODOLOGY-REQUIREMENT--requirement-provide-the-ca-refactoring-skill.md`; SHA-256 `dfd64230e00f4d769cbba6e3b66c076fe6ce8a9c42e99d034334863064a79f89`.
- `CA-R-1356@7`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1356-PROJECT_CONFIGURATION-CORE-REQUIREMENT--define-caprmedio-direct-route-skill.md`; SHA-256 `767ae9c0c0b5a9659d6ccccf19bfd9e6bf27823e84fd971de71df99af0a82ed1`.
- `CA-R-1354@6`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1354-PROJECT_CONFIGURATION-GENERAL-REQUIREMENT--restrict-general-system-prompt-loading-to-main-skill.md`; SHA-256 `aa72d97cf1405ee5ae3773943043be49cd49cdb82a3e56acfa97854f0d061c76`.
- `CA-C-114@2`: `.caprmedio_caprmedio/01_concern/CA-C-114-QUESTION--which-authorities-should-the-unresolved-relations-reference.md`; SHA-256 `9375f762efa0f99b99ec5b05f5b26f8a39ef49fadf5262e2f0566a0cf362bc47`.
- `CA-C-151@1`: `.caprmedio_caprmedio/01_concern/CA-C-151-QUESTION--which-actions-compose-refactoring-verification.md`; SHA-256 `c6fc694d7a449b1e57c3506c26593c06988a4fce87effac9047e2f7ec31f2182`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
