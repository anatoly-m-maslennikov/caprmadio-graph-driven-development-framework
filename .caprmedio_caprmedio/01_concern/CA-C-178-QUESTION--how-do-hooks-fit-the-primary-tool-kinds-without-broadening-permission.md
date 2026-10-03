---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Tool"
  depends_on:
    - "Action"
    - "Actor"
    - "Atom/Content Role"
    - "Scope Unit"
priority: medium
version: 1
updated_at: "2026-09-17 18:43:26 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How do Hooks fit the primary Tool kinds without broadening permission?

does Hook identify a third primary Tool kind, a specialization, **or** an integration role, **and** what permission admits its trigger-intake effect?

## Evidence

- R-1186 combines the TOOLS Goal with a Hooks/Finders/Doers classification **and** a Hook permission restriction.
- R-1066 permits **=1** primary Tool kind from Finder **or** Doer, with registered specializations; Finders never mutate **and** Doers require dry-run/explicit-apply behavior.
- R-802 classifies COMMIT_TRIGGER as a Hook Tool that atomically writes an immutable event into the Runtime inbox. this is an effect, **not** merely read-only observation.

## Principle check

DRY **and** coherence require compatible classification **and** permission rules, but do **not** decide whether Hook is an independent kind **or** an orthogonal integration role. preserving valuable information prevents dropping durable intake, independence, **or** permission limits simply **to** make the names agree. a blanket conversion **to** Doer would introduce an unverified dry-run/explicit-apply interface obligation.

## Disposition

preserve these Claims. separate the ownership Goal, Tool classification, **and** participation/effect permission **only** after mapping their complete constraints **and** current consumers. do **not** silently grant trigger mutation, remove durable intake, add a new Tool kind, **or** change executable behavior.

## Inspected source Revisions

- `CA-R-1186@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/04_requirement/CA-R-1186-PROGRAMMATIC-DEFINES_GOAL_FOR-TOOLS--own-independently-executable-framework-tools.md`; SHA-256 `c79be9327559fc1584c3deadc12dc5391cfcd2c8707529d19b9aaf8e8328f733`.
- `CA-R-1066@14`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1066-TOOLS-REQUIREMENT--register-extensible-tool-capability-classes.md`; SHA-256 `a0edc9da8a73ab5d67259674419ba9f90ae9b421a36de352f94bf3a2a949c715`.
- `CA-R-802@20`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-802-TOOLS-REQUIREMENT--define-asynchronous-commit-provenance-tool-topology.md`; SHA-256 `f70c72f3aa97ac81ed92068ceecb7e5e8a300df5e49098908ec10330f3335658`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
