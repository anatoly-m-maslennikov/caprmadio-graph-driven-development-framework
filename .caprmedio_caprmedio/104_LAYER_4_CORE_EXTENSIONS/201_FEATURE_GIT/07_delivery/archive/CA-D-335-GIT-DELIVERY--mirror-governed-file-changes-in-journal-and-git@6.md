---
atom_id: CA-D-335
cce_version: cce_1
cce_form: atomicity
subjects:
  governs: "Governed File Change Materialization"
  depends_on:
    - "Journal/Record"
    - "Git Commit"
    - "Carrier"
version: 6
updated_at: "2026-09-14 06:21:07 +0400"
relations: {}
---
# Mirror Governed File Changes in Journal and Git

**when** the Git Extension is selected, **every** governed repository File Carrier change **must** be materialized as **`=1`** canonical Journal file-change Event **and** **`=1`** corresponding Git Commit for the same governed Artifact identity **and** classified change set. **every** successor **and** predecessor Carrier change remains a separate one-file Git Commit. a commit records the persisted change **without** becoming another authoritative Journal **or** independently recording the same historical fact.
