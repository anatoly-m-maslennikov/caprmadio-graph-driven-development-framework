---
subjects:
  governs: "Subject Expression Writing"
  depends_on:
    - "Subject Path"
    - "Entity"
    - "Relation"
    - "Term"
    - "Subject"
    - "GOVERNS"
    - "DEPENDS_ON"
version: 13
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
atom_id: "CA-M-228"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Method"
---
# Write Subject Expressions with Bearer and Value Qualification

**to** write a Subject Expression, start with a canonical Entity reference **and** apply `/` **or** `:` qualification **only** **where** the registered relation admits the exact endpoints. `/` retains bearer qualification **and** `:` retains allowed-value qualification; resolve **every** named component, including names **before** **and** **after** the separators, as a Term reference under CA-R-1321. the resulting qualified path identifies its existing canonical target **without** copying it; connecting the Atom **to** that target through GOVERNS **or** DEPENDS_ON creates the Subject Relation, **not** another target Entity.
