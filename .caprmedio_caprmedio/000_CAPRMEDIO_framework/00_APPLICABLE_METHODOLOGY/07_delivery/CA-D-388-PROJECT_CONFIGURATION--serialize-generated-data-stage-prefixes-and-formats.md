---
subjects:
  governs: "Generated Data Stage Prefix"
  depends_on:
    - "Journal"
    - "Projection"
    - "Carrier/Format"
version: 8
updated_at: "2026-10-02 19:27:36 +0400"
relations: {}
atom_id: "CA-D-388"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-388-PROJECT_CONFIGURATION--serialize-generated-data-stage-prefixes-and-formats.md
  source_atom_id: CA-D-388
  source_atom_revision: 8
  source_sha256: dfa9f38febc8d3040f7e4328e256a15d2b134036929111189b8cf2d97f8ff76c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Generated Data Stage Prefixes and Formats

## Scope

Journal input and generated Projection Carriers.

## Claim

Journal input **and** generated Projection Carriers **must** use these ordered stage prefixes: canonical Journal input `src`, deterministic lossless staging Projection `stg`, consumer-ready semantic Projection `mrt`, **and** aggregated metrics Projection `biz`. `src` **must** use canonical NDJSON Journal input; `stg` **must** use TOON. these prefixes classify Journal inputs **and** generated Projections **only**. unregistered stage prefixes remain available for later governed Extension.

## Details
