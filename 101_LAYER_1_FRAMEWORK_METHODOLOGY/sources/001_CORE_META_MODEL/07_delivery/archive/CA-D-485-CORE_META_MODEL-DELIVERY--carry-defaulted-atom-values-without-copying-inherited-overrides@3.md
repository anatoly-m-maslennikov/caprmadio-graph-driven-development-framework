---
subjects:
  governs: "Markdown Atom Carrier/YAML Frontmatter/Default"
  depends_on:
    - "Property"
    - "Artifact/Property/Default"
    - "Atom/Property"
    - "Autonomous Confidence Threshold"
    - "Implementation Retry Limit"
version: 3
updated_at: "2026-09-22 23:02:20 +0000"
relations: {"relates_to": ["CA-D-478", "CA-D-472", "CA-D-447"]}
atom_id: "CA-D-485"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Summary

Carry defaulted Atom values without copying inherited overrides

## Claim

a writer **must** preserve the distinction between a defaulted Atom Property **and** an inherited external setting:

- a required Atom value selected by applying a default is still carried at its canonical internal location; equality **to** that default does **not** permit omitting the value.
- an unselected optional override remains absent; do **not** copy an inherited effective setting into a locally selected override.
- retain an explicit override even **when** it currently equals the inherited value, because later upstream changes **must not** change that selection.
