---
subjects:
  governs: "Directory Carrier/Name"
  depends_on:
    - "Scope Unit/Type: Ordered"
    - "Scope Unit/Type: Unordered"
    - "Scope Unit/Label"
    - "Local Order"
version: 10
updated_at: "2026-09-15 00:13:02 +0000"
relations: {}
atom_id: "CA-D-298"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Serialize Local Order Only for Ordered Scope Unit Directories

**when** the default Scope Unit directory convention is used, a Scope Unit authority Directory Carrier Name **must** serialize Local Order immediately **after** Label **only** for an Ordered Scope Unit **and** **must not** serialize Local Order for an Unordered Scope Unit. a declared native Carrier binding under CA-D-445 **must not** be reinterpreted through this default convention.
