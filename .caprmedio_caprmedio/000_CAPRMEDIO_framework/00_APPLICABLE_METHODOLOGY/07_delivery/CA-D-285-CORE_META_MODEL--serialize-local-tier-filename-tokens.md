---
subjects:
  governs: "Atom/Local Tier/Filename Token"
  depends_on:
    - "Atom"
    - "Atom/Local Tier"
    - "Atom/Local Tier: Standard"
    - "Change Content Roles"
    - "Implementation"
    - "Artifact/Carrier"
version: 13
updated_at: "2026-10-02 18:57:51 +0400"
relations: {"delivery_for": ["CA-R-1566"]}
atom_id: "CA-D-285"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-285-CORE_META_MODEL--serialize-local-tier-filename-tokens.md
  source_atom_id: CA-D-285
  source_atom_revision: 13
  source_sha256: 4434a46931e802ff2c4e0a722f2be39a907314480e8e057c7ac31a99f1b94856
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Local Tier Filename Tokens

## Scope

Ordinary Atom filenames subject **to** the role-tier restrictions under CA-R-1566.

## Claim

an ordinary Atom filename **must** serialize Principle as `PRINCIPLE`, Core as `CORE`, General as `GENERAL`, **and** the default Standard Local Tier by omitting the Local Tier segment at the registered descriptor position **after** its identity **and** current Scope owner. `PRINCIPLE` is admitted **only** for a Project-scoped Atom; `STD`, `STANDARD`, `DETAIL`, **and** combined tier segments **must not** be serialized. the external Project Goal's registered tierless grammar **must** be recognized **before** applying the ordinary omitted-Standard default; a tier token **must not** replace **or** alter the registered identity, owner, target, **or** sequence grammar of a Goal **or** Plan.

## Details
