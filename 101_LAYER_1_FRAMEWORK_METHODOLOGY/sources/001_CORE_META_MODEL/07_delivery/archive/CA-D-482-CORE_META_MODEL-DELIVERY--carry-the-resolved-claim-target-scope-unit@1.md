---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Claim/Target Scope Unit/Carrier"
  depends_on:
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Scope"
    - "Current-scope Atom"
    - "Relational Atom"
version: 1
updated_at: "2026-09-22 23:02:20 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1595", "CA-R-1596", "CA-R-922", "CA-R-923", "CA-D-478"]}
---
# Summary

Carry the resolved Claim Target Scope Unit

## Claim

a Markdown Atom Carrier **must** carry its resolved Claim Target Scope Unit **in** frontmatter, including a Current-scope Atom whose target is its own Scope Unit.

- choose the current Scope Unit as the default during authoring, **not** by relying on the file's later location.
- a carried target equal **to** the current Scope Unit does **not** make the Atom Relational. a different target still requires the applicable Relational Atom admission.
- Claim Scope restrictions remain part of the Claim text under CA-D-477.
