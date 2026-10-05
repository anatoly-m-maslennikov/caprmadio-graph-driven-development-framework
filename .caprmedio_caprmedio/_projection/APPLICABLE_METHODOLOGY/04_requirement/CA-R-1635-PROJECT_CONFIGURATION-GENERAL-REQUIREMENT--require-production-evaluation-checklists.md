---
subjects:
  governs: "evaluation"
  depends_on: []
version: 27
updated_at: "2026-10-03 01:23:33 +0400"
relations: {"relates_to": ["CA-R-1286", "CA-R-1634", "CA-R-1662"], "depends_on": ["CA-R-1503", "CA-R-1504", "CA-R-1505"]}
atom_id: "CA-R-1635"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1635-PROJECT_CONFIGURATION-GENERAL-REQUIREMENT--require-production-evaluation-checklists.md
  source_atom_id: CA-R-1635
  source_atom_revision: 27
  source_sha256: 305cc5cfc9d0d1d9780737e12cc7745d84948374669c157ee08244e0027318b5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Require production evaluation checklists

## Scope

production-relevant components and governed scopes.

## Claim

**every** production-relevant component **or** governed scope **must** define a Production Evaluation Checklist **before** it can pass a production-readiness gate. the checklist states how operators will know that the realized system remains healthy, correct, supportable, **and** within its accepted operating boundaries during real work.

**every** operational condition **or** invariant is owned by one `evaluation_control` Atom. the control identifies:

- the Requirement, Demand For, Constraint, Method, **or** other governed claim being assured;
- the production signal **and** authoritative data source;
- the healthy condition, expected range, threshold, **or** failure predicate;
- the evaluation window, cadence, **and** permitted detection delay;
- the component, entity, lifecycle state, **or** workflow boundary **to** which it applies;
- the accountable owner **and** escalation destination;
- the alert, incident, investigation, degradation, rollback, **or** recovery action triggered by failure;
- the diagnostic context required **to** investigate the condition;
- the required factual execution record **and** evidence-retention boundary; **and**
- known blind spots, sampling limits, unavailable signals, **and** other evaluation limitations.

a Production Evaluation Checklist is a Catalog Projection over the applicable `evaluation_control` Atoms. it organizes **and** navigates those controls **without** absorbing, paraphrasing, **or** replacing their Claims. the Catalog Projection does **not** acquire the Content Role of its source Atoms.

**every** control distinguishes its governed meaning from its realization **and** results:

- the Evaluation Control defines the production evaluation condition;
- monitors, dashboards, alerts, health checks, **and** operational automation are Implementation;
- recorded metrics, logs, traces, alerts, incidents, **and** check outcomes are factual execution records, **not** reusable Operations definitions; **and**
- a Concern Atom of Type `problem` records a material discrepancy requiring disposition.

a Production Evaluation Checklist presents the applicable controls for real production operation **without** becoming their authority. it is **not** a QA Case, **and** passing pre-release Test **or** Evaluation implementations does **not** by itself satisfy the production-evaluation obligation.

## Details

pre-release QA demonstrates behavior under bounded conditions, while production evaluation **must** detect degradation, incorrect state, **and** supportability failures during actual operation. atomic controls preserve independent lifecycle **and** replacement, while the checklist provides a navigable scope view **without** conflating definitions, implementations, **and** observations.
