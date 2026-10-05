---
subjects:
  governs: "CAPRMEDIO/Temporary State Carrier Root"
  depends_on: []
version: 11
updated_at: "2026-10-02 19:05:39 +0400"
relations: {}
atom_id: "CA-D-321"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-321-PROJECT_CONFIGURATION--place-disposable-temporary-state.md
  source_atom_id: CA-D-321
  source_atom_revision: 11
  source_sha256: 1e55763577de42ab991a3cb98d6ca0780ac20adf82b3e29503af9d8d2ed1a872
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Place Disposable Temporary State

## Scope

disposable temporary state in a CAPRMEDIO Project.

## Claim

the CAPRMEDIO Project **must** place disposable scratch, staging, test cache, atomic-write intermediate, build intermediate, **and** interrupted-cleanup Carriers under `.caprmedio_tmp/`.

## Details

deleting `.caprmedio_tmp/` **must not** delete governed authority, Project Journal history, installed Framework Engine releases, runtime logs, sessions, databases, service state, **or** resumable state.
