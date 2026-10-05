---
subjects:
  governs: "artifact-model"
  depends_on: []
version: 21
updated_at: "2026-10-03 02:15:29 +0400"
relations: {}
atom_id: "CA-R-1700"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1700-CORE_META_MODEL-CORE-REQUIREMENT--admit-atoms-only-where-a-role-has-an-atomic-unit.md
  source_atom_id: CA-R-1700
  source_atom_revision: 21
  source_sha256: 6df2206a5d6d534dead7d7d0a6994db1023345e515c40025a01004403cf25832
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Admit Atoms only where a role has an atomic unit

## Scope

Content Role Type admission.

## Claim

a Content Role admits a Type value for an Atom **only** **when** that role has an independently governed atomic unit that benefits from stable identity, admission, **and** whole-unit lifecycle; CAPRMEDIO **must not** create a placeholder Type value merely **to** fill a semantic coordinate.

## Details

an Atom with Content Role Requirement, Method, **or** Delivery has a role-qualified Type **only** **when** a separately governed specialized Type applies. an ordinary Atom in these roles has no role-qualified Type; its Content Role already identifies its contribution. a specialized Atom retains **`=1`** admitted Type under its Content Role.
