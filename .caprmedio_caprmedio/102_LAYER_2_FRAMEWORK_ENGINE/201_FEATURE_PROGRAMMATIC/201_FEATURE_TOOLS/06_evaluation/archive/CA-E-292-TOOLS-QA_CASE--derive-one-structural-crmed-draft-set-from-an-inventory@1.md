---
atom_id: CA-E-292
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - structural-adoption
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:40:00 +0400
relations:
  evaluation_for:
    - CA-M-102
  derived_from:
    - CA-A-057
---
# Derive one structural CRMED draft set from an Inventory

## Claim checked

Structural CRMED drafts derived from one Inventory remain reviewable candidates without acquiring active authority.

## Test case

Derive candidates from one Inventory containing a folder and file hierarchy.

## Acceptance criteria

Each resulting carrier is a draft, retains its observed source boundary, and does not create an active Scope Unit or requirement.

## Failure disposition

Stop adoption reconciliation and report the first authority or source-boundary invention.
