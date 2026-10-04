---
atom_id: CA-O-119
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 01:12:38 +0400"
subjects:
  governs: "RMED Atom Review Workflow/coverage/Step: 119"
  depends_on: [Workflow, Step, Action, Atom, Operator, Journal]
relations:
  relates_to: [CA-O-104, CA-O-118]
---
# Summary

Gate gather result coverage

## Operation

the gather Coverage Gate substep **must** invoke **`=1`** Action, CA-O-118, with stage=gather **after** the main gather Step **and** **before** continuation.

## Details

- inputs: frozen selection, saved Step results, required coverage obligations **and** shared Run evidence.
- covered permits continuation; ask_operator interrupts with the saved missing-work question.
- retain the existing Run ID **and** Journal; do **not** dispatch another Atom reviewer **or** replay completed effects.
