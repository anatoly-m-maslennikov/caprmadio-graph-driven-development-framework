---
content_role: Requirement
type: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Projection"
  depends_on:
    - "Artifact"
    - "Entity"
    - "Scope Unit"
    - "Single Source of Truth"
version: 1
updated_at: "2026-09-23 20:47:56 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1470", "CA-R-1568", "CAPRMEDIO-META-REQU-657"]}
---
# Summary

Distinguish projected representations from represented Entities

## Claim

a representation inside a Projection **must** remain distinct from the Entity it represents.

- depicting an existing Artifact **or** Scope Unit does **not** create another authoritative Artifact **or** Scope Unit.
- a representation **may** identify a source Entity **or** a derived element admitted by the Projection specification; source identities **and** traceability remain governed by CAPRMEDIO-META-REQU-657.
- this boundary introduces no separate Projection Element Term, lifecycle, **or** independently maintained authority.
