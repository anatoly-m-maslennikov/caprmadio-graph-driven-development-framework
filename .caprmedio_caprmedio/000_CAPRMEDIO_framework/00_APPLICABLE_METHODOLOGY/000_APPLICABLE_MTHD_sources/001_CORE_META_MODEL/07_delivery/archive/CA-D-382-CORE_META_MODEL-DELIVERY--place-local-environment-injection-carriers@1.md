---
atom_id: CA-D-382
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "File Carrier"
  depends_on:
    continuant:
      - "Project"
      - "Project-Owned Carrier Root"
version: 1
updated_at: "2026-09-10 20:54:11 +0400"
relations: {}
---
# Place Local Environment Injection Carriers

for local development, secret values **may** be injected from a repository-local `.env` File Carrier outside **every** applicable Project authority Carrier root. **every** real `.env` variant **must** be ignored by Git **and** excluded from CAPRMEDIO discovery. a tracked `.env.example` **may** contain variable names **and** unmistakable dummy placeholders **only**. mutable runtime configuration identifiers **must** receive their runtime values through the local environment Carrier.
