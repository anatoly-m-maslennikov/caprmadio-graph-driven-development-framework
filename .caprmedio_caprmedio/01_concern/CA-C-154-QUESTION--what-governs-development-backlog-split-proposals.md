---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Development Backlog Splitting"
  depends_on:
    - "Development Backlog"
    - "Atom Collection/Type: Epic"
    - "Atom/Content Role: Plan/Type: Task"
    - "Framework Instance Settings"
    - "Operator"
    - "Action"
priority: medium
version: 1
updated_at: "2026-09-17 15:13:27 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# What governs Development Backlog split proposals?

what active selection, Task membership, **and** reusable Action define the backlog-split proposal currently triggered at fifty Tasks?

## Evidence

GOV-REQU-372 requires Governance **to** propose narrower ordered Epics **when** a Development Backlog Epic contains more than fifty Tasks, with Operator approval required **before** applying the split. the source does **not** identify a Framework Instance parameter, its fallback, whether direct **or** recursive Task membership is counted, **or** the lifecycle selection. Governance is **not** an identified Actor **or** a bound Action.

## Principle check

CA-M-002 rejects a second configurable-value owner; CA-M-006 requires Actor, Action, membership **and** control rules **to** agree; Operator authority protects the explicit approval gate. those Principles do **not** justify selecting a new Settings key, silently removing the threshold, inferring concurrent order, **or** treating every descendant historical Task as active work.

## Disposition

preserve the existing proposal **and** approval obligations until their count domain **and** selected-value ownership are explicit. extract operational behavior **without** inventing a Process graph, changing fifty into an unapproved value, or automatically splitting an Epic. no Settings or Plan Carrier changes are performed by this Concern.

## Inspected source Revisions

- `CAPRMEDIO-GOV-REQU-372` Version 15: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CAPRMEDIO-GOV-REQU-372--propose-development-backlog-splits.md`; SHA-256 `272595b23909d7231c4fee3ffed063a43b66b75594ebdc2d30f0c07215081037`.
- `CAPRMEDIO-META-REQU-139` Version 15: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CAPRMEDIO-META-REQU-139-PROJECT_CONFIGURATION-GENERAL-REQUIREMENT--classify-development-backlog-as-epic.md`; SHA-256 `47e6c77ab54867de5c854de29eb15d18f46fdf69359c3d7bf5d7e5fc2c8a3a9e`.
- `CA-R-1370` Version 8: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1370-CORE_META_MODEL-GENERAL-REQUIREMENT--limit-each-task-to-one-direct-epic.md`; SHA-256 `5ac3b0e658337481f2284e67e794f348d00e45bff589cf90c670fc712d9c366d`.
