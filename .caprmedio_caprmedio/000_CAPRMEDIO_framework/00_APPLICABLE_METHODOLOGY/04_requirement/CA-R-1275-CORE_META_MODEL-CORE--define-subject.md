---
subjects:
  governs: "Subject"
  depends_on:
    - "Atom"
    - "Entity"
    - "Term"
    - "Relation"
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Subject Path"
version: 14
updated_at: "2026-10-01 21:41:08 +0400"
relations: {}
atom_id: "CA-R-1275"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1275-CORE_META_MODEL-CORE--define-subject.md
---
# Summary

Define Subject

## Scope

Subjects relating an Atom and an Entity.

## Claim

a Subject **means** a direct Relation between an Atom **and** an Entity, typed as GOVERNS **or** DEPENDS_ON.

## Details

- the Atom is the source; the Entity is the target identified by its full canonical Subject Path.
- the Subject is the Relation, **not** its target, its target's path, **or** a Term used **in** that path.
- the Relation creates no intermediate Subject object **and** no additional target identity; it does **not** make the target bearer-dependent on the source Atom.
