---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - journal-projection
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1128
  derived_from:
    - CA-A-058
---
# Project bounded Work Journal NDJSON to TOON

## Applicable when

Use this Method when a bounded Work Journal frontier must be represented as a compact TOON Projection.

## Procedure

1. Resolve an exact Journal file, event range, or sealed event frontier and record its ordered source identities and digests.
2. Parse every NDJSON line strictly and reject malformed, duplicate, or changed input before projection.
3. Encode the same ordered event values into TOON without adding authority, interpretation, or omitted fields.
4. Attach the source frontier, encoder identity and version, and output digest to the Projection metadata.
5. Decode or independently compare the result to prove lossless identity, value, and order preservation.

## Outcome

One reproducible non-authoritative TOON Projection represents the exact bounded Journal frontier losslessly.

## Failure or stop

Produce no Projection when the frontier changes during generation, any line is malformed, or the result cannot be proven lossless.
