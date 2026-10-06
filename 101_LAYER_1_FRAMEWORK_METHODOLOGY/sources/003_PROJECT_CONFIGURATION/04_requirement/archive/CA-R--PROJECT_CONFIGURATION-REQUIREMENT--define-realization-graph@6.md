---
content_role: Requirement
type: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Realization Graph"
  depends_on:
    - "Atom/Revision"
    - "Entity"
    - "Implementation"
    - "Journal"
    - "Projection"
    - "Relation"
version: 6
updated_at: "2026-09-23 20:47:56 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1470", "CA-R-1493", "CA-R-1494", "CA-R-1568", "CAPRMEDIO-META-REQU-657"]}
---
# Summary

Define Realization Graph

## Claim

Realization Graph **means** a non-authoritative Projection of Entities **and** typed Relations derived from a declared selection of existing Implementation sources **and** available evidence, used **to** understand that Implementation **and** support reverse engineering into proposed RMED.

- retain source traceability under CAPRMEDIO-META-REQU-657 **and** generation identity under CA-R-1493. include **only** the source kinds selected for the job; legacy Implementation need **not** have pre-existing RMED **or** Journal records.
- report missing evidence **and** uncertain interpretations. observed structure **or** behavior does **not** establish intended Requirements, a passed Evaluation, **or** completeness outside the checked selection.
- the Artifact kind remains Projection, including **when** delivered as an Implementation output under CA-R-1568. views derive from its source-backed facts **without** creating another source of truth.
