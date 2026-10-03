---
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - framework-engine-mcp
    occurrent:
      - evaluation
version: 2
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-M-172
  derived_from:
    - CA-A-057
---
# Reject registry publication for one invalid Tool projection

## Claim checked

An invalid selected Tool projection prevents publication of a partial current registry.

## Test case

Introduce one source Tool with an invalid schema into an otherwise valid selected frontier.

## Acceptance criteria

No new registry is published and the invalid source receives an explicit diagnostic.

## Failure disposition

Preserve the defect for repair; do not silently skip it.
