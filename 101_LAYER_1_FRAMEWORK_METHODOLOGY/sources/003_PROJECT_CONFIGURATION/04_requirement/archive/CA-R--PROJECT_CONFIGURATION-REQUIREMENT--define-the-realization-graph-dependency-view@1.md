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
    - "Entity"
    - "Projection"
    - "Relation"
version: 1
updated_at: "2026-09-23 20:47:56 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1246", "CA-R-1494", "CAPRMEDIO-META-REQU-657"]}
---
# Summary

Define the Realization Graph dependency view

## Claim

the dependency view of a Realization Graph **means** an optional derived view of the selected declarations, resources, internal dependency targets, external dependency targets, **and** admitted typed Relations among them.

- its specification identifies the selected population, Relation Types, source boundary, **and** limits of dependency traversal; recursive reachability does **not** establish complete coverage by itself.
- reuse the same source-backed graph facts rather than maintaining another dependency authority. cycles are represented **when** evidenced; their validity is checked against applicable Claims rather than assumed from the view name.
- this view does **not** require a paired Carrier Face **or** a second universal view.
