---
atom_id: CA-E-289
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - plugin-packaging
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:40:00 +0400
relations:
  evaluation_for:
    - CA-M-151
  derived_from:
    - CA-A-057
---
# Reject one invalid Codex plugin package

## Claim checked

A Codex plugin package contains a coherent manifest, contained relative references, and matching marketplace entry.

## Test case

Build one package whose manifest names a missing packaged capability.

## Acceptance criteria

Package validation rejects it before marketplace publication or installation.

## Failure disposition

Stop packaging and report the missing or inconsistent carrier.
