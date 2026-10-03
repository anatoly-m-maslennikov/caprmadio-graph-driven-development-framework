---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "artifact-operations"
  depends_on:
    - "Projection"
    - "Artifact/Revision"
version: 9
updated_at: "2026-09-17 21:58:09 +0000"
relations:
  evaluation_for:
    - CA-M-204
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify validate generated data-stage pipelines

## Claim checked

CA-M-204 accepts **only** registered forward-only source-to-derived pipelines whose materializations match their authoritative source frontiers.

## Applicable when

apply **when** a data-stage registration, dependency, source frontier **or** materialized output changes.

## Test cases

- prepare a valid registered `src → stg → mrt → biz` baseline with a current source frontier **and** validate that unchanged baseline.
- derive separate invalid fixtures from the baseline, introducing one unregistered prefix, one non-forward dependency, one stale materialization input frontier, **or** one derived fact presented as independent semantic authority **without** source provenance.
- validate **every** selected unchanged fixture twice. retain its own source **and** materialization frontier evidence; do **not** accept an invalid variant merely because its baseline was registered.

## Acceptance criteria

- the valid baseline is accepted.
- **every** invalid variant is blocked with an attributable issue identifying its introduced defect **and** exact frontier evidence; repeat validation preserves the diagnostic result.
- no generated output becomes semantic authority. forward direction does **not** imply an additional adjacent-stage-only requirement.
- validation does **not** alter source authority **or** materializations.

## Failure disposition

reject the validator **and** preserve the baseline, selected variant, stage declarations, dependency graph, frontier digests, expected defect **and** observed issue map.
