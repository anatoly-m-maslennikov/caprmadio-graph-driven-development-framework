---
subjects:
  governs: "Generated Data Stage Prefix"
  depends_on:
    - "artifact-catalog"
version: 20
updated_at: "2026-10-03 01:23:33 +0400"
relations:
  {"depends_on": ["CA-R-1717"]}
atom_id: "CA-R-1642"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1642-PROJECT_CONFIGURATION--register-generated-data-stages.md
  source_atom_id: CA-R-1642
  source_atom_revision: 20
  source_sha256: 0da1ada98921a43f7be3bb45792340b32d331022c8e595a19820c288a7b02291
  original_relations_sha256: 080cb6f24a7609727534ac841ce386ea45ed2b79d336841326c46d4f28302a52
---
# Summary

Register generated-data stages

## Scope

the ordered generated-data pipeline stages.

## Claim

the following ordered generated-data pipeline stages **must** be registered, referenced by their Carrier prefixes governed by CA-D-388-PROJECT_CONFIGURATION--serialize-generated-data-stage-prefixes-and-formats:

| Stage reference | Stage meaning |
| --- | --- |
| `src` | canonical Journal input; authority comes from the Journal, **not** the prefix. |
| `stg` | deterministic, lossless Projection of a bounded `src` frontier. |
| `mrt` | consumer-ready semantic Projection, including Requirement groupings by scope **and** tier **or** Mermaid relation maps. |
| `biz` | aggregated CAPRMEDIO artifact **and** implementation metrics, including point-in-time snapshots **and** historical trends. |

dependencies **must** move forward through `src → stg → mrt → biz`; a stage **may** depend on **any** earlier registered stage but **must not** depend on a later stage.

## Details
