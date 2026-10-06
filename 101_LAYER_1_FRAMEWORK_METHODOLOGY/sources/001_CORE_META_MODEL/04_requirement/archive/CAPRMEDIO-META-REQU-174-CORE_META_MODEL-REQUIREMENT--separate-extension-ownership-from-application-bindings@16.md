---
subjects:
  governs: "extension-model"
  depends_on:
    - "Framework Instance Settings"
version: 16
updated_at: "2026-09-10 20:57:22 +0400"
relations:
  child_of:
    - CAPRMEDIO-META-REQU-127-CORE_META_MODEL-CORE-REQUIREMENT--define-two-governance-origins
    - CAPRMEDIO-META-REQU-160-CORE_META_MODEL-CORE-REQUIREMENT--govern-extension-semantics
atom_id: "CAPRMEDIO-META-REQU-174"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 11
---
# Separate Extension ownership from application bindings

an Extension is an owned capability package whose Governance origin is internal **or** external relative **to** the current project. an Extension application is a separate binding Atom whose typed relations identify the applied Extension **and** target Scope Units.

the application binding does **not** own **or** duplicate current Extension activation **or** selected Extension revision decisions; those decisions remain owned by the Framework Instance Settings Artifact under CA-R-1207 **and** CAPRMEDIO-META-REQU-163.
