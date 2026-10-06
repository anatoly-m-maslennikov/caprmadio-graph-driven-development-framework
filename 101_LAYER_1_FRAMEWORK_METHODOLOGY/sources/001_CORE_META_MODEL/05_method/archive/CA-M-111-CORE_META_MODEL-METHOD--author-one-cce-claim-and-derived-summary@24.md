---
subjects:
  governs: "Atom Claim Authoring"
  depends_on:
    - "Atom/Claim"
    - "CCE"
    - "Atom/Summary"
version: 24
updated_at: "2026-09-25 11:32:01 +0000"
relations: {"relates_to": ["CA-R-1624", "CA-O-103", "CA-D-479", "CA-R-1465"]}
atom_id: "CA-M-111"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Method"
global_tier: 11
---
# Summary

Author one CCE Claim and derived Summary

## Claim

an Author **must** write an Atom's primary contribution **and** derived Summary using these authoring constraints:

- express **`=1`** independently replaceable contribution using the applicable CCE Content Role profile. carry it under the first body heading registered **in** CA-D-479 rather than imposing the literal heading Claim on **every** role.
- resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit as the authoring default **or** an explicitly permitted different target; carry the resolved value under CA-D-482. express narrower **or** composite applicability **in** the primary content under CA-D-477; those restrictions alone do **not** make the Atom Relational.
- keep Details within the primary contribution under CA-R-1624. **if** supporting content reveals that the first block is incomplete **or** inaccurate, revise that block explicitly **and** recheck agreement; do **not** hide the change **in** Details.
- write Summary **only after** the other body sections **and** the first-block review are complete. shorten the finalized first block under CA-R-1465 **and** CA-R-1273; do **not** substitute supporting Results **or** TLDR as its source.
- for an existing Atom, retain the established Summary **and** check its faithfulness; **if** the Summary needs changing, use a new Atom identity under CA-R-1464.
- derive **every** Translation from the full corresponding source content, **not** the Summary.

## Details
