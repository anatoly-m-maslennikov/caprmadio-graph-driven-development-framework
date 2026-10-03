---
cce_version: cce_1
cce_form: prohibition
subjects:
  governs: "external-boundary"
version: 14
updated_at: "2026-09-17 14:04:16 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Requirement — Exclude secrets from CAPRMEDIO

secret values **must** remain **in** the permitted secret storage defined by CA-D-452. secrets include passwords, API keys, access **or** refresh tokens, session cookies, private keys, signing **or** encryption keys, authentication certificates, one-time **or** recovery codes, **and** connection strings **or** URLs containing credentials.

## authorized use

- Tools **may** receive secrets from that storage, including through host injection, **and** use them for Operator-authorized authentication.
- credential use **must** remain within the authorized transport **and** resource boundary. permission **to** authenticate does **not** authorize disclosure elsewhere.

## excluded surfaces

- secret values **must not** appear **in** Atoms, Project Settings, Framework Instance Settings, generated Artifacts, runtime traces, logs, prompts, checkpoints, Evaluation inputs **and** results, Test fixtures **and** snapshots, evidence, support bundles, issues, pull requests, commits, **or** release records.
- secret values **must** be redacted **before** data enters those surfaces. encoding **or** encrypting a secret does **not** permit its inclusion outside the permitted secret storage.

## personal identifiers

email addresses, usernames, **and** account identifiers are identifiers rather than authenticators. they **may** appear **in** CAPRMEDIO **when** necessary **and** authorized, but **must** be minimized **and** treated as potentially personal data. CAPRMEDIO does **not** become the runtime owner merely because a human-readable Artifact names it.

## exposure response

**if** a secret reaches an unauthorized durable **or** shared surface, stop propagation, revoke **or** rotate it immediately, **then** clean affected Carriers **and** record the incident **without** reproducing the value. deleting a current file is **not** sufficient remediation for a value already present **in** durable history **or** another replica.
