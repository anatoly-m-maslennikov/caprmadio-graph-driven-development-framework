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
  governs: "Relation Derivation Class"
  depends_on:
    - "Evidence"
    - "Realization Graph"
    - "Relation"
version: 5
updated_at: "2026-09-23 20:47:56 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CAPRMEDIO-META-REQU-097"]}
---
# Summary

Define Relation Derivation Class

## Claim

Relation Derivation Class **means** a classification of how a represented Realization Graph Relation is supported by source declarations, deterministic resolution, possible inference, **or** recorded observation.

it classifies the derivation evidence, **not** the Relation's validity **or** governing authority. multiple supported classes **may** apply **to** the same Relation; their evidence boundaries remain distinguishable.
