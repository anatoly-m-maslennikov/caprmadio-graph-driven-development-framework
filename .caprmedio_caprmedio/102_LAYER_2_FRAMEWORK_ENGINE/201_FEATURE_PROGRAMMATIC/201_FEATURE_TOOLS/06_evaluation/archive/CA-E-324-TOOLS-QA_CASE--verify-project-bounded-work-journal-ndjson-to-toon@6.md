---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "journal-projection"
  depends_on: []
version: 6
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-206
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify project bounded work journal ndjson to toon

## Claim checked

CA-M-206 produces a reproducible lossless TOON Projection of one unchanged bounded Journal frontier.

## Applicable when

Apply whenever the Journal-to-TOON encoder, frontier grammar, or Projection metadata changes.

## Test case

Select a known ordered NDJSON event range, project its unchanged sealed frontier twice, and compare decoded values, identities, order, source frontier, encoder provenance, and output bytes. Then change one selected source line between sealing and publication.

## Acceptance criteria

Both unchanged runs are byte-identical and decode to every original event field in original order; metadata identifies the exact source frontier and encoder; the changed-frontier run produces no accepted Projection.

## Failure disposition

Reject the Projection method and preserve source and output digests, decoded comparisons, provenance metadata, and changed-frontier handling.
