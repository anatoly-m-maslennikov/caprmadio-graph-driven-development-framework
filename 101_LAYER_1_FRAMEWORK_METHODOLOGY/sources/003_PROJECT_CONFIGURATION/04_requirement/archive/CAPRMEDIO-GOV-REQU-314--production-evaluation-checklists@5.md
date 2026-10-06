---
cce_version: cce_1
cce_form: obligation
subjects:
  - evaluation
version: 5
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-094--mechanism-neutral-evaluation-atoms
  relates_to:
    - CAPRMEDIO-GOV-REQU-321--register-caprmedio-atom-type-surface
    - CAPRMEDIO-GOV-REQU-748--register-evaluation-atom-types
    - CAPRMEDIO-GOV-REQU-313--govern-catalog-map-and-hub-projections
---
# Require production evaluation checklists

Every production-relevant component or governed scope MUST define a Production Evaluation Checklist before it can pass a production-readiness gate. The checklist states how operators will know that the realized system remains healthy, correct, supportable, and within its accepted operating boundaries during real work.

Each operational condition or invariant is owned by one `evaluation_control` Atom. The control identifies:

- the Requirement, Demand For, Constraint, Method, or other governed claim being assured;
- the production signal and authoritative data source;
- the healthy condition, expected range, threshold, or failure predicate;
- the evaluation window, cadence, and permitted detection delay;
- the component, entity, lifecycle state, or workflow boundary to which it applies;
- the accountable owner and escalation destination;
- the alert, incident, investigation, degradation, rollback, or recovery action triggered by failure;
- the diagnostic context required to investigate the condition;
- the required Ops record and evidence-retention boundary; and
- known blind spots, sampling limits, unavailable signals, and other evaluation limitations.

A Production Evaluation Checklist is an Evaluation-role Catalog Projection over the applicable `evaluation_control` Atoms. It organizes and navigates those controls without absorbing, paraphrasing, or replacing their claims.

Each control distinguishes its governed meaning from its realization and results:

- the Evaluation Control defines the production evaluation condition;
- monitors, dashboards, alerts, health checks, and operational automation are Implementation;
- metrics, logs, traces, alerts, incidents, and recorded check outcomes are Ops; and
- a Concern Atom of Type `problem` records a material discrepancy requiring disposition.

A Production Evaluation Checklist governs real production operation. It is not a QA Case, and passing pre-release Test or Evaluation implementations does not by itself satisfy the production-evaluation obligation.

## Rationale

Pre-release QA demonstrates behavior under bounded conditions, while production evaluation MUST detect degradation, incorrect state, and supportability failures during actual operation. Atomic controls preserve independent lifecycle and replacement, while the checklist provides a navigable scope view without conflating definitions, implementations, and observations.
