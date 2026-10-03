---
subjects:
  governs: "Subject Expression"
  depends_on:
    - "Entity"
    - "Term"
    - "Property"
    - "Subject"
    - "Atom"
version: 12
updated_at: "2026-09-28 15:12:22 +0400"
relations: {}
atom_id: "CA-R-1321"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary
Define Subject Expression

## Scope
Subject Expressions formed from Term references **and** registered relation syntax.

## Claim

a Subject Expression **means** a reference **to** **`=1`** Entity formed from Term references **and** registered relation syntax. **every** named component, including the initial target name, Property names, **and** named allowed values, references a Term; `/` **and** `:` are syntax, **not** Terms. the expression identifies the target, **not** the Atom's Subject Relation **to** it.

## Details
