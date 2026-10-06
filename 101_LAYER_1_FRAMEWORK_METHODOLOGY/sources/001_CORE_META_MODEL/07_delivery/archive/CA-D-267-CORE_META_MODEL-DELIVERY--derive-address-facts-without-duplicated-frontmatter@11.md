---
subjects:
  governs: "Carrier/Canonical Address"
  depends_on:
    - "Artifact/Property"
    - "Atom/Frontmatter"
version: 11
updated_at: "2026-09-22 23:02:20 +0000"
relations: {}
atom_id: "CA-D-267"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Summary

Derive Address Facts without Duplicated Frontmatter

## Claim

**if** a registered canonical Carrier address completely **and** unambiguously derives a non-Atom Artifact Property, **then** that address **must** be its sole Carrier encoding **and** embedded metadata **must not** duplicate it. Atom Properties instead follow CA-D-478 **and** CA-D-480.
