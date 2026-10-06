---
atom_id: CAPRMEDIO-GOV-REQU-314
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "evaluation"
  depends_on: []
version: 17
updated_at: 2026-09-15 05:51:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-META-REQU-094
  relates_to:
    - CA-R-1286
    - CAPRMEDIO-GOV-REQU-313
    - CAPRMEDIO-GOV-REQU-748
---
# Require production evaluation checklists

**every** production-relevant component **or** governed scope **must** define a Production Evaluation Checklist **before** it can pass a production-readiness gate. The checklist states how operators will know that the realized system remains healthy, correct, supportable, **and** within its accepted operating boundaries during real work.

**every** operational condition **or** invariant is owned by one `evaluation_control` Atom. The control identifies:

- the Requirement, Demand For, Constraint, Method, **or** other governed claim being assured;
- the production signal **and** authoritative data source;
- the healthy condition, expected range, threshold, **or** failure predicate;
- the evaluation window, cadence, **and** permitted detection delay;
- the component, entity, lifecycle state, **or** workflow boundary to which it applies;
- the accountable owner **and** escalation destination;
- the alert, incident, investigation, degradation, rollback, **or** recovery action triggered by failure;
- the diagnostic context required to investigate the condition;
- the required Operations record **and** evidence-retention boundary; **and**
- known blind spots, sampling limits, unavailable signals, **and** other evaluation limitations.

A Production Evaluation Checklist is an Evaluation-role Catalog Projection over the applicable `evaluation_control` Atoms. It organizes **and** navigates those controls **without** absorbing, paraphrasing, **or** replacing their claims.

**every** control distinguishes its governed meaning from its realization **and** results:

- the Evaluation Control defines the production evaluation condition;
- monitors, dashboards, alerts, health checks, **and** operational automation are Implementation;
- metrics, logs, traces, alerts, incidents, **and** recorded check outcomes are Operations; **and**
- a Concern Atom of Type `problem` records a material discrepancy requiring disposition.

A Production Evaluation Checklist governs real production operation. It is **not** a QA Case, **and** passing pre-release Test **or** Evaluation implementations does **not** by itself satisfy the production-evaluation obligation.

## Rationale

Pre-release QA demonstrates behavior under bounded conditions, while production evaluation **must** detect degradation, incorrect state, **and** supportability failures during actual operation. Atomic controls preserve independent lifecycle **and** replacement, while the checklist provides a navigable scope view **without** conflating definitions, implementations, **and** observations.
