---
subjects:
  governs: "extension-model"
  depends_on:
    - "Framework Instance Settings"
version: 17
updated_at: "2026-10-03 02:41:52 +0400"
relations:
  child_of:
    - "CA-R-1709"
    - "CA-R-1722"
atom_id: "CA-R-1733"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1733-CORE_META_MODEL--separate-extension-ownership-from-application-bindings.md
  source_atom_id: CA-R-1733
  source_atom_revision: 17
  source_sha256: a26768fbd323012ded3622c8921cf3d9c013bc42fdd51d07e4f304b0447526ed
  original_relations_sha256: 5536d80246aa6685803605f13b8201a406b184979e50ecb0896e3c62158c2792
---
# Summary

Separate Extension ownership from application bindings

## Scope

Extensions **and** their application bindings within the current project.

## Claim

an Extension is an owned capability package whose Governance Origin is internal **or** external relative **to** the current project. an Extension application is a separate binding Atom whose typed relations identify the applied Extension **and** target Scope Units.

## Details

the application binding does **not** own **or** duplicate current Extension activation **or** selected Extension revision decisions; those decisions remain owned by the Framework Instance Settings Artifact under CA-R-1207 **and** CA-R-1724.
