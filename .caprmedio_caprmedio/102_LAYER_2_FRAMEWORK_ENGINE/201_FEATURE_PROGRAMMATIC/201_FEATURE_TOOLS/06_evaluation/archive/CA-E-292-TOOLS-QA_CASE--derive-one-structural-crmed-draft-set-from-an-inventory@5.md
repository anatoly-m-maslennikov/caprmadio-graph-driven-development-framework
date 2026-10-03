---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "structural-adoption"
  depends_on: []
version: 5
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-102
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
