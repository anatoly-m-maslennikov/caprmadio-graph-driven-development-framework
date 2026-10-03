---
subjects:
  - relation-model
  - atom-boundary
version: 6
updated_at: 2026-08-23 02:55:00
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-767--keep-active-rmed-relations-out-of-archives
---
# Record replacement transitions in the Journal

Replacement history must be recorded only in the authoritative Journal event that archives the predecessor. That event names the explicit predecessor Atom ID and one or more already active successor Atom IDs. Active current-state Atom relations must not carry replacement history. Formal `replaced_by` and `replacement_of` relation realization is deferred; any later navigation is derived from immutable Journal and archive history under separately admitted authority.
