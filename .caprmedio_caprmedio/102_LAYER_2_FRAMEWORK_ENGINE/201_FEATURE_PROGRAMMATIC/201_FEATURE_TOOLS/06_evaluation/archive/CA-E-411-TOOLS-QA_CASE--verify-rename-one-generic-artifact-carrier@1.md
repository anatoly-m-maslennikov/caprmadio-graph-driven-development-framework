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
    - CA-M-245
---
# Verify rename one generic Artifact carrier

## Claim checked

CA-M-245 performs a grammar-valid generic carrier rename with complete canonical-reference rewrites or rolls back entirely.

## Applicable when

Apply whenever generic filename grammar, canonical-reference discovery, or rename transaction mechanics change.

## Test case

Prepare one generic Artifact with two governed canonical references and request a valid new filename; repeat using a filename that collides with another carrier.

## Acceptance criteria

The valid case changes the carrier name, records one old-to-new identity mapping, and rewrites both canonical references with none retaining the old identity. The collision case changes no carrier or reference.

## Failure disposition

Reject the realization and preserve source and target names, grammar result, mapping, reference inventory, transaction evidence, and collision finding.
