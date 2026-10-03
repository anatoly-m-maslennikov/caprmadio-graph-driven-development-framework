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
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-207
---
# Verify read generic Artifact metadata

## Claim checked

CA-M-207 returns selected metadata and derived identity for exactly one generic Artifact without loading its body or hiding absent and malformed fields.

## Applicable when

Apply whenever generic metadata extraction or carrier-identity derivation changes.

## Test case

Select one generic Artifact with a known body-only sentinel, one present requested field, and one absent requested field. Read the selected metadata and derived identity; repeat with malformed frontmatter and an ambiguous carrier identity.

## Acceptance criteria

The valid read returns only the requested field and correct carrier-derived identity, the absent field is explicit, and the body sentinel is neither accessed nor returned. Malformed frontmatter and ambiguous identity produce explicit results without mutation.

## Failure disposition

Reject the realization and preserve carrier identities, requested fields, expected metadata, parse diagnostics, and body-access evidence.
