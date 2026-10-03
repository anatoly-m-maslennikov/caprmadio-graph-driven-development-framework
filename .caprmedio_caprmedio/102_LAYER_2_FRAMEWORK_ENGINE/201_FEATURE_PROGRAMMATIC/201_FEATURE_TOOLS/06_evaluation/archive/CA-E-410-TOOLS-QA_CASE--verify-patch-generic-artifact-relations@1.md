---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 1
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-244
---
# Verify patch generic Artifact relations

## Claim checked

CA-M-244 changes only valid direct relation targets and endpoint descriptors while preserving the source Artifact body and unrelated metadata.

## Applicable when

Apply whenever generic relation-patch validation, canonical-reference resolution, or endpoint-descriptor handling changes.

## Test case

Seal one source Artifact with known body digest and existing relations. Submit one valid relative Scope Unit target with its endpoint descriptor together with one target that violates the registered relation direction; then submit only the valid relation change.

## Acceptance criteria

The mixed request changes nothing and identifies the invalid target. The valid request writes only the canonical direct target and endpoint descriptor, advances revision once, and preserves body digest and unrelated metadata.

## Failure disposition

Reject the realization and preserve relation policy, source-owner context, requested targets, endpoint descriptors, dry-run, exact diff, revision, and body digest.
