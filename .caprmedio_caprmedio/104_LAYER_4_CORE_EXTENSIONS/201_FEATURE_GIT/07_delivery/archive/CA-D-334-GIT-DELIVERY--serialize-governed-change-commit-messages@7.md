---
atom_id: CA-D-334
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Governed Change/Git Commit Message"
  depends_on:
    - "Journal"
    - "Action"
    - "Atom/Content Role: Plan"
version: 7
updated_at: "2026-09-14 06:21:07 +0400"
relations: {}
---
# Serialize Governed Change Commit Messages

**every** Git Commit message created by a CAPRMEDIO Tool **must** be the deterministic one-line Projection of exactly one sealed Git-effect action: a real-change action uses `<initiative-summary> | <CHANGE_CLASS> | <affected-subject>`, where the Initiative summary is derived from the governing human Plan, Task, or ephemeral session task; a Journal-only batch uses `JOURNAL BATCH | APPEND | <journal-batch-id>`. A real-change message **must not** use a technical parent in place of the Initiative summary, and neither message class **may** impersonate or be combined with the other.
