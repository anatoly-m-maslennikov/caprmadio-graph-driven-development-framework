---
subjects:
  governs: "Apply Structural Change"
  depends_on:
    - "Action"
    - "Project Structure"
    - "Operator"
    - "Carrier"
    - "Goal"
    - "Journal"
version: 5
updated_at: "2026-09-15 00:13:02 +0000"
relations: {}
atom_id: "CA-O-014"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-014-CORE_META_MODEL-ACTION--apply-structural-change.md
---
# Apply structural change

Apply Structural Change **means** the Action that rechecks the authorized proposal against the unchanged selected source state **and** applies its accepted declarations, reference repairs, **and** explicitly included Carrier changes through one recoverable cutover. **if** the source state differs, required validation fails, **or** permission no longer covers the effects, it **must** stop **before** mutation. **if** a partial failure occurs, it **must** report the actual effects **and** use **only** the authorized recovery boundary; it **must not** delete unapproved contents, overwrite concurrent edits, reset the retry budget, **or** claim a completed migration. event evidence follows the applicable Journal model, **not** a second structural authority.
