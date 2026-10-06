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
    - CAPRMEDIO-GOV-EVAL-027--canonical-settings-selections-test-case
  check_of:
    - CAPRMEDIO-GOV-REQU-294--interaction-reporting-mode-setting
    - CAPRMEDIO-GOV-REQU-385--resolve-artifact-routes-from-authority-configuration-and-the-scope-unit-graph
    - CAPRMEDIO-GOV-REQU-302--atomic-admission-and-promotion-gate
  child_of:
    - CA-R-1054
---
# Canonical Settings Selection

## Claim checked

the Framework Instance Settings Artifact **and** Project Settings Artifact accept exactly their registered values, resolve deterministically, **and** fail closed on invalid **or** unknown selections; the generated Project Scope Unit Graph reproduces applicable Project Settings **without** becoming selection authority.

## Applicable conditions

1. resolve **and** load the exact current caprmedio_framework_settings Artifact **and** caprmedio_<project_name>_settings Artifact with documented defaults.
2. accept **only** enabled catalog Types, subtypes, **and** Governance loci.
3. accept **only** `medium` **or** `high` artifact creation strictness.
4. accept **only** `silent` **or** `verbose` interaction reporting.
5. accept Project Settings for the Project `caprmedio` **only if** Project Prefix is `CA` **and** Authority Modes are `casual` by default **and** `strict` for governance, metamodel, project, **and** semantics.
6. reject unknown keys **when** the governing schema marks their table closed.
7. confirm a second parse produces identical effective settings **and** a regenerated Project Scope Unit Graph Projection binds to the same Project Settings Revision.

## Acceptance criteria

**every** valid selection resolves deterministically **and** **every** invalid selection fails closed with the exact key **and** allowed values.

## Failure disposition

record a Concern naming the accepted invalid value, rejected valid value, **or** non-deterministic result **and** stop settings-schema readiness.
