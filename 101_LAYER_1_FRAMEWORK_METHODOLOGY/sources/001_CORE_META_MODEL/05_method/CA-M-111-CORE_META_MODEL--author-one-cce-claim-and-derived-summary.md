---
subjects:
  governs: "Atom Claim Authoring"
  depends_on:
    - "Atom/Claim"
    - "CCE"
    - "Atom/Summary"
version: 25
updated_at: "2026-10-02 20:25:13 +0400"
relations: {"relates_to": ["CA-R-1624", "CA-O-103", "CA-D-479", "CA-R-1465"]}
atom_id: "CA-M-111"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Author one CCE Claim and derived Summary

## Scope

authoring an Atom's primary contribution, its applicability, **and** its derived Summary.

## Claim

**to** author one CCE Claim **and** its derived Summary, an Author **must** use these authoring constraints:

- express **`=1`** independently replaceable contribution using the applicable CCE Content Role profile. carry it under the primary contribution heading registered **in** CA-D-479 rather than imposing the literal heading Claim on **every** role.
- resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit as the authoring default **or** an explicitly permitted different target; carry the resolved value under CA-D-482. express applicability under CA-D-495. for RMED, describe what the Claim applies **to**, including applicable conditions **and** exclusions, **in** Scope; do **not** merely repeat the carried current **or** target Scope Unit; those restrictions alone do **not** make the Atom Relational.
- keep Details within the primary contribution under CA-R-1624. for RMED, read the Claim within its Scope; Details **must not** change either. **if** supporting content reveals an incomplete **or** inaccurate contribution **or** applicability, revise the affected Scope **or** primary contribution explicitly **and** recheck agreement; do **not** hide the change **in** Details.
- write Summary **only after** the other body sections **and** the contribution review are complete. shorten the finalized primary contribution under CA-R-1465 **and** CA-R-1273. for RMED, summarize the Claim within its finalized Scope, **not** the Scope alone; do **not** substitute supporting Results **or** TLDR as the source.
- for an existing Atom, retain the established Summary **and** check its faithfulness; **if** the Summary needs changing, use a new Atom identity under CA-R-1464.
- derive **every** Translation from the full corresponding source content, **not** the Summary.

## Details
