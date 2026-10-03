---
cce_version: cce_1
cce_form: restriction
subjects:
  governs: "Artifact/Revision/Status: Archived"
  depends_on:
    - "Artifact/Revision"
    - "Artifact/Activity"
version: 5
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Restrict Archived Status to Non-Current Revisions

an Artifact Revision **may** have Status Archived **only** **if** it is a prior Revision **or** the final Revision of a replaced, absorbed, **or** retired Artifact.
