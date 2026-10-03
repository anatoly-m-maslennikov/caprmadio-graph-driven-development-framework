---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "extension-promotion"
  depends_on: []
version: 8
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-216
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify extract one extension candidate from project adaptation

## Claim checked

CA-M-216 extracts one independently identified Extension candidate with a complete attributable reusable dependency boundary.

## Applicable when

Apply whenever Project Adaptation extraction **or** dependency-closure rules change.

## Test case

Select two Project Adaptation Atoms whose required dependency closure includes one transitive dependency **and** one unresolved required dependency. Extract, **then** resolve the missing dependency with an exact source reference **and** repeat.

## Acceptance criteria

the unresolved attempt produces no candidate; the resolved attempt includes the selected Atoms **and** complete transitive closure with exact revisions **and** one stable candidate identity.

## Failure disposition

Reject the extraction method **and** preserve selection, closure graph, unresolved dependencies, source revisions, emitted candidate manifest, **and** proof that source authority was unchanged.
