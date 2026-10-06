---
subjects:
  governs: "Directory Carrier/Numeric Prefix"
  depends_on:
    - "Scope Unit"
    - "Structural Level"
    - "Navigational Order Number"
version: 13
updated_at: "2026-09-17 14:21:56 +0000"
relations: {}
atom_id: "CA-D-300"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Size Structural Level Prefixes Dynamically

**when** the default Scope Unit directory convention is used, **every** Project-internal numeric Scope Unit Directory Carrier prefix **must** concatenate these components **without** a separator:

- the Structural Level, using the decimal digit count of the greatest current Project Structural Level as its width.
- the Navigational Order Number, using the decimal rendering governed by CA-D-380.

the total prefix width is the sum of those component widths, **not** a fixed limit on the Navigational Order Number. decoding consumes the Structural Level width first **and** treats the remaining digits as the Navigational Order Number. a declared native Carrier binding under CA-D-445 **must not** be reinterpreted through this default convention.
