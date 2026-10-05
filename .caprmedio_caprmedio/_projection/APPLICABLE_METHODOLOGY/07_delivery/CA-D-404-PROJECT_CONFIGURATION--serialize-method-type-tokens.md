---
subjects:
  governs: "Atom/Content Role: Method/Type"
  depends_on:
    - "Carrier"
version: 9
updated_at: "2026-10-01 21:24:33 +0400"
relations: {}
atom_id: "CA-D-404"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-404-PROJECT_CONFIGURATION--serialize-method-type-tokens.md
  source_atom_id: CA-D-404
  source_atom_revision: 9
  source_sha256: e0dd421979dc6630420538c550c79dfc270bccfe27fe7a35361f87a22aedecce
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Method Type Tokens

## Scope

Method Atom File Carriers.

## Claim

a Method Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283-CORE_META_MODEL-CORE-DELIVERY--serialize-project-owned-markdown-atom-filenames **and** CA-D-284-CORE_META_MODEL-CORE-DELIVERY--serialize-filename-token-case:

- Implementation Method: `IMPLEMENTATION_METHOD`.
- Implementation Decision: `IMPLEMENTATION_DECISION`.
- External Implementation Method: `EXTERNAL_IMPLEMENTATION_METHOD`.
- Method Binding: `METHOD_BINDING`.

## Details

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
