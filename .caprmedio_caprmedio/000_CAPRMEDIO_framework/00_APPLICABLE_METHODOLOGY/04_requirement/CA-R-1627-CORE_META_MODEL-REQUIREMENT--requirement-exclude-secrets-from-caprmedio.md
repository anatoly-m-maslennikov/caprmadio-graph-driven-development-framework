---
subjects:
  governs: "external-boundary"
version: 18
updated_at: "2026-10-03 01:07:45 +0400"
relations: {}
atom_id: "CA-R-1627"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1627-CORE_META_MODEL-REQUIREMENT--requirement-exclude-secrets-from-caprmedio.md
  source_atom_id: CA-R-1627
  source_atom_revision: 18
  source_sha256: 7a4452c2e826101eab3d3e19b9b7d672897606ad6f20850e1d330682749f5194
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Requirement — Exclude secrets from CAPRMEDIO

## Scope

secret values and their use across CAPRMEDIO surfaces.

## Claim

secret values **must** remain **in** the permitted secret storage defined by CA-D-452. secrets include passwords, API keys, access **or** refresh tokens, session cookies, private keys, signing **or** encryption keys, authentication certificates, one-time **or** recovery codes, **and** connection strings **or** URLs containing credentials.

### authorized use

- Tools **may** receive secrets from that storage, including through host injection, **and** use them for Operator-authorized authentication.
- credential use **must** remain within the authorized transport **and** resource boundary. permission **to** authenticate does **not** authorize disclosure elsewhere.

### excluded surfaces

- secret values **must not** appear **in** Atoms, Project Settings, Framework Instance Settings, generated Artifacts, runtime traces, logs, prompts, checkpoints, Evaluation inputs **and** results, Test fixtures **and** snapshots, evidence, support bundles, issues, pull requests, commits, **or** release records.
- secret values **must** be redacted **before** data enters those surfaces. encoding **or** encrypting a secret does **not** permit its inclusion outside the permitted secret storage.

### personal identifiers

email addresses, usernames, **and** account identifiers are identifiers rather than authenticators. they **may** appear **in** CAPRMEDIO **when** necessary **and** authorized, but **must** be minimized **and** treated as potentially personal data. CAPRMEDIO does **not** become the runtime owner merely because a human-readable Artifact names it.

### exposure response

**if** a secret reaches an unauthorized durable **or** shared surface, stop propagation, revoke **or** rotate it immediately, **then** clean affected Carriers **and** record the incident **without** reproducing the value. deleting a current file is **not** sufficient remediation for a value already present **in** durable history **or** another replica.

## Details
