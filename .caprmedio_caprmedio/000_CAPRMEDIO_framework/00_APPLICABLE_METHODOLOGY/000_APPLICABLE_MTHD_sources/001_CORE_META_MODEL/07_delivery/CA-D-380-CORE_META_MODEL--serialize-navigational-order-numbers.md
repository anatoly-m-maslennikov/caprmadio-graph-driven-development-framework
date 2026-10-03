---
subjects:
  governs: "Navigational Order Number"
  depends_on:
    - "Carrier"
    - "Scope Unit"
    - "Project Structure"
version: 6
updated_at: "2026-10-02 19:27:36 +0400"
relations: {}
atom_id: "CA-D-380"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Navigational Order Numbers

## Scope

Carrier renderings of a Navigational Order Number.

## Claim

**every** Carrier rendering of a Navigational Order Number **must** use decimal digits. the default directory-name rendering of a non-Project Scope Unit **must** use **`>=2`** digits; a typed TOML integer stores the numeric value **without** leading-zero padding.

## Details
