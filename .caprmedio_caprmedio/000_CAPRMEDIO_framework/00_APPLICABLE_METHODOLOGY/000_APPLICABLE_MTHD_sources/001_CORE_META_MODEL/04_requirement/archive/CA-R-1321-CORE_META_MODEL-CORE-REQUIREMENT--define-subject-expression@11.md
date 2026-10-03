---
subjects:
  governs: "Subject Expression"
  depends_on:
    - "Entity"
    - "Term"
    - "Property"
    - "Subject"
version: 11
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
atom_id: "CA-R-1321"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define Subject Expression

a Subject Expression **means** a reference **to** **`=1`** Entity formed from Term references **and** registered relation syntax. **every** named component, including the initial target name, Property names, **and** named allowed values, references a Term; `/` **and** `:` are syntax, **not** Terms. the expression identifies the target, **not** the Atom's Subject Relation **to** it.
