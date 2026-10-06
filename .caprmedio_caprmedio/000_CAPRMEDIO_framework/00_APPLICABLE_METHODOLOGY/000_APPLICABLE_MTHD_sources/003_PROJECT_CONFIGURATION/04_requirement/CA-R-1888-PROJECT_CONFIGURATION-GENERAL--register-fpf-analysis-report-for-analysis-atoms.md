---
atom_id: "CA-R-1888"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "General"
global_tier: 10
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Atom/Content Role: Analysis/Type"
  depends_on:
    - "Atom/Content Role: Analysis"
    - "FPF"
version: 1
updated_at: "2026-10-05 23:46:22 +0400"
relations:
  relates_to: ["CA-R-1232", "CA-R-1286", "CA-R-1889"]
---
# Summary

Register FPF Analysis Report for Analysis Atoms

## Scope

the CAPRMEDIO Project Configuration contribution to `Atom/Content Role: Analysis/Type`.

## Claim

the CAPRMEDIO Project Configuration **must** register FPF Analysis Report as an additional value of `Atom/Content Role: Analysis/Type` under CA-R-1286. this registration does **not** change the Core contribution under CA-R-1232 **or** create another Type Property.

## Details

CA-R-1889 defines the registered Type. CA-D-581 defines its filename token. The Type remains within Content Role Analysis.
