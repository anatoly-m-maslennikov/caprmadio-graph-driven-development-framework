---
atom_id: CA-D-271
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Plan Type: Task/Markdown Carrier"
  depends_on:
    continuant:
      - Atom/Summary
      - Atom/Claim
      - Task/Scope
      - Task/Definition of Done
      - Task/Details
version: 2
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Serialize Task Sections

**every** Markdown Task Atom Carrier **must** contain, **in** order, one H1 Summary, one CCE Claim, one `Scope` section, one `Definition of Done` section, **and** **`<=1`** `Details` section.
