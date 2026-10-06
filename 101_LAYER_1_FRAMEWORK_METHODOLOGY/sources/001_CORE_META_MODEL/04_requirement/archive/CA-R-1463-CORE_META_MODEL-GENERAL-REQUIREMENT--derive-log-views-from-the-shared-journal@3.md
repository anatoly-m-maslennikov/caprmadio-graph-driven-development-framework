---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Projection"
  depends_on:
    - "Journal"
    - "Journal/Record"
    - "Work Journal/Event"
    - "Artifact"
    - "Action"
    - "Process"
    - "Project"
    - "Projection/Type: Artifact Change Log"
    - "Projection/Type: Process Log"
version: 3
updated_at: "2026-09-14 06:21:07 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive log views from the shared Journal

the Core Meta-Model **must** provide Artifact Change Log **and** Process Log as **`=2`** log Projection Types derived from the same Project Journal, under CA-R-1467 **and** CA-R-1468. these Types organize recorded history **without** introducing independent Journals; additional Projection Types remain governed by the open Projection model.

**every** represented historical fact **must** remain traceable **to** its canonical source event record **and** Event identity. the same source event **may** appear **in** both views **without** becoming two authoritative records. a read-only execution requires no fictitious Artifact change; membership **and** execution associations **must** come from recorded source evidence rather than invented events **or** inferred success. a view **must** remain rebuildable from its declared Journal selection, disclose known incomplete **or** stale source coverage **without** claiming complete current history, **and** obtain corrections through the owning source authority rather than independent log edits.
