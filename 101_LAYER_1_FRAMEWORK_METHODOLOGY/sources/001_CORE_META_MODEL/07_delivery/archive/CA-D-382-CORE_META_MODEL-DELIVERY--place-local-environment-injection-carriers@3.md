---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "File Carrier"
  depends_on:
    - "Project"
    - "Project-Owned Carrier Root"
version: 3
updated_at: "2026-09-16 11:59:49 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Place Local Environment Injection Carriers

secret values **must** be stored **only** **in**:

- gitignored `.env` File Carriers; **or**
- a dedicated secret vault.

## file placement

- a repository-local `.env` File Carrier **must** remain outside **every** applicable Project authority Carrier root.
- **every** real `.env` variant **must** be gitignored, untracked, **and** excluded from durable **or** shared Git history **and** CAPRMEDIO discovery. a Git ignore rule does **not** remove a previously tracked secret from history.
- a tracked `.env.example` **may** contain variable names **and** unmistakable dummy placeholders **only**.

## runtime injection

secret values **may** reach authorized runtime consumers through host injection from a permitted secret store; the injected value is **not** a separate persisted source. mutable runtime configuration identifiers **must** receive their runtime values through the local environment Carrier.
