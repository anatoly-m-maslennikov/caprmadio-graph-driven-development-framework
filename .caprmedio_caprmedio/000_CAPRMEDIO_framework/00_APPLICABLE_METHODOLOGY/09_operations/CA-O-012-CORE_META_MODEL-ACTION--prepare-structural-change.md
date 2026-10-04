---
subjects:
  governs: "Prepare Structural Change"
  depends_on:
    - "Action"
    - "Project Structure"
    - "Scope Unit"
    - "Goal"
    - "Carrier"
    - "Artifact/Revision"
version: 5
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  relates_to:
    - "CA-M-291"
    - "CA-R-926"
atom_id: "CA-O-012"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-012-CORE_META_MODEL-ACTION--prepare-structural-change.md
---
# Prepare structural change

Prepare Structural Change **means** the Action that produces one bounded change proposal against the exact current Project Structure state. the proposal identifies the requested creation, rename, reparenting, reorder, path rebinding, removal, **or** reconciliation; its expected declarations; affected references, Goals, descendants **and** Carriers; required source changes; validation conditions; **and** a recoverable cutover boundary. a rename **or** reparenting **must** account for incoming references **and** parent-owned Goals, rather than leaving them attached **to** a different unit. declaration removal **must not** imply Carrier deletion. an undeclared folder, missing folder, **or** missing Active Goal is an observation requiring an explicit disposition, **not** permission **to** invent, erase, **or** accept authority.
