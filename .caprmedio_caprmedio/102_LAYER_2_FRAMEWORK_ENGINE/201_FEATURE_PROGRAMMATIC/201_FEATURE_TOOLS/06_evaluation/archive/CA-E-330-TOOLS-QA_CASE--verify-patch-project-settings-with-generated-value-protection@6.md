---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "project-settings"
  depends_on: []
version: 6
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-212
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
