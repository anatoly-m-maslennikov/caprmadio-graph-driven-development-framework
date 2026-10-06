---
atom_id: "CA-D-498"
version: 1
updated_at: "2026-10-02 19:54:46 +0400"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Atom/Scope/Filename Token"
  depends_on:
    - "Atom"
    - "Project"
    - "Scope Unit"
    - "Scope Unit/Name"
relations:
  depends_on:
    - CA-D-284
    - CA-D-302
---
# Summary

Use full Scope Unit names in filenames

## Scope

Scope Unit references serialized **in** Atom filenames **in** the CAPRMEDIO Project.

## Claim

**every** filename token representing a Scope Unit **must** use its complete Scope Unit Name, rendered **in** uppercase with underscores under `CA-D-284-CORE_META_MODEL-DELIVERY--serialize-filename-token-case`, **without** abbreviation **or** a separately maintained alias.

## Details

this selects the representation required by `CA-D-302-CORE_META_MODEL-DELIVERY--serialize-scope-unit-references-as-filename-tokens`. `CORE_META_MODEL` remains `CORE_META_MODEL`; `PROJECT_CONFIGURATION` remains `PROJECT_CONFIGURATION`. the Scope Unit Name is the source; the filename token is its representation.
