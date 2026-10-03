---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 6
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-208
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify patch generic Artifact metadata

## Claim checked

CA-M-208 applies only schema-valid generic Artifact frontmatter patches while preserving body, identity, and atomicity.

## Applicable when

Apply whenever generic frontmatter patch mechanics or schemas change.

## Test case

Seal one Artifact with known body bytes. Request one valid field change together with one unknown field; observe apply, then remove the unknown field and apply the sealed valid patch.

## Acceptance criteria

The invalid patch changes nothing; the valid patch changes only the declared frontmatter field, advances revision once, and preserves body bytes, path, filename, and identity.

## Failure disposition

Reject the realization and preserve schema, patch operations, exact diff, revision, and body digest.
