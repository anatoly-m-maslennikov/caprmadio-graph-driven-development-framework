---
subject_scopes:
  - artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
project_settings:
  artifacts:
    enabled_subtypes:
      - plan:development_backlog
      - plan:version_plan
      - plan:change_plan
      - plan:refactoring_plan
version: 3
updated_at: 2026-08-19 04:33:37
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-472--register-development-backlog-projection
    - CAPRMEDIO-GOV-REQU-477--register-change-plan-subtype
    - CAPRMEDIO-GOV-REQU-486--register-refactoring-plan-plan-subtype
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register Plan subtypes

GOV must register `development_backlog`, `version_plan`, `change_plan`, and `refactoring_plan` as direct subtypes of the internal `plan` Atom Type.

| Subtype | Governed unit |
| --- | --- |
| `development_backlog` | Accepted unscheduled action points and, before an approved split, target-version sections in the project's default planning carrier. |
| `version_plan` | Action points assigned exclusively to one target version after an approved split. |
| `change_plan` | One bounded execution package that changes governed artifacts or their native realization. |
| `refactoring_plan` | Action points for one bounded structural transformation that preserves declared behavior and other applicable obligations. |
