---
atom_id: CA-R-1462
cce_version: cce_1
cce_form: classification
subjects:
  governs: "Atom/Content Role: Operations/Type"
  depends_on:
    - "Atom/Content Role: Operations"
    - "Type"
    - "Action"
    - "Process"
    - "Atom/Claim"
version: 2
updated_at: 2026-09-15 05:51:38
relations: {}
---
# Admit Action and Process Types for Operations Atoms

Action **and** Process **must** be admitted internal Type values under `Atom/Content Role: Operations/Type`. Action classifies an Operations Atom whose Claim defines reusable Action behavior; Process classifies an Operations Atom whose Claim defines reusable Process behavior, including a context-specific binding of a reused flow. these values classify definition Atoms, **not** their governed Actions **or** Processes, particular executions, **or** execution records; the Atom **and** its governed target retain distinct identities. this admission adds the two values **without** closing the qualified Type domain **or** changing other admitted values.
