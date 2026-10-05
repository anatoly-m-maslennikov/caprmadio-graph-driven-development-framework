---
subjects:
  governs: "File Carrier"
  depends_on:
    - "Project"
    - "Project-Owned Carrier Root"
version: 4
updated_at: "2026-10-02 19:44:54 +0400"
relations: {}
atom_id: "CA-D-452"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-452-CORE_META_MODEL-STANDARD--place-local-environment-injection-carriers.md
  source_atom_id: CA-D-452
  source_atom_revision: 4
  source_sha256: d41df8b908601938efc6a08fdd661e6d51422950ce0c83070340592720a0980e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Place Local Environment Injection Carriers

## Scope

secret values and local environment injection Carriers.

## Claim

secret values **must** be stored **only** **in**:

- gitignored `.env` File Carriers; **or**
- a dedicated secret vault.

## Details

### File placement

- a repository-local `.env` File Carrier **must** remain outside **every** applicable Project authority Carrier root.
- **every** real `.env` variant **must** be gitignored, untracked, **and** excluded from durable **or** shared Git history **and** CAPRMEDIO discovery. a Git ignore rule does **not** remove a previously tracked secret from history.
- a tracked `.env.example` **may** contain variable names **and** unmistakable dummy placeholders **only**.

### Runtime injection

secret values **may** reach authorized runtime consumers through host injection from a permitted secret store; the injected value is **not** a separate persisted source.
