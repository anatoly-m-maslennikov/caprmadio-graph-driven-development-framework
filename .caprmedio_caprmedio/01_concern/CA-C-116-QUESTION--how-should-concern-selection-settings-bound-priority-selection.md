---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Priority"
  depends_on:
    - "Operator"
    - "Framework Instance Settings"
    - "Default Settings"
    - "Atom/Content Role: Concern"
    - "Atom/Claim"
priority: medium
version: 1
updated_at: "2026-09-17 02:47:51 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should Concern selection settings bound priority selection?

how should the Concern selection mode be represented **and** applied independently of the Operator-selected comparison model, so that CAPRMEDIO-GOV-REQU-299 can be split **without** losing a permission boundary **or** inventing a settings parameter?

## Evidence

GOV-REQU-299 combines Concern Priority values, priority-model application, an ancestry restriction, **=2** selection modes, a default, **and** escalation behavior. GOV-EVAL-009 relies on the whole bundle. the present `ask_always` **and** `auto_by_effective_priority` modes govern whether selection is automatic; they are **not** themselves comparison algorithms. neither current Framework Instance Settings nor Default Settings contains those mode values **or** a corresponding declared parameter key. CA-D-386 defines the Concern's `priority` field, **not** the separate selection-mode field.

## Principle check

CA-R-815 **and** CA-R-1487 preserve the Operator-selected admissible model; CA-M-002 requires one parameter owner; CA-M-006 requires coherent mode, procedure, **and** Evaluation meanings. these support separating value authority, encoding, **and** Operations. they do **not** determine the missing parameter's exact Carrier key, whether the mode catalog is closed **or** extensible, **or** whether mode-specific escalation overrides an explicitly selected model's tie-handling rule. do **not** silently equate a selection-permission mode with a comparison algorithm.

## Disposition

defer the unsupported parameter **and** policy choices. preserve GOV-REQU-299 **and** its checked conditions **until** their exact successors **and** settings binding are established. retain the already accepted removal of the implicit ancestry bonus **and** the distinction from Global Tier precedence. the later split must preserve **=1** Concern Priority, its admitted values, selected-model application, supported mode behavior, **and** explicit unresolved outcomes **without** duplicate active authority.

## Current authority inspected

- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-299-CORE_META_MODEL-REQUIREMENT--effective-priority-conflict-selection.md` at Version **18**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CAPRMEDIO-GOV-EVAL-009-CORE_META_MODEL-QA_CASE--effective-priority-selection.md` at Version **14**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1487-CORE_META_MODEL-REQUIREMENT--follow-the-operator-selected-priority-model.md` at Version **2**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-386-CORE_META_MODEL-DELIVERY--serialize-concern-priority.md` at Version **4**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-022-CORE_META_MODEL-ACTION--resolve-and-activate-operator-priorities.md` at Version **3**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-023-CORE_META_MODEL-ACTION--select-an-alternative-under-active-priorities.md` at Version **2**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-279-CORE_META_MODEL-GENERAL-METHOD--resolve-missing-framework-parameters-from-default-settings.md` at Version **4**.
