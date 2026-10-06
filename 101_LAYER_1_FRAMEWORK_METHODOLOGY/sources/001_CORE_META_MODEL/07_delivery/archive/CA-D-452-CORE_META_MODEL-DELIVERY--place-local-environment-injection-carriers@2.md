---
subjects:
  governs: "File Carrier"
  depends_on:
    - "Project"
    - "Project-Owned Carrier Root"
version: 2
updated_at: "2026-09-17 14:04:16 +0000"
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

secret values **may** reach authorized runtime consumers through host injection from a permitted secret store; the injected value is **not** a separate persisted source.
