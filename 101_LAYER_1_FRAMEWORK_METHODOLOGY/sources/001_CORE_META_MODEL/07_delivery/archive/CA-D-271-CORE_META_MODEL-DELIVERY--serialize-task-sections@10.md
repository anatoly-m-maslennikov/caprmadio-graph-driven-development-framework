---
atom_id: CA-D-271
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Plan/Type: Task/Markdown Atom Carrier"
  depends_on:
    - "Atom/Summary"
    - "Atom/Claim"
    - "Atom/Claim/Scope"
    - "Atom/Content Role: Plan/Type: Task/Definition of Done"
    - "Atom/Content Role: Plan/Type: Task/Details"
version: 10
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Task Sections

**every** Markdown Task Atom Carrier **must** contain, **in** order, one H1 Summary, one CCE Claim, one `Scope` section, one `Definition of Done` section, **and** **`<=1`** `Details` section.
