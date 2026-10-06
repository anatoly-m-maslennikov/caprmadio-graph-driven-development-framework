---
atom_id: CAPRMEDIO-GOV-EVAL-002
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - evaluation
version: 15
updated_at: "2026-09-10 05:28:44 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1052
    - CA-R-1402
    - CAPRMEDIO-META-REQU-675
    - CA-R-1430
---
# Settings Artifact Usability

## Claim checked

an Operator unfamiliar with the repository can configure framework-instance behavior, including Authority Modes, through Framework Instance Settings **and** Project initialization inputs through Project Settings using **only** the two Settings Artifacts **and** their in-file documentation, while recognizing the Project Scope Unit Graph as a read-only derived view.

## Applicable conditions

the Operator has no undocumented Framework knowledge **and** **must not** edit the Framework Catalog.

## Acceptance criteria

**every** intended change is made through the owning Settings Artifact, **and** **`>=90`**% of classifications correctly distinguish project choices from methodology definitions.

## Failure disposition

record a Concern for **every** misleading **or** missing setting instruction **and** stop settings-usability readiness **until** it is corrected.
