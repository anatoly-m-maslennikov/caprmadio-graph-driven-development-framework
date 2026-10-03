---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 00:15:00 +0400
relations:
  evaluation_for:
    - CA-M-204
---
# Verify validate generated data-stage pipelines

## Claim checked

CA-M-204 accepts only registered forward-only source-to-derived pipelines whose materializations match their authority frontiers.

## Applicable when

Apply whenever a data-stage registration, dependency, source frontier, or materialized output changes.

## Test case

Consider one bounded registered `src → stg → mrt → biz` pipeline with a current source frontier. In that same declared pipeline, include one output using an unregistered prefix, one non-forward dependency, one materialization whose recorded input frontier is stale, and one derived fact presented as semantic authority without source provenance.

## Acceptance criteria

The registered pipeline is accepted; each introduced defect produces one attributable blocking issue; no generated output is treated as semantic authority; and each issue identifies its exact source and materialization frontiers.

## Failure disposition

Reject the validator and preserve stage declarations, dependency graph, source and materialization frontier digests, expected defects, and observed issue map.
