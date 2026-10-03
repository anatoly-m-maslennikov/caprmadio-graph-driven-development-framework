---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 5
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-201
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify normalize portable repository text bytes

## Claim checked

CA-M-201 produces one semantic-preserving and byte-idempotent representation of supported repository text.

## Applicable when

Apply whenever the repository text-normalization policy or normalizer implementation changes.

## Test case

Prepare equivalent supported text files with mixed line endings, optional byte-order marks, different final-newline states, and one undecodable file. Normalize the supported files twice and compare decoded text and bytes.

## Acceptance criteria

All supported variants become byte-identical while decoded semantic text is preserved; the second pass changes no bytes; the undecodable file is rejected and remains byte-identical to its input.

## Failure disposition

Reject the realization and preserve policy version, input and output digests, decoded comparisons, second-pass result, and rejected-file bytes.
