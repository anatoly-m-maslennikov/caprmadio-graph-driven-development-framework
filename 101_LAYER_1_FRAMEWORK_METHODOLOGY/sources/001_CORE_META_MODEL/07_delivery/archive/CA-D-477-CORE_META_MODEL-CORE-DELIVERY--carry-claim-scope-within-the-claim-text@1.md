---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Claim/Carrier"
  depends_on:
    - "Atom/Claim"
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Carrier"
version: 1
updated_at: "2026-09-22 17:59:17 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1271", "CA-D-476"]}
---
# Carry Claim Scope within the Claim text

a Markdown Atom Carrier **must** carry **any** Claim Scope as applicability restrictions within the Claim text after frontmatter, **not** as a separate frontmatter Property **or** independently maintained scope declaration.
