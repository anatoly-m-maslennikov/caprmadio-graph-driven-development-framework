---
cce_version: cce_1
cce_form: resolution
subjects:
  governs: "Active Atom Carrier Discovery"
  depends_on:
    - "Atom/Identity"
    - "Carrier/Canonical Address"
version: 9
updated_at: "2026-09-22 23:02:20 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Resolve Active Atoms from Canonical Carrier Identities

## Claim

Active Atom Carrier discovery **must** resolve requested Atom IDs from the identities carried inside the selected Project-owned Markdown source frontier **and** select carried Status Active.

- validate the associated canonical addresses against those internal values under CA-D-480.
- report zero **or** multiple Active matches **and** missing **or** conflicting identity **or** Status; do **not** repair discovery by silently preferring a filename **or** directory.
- a non-Active containing Hub does **not** change the Status of a nested Atom.
