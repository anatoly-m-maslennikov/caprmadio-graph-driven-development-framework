---
atom_id: CA-O-110
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-03 06:11:33 +0400"
subjects:
  governs: "RMED Review Repair Step"
  depends_on:
    - "Step"
    - "Action"
    - "Step/Agentic Execution Context"
    - "Workflow Run"
    - "Step Run"
relations: {"relates_to":["CA-O-111"]}
---
# Summary

Repair the evaluated RMED review batch

## Operation

RMED Review Repair Step **means** the Workflow node invoking **`=1`** Action, CA-O-111, **in** Isolated context.

- bind the local check report, current source, correction boundary, confidence/retry policy, **and** context budget.
- apply confirmed corrections **and** record them **in** the same report. return `fixed_not_rechecked` **only** **when** **all** initial checks concluded **and** no unresolved findings remain. safe partial fixes retain `blocked` **when** coverage **or** findings remain unresolved; this Step has no proposal review **or** saved-Atom recheck.
- preserve Entity **and** relation targets; route required identity-changing **or** cross-Atom work as a blocked proposal for separate authorization.
- at the context threshold, save completed edits **and** unfinished work for a fresh subagent; resume **only** unfinished work.

## Details

the Step passes results **to** the caller **and** does **not** expand the local-review mutation boundary. native file **and** session capabilities are sufficient.

