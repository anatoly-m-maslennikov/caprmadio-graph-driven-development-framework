---
atom_id: CA-R-1463
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Projection"
  depends_on:
    - "Journal"
    - "Journal/Record"
    - "Work Journal/Event"
    - "Artifact"
    - "Process"
    - "Project"
version: 1
updated_at: "2026-09-14 01:17:47 +0400"
relations: {}
---
# Derive log views from the shared Journal

artifact-change **and** Process-execution logs **must** be non-authoritative Projections derived from the same Project Journal: the artifact-change view selects recorded changes **to** Artifacts, **and** the Process-execution view organizes recorded events by their identified execution. these are distinct views of recorded history, **not** independently authored Journals **or** newly admitted Projection Types.

**every** represented historical fact **must** remain traceable **to** its canonical source event record **and** Event identity. the same source event **may** appear **in** both views **without** becoming two authoritative records. a read-only execution requires no fictitious Artifact change; membership **and** execution associations **must** come from recorded source evidence rather than invented events **or** inferred success. a view **must** remain rebuildable from its declared Journal selection, disclose known incomplete **or** stale source coverage **without** claiming complete current history, **and** obtain corrections through the owning source authority rather than independent log edits.
