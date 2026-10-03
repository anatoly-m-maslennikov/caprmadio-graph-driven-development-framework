---
subjects:
  governs: "Journal"
  depends_on:
    - "Artifact"
    - "Journal/Record"
    - "Atom/Claim"
version: 14
updated_at: "2026-09-14 06:21:07 +0400"
relations: {}
atom_id: "CAPRMEDIO-META-REQU-656"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define Journal Artifact form

a Journal, also called an Event Log, **means** an authoritative Artifact whose recorded history forms **`=1`** logically ordered table of admitted records about events. a record describes an event **and** its recorded evidence; the record is **not** the event itself **or** automatic proof of its asserted outcome. accepted records **must not** be edited, reordered, **or** removed; corrections append new traceable records **without** rewriting accepted history. Journal authority concerns recorded history **and** does **not** independently redefine governing Atom Claims.
