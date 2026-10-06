---
atom_id: CA-D-267
cce_version: cce_1
cce_form: derivation
subjects:
  governs: "Carrier/Canonical Address"
  depends_on:
    - "Artifact/Property"
    - "Atom/Frontmatter"
version: 7
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive Address Facts without Duplicated Frontmatter

**if** a registered canonical Carrier address completely **and** unambiguously derives an Artifact Property, **then** that address **must** be its sole Carrier encoding **and** frontmatter **must not** duplicate it.
