---
atom_id: CA-E-431
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - evaluation
version: 1
updated_at: 2026-09-04 03:10:59 +0400
relations:
  evaluation_for:
    - CA-R-802
    - CA-R-812
    - CA-M-087
---
# Preserve independent real-change and Journal commit progress

## Test case

Delay Journal append while a valid real-change action reaches the Git gate, then delay the real-change commit while Journal append completes. Batch the completed Journal record later, including a batch on the configured periodic interval.

## Acceptance criteria

Neither branch gates the other's non-conflicting progress. The real-change commit contains only its sealed targets; Journal append remains independently durable; the later Journal-only commit contains only selected Journal Carriers; and both commit effects remain serialized by one repository gate without losing their common action provenance.
