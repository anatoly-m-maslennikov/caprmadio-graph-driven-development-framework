---
content_role: Delivery
type: Delivery
current_scope_unit: GRAPH_UI
claim_target_scope_unit: GRAPH_UI
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "GRAPH_UI/interface-state Carriers"
  depends_on:
    - "Atom"
    - "Carrier"
    - "Journal"
    - "Project Temporary State"
    - "Projection"
version: 1
updated_at: "2026-09-23 19:20:45 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-R-1076"], "relates_to": ["CA-D-437", "CA-D-489", "CA-M-153", "CA-M-222", "CA-R-1100"]}
---
# Summary

Separate interface state from governed sources

## Claim

GRAPH_UI interface-state Carriers **must** remain separate from governed source Artifacts **and** from the delivered frontend assets.

- filter **and** focused-node state use their existing URL representation under CA-M-153; transient interface state remains session-local **unless** an explicit retained-state binding applies.
- retained UI service state uses its declared project-local runtime location. disposable frontend build output **and** caches use Project Temporary State under CA-D-437.
- retained state identifies its interface owner **and** referenced source frontier; it **must not** carry an independently authoritative copy of an Atom, Journal, **or** graph Projection.

CA-D-489 **and** the existing frontend Delivery declaration retain ownership of frontend placement. this state boundary does **not** split embedded assets, select a new browser-output filename, **or** change the service contract under CA-M-222.
