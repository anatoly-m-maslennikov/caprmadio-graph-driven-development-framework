---
subjects:
  governs: "Journal/Record"
  depends_on:
    - "Journal"
    - "Artifact/Carrier"
    - "Artifact/Revision"
    - "Actor"
version: 16
updated_at: "2026-09-17 13:36:16 +0000"
relations: {}
atom_id: "CAPRMEDIO-GOV-REQU-340"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Recover Work Journal coverage without invention

a `recovered` Journal event is admissible **only** for facts established by **any** of:

- observed Carrier state;
- preserved history;
- Artifact movement;
- native targets;
- review records; **or**
- bounded session state.

unresolved Actor, time, intent, scope, **or** outcome **must** remain explicit uncertainty rather than fabricated history.
