---
atom_id: CA-D-271
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Type: Task/Markdown Carrier"
  depends_on:
    continuant:
      - Atom/Summary
      - Atom/Claim
      - "Atom/Content Role: Plan/Type: Task/Scope"
      - "Atom/Content Role: Plan/Type: Task/Definition of Done"
      - "Atom/Content Role: Plan/Type: Task/Details"
version: 4
updated_at: 2026-08-29 04:33:13 +0400
relations: {}
---
# Serialize Task Sections

**every** Markdown Task Atom Carrier **must** contain, **in** order, one H1 Summary, one CCE Claim, one `Scope` section, one `Definition of Done` section, **and** **`<=1`** `Details` section.
