---
atom_id: "CA-D-502"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Carrier"
  depends_on: []
version: 1
updated_at: "2026-09-28 15:12:22 +0400"
relations: {}
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-502-PROJECT_CONFIGURATION--exclude-secrets-from-production-logs.md
  source_atom_id: CA-D-502
  source_atom_revision: 1
  source_sha256: b59982d93ad84f2017e52209eab1980e205c7d6e1da8408290c64a1fd798307c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Exclude secrets from production logs

## Scope

production logs that can contain credentials **or** secret-bearing payloads.

## Claim

production logs **must not** contain passwords, API keys, access tokens, session secrets, cookies, private keys, complete credentials, **or** unredacted secret-bearing payloads.

## Details

this is the explicit secret-exposure boundary for production log records.
