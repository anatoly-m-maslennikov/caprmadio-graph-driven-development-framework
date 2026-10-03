---
subjects:
  governs: "Owned Atoms"
  depends_on:
    - "Atom"
    - "Scope Unit"
    - "Atom Collection"
version: 7
updated_at: "2026-09-24 13:59:55 +0000"
relations: {}
atom_id: "CA-R-1447"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define Owned Atoms

Owned Atoms **means** the set of **all** Atoms whose internally carried current Scope Unit equals the selected Scope Unit.

- a grouping Carrier, Plan decomposition, **or** physical placement does **not** replace that ownership value.
- a missing, invalid, **or** ambiguous ownership value leaves membership unresolved; do **not** derive it from the filename **or** containing folders.
- evaluate placement consistency separately **without** changing the selected Atom's declared ownership.
