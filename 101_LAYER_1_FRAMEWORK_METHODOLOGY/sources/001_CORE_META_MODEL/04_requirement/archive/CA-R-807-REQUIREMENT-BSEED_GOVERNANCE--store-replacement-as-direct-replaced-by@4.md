---
subject_scopes:
  - relation-model
version: 4
updated_at: 2026-08-22 01:32:10
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-767--keep-active-rmed-relations-out-of-archives
---
# Declare replacement as replaced_by

Replacement lineage must be declared only as `replaced_by` from each predecessor to one or more successors in the authoritative Journal event that archives the predecessor. Active current-state Atom relations must not carry replacement history. `replacement_of` is the inverse-derived view from a successor to its predecessor and must never be declared. Replacement chains and the current active successor are derived from the immutable Journal and archive history.
