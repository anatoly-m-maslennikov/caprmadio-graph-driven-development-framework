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
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression.md
  source_atom_id: CA-R-1321
  source_atom_revision: 12
  source_sha256: 6baf3f4179591dcc89c458dcb6503a55f24b70f9f1bd93203f4b748a9bcb1b8c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Define Subject Expression

## Scope
Subject Expressions formed from Term references **and** registered relation syntax.

## Claim

a Subject Expression **means** a reference **to** **`=1`** Entity formed from Term references **and** registered relation syntax. **every** named component, including the initial target name, Property names, **and** named allowed values, references a Term; `/` **and** `:` are syntax, **not** Terms. the expression identifies the target, **not** the Atom's Subject Relation **to** it.

## Details
