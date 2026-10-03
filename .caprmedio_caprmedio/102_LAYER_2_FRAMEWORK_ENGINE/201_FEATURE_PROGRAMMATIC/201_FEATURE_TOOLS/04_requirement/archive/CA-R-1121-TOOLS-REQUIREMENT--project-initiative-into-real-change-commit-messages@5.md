---
subjects:
  governs:
    continuant:
      - provenance
cce_version: cce_1
cce_form: obligation
version: 5
updated_at: 2026-08-30 16:44:07 +0400
---
# Project Initiative into real-change commit messages

Every real-change Git commit message MUST begin with the sealed Initiative's concise summary of its human input before the first ` | `. The summary comes from the human-created Plan or Task, or from the human instruction recorded by an ephemeral session task; it MUST NOT be derived from a process, thread, adapter, queue, relation list, or other technical parent. The remaining fields identify the governed change class and affected subject:

```text
<initiative-summary> | <CHANGE_CLASS> | <affected-subject>
```

For an atomic action, `<affected-subject>` is its canonical carrier. For a bulk action, `<CHANGE_CLASS>` is `BULK` and `<affected-subject>` is `target-set:<count>:<sealed-target-set-id>`; the complete ordered target set remains in durable action state and the canonical Journal record. The summary is a deterministic bounded Projection for Git navigation, not the Initiative authority.

Journal-only batch commits use the distinct deterministic form `JOURNAL BATCH | APPEND | <journal-batch-id>` and MUST NOT impersonate a real-change Initiative commit. They identify only the selected Journal batch; the exact action bindings remain in the Journal records and reconciliation state.
