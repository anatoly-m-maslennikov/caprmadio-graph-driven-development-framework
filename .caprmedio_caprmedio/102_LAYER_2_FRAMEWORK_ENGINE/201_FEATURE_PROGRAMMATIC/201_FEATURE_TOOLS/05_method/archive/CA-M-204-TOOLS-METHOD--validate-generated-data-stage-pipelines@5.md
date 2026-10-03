---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 5
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  method_for:
    - CA-R-1125
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate generated data-stage pipelines

## Applicable when

Use this Method when validating a registered generated-data pipeline from source carriers through derived stages.

## Procedure

1. Load the registered `src`, `stg`, `mrt`, and `biz` stage declarations, their declared dependencies, and their materializations.
2. Resolve the authoritative source frontier for every declared generated output.
3. Check that every stage uses one registered prefix, every dependency advances from `src` toward `biz`, and no generated output becomes semantic authority.
4. Compare each materialization's recorded input frontier with the current declared source frontier.
5. Report each unregistered prefix, non-forward dependency, missing source frontier, stale materialization, and independently authored derived fact with its exact carrier.

## Outcome

The pipeline has an attributable `src → stg → mrt → biz` topology with current source-derived materializations, or explicit blocking violations.

## Failure or stop

Block acceptance when a stage uses an unregistered prefix, lacks a source frontier, depends non-forward, claims semantic authority, or cannot prove currentness.
