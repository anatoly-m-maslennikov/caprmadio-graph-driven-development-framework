---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Carrier/Filename"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Label"
    - "Atom/Content Role: Plan/Type: Plan/Work Sequence Number"
    - "Atom/Summary"
    - "Atom/Identity"
    - "Carrier"
version: 3
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"relates_to": ["CA-R-1576", "CA-R-991", "CA-D-381", "CA-D-282", "CA-D-284", "CA-D-460", "CA-R-997"]}
atom_id: "CA-D-469"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Serialize Plan Carrier stems

**every** identified Plan Carrier stem **must** use `[<WORK_SEQUENCE_NUMBER>-]<ATOM_ID>[-<LABEL>]--<SUMMARY_SLUG>`, with `.md` **only** on its File Carrier.

- the optional Label is a navigation token, **not** an Atom Type token; normalize it under CA-D-284.
- render the Summary under CA-D-282.
- **by default**, direct Plans decomposing the same Hub use unique leading Work Sequence Numbers **before** their Atom IDs, under CA-D-381 **and** CA-R-997.
- a same-bundle Directory Carrier **and** File Carrier use the same stem; number **or** Label changes preserve Atom identity **and** do **not** declare `BLOCKS`.
