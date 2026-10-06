---
atom_id: CAPRMEDIO-GOV-EVAL-006
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - evaluation
version: 18
updated_at: "2026-09-11 18:06:22 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - "CA-D-361"
    - "CA-D-366"
    - "CA-D-383"
    - "CA-D-387"
    - "CA-R-1052"
    - "CA-R-1430"
    - "CAPRMEDIO-GOV-REQU-294"
    - "CAPRMEDIO-GOV-REQU-302"
    - "CAPRMEDIO-GOV-REQU-385"
    - "CAPRMEDIO-META-REQU-627"
---
# Canonical Settings Selection

## Claim checked

the Framework Instance Settings Artifact **and** Project Settings Artifact accept exactly their registered values, resolve deterministically, **and** fail closed on invalid **or** unknown selections; the generated Project Scope Unit Graph reproduces applicable Project Settings **without** becoming selection authority.

## Applicable conditions

1. resolve **and** load the exact current caprmedio_framework_settings Artifact **and** caprmedio_<project_name>_settings Artifact with documented defaults.
2. accept **only** enabled catalog Artifact Types, Atom Content Roles **and** their qualified Types, **and** Governance Origins.
3. accept **only** `medium` **or** `high` artifact creation strictness.
4. accept **only** `silent` **or** `verbose` interaction reporting. select **every** allowed value through Framework Instance Settings **and** confirm that the effective reporting default follows that selection **without** changing source Atoms, using Project Settings as reporting authority, **or** applying an independent Atom-fixed default.
5. validate initialization inputs against Project Settings field authority **and** Authority Modes against Framework Instance Settings field authority; do **not** hard-code this Project's selected values in the Evaluation.
6. reject unknown keys **when** the governing schema marks their table closed.
7. confirm a second parse produces identical effective settings **and** a regenerated Project Scope Unit Graph Projection binds to the same consumed Settings revisions.

## Acceptance criteria

**every** valid selection resolves deterministically **and** **every** invalid selection fails closed with the exact key **and** allowed values.

## Failure disposition

record a Concern naming the accepted invalid value, rejected valid value, **or** non-deterministic result **and** stop settings-schema readiness.
