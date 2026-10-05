---
subjects:
  governs: "CAPRMEDIO/Framework Engine Runtime Carrier Root"
  depends_on: []
version: 13
updated_at: "2026-10-04 22:10:46 +0000"
relations: {}
atom_id: "CA-D-320"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-320-PROJECT_CONFIGURATION--place-framework-engine-runtime-carriers.md
  source_atom_id: CA-D-320
  source_atom_revision: 13
  source_sha256: adfeda738036cc3b35ca485e835fa94656784531f6027065d264f4fd693ee968
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Place Framework Engine Runtime Carriers

## Scope

Framework Engine executable installation and mutable execution-state Carriers in a CAPRMEDIO Project.

## Claim

the CAPRMEDIO Project **must** place its selected running Framework Engine releases, stable launchers, Tools, Apps, Skills, sessions, service state, **and** resumable execution state under `.caprmedio_runtime/`. runtime technical **and** business Journal Carriers use their explicitly configured governed sinks **and** are **not** required **to** use this Directory Carrier.

## Details

Runtime executable copies and mutable service state do not govern RMED Claims. Selected releases, launchers, Tools, Apps, and Skills must be reconstructible from governed source and configuration. Journal history may be non-reconstructible and retains its recorded-history authority wherever its Carrier is delivered. Stopping, reinstalling, or deleting disposable runtime state must not remove accepted Journal records, including runtime Journal history retained in a local or remote sink. The Project Work Journal remains under the Project-control _journal directory.
