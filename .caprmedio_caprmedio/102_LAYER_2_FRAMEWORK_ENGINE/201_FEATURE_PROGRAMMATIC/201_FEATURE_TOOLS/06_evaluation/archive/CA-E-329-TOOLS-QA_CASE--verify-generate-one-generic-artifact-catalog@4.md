---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-catalog
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-211
---
# Verify generate one generic Artifact catalog

## Claim checked

CA-M-211 materializes a deterministic non-authoritative catalog from exactly its declared authority frontier.

## Applicable when

Apply whenever a catalog definition, source contribution, or generator changes.

## Test case

Build one catalog twice from a known declared authority frontier, then attempt generation with a source contribution whose required ordering value is unresolved.

## Acceptance criteria

The two valid builds are byte-identical, contain every and only declared source contribution in stable order, and identify the source frontier and generator. The unresolved-ordering case produces no catalog.

## Failure disposition

Reject the catalog method and preserve definition, source frontier, both derived outputs, unresolved-ordering finding, and source-to-output comparison.
