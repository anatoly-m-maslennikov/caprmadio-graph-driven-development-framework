---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 17
updated_at: "2026-09-10 06:39:08 +0400"
relations: {}
---
# Record replacement transitions in the Journal

replacement **or** absorption history **must** be recorded **only** **in** the authoritative Journal event that archives the predecessor. the authoritative Journal event that archives the predecessor **must** name the explicit predecessor Atom ID **and** **`>=1`** already active successor Atom IDs. active current-state Atom relations **must not** carry replacement history. formal `replaced_by` **and** `replacement_of` relation realization **must** remain deferred, **and** **any** later replacement navigation **must** be derived from immutable Journal **and** archive history under separately admitted authority.
