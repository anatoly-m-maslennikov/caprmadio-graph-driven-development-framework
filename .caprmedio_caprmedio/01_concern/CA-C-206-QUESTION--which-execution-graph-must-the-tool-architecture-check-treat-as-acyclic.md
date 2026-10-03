---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "CAPRMEDIO Graph"
  depends_on:
    - "Evaluation"
    - "Process"
priority: medium
version: 1
updated_at: "2026-09-17 22:33:25 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which execution graph must the Tool architecture check treat as acyclic?

which admitted graph **and** authority make the execution graph **in** E-354 acyclic, **and** how does that boundary relate **to** declared retry **and** recovery routes?

## Evidence and Principle check

E-354 requires an acyclic manager-defined execution graph. its linked M-182 instead requires declared transitions **and** bounded retry routes **and** rejects undeclared cycles; it does **not** identify a universally acyclic execution graph. M-157/M-158/M-160/M-162 supply source allocation **and** boundary conventions, **not** that graph constraint. the general Process model **in** R-1453 permits declared bounded control flow. a dependency DAG, one run's unrolled execution **and** the reusable Process flow are different graphs.

coherence **and** graph-specific Relation ownership require the evaluated graph **to** be identified. DRY rejects duplicating a constraint on a different graph merely because the word dependency appears **in** both. information preservation protects a legitimate architecture restriction **without** silently banning valid bounded retry **or** allowing an undeclared cycle.

## Disposition

preserve the acyclicity clause **in** E-354 **until** its exact graph, source authority **and** cycle diagnostics are bound, **or** a lossless correction is established. do **not** generalize it **to** **all** Process graphs, assume a DAG automatically excludes **all** retry, **or** certify Tool architecture from a different graph's cycle check. the separate effect-owner allocation mismatch is corrected against M-158/M-160.

## Inspected source Revisions

- `CA-E-354@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-354-TOOLS-EVAL_APPROACH--evaluate-tool-source-architecture-and-dispatch-conformance.md`; SHA-256 `7b7700f33d5d5d39e7dab12cc7785a9ab2c5787707609f8a1bd92a3702d37983`.
- `CA-M-182@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-182-TOOLS-METHOD--design-asynchronous-commit-provenance-tool-topology.md`; SHA-256 `3b27829f3897e3504647ee70591706bf30f9367608e61e6c6edf7533fb7f4924`.
- `CA-M-157@12`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-157-PROGRAMMATIC-CORE-METHOD--allocate-deterministic-transformations-to-functions.md`; SHA-256 `65f8c4496c07b9553d47869c421eba310ccc1a223e7fecb50d1b084ba4b95226`.
- `CA-M-158@13`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-158-PROGRAMMATIC-CORE-METHOD--allocate-owned-state-and-lifecycle-to-objects.md`; SHA-256 `30d62f331388ae10d60a1b5ce469303d69cc52ff60f200266ac4f135f9172a17`.
- `CA-M-160@12`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-160-PROGRAMMATIC-CORE-METHOD--separate-deterministic-transformations-from-effects-and-lifecycle.md`; SHA-256 `35dfd41dd9edc6bf5131ba439b2e3a0670170620381b87b95549fd73dc815ce2`.
- `CA-M-162@14`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md`; SHA-256 `f059d7c21b0eb66f9f4164049ea4a250d41a2f74efc89a3a5a43378b0b57cb2d`.
- `CA-R-1453@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1453-CORE_META_MODEL-CORE-REQUIREMENT--define-process.md`; SHA-256 `ef8aef1fb7a2193b3647e4de316069b2dfa2f0fd4009178421fd61d886356db4`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
