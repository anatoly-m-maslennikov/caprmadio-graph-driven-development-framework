---
atom_id: CA-E-295
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - project-graph-state
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:40:00 +0400
relations:
  evaluation_for:
    - CA-M-149
  derived_from:
    - CA-A-057
---
# Rebuild one project graph state from configuration

## Claim checked

The graph-state Tool derives one current non-authoritative projection from its declared configuration authority.

## Test case

Rebuild graph state twice from one unchanged configuration frontier.

## Acceptance criteria

The projections agree semantically, name their configuration sources, and no direct output edit becomes authority.

## Failure disposition

Reject the projection as stale, nondeterministic, or authority-creating.
