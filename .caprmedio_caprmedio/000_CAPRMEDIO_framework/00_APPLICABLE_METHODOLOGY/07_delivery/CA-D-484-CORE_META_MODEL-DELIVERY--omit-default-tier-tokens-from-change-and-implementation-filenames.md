---
subjects:
  governs: "Atom Carrier/Filename/Local Tier"
  depends_on:
    - "Change Content Roles"
    - "Implementation"
    - "Atom/Local Tier: Standard"
    - "Projection"
version: 4
updated_at: "2026-10-01 21:36:04 +0400"
relations: {"relates_to": ["CA-R-1566", "CA-D-285", "CA-D-478"]}
atom_id: "CA-D-484"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-484-CORE_META_MODEL-DELIVERY--omit-default-tier-tokens-from-change-and-implementation-filenames.md
  source_atom_id: CA-D-484
  source_atom_revision: 4
  source_sha256: b64b3b5f2cb9c0e246fc6b7fd314610d19fb99168fb6bbdb2a7d76e3b086e66f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Omit default tier tokens from Change **and** Implementation filenames

## Scope

CAPO **or** I Atom filenames that carry the default Standard Local Tier.

## Claim

a CAPO **or** I Atom filename **must** omit the default Standard Local Tier token under CA-D-285-CORE_META_MODEL-DELIVERY--serialize-local-tier-filename-tokens while the Atom carries its Local Tier internally under CA-D-478-CORE_META_MODEL-CORE-DELIVERY--store-every-atom-property-in-one-internal-location.

this filename rule does **not** add Atom Properties **to** a non-Atom Artifact **or** alter the represented source Properties **in** a Projection.

## Details
