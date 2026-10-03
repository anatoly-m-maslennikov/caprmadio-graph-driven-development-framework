---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Content Role: Evaluation"
  depends_on:
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Delivery"
    - "Action"
    - "Journal/Record"
priority: medium
version: 2
updated_at: "2026-09-17 19:34:24 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should software Evaluation selection separate technique, gates, and evidence?

which M-285 clauses define Evaluation-technique selection, execution gates, **and** evidence content respectively?

## Evidence

M-285 maps failure modes **to** complementary techniques, locates fast versus expensive checks, requires a measured bound for expensive synchronous work, **and** records target/configuration/frontier/versions/seed-or-case/result/replay information. its covered-failure-mode rule is distinct from a record schema **or** execution flow. removing the record list **or** the synchronous-work exception as incidental would lose useful constraints.

## Principle check

DRY favors one evidence owner **and** reusable technique selection; coherence requires every acceptance claim **to** match its failure coverage. minimum complexity does **not** authorize a universal test suite **or** invented benchmark. information preservation retains reproducibility, measured-bound exceptions, **and** the prohibition on using a passing technique as proof of an uncovered failure mode.

## Disposition

preserve all conditions while mapping selection **to** M, evidence representation **to** applicable D, **and** execution/admission behavior **to** O. reuse existing authority **where** equivalent; do **not** choose numeric budgets, create new tests or Tools, discard replay information, **or** claim an observed run merely from its definition.

## Inspected source Revisions

- `CA-M-285@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md`; SHA-256 `5700df025414ee701eb891d8a4c7fadc05889582c06933a6051920422d1d1c66`.
- `CA-M-165@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-165-PROGRAMMATIC-CORE-METHOD--measure-before-optimizing-programmatic-performance.md`; SHA-256 `319c2f8b8e4fd974d63281118c767ead78f7bbbc17808201485b4d12018bb5ee`.
- `CA-R-1340@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1340-CORE_META_MODEL-CORE-REQUIREMENT--define-method-content-role.md`; SHA-256 `f00d924a7f6f44ec8bd34548030ef5eb8f6f47e95a4437914a323aec6465fc8f`.
- `CA-R-1344@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1344-CORE_META_MODEL-CORE-REQUIREMENT--define-operations-content-role.md`; SHA-256 `300b0d772013aad37e26ec465f6b59279fe1f756d45643b5b91434d0d7020401`.
- `CA-R-1453@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1453-CORE_META_MODEL-CORE-REQUIREMENT--define-process.md`; SHA-256 `ef8aef1fb7a2193b3647e4de316069b2dfa2f0fd4009178421fd61d886356db4`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.

## Expensive Evaluation consumers

E-391 **and** E-395 require their expensive campaigns **to** remain outside synchronous Hooks. M-285 permits expensive synchronous work **when** a measured bound admits it. the existing Evaluation wording might intentionally impose a stricter boundary for these campaign kinds; the general exception does **not** prove that this restriction is accidental. preserve the restriction pending an exact applicability map rather than silently broadening permission **or** removing the Method's exception. C-188 independently records the meaning of **pass** for these defect-discovery cases.

## Additional inspected source Revisions

- `CA-E-391@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-391-PROGRAMMATIC-CORE-EVAL_APPROACH--detect-weak-python-assertions-through-mutation-testing.md`; SHA-256 `0cf0956db4772ed5363bdc9cabdd15aa3ebed3067926bc1aaa5a4dba3467f4ad`.
- `CA-E-395@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-395-PROGRAMMATIC-CORE-EVAL_APPROACH--fuzz-parsers-and-stateful-boundaries.md`; SHA-256 `8860032af7949b78f27ad13591ca844ae3123233777afb1d0cef4c816b95f64e`.
- `CA-M-285@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md`; SHA-256 `ab57a74d62e1a75aa1a7c56c2e2b0659ecdfdb88b722c729c6fd208ae8af47c2`.
- `CA-C-188@1`: `.caprmedio_caprmedio/01_concern/CA-C-188-QUESTION--which-outcome-does-pass-denote-in-software-evaluations.md`; SHA-256 `ada268e6417cfb45fff05d37db325933fee89ce2b72ca843f860c26237e718df`.
