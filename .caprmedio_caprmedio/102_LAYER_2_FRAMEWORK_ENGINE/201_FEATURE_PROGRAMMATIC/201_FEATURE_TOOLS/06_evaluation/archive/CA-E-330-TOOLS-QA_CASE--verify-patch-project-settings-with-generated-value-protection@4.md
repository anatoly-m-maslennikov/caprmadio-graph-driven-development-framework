---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - project-settings
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-212
---
# Verify patch project settings with generated-value protection

## Claim checked

CA-M-212 changes only schema-editable Project Settings keys and rejects generated, unknown, or stale targets.

## Applicable when

Apply whenever the Project Settings schema, ownership classification, or patch mechanics change.

## Test case

Seal one settings carrier and request changes to one schema-editable key, one generated key, and one unknown key. Observe rejection, then apply only the editable change and compare every key and byte-level diff.

## Acceptance criteria

The mixed patch changes nothing and identifies both prohibited keys; the valid patch changes exactly the editable key, preserves all unrelated and generated values, remains schema-valid, and has no undeclared diff.

## Failure disposition

Reject the realization and preserve schema, key classifications, requested operations, dry-run diff, final carrier, and undeclared-change comparison.
