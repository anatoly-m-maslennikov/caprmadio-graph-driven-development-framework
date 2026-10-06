---
atom_id: CA-R-1608
content_role: Requirement
type: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: allowed_values
subjects:
  governs: "Atom/Content Role: Concern/Status"
  depends_on:
    - "Atom/Content Role: Concern"
    - "Artifact/Revision/Status"
version: 1
updated_at: "2026-09-23 21:34:42 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-R-1308
    - CA-R-1313
    - CA-R-1336
---
# Summary

Register Core Concern Status Values

## Claim

the Core allowed values of `Atom/Content Role: Concern/Status` **must** be exactly (`draft`, `active`, `resolved`, `canceled`).
