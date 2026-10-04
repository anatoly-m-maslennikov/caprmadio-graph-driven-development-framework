---
subjects:
  governs: "DEPENDS_ON"
  depends_on:
    - "Subject"
    - "Atom/Subjects"
    - "Entity"
    - "Atom/Claim"
    - "Atom/Summary"
version: 16
updated_at: "2026-10-02 21:52:05 +0400"
relations: {}
atom_id: "CA-R-1280"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1280-CORE_META_MODEL-CORE-REQUIREMENT--reference-every-prerequisite-subject-through-depends-on.md
---
# Summary

Reference Every Prerequisite Subject through DEPENDS_ON

## Scope

coverage of canonical Entity mentions by an Atom's Subjects.

## Claim

**every** Atom's Subject targets **must** be exactly the distinct canonical Entities independently mentioned **in** its Markdown Main Content, **not** an Atom citation label rendered under `CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand` as the referenced Atom's complete filename **without** its `.md` extension **or** directory path: **`=1`** GOVERNS target for the Entity governed by its Claim, **and** DEPENDS_ON targets for **every** other mentioned Entity.

## Details

coverage includes Summary **and** **all** other body sections, nested headings, tables, examples, **and** reference labels. an Atom citation label is readable authority evidence, **not** an Entity mention **or** Subject target. this exclusion holds **when** the label occurs **in** the same sentence as Entity language; inventory that Entity **only** **when** the surrounding prose independently uses it. a mention outside Claim is **not** otherwise optional coverage. do **not** repeat GOVERNS **in** DEPENDS_ON **or** include an Entity absent from Main Content. a qualified Subject Path identifies its complete target; its component Terms **and** implicit bearer prefixes are **not** additional Entity mentions **unless** independently referenced. Subjects remain Relations rather than their Entity targets. unresolved Entity mentions require resolution **before** coverage can pass.
