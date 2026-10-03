---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "provenance"
  depends_on: []
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-250
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify ingest one external Analysis

## Claim checked

CA-M-250 creates an attributable bounded external-Analysis provenance envelope without creating or revising accepted project authority.

## Applicable when

Apply whenever external-Analysis ingestion, provenance-envelope composition, or adoption-boundary handling changes.

## Test case

Supply one external Analysis with source identity, source digest, transformation session, and exact target frontier. Ingest it without an adoption decision and compare accepted project authority before and after; repeat with the target frontier absent.

## Acceptance criteria

The complete case produces one envelope with every supplied provenance value and marks imported claims non-authoritative. The incomplete case produces no envelope. Neither case creates or revises accepted project authority.

## Failure disposition

Reject the realization and preserve source and frontier inputs, envelope contents, authority comparison, and incomplete-provenance result.
