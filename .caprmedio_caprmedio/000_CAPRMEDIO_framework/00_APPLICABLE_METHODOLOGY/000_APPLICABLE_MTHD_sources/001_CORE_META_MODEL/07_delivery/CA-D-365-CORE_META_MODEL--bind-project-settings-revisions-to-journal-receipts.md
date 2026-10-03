---
subjects:
  governs: "Project Settings/Revision Binding"
  depends_on:
    - "Artifact/Revision"
    - "Work Journal/Record"
version: 11
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - CA-D-364
atom_id: "CA-D-365"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Bind Project Settings Revisions to Journal Receipts

## Scope

the current Project Settings Revision and SHA-256 Digest.

## Claim

the current Project Settings Revision **and** SHA-256 Digest **must** bind **to** its authoritative TOML Carrier through the canonical completed governed-change Work Journal receipt; absence, ambiguity, **or** mismatch **must** leave its currentness unknown.

## Details
