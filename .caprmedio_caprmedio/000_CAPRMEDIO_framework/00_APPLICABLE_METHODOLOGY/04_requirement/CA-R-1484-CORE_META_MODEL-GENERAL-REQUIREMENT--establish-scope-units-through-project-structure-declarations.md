---
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Project Structure"
    - "Project Settings"
    - "Project"
    - "Atom/Content Role: Requirement/Type: Goal"
    - "Structural Parent Relation"
version: 5
updated_at: "2026-10-02 23:35:16 +0400"
relations: {}
atom_id: "CA-R-1484"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1484-CORE_META_MODEL-GENERAL-REQUIREMENT--establish-scope-units-through-project-structure-declarations.md
---
# Summary

Establish Scope Units through Project Structure declarations

## Scope

non-Project Scope Unit declarations in their owning Project Structure.

## Claim

**every** non-Project Scope Unit **must** have **`=1`** declaration **in** its owning Project Structure that supplies its unique Name, direct parent, Type, Label, applicable Local Order, navigation number, **and** authority/Implementation Folder bindings. the declaration establishes the unit independently of Goal coverage **and** Carrier materialization; these remain separately evaluated conditions. Project Settings establishes the root identity, **and** Project Structure **must not** redeclare it as a child. Name/Order Atoms **and** concrete binding Atoms **must not** coexist as independent authorities for the same declared values.

## Details
