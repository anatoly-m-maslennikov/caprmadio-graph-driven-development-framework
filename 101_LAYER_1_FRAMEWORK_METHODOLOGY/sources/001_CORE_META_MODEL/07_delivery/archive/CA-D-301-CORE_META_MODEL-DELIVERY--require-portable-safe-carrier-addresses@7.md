---
atom_id: CA-D-301
cce_version: cce_1
cce_form: restriction
subjects:
  governs: "Carrier/Canonical Address/Segment"
  depends_on: []
version: 7
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Require Portable-Safe Carrier Addresses

**every** Project-owned Carrier address segment **must** use **only** portable automation-safe ASCII letters, digits, underscores, hyphens, **and** dots, with `@` admitted **only** in the `@<version>` Archive suffix immediately **before** the file extension, as specified by CA-D-289, **must not** contain whitespace, control characters, path separators, shell metacharacters, empty **or** reserved segments, **or** unsafe leading **or** trailing characters, **and** **must** remain sibling-unique under ASCII case folding.
