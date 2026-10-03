---
content_role: Delivery
type: Delivery
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "PROGRAMMATIC/machine boundary schema Carrier"
  depends_on:
    - "App"
    - "Artifact/Carrier"
    - "Artifact/Revision"
    - "PROGRAMMATIC/software carriers"
    - "Tool"
    - "compatibility-boundary"
version: 1
updated_at: "2026-09-23 19:08:49 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-M-159"], "relates_to": ["CA-D-250", "CA-E-394", "CA-E-397", "CA-M-166", "CA-M-281", "CA-M-286"]}
---
# Summary

Publish version-bound machine boundary schemas

## Claim

**when** another Tool, App, protocol peer, **or** external system consumes the schema of a PROGRAMMATIC structured-data boundary, its integration-contract Carrier **must** publish a generated JSON Schema bound **to** the delivered interface Revision.

- the published schema identifies its owning interface **and** schema version, **and** represents the accepted fields, constraints, **and** extra-field policy selected by CA-M-159 **and** CA-M-286.
- the publication carries the applicable serialization contract **and** version references needed **to** interpret it. deterministic serialization is specified **where** it is part of the declared public behavior; no new universal serialization algorithm is selected here.
- **when** Pydantic supplies the schema, the publication identifies the supported Pydantic version boundary from the accepted technical configuration **without** selecting a new version **or** copying its authoritative selection.
- the schema **and** its version references occupy the owning component's declared integration-contract location under CA-D-250. component-specific interfaces remain owned by that component under CA-M-166.
