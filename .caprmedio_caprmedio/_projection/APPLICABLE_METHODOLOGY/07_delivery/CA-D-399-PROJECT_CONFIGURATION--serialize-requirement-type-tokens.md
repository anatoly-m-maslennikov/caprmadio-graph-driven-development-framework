---
subjects:
  governs: "Atom/Content Role: Requirement/Type"
  depends_on:
    - "Carrier"
version: 9
updated_at: "2026-10-02 19:36:21 +0400"
relations: {}
atom_id: "CA-D-399"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-399-PROJECT_CONFIGURATION--serialize-requirement-type-tokens.md
  source_atom_id: CA-D-399
  source_atom_revision: 9
  source_sha256: 1f356dc9e8620886115f5e857dd5a9e518681787a9020942d01eeb51aa410b20
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Requirement Type Tokens

## Scope

the serialization of Requirement Type tokens in a Requirement Atom File Carrier filename.

## Claim

a Requirement Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Constraint: `CONSTRAINT`.
- Boundary: `BOUNDARY`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.

## Details
