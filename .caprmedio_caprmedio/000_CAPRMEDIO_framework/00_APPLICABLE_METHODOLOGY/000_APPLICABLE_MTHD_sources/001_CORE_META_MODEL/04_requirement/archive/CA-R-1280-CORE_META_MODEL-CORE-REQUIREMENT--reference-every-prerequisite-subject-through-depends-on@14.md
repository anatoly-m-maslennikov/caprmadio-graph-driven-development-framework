---
subjects:
  governs: "DEPENDS_ON"
  depends_on:
    - "Subject"
    - "Atom/Subjects"
    - "Entity"
    - "Atom/Claim"
version: 14
updated_at: "2026-09-25 22:01:55 +0000"
relations: {}
atom_id: "CA-R-1280"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Archived"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Summary

Reference Every Prerequisite Subject through DEPENDS_ON

## Scope

coverage of canonical Entity mentions by an Atom's Subjects.

## Claim

**every** Atom's Subject targets **must** be exactly the distinct canonical Entities mentioned **in** its Markdown Main Content: **`=1`** GOVERNS target for the Entity governed by its Claim, **and** DEPENDS_ON targets for **every** other mentioned Entity.

## Details

coverage includes Summary **and** **all** other body sections, nested headings, tables, examples, **and** reference labels. a mention outside Claim is **not** optional coverage. do **not** repeat GOVERNS **in** DEPENDS_ON **or** include an Entity absent from Main Content. a qualified Subject Path identifies its complete target; its component Terms **and** implicit bearer prefixes are **not** additional Entity mentions **unless** independently referenced. Subjects remain Relations rather than their Entity targets. unresolved Entity mentions require resolution **before** coverage can pass.
