---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Temporary State"
  depends_on:
    - "Carrier"
    - "Project Settings"
    - "Action"
    - "Atom/Content Role"
priority: medium
version: 1
updated_at: "2026-09-17 18:44:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should temporary-state confinement separate outcome, placement, and failure behavior?

which owners retain the confinement outcome, configured placement, **and** stop/report behavior currently combined **in** R-1473 **and** M-289?

## Evidence

R-1473 states required confinement, names `.caprmedio_tmp/`, excludes authority/runtime fallbacks, **and** requires stopping before an unsafe effect. M-289 adds allocation, dependency/cache routing, atomicity preconditions, **and** cleanup behavior. M-161 requires staging on the destination filesystem, **not** a sibling directory: that is compatible with project-temp confinement **when** the required same-filesystem condition holds.

## Principle check

coherence requires R/M/D/O responsibility boundaries **without** weakening safety. DRY disfavors duplicated concrete path authority; information preservation protects every excluded fallback, bytecode cache boundary, durable-state exclusion, **and** failure gate. these do **not** permit choosing a new path **or** assuming cross-filesystem atomicity.

## Disposition

preserve confinement **and** the current configured placement while mapping exact Settings/Delivery **and** operational owners. do **not** delete the only retained placement value, turn temporary output into authority, relocate runtime state, **or** allow a host-temp/destination-sibling fallback. keep the atomicity precondition **and** blocked outcome explicit.

## Inspected source Revisions

- `CA-R-1473@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/04_requirement/CA-R-1473-PROGRAMMATIC-CORE-REQUIREMENT--confine-all-temporary-state-to-project-temp.md`; SHA-256 `5764bfbeff60c5b846f9d2082670802c66b0c15f03f28d8511a262f84a9c16fd`.
- `CA-M-289@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-289-PROGRAMMATIC-CORE-METHOD--route-all-temporary-carriers-through-project-temp.md`; SHA-256 `9919231e55ed2c034a5404405d3c6cdcf65bec0f2f95b7fc50a92a75adfe861b`.
- `CA-M-161@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-161-PROGRAMMATIC-CORE-METHOD--bound-file-and-subprocess-effects.md`; SHA-256 `d01c02b3fb723587fff6ee6d2f613c3fcbdc2bbbf275bcc10c45e76bef6a13d8`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
