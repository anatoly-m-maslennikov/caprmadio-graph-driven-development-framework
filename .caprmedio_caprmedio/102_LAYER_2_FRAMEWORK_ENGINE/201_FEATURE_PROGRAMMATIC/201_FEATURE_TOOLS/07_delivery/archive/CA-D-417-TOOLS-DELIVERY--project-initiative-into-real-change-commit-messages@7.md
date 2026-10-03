---
subjects:
  governs:
    continuant:
      - provenance
cce_version: cce_1
cce_form: obligation
version: 7
updated_at: "2026-09-11 23:07:09 +0400"
---
# Project Initiative into real-change commit messages

**every** real-change Git commit message **must** begin with the sealed Initiative's concise summary of its human input **before** the first ` | `. the summary comes from the human-created Plan **or** Task, **or** from the human instruction recorded by an ephemeral session task; it **must not** be derived from a process, thread, adapter, queue, relation list, **or** other technical parent. the remaining fields identify the governed change class **and** affected subject:

```text
<initiative-summary> | <CHANGE_CLASS> | <affected-subject>
```

for an atomic action, `<affected-subject>` is its canonical Carrier. for a bulk action, `<CHANGE_CLASS>` is `BULK` **and** `<affected-subject>` is `target-set:<count>:<sealed-target-set-id>`; the complete ordered target set remains **in** durable action state **and** the canonical Journal record. the summary is a deterministic bounded Projection for Git navigation, **not** the Initiative authority.

Journal-only batch commits use the distinct deterministic form `JOURNAL BATCH | APPEND | <journal-batch-id>` **and** **must not** impersonate a real-change Initiative commit. they identify **only** the selected Journal batch; the exact action bindings remain **in** the Journal records **and** reconciliation state.
