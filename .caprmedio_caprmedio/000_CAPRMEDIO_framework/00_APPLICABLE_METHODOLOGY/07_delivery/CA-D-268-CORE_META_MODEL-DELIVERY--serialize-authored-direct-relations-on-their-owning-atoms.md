---
subjects:
  governs: "Atom/Direct Relation Serialization"
  depends_on:
    - "Atom/Relation Owner"
version: 12
updated_at: "2026-10-02 18:57:51 +0400"
relations: {}
atom_id: "CA-D-268"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-268-CORE_META_MODEL-DELIVERY--serialize-authored-direct-relations-on-their-owning-atoms.md
  source_atom_id: CA-D-268
  source_atom_revision: 12
  source_sha256: 2afc204f59d90286345c9f4b5f74f8fcf2b8b40b992ab5aca734b0ad53e46335
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Authored Direct Relations on Their Owning Atoms

## Scope

Authored direct semantic relations.

## Claim

**every** authored direct semantic relation **must** be serialized once under `relations.<RELATION_KIND>` on the Atom that owns its declared direction as a nonempty unordered collection of unique canonical target references **in** deterministic canonical order; target position **must not** add, remove, **or** alter a direct relation **or** dependency.

## Details
