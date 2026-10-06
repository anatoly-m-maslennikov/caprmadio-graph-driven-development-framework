---
artifact_subtype: qa_case
subjects:
  - evaluation
version: 5
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-EVAL-014--verbose-project-settings-evaluation-case
  check_of:
    - CAPRMEDIO-GOV-REQU-294--interaction-reporting-mode-setting
    - CAPRMEDIO-GOV-REQU-385--resolve-artifact-routes-from-governed-authority-and-project-settings
    - CAPRMEDIO-GOV-REQU-302--atomic-admission-and-promotion-gate
  child_of:
    - CA-R-1054
---

# Project Configuration usability

## Claim checked

An operator unfamiliar with the repository can configure reporting mode, artifact strictness, and one enabled artifact Type using only the Project Configuration Atom and its in-file documentation, while recognizing the Project Scope Unit Graph as a read-only derived view.

## Applicable conditions

The operator has no undocumented framework knowledge and must not edit the
framework catalog.

## Acceptance criteria

Every intended change is made through Project Configuration, and at least 90% of
classifications correctly distinguish project choices from methodology
definitions.

## Failure disposition

Record a Concern for every misleading or missing setting instruction and stop
settings-usability readiness until it is corrected.
