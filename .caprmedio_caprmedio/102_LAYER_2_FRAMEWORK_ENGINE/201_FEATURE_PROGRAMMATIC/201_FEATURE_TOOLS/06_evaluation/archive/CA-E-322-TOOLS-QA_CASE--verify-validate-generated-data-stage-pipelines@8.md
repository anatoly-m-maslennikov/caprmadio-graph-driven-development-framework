---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 8
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-204
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify validate generated data-stage pipelines

## Claim checked

CA-M-204 accepts **only** registered forward-only source-to-derived pipelines whose materializations match their authority frontiers.

## Applicable when

Apply whenever a data-stage registration, dependency, source frontier, **or** materialized output changes.

## Test case

Consider one bounded registered `src → stg → mrt → biz` pipeline with a current source frontier. In that same declared pipeline, include one output using an unregistered prefix, one non-forward dependency, one materialization whose recorded input frontier is stale, **and** one derived fact presented as semantic authority **without** source provenance.

## Acceptance criteria

the registered pipeline is accepted; each introduced defect produces one attributable blocking issue; no generated output is treated as semantic authority; **and** each issue identifies its exact source **and** materialization frontiers.

## Failure disposition

Reject the validator **and** preserve stage declarations, dependency graph, source **and** materialization frontier digests, expected defects, **and** observed issue map.
