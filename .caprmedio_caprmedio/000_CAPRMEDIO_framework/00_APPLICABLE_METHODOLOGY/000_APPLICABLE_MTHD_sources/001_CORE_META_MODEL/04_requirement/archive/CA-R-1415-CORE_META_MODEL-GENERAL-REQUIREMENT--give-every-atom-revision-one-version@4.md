---
atom_id: CA-R-1415
cce_version: cce_1
cce_form: cardinality
subjects:
  governs:
    continuant:
      - "Atom/Revision/Version"
  depends_on:
    continuant:
      - "Atom/Revision"
      - "Atom"
version: 4
updated_at: "2026-09-10 20:53:38 +0400"
relations: {}
---
# Give Every Atom Revision One Version

**every** Atom Revision **must** have **`=1`** positive integer Version that increases monotonically across successive Revisions of the same Atom.
