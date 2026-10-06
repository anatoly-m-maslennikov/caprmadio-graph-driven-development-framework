---
cce_version: cce_1
cce_form: prohibition
subjects:
  - external-boundary
version: 5
updated_at: 2026-08-23 12:02:00
relations:
  child_of:
    - CA-R-1054
---
# Requirement — Exclude secrets from DSET

DSET never stores, transmits, summarizes, or reproduces secret values. Secrets include passwords, API keys, access or refresh tokens, session cookies, private keys, signing or encryption keys, authentication certificates, one-time or recovery codes, and connection strings or URLs containing credentials.

The prohibition covers atomic and evergreen artifacts, settings, generated files, runtime traces, logs, prompts, checkpoints, Evaluation inputs and results, Test fixtures and snapshots, evidence, support bundles, issues, pull requests, commits, and release records. A secret MUST be redacted before any such surface enters DSET; encoding or encrypting a value does not make it ordinary DSET data.

For local development, secret values MAY be injected from a repository-local `.env` file outside `.caprmedio`. Every real `.env` variant is ignored by Git and is excluded from DSET discovery. A tracked `.env.example` MAY contain variable names and unmistakable dummy placeholders only. Production and shared automation use the host's secret injection or a dedicated secret manager, not a committed file or DSET setting.

Email addresses, usernames, and account identifiers are identifiers rather than authenticators. They MAY appear in DSET when necessary and authorized, but MUST be minimized and treated as potentially personal data. When an identifier is mutable runtime configuration, its runtime value is supplied through the local environment carrier as well; DSET does not become the runtime owner merely because a human-readable artifact names it.

If a secret reaches any durable or shared surface, stop propagation, revoke or rotate it immediately, then clean affected carriers and record the incident without reproducing the value. Deleting a current file is not sufficient remediation for a value already present in Git history or another replica.
