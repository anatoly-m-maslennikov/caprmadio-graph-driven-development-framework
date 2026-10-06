---
atom_id: CA-D-335
cce_version: cce_1
cce_form: atomicity
subjects:
  governs:
    occurrent:
      - Governed File Change Materialization
  depends_on:
    continuant:
      - Work Journal/Event
      - Git Commit
version: 2
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Mirror Governed File Changes in Journal and Git

**every** governed repository File Carrier change **must** be materialized as one canonical Work Journal file-change Event **and** one Git Commit for the same governed Artifact identity **and** classified change set.
