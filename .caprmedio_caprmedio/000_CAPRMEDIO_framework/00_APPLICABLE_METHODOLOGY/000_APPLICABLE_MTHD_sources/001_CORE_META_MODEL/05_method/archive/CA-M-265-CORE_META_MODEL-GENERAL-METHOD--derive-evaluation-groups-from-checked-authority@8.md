---
subjects:
  governs: "Atom/Content Role: Evaluation/grouping"
  depends_on:
    - "Atom/Content Role"
    - "Evaluation For Relation"
version: 8
updated_at: "2026-09-10 02:19:47 +0400"
relations: {}
atom_id: "CA-M-265"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Method"
---
# Derive evaluation groups from checked authority

**to** derive Er, Em, **and** Ed groups, resolve the Content Role of **every** `evaluation_for` target **and** include the Evaluation **in** the corresponding Requirement, Method, **or** Delivery group; **if** targets span multiple roles, **then** include it **in** **every** applicable group **without** assigning a new Content Role **or** persisting a duplicate target-role field. absence of individual targets on a Core **or** General Evaluation policy admitted by CA-R-1018 **must not** require an invented classification.
