---
atom_id: CA-D-334
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Governed Change/Git Commit Message
  depends_on:
    continuant:
      - Work Journal/Governed File Change Event
version: 2
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Serialize Governed Change Commit Messages

**every** governed file-change Git Commit message **must** be the deterministic one-line Projection `<DIRECT_RELATIONS> | <CHANGE> | <AFFECTED_FILE>` of its canonical Work Journal Event.
