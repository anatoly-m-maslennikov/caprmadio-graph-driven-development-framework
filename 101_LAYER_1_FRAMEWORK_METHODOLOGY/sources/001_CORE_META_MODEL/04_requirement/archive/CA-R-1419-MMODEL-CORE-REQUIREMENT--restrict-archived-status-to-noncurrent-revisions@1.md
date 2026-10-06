---
atom_id: CA-R-1419
cce_version: cce_1
cce_form: restriction
subjects:
  governs:
    continuant:
      - "Artifact/Revision/Status: Archived"
  depends_on:
    continuant:
      - Artifact/Revision
      - Artifact/Activity
version: 1
updated_at: 2026-09-04 23:45:00 +0400
relations: {}
---
# Restrict Archived Status to Non-Current Revisions

an Artifact Revision **may** have Status Archived **only** **if** it is a prior Revision **or** the final Revision of a replaced, absorbed, **or** retired Artifact.
