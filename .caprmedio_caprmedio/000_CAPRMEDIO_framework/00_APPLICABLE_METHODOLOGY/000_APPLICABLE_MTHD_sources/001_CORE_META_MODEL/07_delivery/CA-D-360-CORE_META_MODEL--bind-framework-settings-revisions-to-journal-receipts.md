---
subjects:
  governs: "Framework Instance Settings/Revision Binding"
  depends_on:
    - "Artifact/Revision"
    - "Work Journal/Record"
version: 12
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - CA-D-359
atom_id: "CA-D-360"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Bind Framework Settings Revisions to Journal Receipts

## Scope

the current `caprmedio_framework_settings` Revision and SHA-256 Digest.

## Claim

the current caprmedio_framework_settings Revision **and** SHA-256 Digest **must** bind **to** its authoritative TOML Carrier through the canonical completed governed-change Work Journal receipt; absence, ambiguity, **or** mismatch **must** leave its currentness unknown.

## Details
