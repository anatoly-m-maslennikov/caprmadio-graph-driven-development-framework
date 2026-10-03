---
cce_version: cce_1
cce_form: evaluation
artifact_subtype: qa_case
subjects:
  governs:
    occurrent:
      - evaluation
version: 11
updated_at: 2026-09-04 04:05:44 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-EVAL-014--verbose-project-settings-evaluation-case
  check_of:
    - CAPRMEDIO-GOV-REQU-294--interaction-reporting-mode-setting
    - CAPRMEDIO-GOV-REQU-385--resolve-artifact-routes-from-authority-configuration-and-the-scope-unit-graph
    - CAPRMEDIO-GOV-REQU-302--atomic-admission-and-promotion-gate
  child_of:
    - CA-R-1054
---
# Settings Artifact Usability

## Claim checked

an Operator unfamiliar with the repository can configure framework-instance behavior through Framework Instance Settings **and** Project identity, Atom prefix, **and** Authority Modes through Project Settings using **only** the two Settings Artifacts **and** their in-file documentation, while recognizing the Project Scope Unit Graph as a read-only derived view.

## Applicable conditions

the Operator has no undocumented Framework knowledge **and** **must not** edit the Framework Catalog.

## Acceptance criteria

**every** intended change is made through the owning Settings Artifact, **and** **`>=90`**% of classifications correctly distinguish project choices from methodology definitions.

## Failure disposition

record a Concern for **every** misleading **or** missing setting instruction **and** stop settings-usability readiness **until** it is corrected.
