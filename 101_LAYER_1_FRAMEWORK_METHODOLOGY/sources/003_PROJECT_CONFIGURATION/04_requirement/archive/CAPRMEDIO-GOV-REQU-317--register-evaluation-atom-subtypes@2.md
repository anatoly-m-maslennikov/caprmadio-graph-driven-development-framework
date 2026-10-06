---
subject_scopes:
  - artifact-catalog
project_settings:
  artifacts:
    enabled_subtypes:
      - evaluation:qa_case
      - evaluation:evaluation_control
version: 2
updated_at: 2026-08-18 20:19:17
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-467--register-atom-types-by-role-and-locus
  child_of:
    - CAPRMEDIO-META-REQU-094--mechanism-neutral-evaluation-atoms
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register Evaluation Atom subtypes

GOV registers exactly these current direct subtypes of the internal Evaluation
Atom Type:

- `qa_case` defines one mechanism-neutral bounded check, including the claim
  checked, applicable conditions, acceptance criteria, and disposition rule;
  and
- `evaluation_control` defines one condition or invariant checked during real
  operation, including its signal, healthy boundary, evaluation window,
  ownership, and failure response.

Automated tests, evaluation prompts, executable rubrics, statistical
evaluators, model judges, monitors, alerts, and health checks are
Implementation realizations rather than Evaluation subtypes. Their executions
and factual results use the Ops Content role.

One QA Case may have distinct Test and Evaluation implementations. One
implementation may realize several QA Cases only when coverage and results
remain individually attributable. Test and Evaluation chains remain explicit
even when they assure the same Case.

Another Evaluation pattern uses the top-level `evaluation` Type until GOV admits
a direct subtype for it. Sub-subtypes are forbidden.

## Rationale

Mechanism-neutral QA obligations avoid duplicating one evaluation claim across
Test and Evaluation implementations, while Evaluation Controls keep continuous
production checking distinct from bounded QA.
